# ⚡ FastAPI — Learning Journey

> **React Developer → Full Stack GenAI Engineer**
> Building a production-ready backend with FastAPI + PostgreSQL, one day at a time.

---

## 📅 Day-by-Day Progress

| Day | Commit | What I Learned |
|-----|--------|----------------|

| **Day 01** | `setup and explore path and query parameter` | FastAPI setup, path params (`/tasks/{id}`), query params (`?limit=10`) |

| **Day 02** | `explore all http method crud method` | GET, POST, PUT, PATCH, DELETE — REST ka full picture |

| **Day 03** | `understand folder structure` | Clean project structure — routes, controllers, models, schemas alag kiye |

| **Day 04** | `connect postgresql database with fastapi` | SQLAlchemy engine setup, `get_db` dependency, `.env` config |

| **Day 05** | `make model and create table` | SQLAlchemy `TaskModel` banaya, `Base.metadata.create_all()` se table create kiya |

| **Day 06** | `make a basic controller import to route file` | Controller aur Route alag kiye — separation of concerns |

| **Day 07** | `create post route and safe data in database` | POST route, Pydantic schema validation, `db.add()` → `db.commit()` → `db.refresh()` |

| **Day 08** | `make get route for getting all tasks present in db` | `db.query(TaskModel).all()` — saari tasks fetch karna 

| **Day 09** | `make a get route for get a specific task in database `| query params

| **Day 10** | `make route of delete and update task in database` | PUT/PATCH for update, DELETE route, 

| **Day 11** | `production level code improvements` | Folder structure best practices, environment variables, proper error handling, response models, correct HTTP status codes |

---

## 🗂️ Folder Structure

```
fastapi/
├── day-01/          # Path & Query params
├── day-02/          # HTTP Methods
├── day-03/          # Folder Structure
├── day-04/          # PostgreSQL Connection
├── day-05/          # Models & Tables
├── day-06/          # Controller + Route split
├── day-07/          # POST — Create Task
├── day-08/          # GET — All Tasks
├── day-09/          # GET — Single Task
└── day-10/          # PUT/DELETE — Update & Delete
└── day-11/          # Production-level improvements
```

---

## 🛠️ Tech Stack

```
Backend      →   FastAPI (Python)
Database     →   PostgreSQL
ORM          →   SQLAlchemy
Validation   →   Pydantic
API Testing  →   Thunder Client / Postman
```

---

## 📦 CRUD — What I Built

| Operation | Method | Route | Status |
|-----------|--------|-------|--------|
| Create Task | `POST` | `/tasks/create_task` | ✅ |
| Get All Tasks | `GET` | `/tasks/get_tasks` | ✅ |
| Get One Task | `GET` | `/tasks/get_task/{id}` | ✅ |
| Update Task | `PUT` | `/tasks/update_task/{id}` | ✅ |
| Delete Task | `DELETE` | `/tasks/delete_task/{id}` | ✅ |

---

## 💡 Key Learnings

- **`TaskSchema`** — ek hi schema se create aur update dono handle kiye
- **`db.refresh()` mat karo delete ke baad** — object session me rehta hi nahi
- **Controller ka argument order** route call se match hona chahiye
- **`db.query().filter().first()`** — `.get()` se better aur safe

---

## 🚀 Next Up

- [ ] JWT Authentication
- [ ] LLM APIs + Prompt Engineering
- [ ] RAG System with pgvector
- [ ] AI Agents with LangGraph

---
