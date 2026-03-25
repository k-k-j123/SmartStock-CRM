# SmartStock - CRM & Inventory Management System

SmartStock is a modern, efficient CRM and Inventory Management application built with **Spring Boot** and **MongoDB**. It provides a robust backend for managing customers, tracking product inventory, and processing sales with intelligent automation.

## 🚀 Features

- **Customer Management (CRM)**: Maintain detailed customer profiles including contact info, total spending, and visit frequency.
- **Inventory Tracking**: Manage product stock levels, categories, and pricing with automatic low-stock alerts.
- **Intelligent Sales Flow**: 
   - **Automatic Customer Discovery**: Create sales using just a customer's phone number. If they don't exist, the system creates them automatically.
   - **Stock Automation**: Real-time stock decrementing upon successful sales.
   - **Loyalty Insights**: Automatically tracks customer "Loyal" status based on purchase history.
- **AI-Powered Insights**: Integrated AI service for advanced data processing and insights.
- **API Documentation**: Built-in Swagger/OpenAPI support for easy testing and integration.

## 🛠️ Tech Stack

- **Backend**: Java 21, Spring Boot (Data MongoDB, Web), MongoDB (NoSQL Database)
- **AI Service**: Python 3.12, FastAPI, Uvicorn
- **Frontend**: React, Vite, TailwindCSS
- **Tools**: Docker, Docker Compose, Maven, Lombok, SpringDoc OpenAPI

## 📦 Prerequisites

Ensure you have the following installed on your local machine:

- **JDK 21** or higher
- **Python 3.12+**
- **Node.js 18+**
- **Docker & Docker Compose**
- **MongoDB** (if running services individually without Docker)

---

## 🐳 Docker Deployment (Recommended)

The easiest way to run the entire SmartStock ecosystem is using Docker Compose.

1. **Build and start all services**:
   ```bash
   docker-compose up --build
   ```

2. **Access the services**:
   - **Frontend UI**: [http://localhost:5173](http://localhost:5173)
   - **Backend API**: [http://localhost:8080](http://localhost:8080)
   - **AI Service API**: [http://localhost:8000](http://localhost:8000)
   - **Swagger UI**: [http://localhost:8080/swagger-ui/index.html](http://localhost:8080/swagger-ui/index.html)

---

## ⚙️ Local Development (Individual Services)

If you prefer to run services individually, follow the steps below. Ensure a MongoDB instance is running locally on `mongodb://localhost:27017/smartstock`.

### 1. Backend (Spring Boot)
1. **Navigate to the root directory**:
   ```bash
   cd SmartStock
   ```
2. **Build and run**:
   ```bash
   ./mvnw spring-boot:run
   ```
   *Alternative: Build JAR and run:*
   ```bash
   ./mvnw clean package
   java -jar target/SmartStock-0.0.1-SNAPSHOT.jar
   ```

### 2. AI Service (FastAPI)
1. **Navigate to the AI service directory**:
   ```bash
   cd ai-service
   ```
2. **Setup virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```
3. **Install dependencies and run**:
   ```bash
   pip install -r requirements.txt
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

### 3. Frontend (React)
1. **Navigate to the UI directory**:
   ```bash
   cd SmartStockUI
   ```
2. **Install dependencies and run**:
   ```bash
   npm install
   npm run dev
   ```

---

## 📖 API Documentation

Once the backend is running, you can access the interactive documentation:
- **Swagger UI**: [http://localhost:8080/swagger-ui/index.html](http://localhost:8080/swagger-ui/index.html)
- **OpenAPI Spec**: `http://localhost:8080/v3/api-docs`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.
