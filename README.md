# Smart Greenhouse Management System

A web-based platform to simulate and manage smart greenhouses.
This project is designed to support real-world greenhouse scenarios by allowing users to create, monitor, and control greenhouse environments using a flexible permission system and real-time data handling.

---

## 🚀 Features

* **User Registration & Authentication**

  * Each user can sign up and manage their own greenhouses.
  * Uses a **Custom User model** (`CustomUser`) for authentication and user management.
  * Supports **JWT Authentication**:
    * Users can log in via an API endpoint.
    * On successful login, the system generates **access** and **refresh JWT tokens**.
    * Tokens are used for authenticated requests to protected endpoints.

* **Greenhouse Ownership**

  * Users can create multiple greenhouses.
  * Each greenhouse has an owner (admin).

* **Zone Management**

  * Greenhouses can be divided into multiple *zones* (e.g., temperature zones).
  * Each zone holds real-time environmental data (temperature, humidity, smoke, etc).
  * **Real-time updates via WebSocket** for zone data streaming.

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
git clone https://github.com/Mahdi-jahanfar-dev/GreenLand.git
cd GreenLand
```
### 2. Create .env File
```bash
POSTGRES_DB=your_db_name
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
```
### 3. Run With Docker Compose
```bash
sudo docker-compose up --build
```

## 🔐 JWT Authentication Example
### A simple login API using Django REST Framework and SimpleJWT:
### Serializer
```
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
        
    def validate(self, data):
        
        user = authenticate(
            username = data.get("username"),
            password = data.get("password")
        )
        
        if not user:
            raise serializers.ValidationError("username or password wrong")
        
        data["user"] = user
        return data
```
### views
```
class UserLoginVIew(APIView):
    
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        
        refresh_token = RefreshToken.for_user(user)
        
        return Response ({
            "user": user.username,
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token),
            },
            status=status.HTTP_200_OK
        )
```

## 📌 Future Enhancements
* WebSocket-based real-time frontend updates
* Sensor integration for real hardware communication
* Graphical dashboard for zone statistics
* Alerts and automation triggers (e.g., if temperature too high)
