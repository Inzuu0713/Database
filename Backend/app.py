from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import hashlib
import os

app = Flask(__name__)
CORS(app)

DB_PATH = os.path.join(os.path.dirname(__file__), 'Database.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS households (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            zone TEXT NOT NULL,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            no_of_families INTEGER DEFAULT 1,
            no_of_members INTEGER DEFAULT 0,
            basic_water TEXT DEFAULT 'No',
            safe_water TEXT DEFAULT 'No',
            sanitation TEXT DEFAULT 'No',
            safe_sanitation TEXT DEFAULT 'No',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS residents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            household_id INTEGER NOT NULL,
            full_name TEXT NOT NULL,
            birthday TEXT,
            age INTEGER,
            sex TEXT,
            relation_to_head TEXT,
            occupation TEXT,
            monthly_income REAL DEFAULT 0,
            education TEXT,
            philhealth_number TEXT,
            philhealth_category TEXT,
            four_ps TEXT DEFAULT 'No',
            disability TEXT DEFAULT 'None',
            medical_history TEXT,
            health_risk TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (household_id) REFERENCES households(id) ON DELETE CASCADE
        );
    """)

    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    full_name = data.get('fullName', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not full_name or not email or not password:
        return jsonify({'error': 'All fields are required.'}), 400

    conn = get_db()
    try:
        conn.execute(
            'INSERT INTO users (full_name, email, password) VALUES (?, ?, ?)',
            (full_name, email, hash_password(password))
        )
        conn.commit()
        return jsonify({'message': 'Account created successfully.'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists.'}), 409
    finally:
        conn.close()


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    conn = get_db()
    user = conn.execute(
        'SELECT * FROM users WHERE email = ? AND password = ?',
        (email, hash_password(password))
    ).fetchone()
    conn.close()

    if user:
        return jsonify({
            'message': 'Login successful.',
            'user': {
                'id': user['id'],
                'fullName': user['full_name'],
                'email': user['email']
            }
        }), 200
    else:
        return jsonify({'error': 'Invalid email or password.'}), 401


# ✅ NEW ROUTE: Update user's display name
@app.route('/api/user/name', methods=['PUT'])
def update_user_name():
    data = request.get_json()
    email = data.get('email', '').strip().lower()
    full_name = data.get('fullName', '').strip()

    if not email or not full_name:
        return jsonify({'error': 'Email and name are required.'}), 400

    conn = get_db()
    result = conn.execute(
        'UPDATE users SET full_name = ? WHERE email = ?',
        (full_name, email)
    )
    conn.commit()
    conn.close()

    if result.rowcount == 0:
        return jsonify({'error': 'User not found.'}), 404

    return jsonify({'message': 'Name updated successfully.', 'fullName': full_name}), 200


@app.route('/api/households', methods=['GET'])
def get_households():
    conn = get_db()
    households = conn.execute('SELECT * FROM households ORDER BY created_at DESC').fetchall()

    result = []
    for h in households:
        residents = conn.execute(
            'SELECT * FROM residents WHERE household_id = ?', (h['id'],)
        ).fetchall()

        children = sum(1 for r in residents if r['age'] is not None and int(r['age']) < 18)
        seniors = sum(1 for r in residents if r['age'] is not None and int(r['age']) >= 60)
        pwd = sum(1 for r in residents if r['disability'] and r['disability'].lower() != 'none' and r['disability'] != '')

        result.append({
            'id': h['id'],
            'zone': h['zone'],
            'headName': f"{h['last_name']}, {h['first_name']}" + (f", {h['middle_name']}" if h['middle_name'] else ''),
            'lastName': h['last_name'],
            'firstName': h['first_name'],
            'middleName': h['middle_name'],
            'families': h['no_of_families'],
            'members': h['no_of_members'],
            'basicWater': h['basic_water'],
            'safeWater': h['safe_water'],
            'sanitation': h['sanitation'],
            'safeSanitation': h['safe_sanitation'],
            'waterStatus': 'Safe' if h['safe_water'] == 'Yes' else 'Basic',
            'children': children,
            'seniors': seniors,
            'pwd': pwd,
            'residents': [dict(r) for r in residents]
        })

    conn.close()
    return jsonify(result), 200


@app.route('/api/households', methods=['POST'])
def add_household():
    data = request.get_json()
    residents_data = data.get('residents', [])

    conn = get_db()
    cursor = conn.execute(
        '''INSERT INTO households
           (zone, last_name, first_name, middle_name, no_of_families, no_of_members,
            basic_water, safe_water, sanitation, safe_sanitation)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (
            data.get('zone', ''),
            data.get('lastName', ''),
            data.get('firstName', ''),
            data.get('middleName', ''),
            int(data.get('families', 1)),
            int(data.get('membersCount', 0)),
            data.get('basicWater', 'No'),
            data.get('safeWater', 'No'),
            data.get('sanitation', 'No'),
            data.get('safeSanitation', 'No'),
        )
    )
    household_id = cursor.lastrowid

    for r in residents_data:
        conn.execute(
            '''INSERT INTO residents
               (household_id, full_name, birthday, age, sex, relation_to_head,
                occupation, monthly_income, education, philhealth_number,
                philhealth_category, four_ps, disability, medical_history, health_risk)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (
                household_id,
                r.get('fullName', ''),
                r.get('birthday', ''),
                int(r['age']) if r.get('age') else None,
                r.get('sex', ''),
                r.get('relation', ''),
                r.get('occupation', ''),
                float(r['income']) if r.get('income') else 0,
                r.get('education', ''),
                r.get('philhealth', ''),
                r.get('philhealthCategory', ''),
                r.get('fourPs', 'No'),
                r.get('disability', 'None'),
                r.get('medicalHistory', ''),
                r.get('healthRisk', ''),
            )
        )

    conn.commit()
    conn.close()
    return jsonify({'message': 'Household added successfully.', 'id': household_id}), 201


@app.route('/api/households/<int:household_id>', methods=['PUT'])
def update_household(household_id):
    data = request.get_json()
    residents_data = data.get('residents', [])

    conn = get_db()
    conn.execute(
        '''UPDATE households SET
           zone=?, last_name=?, first_name=?, middle_name=?,
           no_of_families=?, no_of_members=?,
           basic_water=?, safe_water=?, sanitation=?, safe_sanitation=?,
           updated_at=CURRENT_TIMESTAMP
           WHERE id=?''',
        (
            data.get('zone', ''),
            data.get('lastName', ''),
            data.get('firstName', ''),
            data.get('middleName', ''),
            int(data.get('families', 1)),
            int(data.get('membersCount', 0)),
            data.get('basicWater', 'No'),
            data.get('safeWater', 'No'),
            data.get('sanitation', 'No'),
            data.get('safeSanitation', 'No'),
            household_id
        )
    )

    conn.execute('DELETE FROM residents WHERE household_id = ?', (household_id,))
    for r in residents_data:
        conn.execute(
            '''INSERT INTO residents
               (household_id, full_name, birthday, age, sex, relation_to_head,
                occupation, monthly_income, education, philhealth_number,
                philhealth_category, four_ps, disability, medical_history, health_risk)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (
                household_id,
                r.get('fullName', ''),
                r.get('birthday', ''),
                int(r['age']) if r.get('age') else None,
                r.get('sex', ''),
                r.get('relation', ''),
                r.get('occupation', ''),
                float(r['income']) if r.get('income') else 0,
                r.get('education', ''),
                r.get('philhealth', ''),
                r.get('philhealthCategory', ''),
                r.get('fourPs', 'No'),
                r.get('disability', 'None'),
                r.get('medicalHistory', ''),
                r.get('healthRisk', ''),
            )
        )

    conn.commit()
    conn.close()
    return jsonify({'message': 'Household updated successfully.'}), 200


@app.route('/api/households/<int:household_id>', methods=['DELETE'])
def delete_household(household_id):
    conn = get_db()
    conn.execute('DELETE FROM households WHERE id = ?', (household_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Household deleted successfully.'}), 200

@app.route('/api/stats', methods=['GET'])
def get_stats():
    conn = get_db()

    total_households = conn.execute('SELECT COUNT(*) FROM households').fetchone()[0]
    total_residents = conn.execute('SELECT COUNT(*) FROM residents').fetchone()[0]
    children = conn.execute('SELECT COUNT(*) FROM residents WHERE age < 18').fetchone()[0]
    seniors = conn.execute('SELECT COUNT(*) FROM residents WHERE age >= 60').fetchone()[0]
    pwd = conn.execute(
        "SELECT COUNT(*) FROM residents WHERE disability IS NOT NULL AND disability != 'None' AND disability != ''"
    ).fetchone()[0]

    conn.close()
    return jsonify({
        'households': total_households,
        'residents': total_residents,
        'children': children,
        'seniors': seniors,
        'pwd': pwd
    }), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)