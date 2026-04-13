<template>
  <div class="hhp-app">
    <aside class="sidebar">
      <div class="sidebar-logo">
        <span class="logo-text">HHP</span>
      </div>
      <nav class="sidebar-nav">
        <button class="nav-item" :class="{ active: currentPage === 'dashboard' }" @click="currentPage = 'dashboard'">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
          <span>Dashboard</span>
        </button>
        <button class="nav-item" :class="{ active: currentPage === 'households' || currentPage === 'household-detail' }" @click="currentPage = 'households'; selectedHousehold = null">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          <span>Households</span>
        </button>
        <button class="nav-item" :class="{ active: currentPage === 'reports' }" @click="currentPage = 'reports'">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          <span>Reports</span>
        </button>
      </nav>
    </aside>

    <main class="main-content">
      <header class="topbar">
        <h1 class="page-title">
          <template v-if="currentPage === 'dashboard'">Data Profiling Household and Health Profile</template>
          <template v-else-if="currentPage === 'households'">Households</template>
          <template v-else-if="currentPage === 'household-detail'">Household Details</template>
          <template v-else-if="currentPage === 'reports'">Reports</template>
        </h1>
        <div class="topbar-right">
          <div class="search-box">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <input type="text" placeholder="Search households or members..." />
          </div>
          <!-- USER BADGE WITH DROPDOWN -->
          <div class="user-badge" @click="toggleUserMenu" ref="userBadge">
            <span class="user-avatar">{{ userInitials }}</span>
            <span class="user-name">{{ userName }}</span>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
            <!-- DROPDOWN MENU -->
            <div v-if="showUserMenu" class="user-dropdown" @click.stop>
              <div class="user-dropdown-header">
                <span class="user-avatar-lg">{{ userInitials }}</span>
                <div>
                  <div class="user-dropdown-name">{{ userName }}</div>
                  <div class="user-dropdown-email">{{ userEmail }}</div>
                </div>
              </div>
              <div class="user-dropdown-divider"></div>
              <!-- SETTINGS -->
              <div v-if="!showEditName" class="user-dropdown-item" @click="showEditName = true; editNameValue = userName">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
                Settings
              </div>
              <!-- EDIT NAME FORM -->
              <div v-if="showEditName" class="user-dropdown-edit">
                <label>Display Name</label>
                <input type="text" v-model="editNameValue" class="user-edit-input" placeholder="Enter your name" />
                <div class="user-edit-actions">
                  <button class="btn-edit-cancel" @click="showEditName = false">Cancel</button>
                  <button class="btn-edit-save" @click="saveName" :disabled="savingName">
                    {{ savingName ? 'Saving...' : 'Save' }}
                  </button>
                </div>
              </div>
              <div class="user-dropdown-divider"></div>
              <!-- LOGOUT -->
              <div class="user-dropdown-item user-dropdown-logout" @click="logout">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
                Logout
              </div>
            </div>
          </div>
        </div>
      </header>

      <!-- DASHBOARD PAGE -->
      <div v-if="currentPage === 'dashboard'" class="page-content">
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9.5L12 3l9 6.5V20a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9.5z"/><polyline points="9 21 9 12 15 12 15 21"/></svg></div>
            <div class="stat-label">Total Households</div>
            <div class="stat-value">{{ stats.households }}</div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
            <div class="stat-label">Total Residents</div>
            <div class="stat-value">{{ stats.residents }}</div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M3 21a9 9 0 0 1 18 0"/></svg></div>
            <div class="stat-label">Children</div>
            <div class="stat-value">{{ stats.children }}</div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>
            <div class="stat-label">Senior Citizens</div>
            <div class="stat-value">{{ stats.seniors }}</div>
          </div>
          <div class="stat-card">
            <div class="stat-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="5" r="2"/><path d="M11 7v6l3 3"/><path d="M5 21c0-3.5 3-6 6-6"/><path d="M17 21a4 4 0 0 0-4-4"/></svg></div>
            <div class="stat-label">Persons with Disability</div>
            <div class="stat-value">{{ stats.pwd }}</div>
          </div>
        </div>

        <div class="table-section">
          <div class="table-toolbar">
            <div class="search-box">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input type="text" v-model="householdSearch" placeholder="Search Household..." />
            </div>
            <button class="btn-primary" @click="openAddModal">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Add Household
            </button>
          </div>
          <div v-if="loadingHouseholds" class="loading-state">Loading households...</div>
          <table v-else class="data-table">
            <thead>
              <tr>
                <th>Zone</th>
                <th>Head Name</th>
                <th>Members</th>
                <th>Children</th>
                <th>Water Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="filteredHouseholds.length === 0">
                <td colspan="6" style="text-align: center; color: #8aab99; padding: 32px;">No households found.</td>
              </tr>
              <tr v-for="h in filteredHouseholds" :key="h.id">
                <td>{{ h.zone }}</td>
                <td>{{ h.headName }}</td>
                <td>{{ h.members }}</td>
                <td>{{ h.children }}</td>
                <td><span class="badge" :class="h.waterStatus === 'Safe' ? 'badge-safe' : 'badge-basic'">{{ h.waterStatus }}</span></td>
                <td>
                  <div class="action-btn-wrap">
                    <button class="btn-view" @click="viewHousehold(h)">View <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- HOUSEHOLDS PAGE -->
      <div v-else-if="currentPage === 'households'" class="page-content">
        <div class="table-section">
          <div class="table-toolbar">
            <div class="search-box">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input type="text" v-model="householdSearch" placeholder="Search Household..." />
            </div>
            <button class="btn-primary" @click="openAddModal">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Add Household
            </button>
          </div>
          <div v-if="loadingHouseholds" class="loading-state">Loading households...</div>
          <table v-else class="data-table">
            <thead>
              <tr>
                <th>Zone</th>
                <th>Head Name</th>
                <th>Members</th>
                <th>Children</th>
                <th>Water Status</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="filteredHouseholds.length === 0">
                <td colspan="6" style="text-align: center; color: #8aab99; padding: 32px;">No households found.</td>
              </tr>
              <tr v-for="h in filteredHouseholds" :key="h.id">
                <td>{{ h.zone }}</td>
                <td>{{ h.headName }}</td>
                <td>{{ h.members }}</td>
                <td>{{ h.children }}</td>
                <td><span class="badge" :class="h.waterStatus === 'Safe' ? 'badge-safe' : 'badge-basic'">{{ h.waterStatus }}</span></td>
                <td>
                  <div class="action-btn-wrap">
                    <button class="btn-view" @click="viewHousehold(h)">View <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg></button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- HOUSEHOLD DETAIL PAGE -->
      <div v-else-if="currentPage === 'household-detail' && selectedHousehold" class="page-content">
        <div class="detail-back" @click="currentPage = 'households'; selectedHousehold = null">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
          Back to Household List
        </div>
        <div class="detail-header">
          <div>
            <h2 class="detail-title">Household Details</h2>
            <p class="detail-sub">View, edit, and manage household information</p>
          </div>
          <div class="detail-actions">
            <button class="btn-primary" @click="openEditModal">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
              Edit Household
            </button>
            <button class="btn-danger" @click="deleteHousehold">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/></svg>
              Delete Household
            </button>
          </div>
        </div>

        <div class="detail-card">
          <h3 class="section-title-sm">HOUSEHOLD INFORMATION</h3>
          <div class="detail-field">
            <label>Zone No.</label>
            <div class="detail-value">{{ selectedHousehold.zone }}</div>
          </div>
          <div class="detail-field">
            <label>Household Head</label>
            <div class="detail-value">{{ selectedHousehold.headName }}</div>
          </div>
          <div class="detail-row-2">
            <div class="detail-field">
              <label>No. of Families</label>
              <div class="detail-value">{{ selectedHousehold.families }}</div>
            </div>
            <div class="detail-field">
              <label>No. of Household Members</label>
              <div class="detail-value">{{ selectedHousehold.members }}</div>
            </div>
          </div>
        </div>

        <div class="detail-card" style="margin-top: 20px;">
          <h3 class="section-title-sm">RESIDENTS</h3>
          <table class="data-table">
            <thead>
              <tr>
                <th>Full Name</th>
                <th>Birthday</th>
                <th>Age</th>
                <th>Sex</th>
                <th>Relation to Head</th>
                <th>Occupation</th>
                <th>Monthly Income</th>
                <th>Education</th>
                <th>PhilHealth</th>
                <th>4Ps</th>
                <th>Disability</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="!selectedHousehold.residents || selectedHousehold.residents.length === 0">
                <td colspan="11" style="text-align: center; color: #8aab99; padding: 32px;">No residents added yet.</td>
              </tr>
              <tr v-for="r in selectedHousehold.residents" :key="r.id">
                <td>{{ r.full_name }}</td>
                <td>{{ r.birthday }}</td>
                <td>{{ r.age }}</td>
                <td>{{ r.sex }}</td>
                <td>{{ r.relation_to_head }}</td>
                <td>{{ r.occupation }}</td>
                <td>{{ r.monthly_income ? '₱' + r.monthly_income : '—' }}</td>
                <td>{{ r.education }}</td>
                <td>{{ r.philhealth_number }}</td>
                <td><span class="badge" :class="r.four_ps === 'Yes' ? 'badge-safe' : 'badge-no'">{{ r.four_ps }}</span></td>
                <td>{{ r.disability }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- REPORTS PAGE -->
      <div v-else-if="currentPage === 'reports'" class="page-content">
        <div class="empty-state">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          <p>Reports feature coming soon.</p>
        </div>
      </div>
    </main>

    <!-- TOAST NOTIFICATION -->
    <div v-if="toast.show" class="toast" :class="'toast-' + toast.type">
      <svg v-if="toast.type === 'success'" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
      <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
      {{ toast.message }}
    </div>

    <!-- MODAL -->
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <div class="modal-title">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
            {{ modalMode === 'add' ? 'Add Household & Residents' : 'Edit Household & Residents' }}
          </div>
          <button class="modal-close" @click="closeModal">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
        </div>
        <div class="modal-body">
          <div class="modal-section-header">HOUSEHOLD INFORMATION</div>
          <div class="form-group">
            <label>Zone No.</label>
            <input type="text" v-model="form.zone" class="form-input" />
          </div>
          <div class="form-group">
            <label>Household Head</label>
            <div class="form-row-3">
              <input type="text" v-model="form.lastName" placeholder="Last Name" class="form-input" />
              <input type="text" v-model="form.firstName" placeholder="First Name" class="form-input" />
              <input type="text" v-model="form.middleName" placeholder="Middle Name" class="form-input" />
            </div>
          </div>
          <div class="form-row-2">
            <div class="form-group">
              <label>No. of Families</label>
              <input type="number" v-model="form.families" class="form-input" />
            </div>
            <div class="form-group">
              <label>No. of Household Members</label>
              <input type="number" v-model="form.membersCount" class="form-input" />
            </div>
          </div>

          <div class="modal-section-header">WATER &amp; SANITATION</div>
          <div class="form-row-2">
            <div class="form-group">
              <label>Basic Safe Water Source</label>
              <select v-model="form.basicWater" class="form-input">
                <option value="">Select</option>
                <option>Yes</option><option>No</option>
              </select>
            </div>
            <div class="form-group">
              <label>Safely Managed Water</label>
              <select v-model="form.safeWater" class="form-input">
                <option value="">Select</option>
                <option>Yes</option><option>No</option>
              </select>
            </div>
          </div>
          <div class="form-row-2">
            <div class="form-group">
              <label>Sanitation Service</label>
              <select v-model="form.sanitation" class="form-input">
                <option value="">Select</option>
                <option>Yes</option><option>No</option>
              </select>
            </div>
            <div class="form-group">
              <label>Safely Managed Sanitation</label>
              <select v-model="form.safeSanitation" class="form-input">
                <option value="">Select</option>
                <option>Yes</option><option>No</option>
              </select>
            </div>
          </div>

          <div class="modal-section-header">RESIDENT INFORMATION</div>
          <div v-for="(resident, idx) in form.residents" :key="idx" class="resident-card">
            <div class="resident-card-header">
              <div class="resident-card-title">Resident {{ idx + 1 }}</div>
              <button
                class="btn-remove-resident"
                @click="removeResident(idx)"
                v-if="form.residents.length > 1"
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                Remove
              </button>
            </div>
            <div class="form-group">
              <label>Full Name</label>
              <input type="text" v-model="resident.fullName" placeholder="Dela Cruz, Juan, Santos" class="form-input" />
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label>Birthday</label>
                <input type="date" v-model="resident.birthday" class="form-input" />
              </div>
              <div class="form-group">
                <label>Age</label>
                <input type="number" v-model="resident.age" class="form-input" />
              </div>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label>Sex</label>
                <select v-model="resident.sex" class="form-input">
                  <option>Male</option><option>Female</option>
                </select>
              </div>
              <div class="form-group">
                <label>Relation to Household Head</label>
                <input type="text" v-model="resident.relation" placeholder="e.g., Head, Spouse, Child" class="form-input" />
              </div>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label>Occupation</label>
                <input type="text" v-model="resident.occupation" class="form-input" />
              </div>
              <div class="form-group">
                <label>Monthly Income</label>
                <div class="input-prefix-wrap">
                  <span class="input-prefix">₱</span>
                  <input type="number" v-model="resident.income" class="form-input with-prefix" />
                </div>
              </div>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label>Educational Attainment</label>
                <select v-model="resident.education" class="form-input">
                  <option value="">Select</option>
                  <option>No formal education</option>
                  <option>Elementary</option>
                  <option>High School</option>
                  <option>Senior High School</option>
                  <option>College</option>
                  <option>Post-graduate</option>
                </select>
              </div>
              <div class="form-group">
                <label>PhilHealth Number</label>
                <input type="text" v-model="resident.philhealth" class="form-input" />
              </div>
            </div>
            <div class="form-row-2">
              <div class="form-group">
                <label>PhilHealth Category</label>
                <input type="text" v-model="resident.philhealthCategory" class="form-input" />
              </div>
              <div class="form-group">
                <label>4Ps Eligibility</label>
                <select v-model="resident.fourPs" class="form-input">
                  <option>No</option><option>Yes</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <label>Disability Status</label>
              <input type="text" v-model="resident.disability" placeholder="None or specify" class="form-input" />
            </div>
            <div class="form-group">
              <label>Medical History</label>
              <textarea v-model="resident.medicalHistory" class="form-textarea"></textarea>
            </div>
            <div class="form-group">
              <label>Health Risk Classification</label>
              <input type="text" v-model="resident.healthRisk" class="form-input" />
            </div>
          </div>

          <button class="btn-add-resident" @click="addResident">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
            Add Another Resident
          </button>
        </div>
        <div class="modal-footer">
          <button class="btn-cancel" @click="closeModal">Cancel</button>
          <button class="btn-primary" @click="saveAll" :disabled="saving">
            {{ saving ? 'Saving...' : 'Save All' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router'
import { getStats, getHouseholds, addHousehold, updateHousehold, deleteHousehold, updateUserName } from '../api.js'

export default {
  name: 'Dashboard',
  setup() {
    const router = useRouter()
    return { router }
  },
  data() {
    return {
      currentPage: 'dashboard',
      selectedHousehold: null,
      showModal: false,
      modalMode: 'add',
      householdSearch: '',
      loadingHouseholds: false,
      saving: false,
      savingName: false, // ✅ NEW: loading state for name save
      stats: { households: 0, residents: 0, children: 0, seniors: 0, pwd: 0 },
      households: [],
      form: this.blankForm(),
      userName: localStorage.getItem('user_name') || 'Admin',
      userEmail: localStorage.getItem('user_email') || '',
      toast: { show: false, message: '', type: 'success' },
      showUserMenu: false,
      showEditName: false,
      editNameValue: '',
    }
  },
  computed: {
    userInitials() {
      return this.userName.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2)
    },
    filteredHouseholds() {
      const q = this.householdSearch.toLowerCase()
      if (!q) return this.households
      return this.households.filter(h =>
        h.headName.toLowerCase().includes(q) || h.zone.toLowerCase().includes(q)
      )
    },
  },
  mounted() {
    // ✅ Always re-read from localStorage on mount so fresh login data is picked up
    this.userName = localStorage.getItem('user_name') || 'Admin'
    this.userEmail = localStorage.getItem('user_email') || ''
    this.loadData()
    document.addEventListener('click', (e) => {
      if (this.$refs.userBadge && !this.$refs.userBadge.contains(e.target)) {
        this.showUserMenu = false
      }
    })
  },
  methods: {
    async loadData() {
      this.loadingHouseholds = true
      try {
        const [statsData, householdsData] = await Promise.all([
          getStats(),
          getHouseholds()
        ])
        this.stats = statsData
        this.households = householdsData
      } catch (err) {
        console.error('Failed to load data:', err)
      } finally {
        this.loadingHouseholds = false
      }
    },
    blankForm() {
      return {
        zone: '', lastName: '', firstName: '', middleName: '',
        families: '', membersCount: '',
        basicWater: '', safeWater: '', sanitation: '', safeSanitation: '',
        residents: [this.blankResident()],
      }
    },
    blankResident() {
      return {
        fullName: '', birthday: '', age: '', sex: 'Male', relation: '',
        occupation: '', income: '', education: '', philhealth: '',
        philhealthCategory: '', fourPs: 'No', disability: '',
        medicalHistory: '', healthRisk: '',
      }
    },
    openAddModal() {
      this.modalMode = 'add'
      this.form = this.blankForm()
      this.showModal = true
    },
    openEditModal() {
      this.modalMode = 'edit'
      if (this.selectedHousehold) {
        this.form = {
          zone: this.selectedHousehold.zone,
          lastName: this.selectedHousehold.lastName || '',
          firstName: this.selectedHousehold.firstName || '',
          middleName: this.selectedHousehold.middleName || '',
          families: this.selectedHousehold.families,
          membersCount: this.selectedHousehold.members,
          basicWater: this.selectedHousehold.basicWater || '',
          safeWater: this.selectedHousehold.safeWater || '',
          sanitation: this.selectedHousehold.sanitation || '',
          safeSanitation: this.selectedHousehold.safeSanitation || '',
          residents: this.selectedHousehold.residents.length
            ? this.selectedHousehold.residents.map(r => ({
                fullName: r.full_name,
                birthday: r.birthday,
                age: r.age,
                sex: r.sex,
                relation: r.relation_to_head,
                occupation: r.occupation,
                income: r.monthly_income,
                education: r.education,
                philhealth: r.philhealth_number,
                philhealthCategory: r.philhealth_category,
                fourPs: r.four_ps,
                disability: r.disability,
                medicalHistory: r.medical_history,
                healthRisk: r.health_risk,
              }))
            : [this.blankResident()],
        }
      }
      this.showModal = true
    },
    closeModal() {
      this.showModal = false
    },
    addResident() {
      this.form.residents.push(this.blankResident())
    },
    removeResident(idx) {
      this.form.residents.splice(idx, 1)
    },
    showToast(message, type = 'success') {
      this.toast = { show: true, message, type }
      setTimeout(() => { this.toast.show = false }, 3000)
    },
    toggleUserMenu() {
      this.showUserMenu = !this.showUserMenu
      if (this.showUserMenu) {
        this.showEditName = false
        this.editNameValue = this.userName
      }
    },
    // ✅ FIXED: saveName now saves to the database, not just localStorage
    async saveName() {
      if (!this.editNameValue.trim()) return
      this.savingName = true
      try {
        await updateUserName(this.userEmail, this.editNameValue.trim())
        this.userName = this.editNameValue.trim()
        localStorage.setItem('user_name', this.userName)
        this.showEditName = false
        this.showToast('Name updated successfully!')
      } catch (err) {
        this.showToast('Error updating name: ' + err.message, 'error')
      } finally {
        this.savingName = false
      }
    },
    async saveAll() {
      this.saving = true
      try {
        if (this.modalMode === 'add') {
          await addHousehold(this.form)
          this.showToast('Household added successfully!')
        } else if (this.modalMode === 'edit' && this.selectedHousehold) {
          await updateHousehold(this.selectedHousehold.id, this.form)
          this.showToast('Household updated successfully!')
        }
        await this.loadData()
        if (this.modalMode === 'edit') {
          this.selectedHousehold = this.households.find(h => h.id === this.selectedHousehold.id)
        }
        this.closeModal()
      } catch (err) {
        this.showToast('Error saving: ' + err.message, 'error')
      } finally {
        this.saving = false
      }
    },
    viewHousehold(h) {
      this.selectedHousehold = h
      this.currentPage = 'household-detail'
    },
    async deleteHousehold() {
      if (confirm('Are you sure you want to delete this household?')) {
        try {
          await deleteHousehold(this.selectedHousehold.id)
          await this.loadData()
          this.selectedHousehold = null
          this.currentPage = 'households'
          this.showToast('Household deleted successfully!')
        } catch (err) {
          this.showToast('Error deleting: ' + err.message, 'error')
        }
      }
    },
    logout() {
      this.showUserMenu = false
      if (confirm('Are you sure you want to logout?')) {
        localStorage.removeItem('isLoggedIn')
        localStorage.removeItem('user_email')
        localStorage.removeItem('user_name')
        this.router.push('/login')
      }
    },
  },
}
</script>

<style scoped>
* { box-sizing: border-box; margin: 0; padding: 0; }

.hhp-app { display: flex; height: 100vh; font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; background: #f4f6f5; color: #1a2e25; }

.sidebar { width: 150px; background: #1a4a35; display: flex; flex-direction: column; align-items: center; padding: 20px 0; flex-shrink: 0; }
.sidebar-logo { width: 52px; height: 52px; background: #fff; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 32px; }
.logo-text { font-weight: 800; font-size: 16px; color: #1a4a35; }
.sidebar-nav { display: flex; flex-direction: column; gap: 4px; width: 100%; padding: 0 10px; }
.nav-item { display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 14px 8px; border-radius: 12px; border: none; background: transparent; color: rgba(255,255,255,0.6); cursor: pointer; font-size: 12px; font-weight: 500; transition: all 0.2s; width: 100%; }
.nav-item svg { width: 22px; height: 22px; }
.nav-item:hover { background: rgba(255,255,255,0.1); color: #fff; }
.nav-item.active { background: #2d6e50; color: #fff; }

.main-content { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.topbar { display: flex; align-items: center; justify-content: space-between; padding: 16px 32px; background: #fff; border-bottom: 1px solid #e8eeeb; }
.page-title { font-size: 20px; font-weight: 700; color: #1a2e25; }
.topbar-right { display: flex; align-items: center; gap: 16px; }
.search-box { display: flex; align-items: center; gap: 8px; background: #f4f6f5; border: 1px solid #dde6e2; border-radius: 8px; padding: 8px 14px; min-width: 260px; }
.search-box svg { width: 16px; height: 16px; color: #8aab99; flex-shrink: 0; }
.search-box input { border: none; background: transparent; outline: none; font-size: 13px; color: #1a2e25; width: 100%; }
.search-box input::placeholder { color: #9db8ab; }

.user-badge { display: flex; align-items: center; gap: 8px; cursor: pointer; position: relative; }
.user-avatar { width: 36px; height: 36px; background: #1a4a35; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; }
.user-name { font-size: 14px; font-weight: 600; color: #1a2e25; }
.user-badge > svg { width: 14px; height: 14px; color: #8aab99; }
.user-dropdown { position: absolute; top: calc(100% + 12px); right: 0; background: #fff; border: 1px solid #e8eeeb; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); min-width: 250px; z-index: 500; overflow: hidden; }
.user-dropdown-header { display: flex; align-items: center; gap: 12px; padding: 16px; }
.user-avatar-lg { width: 42px; height: 42px; background: #1a4a35; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 700; flex-shrink: 0; }
.user-dropdown-name { font-size: 14px; font-weight: 700; color: #1a2e25; }
.user-dropdown-email { font-size: 12px; color: #8aab99; margin-top: 2px; }
.user-dropdown-divider { height: 1px; background: #e8eeeb; }
.user-dropdown-item { display: flex; align-items: center; gap: 10px; padding: 12px 16px; font-size: 13.5px; font-weight: 500; color: #2a3e32; cursor: pointer; transition: background 0.15s; }
.user-dropdown-item svg { width: 16px; height: 16px; color: #5a7a6a; }
.user-dropdown-item:hover { background: #f4f8f6; }
.user-dropdown-logout { color: #c0392b; }
.user-dropdown-logout svg { color: #c0392b; }
.user-dropdown-logout:hover { background: #fdf0ef; }
.user-dropdown-edit { padding: 12px 16px; }
.user-dropdown-edit label { display: block; font-size: 12px; font-weight: 600; color: #5a7a6a; margin-bottom: 6px; }
.user-edit-input { width: 100%; padding: 8px 10px; border: 1.5px solid #dde6e2; border-radius: 7px; font-size: 13px; color: #1a2e25; outline: none; box-sizing: border-box; }
.user-edit-input:focus { border-color: #2d6e50; }
.user-edit-actions { display: flex; gap: 8px; margin-top: 8px; }
.btn-edit-cancel { flex: 1; padding: 7px; background: #fff; border: 1.5px solid #ccd9d3; border-radius: 7px; font-size: 12.5px; font-weight: 600; cursor: pointer; color: #1a2e25; }
.btn-edit-save { flex: 1; padding: 7px; background: #1a4a35; border: none; border-radius: 7px; font-size: 12.5px; font-weight: 600; cursor: pointer; color: #fff; }
.btn-edit-save:hover:not(:disabled) { background: #0f3326; }
.btn-edit-save:disabled { opacity: 0.6; cursor: not-allowed; }

.page-content { flex: 1; overflow-y: auto; padding: 28px 32px; }
.stats-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; margin-bottom: 28px; }
.stat-card { background: #fff; border-radius: 14px; padding: 24px 20px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 10px; border: 1px solid #e8eeeb; }
.stat-icon { color: #2d6e50; }
.stat-icon svg { width: 36px; height: 36px; }
.stat-label { font-size: 12px; color: #7a9989; font-weight: 500; }
.stat-value { font-size: 28px; font-weight: 800; color: #1a2e25; line-height: 1; }

.table-section { background: #fff; border-radius: 14px; border: 1px solid #e8eeeb; padding: 20px; }
.table-toolbar { display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; }
.loading-state { text-align: center; padding: 32px; color: #8aab99; font-size: 14px; }

.data-table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
.data-table th { text-align: left; padding: 10px 14px; font-size: 12.5px; font-weight: 600; color: #5a7a6a; background: #f4f8f6; border-bottom: 1px solid #e8eeeb; }
.data-table td { padding: 14px 14px; border-bottom: 1px solid #f0f4f2; color: #2a3e32; vertical-align: middle; }
.data-table tbody tr:last-child td { border-bottom: none; }
.data-table tbody tr:hover td { background: #f8faf9; }

.badge { display: inline-block; padding: 3px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; }
.badge-safe { background: #d4f0e4; color: #1a6b42; }
.badge-basic { background: #fef3cd; color: #856404; }
.badge-no { background: #f0f0f0; color: #666; }

.btn-primary { display: flex; align-items: center; gap: 7px; background: #1a4a35; color: #fff; border: none; border-radius: 8px; padding: 10px 18px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: background 0.2s; white-space: nowrap; }
.btn-primary svg { width: 15px; height: 15px; }
.btn-primary:hover:not(:disabled) { background: #0f3326; }
.btn-primary:disabled { opacity: 0.6; cursor: not-allowed; }
.btn-danger { display: flex; align-items: center; gap: 7px; background: #c0392b; color: #fff; border: none; border-radius: 8px; padding: 10px 18px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: background 0.2s; white-space: nowrap; }
.btn-danger svg { width: 15px; height: 15px; }
.btn-danger:hover { background: #992d22; }
.btn-cancel { background: #fff; color: #1a2e25; border: 1.5px solid #ccd9d3; border-radius: 8px; padding: 10px 22px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: all 0.2s; }
.btn-cancel:hover { background: #f4f6f5; }
.btn-view { display: flex; align-items: center; gap: 5px; background: #fff; border: 1.5px solid #ccd9d3; border-radius: 7px; padding: 7px 14px; font-size: 13px; font-weight: 500; color: #2a3e32; cursor: pointer; transition: all 0.2s; }
.btn-view:hover { border-color: #1a4a35; color: #1a4a35; }
.btn-view svg { width: 13px; height: 13px; }
.action-btn-wrap { display: flex; }

.detail-back { display: flex; align-items: center; gap: 6px; font-size: 13.5px; color: #2d6e50; font-weight: 600; cursor: pointer; margin-bottom: 16px; width: fit-content; }
.detail-back svg { width: 18px; height: 18px; }
.detail-back:hover { color: #1a4a35; }
.detail-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 24px; gap: 16px; flex-wrap: wrap; }
.detail-title { font-size: 22px; font-weight: 700; color: #1a2e25; }
.detail-sub { font-size: 13px; color: #8aab99; margin-top: 4px; }
.detail-actions { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.detail-card { background: #fff; border-radius: 14px; border: 1px solid #e8eeeb; padding: 24px; overflow-x: auto; }
.section-title-sm { font-size: 13px; font-weight: 700; color: #5a7a6a; letter-spacing: 0.6px; margin-bottom: 20px; }
.detail-field { margin-bottom: 16px; }
.detail-field label { font-size: 12px; color: #7a9989; font-weight: 600; display: block; margin-bottom: 6px; }
.detail-value { font-size: 14px; color: #1a2e25; font-weight: 500; background: #f8faf9; padding: 10px 14px; border-radius: 8px; border: 1px solid #e8eeeb; }
.detail-row-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.45); display: flex; align-items: flex-start; justify-content: center; z-index: 1000; padding: 20px; overflow-y: auto; }
.modal { background: #fff; border-radius: 16px; width: 100%; max-width: 760px; display: flex; flex-direction: column; max-height: 90vh; margin: auto; box-shadow: 0 20px 60px rgba(0,0,0,0.2); }
.modal-header { background: #1a4a35; color: #fff; padding: 18px 24px; border-radius: 16px 16px 0 0; display: flex; align-items: center; justify-content: space-between; flex-shrink: 0; }
.modal-title { display: flex; align-items: center; gap: 10px; font-size: 15px; font-weight: 700; }
.modal-title svg { width: 18px; height: 18px; }
.modal-close { background: transparent; border: none; color: #fff; cursor: pointer; padding: 4px; border-radius: 6px; opacity: 0.8; transition: opacity 0.2s; }
.modal-close:hover { opacity: 1; }
.modal-close svg { width: 20px; height: 20px; }
.modal-body { padding: 24px; overflow-y: auto; flex: 1; }
.modal-section-header { font-size: 12.5px; font-weight: 700; color: #3a6a52; letter-spacing: 0.5px; margin: 20px 0 16px; padding-bottom: 8px; border-bottom: 1.5px solid #e8eeeb; }
.form-group { margin-bottom: 14px; }
.form-group label { display: block; font-size: 12.5px; color: #5a7a6a; font-weight: 600; margin-bottom: 5px; }
.form-input { width: 100%; padding: 9px 12px; border: 1.5px solid #dde6e2; border-radius: 8px; font-size: 13.5px; color: #1a2e25; background: #fff; outline: none; transition: border-color 0.2s; appearance: none; }
.form-input:focus { border-color: #2d6e50; }
.form-textarea { width: 100%; padding: 9px 12px; border: 1.5px solid #dde6e2; border-radius: 8px; font-size: 13.5px; color: #1a2e25; background: #fff; outline: none; transition: border-color 0.2s; min-height: 80px; resize: vertical; }
.form-textarea:focus { border-color: #2d6e50; }
.form-row-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.form-row-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; }
.input-prefix-wrap { position: relative; display: flex; align-items: center; }
.input-prefix { position: absolute; left: 12px; font-size: 13.5px; color: #7a9989; pointer-events: none; }
.form-input.with-prefix { padding-left: 24px; }
.resident-card { border: 1.5px solid #e8eeeb; border-radius: 10px; padding: 18px; margin-bottom: 16px; background: #fafcfb; }
.resident-card-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; }
.resident-card-title { font-size: 13px; font-weight: 700; color: #2d6e50; }
.btn-remove-resident { display: flex; align-items: center; gap: 5px; background: transparent; border: 1.5px solid #e8b4b0; color: #c0392b; border-radius: 7px; padding: 5px 12px; font-size: 12.5px; font-weight: 600; cursor: pointer; transition: all 0.2s; }
.btn-remove-resident svg { width: 13px; height: 13px; }
.btn-remove-resident:hover { background: #fdf0ef; border-color: #c0392b; }
.btn-add-resident { display: flex; align-items: center; gap: 7px; background: transparent; border: 2px solid #2d6e50; color: #2d6e50; border-radius: 8px; padding: 10px 18px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: all 0.2s; }
.btn-add-resident svg { width: 15px; height: 15px; }
.btn-add-resident:hover { background: #e8f5ee; }
.modal-footer { padding: 16px 24px; border-top: 1px solid #e8eeeb; display: flex; justify-content: flex-end; gap: 12px; flex-shrink: 0; background: #fafcfb; border-radius: 0 0 16px 16px; }
.empty-state { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; height: 300px; color: #8aab99; }
.empty-state svg { width: 48px; height: 48px; }
.empty-state p { font-size: 15px; }

.toast { position: fixed; bottom: 28px; right: 28px; z-index: 2000; display: flex; align-items: center; gap: 10px; padding: 14px 20px; border-radius: 10px; font-size: 14px; font-weight: 600; box-shadow: 0 8px 24px rgba(0,0,0,0.15); animation: slideUp 0.3s ease; }
.toast svg { width: 18px; height: 18px; flex-shrink: 0; }
.toast-success { background: #1a4a35; color: #fff; }
.toast-error { background: #c0392b; color: #fff; }
@keyframes slideUp { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
</style>