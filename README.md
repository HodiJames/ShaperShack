# 🏄 Shaper Shed

> The world's best surfboard shapers and glassers — all in one place.

Shaper Shack is a community-built directory of surfboard shapers, glassers, and board-makers from around the world. Built for surfers who care about craft, provenance, and the people behind their boards.

---

## ✨ Features

### 📋 Directory
- Searchable, filterable listing of shapers and glassers worldwide
- Filter by board type, country, and craft category
- Featured and Premium listing tiers
- Hero image with admin-managed upload

### 🏭 Shaper Profiles
- Rich listing pages with bio, specialties, and board portfolio
- Embedded video support for Premium profiles
- Shaping Knowledge cards — educational content direct from the shaper
- Social links (website, Instagram, YouTube, X)
- Ask a Shaper — community Q&A with upvoting and threshold-based live session proposals
- Bookmark / save listings for later

### ⭐ Reviews
- Community review system with star ratings
- Optional board attribution per review
- Moderation queue — reviews go live once approved
- Review modal with full read

### 🏄 Quiver Tracker *(user feature)*
- Log your current boards and boards you've owned over your surfing life
- Per-board: shaper (linked to directory or free text), length, volume, year
- Wave type tags (beach break, point break, reef break, etc.)
- Conditions range slider (1ft mush → 6ft+)
- 0–5 star rating
- Fin tracking — log every fin setup tried, mark your best combo
- Notes / impressions per board
- Archive boards to "Past Boards" section
- Shaper search links boards back to live directory listings
- "Looking for a replacement" flag
- "Shaper not listed? Add them →" shortcut to submission flow

### 👤 User Accounts
- Free account registration
- 4-tier progression system: Newcomer → Regular → Contributor → Local Voice
- 7 earnable badges: 🌊 Founding Member, 🪚 Nominator, ⭐ Trusted Reviewer, 🤙 Loyal, ❓ Curious, ✏️ Contributor, 🪟 Glass Head
- Profile page with stats, activity feed, badge showcase, and quiver
- Saved listings tab

### 🌍 Internationalisation
- 10 locales with flag picker: 🇦🇺 🇺🇸 🇬🇧 🇧🇷 🇵🇹 🇫🇷 🇪🇸 🇩🇪 🇯🇵 🇰🇷
- All three English variants (AU, US, UK) are recognised with their own flag while sharing a single English content layer

### 🛠 Admin Panel
- Approve and manage submitted listings
- Toggle featured / premium status
- Edit listings inline
- Manage category pills
- Hero image upload and management
- Analytics dashboard (source tracking, social link clicks, board type breakdown)

### 📊 Data Management
- Full CSV import/export for all 5 databases:
  - **shapers.csv** — core directory listings
  - **boards.csv** — board portfolios per shaper
  - **knowledge.csv** — shaping knowledge cards
  - **reviews.csv** — community reviews
  - **questions.csv** — Ask a Shaper questions
- Drag-and-drop CSV upload with live preview
- Download current data as CSV at any time

### 📬 Submission Flow
- 3-step shaper submission form
- Step 1: Who are you adding? (Shaper or Glasser, craft categories)
- Step 2: Their details (location, website, Instagram, bio)
- Step 3: Your info (submitter details, privacy consent)
- Post-submission confirmation with "what happens next" steps

---

## 🗂 Project Structure

```
ShaperShack/
├── index.html              # Vite HTML entry point
├── vite.config.js          # Vite configuration
├── package.json            # Dependencies and scripts
├── vercel.json             # Vercel deployment config
├── .gitignore
├── public/
│   └── favicon.svg         # 🏄 emoji favicon
└── src/
    ├── main.jsx            # React root mount
    └── App.jsx             # Full application (single-file)
```

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- npm or yarn

### Local Development

```bash
# Clone the repo
git clone https://github.com/HodiJames/ShaperShack.git
cd ShaperShack

# Install dependencies
npm install

# Start dev server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

### Production Build

```bash
npm run build
```

Output goes to `/dist` — ready to deploy.

---

## ☁️ Deploying to Vercel

The easiest way to deploy:

1. Push to GitHub (already done)
2. Go to [vercel.com/new](https://vercel.com/new)
3. Import the `HodiJames/ShaperShack` repository
4. Vercel auto-detects Vite — click **Deploy**

Vercel will assign a `.vercel.app` URL instantly. Every push to `main` triggers a redeploy automatically.

---

## 📁 CSV Data Format

The app uses five CSV files for data management via the Admin panel. Sample files are included in the repo.

### shapers.csv
| Column | Description |
|--------|-------------|
| id | Unique numeric ID |
| name | Shaper / business name |
| tagline | Short descriptor |
| type | `Shaper` or `Glasser` |
| category | Comma-separated board types |
| country | Country name |
| address | Town / city |
| website | Full URL |
| instagram | Handle (no @) |
| founded | Year founded |
| bio | Full biography |
| tags | Semicolon-separated tags |
| logo_emoji | Emoji for avatar fallback |
| logo_color | Hex colour for avatar |
| logo_url | URL to logo image |
| featured | `true` / `false` |
| premium | `true` / `false` |

### boards.csv
`shaper_id, shaper_name, board_name, type, length, fins, description, price`

### knowledge.csv
`shaper_id, shaper_name, topic, icon, summary, display_order`

### reviews.csv
`id, shaper_id, shaper_name, author, location, board, rating, text, date, approved`

### questions.csv
`id, shaper_id, shaper_name, question, submitted_by, upvotes, date, approved`

---

## 🔐 Admin Access

The admin panel is accessible via the **Admin** button in the nav. Super admin emails are configured directly in `src/App.jsx`:

```js
const SUPER_ADMINS = ["your@email.com"];
```

Add your email there to unlock the full admin panel.

---

## 🛣 Roadmap

- [ ] Backend / database (Supabase or PlanetScale)
- [ ] Real authentication (Supabase Auth or Clerk)
- [ ] Image uploads to cloud storage (Cloudinary / S3)
- [ ] Shaper-managed profiles (claim your listing)
- [ ] Quiver data persistence (currently session-only)
- [ ] Excel (.xlsx) import/export with multi-tab support
- [ ] Aggregate fin data by region
- [ ] "Looking for replacement" → surface matching shapers
- [ ] Full multi-language translations (currently English across all locales)

---

## 🤝 Contributing

This is a community project. If you're a developer who surfs (or a surfer who codes), contributions are welcome.

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 Licence

MIT — do whatever you want with it, just don't be a kook about it.

---

*Built with React, Vite, and a deep appreciation for handcrafted surfboards.*
