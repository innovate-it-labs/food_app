Here's your complete content converted into a **professionally styled `README.md`** for your Django **Foodie App**, while keeping all your content intact and improving its presentation and structure:

---

```markdown
# 🍔 Foodie App

A Django-based full-stack food delivery platform with role-based user management, product listings, shopping carts, and order processing.

---

## ✅ Structure for the Foodie App Documentation

---

### 1. 📘 Project Overview

**Foodie** is a Django-based web application that implements:

- Secure authentication for users
- Role-based profile creation
- Two types of users: **Customer** and **Seller**
- Sellers can add new **categories**, **subcategories**, and **products**
- Customers can **add items to cart** and **place orders**

---

### 2. 📁 Directory Structure

Project codebase organization:

```

foodie/
├── main/                  # Main Django project settings
│   ├── settings/          # Modular settings (JWT, Google login, Email config)
│   └── urls.py            # URL routing for all apps
├── users/                 # User app (auth, profile, Google login, role setup)
├── products/              # Product catalog (categories, subcategories)
├── cart/                  # Cart management (add, remove, retrieve)
├── orders/                # Order processing (place, track)
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md

````

---

### 3. ⚙️ Tech Stack

- **Backend**: Django, Python, Django REST Framework  
- **Database**: SQLite  
- **Authentication**: Custom auth, Google Login (all-auth), JWT, password reset  
- **Deployment**: Docker, Gunicorn, Nginx (optional)

---

### 4. 🚀 Getting Started

#### Step-by-step instructions:

1. **Clone the Repo**

