<template>
  <div class="hhp-app">
    <aside class="sidebar">
      <div class="sidebar-logo">
        <img src="data:image/png;base64,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" alt="Barangay Tampadong" class="logo-img" />
      </div>
      <nav class="sidebar-nav">
        <button class="nav-item" :class="{ active: currentPage === 'dashboard' }" @click="currentPage = 'dashboard'">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
          <span>Dashboard</span>
        </button>
        <button class="nav-item" :class="{ active: currentPage === 'households' || currentPage === 'household-detail' }" @click="currentPage = 'households'; selectedHousehold = null; viewingZone = null; householdSearch = ''">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          <span>Households</span>
        </button>
        <button class="nav-item" :class="{ active: currentPage === 'residents' }" @click="currentPage = 'residents'; residentListSearch = ''; residentListZone = ''">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          <span>Residents</span>
        </button>
        <button class="nav-item" :class="{ active: currentPage === 'barangay' }" @click="currentPage = 'barangay'">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          <span>Barangay</span>
        </button>
      </nav>
    </aside>

    <main class="main-content">
      <header class="topbar">
        <h1 class="page-title">
          <template v-if="currentPage === 'dashboard'">Barangay Tampadong Data Profiling</template>
          <template v-else-if="currentPage === 'households'">{{ viewingZone ? `Zone ${viewingZone} — Households` : 'Households' }}</template>
          <template v-else-if="currentPage === 'household-detail'">Household Details</template>
          <template v-else-if="currentPage === 'reports'">Reports</template>
          <template v-else-if="currentPage === 'barangay'">Barangay Info</template>
          <template v-else-if="currentPage === 'residents'">Residents</template>
        </h1>
        <div class="topbar-right">
          <!-- GLOBAL SEARCH -->
          <div class="global-search-wrap" @click.stop ref="globalSearchWrap">
            <div class="global-search-box" :class="{ active: globalSearchQuery }">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input type="text" v-model="globalSearchQuery" placeholder="Search residents, households..." @focus="showSearchResults = true" @input="showSearchResults = true" />
              <button v-if="globalSearchQuery" class="search-clear" @click="globalSearchQuery = ''; showSearchResults = false">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="14" height="14"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
              </button>
            </div>
            <div v-if="showSearchResults && globalSearchQuery.trim().length > 0" class="search-dropdown">
              <div v-if="globalSearchResults.length === 0" class="search-no-results">No matches found</div>
              <template v-else>
                <div class="search-results-header">
                  <span>{{ globalSearchResults.length }} match{{ globalSearchResults.length !== 1 ? 'es' : '' }} found</span>
                  <button class="search-close-btn" @click="globalSearchQuery = ''; showSearchResults = false">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="14" height="14"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                  </button>
                </div>
                <div class="search-results-cols"><span>RESIDENT NAME</span><span>ZONE</span><span>HOUSEHOLD</span><span></span></div>
                <div v-for="result in globalSearchResults" :key="result.residentId" class="search-result-row">
                  <div class="search-result-name">
                    <span v-html="highlightMatch(result.residentName, globalSearchQuery)"></span>
                    <span class="search-result-meta">{{ result.sex }} · Age {{ result.age }} · {{ result.relation }}</span>
                  </div>
                  <div><span class="search-zone-badge">Zone {{ result.zone }}</span></div>
                  <div class="search-result-household" v-html="highlightMatch(result.householdHead, globalSearchQuery)"></div>
                  <div><button class="btn-view-profile" @click="viewHouseholdFromSearch(result)">View Profile</button></div>
                </div>
              </template>
            </div>
          </div>
          <div class="user-badge" @click="toggleUserMenu" ref="userBadge">
            <span class="user-avatar">{{ userInitials }}</span>
            <span class="user-name">{{ userName }}</span>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
            <div v-if="showUserMenu" class="user-dropdown" @click.stop>
              <div class="user-dropdown-header">
                <span class="user-avatar-lg">{{ userInitials }}</span>
                <div>
                  <div class="user-dropdown-name">{{ userName }}</div>
                  <div class="user-dropdown-email">{{ userEmail }}</div>
                </div>
              </div>
              <div class="user-dropdown-divider"></div>
              <div v-if="!showEditName" class="user-dropdown-item" @click="showEditName = true; editNameValue = userName">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
                Settings
              </div>
              <div v-if="showEditName" class="user-dropdown-edit">
                <label>Display Name</label>
                <input type="text" v-model="editNameValue" class="user-edit-input" placeholder="Enter your name" />
                <div class="user-edit-actions">
                  <button class="btn-edit-cancel" @click="showEditName = false">Cancel</button>
                  <button class="btn-edit-save" @click="saveName" :disabled="savingName">{{ savingName ? 'Saving...' : 'Save' }}</button>
                </div>
              </div>
              <div class="user-dropdown-divider"></div>
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
          <div class="stat-card"><div class="stat-label">Total Households</div><div class="stat-value">{{ stats.households }}</div></div>
          <div class="stat-card"><div class="stat-label">Total Residents</div><div class="stat-value">{{ stats.residents }}</div></div>
          <div class="stat-card"><div class="stat-label">Children</div><div class="stat-value">{{ stats.children }}</div></div>
          <div class="stat-card"><div class="stat-label">Senior Citizens</div><div class="stat-value">{{ stats.seniors }}</div></div>
          <div class="stat-card"><div class="stat-label">Persons with Disability</div><div class="stat-value">{{ stats.pwd }}</div></div>
        </div>
        <div class="zone-overview-header">
          <div>
            <h2 class="zone-overview-title">Zone Overview — All Zones</h2>
            <p class="zone-overview-sub">Click "View Zone" to see households within a zone</p>
          </div>
          <div class="zone-overview-controls">
            <span class="sort-label">Sort by:</span>
            <select v-model="zoneSortBy" class="sort-select"><option value="households">Households</option><option value="population">Population</option><option value="zone">Zone Name</option></select>
            <select v-model="zoneSortDir" class="sort-select"><option value="asc">Ascending</option><option value="desc">Descending</option></select>
            <button class="btn-add-zone" @click="openAddModal">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              Add Zone
            </button>
          </div>
        </div>
        <div v-if="loadingHouseholds" class="loading-state">Loading zones...</div>
        <div v-else class="zone-cards-grid">
          <div v-if="sortedZones.length === 0" class="zone-empty">No zones found. Add a household to get started.</div>
          <div v-for="zone in sortedZones" :key="zone.zone" class="zone-card">
            <div class="zone-card-header"><span class="zone-card-name">Zone {{ zone.zone }}</span></div>
            <div class="zone-card-body">
              <div class="zone-stat-row">
                <div class="zone-stat"><div class="zone-stat-label">HOUSEHOLDS</div><div class="zone-stat-value">{{ zone.households }}</div><div class="zone-stat-sub">registered</div></div>
                <div class="zone-stat"><div class="zone-stat-label">POPULATION</div><div class="zone-stat-value">{{ zone.population }}</div><div class="zone-stat-sub">residents</div></div>
              </div>
              <div class="zone-badges-row">
                <span class="zone-badge-label">Water:</span>
                <span class="zone-status-badge" :class="getWaterClass(zone.waterStatus)">{{ zone.waterStatus || 'Safe' }}</span>
                <span class="zone-badge-label" style="margin-left:10px;">Sanitation:</span>
                <span class="zone-status-badge" :class="getSanitationClass(zone.sanitationStatus)">{{ zone.sanitationStatus || 'Good' }}</span>
              </div>
              <div class="zone-card-actions">
              <button class="btn-view-zone" @click="viewZone(zone.zone)">View Zone</button>
              <button class="btn-zone-delete" @click="deleteZone(zone.zone)">Delete</button>
            </div>
            </div>
          </div>
        </div>
      </div>

      <!-- HOUSEHOLDS PAGE -->
      <div v-else-if="currentPage === 'households'" class="page-content">
        <div v-if="viewingZone" class="detail-back" @click="currentPage = 'dashboard'; viewingZone = null; householdSearch = ''" style="margin-bottom:12px;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
          Back to All Zones
        </div>
        <div class="table-section">
          <div class="table-toolbar">
            <div class="search-box">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input type="text" v-model="householdSearch" placeholder="Search Household..." />
            </div>
            <button class="btn-primary" @click="openAddModal">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              {{ viewingZone ? `Add Household to Zone ${viewingZone}` : 'Add Household' }}
            </button>
          </div>
          <div v-if="loadingHouseholds" class="loading-state">Loading households...</div>
          <table v-else class="data-table">
            <thead>
              <tr>
                <th>Zone</th><th>Head Name</th><th>Members</th><th>Children</th><th>Water Status</th><th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="filteredHouseholds.length === 0">
                <td colspan="6" style="text-align:center;color:#8aab99;padding:32px;">No households found.</td>
              </tr>
              <tr v-for="h in filteredHouseholds" :key="h.id">
                <td>{{ h.zone }}</td>
                <td>{{ h.headName }}</td>
                <td>{{ h.members }}</td>
                <td>{{ h.children }}</td>
                <td><span class="badge" :class="h.waterStatus === 'Safe' ? 'badge-safe' : 'badge-basic'">{{ h.waterStatus }}</span></td>
                <td>
                  <div class="act-wrap" @click.stop>
                    <button class="btn-act" :class="{ open: openActionsId === h.id }" @click="toggleActions(h.id)">
                      Actions
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="12" height="12"><polyline :points="openActionsId === h.id ? '18 15 12 9 6 15' : '6 9 12 15 18 9'"/></svg>
                    </button>
                    <div v-if="openActionsId === h.id" class="act-menu">
                      <div class="act-item" @click="viewHousehold(h)"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>View Household</div>
                      <div class="act-item" @click="openEditModalFor(h)"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>Edit Household</div>
                      <div class="act-item" @click="openAddResidentFor(h)"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>Add Resident</div>
                      <div class="act-item" @click="openTransferFor(h)"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>Transfer Household</div>
                      <div class="act-divider"></div>
                      <div class="act-item act-danger" @click="deleteHouseholdById(h)"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/></svg>Delete Household</div>
                    </div>
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
        <div class="hd-breadcrumb">
          <span class="hd-bc-link" @click="currentPage = 'dashboard'; selectedHousehold = null">Dashboard</span>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="13" height="13"><polyline points="9 18 15 12 9 6"/></svg>
          <span v-if="viewingZone" class="hd-bc-link" @click="currentPage = 'households'">Zone {{ selectedHousehold.zone }} — Households</span>
          <svg v-if="viewingZone" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="13" height="13"><polyline points="9 18 15 12 9 6"/></svg>
          <span class="hd-bc-current">{{ selectedHousehold.headName }}</span>
        </div>
        <div class="hd-header">
          <h2 class="hd-title">Household Profile</h2>
          <div class="hd-actions">
            <button class="btn-primary" @click="openEditModal">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
              Edit Household
            </button>
            <button class="btn-danger" @click="deleteHousehold">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/></svg>
              Delete Household
            </button>
          </div>
        </div>
        <div class="hd-cards-row" style="grid-template-columns:1fr 1fr;">
          <div class="hd-info-card">
            <div class="hd-card-title">HOUSEHOLD INFORMATION</div>
            <div class="hd-info-row"><span class="hd-info-label">Household Head</span><span class="hd-info-val bold">{{ selectedHousehold.headName }}</span></div>
            <div class="hd-info-row"><span class="hd-info-label">Zone</span><span class="hd-info-val bold">Zone {{ selectedHousehold.zone }}</span></div>
            <div class="hd-info-row"><span class="hd-info-label">Number of Families</span><span class="hd-info-val bold">{{ selectedHousehold.families || '—' }}</span></div>
            <div class="hd-info-row"><span class="hd-info-label">Number of Members</span><span class="hd-info-val bold">{{ selectedHousehold.members || '—' }}</span></div>
          </div>
          <div class="hd-info-card">
            <div class="hd-card-title">WATER &amp; SANITATION</div>
            <div class="hd-info-row"><span class="hd-info-label">Basic Safe Water Source</span><span class="badge" :class="selectedHousehold.basicWater === 'Yes' ? 'badge-safe' : selectedHousehold.basicWater === 'No' ? 'badge-no' : 'badge-basic'">{{ selectedHousehold.basicWater || '—' }}</span></div>
            <div class="hd-info-row"><span class="hd-info-label">Safely Managed Water</span><span class="badge" :class="selectedHousehold.safeWater === 'Yes' ? 'badge-safe' : selectedHousehold.safeWater === 'No' ? 'badge-no' : 'badge-basic'">{{ selectedHousehold.safeWater || '—' }}</span></div>
            <div class="hd-info-row"><span class="hd-info-label">Sanitation Service</span><span class="badge" :class="selectedHousehold.sanitation === 'Good' ? 'badge-safe' : selectedHousehold.sanitation === 'Basic' ? 'badge-basic' : selectedHousehold.sanitation === 'No' ? 'badge-no' : 'badge-basic'">{{ selectedHousehold.sanitation || '—' }}</span></div>
            <div class="hd-info-row"><span class="hd-info-label">Safely Managed Sanitation</span><span class="badge" :class="selectedHousehold.safeSanitation === 'Yes' ? 'badge-safe' : selectedHousehold.safeSanitation === 'No' ? 'badge-no' : 'badge-basic'">{{ selectedHousehold.safeSanitation || '—' }}</span></div>
          </div>
        </div>
        <div class="hd-resident-section">
          <div class="hd-resident-toolbar">
            <h3 class="hd-resident-title">Resident List</h3>
            <div class="hd-resident-controls">
              <div class="search-box" style="min-width:220px;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                <input type="text" v-model="residentSearch" placeholder="Search name, occupation, relation..." />
              </div>
              <span class="sort-label">Sort:</span>
              <select v-model="residentSortBy" class="sort-select"><option value="name">Name</option><option value="age">Age</option><option value="relation">Relation</option></select>
              <select v-model="residentSortDir" class="sort-select"><option value="asc">Ascending</option><option value="desc">Descending</option></select>
              <button class="btn-primary" @click="openAddResidentFor(selectedHousehold)">+ Add Resident</button>
            </div>
          </div>
          <table class="data-table">
            <thead>
              <tr><th>#</th><th>FULL NAME</th><th>SEX</th><th>BIRTHDAY</th><th>AGE</th><th>RELATION TO HEAD</th><th>ACTIONS</th></tr>
            </thead>
            <tbody>
              <tr v-if="filteredResidents.length === 0">
                <td colspan="7" style="text-align:center;color:#8aab99;padding:32px;">No residents added yet.</td>
              </tr>
              <tr v-for="(r, idx) in filteredResidents" :key="r.id || idx">
                <td class="td-num">{{ idx + 1 }}</td>
                <td class="td-res-name">{{ r.full_name }}</td>
                <td>{{ r.sex }}</td>
                <td>{{ r.birthday }}</td>
                <td>{{ r.age }}</td>
                <td>{{ r.relation_to_head }}</td>
                <td>
  <div class="act-wrap" @click.stop>
    <button class="btn-act" :class="{ open: openResidentActionsId === (r.id || idx) }"
            @click="toggleResidentActions(r.id || idx)">
      Actions
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="12" height="12">
        <polyline :points="openResidentActionsId === (r.id || idx) ? '18 15 12 9 6 15' : '6 9 12 15 18 9'"/>
      </svg>
    </button>
    <div v-if="openResidentActionsId === (r.id || idx)" class="act-menu">
      <div class="act-item" @click="openResidentProfile(r)">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15">
          <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
        </svg>
        View Profile
      </div>
      <div class="act-item" @click="promoteToHead(r)">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15">
          <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>
          <polyline points="16 11 18 13 22 9"/>
        </svg>
        Make Household Head
      </div>
    </div>
  </div>
