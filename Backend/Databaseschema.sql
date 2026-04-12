-- DATA PROFILING: HOUSEHOLD & HEALTH PROFILE
-- Database Schema
-- Users table (for login/signup)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Households table
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

-- Residents table
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