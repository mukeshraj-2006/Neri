# 🚀 NERI — Performance Tracker Phase 3

**A comprehensive personal performance tracking web application** that unifies career development, physical health, nutrition, daily productivity, and personal finance into a single intelligent dashboard. Featuring a **fully responsive design** optimized for Desktop, Tablet, and Mobile devices, along with seamless **Dark and Light Mode** support.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini_API-Integrated-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-Data_Viz-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technical Architecture](#technical-architecture)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [AI-Powered Task Suggestions](#ai-powered-task-suggestions)

---

## Overview

**NERI Performance Tracker** is a full-stack web application designed to help users track and improve across multiple dimensions of their life — from career skills and professional growth to physical health, nutrition, financial habits, and daily productivity. It provides a unified dashboard with real-time progress tracking, intelligent daily recommendations, interactive charts, and a calendar system.

The application leverages **FastAPI** as the backend framework for high-performance, async-capable API routing, **PostgreSQL** for robust, scalable persistent storage, and the **Google Gemini API** for AI-powered personalized task suggestions based on the user's BMI metrics and career skill profile. The entire application features a **fully responsive, dual-theme UI**, ensuring a seamless and visually appealing experience across all screen sizes and user preferences.

---

## Key Features

### 🎨 Intuitive User Experience
- **Dynamic Theme Toggle**: Instantly switch between an immersive Dark Mode and a crisp, high-contrast Light Mode. Theme preferences are automatically saved across sessions.
- **Responsive Layout**: Adapts seamlessly to Desktop, Tablet, and Mobile viewing environments with smart, collapsible navigation.

### 🎯 Overview Dashboard
- Daily performance summary with combined completion percentages
- Interactive calendar with day-by-day progress heatmap (color-coded: green/amber/red)
- Quick reminder sticky notes with deadlines
- Motivational daily quotes fetched from an external API
- Day notes for journaling and reflection

### 💼 Profession Tracker
- Personalized daily task checklists generated based on profession type and field of interest
- Support for multiple profession types: Student, Working Professional, Freelancer, and more
- Task CRUD operations with completion tracking
- Career development goals auto-synced daily via the Gemini API
- Progress percentage calculation combining core tasks and career goals

### 🏋️ Physical Health Tracker
- BMI calculation with real-time status classification (Underweight / Normal / Overweight / Obese)
- Water intake tracking against personalized daily targets
- Protein intake monitoring with BMI-based target calculation
- Auto-generated daily nutrition checklist (breakfast, lunch, dinner, fruits)
- Rotating daily workout routines (Cardio, Leg Day, Chest & Triceps, etc.)
- Physical goal scheduling with deadlines and notes

### 💰 Finance Tracker
- Detailed daily expense tracking and categorization
- Visual breakdown of spending (last 30 days) using an interactive Doughnut chart
- Add, review, and delete functionality for recent transactions
- Easy navigation across past and present dates to inspect historical spending habits
- **Mobile-Optimized Layout**: Forms and charts intelligently stack for compact viewing.

### 👤 Career Profile
- Comprehensive editable profile: name, profession type, field of interest, degree, branch, institution, bio
- Distinct view and edit modes with "Edit Profile" toggle
- Support for Student and Working Professional profile variants
- Profile data drives personalized task generation across the entire app

### 📅 Calendar System
- Month-at-a-glance view with daily completion dots
- Click any date to view historical performance data
- Past dates show frozen, read-only snapshots
- Future dates are blurred with "Future date" indicators
- Persistent day notes per date

---

## Technical Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                        CLIENT (Browser)                                │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐      │
│  │ Overview │ │Profession│ │ Physical │ │  Career  │ │ Finance  │      │
│  │  .html   │ │  .html   │ │  .html   │ │  .html   │ │  .html   │      │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘      │
│       │             │            │             │            │          │
│  ┌────┴─────────────┴────────────┴─────────────┴────────────┴─────┐    │
│  │                 Vanilla JS (script.js) & Chart.js              │    │
│  │      fetch() API calls · DOM manipulation · Event mgmt         │    │
│  └───────────────────────────┬────────────────────────────────────┘    │
│                              │                                         │
│  ┌───────────────────────────┴────────────────────────────────────┐    │
│  │                 CSS (style.css) — Dark & Light Theme           │    │
│  │   Glassmorphism · Responsive Mobile-First Grids · Animations   │    │
│  └────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────┬──────────────────────────────────────┘
                                  │  HTTP (JSON / Form POST)
┌─────────────────────────────────┴──────────────────────────────────────┐
│                        SERVER (FastAPI + Jinja2)                       │
│                                                                        │
│  ┌───────────────────────────────────────────────────────────────┐     │
│  │                      app.py (1800+ LOC)                       │     │
│  │                                                               │     │
│  │  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────┐   │     │
│  │  │   Auth      │  │  Page Routes │  │    API Endpoints    │   │     │
│  │  │  login      │  │  /overview   │  │  /api/tasks         │   │     │
│  │  │  signup     │  │  /profession │  │  /api/physical      │   │     │
│  │  │  logout     │  │  /physical   │  │  /api/finance       │   │     │
│  │  │  decorator  │  │  /finance    │  │  /api/calendar      │   │     │
│  │  └─────────────┘  └──────────────┘  └─────────────────────┘   │     │
│  │                                                               │     │
│  │  ┌────────────────────────────────────────────────────────┐   │     │
│  │  │                  Business Logic Layer                  │   │     │
│  │  │  • recalculate_daily_activity()                        │   │     │
│  │  │  • compute_nutrition_targets()                         │   │     │
│  │  │  • _generate_profession_checklist()                    │   │     │
│  │  │  • track_daily_finance()                               │   │     │
│  │  └────────────────────────────────────────────────────────┘   │     │
│  └───────────────────────────────────────────────────────────────┘     │
│                                                                        │
│  ┌──────────────┐    ┌───────────────────────────────────────────┐     │
│  │ database.py  │    │           Gemini API (External)           │     │
│  │ get_db()     │    │    AI-powered task & goal suggestions     │     │
│  │ init_db()    │    │    based on BMI + career skill profile    │     │
│  └──────┬───────┘    └───────────────────────────────────────────┘     │
│         │                                                              │
│  ┌──────┴────────────────────────────────────────────────────────┐     │
│  │                    PostgreSQL Database                        │     │
│  │    13 Tables · Row-factory dict access · UNIQUE constraints   │     │
│  └───────────────────────────────────────────────────────────────┘     │
└────────────────────────────────────────────────────────────────────────┘
```

### Architecture Highlights

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend Framework** | FastAPI | High-performance async web framework with automatic request validation |
| **Templating** | Jinja2 | Server-side HTML rendering with template inheritance (`base.html`) |
| **Database** | PostgreSQL | Robust, scalable relational database for production deployments |
| **Frontend UI/Logic**| Vanilla JS + CSS | No framework overhead; direct DOM manipulation and themed styling |
| **Data Visualization**| Chart.js | Renders interactive, theme-aware doughnut charts for expenses |
| **AI Integration** | Google Gemini API | Intelligent, personalized task and goal suggestions |
| **Auth** | Session-based | SHA-256 password hashing with server-side session management |

---

## Database Schema

The application uses **13 normalized tables** in PostgreSQL, including the new `daily_finance` table:

```
┌──────────────────┐       ┌───────────────────┐       ┌────────────────────┐
│      users       │       │      tasks        │       │  daily_finance     │
│──────────────────│       │───────────────────│       │────────────────────│
│ id (PK)          │◄──┐   │ id (PK)           │   ┌──►│ id (PK)            │
│ username         │   ├──►│ user_id (FK)      │   │   │ user_id (FK)       │
│ password_hash    │   │   │ title             │   │   │ entry_date         │
│ height           │   │   │ weight            │   │   │ category           │
│ bmi              │   │   │ is_completed      │   │   │ amount             │
└──────────────────┘   │   └───────────────────┘   │   │ notes              │
                       │                           │   └────────────────────┘
┌──────────────────┐   │   ┌───────────────────┐   │
│  user_profiles   │   ├──►│  daily_physical   │   │   ┌────────────────────┐
│──────────────────│   │   │───────────────────│   │   │ profession_tasks   │
│ user_id (FK, UQ) │◄──┤   │ user_id (FK)      │   │   │────────────────────│
│ full_name        │   │   │ entry_date        │   ├──►│ id (PK)            │
│ profession_type  │   │   │ water_intake      │   │   │ title              │
│ bio              │   │   │ protein_intake    │   │   │ is_completed       │
└──────────────────┘   │   └───────────────────┘   │   └────────────────────┘
                       │                           │
┌──────────────────┐   │   ┌───────────────────┐   │   ┌────────────────────┐
│   reminders      │   ├──►│  daily_activity   │   │   │nutrition_checklist │
│──────────────────│   │   │───────────────────│   │   │────────────────────│
│ user_id (FK)     │◄──┤   │ user_id (FK)      │   ├──►│ user_id (FK)       │
│ title            │   │   │ entry_date (UQ)   │   │   │ entry_date         │
│ reminder_date    │   │   │ total_points      │   │   │ item_label         │
└──────────────────┘   │   │ day_note          │   │   └────────────────────┘
                       │   └───────────────────┘   │
                       │                           │   ┌────────────────────┐
                       ├──►│ physical_goals    │   │   │scheduled_activities│
                       │   │───────────────────│   │   │────────────────────│
                       │   │ user_id (FK)      │   └──►│ user_id (FK)       │
                       │   │ goal_date         │       │ activity_date      │
                       │   │ goal_title        │       │ activity_name      │
                       │   └───────────────────┘       └────────────────────┘
```

---

## API Endpoints

### Finance & Expense Tracking APIs (New in Phase 3)
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/finance` | Finance tracking page dashboard |
| `GET` | `/api/finance/data` | Retrieve 30-day grouped data or single date specifics |
| `POST` | `/api/finance/add` | Logs a new expense item into the database |
| `POST` | `/api/finance/delete` | Removes an expense transaction securely |

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET/POST` | `/login` | User login with session creation |
| `GET/POST` | `/signup` | New user registration |
| `GET` | `/logout` | Session teardown and redirect |

### Page Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/overview` | Main dashboard with daily summary |
| `GET` | `/profession` | Profession task tracker |
| `GET` | `/physical` | Physical health & nutrition tracker |
| `GET` | `/career` | Career profile management |
| `GET` | `/profile-setup` | Initial profile setup wizard |

### Core Tracking APIs
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/tasks/add` | Create a new daily task |
| `POST` | `/api/physical/update`| Update water/protein intake |
| `GET` | `/api/calendar/month` | Get monthly activity data |
| `POST` | `/api/profession/tasks/add` | Manage professional tasks |

---

## Project Structure

```text
Performance_Tracker Phase-03/
│
├── app.py                      # Main application — routes, APIs, business logic
├── database.py                 # Database connection helper (PostgreSQL adapter)
├── schema.sql                  # Full database schema (13 tables)
│
├── templates/                  # Jinja2 HTML templates
│   ├── base.html               # Base layout with navbar, theme toggle, mobile menu
│   ├── overview.html           # Main dashboard
│   ├── profession.html         # Profession tasks
│   ├── physical.html           # Physical health
│   ├── career.html             # Profile management
│   └── finance.html            # Finance / Expense dashboard
│
├── static/
│   ├── css/style.css           # Global stylesheet — responsive design, dark/light themes
│   └── js/script.js            # Client-side API calls & interaction logic
│
└── requirements.txt            # Environment spec (psycopg2-binary, etc.)
```

---

## Setup & Installation

### Prerequisites
- Python 3.10 or higher
- PostgreSQL Server (Local or Cloud)
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone https://github.com/mukeshraj-2006/Performance-Tracker-Phase-03.git
cd Performance-Tracker-Phase-03
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Ensure `psycopg2-binary` is installed for PostgreSQL support).*

### 3. Set Environment Variables
```bash
# Database URL for PostgreSQL
export DATABASE_URL="postgresql://user:password@localhost:5432/neri_db"

# Set a custom secret key (defaults to 'dev_key_neri_dark_mode')
export SECRET_KEY="your-secret-key-here"

# Set your Gemini API key for AI-powered suggestions
export GEMINI_API_KEY="your-gemini-api-key"
```

### 4. Run the Application
```bash
uvicorn app:app --reload --port 5000
```

The application will be available at **http://localhost:5000**

---

## Usage

1. **Overview Dashboard** — View daily summary metrics, calendar, and reminders. The layout automatically adapts to mobile and tablet views.
2. **Profession** — Tackle AI-generated career tasks and check off your skills-oriented routines.
3. **Physical** — Maintain health streaks tracking calories, macros, and scheduled workout routines.
4. **Finance** — Track daily expenses and review historical financial flows with interactive charts that stack cleanly on small screens.
5. **Career** — Setup personal profile details shaping all AI features.
6. **Theme Customization** — Use the sun/moon toggle in the sidebar to switch between light and dark modes instantly.

---

## AI-Powered Task Suggestions

NERI integrates with the **Google Gemini API** to provide intelligent, automated task and goal suggestions tailored to each user's unique profile:

### How It Works

```text
┌────────────────────────┐
│     User Profile       │
│  Profession | Metrics  │
└──────────┬─────────────┘
           ▼
┌────────────────────────┐      ┌────────────────────────┐
│   Gemini Processing    │─────►│  Generated Outputs     │
└────────────────────────┘      │  📋 Profession Tasks   │
                                │  🏋️ Health Goals       │
                                │  🎯 Career Goals       │
                                └────────────────────────┘
```
- **BMI-Aware Nutrition**: Calculates daily protein and water targets logically scaling by body limits.
- **Career-Skill Alignment**: Generates specific tasks dynamically matching CS, Medical, Business, and varied pathways.
- **Adaptive Loading**: Limits and updates suggested checkboxes without duplicating daily routines.

---

<p align="center">
  Built with ❤️ by <strong>Mukesh Raj</strong>
</p>
