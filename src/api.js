const BASE_URL = 'http://localhost:5000/api'

export async function login(email, password) {
  const res = await fetch(`${BASE_URL}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Login failed')
  return data
}

export async function signup(fullName, email, password) {
  const res = await fetch(`${BASE_URL}/signup`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ fullName, email, password })
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Signup failed')
  return data
}

export async function getStats() {
  const res = await fetch(`${BASE_URL}/stats`)
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Failed to fetch stats')
  return data
}

export async function getHouseholds() {
  const res = await fetch(`${BASE_URL}/households`)
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Failed to fetch households')
  return data
}

export async function addHousehold(payload) {
  const res = await fetch(`${BASE_URL}/households`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Failed to add household')
  return data
}

export async function updateHousehold(id, payload) {
  const res = await fetch(`${BASE_URL}/households/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Failed to update household')
  return data
}

export async function deleteHousehold(id) {
  const res = await fetch(`${BASE_URL}/households/${id}`, {
    method: 'DELETE'
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Failed to delete household')
  return data
}