# GEMINI.md - SmartStock Project Context

This document provides foundational context, architectural overview, and development guidelines for the **SmartStock** CRM & Inventory Management System.

## 🚀 Project Overview
SmartStock is a modern distributed system designed for retail inventory tracking and AI-driven business analytics.

- **Primary Backend:** Java 21, Spring Boot 4.0.2 (Handles CRUD, Transactions, and Inventory).
- **AI Microservice:** Python 3.12, FastAPI, Pandas (Provides demand forecasting and business insights).
- **Frontend UI:** React 18, Vite, TypeScript, Tailwind CSS, Shadcn UI (Interactive dashboard and management).
- **Database:** MongoDB (Shared by both services).
- **Interactive UI:** Swagger / OpenAPI available for both services.

## 🏗️ Architecture & Conventions

### Directory Structure
- `src/main/java/com.kaushik.SmartStock`: Core Java backend logic.
    - `Documents`: MongoDB collections (`customers`, `products`, `sales`).
    - `DTO`: API request/response objects.
    - `Service`: Transactional business logic (e.g., Sales Flow).
- `ai-service/`: Python-based AI analytics service.
    - `app/services`: Analytics and Prediction logic using Pandas.
    - `app/routes`: FastAPI endpoints for AI insights.
- `SmartStockUI/`: React-based frontend dashboard.
    - `src/pages`: Main application views (Analytics, Customers, Products, etc.).
    - `src/components`: Reusable UI components (Shadcn UI).
    - `src/hooks`: Custom React hooks (API, mobile state).
    - `src/lib`: API clients and utility functions.

### Key Business Logic
1.  **Sales Flow (Java):** Automatically updates stock levels and customer loyalty snapshots during transactions.
2.  **AI Analytics (Python):** 
    - **Demand Forecasting:** Uses Simple Moving Average (SMA) on sales history.
    - **Restock Suggestions:** Predicts stockouts and suggests reorder quantities.
    - **Customer Segmentation:** Identifies top-tier loyal customers based on lifetime spend.
3.  **Frontend Dashboard (React):** 
    - Real-time stock alerts and visual data analytics using Recharts.
    - Modular forms for inventory and customer management.

### Coding Standards
- **Java:** Use Lombok annotations; strictly use DTOs for API boundaries.
- **Python:** Use Pydantic for models; maintain modularity in service/route layers.
- **Frontend:** Use TypeScript for type safety; prefer functional components; follow Shadcn UI patterns.
- **REST:** Both services follow standard RESTful conventions.

## 🛠️ Building and Running

### Main Backend (Java)
- **Run:** `./mvnw spring-boot:run`
- **Build:** `./mvnw clean install`
- **Port:** `8080` (Swagger: `/swagger-ui/index.html`)

### AI Microservice (Python)
- **Setup:** `cd ai-service && python -m venv venv && .\venv\Scripts\activate && pip install -r requirements.txt`
- **Run:** `uvicorn app.main:app --reload`
- **Port:** `8000` (Swagger: `/docs`)

### Frontend UI (React)
- **Setup:** `cd SmartStockUI && npm install`
- **Run:** `npm run dev`
- **Build:** `npm run build`
- **Port:** `5173` (Default Vite port)

### Docker Deployment (Recommended)
You can run the core stack (MongoDB, Java Backend, and AI Service) using Docker Compose:
- **Command:** `docker-compose up --build`
- **Ports:**
    - Java Backend: `8080`
    - AI Service: `8000`
    - MongoDB: `27017`

### Configuration
- **Database:** `mongodb://localhost:27017/smartstock_crm`
- **Environment:** Requires JDK 21, Python 3.12+, and Node.js 18+.
- **Docker Environment:** Managed via `docker-compose.yml`.

## 🧪 Testing Strategy
- **Java:** Integration tests in `src/test/java` using `@SpringBootTest`.
- **Python:** Service-level verification using Pandas on mock MongoDB collections.
- **Frontend:** Unit testing with Vitest and E2E testing with Playwright (in `SmartStockUI/src/test`).

## 📝 Future TODOs
- [x] Implement AI Analytics Microservice.
- [x] Add Docker and Docker Compose support for easy deployment.
- [x] Implement initial React Frontend.
- [ ] Implement a Global Exception Handler in Java.
- [ ] Add Stock Alert notifications (via email or SMS).
- [ ] Add user authentication (Spring Security).
- [ ] Implement pagination for large sales/product lists.
- [ ] Add Dockerfile for SmartStockUI and integrate into `docker-compose.yml`.
