# Volleyball Rotation Tracker – High-Level Design Overview

## 1. Purpose
The goal of this project is to create a simple, fast, coach-friendly tool for tracking volleyball player rotations and substitutions during a live match. Coaches currently track these changes manually on paper, which is slow, error-prone, and difficult to review later. This app aims to automate that process.

---

## 2. Target User
**Primary User:**  
- Volleyball coaches, team managers, or assistants  
- Using a phone, tablet, or laptop during a match  

**User needs:**  
- Update rotations quickly  
- Log substitutions with minimal taps  
- See the current court layout clearly  
- Review rotation history

---

## 3. High-Level Features (MVP)
1. Create a match and starting lineup  
2. Display current rotation (positions 1–6)  
3. Rotate the court with one button  
4. Substitute players (select position + bench player)  
5. Automatically log every event  
6. Show an event timeline  
7. Simple UI, no login needed for V1

---

## 4. Screens Overview

### Screen A — Match Setup
- Enter team name (optional)
- Enter opponent name (optional)
- Select 6 starting players from roster
- Button: **Start Match**

### Screen B — Live Match Screen
- Large 6-position court layout  
- **Rotate** button  
- **Substitution controls:**  
  - Dropdown: Position (1–6)  
  - Dropdown: Bench player  
  - Button: **Substitute**  
- Event log showing sequence of actions

---

## 5. System Architecture (Simple Version)


### Frontend
- Displays UI (court, buttons, log)
- Sends requests to backend (rotate, substitute)
- Shows updated rotation state

### Backend (Flask)
- Exposes API endpoints:
  - `/api/start-set`
  - `/api/rotate`
  - `/api/substitute`
  - `/api/state`
  - `/api/events`

### Logic Layer
- Manages current rotation state
- Applies substitutions and rotations
- Logs events

---

## 6. Data Model (Simple Version)

### Player
- id  
- name  
- number  
- is_libero (optional)

### RotationState
- court (list of 6 player IDs in position order)
- bench (remaining player IDs)
- sequence number

### Event
- sequence
- event_type (`start`, `rotation`, `substitution`)
- details (JSON)

---

## 7. MVP Limitations
- Only supports one team and one match at a time  
- No user accounts  
- No persistent database (state resets on server restart)  
- Basic UI styling

These will be expanded in future versions.

---

## 8. Future Expansions
- Multiple teams
- Multiple matches + sets
- Login accounts
- Database storage (SQLite/Postgres)
- Illegal rotation detection
- Exportable rotation logs
- Mobile app (React Native or PWA)
