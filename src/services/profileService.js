// src/services/profileService.js
import axios from 'axios';

// Base API client (adjust baseURL as needed)
const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '',
  headers: {
    'Content-Type': 'application/json'
  }
});

/**
 * Fetch the current user profile
 */
export function getProfile() {
  return apiClient.get('/api/profile').then(res => res.data);
}

/**
 * Update basic info: avatar, email, salutation, firstName, lastName
 */
export function updateBasic(data) {
  return apiClient.put('/api/profile/basic', data).then(res => res.data);
}

/**
 * Update additional details: maritalStatus, dob, phone, address, homeAddress, country, postalCode, nationality
 */
export function updateAdditional(data) {
  return apiClient.put('/api/profile/additional', data).then(res => res.data);
}

/**
 * Update spouse details
 */
export function updateSpouse(data) {
  return apiClient.put('/api/profile/spouse', data).then(res => res.data);
}

/**
 * Update user preferences
 */
export function updatePreferences(data) {
  return apiClient.put('/api/profile/preferences', data).then(res => res.data);
}
