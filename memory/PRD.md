# Shaper Shed - Product Requirements Document

## Original Problem Statement
1. Bookmarks not saving for registered users
2. Need video upload for users to share surfing videos with shapers
3. Premium Listing flow for shapers to showcase their work
4. Admin Panel functionalities (Premium requests review, Questions review)

## Architecture
- **Frontend**: React + Vite (port 3000)
- **Backend**: FastAPI (port 8001)
- **Database**: MongoDB Atlas (shapershed)
- **Storage**: Firebase Storage (for videos - pending)
- **Deployment**: Vercel (frontend), Railway (backend)

## What's Been Implemented

### April 1, 2026 - Premium Flow Simplification
- ✅ **Simplified Premium Flow** - Single process: Request → Admin Approve → Premium Active
- ✅ **Admin approval now grants BOTH** ownership AND premium status in one step
- ✅ **Renamed "Claims" to "Premium Requests"** in Admin Panel
- ✅ **Updated PremiumLock component** - Shows "Request Premium Features" button
- ✅ **My Listings tab** - Premium owners see their listings and can edit content
- ✅ **Premium Edit Page** - Add videos, knowledge articles, board portfolio
- ✅ **Fixed button click issue** - `pointer-events: none` on overlay

### Previous Work
- ✅ MongoDB Atlas integration (bookmarks, listings, questions persist)
- ✅ Railway backend deployment with custom Dockerfile
- ✅ Ask a Shaper questions system with approval workflow
- ✅ Admin Panel with Questions approval

## Premium Flow (Simplified)

### Step 1: User Requests Premium
1. User visits a listing page
2. Sees locked premium sections (Videos, Knowledge, Boards)
3. Clicks "Request Premium Features" button
4. Fills out form with contact info and role

### Step 2: Admin Reviews & Approves
1. Admin goes to Admin Panel → "Premium Requests" tab
2. Reviews pending requests
3. Clicks "Approve Premium" → listing gets:
   - `premium: true`
   - `ownerEmail: <user's email>`
   - `premiumContent: { videos: [], knowledge: [], boards: [] }`

### Step 3: User Manages Premium Content
1. User logs in → Profile → "💎 My Listings" tab
2. Sees their premium listing with "Edit Premium Content" button
3. Can add:
   - 🎬 YouTube videos (Watch This Shaper at Work)
   - 📚 Knowledge topics (Shaping Knowledge)
   - 🏄 Board portfolio with specs/pricing

### API Endpoints
- POST /api/claims - Submit premium request
- PUT /api/claims/{listing_id}/approve - Approve (grants premium + ownership)
- PUT /api/claims/{listing_id}/reject - Reject
- PUT /api/listings/{id} - Update listing (including premiumContent)

## Prioritized Backlog

### P1 - Important
- [ ] Firebase Video Upload Integration (direct uploads)
- [ ] Forgot Password flow (email reset)

### P2 - Nice to Have
- [ ] Translation storage via OpenAI
- [ ] CSV Export for Questions

## Test Credentials
- Admin: admin@shapershed.com / admin123
