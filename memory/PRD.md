# Shaper Shed - Product Requirements Document

## Original Problem Statement
1. Bookmarks not saving for registered users
2. Need video upload for users to share surfing videos with shapers
3. Premium Listing flow for shapers to showcase their work
4. Admin Panel functionalities (Premium requests review, Questions review)
5. Premium subscription billing with trial periods and Stripe integration
6. Admin ability to manage premium listings (remove privileges, reallocate ownership)

## Architecture
- **Frontend**: React + Vite (port 3000)
- **Backend**: FastAPI (port 8001)
- **Database**: MongoDB Atlas (shapershed)
- **Storage**: Firebase Storage (for images, board portfolio)
- **Payments**: Stripe (via emergentintegrations library)
- **Deployment**: Vercel (frontend), Railway (backend)

## What's Been Implemented

### April 1, 2026 - Premium Billing & Admin Management
- ✅ **Admin Premium Management Tab** - New "💎 Premium Mgmt" tab in Admin Panel
  - View all premium listings with trial status and days remaining
  - Remove premium privileges from any listing
  - Reallocate listing control to a different user email
- ✅ **User Billing Dashboard** - New "💳 Billing" tab in User Profile
  - View owned premium subscriptions with trial countdown
  - Payment history / invoices table
  - Payment method info (Stripe managed)
  - Terms & Conditions accordion
  - "Upgrade to Paid Plan" button for trial users
- ✅ **Backend Subscription APIs**
  - GET /api/subscription/{listing_id} - Subscription details with trial days
  - GET /api/billing/{email} - User billing data (subscriptions, transactions, listings)
  - GET /api/admin/premium-listings - All premium listings for admin
  - PUT /api/admin/listings/{id}/remove-premium - Remove premium privileges
  - PUT /api/admin/listings/{id}/reallocate-owner - Transfer ownership
- ✅ **Stripe Integration** - Using emergentintegrations library for checkout

### April 1, 2026 - Premium Flow Simplification
- ✅ **Simplified Premium Flow** - Single process: Request → Admin Approve → Premium Active
- ✅ **Admin approval now grants BOTH** ownership AND premium status in one step
- ✅ **Renamed "Claims" to "Premium Requests"** in Admin Panel
- ✅ **My Listings tab** - Premium owners see their listings and can edit content
- ✅ **Premium Edit Page** - Add videos, knowledge articles, board portfolio
- ✅ **Board Portfolio with Firebase** - Image carousel, URL field, "Ask about this board"
- ✅ **User Quiver Management** - Add boards to personal quiver with photos
- ✅ **Surfers Using Boards Gallery** - Show user quiver photos on shaper listings
- ✅ **Mobile optimization** - Collapsed nav, removed language selector

### Previous Work
- ✅ MongoDB Atlas integration (bookmarks, listings, questions persist)
- ✅ Railway backend deployment with custom Dockerfile
- ✅ Ask a Shaper questions system with approval workflow
- ✅ Admin Panel with Questions approval

## Premium Subscription Flow

### Trial Flow (7 days free)
1. Admin approves premium request → Trial starts automatically
2. User sees "X days left in trial" badge in My Listings and Billing
3. User can upgrade to paid plan ($39/mo) anytime via Stripe Checkout
4. Trial expiration disables premium features

### Admin Management
1. Admin Panel → "💎 Premium Mgmt" tab
2. View all premium listings with status (Trial/Active/Premium)
3. Enter email + click "Transfer Control" to reassign ownership
4. Click "Remove Premium Privileges" to revoke premium status

### API Endpoints - Subscriptions
- POST /api/premium/start-trial - Start 7-day trial
- POST /api/premium/checkout - Create Stripe checkout session
- GET /api/premium/status/{session_id} - Check payment status
- POST /api/webhook/stripe - Handle Stripe webhooks

## Prioritized Backlog

### P0 - In Progress
- [ ] Two-way sync: Quiver ↔ Reviews (comments/ratings link both ways)
- [ ] "Current board / past board" field in review submission

### P1 - Important
- [ ] "Forgot Password" email reset flow
- [ ] Delete button in Quiver board editor
- [ ] Remove tick icon from Save button in Quiver

### P2 - Nice to Have
- [ ] Translation storage via OpenAI (requires API key)
- [ ] CSV Export for Questions in Admin
- [ ] App.tsx refactoring (4800+ lines)

## Test Credentials
- Admin: admin@shapershed.com / admin123
- Premium listing: Semente Surfboards (ID: 49) - owned by freeflyjames@gmail.com
