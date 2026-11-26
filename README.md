# FlexiSAF AI-Native Python Internship — Beginner Stage

**Intern:** Chinedu Iroanyah
**Stage:** Beginner (4 months / 13 guided weeks)
**Programme:** FlexiSAF AI-Native Python Programming Internship
**AI Rule:** No AI-generated code — all code is learner-written and explained.

---

## 📋 About This Repository

This repository contains my weekly deliverables and four embedded projects
for the **Beginner stage** of the FlexiSAF AI-Native Python Programming
Internship. It documents my progression from zero programming experience
to building complete Python applications.

Each week has its own folder with a dedicated `README.md` explaining:
- What I learned
- How to run the code
- What evidence is included

---

## 📍 Current Status

**Current stage:** Beginner (Week 9 of 13 complete, Week 10 in progress)
**Last updated:** 2026-11-26

---

## 🗂️ Weekly Submissions

| Week | Topic | Deliverable | Status |
|------|-------|-------------|--------|
| [01](./week-01-setup/) | Setup & Programming Mindset | Environment checklist, first script, flowchart | ✅ |
| [02](./week-02-syntax/) | Syntax, Variables & I/O | Five mini-programs | ✅ |
| [03](./week-03-project-1-number-decision-toolkit/) | **Project 1** | Number & Decision Toolkit | ✅ |
| [04](./week-04-collections/)| Collections & Data Organisation | Contact book & score exercises | ✅ |
| [05](./week-05-functions-modules/) | Functions, Modules & Clean Code | Utility package (≥6 functions) | ✅ |
| [06](./week-06-project-2-expense-tracker/) | **Project 2** | File-Based Expense Tracker | ✅ |
| [07](./week-07-oop-fundamentals/) | OOP Fundamentals | Two-class domain model | ✅ |
| 08 | Git, GitHub & Collaboration | Repo with PR, issue, peer review | ✅ |
| [09](./week-09-project-3-public-data-explorer/) | **Project 3** | Public Data Explorer | ✅ |
| 10 | SQL & SQLite | CRUD record manager | 🟡 |
| 11 | Testing, Debugging & Logging | Test suite (≥8 tests) + bug log | ⭕ |
| 12 | Environments, Packages & Docs | Installable project + docs | ⭕ |
| 13 | **Project 4** | Small Business Operations Manager | ⭕ |

**Legend:** ⭕ Not started · 🟡 In progress · ✅ Completed

**Progress:** 9 / 13 weeks complete (69.23%)

---

## 🛠️ Tools & Environment

| Tool | Purpose |
|------|---------|
| Python 3.x | Primary language |
| VS Code | Code editor |
| Git & GitHub | Version control |
| Render | Deployment (for deployed services) |
| pytest | Testing (from Week 11) |

---

## 🚀 How to Run Any Week

Each week folder contains its own `README.md` with specific instructions.
In general:

```bash
# Clone the repository
git clone https://github.com/chinedudeoracle/flexisaf-ai-native-python-beginner.git
cd flexisaf-ai-native-python-beginner

# Navigate to a specific week
cd week-01-setup

# (Weeks 1–7 use only the standard library — no installs needed.)
# From Week 11 onward:
python -m venv .venv
source .venv/bin/activate          # macOS/Linux
.venv\Scripts\Activate.ps1         # Windows PowerShell
pip install -r requirements.txt

# Run the code
python <script_name>.py