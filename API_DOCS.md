# SmartStock API Documentation

This document provides a comprehensive overview of the SmartStock REST API endpoints, including request and response JSON structures, and the MongoDB database schema.

---

## 🗄️ Database Schema (MongoDB)

SmartStock uses MongoDB to store data. Below are the collection schemas based on the domain entities.

### 1. `customers` Collection
Stores customer profiles and loyalty tracking data.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `_id` | `ObjectId` | Unique identifier (represented as String in Java). |
| `name` | `String` | Full name of the customer. |
| `phone` | `String` | Unique contact number (used for lookup). |
| `email` | `String` | Email address. |
| `totalSpent` | `Double` | Cumulative amount spent by the customer. |
| `lastVisit` | `ISODate` | Timestamp of the last purchase. |
| `recentPurchaseIds` | `Array<String>` | List of IDs for recent transactions (used for loyalty status). |

### 2. `products` Collection
Stores inventory items.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `_id` | `ObjectId` | Unique identifier. |
| `name` | `String` | Product name. |
| `category` | `String` | Product category (e.g., Electronics, Grocery). |
| `costPrice` | `Double` | Price paid by the business to acquire the product. |
| `sellingPrice` | `Double` | Price charged to the customer. |
| `stockQuantity` | `Int32` | Current units in stock. |
| `lowStockThreshold` | `Int32` | Threshold for low-stock alerts. |

### 3. `sales` Collection
Stores transaction history.

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `_id` | `ObjectId` | Unique identifier. |
| `customerId` | `String` | Reference to the customer. |
| `totalAmount` | `Double` | Total cost of the sale. |
| `createdAt` | `ISODate` | Timestamp of the transaction. |
| `items` | `Array<Object>` | List of items sold (see structure below). |

**`items` object structure:**
- `productId`: `String`
- `name`: `String`
- `quantity`: `Int32`
- `priceAtSale`: `Double` (Snapshotted price at the time of transaction)

---

## 🚀 API Endpoints

### 1. Customer Management (`/api/customer`)

#### Create Customer
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "phone": "9876543210",
    "email": "john.doe@example.com"
  }
  ```
- **Response:** `200 OK` - `"customer created successfully"`

#### Get All Customers
- **Method:** `GET`
- **Response Body:**
  ```json
  [
    {
      "id": "65f1a...",
      "name": "John Doe",
      "phone": "9876543210",
      "email": "john.doe@example.com",
      "totalSpent": 1250.0,
      "lastVisit": "2024-03-07T10:00:00",
      "recentPurchaseIds": ["sale_001", "sale_002"]
    }
  ]
  ```

#### Get Customer by ID or Phone
- **Method:** `GET`
- **Endpoint:** `/api/customer/{id}` or `/api/customer/phone/{phone}`
- **Response Body:** Single customer object (same as above).

#### Update Customer
- **Method:** `PUT`
- **Endpoint:** `/api/customer/{id}`
- **Request Body:** Same as Create Customer.
- **Response:** `200 OK` - `"customer updated successfully"`

---

### 2. Product Management (`/api/product`)

#### Create Product
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "Wireless Mouse",
    "category": "Peripherals",
    "costPrice": 15.0,
    "sellingPrice": 25.0,
    "stockQuantity": 100,
    "lowStockThreshold": 10
  }
  ```
- **Response Body:** Created product object with `id`.

#### Get All Products
- **Method:** `GET`
- **Response Body:** Array of product objects.

#### Get Low Stock Products
- **Method:** `GET`
- **Endpoint:** `/api/product/low-stock?threshold=10`
- **Response Body:** Array of products where `stockQuantity <= threshold`.

#### Update Product
- **Method:** `PUT`
- **Endpoint:** `/api/product/{id}`
- **Request Body:** Updated product details.
- **Response Body:** Updated product object.

---

### 3. Sales Processing (`/api/sales`)

#### Create Sale (Process Transaction)
Automatically updates stock levels and customer loyalty data.
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "customerId": "optional_id",
    "customerPhone": "9876543210",
    "customerName": "John Doe",
    "items": [
      {
        "productId": "prod_123",
        "quantity": 2
      }
    ]
  }
  ```
- **Response Body:**
  ```json
  {
    "id": "sale_789",
    "customerId": "cust_456",
    "items": [
      {
        "productId": "prod_123",
        "name": "Wireless Mouse",
        "quantity": 2,
        "priceAtSale": 25.0
      }
    ],
    "totalAmount": 50.0,
    "createdAt": "2024-03-07T11:45:00"
  }
  ```

#### Get All Sales
- **Method:** `GET`
- **Response Body:** Array of sale response objects.

#### Delete Sale
- **Method:** `DELETE`
- **Endpoint:** `/api/sales/{id}`
- **Response:** `200 OK` - `"Sale deleted successfully"`

---

### 4. AI Analytics Microservice (`:8000/analytics`)
This service runs independently on port `8000` and provides business intelligence insights using Python and Pandas.

#### Get Best Selling Products
Returns the top 10 products based on quantity sold in the last 30 days.
- **Method:** `GET`
- **Endpoint:** `http://localhost:8000/analytics/best-products`
- **Response Body:**
  ```json
  [
    {
      "productId": "prod_123",
      "name": "Milk",
      "quantitySold": 150,
      "totalRevenue": 4500.0
    }
  ]
  ```

#### Get Restock Suggestions
Predicts demand for the next 7 days and suggests reorder quantities if stock is insufficient.
- **Method:** `GET`
- **Endpoint:** `http://localhost:8000/analytics/restock-suggestions`
- **Response Body:**
  ```json
  [
    {
      "product": "Milk",
      "currentStock": 20,
      "predictedDemand": 45,
      "suggestedOrder": 25
    }
  ]
  ```

#### Get Loyal Customers
Returns the top 10 customers based on cumulative spending.
- **Method:** `GET`
- **Endpoint:** `http://localhost:8000/analytics/loyal-customers`
- **Response Body:**
  ```json
  [
    {
      "customerId": "65f1a...",
      "name": "Rahul",
      "phone": "9876543210",
      "totalSpent": 4000.0,
      "lastVisit": "2026-03-02"
    }
  ]
  ```

#### AI Recommendations (Combined)
Returns a unified view of best sellers, restock suggestions, and loyal customers.
- **Method:** `GET`
- **Endpoint:** `http://localhost:8000/analytics/recommendations`
- **Response Body:**
  ```json
  {
    "bestSellingProducts": [...],
    "restockSuggestions": [...],
    "loyalCustomers": [...]
  }
  ```

---

## 🔍 Interactive API Documentation (Swagger UI)

SmartStock provides interactive UI to test the API endpoints directly from your browser.

- **Main Backend (Java):** `http://localhost:8080/swagger-ui/index.html`
- **AI Microservice (Python):** `http://localhost:8000/docs`


