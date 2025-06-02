# Smart Greenhouse Management System

A web-based platform to simulate and manage smart greenhouses.
This project is designed to support real-world greenhouse scenarios by allowing users to create, monitor, and control greenhouse environments using a flexible permission system and real-time data handling.

---

## 🚀 Features

* **User Registration & Authentication**

  * Each user can sign up and manage their own greenhouses.

* **Greenhouse Ownership**

  * Users can create multiple greenhouses.
  * Each greenhouse has an owner (admin).

* **Zone Management**

  * Greenhouses can be divided into multiple *zones* (e.g., temperature zones).
  * Each zone holds real-time environmental data (temperature, humidity, smoke, etc).

* **Advanced Permission System**

  * Greenhouse owners can invite other users to their greenhouses.
  * Each invited user gets a role (admin, read-only, etc).
  * Users can control whether they allow others to add them to greenhouses.

* **Real-Time Data Updates**

  * Uses **Celery** + **Redis** + **Celery Beat** to periodically refresh zone data.

* **Dockerized Architecture**

  * Entire project runs in Docker containers for easy deployment and scalability.

---

## ⚙️ Tech Stack

* **Backend:** Django
* **Task Queue:** Celery
* **Scheduler:** Celery Beat
* **Broker:** Redis
* **Database:** PostgreSQL
* **Containerization:** Docker / Docker Compose

---

## 🐳 Running the Project (Development)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create `.env` file

Create a `.env` file in the root directory and define your environment variables:

```env
POSTGRES_DB=your_db_name
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
```

### 3. Run with Docker Compose

```bash
docker-compose up --build
```

This will spin up the following services:

* `backend`: Django application (port 8000)
* `postgres_db`: PostgreSQL database (port 5432)
* `backend_redis`: Redis broker (port 6379)
* `backend_celery`: Celery worker
* `backend_celery_beat`: Celery scheduler for periodic tasks

---

## 📌 Future Enhancements

* WebSocket-based real-time frontend updates
* Sensor integration for real hardware communication
* Graphical dashboard for zone statistics
* Alerts and automation triggers (e.g., if temperature too high)

---
