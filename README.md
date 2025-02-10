
# Django REST API Service

This is a Django REST API service for test.

## Features

- **User Registration (`/signup`)**: Register users with email or phone number.
- **User Login (`/signin`)**: Authenticate users and return a Bearer token.
- **User Info (`/info`)**: Retrieve user ID and ID type.
- **Latency Check (`/latency`)**: Measure latency to `ya.ru`.
- **Logout (`/logout`)**: Invalidate tokens (all or current).

## API Endpoints

### 1. **`/signup`**  
Registers a new user using an ID (email or phone number) and password.
**Request:**
```json
{
  "id": "test@example.com",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "token": "<JWT_BEARER_TOKEN>"
}
```

### 2. **`/signin`**  
Logs in a user with ID and password.
**Request:**
```json
{
  "id": "test@example.com",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "token": "<JWT_BEARER_TOKEN>"
}
```

### 3. **`/info`**  
Returns user ID and ID type.
**Headers:**
```
Authorization: Bearer <JWT_BEARER_TOKEN>
```
**Response:**
```json
{
  "id": "test@example.com",
  "id_type": "email"
}
```

### 4. **`/latency`**  
Returns latency to `ya.ru`.
**Headers:**
```
Authorization: Bearer <JWT_BEARER_TOKEN>
```
**Response:**
```json
{
  "latency_ms": 120
}
```

### 5. **`/logout`**  
Logs out the user. Can delete all tokens or just the current one.
**Headers:**
```
Authorization: Bearer <JWT_BEARER_TOKEN>
Content-Type: application/json
```
**Request:**
```json
{
  "all": true
}
```
**Response:**
```json
{
  "message": "Logged out"
}
```

---

## Deployment Instructions

### 1. **Clone the Repository**

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3. **Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. **Run the Server**
```bash
python manage.py runserver
```

---

## CORS Configuration

The API allows access from any domain. CORS settings in `settings.py`:
```python
CORS_ALLOW_ALL_ORIGINS = True
```

---

## Postman Collection

A Postman collection with all API methods: `postman_collection.json`.

To use:
1. Import the collection into Postman.
2. Use the provided requests for testing.

---

## License

This project is licensed under the MIT License.
