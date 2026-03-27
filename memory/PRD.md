# Shaper Shed - Product Requirements Document

## Original Problem Statement
1. Bookmarks not saving for registered users
2. Need video upload for users to share surfing videos with shapers
3. Need translation storage so language tool works properly
4. CSV uploaded shapers need to be stored so everyone can access them

## Architecture
- **Frontend**: React + Vite (port 3000)
- **Backend**: FastAPI (port 8001)
- **Database**: MongoDB (shaper_shed)
- **Storage**: Firebase Storage (for videos - pending implementation)

## User Personas
1. **Surfers** - Browse shapers, save bookmarks, upload videos, read reviews
2. **Shapers** - Listed in directory, receive video shares, answer questions
3. **Admin** - Manage listings, approve submissions, import/export CSV

## Core Requirements (Static)
- User registration and authentication
- Bookmark functionality tied to user accounts
- Multi-language support with persistent translations
- CSV import/export for shapers data
- All data stored in MongoDB for cross-device access

## What's Been Implemented

### March 27, 2026
- ✅ **Bookmark persistence** - Bookmarks now saved to MongoDB tied to user email
- ✅ **User authentication** - Backend API for register/login with MongoDB storage
- ✅ **Listings persistence** - All shapers stored in MongoDB, accessible from any device
- ✅ **CSV import to backend** - Uploaded CSV data saved to MongoDB
- ✅ **Admin sync** - All admin actions (edit, delete, toggle featured/premium) sync to backend
- ✅ **Translation caching** - Translations stored in MongoDB for persistence
- ✅ **Firebase config** - Firebase SDK installed and configured for video uploads

### API Endpoints Added
- POST /api/auth/register - User registration
- POST /api/auth/login - User login
- GET /api/bookmarks/{email} - Get user's bookmarks
- POST /api/bookmarks/{email}/toggle - Toggle bookmark
- GET /api/listings - Get all shapers
- POST /api/listings - Create/update single listing
- POST /api/listings/bulk - Bulk import listings (CSV)
- PUT /api/listings/{id} - Update listing
- DELETE /api/listings/{id} - Delete listing
- POST /api/translate - Translate text with caching

## Prioritized Backlog

### P0 - Critical (Next)
- [ ] Video upload feature with Firebase Storage
- [ ] Video sharing with specific shapers

### P1 - Important
- [ ] Fix Admin button z-index issue (minor UI bug)
- [ ] Video management UI for users
- [ ] Shaper notification when video shared with them

### P2 - Nice to Have
- [ ] Video comments/feedback from shapers
- [ ] Video analytics (views, shares)
- [ ] Batch translation on content change

## Next Tasks
1. Implement video upload component using Firebase Storage
2. Add video gallery to user profile
3. Create video sharing modal to select shapers
4. Add "Videos" tab to shaper profiles showing shared videos
