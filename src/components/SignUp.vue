<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { signup } from '../api.js'

const router = useRouter()
const fullName = ref('')
const email = ref('')
const password = ref('')
const showSuccessMessage = ref(false)
const errorMsg = ref('')
const loading = ref(false)

const handleSignUp = async () => {
  if (!fullName.value || !email.value || !password.value) {
    errorMsg.value = 'Please fill in all fields!'
    return
  }
  loading.value = true
  errorMsg.value = ''
  try {
    await signup(fullName.value, email.value, password.value)
    showSuccessMessage.value = true
    setTimeout(() => {
      router.push('/login')
    }, 2000)
  } catch (err) {
    errorMsg.value = err.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="auth-page">
    <div class="glass-container">
      <div class="brand-section">
        <div class="logo-container">
          <div class="logo-box">⬡</div>
          <span class="logo-text">Pamplona</span>
        </div>
        <h1 class="tagline">Data Profiling</h1>
        <div class="tagline-sub">Sign up to create your account for Pamplona Data Profiling records</div>
      </div>

      <div class="form-section">
        <div class="form-card">
          <div class="tabs">
            <router-link to="/login" class="tab" active-class="active">LOGIN</router-link>
            <router-link to="/signup" class="tab" active-class="active">SIGN UP</router-link>
          </div>

          <div v-if="showSuccessMessage" class="success-notification">
            <div class="success-icon">✔</div>
            <h3>Account Created!</h3>
            <p>Welcome, {{ fullName }}. Redirecting you to login...</p>
          </div>

          <form v-else @submit.prevent="handleSignUp" class="auth-form">
            <div class="input-group">
              <label>Full Name</label>
              <input v-model="fullName" type="text" placeholder="Enter your full name" required />
            </div>

            <div class="input-group">
              <label>Email</label>
              <input v-model="email" type="email" placeholder="Enter your email" required />
            </div>

            <div class="input-group">
              <label>Password</label>
              <input v-model="password" type="password" placeholder="Create a password" required />
            </div>

            <div v-if="errorMsg" class="error-msg">{{ errorMsg }}</div>

            <button type="submit" class="submit-btn" :disabled="loading">
              {{ loading ? 'Creating account...' : 'Create Account →' }}
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.auth-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #042f24 0%, #064e3b 50%, #022c22 100%);
  padding: 20px;
}

.glass-container {
  display: flex;
  width: 100%;
  max-width: 1000px;
  background: rgba(255, 255, 255, 0.04);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(16, 185, 129, 0.25);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 25px 60px -12px rgba(0, 0, 0, 0.6), 0 0 40px rgba(16, 185, 129, 0.08);
}

.brand-section {
  flex: 1;
  padding: 60px;
  color: white;
  display: flex;
  flex-direction: column;
  background: rgba(16, 185, 129, 0.06);
  border-right: 1px solid rgba(16, 185, 129, 0.15);
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 30px;
}

.logo-box {
  width: 45px;
  height: 45px;
  background: linear-gradient(135deg, #10b981, #059669);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
}

.logo-text {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -0.5px;
  background: linear-gradient(135deg, #fff 0%, #a7f3d0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tagline {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 15px;
  line-height: 1.4;
  color: #e8f5e9;
}

.tagline-sub {
  font-size: 16px;
  opacity: 0.8;
  color: #c7d1cc;
  line-height: 1.4;
}

.form-section {
  flex: 1.1;
  padding: 20px;
  display: flex;
}

.form-card {
  background: #061f17;
  width: 100%;
  border-radius: 20px;
  padding: 40px;
  box-sizing: border-box;
  border: 1px solid rgba(16, 185, 129, 0.15);
}

.tabs {
  display: flex;
  background: #0a291f;
  border-radius: 12px;
  padding: 6px;
  margin-bottom: 30px;
}

.tab {
  flex: 1;
  padding: 12px;
  text-decoration: none;
  text-align: center;
  border-radius: 10px;
  font-weight: 700;
  font-size: 13px;
  letter-spacing: 0.05em;
  color: #4b635a;
  transition: all 0.3s ease;
}

.tab.active {
  background: #10b981;
  color: white;
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4);
}

.auth-form {
  text-align: left;
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  font-size: 12px;
  font-weight: 700;
  color: #8da199;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.input-group input {
  width: 100%;
  padding: 14px;
  background: #0a291f;
  border: 1px solid #1a3d32;
  border-radius: 12px;
  font-size: 14px;
  color: #e8f5e9;
  box-sizing: border-box;
  transition: border-color 0.2s;
  outline: none;
}

.input-group input::placeholder {
  color: #3b5249;
}

.input-group input:focus {
  border-color: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
}

.error-msg {
  background: rgba(220, 38, 38, 0.15);
  border: 1px solid rgba(220, 38, 38, 0.4);
  color: #f87171;
  padding: 10px 14px;
  border-radius: 10px;
  font-size: 13px;
  margin-bottom: 16px;
}

.submit-btn {
  width: 100%;
  padding: 15px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 700;
  font-size: 15px;
  cursor: pointer;
  letter-spacing: 0.03em;
  transition: all 0.2s;
  box-shadow: 0 4px 20px rgba(16, 185, 129, 0.35);
}

.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(16, 185, 129, 0.5);
}

.success-notification {
  text-align: center;
  padding: 20px;
  animation: fadeIn 0.4s ease-out;
  color: #e8f5e9;
}

.success-notification h3 {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
  color: #e8f5e9;
}

.success-notification p {
  font-size: 14px;
  color: #8da199;
}

.success-icon {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #3dffa0, #1a7a4a);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  margin: 0 auto 20px;
  box-shadow: 0 0 20px rgba(61, 255, 160, 0.3);
}

@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}
</style>