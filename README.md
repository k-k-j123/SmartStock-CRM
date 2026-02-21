# SmartStock - CRM & Inventory Management System

SmartStock is a modern, efficient CRM and Inventory Management application built with **Spring Boot** and **MongoDB**. It provides a robust backend for managing customers, tracking product inventory, and processing sales with intelligent automation.

## 🚀 Features

- **Customer Management (CRM)**: Maintain detailed customer profiles including contact info, total spending, and visit frequency.
- **Inventory Tracking**: Manage product stock levels, categories, and pricing with automatic low-stock alerts.
- **Intelligent Sales Flow**: 
    - **Automatic Customer Discovery**: Create sales using just a customer's phone number. If they don't exist, the system creates them automatically.
    - **Stock Automation**: Real-time stock decrementing upon successful sales.
    - **Loyalty Insights**: Automatically tracks customer "Loyal" status based on purchase history.
- **API Documentation**: Built-in Swagger/OpenAPI support for easy testing and integration.

## 🛠️ Tech Stack

- **Java 21**
- **Spring Boot** (Data MongoDB, Web)
- **MongoDB** (NoSQL Database)
- **Lombok** (Boilerplate reduction)
- **SpringDoc OpenAPI** (Swagger UI)

## 📦 Prerequisites

- **JDK 21** or higher
- **MongoDB** (running on `localhost:27017` by default)
- **Maven** (optional, wrapper included)

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/SmartStock.git
   cd SmartStock
   ```

2. **Configure Database**:
   Update `src/main/resources/application.properties` with your MongoDB URI if different from the default:
   ```properties
   spring.data.mongodb.uri=mongodb://localhost:27017/smartstock_crm
   ```

3. **Run the application**:
   ```bash
   ./mvnw spring-boot:run
   ```

## 📖 API Documentation

Once the application is running, you can access the interactive Swagger UI at:
- **Swagger UI**: [http://localhost:8080/swagger-ui/index.html](http://localhost:8080/swagger-ui/index.html)
- **OpenAPI Spec**: `http://localhost:8080/v3/api-docs`

### Key Endpoints

- `POST /api/customer`: Create a new customer profile.
- `GET /api/products`: List all inventory items.
- `POST /api/sales`: Process a sale (supports automatic customer creation via phone).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.
