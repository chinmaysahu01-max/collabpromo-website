# CollabPromo.com — Creator & Brand Promotional Matching Platform

**CollabPromo.com** is a modern, responsive website that connects social media creators with brands seeking promotional content such as reels, videos, posts, and stories. The platform acts as a trusted introductory mediator: creators submit verified rate cards while keeping their personal contact details shielded from public scraping, brands discover and filter creators based on commercial alignment, and campaign enquiries are coordinated smoothly through the platform.

---

## 🚀 Quick Start / How to Run

### Method 1: Instant Direct Launch (No dependencies required)
Simply double-click or open `index.html` in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, or Safari):
```
C:\Users\Chinmay sahu\.gemini\antigravity\scratch\collabpromo-website\index.html
```
The application includes a self-contained bundle (`js/bundle.js`) that works immediately without CORS issues or local server prerequisites.

### Method 2: Local Python Server
To run with local HTTP serving:
```powershell
cd "C:\Users\Chinmay sahu\.gemini\antigravity\scratch\collabpromo-website"
python server.py 8000
```
Then navigate to `http://localhost:8000` in your browser.

---

## 🌟 Key Features & Workflows

### 1. Role-Based Navigation & Instant Testing
- **Role Switcher**: Click the badge in the header ("Visitor Mode" / "Demo Role Switcher") or the footer links to test the four personas:
  - **Public Visitor (Guest)**: Explores homepage, "How It Works", benefits, and public directory.
  - **Creator Persona (Maya Lin / Custom)**: Accesses Creator Hub, updates rate cards, toggles collaboration availability, and monitors received campaign briefs.
  - **Brand Persona (Lumina Skin Co. / Custom)**: Browses directory, filters creator tiers, submits campaign proposals, and tracks enquiry statuses.
  - **Platform Administrator**: Moderates submissions, reviews explicit consent, publishes/hides directory listings, edits coordinator notes, and manages demo data.

### 2. Homepage & Marketing Experience
- **Brand Identity**: Modern typography, clean layout, generous whitespace, accessible contrast, and zero clutter.
- **Top Dual-Role CTAs**: Prominent **Continue as a Brand** and **Continue as a Creator** action buttons near the top of the hero section.
- **How It Works**: 3-step breakdown explaining rates submission, brand discovery, and platform-mediated introductions.
- **Benefits Section**: Dedicated value propositions for both advertisers and content creators.
- **Featured Creators**: High-impact snapshot of verified sample creator profiles labeled with sample indicators.
- **Trust & Non-Guarantee Disclaimers**: Clear statements that profile submission does not guarantee sponsorships, and brand enquiries are introductory proposals rather than automatic bookings.

### 3. Creator Registration & Profile Management
- **Structured Onboarding Form**:
  - Personal Name & **Private Email / Phone** (strictly protected; never displayed to brands).
  - Social Platform (Instagram, YouTube, TikTok, X) and validated Channel URL.
  - Niche Category, City/Country Location, Follower Count, and optional Average Views.
  - Rate Card for Reels/Shorts, Feed Posts, Story tags, and Content Bundles.
  - Deliverables Scope Notes (revisions included, usage rights).
  - Availability Toggle (*"Open for brand collaborations"*).
  - **Explicit Consent Checkbox**: Mandatory agreement before any profile details appear in the public directory.
- **Creator Dashboard**:
  - Real-time rate card editor.
  - Live preview of "How Brands See Your Profile Card".
  - Log of campaign briefs forwarded by the platform coordinator.

### 4. Brand Discovery & Creator Directory
- **Card-Based Creator Listings**: Highlighting handle, platform, category, location, follower tier, starting rates, and collaboration status.
- **Working Interactive Filters**:
  - Filter by Social Media Platform (Instagram, YouTube, TikTok, X).
  - Filter by Niche / Content Category.
  - Filter by Follower Tiers (Micro <50K, Mid-tier 50K–200K, Macro 200K+).
  - Filter by Maximum Reel / Video Rate.
  - Toggle *"Open for collaborations only"*.
  - Full-text search by creator name, @handle, or location.
- **Working Sorting Options**:
  - Followers: High to Low & Low to High.
  - Reel Rate: Low to High & High to Low.
  - Post Rate: Low to High.
- **Empty State**: Friendly reset prompt when no creators match active filters.
- **Full Profile Modal**: Shows detailed rate breakdown, platform link, deliverable scope, and privacy protection note.

### 5. Brand Campaign Enquiry Flow
- **Comprehensive Brief Form**: Collects brand information, campaign objective, content format, target audience, budget bracket, timeline, usage rights, and creative notes.
- **Multi-State Confirmation**: Displays confirmation with unique reference number (e.g. `#CP-8492`), next steps, and non-binding disclaimer.
- **Brand Campaign Dashboard**: Allows brands to review submitted enquiries and coordinator status updates.

### 6. Platform Administrator Experience
- **Directory Moderation**:
  - Table of all creator submissions with consent audit indicator.
  - One-click *Approve & Publish* or *Hide from Brands*.
  - Permanent delete or demo reset buttons.
- **Enquiry Pipeline & Mediation**:
  - View all brand briefs and requested creators.
  - Status pipeline: `Submitted` &rarr; `Under Review` &rarr; `Intro Made` &rarr; `Closed`.
  - Inline coordinator notes log.

---

## 🔒 Privacy, Security & Trust Architecture

1. **Strict Contact Shielding**: Creator email addresses and phone numbers are excluded from brand-facing discovery data models (`getPublicCreators()` systematically removes `privateEmail` and `privatePhone`).
2. **Explicit Consent Gate**: Profiles require an active consent flag (`hasConsented: true`) and platform approval (`status: 'approved'`) before appearing in public listings.
3. **No Password Harvesting**: The platform never requests social media account passwords or OAuth tokens.
4. **Legally Transparent Disclaimers**: Clarifies independent contractor relationships, non-guarantee of commercial placement, and non-binding enquiry terms.

---

## 📁 Project Directory Structure

```
collabpromo-website/
├── index.html            # Main single-page web app with all views & semantic sections
├── css/
│   └── styles.css        # Custom CSS, accessible focus rings, and badge themes
├── js/
│   ├── data.js           # Initial sample creators, enquiries, and category constants
│   ├── store.js          # Persistent state store (LocalStorage) and privacy filtering
│   ├── app.js            # Main application controller, routing, and form validation
│   └── bundle.js         # Universal standalone bundle for file:// and HTTP execution
├── server.py             # Optional zero-dependency Python 3 HTTP and API server
├── build_bundle.py       # Helper script to compile modular JS into standalone bundle
└── README.md             # Complete project and architecture documentation
```

---

## 💻 Recommended Workspace Setup

To make this project your active workspace in Antigravity or your IDE:
```
C:\Users\Chinmay sahu\.gemini\antigravity\scratch\collabpromo-website
```