</td>
              </tr>
            </tbody>
          </table>
          <div class="hd-resident-footer">{{ filteredResidents.length }} resident{{ filteredResidents.length !== 1 ? 's' : '' }}</div>
        </div>
      </div>

      <!-- REPORTS PAGE -->
      <div v-else-if="currentPage === 'reports'" class="page-content">
        <div class="empty-state">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
          <p>Reports feature coming soon.</p>
        </div>
      </div>

      <!-- RESIDENTS PAGE -->
      <div v-else-if="currentPage === 'residents'" class="page-content">
        <div class="table-section">
          <div class="table-toolbar">
            <div class="search-box" style="flex:1;max-width:340px;">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input type="text" v-model="residentListSearch" placeholder="Search by name, occupation, relation..." />
            </div>
            <div style="display:flex;align-items:center;gap:8px;">
              <span class="sort-label">Zone:</span>
              <select v-model="residentListZone" class="sort-select">
                <option value="">All Zones</option>
                <option v-for="z in availableZones" :key="z" :value="z">Zone {{ z }}</option>
              </select>
              <span class="sort-label">Sort:</span>
              <select v-model="residentListSortBy" class="sort-select">
                <option value="name">Name</option>
                <option value="age">Age</option>
                <option value="zone">Zone</option>
              </select>
              <select v-model="residentListSortDir" class="sort-select">
                <option value="asc">Ascending</option>
                <option value="desc">Descending</option>
              </select>
            </div>
          </div>

          <table class="data-table">
            <thead>
              <tr>
                <th>#</th>
                <th>FULL NAME</th>
                <th>SEX</th>
                <th>AGE</th>
                <th>BIRTHDAY</th>
                <th>RELATION TO HEAD</th>
                <th>HOUSEHOLD HEAD</th>
                <th>ZONE</th>
                <th>ACTIONS</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="allResidents.length === 0">
                <td colspan="9" style="text-align:center;color:#8aab99;padding:32px;">No residents found.</td>
              </tr>
              <tr v-for="(r, idx) in allResidents" :key="idx">
                <td class="td-num">{{ idx + 1 }}</td>
                <td class="td-res-name">{{ r.full_name }}</td>
                <td>{{ r.sex }}</td>
                <td>{{ r.age }}</td>
                <td>{{ r.birthday }}</td>
                <td>{{ r.relation_to_head }}</td>
                <td>{{ r.householdHead }}</td>
                <td><span class="search-zone-badge">Zone {{ r.zone }}</span></td>
                <td>
                  <button class="btn-view-profile" @click="openResidentProfile(r)">View Profile</button>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="hd-resident-footer">{{ allResidents.length }} resident{{ allResidents.length !== 1 ? 's' : '' }}</div>
        </div>
      </div>

      <!-- BARANGAY PAGE -->
      <div v-else-if="currentPage === 'barangay'" class="page-content">
        <div class="bgy-hero">
          <div class="bgy-hero-left">
            <div class="bgy-logo-wrap">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="40" height="40"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
            </div>
            <div>
              <div class="bgy-hero-label">Official Barangay Profile</div>
              <div class="bgy-hero-name">Barangay {{ barangay.name }}</div>
              <div class="bgy-hero-address">{{ barangay.municipality }}, {{ barangay.province }} · Postal Code {{ barangay.postalCode }}</div>
              <div class="bgy-hero-badges">
                <span class="bgy-badge">Population: {{ barangay.population }}</span>
                <span class="bgy-badge">PSGC: {{ barangay.psgcCode }}</span>
                <span class="bgy-badge">{{ barangay.classification }} Barangay</span>
              </div>
            </div>
          </div>
          <button class="btn-edit-info" @click="showEditBarangay = true">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="14" height="14"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
            Edit Info
          </button>
        </div>
        <div class="bgy-cards-row">
          <div class="bgy-card">
            <div class="bgy-card-title">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><circle cx="12" cy="10" r="3"/><path d="M12 2a8 8 0 0 1 8 8c0 5.25-8 12-8 12S4 15.25 4 10a8 8 0 0 1 8-8z"/></svg>
              LOCATION &amp; CLASSIFICATION
            </div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><div><div class="bgy-row-label">Barangay</div><div class="bgy-row-val">{{ barangay.name }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><circle cx="12" cy="10" r="3"/><path d="M12 2a8 8 0 0 1 8 8c0 5.25-8 12-8 12S4 15.25 4 10a8 8 0 0 1 8-8z"/></svg><div><div class="bgy-row-label">Municipality</div><div class="bgy-row-val">{{ barangay.municipality }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/></svg><div><div class="bgy-row-label">Province</div><div class="bgy-row-val">{{ barangay.province }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg><div><div class="bgy-row-label">Region</div><div class="bgy-row-val">{{ barangay.region }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg><div><div class="bgy-row-label">Classification</div><div class="bgy-row-val">{{ barangay.classification }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/></svg><div><div class="bgy-row-label">PSGC Code</div><div class="bgy-row-val">{{ barangay.psgcCode }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.59 1.18h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.73a16 16 0 0 0 6 6l.92-.92a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7a2 2 0 0 1 1.72 2.03z"/></svg><div><div class="bgy-row-label">City ZIP / Postal Code</div><div class="bgy-row-val">{{ barangay.postalCode }}</div></div></div>
          </div>
          <div class="bgy-card">
            <div class="bgy-card-title">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              CONTACT &amp; ADMINISTRATION
            </div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg><div><div class="bgy-row-label">Punong Barangay</div><div class="bgy-row-val">{{ barangay.captain }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.59 1.18h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.73a16 16 0 0 0 6 6l.92-.92a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7a2 2 0 0 1 1.72 2.03z"/></svg><div><div class="bgy-row-label">Contact Number</div><div class="bgy-row-val">{{ barangay.contactNumber }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg><div><div class="bgy-row-label">Email Address</div><div class="bgy-row-val">{{ barangay.email }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg><div><div class="bgy-row-label">Office Hours</div><div class="bgy-row-val">{{ barangay.officeHours }}</div></div></div>
            <div class="bgy-info-row"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg><div><div class="bgy-row-label">Barangay Hall Address</div><div class="bgy-row-val">{{ barangay.hallAddress }}</div></div></div>
          </div>
        </div>

        <!-- Water & Sanitation Summary -->
        <div class="bgy-ws-section">
          <div class="bgy-ws-title">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><circle cx="12" cy="12" r="10"/></svg>
            WATER &amp; SANITATION SUMMARY
          </div>
          <div class="bgy-ws-grid">
            <div class="bgy-ws-card">
              <div class="bgy-ws-label">Safe water access</div>
              <div class="bgy-ws-pct">{{ waterSummary.safe }}%</div>
              <div class="bgy-ws-bar-track"><div class="bgy-ws-bar bgy-ws-bar-safe" :style="{ width: waterSummary.safe + '%' }"></div></div>
            </div>
            <div class="bgy-ws-card">
              <div class="bgy-ws-label">Basic water access</div>
              <div class="bgy-ws-pct">{{ waterSummary.basic }}%</div>
              <div class="bgy-ws-bar-track"><div class="bgy-ws-bar bgy-ws-bar-basic" :style="{ width: waterSummary.basic + '%' }"></div></div>
            </div>
            <div class="bgy-ws-card">
              <div class="bgy-ws-label">Limited water access</div>
              <div class="bgy-ws-pct">{{ waterSummary.limited }}%</div>
              <div class="bgy-ws-bar-track"><div class="bgy-ws-bar bgy-ws-bar-limited" :style="{ width: waterSummary.limited + '%' }"></div></div>
            </div>
            <div class="bgy-ws-card">
              <div class="bgy-ws-label">Good sanitation</div>
              <div class="bgy-ws-pct">{{ sanitationSummary.good }}%</div>
              <div class="bgy-ws-bar-track"><div class="bgy-ws-bar bgy-ws-bar-safe" :style="{ width: sanitationSummary.good + '%' }"></div></div>
            </div>
            <div class="bgy-ws-card">
              <div class="bgy-ws-label">Basic sanitation</div>
              <div class="bgy-ws-pct">{{ sanitationSummary.basic }}%</div>
              <div class="bgy-ws-bar-track"><div class="bgy-ws-bar bgy-ws-bar-basic" :style="{ width: sanitationSummary.basic + '%' }"></div></div>
            </div>
            <div class="bgy-ws-card">
              <div class="bgy-ws-label">Poor sanitation</div>
              <div class="bgy-ws-pct">{{ sanitationSummary.poor }}%</div>
              <div class="bgy-ws-bar-track"><div class="bgy-ws-bar bgy-ws-bar-limited" :style="{ width: sanitationSummary.poor + '%' }"></div></div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- TOAST -->
    <div v-if="toast.show" class="toast" :class="'toast-' + toast.type">
      <svg v-if="toast.type === 'success'" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
      <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
      {{ toast.message }}
    </div>

    <!-- ADD/EDIT HOUSEHOLD MODAL -->
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
          <div class="form-group"><label>Zone No.</label><div v-if="viewingZone && modalMode === 'add'" class="detail-value" style="font-size:14px;">{{ viewingZone }}</div><input v-else type="text" v-model="form.zone" class="form-input" /></div>
          <div class="form-group"><label>Household Head Name</label><div class="form-row-3"><input type="text" v-model="form.lastName" placeholder="Last Name" class="form-input" /><input type="text" v-model="form.firstName" placeholder="First Name" class="form-input" /><input type="text" v-model="form.middleName" placeholder="Middle Name" class="form-input" /></div></div>
          <div class="form-row-2"><div class="form-group"><label>No. of Families</label><input type="number" v-model="form.families" class="form-input" /></div><div class="form-group"><label>No. of Household Members</label><input type="number" v-model="form.membersCount" class="form-input" /></div></div>

          <div class="modal-section-header">HOUSEHOLD HEAD DETAILS</div>
          <div class="resident-card">
            <div class="form-row-2">
              <div class="form-group"><label>Birthday</label><input type="date" v-model="form.head.birthday" class="form-input" /></div>
              <div class="form-group"><label>Age</label><input type="number" v-model="form.head.age" class="form-input" /></div>
            </div>
            <div class="form-row-2">
              <div class="form-group"><label>Sex</label><select v-model="form.head.sex" class="form-input"><option value="">Select</option><option>Male</option><option>Female</option></select></div>
              <div class="form-group"><label>Civil Status</label><select v-model="form.head.civilStatus" class="form-input"><option value="">Select</option><option>Single</option><option>Married</option><option>Widowed</option><option>Separated</option></select></div>
            </div>
            <div class="form-row-2">
              <div class="form-group"><label>Occupation</label><input type="text" v-model="form.head.occupation" class="form-input" /></div>
              <div class="form-group"><label>Monthly Income</label><div class="input-prefix-wrap"><span class="input-prefix">₱</span><input type="number" v-model="form.head.income" class="form-input with-prefix" /></div></div>
            </div>
            <div class="form-row-2">
              <div class="form-group"><label>Educational Attainment</label><select v-model="form.head.education" class="form-input"><option value="">Select</option><option>No formal education</option><option>Elementary</option><option>High School</option><option>Senior High School</option><option>College</option><option>Post-graduate</option></select></div>
              <div class="form-group"><label>PhilHealth Number</label><input type="text" v-model="form.head.philhealth" class="form-input" /></div>
            </div>
            <div class="form-row-2">
              <div class="form-group"><label>PhilHealth Category</label><input type="text" v-model="form.head.philhealthCategory" class="form-input" /></div>
              <div class="form-group"><label>4Ps Eligibility</label><select v-model="form.head.fourPs" class="form-input"><option value="">Select</option><option>No</option><option>Yes</option></select></div>
            </div>
            <div class="form-group"><label>Disability Status</label><input type="text" v-model="form.head.disability" placeholder="None or specify" class="form-input" /></div>
            <div class="form-group"><label>Medical History</label><textarea v-model="form.head.medicalHistory" class="form-textarea"></textarea></div>
            <div class="form-group"><label>Age/Health Risk Classification</label>
            <select v-model="form.head.healthRisk" class="form-input">
            <option value="">Select</option>
            <option>Early Childhood (0–4 y/o)</option>
            <option>School Age (5–9 y/o)</option>
            <option>Adolescent (10–19 y/o)</option>
            <option>Adult (20–59 y/o)</option>
            <option>Senior Citizen (60+ y/o)</option>
        </select>
        </div>
          </div>
          <div class="modal-section-header">WATER &amp; SANITATION</div>
          <div class="form-row-2"><div class="form-group"><label>Basic Safe Water Source</label><select v-model="form.basicWater" class="form-input"><option value="">Select</option><option>Yes</option><option>No</option></select></div><div class="form-group"><label>Safely Managed Water</label><select v-model="form.safeWater" class="form-input"><option value="">Select</option><option>Yes</option><option>No</option></select></div></div>
          <div class="form-row-2"><div class="form-group"><label>Sanitation Service</label><select v-model="form.sanitation" class="form-input"><option value="">Select</option><option>Yes</option><option>No</option></select></div><div class="form-group"><label>Safely Managed Sanitation</label><select v-model="form.safeSanitation" class="form-input"><option value="">Select</option><option>Yes</option><option>No</option></select></div></div>
          <div class="modal-section-header">RESIDENT INFORMATION</div>
          <div v-for="(resident, idx) in form.residents" :key="idx" class="resident-card">
            <div class="resident-card-header"><div class="resident-card-title">Resident {{ idx + 1 }}</div><button class="btn-remove-resident" @click="removeResident(idx)" v-if="form.residents.length > 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>Remove</button></div>
            <div class="form-group"><label>Full Name</label><input type="text" v-model="resident.fullName" placeholder="Dela Cruz, Juan, Santos" class="form-input" /></div>
            <div class="form-row-2"><div class="form-group"><label>Birthday</label><input type="date" v-model="resident.birthday" class="form-input" /></div><div class="form-group"><label>Age</label><input type="number" v-model="resident.age" class="form-input" /></div></div>
            <div class="form-row-2"><div class="form-group"><label>Sex</label><select v-model="resident.sex" class="form-input"><option value="">Select</option><option>Male</option><option>Female</option></select></div><div class="form-group"><label>Relation to Household Head</label><input type="text" v-model="resident.relation" placeholder="e.g., Head, Spouse, Child" class="form-input" /></div></div>
            <div class="form-row-2"><div class="form-group"><label>Occupation</label><input type="text" v-model="resident.occupation" class="form-input" /></div><div class="form-group"><label>Monthly Income</label><div class="input-prefix-wrap"><span class="input-prefix">₱</span><input type="number" v-model="resident.income" class="form-input with-prefix" /></div></div></div>
            <div class="form-row-2"><div class="form-group"><label>Educational Attainment</label><select v-model="resident.education" class="form-input"><option value="">Select</option><option>No formal education</option><option>Elementary</option><option>High School</option><option>Senior High School</option><option>College</option><option>Post-graduate</option></select></div><div class="form-group"><label>PhilHealth Number</label><input type="text" v-model="resident.philhealth" class="form-input" /></div></div>
            <div class="form-row-2"><div class="form-group"><label>PhilHealth Category</label><input type="text" v-model="resident.philhealthCategory" class="form-input" /></div><div class="form-group"><label>4Ps Eligibility</label><select v-model="resident.fourPs" class="form-input"><option value="">Select</option><option>No</option><option>Yes</option></select></div></div>
            <div class="form-group"><label>Disability Status</label><input type="text" v-model="resident.disability" placeholder="None or specify" class="form-input" /></div>
            <div class="form-group"><label>Medical History</label><textarea v-model="resident.medicalHistory" class="form-textarea"></textarea></div>
            <div class="form-group"><label>Health Risk Classification</label>
            <select v-model="newResident.healthRisk" class="form-input">
              <option value="">Select</option>
              <option>Early Childhood (0–4 y/o)</option>
              <option>School Age (5–9 y/o)</option>
              <option>Adolescent (10–19 y/o)</option>
              <option>Adult (20–59 y/o)</option>
              <option>Senior Citizen (60+ y/o)</option>
            </select>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn-cancel" @click="closeModal">Cancel</button>
          <button class="btn-primary" @click="saveAll" :disabled="saving">{{ saving ? 'Saving...' : 'Save All' }}</button>
        </div>
      </div>
    </div>

    <!-- ADD RESIDENT MODAL -->
    <div v-if="showAddResidentModal" class="modal-overlay" @click.self="showAddResidentModal = false">
      <div class="modal">
        <div class="modal-header">
          <div class="modal-title">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><line x1="20" y1="8" x2="20" y2="14"/><line x1="23" y1="11" x2="17" y2="11"/></svg>
            Add Resident — {{ addResidentTarget ? addResidentTarget.headName : '' }}
          </div>
          <button class="modal-close" @click="showAddResidentModal = false"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
        </div>
        <div class="modal-body">
          <div class="resident-card" style="margin-bottom:0;">
            <div class="form-group"><label>Full Name</label><input type="text" v-model="newResident.fullName" placeholder="Dela Cruz, Juan, Santos" class="form-input" /></div>
            <div class="form-row-2"><div class="form-group"><label>Birthday</label><input type="date" v-model="newResident.birthday" class="form-input" /></div><div class="form-group"><label>Age</label><input type="number" v-model="newResident.age" class="form-input" /></div></div>
            <div class="form-row-2"><div class="form-group"><label>Sex</label><select v-model="newResident.sex" class="form-input"><option value="">Select</option><option>Male</option><option>Female</option></select></div><div class="form-group"><label>Relation to Household Head</label><input type="text" v-model="newResident.relation" placeholder="e.g., Head, Spouse, Child" class="form-input" /></div></div>
            <div class="form-row-2"><div class="form-group"><label>Occupation</label><input type="text" v-model="newResident.occupation" class="form-input" /></div><div class="form-group"><label>Monthly Income</label><div class="input-prefix-wrap"><span class="input-prefix">₱</span><input type="number" v-model="newResident.income" class="form-input with-prefix" /></div></div></div>
            <div class="form-row-2"><div class="form-group"><label>Educational Attainment</label><select v-model="newResident.education" class="form-input"><option value="">Select</option><option>No formal education</option><option>Elementary</option><option>High School</option><option>Senior High School</option><option>College</option><option>Post-graduate</option></select></div><div class="form-group"><label>PhilHealth Number</label><input type="text" v-model="newResident.philhealth" class="form-input" /></div></div>
            <div class="form-row-2"><div class="form-group"><label>PhilHealth Category</label><input type="text" v-model="newResident.philhealthCategory" class="form-input" /></div><div class="form-group"><label>4Ps Eligibility</label><select v-model="newResident.fourPs" class="form-input"><option value="">Select</option><option>No</option><option>Yes</option></select></div></div>
            <div class="form-group"><label>Disability Status</label><input type="text" v-model="newResident.disability" placeholder="None or specify" class="form-input" /></div>
            <div class="form-group"><label>Medical History</label><textarea v-model="newResident.medicalHistory" class="form-textarea"></textarea></div>
            <div class="form-group"><label>Health Risk Classification</label>
            <select v-model="newResident.healthRisk" class="form-input">
              <option value="">Select</option>
              <option>Early Childhood (0–4 y/o)</option>
              <option>School Age (5–9 y/o)</option>
              <option>Adolescent (10–19 y/o)</option>
              <option>Adult (20–59 y/o)</option>
              <option>Senior Citizen (60+ y/o)</option>
            </select>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn-cancel" @click="showAddResidentModal = false">Cancel</button>
          <button class="btn-primary" @click="saveNewResident" :disabled="saving">{{ saving ? 'Saving...' : 'Add Resident' }}</button>
        </div>
      </div>
    </div>

    <!-- TRANSFER MODAL -->
    <div v-if="showTransferModal" class="modal-overlay" @click.self="showTransferModal = false">
      <div class="modal" style="max-width:440px;">
        <div class="modal-header">
          <div class="modal-title"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="18" height="18"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>Transfer Household</div>
          <button class="modal-close" @click="showTransferModal = false"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
        </div>
        <div class="modal-body">
          <p style="font-size:14px;color:#2a3e32;margin-bottom:16px;">Transfer <strong>{{ transferTarget ? transferTarget.headName : '' }}</strong> to another zone.</p>
          <div class="form-group"><label>Current Zone</label><div class="detail-value" style="font-size:14px;">Zone {{ transferTarget ? transferTarget.zone : '' }}</div></div>
          <div class="form-group"><label>Transfer to Zone No.</label><input type="text" v-model="transferToZone" class="form-input" placeholder="Enter destination zone number" /></div>
        </div>
        <div class="modal-footer">
          <button class="btn-cancel" @click="showTransferModal = false">Cancel</button>
          <button class="btn-primary" @click="confirmTransfer" :disabled="saving">{{ saving ? 'Transferring...' : 'Confirm Transfer' }}</button>
        </div>
      </div>
    </div>
     <!-- PROMOTE TO HEAD MODAL --> 
    <div v-if="showPromoteModal" class="modal-overlay" @click.self="showPromoteModal = false">
      <div class="modal" style="max-width:460px;">
        <div class="modal-header">
          <div class="modal-title">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="18" height="18">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>
              <polyline points="16 11 18 13 22 9"/>
            </svg>
          </div>
          <button class="modal-close" @click="showPromoteModal = false">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>
        <div class="modal-body">
          <p style="font-size:14px;color:#2a3e32;margin-bottom:18px;">
            <strong>{{ promotingResident ? promotingResident.full_name : '' }}</strong> will be registered as the head of a new household. They will be removed from the current household's resident list.
          </p>
          <div class="form-group">
            <label>New Household Zone</label>
            <input type="text" v-model="promoteNewZone" class="form-input" placeholder="Enter zone number" />
          </div>
          <div class="form-row-2">
            <div class="form-group">
              <label>No. of Families</label>
              <input type="number" v-model="promoteNewFamilies" class="form-input" min="1" />
            </div>
            <div class="form-group">
              <label>No. of Members</label>
              <input type="number" v-model="promoteNewMembers" class="form-input" min="1" />
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button class="btn-cancel" @click="showPromoteModal = false">Cancel</button>
          <button class="btn-primary" @click="confirmPromoteToHead" :disabled="saving">
            {{ saving ? 'Processing...' : 'Confirm' }}
          </button>
        </div>
      </div>
    </div>

    <!-- RESIDENT PROFILE MODAL -->
    <div v-if="showResidentProfile" class="modal-overlay" @click.self="showResidentProfile = false">
      <div class="modal" style="max-width:560px;">
        <div class="modal-header">
          <div class="modal-title"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="18" height="18"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>Resident Profile</div>
          <button class="modal-close" @click="showResidentProfile = false"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
        </div>
        <div class="modal-body" v-if="viewingResident">
          <div class="rp-avatar-row">
            <div class="rp-avatar">{{ viewingResident.full_name ? viewingResident.full_name.charAt(0).toUpperCase() : '?' }}</div>
            <div><div class="rp-name">{{ viewingResident.full_name }}</div><div class="rp-meta">{{ viewingResident.relation_to_head }} · {{ viewingResident.sex }} · Age {{ viewingResident.age }}</div></div>
          </div>
          <div class="rp-grid">
            <div class="rp-field"><div class="rp-label">Birthday</div><div class="rp-val">{{ viewingResident.birthday || '—' }}</div></div>
            <div class="rp-field"><div class="rp-label">Sex</div><div class="rp-val">{{ viewingResident.sex || '—' }}</div></div>
            <div class="rp-field"><div class="rp-label">Occupation</div><div class="rp-val">{{ viewingResident.occupation || '—' }}</div></div>
            <div class="rp-field"><div class="rp-label">Monthly Income</div><div class="rp-val">{{ viewingResident.monthly_income ? '₱' + viewingResident.monthly_income : '—' }}</div></div>
            <div class="rp-field"><div class="rp-label">Education</div><div class="rp-val">{{ viewingResident.education || '—' }}</div></div>
            <div class="rp-field"><div class="rp-label">PhilHealth No.</div><div class="rp-val">{{ viewingResident.philhealth_number || '—' }}</div></div>
            <div class="rp-field"><div class="rp-label">PhilHealth Category</div><div class="rp-val">{{ viewingResident.philhealth_category || '—' }}</div></div>
            <div class="rp-field"><div class="rp-label">4Ps</div><div class="rp-val"><span class="badge" :class="viewingResident.four_ps === 'Yes' ? 'badge-safe' : 'badge-no'">{{ viewingResident.four_ps || '—' }}</span></div></div>
            <div class="rp-field" style="grid-column:1/-1"><div class="rp-label">Disability</div><div class="rp-val">{{ viewingResident.disability || 'None' }}</div></div>
            <div class="rp-field" style="grid-column:1/-1"><div class="rp-label">Medical History</div><div class="rp-val">{{ viewingResident.medical_history || '—' }}</div></div>
            <div class="rp-field" style="grid-column:1/-1"><div class="rp-label">Health Risk Classification</div><div class="rp-val">{{ viewingResident.health_risk || '—' }}</div></div>
          </div>
        </div>
        <div class="modal-footer"><button class="btn-cancel" @click="showResidentProfile = false">Close</button></div>
      </div>
    </div>

    <!-- EDIT BARANGAY MODAL -->
    <div v-if="showEditBarangay" class="modal-overlay" @click.self="showEditBarangay = false">
      <div class="modal" style="max-width:560px;">
        <div class="modal-header">
          <div class="modal-title"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="18" height="18"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>Edit Barangay Info</div>
          <button class="modal-close" @click="showEditBarangay = false"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
        </div>
        <div class="modal-body">
          <div class="modal-section-header">LOCATION &amp; CLASSIFICATION</div>
          <div class="form-row-2"><div class="form-group"><label>Barangay Name</label><input type="text" v-model="barangay.name" class="form-input" /></div><div class="form-group"><label>Municipality</label><input type="text" v-model="barangay.municipality" class="form-input" /></div></div>
          <div class="form-row-2"><div class="form-group"><label>Province</label><input type="text" v-model="barangay.province" class="form-input" /></div><div class="form-group"><label>Region</label><input type="text" v-model="barangay.region" class="form-input" /></div></div>
          <div class="form-row-2"><div class="form-group"><label>Classification</label><input type="text" v-model="barangay.classification" class="form-input" /></div><div class="form-group"><label>PSGC Code</label><input type="text" v-model="barangay.psgcCode" class="form-input" /></div></div>
          <div class="form-row-2"><div class="form-group"><label>Postal Code</label><input type="text" v-model="barangay.postalCode" class="form-input" /></div><div class="form-group"><label>Population</label><input type="text" v-model="barangay.population" class="form-input" /></div></div>
          <div class="modal-section-header">CONTACT &amp; ADMINISTRATION</div>
          <div class="form-row-2"><div class="form-group"><label>Punong Barangay</label><input type="text" v-model="barangay.captain" class="form-input" /></div><div class="form-group"><label>Contact Number</label><input type="text" v-model="barangay.contactNumber" class="form-input" /></div></div>
          <div class="form-group"><label>Email Address</label><input type="text" v-model="barangay.email" class="form-input" /></div>
          <div class="form-group"><label>Office Hours</label><input type="text" v-model="barangay.officeHours" class="form-input" /></div>
          <div class="form-group"><label>Barangay Hall Address</label><input type="text" v-model="barangay.hallAddress" class="form-input" /></div>
        </div>
        <div class="modal-footer">
          <button class="btn-cancel" @click="showEditBarangay = false">Cancel</button>
          <button class="btn-primary" @click="showEditBarangay = false; showToast('Barangay info updated!')">Save Changes</button>
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
      logoUrl: localStorage.getItem('logo_url') || '',
      currentPage: 'dashboard',
      selectedHousehold: null,
      viewingZone: null,
      showModal: false,
      modalMode: 'add',
      householdSearch: '',
      loadingHouseholds: false,
      saving: false,
      savingName: false,
      zoneSortBy: 'households',
      zoneSortDir: 'asc',
      stats: { households: 0, residents: 0, children: 0, seniors: 0, pwd: 0 },
      households: [],
      form: this.blankForm(),
      userName: localStorage.getItem('user_name') || 'Admin',
      userEmail: localStorage.getItem('user_email') || '',
      toast: { show: false, message: '', type: 'success' },
      showUserMenu: false,
      showEditName: false,
      editNameValue: '',
      barangay: {
        name: 'Tampadong',
        municipality: 'Pamplona',
        province: 'Camarines Sur',
        region: 'Bicol Region (Region V)',
        classification: 'Rural',
        psgcCode: '0501726018',
        postalCode: '4416',
        population: '2,502',
        captain: 'Agnes Miranda Rosana',
        contactNumber: '0938 517 4155',
        email: 'blgutampadongofficial@gmail.com',
        officeHours: 'Mon–Fri, 8:00 AM – 5:00 PM',
        hallAddress: 'Barangay Tampadong, Pamplona, Camarines Sur, Philippines',
      },
      showEditBarangay: false,
      globalSearchQuery: '',
      showSearchResults: false,
      residentSearch: '',
      residentSortBy: 'name',
      residentSortDir: 'asc',
      residentListSearch: '',
      residentListZone: '',
      residentListSortBy: 'name',
      residentListSortDir: 'asc',
      showResidentProfile: false,
      viewingResident: null,
      openActionsId: null,
      openActionsId: null,
      openResidentActionsId: null,
      showPromoteModal: false,
      promotingResident: null,
      promoteNewZone: '',
      promoteNewFamilies: 1,
      promoteNewMembers: 1,
      showAddResidentModal: false,
      addResidentTarget: null,
      newResident: this.blankResident(),
      showTransferModal: false,
      transferTarget: null,
      transferToZone: '',
    }
  },
  computed: {
    userInitials() { return this.userName.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2) },
    filteredHouseholds() {
      let list = this.viewingZone ? this.households.filter(h => String(h.zone) === String(this.viewingZone)) : this.households
      const q = this.householdSearch.toLowerCase()
      if (!q) return list
      return list.filter(h => h.headName.toLowerCase().includes(q) || String(h.zone).toLowerCase().includes(q))
    },
    filteredResidents() {
      if (!this.selectedHousehold || !this.selectedHousehold.residents) return []
      let list = [...this.selectedHousehold.residents]
      const q = this.residentSearch.trim().toLowerCase()
      if (q) list = list.filter(r => (r.full_name || '').toLowerCase().includes(q) || (r.occupation || '').toLowerCase().includes(q) || (r.relation_to_head || '').toLowerCase().includes(q))
      list.sort((a, b) => {
        let av = this.residentSortBy === 'age' ? Number(a.age) || 0 : this.residentSortBy === 'relation' ? (a.relation_to_head || '') : (a.full_name || '')
        let bv = this.residentSortBy === 'age' ? Number(b.age) || 0 : this.residentSortBy === 'relation' ? (b.relation_to_head || '') : (b.full_name || '')
        if (av < bv) return this.residentSortDir === 'asc' ? -1 : 1
        if (av > bv) return this.residentSortDir === 'asc' ? 1 : -1
        return 0
      })
      return list
    },
    globalSearchResults() {
      const q = this.globalSearchQuery.trim().toLowerCase()
      if (!q) return []
      const results = []
      this.households.forEach(h => {
        (h.residents || []).forEach((r, idx) => {
          if ((r.full_name || '').toLowerCase().includes(q) || (h.headName || '').toLowerCase().includes(q)) {
            results.push({ residentId: h.id + '-' + idx, householdId: h.id, residentName: r.full_name || '', householdHead: h.headName || '', zone: h.zone, sex: r.sex || '', age: r.age || '', relation: r.relation_to_head || '' })
          }
        })
      })
      return results.slice(0, 20)
    },
    availableZones() {
      return [...new Set(this.households.map(h => String(h.zone)))].sort()
    },
    allResidents() {
  const q = this.residentListSearch.trim().toLowerCase()
  const zoneFilter = this.residentListZone
  let list = []
  this.households.forEach(h => {
    const passesZone = !zoneFilter || String(h.zone) === String(zoneFilter)
    if (passesZone) {
      const headEntry = {
        full_name: h.headName || '—',
        sex: h.headSex || '—',
        age: h.headAge || '—',
        birthday: h.headBirthday || '—',
        relation_to_head: 'Head',
        occupation: h.headOccupation || '—',
        monthly_income: h.headIncome || '',
        education: h.headEducation || '—',
        philhealth_number: h.headPhilhealth || '—',
        philhealth_category: h.headPhilhealthCategory || '—',
        four_ps: h.headFourPs || '—',
        disability: h.headDisability || 'None',
        medical_history: h.headMedicalHistory || '—',
        health_risk: h.headHealthRisk || '—',
        householdHead: h.headName,
        zone: h.zone,
        householdId: h.id,
      }
      if (!q || (headEntry.full_name || '').toLowerCase().includes(q) || 'head'.includes(q)) {
        list.push(headEntry)
      }
    }
    ;(h.residents || []).forEach(r => {
      if (!passesZone) return
      if (q && !(
        (r.full_name || '').toLowerCase().includes(q) ||
        (r.occupation || '').toLowerCase().includes(q) ||
        (r.relation_to_head || '').toLowerCase().includes(q)
      )) return
      list.push({ ...r, householdHead: h.headName, zone: h.zone, householdId: h.id })
    })
  })
  list.sort((a, b) => {
    let av = this.residentListSortBy === 'age' ? Number(a.age) || 0
      : this.residentListSortBy === 'zone' ? String(a.zone)
      : (a.full_name || '')
    let bv = this.residentListSortBy === 'age' ? Number(b.age) || 0
      : this.residentListSortBy === 'zone' ? String(b.zone)
      : (b.full_name || '')
    if (av < bv) return this.residentListSortDir === 'asc' ? -1 : 1
    if (av > bv) return this.residentListSortDir === 'asc' ? 1 : -1
    return 0
  })
  return list
},
    waterSummary() {
      const total = this.households.length
      if (!total) return { safe: 0, basic: 0, limited: 0 }
      const safe = this.households.filter(h => h.basicWater === 'Yes' && h.safeWater === 'Yes').length
      const basic = this.households.filter(h => h.basicWater === 'Yes' && h.safeWater !== 'Yes').length
      const limited = total - safe - basic
      return {
        safe: Math.round((safe / total) * 100),
        basic: Math.round((basic / total) * 100),
        limited: Math.round((limited / total) * 100),
      }
    },
    sanitationSummary() {
      const total = this.households.length
      if (!total) return { good: 0, basic: 0, poor: 0 }
      const good = this.households.filter(h => h.sanitation === 'Good' || (h.sanitation === 'Yes' && h.safeSanitation === 'Yes')).length
      const basic = this.households.filter(h => h.sanitation === 'Basic' || (h.sanitation === 'Yes' && h.safeSanitation !== 'Yes')).length
      const poor = total - good - basic
      return {
        good: Math.round((good / total) * 100),
        basic: Math.round((basic / total) * 100),
        poor: Math.round((poor / total) * 100),
      }
    },
    zoneGroups() {
      const map = {}
      this.households.forEach(h => {
        const z = h.zone
        if (!map[z]) map[z] = { zone: z, households: 0, population: 0, waterStatus: h.waterStatus || 'Safe', sanitationStatus: h.sanitationStatus || 'Good' }
        map[z].households++
        map[z].population += Number(h.members) || 0
      })
      return Object.values(map)
    },
    sortedZones() {
      return [...this.zoneGroups].sort((a, b) => {
        let av = this.zoneSortBy === 'zone' ? a.zone : this.zoneSortBy === 'population' ? a.population : a.households
        let bv = this.zoneSortBy === 'zone' ? b.zone : this.zoneSortBy === 'population' ? b.population : b.households
        if (av < bv) return this.zoneSortDir === 'asc' ? -1 : 1
        if (av > bv) return this.zoneSortDir === 'asc' ? 1 : -1
        return 0
      })
    },
  },
  mounted() {
    this.userName = localStorage.getItem('user_name') || 'Admin'
    this.userEmail = localStorage.getItem('user_email') || ''
    this.loadData()
    document.addEventListener('click', (e) => {
      if (this.$refs.userBadge && !this.$refs.userBadge.contains(e.target)) this.showUserMenu = false
      if (this.$refs.globalSearchWrap && !this.$refs.globalSearchWrap.contains(e.target)) this.showSearchResults = false
      this.openActionsId = null
      this.openResidentActionsId = null
    })
  },
  methods: {
    async loadData() {
      this.loadingHouseholds = true
      try { const [s, h] = await Promise.all([getStats(), getHouseholds()]); this.stats = s; this.households = h }
      catch (err) { console.error('Failed to load data:', err) }
      finally { this.loadingHouseholds = false }
    },
    blankForm() { return { zone: '', lastName: '', firstName: '', middleName: '', families: '', membersCount: '', basicWater: '', safeWater: '', sanitation: '', safeSanitation: '', head: { birthday: '', age: '', sex: '', civilStatus: '', occupation: '', income: '', education: '', philhealth: '', philhealthCategory: '', fourPs: 'No', disability: '', medicalHistory: '', healthRisk: '' }, residents: [this.blankResident()] } },
    blankResident() { return { fullName: '', birthday: '', age: '', sex: 'Male', relation: '', occupation: '', income: '', education: '', philhealth: '', philhealthCategory: '', fourPs: 'No', disability: '', medicalHistory: '', healthRisk: '' } },
    openResidentProfile(r) { this.viewingResident = r; this.showResidentProfile = true },
    highlightMatch(text, query) {
      if (!query || !text) return text
      const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
      return text.replace(new RegExp(`(${escaped})`, 'gi'), '<mark>$1</mark>')
    },
    viewHouseholdFromSearch(result) {
      const h = this.households.find(hh => hh.id === result.householdId)
      if (h) { this.globalSearchQuery = ''; this.showSearchResults = false; this.viewHousehold(h) }
    },
    toggleActions(id) { this.openActionsId = this.openActionsId === id ? null : id },
    toggleResidentActions(id) { this.openResidentActionsId = this.openResidentActionsId === id ? null : id },
    promoteToHead(r) {
    this.openResidentActionsId = null
    this.promotingResident = r
    this.promoteNewZone = this.selectedHousehold ? String(this.selectedHousehold.zone) : ''
    this.promoteNewFamilies = 1
    this.promoteNewMembers = 1
    this.showPromoteModal = true
    },
    async confirmPromoteToHead() {
    if (!this.promoteNewZone.trim()) {
      this.showToast('Please enter a zone number for the new household.', 'error')
    return
  }
    this.saving = true
  try {
    const nameParts = (this.promotingResident.full_name || '').split(',').map(s => s.trim())
    const newHousehold = {
      zone: this.promoteNewZone.trim(),
      lastName: nameParts[0] || '',
      firstName: nameParts[1] || '',
      middleName: nameParts[2] || '',
      families: this.promoteNewFamilies,
      membersCount: this.promoteNewMembers,
      basicWater: '',
      safeWater: '',
      sanitation: '',
      safeSanitation: '',
      head: {
        birthday: this.promotingResident.birthday || '',
        age: this.promotingResident.age || '',
        sex: this.promotingResident.sex || '',
        civilStatus: this.promotingResident.civil_status || '',
        occupation: this.promotingResident.occupation || '',
        income: this.promotingResident.monthly_income || '',
        education: this.promotingResident.education || '',
        philhealth: this.promotingResident.philhealth_number || '',
        philhealthCategory: this.promotingResident.philhealth_category || '',
        fourPs: this.promotingResident.four_ps || 'No',
        disability: this.promotingResident.disability || '',
        medicalHistory: this.promotingResident.medical_history || '',
        healthRisk: this.promotingResident.health_risk || '',
      },
      residents: [],
    }
    await addHousehold(newHousehold)

    const remaining = (this.selectedHousehold.residents || [])
      .filter(res => res.full_name !== this.promotingResident.full_name)
      .map(res => ({
        fullName: res.full_name, birthday: res.birthday, age: res.age,
        sex: res.sex, relation: res.relation_to_head, occupation: res.occupation,
        income: res.monthly_income, education: res.education,
        philhealth: res.philhealth_number, philhealthCategory: res.philhealth_category,
        fourPs: res.four_ps, disability: res.disability,
        medicalHistory: res.medical_history, healthRisk: res.health_risk,
      }))

    await updateHousehold(this.selectedHousehold.id, {
      zone: this.selectedHousehold.zone,
      lastName: this.selectedHousehold.lastName || '',
      firstName: this.selectedHousehold.firstName || '',
      middleName: this.selectedHousehold.middleName || '',
      families: this.selectedHousehold.families,
      membersCount: remaining.length,
      basicWater: this.selectedHousehold.basicWater || '',
      safeWater: this.selectedHousehold.safeWater || '',
      sanitation: this.selectedHousehold.sanitation || '',
      safeSanitation: this.selectedHousehold.safeSanitation || '',
      residents: remaining,
    })

    await this.loadData()
    this.selectedHousehold = this.households.find(h => h.id === this.selectedHousehold.id)
    this.showPromoteModal = false
    this.showToast(`${this.promotingResident.full_name} is now a Household Head in Zone ${this.promoteNewZone}!`)
  } catch (err) {
    this.showToast('Error promoting resident: ' + err.message, 'error')
  } finally {
    this.saving = false
  }
  },
    viewHousehold(h) { this.openActionsId = null; this.selectedHousehold = h; this.currentPage = 'household-detail' },
    openEditModalFor(h) { this.openActionsId = null; this.selectedHousehold = h; this.openEditModal() },
    openEditModal() {
      this.modalMode = 'edit'
      if (this.selectedHousehold) {
        this.form = {
          zone: this.selectedHousehold.zone, lastName: this.selectedHousehold.lastName || '', firstName: this.selectedHousehold.firstName || '', middleName: this.selectedHousehold.middleName || '',
          families: this.selectedHousehold.families, membersCount: this.selectedHousehold.members,
          basicWater: this.selectedHousehold.basicWater || '', safeWater: this.selectedHousehold.safeWater || '', sanitation: this.selectedHousehold.sanitation || '', safeSanitation: this.selectedHousehold.safeSanitation || '',
          head: {
            birthday: this.selectedHousehold.headBirthday || '',
            age: this.selectedHousehold.headAge || '',
            sex: this.selectedHousehold.headSex || '',
            civilStatus: this.selectedHousehold.headCivilStatus || '',
            occupation: this.selectedHousehold.headOccupation || '',
            income: this.selectedHousehold.headIncome || '',
            education: this.selectedHousehold.headEducation || '',
            philhealth: this.selectedHousehold.headPhilhealth || '',
            philhealthCategory: this.selectedHousehold.headPhilhealthCategory || '',
            fourPs: this.selectedHousehold.headFourPs || 'No',
            disability: this.selectedHousehold.headDisability || '',
            medicalHistory: this.selectedHousehold.headMedicalHistory || '',
            healthRisk: this.selectedHousehold.headHealthRisk || '',
          },
          residents: this.selectedHousehold.residents && this.selectedHousehold.residents.length
            ? this.selectedHousehold.residents.map(r => ({ fullName: r.full_name, birthday: r.birthday, age: r.age, sex: r.sex, relation: r.relation_to_head, occupation: r.occupation, income: r.monthly_income, education: r.education, philhealth: r.philhealth_number, philhealthCategory: r.philhealth_category, fourPs: r.four_ps, disability: r.disability, medicalHistory: r.medical_history, healthRisk: r.health_risk }))
            : [this.blankResident()],
        }
      }
      this.showModal = true
    },
    openAddResidentFor(h) { this.openActionsId = null; this.addResidentTarget = h; this.newResident = this.blankResident(); this.showAddResidentModal = true },
    async saveNewResident() {
      if (!this.newResident.fullName.trim()) { this.showToast('Please enter the resident\'s full name.', 'error'); return }
      this.saving = true
      try {
        const existing = (this.addResidentTarget.residents || []).map(r => ({ fullName: r.full_name, birthday: r.birthday, age: r.age, sex: r.sex, relation: r.relation_to_head, occupation: r.occupation, income: r.monthly_income, education: r.education, philhealth: r.philhealth_number, philhealthCategory: r.philhealth_category, fourPs: r.four_ps, disability: r.disability, medicalHistory: r.medical_history, healthRisk: r.health_risk }))
        await updateHousehold(this.addResidentTarget.id, { zone: this.addResidentTarget.zone, lastName: this.addResidentTarget.lastName || '', firstName: this.addResidentTarget.firstName || '', middleName: this.addResidentTarget.middleName || '', families: this.addResidentTarget.families, membersCount: this.addResidentTarget.members, basicWater: this.addResidentTarget.basicWater || '', safeWater: this.addResidentTarget.safeWater || '', sanitation: this.addResidentTarget.sanitation || '', safeSanitation: this.addResidentTarget.safeSanitation || '', residents: [...existing, this.newResident] })
        await this.loadData()
        if (this.selectedHousehold && this.selectedHousehold.id === this.addResidentTarget.id) this.selectedHousehold = this.households.find(h => h.id === this.addResidentTarget.id)
        this.showAddResidentModal = false; this.showToast('Resident added successfully!')
      } catch (err) { this.showToast('Error adding resident: ' + err.message, 'error') }
      finally { this.saving = false }
    },
    openTransferFor(h) { this.openActionsId = null; this.transferTarget = h; this.transferToZone = ''; this.showTransferModal = true },
    async confirmTransfer() {
      if (!this.transferToZone.trim()) { this.showToast('Please enter the destination zone.', 'error'); return }
      if (String(this.transferToZone).trim() === String(this.transferTarget.zone)) { this.showToast('Household is already in this zone.', 'error'); return }
      this.saving = true
      try {
        await updateHousehold(this.transferTarget.id, { zone: this.transferToZone.trim(), lastName: this.transferTarget.lastName || '', firstName: this.transferTarget.firstName || '', middleName: this.transferTarget.middleName || '', families: this.transferTarget.families, membersCount: this.transferTarget.members, basicWater: this.transferTarget.basicWater || '', safeWater: this.transferTarget.safeWater || '', sanitation: this.transferTarget.sanitation || '', safeSanitation: this.transferTarget.safeSanitation || '', residents: (this.transferTarget.residents || []).map(r => ({ fullName: r.full_name, birthday: r.birthday, age: r.age, sex: r.sex, relation: r.relation_to_head, occupation: r.occupation, income: r.monthly_income, education: r.education, philhealth: r.philhealth_number, philhealthCategory: r.philhealth_category, fourPs: r.four_ps, disability: r.disability, medicalHistory: r.medical_history, healthRisk: r.health_risk })) })
        await this.loadData(); this.showTransferModal = false; this.showToast(`Household transferred to Zone ${this.transferToZone} successfully!`)
      } catch (err) { this.showToast('Error transferring: ' + err.message, 'error') }
      finally { this.saving = false }
    },
    async deleteHouseholdById(h) {
      this.openActionsId = null
      if (confirm(`Delete household of ${h.headName}? This cannot be undone.`)) {
        try { await deleteHousehold(h.id); await this.loadData(); this.showToast('Household deleted successfully!') }
        catch (err) { this.showToast('Error deleting: ' + err.message, 'error') }
      }
    },
    async deleteHousehold() {
      if (confirm('Are you sure you want to delete this household?')) {
        try { await deleteHousehold(this.selectedHousehold.id); await this.loadData(); this.selectedHousehold = null; this.currentPage = 'households'; this.showToast('Household deleted successfully!') }
        catch (err) { this.showToast('Error deleting: ' + err.message, 'error') }
      }
    },
    openAddModal() { this.modalMode = 'add'; this.form = this.blankForm(); if (this.viewingZone) this.form.zone = this.viewingZone; this.showModal = true },
    closeModal() { this.showModal = false },
    addResident() { this.form.residents.push(this.blankResident()) },
    removeResident(idx) { this.form.residents.splice(idx, 1) },
    async saveAll() {
      this.saving = true
      try {
        if (this.modalMode === 'add') { await addHousehold(this.form); this.showToast('Household added successfully!') }
        else if (this.modalMode === 'edit' && this.selectedHousehold) { await updateHousehold(this.selectedHousehold.id, this.form); this.showToast('Household updated successfully!') }
        await this.loadData()
        if (this.modalMode === 'edit') this.selectedHousehold = this.households.find(h => h.id === this.selectedHousehold.id)
        this.closeModal()
      } catch (err) { this.showToast('Error saving: ' + err.message, 'error') }
      finally { this.saving = false }
    },
    viewZone(zone) { this.viewingZone = zone; this.householdSearch = zone; this.currentPage = 'households' },
    editZone(zone) { const h = this.households.find(hh => hh.zone === zone.zone); if (h) this.viewHousehold(h) },
    async deleteZone(zone) {
      if (confirm(`Delete ALL households in Zone ${zone}? This cannot be undone.`)) {
        try { await Promise.all(this.households.filter(h => h.zone === zone).map(h => deleteHousehold(h.id))); await this.loadData(); this.showToast(`Zone ${zone} deleted successfully!`) }
        catch (err) { this.showToast('Error deleting zone: ' + err.message, 'error') }
      }
    },
    showToast(message, type = 'success') { this.toast = { show: true, message, type }; setTimeout(() => { this.toast.show = false }, 3000) },
    toggleUserMenu() { this.showUserMenu = !this.showUserMenu; if (this.showUserMenu) { this.showEditName = false; this.editNameValue = this.userName } },
    async saveName() {
      if (!this.editNameValue.trim()) return
      this.savingName = true
      try { await updateUserName(this.userEmail, this.editNameValue.trim()); this.userName = this.editNameValue.trim(); localStorage.setItem('user_name', this.userName); this.showEditName = false; this.showToast('Name updated successfully!') }
      catch (err) { this.showToast('Error updating name: ' + err.message, 'error') }
      finally { this.savingName = false }
    },
    getWaterClass(s) { if (!s) return 'zone-badge-safe'; s = s.toLowerCase(); return s === 'safe' ? 'zone-badge-safe' : s === 'basic' ? 'zone-badge-basic' : 'zone-badge-limited' },
    getSanitationClass(s) { if (!s) return 'zone-badge-good'; s = s.toLowerCase(); return s === 'good' ? 'zone-badge-good' : s === 'basic' ? 'zone-badge-basic' : 'zone-badge-limited' },
    logout() {
      this.showUserMenu = false
      if (confirm('Are you sure you want to logout?')) { localStorage.removeItem('isLoggedIn'); localStorage.removeItem('user_email'); localStorage.removeItem('user_name'); this.router.push('/login') }
    },
  },
}
</script>

<style scoped>
* { box-sizing: border-box; margin: 0; padding: 0; }
.hhp-app { display: flex; height: 100vh; font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; background: #f4f6f5; color: #1a2e25; }
.sidebar { width: 150px; background: #1a4a35; display: flex; flex-direction: column; align-items: center; padding: 20px 0; flex-shrink: 0; }
.sidebar-logo { width: 64px; height: 64px; border-radius: 50%; overflow: hidden; display: flex; align-items: center; justify-content: center; margin-bottom: 24px; flex-shrink: 0; }
.logo-img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }
.logo-text { font-weight: 800; font-size: 16px; color: #1a4a35; }
.sidebar-nav { display: flex; flex-direction: column; gap: 4px; width: 100%; padding: 0 10px; }
.nav-item { display: flex; flex-direction: column; align-items: center; gap: 6px; padding: 14px 8px; border-radius: 12px; border: none; background: transparent; color: rgba(255,255,255,0.6); cursor: pointer; font-size: 12px; font-weight: 500; transition: all 0.2s; width: 100%; }
.nav-item svg { width: 22px; height: 22px; }
.nav-item:hover { background: rgba(255,255,255,0.1); color: #fff; }
.nav-item.active { background: #2d6e50; color: #fff; }
.main-content { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.topbar { display: flex; align-items: center; justify-content: space-between; padding: 16px 32px; background: #fff; border-bottom: 1px solid #e8eeeb; }
.page-title { font-size: 18px; font-weight: 700; color: #1a2e25; }
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
.stats-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 0; margin-bottom: 28px; background: #fff; border-radius: 14px; border: 1px solid #e8eeeb; overflow: hidden; }
.stat-card { padding: 20px 24px; display: flex; flex-direction: column; gap: 6px; border-right: 1px solid #e8eeeb; background: #fff; }
.stat-card:last-child { border-right: none; }
.stat-label { font-size: 12px; color: #7a9989; font-weight: 500; }
.stat-value { font-size: 32px; font-weight: 800; color: #1a2e25; line-height: 1.1; }
.zone-overview-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; }
.zone-overview-title { font-size: 18px; font-weight: 700; color: #1a2e25; }
.zone-overview-sub { font-size: 12.5px; color: #8aab99; margin-top: 4px; }
.zone-overview-controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.sort-label { font-size: 13px; color: #5a7a6a; font-weight: 500; }
.sort-select { padding: 8px 12px; border: 1.5px solid #dde6e2; border-radius: 8px; font-size: 13px; color: #1a2e25; background: #fff; outline: none; cursor: pointer; }
.btn-add-zone { display: flex; align-items: center; gap: 6px; background: #1a4a35; color: #fff; border: none; border-radius: 8px; padding: 9px 18px; font-size: 13.5px; font-weight: 700; cursor: pointer; transition: background 0.2s; }
.btn-add-zone svg { width: 15px; height: 15px; }
.btn-add-zone:hover { background: #0f3326; }
.zone-cards-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }
.zone-empty { grid-column: 1 / -1; text-align: center; color: #8aab99; padding: 48px; font-size: 14px; background: #fff; border-radius: 14px; border: 1px solid #e8eeeb; }
.zone-card { background: #fff; border-radius: 14px; border: 1px solid #e8eeeb; overflow: hidden; display: flex; flex-direction: column; }
.zone-card-header { background: #1a4a35; color: #fff; padding: 14px 18px; font-size: 16px; font-weight: 700; }
.zone-card-body { padding: 18px; display: flex; flex-direction: column; gap: 14px; flex: 1; }
.zone-stat-row { display: flex; gap: 32px; }
.zone-stat { display: flex; flex-direction: column; gap: 2px; }
.zone-stat-label { font-size: 10px; font-weight: 700; color: #8aab99; letter-spacing: 0.5px; text-transform: uppercase; }
.zone-stat-value { font-size: 28px; font-weight: 800; color: #1a2e25; line-height: 1.1; }
.zone-stat-sub { font-size: 11px; color: #8aab99; }
.zone-badges-row { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }
.zone-badge-label { font-size: 13px; color: #2a3e32; font-weight: 500; }
.zone-status-badge { display: inline-block; padding: 3px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; }
.zone-badge-safe { background: #d4f0e4; color: #1a6b42; }
.zone-badge-good { background: #d4f0e4; color: #1a6b42; }
.zone-badge-basic { background: #fef3cd; color: #856404; }
.zone-badge-limited { background: #fde8e8; color: #c0392b; }
.zone-card-actions { display: flex; align-items: center; gap: 8px; margin-top: 4px; }
.btn-view-zone { background: #1a4a35; color: #fff; border: none; border-radius: 8px; padding: 9px 0; font-size: 13px; font-weight: 600; cursor: pointer; transition: background 0.2s; flex: 1; }
.btn-view-zone:hover { background: #0f3326; }
.btn-zone-edit { background: #fff; color: #2a3e32; border: 1.5px solid #ccd9d3; border-radius: 8px; padding: 8px 14px; font-size: 13px; font-weight: 500; cursor: pointer; transition: all 0.2s; }
.btn-zone-edit:hover { border-color: #1a4a35; color: #1a4a35; }
.btn-zone-delete { background: #fff; color: #c0392b; border: 1.5px solid #e8b4b0; border-radius: 8px; padding: 8px 14px; font-size: 13px; font-weight: 500; cursor: pointer; transition: all 0.2s; }
.btn-zone-delete:hover { background: #fdf0ef; border-color: #c0392b; }
.loading-state { text-align: center; padding: 48px; color: #8aab99; font-size: 14px; background: #fff; border-radius: 14px; border: 1px solid #e8eeeb; }
.table-section { background: #fff; border-radius: 14px; border: 1px solid #e8eeeb; padding: 20px; }
.table-toolbar { display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; }
.data-table { width: 100%; border-collapse: collapse; font-size: 13.5px; }
.data-table th { text-align: left; padding: 10px 14px; font-size: 12.5px; font-weight: 600; color: #5a7a6a; background: #f4f8f6; border-bottom: 1px solid #e8eeeb; }
.data-table td { padding: 14px 14px; border-bottom: 1px solid #f0f4f2; color: #2a3e32; vertical-align: middle; }
.data-table tbody tr:last-child td { border-bottom: none; }
.data-table tbody tr:hover td { background: #f8faf9; }
.badge { display: inline-block; padding: 3px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; }
.badge-safe { background: #d4f0e4; color: #1a6b42; }
.badge-basic { background: #fef3cd; color: #856404; }
.badge-no { background: #f0f0f0; color: #666; }
.act-wrap { position: relative; display: inline-block; }
.btn-act { display: inline-flex; align-items: center; gap: 6px; background: #fff; border: 1.5px solid #ccd9d3; border-radius: 8px; padding: 7px 14px; font-size: 13px; font-weight: 600; color: #2a3e32; cursor: pointer; transition: all 0.15s; white-space: nowrap; }
.btn-act:hover, .btn-act.open { border-color: #1a4a35; color: #1a4a35; background: #f4f8f6; }
.act-menu { position: absolute; right: 0; top: calc(100% + 5px); background: #fff; border: 1px solid #e8eeeb; border-radius: 10px; box-shadow: 0 8px 28px rgba(0,0,0,0.13); min-width: 185px; z-index: 300; overflow: hidden; }
.act-item { display: flex; align-items: center; gap: 10px; padding: 11px 16px; font-size: 13.5px; font-weight: 500; color: #2a3e32; cursor: pointer; transition: background 0.12s; }
.act-item:hover { background: #f4f8f6; }
.act-item svg { flex-shrink: 0; color: #5a7a6a; }
.act-divider { height: 1px; background: #e8eeeb; margin: 4px 0; }
.act-danger { color: #c0392b; }
.act-danger svg { color: #c0392b; }
.act-danger:hover { background: #fdf0ef; }
.btn-primary { display: flex; align-items: center; gap: 7px; background: #1a4a35; color: #fff; border: none; border-radius: 8px; padding: 10px 18px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: background 0.2s; white-space: nowrap; }
.btn-primary svg { width: 15px; height: 15px; }
.btn-primary:hover:not(:disabled) { background: #0f3326; }
.btn-primary:disabled { opacity: 0.6; cursor: not-allowed; }
.btn-secondary { display: flex; align-items: center; gap: 7px; background: #fff; color: #1a4a35; border: 1.5px solid #1a4a35; border-radius: 8px; padding: 9px 18px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: all 0.2s; white-space: nowrap; }
.btn-secondary:hover { background: #e8f5ee; }
.btn-danger { display: flex; align-items: center; gap: 7px; background: #c0392b; color: #fff; border: none; border-radius: 8px; padding: 10px 18px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: background 0.2s; white-space: nowrap; }
.btn-danger svg { width: 15px; height: 15px; }
.btn-danger:hover { background: #992d22; }
.btn-cancel { background: #fff; color: #1a2e25; border: 1.5px solid #ccd9d3; border-radius: 8px; padding: 10px 22px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: all 0.2s; }
.btn-cancel:hover { background: #f4f6f5; }
.detail-back { display: flex; align-items: center; gap: 6px; font-size: 13.5px; color: #2d6e50; font-weight: 600; cursor: pointer; margin-bottom: 16px; width: fit-content; }
.detail-back svg { width: 18px; height: 18px; }
.detail-back:hover { color: #1a4a35; }
.detail-value { font-size: 14px; color: #1a2e25; font-weight: 500; background: #f8faf9; padding: 10px 14px; border-radius: 8px; border: 1px solid #e8eeeb; }
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
.modal-footer { padding: 16px 24px; border-top: 1px solid #e8eeeb; display: flex; justify-content: flex-end; gap: 12px; flex-shrink: 0; background: #fafcfb; border-radius: 0 0 16px 16px; }
.empty-state { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; height: 300px; color: #8aab99; }
.empty-state svg { width: 48px; height: 48px; }
.empty-state p { font-size: 15px; }
.toast { position: fixed; bottom: 28px; right: 28px; z-index: 2000; display: flex; align-items: center; gap: 10px; padding: 14px 20px; border-radius: 10px; font-size: 14px; font-weight: 600; box-shadow: 0 8px 24px rgba(0,0,0,0.15); animation: slideUp 0.3s ease; }
.toast svg { width: 18px; height: 18px; flex-shrink: 0; }
.toast-success { background: #1a4a35; color: #fff; }
.toast-error { background: #c0392b; color: #fff; }
/* HOUSEHOLD DETAIL */
.hd-breadcrumb { display: flex; align-items: center; gap: 6px; font-size: 13px; margin-bottom: 16px; }
.hd-breadcrumb svg { color: #8aab99; }
.hd-bc-link { color: #2d6e50; font-weight: 600; cursor: pointer; }
.hd-bc-link:hover { text-decoration: underline; }
.hd-bc-current { color: #1a2e25; font-weight: 600; }
.hd-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; flex-wrap: wrap; gap: 12px; }
.hd-title { font-size: 22px; font-weight: 700; color: #1a2e25; }
.hd-actions { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
.hd-cards-row { display: grid; gap: 16px; margin-bottom: 24px; }
.hd-info-card { background: #fff; border-radius: 12px; border: 1px solid #e8eeeb; padding: 20px 24px; }
.hd-card-title { font-size: 12px; font-weight: 700; color: #5a7a6a; letter-spacing: 0.6px; margin-bottom: 14px; }
.hd-info-row { display: flex; align-items: center; justify-content: space-between; padding: 9px 0; border-bottom: 1px solid #f0f4f2; font-size: 13.5px; }
.hd-info-row:last-child { border-bottom: none; }
.hd-info-label { color: #5a7a6a; font-weight: 400; }
.hd-info-val { color: #1a2e25; }
.hd-info-val.bold { font-weight: 700; }
.hd-resident-section { background: #fff; border-radius: 12px; border: 1px solid #e8eeeb; padding: 20px; }
.hd-resident-toolbar { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; flex-wrap: wrap; gap: 12px; }
.hd-resident-title { font-size: 17px; font-weight: 700; color: #1a2e25; }
.hd-resident-controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.hd-resident-footer { padding: 12px 4px 0; font-size: 13px; color: #8aab99; }
.td-num { color: #8aab99; font-size: 13px; }
.td-res-name { font-weight: 600; color: #1a2e25; }
/* RESIDENT PROFILE MODAL */
.rp-avatar-row { display: flex; align-items: center; gap: 16px; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid #e8eeeb; }
.rp-avatar { width: 52px; height: 52px; background: #1a4a35; color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; flex-shrink: 0; }
.rp-name { font-size: 16px; font-weight: 700; color: #1a2e25; }
.rp-meta { font-size: 13px; color: #8aab99; margin-top: 3px; }
.rp-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.rp-field { background: #f8faf9; border-radius: 8px; padding: 10px 14px; }
.rp-label { font-size: 11.5px; font-weight: 600; color: #7a9989; margin-bottom: 4px; }
.rp-val { font-size: 13.5px; color: #1a2e25; font-weight: 500; }
/* BARANGAY PAGE */
.bgy-hero { background: #1a4a35; border-radius: 14px; padding: 28px 32px; display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; gap: 20px; }
.bgy-hero-left { display: flex; align-items: center; gap: 20px; }
.bgy-logo-wrap { width: 72px; height: 72px; background: rgba(255,255,255,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: #fff; }
.bgy-hero-label { font-size: 12px; color: rgba(255,255,255,0.6); font-weight: 500; margin-bottom: 4px; }
.bgy-hero-name { font-size: 26px; font-weight: 800; color: #fff; line-height: 1.1; margin-bottom: 4px; }
.bgy-hero-address { font-size: 13px; color: rgba(255,255,255,0.7); margin-bottom: 12px; }
.bgy-hero-badges { display: flex; gap: 8px; flex-wrap: wrap; }
.bgy-badge { background: rgba(255,255,255,0.15); color: #fff; border-radius: 20px; padding: 4px 14px; font-size: 12.5px; font-weight: 600; }
.btn-edit-info { display: flex; align-items: center; gap: 7px; background: rgba(255,255,255,0.12); color: #fff; border: 1.5px solid rgba(255,255,255,0.3); border-radius: 8px; padding: 9px 18px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: all 0.2s; white-space: nowrap; flex-shrink: 0; }
.btn-edit-info:hover { background: rgba(255,255,255,0.22); }
.bgy-cards-row { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
.bgy-card { background: #fff; border-radius: 14px; border: 1px solid #e8eeeb; padding: 24px; }
.bgy-card-title { display: flex; align-items: center; gap: 8px; font-size: 12px; font-weight: 700; color: #3a6a52; letter-spacing: 0.6px; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid #f0f4f2; }
.bgy-info-row { display: flex; align-items: flex-start; gap: 12px; padding: 12px 0; border-bottom: 1px solid #f8faf9; }
.bgy-info-row:last-child { border-bottom: none; }
.bgy-info-row > svg { color: #5a7a6a; flex-shrink: 0; margin-top: 3px; }
.bgy-row-label { font-size: 12px; color: #8aab99; font-weight: 500; margin-bottom: 2px; }
.bgy-row-val { font-size: 14px; font-weight: 600; color: #1a2e25; }
/* WATER & SANITATION SUMMARY */
.bgy-ws-section { background: #fff; border-radius: 14px; border: 1px solid #e8eeeb; padding: 24px; margin-top: 18px; }
.bgy-ws-title { display: flex; align-items: center; gap: 8px; font-size: 12px; font-weight: 700; color: #3a6a52; letter-spacing: 0.6px; margin-bottom: 20px; }
.bgy-ws-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
.bgy-ws-card { background: #f4f8f6; border-radius: 10px; padding: 16px 18px; }
.bgy-ws-label { font-size: 12.5px; color: #5a7a6a; font-weight: 500; margin-bottom: 4px; }
.bgy-ws-pct { font-size: 22px; font-weight: 800; color: #1a2e25; margin-bottom: 10px; line-height: 1; }
.bgy-ws-bar-track { height: 6px; background: #d4e9df; border-radius: 99px; overflow: hidden; }
.bgy-ws-bar { height: 100%; border-radius: 99px; transition: width 0.6s ease; min-width: 2px; }
.bgy-ws-bar-safe { background: #1a4a35; }
.bgy-ws-bar-basic { background: #d4a017; }
.bgy-ws-bar-limited { background: #c0392b; }
/* GLOBAL SEARCH */
.global-search-wrap { position: relative; }
.global-search-box { display: flex; align-items: center; gap: 8px; background: #f4f6f5; border: 1.5px solid #dde6e2; border-radius: 8px; padding: 8px 12px; min-width: 280px; transition: border-color 0.2s; }
.global-search-box.active, .global-search-box:focus-within { border-color: #2d6e50; background: #fff; }
.global-search-box svg { width: 15px; height: 15px; color: #8aab99; flex-shrink: 0; }
.global-search-box input { border: none; background: transparent; outline: none; font-size: 13px; color: #1a2e25; width: 100%; }
.global-search-box input::placeholder { color: #9db8ab; }
.search-clear { background: none; border: none; cursor: pointer; display: flex; align-items: center; color: #8aab99; padding: 2px; border-radius: 4px; flex-shrink: 0; }
.search-clear:hover { color: #1a2e25; background: #e8eeeb; }
.search-dropdown { position: absolute; top: calc(100% + 8px); left: 0; right: 0; min-width: 580px; background: #fff; border: 1px solid #e8eeeb; border-radius: 12px; box-shadow: 0 12px 40px rgba(0,0,0,0.15); z-index: 600; overflow: hidden; }
.search-results-header { display: flex; align-items: center; justify-content: space-between; padding: 12px 16px 8px; font-size: 13px; font-weight: 600; color: #5a7a6a; border-bottom: 1px solid #f0f4f2; }
.search-close-btn { background: none; border: none; cursor: pointer; color: #8aab99; display: flex; align-items: center; padding: 4px; border-radius: 4px; }
.search-close-btn:hover { background: #f0f4f2; color: #1a2e25; }
.search-no-results { padding: 24px; text-align: center; color: #8aab99; font-size: 13.5px; }
.search-results-cols { display: grid; grid-template-columns: 2fr 100px 1.5fr 110px; gap: 8px; padding: 8px 16px 6px; font-size: 11px; font-weight: 700; color: #8aab99; letter-spacing: 0.5px; text-transform: uppercase; background: #fafcfb; border-bottom: 1px solid #f0f4f2; }
.search-result-row { display: grid; grid-template-columns: 2fr 100px 1.5fr 110px; gap: 8px; align-items: center; padding: 11px 16px; border-bottom: 1px solid #f8faf9; transition: background 0.12s; }
.search-result-row:last-child { border-bottom: none; }
.search-result-row:hover { background: #f4f8f6; }
.search-result-name { display: flex; flex-direction: column; gap: 2px; font-size: 13.5px; font-weight: 600; color: #1a2e25; }
.search-result-meta { font-size: 12px; font-weight: 400; color: #8aab99; }
.search-result-household { font-size: 13px; color: #2a3e32; }
.search-zone-badge { display: inline-block; background: #d4f0e4; color: #1a6b42; border-radius: 20px; padding: 2px 10px; font-size: 12px; font-weight: 600; }
.btn-view-profile { background: #1a4a35; color: #fff; border: none; border-radius: 7px; padding: 6px 14px; font-size: 12.5px; font-weight: 600; cursor: pointer; transition: background 0.2s; white-space: nowrap; }
.btn-view-profile:hover { background: #0f3326; }
mark { background: #fef3cd; color: #856404; border-radius: 2px; padding: 0 1px; font-style: normal; }
@keyframes slideUp { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
</style>