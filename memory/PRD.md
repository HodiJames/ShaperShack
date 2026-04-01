# Shaper Shed - Product Requirements Document

## Original Problem Statement
1. Bookmarks not saving for registered users
2. Need video upload for users to share surfing videos with shapers
3. Need translation storage so language tool works properly
4. CSV uploaded shapers need to be stored so everyone can access them
5. Premium Listing flow ($39/month via Stripe, 7-day trial)
6. Admin Panel functionalities (Claims, Questions review, Impersonate Premium users)

## Architecture
- **Frontend**: React + Vite (port 3000)
- **Backend**: FastAPI (port 8001)
- **Database**: MongoDB Atlas (shapershed)
- **Storage**: Firebase Storage (for videos - pending implementation)
- **Payments**: Stripe (stubbed, needs API key)
- **Deployment**: Vercel (frontend), Railway (backend with custom Dockerfile)

## User Personas
1. **Surfers** - Browse shapers, save bookmarks, upload videos, read reviews, ask questions
2. **Shapers** - Listed in directory, receive video shares, answer questions, claim & upgrade listings
3. **Admin** - Manage listings, approve submissions, review questions, impersonate premium users

## Core Requirements (Static)
- User registration and authentication
- Bookmark functionality tied to user accounts
- Multi-language support with persistent translations
- CSV import/export for shapers data
- All data stored in MongoDB for cross-device access
- Premium listing claim flow with Stripe payments

## What's Been Implemented

### April 1, 2026
- ✅ **Fixed PremiumLock button click issue** - Added `pointer-events: none;` to `.ld-lock::before` pseudo-element
- ✅ **Added "My Listings" tab to Profile** - Users can see and manage their claimed listings
- ✅ **Created PremiumEditPage** - Premium owners can add videos, knowledge articles, and board portfolio
- ✅ **Enhanced ListingPage** - Shows user-added premium content (videos, knowledge, boards)
- ✅ **Owner Edit Button** - Premium listing owners see "Edit Content" button on their listing

### Previous Session
- ✅ **MongoDB Atlas integration** - Bookmarks, listings, questions persist across sessions
- ✅ **Railway backend deployment** - Custom Dockerfile for Python backend
- ✅ **Premium Listing UI** - Claim flow, "Watch this Shaper at Work", "Shaping Knowledge" sections
- ✅ **Admin Panel** - Claims review, Questions approval, Premium Impersonation
- ✅ **Ask a Shaper** - Questions system with voting and approval workflow
- ✅ **Repairs category** - Added with icon
- ✅ **CSV import to backend** - Uploaded CSV data saved to MongoDB
- ✅ **Translation caching** - Translations stored for persistence
- ✅ **Firebase config** - Firebase SDK installed (not fully wired)

## Premium Flow (Complete)

### Step 1: Claim Listing
1. User clicks "Unlock Premium Features" on any listing
2. ClaimModal opens → user fills contact info
3. Claim saved to DB with status "pending"
4. Admin reviews in Admin Panel → Claims tab
5. Admin approves → listing marked `claimed: true`, `ownerEmail` set

### Step 2: Access from "My Listings"
1. Owner logs in → Profile → "💎 My Listings" tab
2. Shows claimed listings with actions:
   - View Listing
   - Upgrade to Premium / Edit Premium Content

### Step 3: Upgrade to Premium
1. Owner clicks "Start 7-Day Free Trial"
2. Listing marked `premium: true, premiumTrial: true`
3. After trial → Stripe checkout ($39/mo)

### Step 4: Edit Premium Content
Premium owners can add via PremiumEditPage:
- 🎬 YouTube videos (Watch This Shaper at Work)
- 📚 Shaping Knowledge (topics with descriptions)
- 🏄 Board Portfolio (specs, pricing)

### API Endpoints
- POST /api/auth/register, POST /api/auth/login
- GET /api/bookmarks/{email}, POST /api/bookmarks/{email}/toggle
- GET /api/listings, POST /api/listings, POST /api/listings/bulk
- PUT /api/listings/{id}, DELETE /api/listings/{id}
- POST /api/translate
- GET /api/questions, POST /api/questions, POST /api/questions/{qid}/vote
- GET /api/claims, POST /api/claims
- PUT /api/claims/{listing_id}/approve, PUT /api/claims/{listing_id}/reject
- POST /api/premium/start-trial, POST /api/premium/checkout, GET /api/premium/status/{session_id}

## Prioritized Backlog

### P0 - Critical (Awaiting Keys)
- [ ] Stripe Integration activation (backend stubs exist, needs STRIPE_API_KEY in Railway)
- [ ] Firebase Video Upload Integration (config provided, needs full wiring)

### P1 - Important
- [ ] Forgot Password flow - Backend email reset + frontend modal
- [ ] Translation storage via OpenAI (requires OPENAI_API_KEY)
- [ ] CSV Export for Questions in Admin panel

### P2 - Nice to Have
- [ ] Impersonate Premium feature refinement
- [ ] Video management UI for users
- [ ] Video analytics (views, shares)

## Pending Issues

### Issue 1: Forgot Password (P1)
- Status: NOT STARTED
- Current: Link shows toast message "Coming soon"
- Needed: Backend email reset flow + frontend modal

## Known Mocked/Stubbed Features
- **Stripe Payments**: Backend endpoints exist but need actual API key
- **OpenAI Translations**: Library installed but needs API key
- **Firebase Video**: Config provided but not fully integrated

## Test Credentials
- Admin: admin@shapershed.com / admin123

## Next Tasks
1. Complete Stripe checkout flow when API key provided
2. Wire up Firebase Video Upload in Premium Edit Modal
3. Implement Forgot Password email reset flow