```bash
git clone https://github.com/ksaidurga/foodie.git
cd foodie
````

2. **Create Virtual Environment**

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. **Setup Database and Migrate**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Run the Development Server**

```bash
python manage.py runserver
```

---

### 5. 🧑‍💻 Core Features

* ✅ User registration and login
* ✅ Forgot Password & Reset Password
* ✅ Customer and Seller Profiles
* ✅ Google login using all-auth
* ✅ JWT Authentication
* ✅ Set user type on registration
* ✅ Seller-only: Create/remove categories, subcategories, products
* ✅ Add to Cart & Remove from Cart
* ✅ Checkout and Order Summary
* ✅ Admin panel for item management

---

### 6. 🧱 Models Description

---

## 👤 `users/models.py`

### 6.1. `CustomUser`

Custom user model replacing Django's default.

| Field         | Description                       |
| ------------- | --------------------------------- |
| `email`       | Unique identifier for login       |
| `full_name`   | Optional full name                |
| `user_type`   | Either `customer` or `seller`     |
| `is_active`   | Boolean: is the account active?   |
| `is_staff`    | Boolean: can access Django admin? |
| `date_joined` | Timestamp of registration         |

> ⚙️ **Authentication Settings:**

```python
USERNAME_FIELD = 'email'
REQUIRED_FIELDS = []
```

---

### 6.2. 🧾 `CustomerProfile`

Linked to `CustomUser` when `user_type = customer`.

| Field              | Description                                |
| ------------------ | ------------------------------------------ |
| `user`             | One-to-One with `CustomUser`               |
| `name`             | Customer name                              |
| `address, city...` | Optional address fields                    |
| `preferences`      | JSON field for preferences                 |
| `profile_picture`  | Optional image (stored in `profile_pics/`) |

---

### 6.3 🛍️ `SellerProfile`

Linked to `CustomUser` when `user_type = seller`.

| Field        | Description                                    |
| ------------ | ---------------------------------------------- |
| `user`       | One-to-One with `CustomUser`                   |
| `shop_name`  | Seller's shop name                             |
| `gst_number` | GST number for legal purposes                  |
| `address...` | Address and city info                          |
| `logo`       | Optional shop logo (stored in `seller_logos/`) |
| `verified`   | Boolean flag for admin approval                |

---

## 📦 `products/models.py`

### 🔹 `Category`

Represents a product category.

| Field         | Type         | Description                 |
| ------------- | ------------ | --------------------------- |
| `Category_id` | BigAutoField | Primary Key                 |
| `name`        | CharField    | Unique name of the category |

---

### 🔹 `SubCategory`

Subcategory under a main category.

| Field            | Type         | Description            |
| ---------------- | ------------ | ---------------------- |
| `SubCategory_id` | BigAutoField | Primary Key            |
| `name`           | CharField    | Subcategory name       |
| `category`       | ForeignKey   | Linked to a `Category` |

---

### 🔹 `Product`

Core product model with seller and category linkage.

| Field              | Type         | Description              |
| ------------------ | ------------ | ------------------------ |
| `product_id`       | BigAutoField | Primary Key              |
| `seller`           | ForeignKey   | Linked to a Seller User  |
| `category`         | ForeignKey   | Product category         |
| `subcategory`      | ForeignKey   | Optional subcategory     |
| `name`             | CharField    | Product name             |
| `rating`           | DecimalField | Product rating (0.0–9.9) |
| `distance`         | DecimalField | Delivery distance        |
| `description`      | TextField    | Product details          |
| `price`            | DecimalField | Product price            |
| `delivery_charges` | CharField    | "free" or "paid"         |
| `is_active`        | BooleanField | Availability status      |
| `created_at`       | DateTime     | Timestamp on creation    |
| `updated_at`       | DateTime     | Timestamp on update      |
| `brand`            | CharField    | Optional brand info      |
| `weight`           | DecimalField | Product weight           |
| `tags`             | CharField    | Comma-separated tags     |

---

### 🔹 `ProductImage`

Represents product images.

| Field      | Type       | Description                              |
| ---------- | ---------- | ---------------------------------------- |
| `product`  | ForeignKey | Linked to a `Product`                    |
| `image`    | ImageField | Image file (stored in `product_images/`) |
| `alt_text` | CharField  | Optional alt description                 |

---

## 🔁 Product Relationships

* One `Category` → Many `SubCategories`
* One `Category/SubCategory` → Many `Products`
* One `Product` → Many `ProductImage`
* One `Seller` → Many `Products`

---

## 🛒 `cart/models.py`

### 🔹 `Cart`

Represents a user's shopping cart.

| Field        | Type          | Description                   |
| ------------ | ------------- | ----------------------------- |
| `user`       | ForeignKey    | Linked to Django `User` model |
| `created_at` | DateTimeField | Auto timestamp at creation    |
| `is_active`  | BooleanField  | Active/inactive status        |

**String Representation:**

```python
"Cart <id> - User <user_email>"
```

---

### 🔹 `CartItem`

Represents a product in a cart.

| Field      | Type            | Description             |
| ---------- | --------------- | ----------------------- |
| `cart`     | ForeignKey      | Linked to `Cart`        |
| `product`  | ForeignKey      | Linked to `Product`     |
| `quantity` | PositiveInteger | Quantity of the product |

**String Representation:**

```python
"<quantity> of <product_name> in Cart <cart_id>"
```

---

### 🔁 Cart Relationships

* A `Cart` belongs to a `User`
* A `Cart` contains multiple `CartItems`
* Each `CartItem` is linked to a specific `Product`

---

## 🔐 Auth & Security

* JWT-based authentication for APIs
* Google login via `allauth`
* Email-based reset for password recovery
* Role-based logic to restrict seller/customer actions

---


Here is a well-structured **README.md** file for your **orders** Django app based on the provided models:

---

## 🛒 Orders App

The `orders` app handles the creation and management of customer orders and order items in the system. It maintains order statuses, timestamps, total pricing, and relationships with users and products.

---

### 📂 Models

#### 1. **Order**

Represents a customer order.

**Fields:**

* `user`: ForeignKey to the authenticated user placing the order.
* `created_at`: DateTime when the order was created (auto-generated).
* `status`: Status of the order. Choices:

  * `PENDING`
  * `PROCESSING`
  * `COMPLETED`
  * `CANCELLED`
* `total_amount`: Total cost of the order (decimal value).

**Example:**

```python
Order.objects.create(user=request.user, total_amount=499.99)
```

---

#### 2. **OrderItem**

Represents an individual item within an order.

**Fields:**

* `order`: ForeignKey to the associated order.
* `product`: ForeignKey to the purchased product.
* `quantity`: Number of product units ordered.
* `price`: Price per unit at the time of order.

**Example:**

```python
OrderItem.objects.create(
    order=my_order,
    product=my_product,
    quantity=2,
    price=249.99
)
```

---

### 🔁 Relationships

* One `Order` ➡️ many `OrderItem`s.
* Each `OrderItem` is linked to one `Product` and one `Order`.
* Each `Order` belongs to a single `User`.

---

### 🛠 Usage

* Useful for generating order history.
* Helps in tracking the lifecycle of an order.
* Calculates total amounts for checkout/invoice systems.

---

### ✅ Example Workflow

1. A user places an order.
2. The system creates an `Order` instance.
3. For each product in the cart, create `OrderItem` entries linked to that order.
4. Total price is calculated and saved in `Order.total_amount`.

---
