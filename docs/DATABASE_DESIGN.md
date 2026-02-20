# Database Design: Experience Review Platform

This document describes the relational database schema for the Experience Review app as of the latest updates: **9 categories** (Cars, Laptops, Phones, Travel, Restaurants, Electronics, Food, Drink, Company), **subcategories** (brands or countries for Company), **products** (model-level, e.g. Innova, iPhone 15), **users**, and **reviews** (with optional year and category/subcategory/product links).

---

## Entity Relationship Overview

```
┌─────────────┐       ┌──────────────────┐       ┌─────────────┐       ┌─────────────┐
│  categories │──1:N──│  subcategories   │──1:N──│  products   │       │   users     │
└─────────────┘       └──────────────────┘       └─────────────┘       └──────┬──────┘
        │                        │                        │                    │
        └────────────────────────┴────────────────────────┴────────────────────┘
                                         │
                                    ┌────┴────┐
                                    │ reviews │  (category_id, subcategory_id?, product_id?, year?)
                                    └─────────┘
```

- **categories**: Cars, Laptops, Phones, Travel, Restaurants, Electronics, Food, Drink, Company.
- **subcategories**: Per-category (e.g. Toyota, Apple for Cars/Laptops/Phones; countries US, Vietnam for Company).
- **products**: Per subcategory where applicable (e.g. Innova, Fortuner for Toyota; no products for Company).
- **users**: Auth (username, password_hash).
- **reviews**: One per row; required `category_id`; optional `subcategory_id`, `product_id`, `year`; optional `user_id`.

---

## Table Definitions

### 1. `categories`

| Column      | Type         | Constraints     | Description        |
|------------|--------------|-----------------|--------------------|
| id         | VARCHAR(50)  | PRIMARY KEY     | e.g. cars, company |
| name       | VARCHAR(100) | NOT NULL        | Display name       |
| slug       | VARCHAR(100) | NOT NULL UNIQUE | URL-friendly      |
| icon       | VARCHAR(10)  |                 | Emoji or icon key  |
| description| TEXT         |                 | Short description  |
| created_at | TIMESTAMP    | DEFAULT NOW()   | Optional           |

### 2. `subcategories`

| Column      | Type         | Constraints   | Description          |
|------------|--------------|---------------|----------------------|
| id         | VARCHAR(50)  | PRIMARY KEY   | e.g. cars-toyota, company-vietnam |
| category_id| VARCHAR(50)  | NOT NULL, FK → categories(id) | Parent category |
| name       | VARCHAR(100) | NOT NULL      | e.g. Toyota, Vietnam |
| slug       | VARCHAR(100) | NOT NULL      | URL-friendly         |
| created_at | TIMESTAMP    | DEFAULT NOW() | Optional             |

**Index:** `idx_subcategories_category_id (category_id)`.

### 3. `products`

| Column         | Type         | Constraints   | Description            |
|----------------|--------------|---------------|------------------------|
| id             | VARCHAR(50)  | PRIMARY KEY   | e.g. cars-toyota-innova |
| subcategory_id | VARCHAR(50)  | NOT NULL, FK → subcategories(id) | Parent subcategory |
| name           | VARCHAR(100) | NOT NULL      | e.g. Innova, iPhone 15 |
| slug           | VARCHAR(100) | NOT NULL      | URL-friendly           |
| created_at     | TIMESTAMP    | DEFAULT NOW() | Optional               |

**Index:** `idx_products_subcategory_id (subcategory_id)`.

Not all subcategories have products (e.g. Company uses subcategories as countries only).

### 4. `users`

| Column        | Type         | Constraints   | Description     |
|---------------|--------------|---------------|-----------------|
| id            | UUID         | PRIMARY KEY   | Internal ID     |
| username      | VARCHAR(50)  | NOT NULL UNIQUE | Login name   |
| password_hash | VARCHAR(255) | NOT NULL      | Never store plain password |
| created_at    | TIMESTAMP    | DEFAULT NOW() |                 |

### 5. `reviews`

| Column         | Type         | Constraints   | Description                    |
|----------------|--------------|---------------|--------------------------------|
| id             | UUID         | PRIMARY KEY   |                                |
| user_id        | UUID         | NULLABLE, FK → users(id) | Who wrote it (if auth used) |
| category_id    | VARCHAR(50)  | NOT NULL, FK → categories(id) | Required category    |
| subcategory_id | VARCHAR(50)  | NULLABLE, FK → subcategories(id) | Optional (brand/country) |
| product_id     | VARCHAR(50)  | NULLABLE, FK → products(id) | Optional product   |
| year           | SMALLINT     | NULLABLE      | Model year (e.g. 2025); not used for Company |
| title          | VARCHAR(255) | NOT NULL      |                                |
| body           | TEXT         | NOT NULL      |                                |
| rating         | SMALLINT     | CHECK (1–5)   | 1–5 stars                      |
| created_at     | TIMESTAMP    | DEFAULT NOW() |                                |
| updated_at     | TIMESTAMP    | DEFAULT NOW() | Optional                        |

**Indexes:**

- `idx_reviews_category_id (category_id)`
- `idx_reviews_subcategory_id (subcategory_id)`
- `idx_reviews_product_id (product_id)`
- `idx_reviews_year (year)`
- `idx_reviews_created_at (created_at DESC)`
- `idx_reviews_user_id (user_id)` (if filtering by user)

---

## API ↔ Database Mapping

| App / API field   | Database column / table        |
|-------------------|-------------------------------|
| categoryId        | reviews.category_id → categories.id |
| subcategoryId    | reviews.subcategory_id → subcategories.id |
| productId        | reviews.product_id → products.id |
| year             | reviews.year                  |
| GET /reviews     | SELECT * FROM reviews (with optional filters) |
| GET /reviews/:id | SELECT * FROM reviews WHERE id = :id |
| POST /reviews    | INSERT INTO reviews (...)     |
| GET /categories  | SELECT * FROM categories      |
| GET /categories/:id | SELECT * FROM categories WHERE id = :id |

---

## Query Examples

**All categories:**
```sql
SELECT * FROM categories ORDER BY name;
```

**Subcategories for a category (e.g. Cars):**
```sql
SELECT * FROM subcategories WHERE category_id = 'cars' ORDER BY name;
```

**Products for a subcategory (e.g. Toyota):**
```sql
SELECT * FROM products WHERE subcategory_id = 'cars-toyota' ORDER BY name;
```

**All reviews (with category/subcategory/product names):**
```sql
SELECT r.*, c.name AS category_name, s.name AS subcategory_name, p.name AS product_name
FROM reviews r
JOIN categories c ON c.id = r.category_id
LEFT JOIN subcategories s ON s.id = r.subcategory_id
LEFT JOIN products p ON p.id = r.product_id
ORDER BY r.created_at DESC;
```

**Review by id:**
```sql
SELECT r.*, c.name AS category_name, s.name AS subcategory_name, p.name AS product_name
FROM reviews r
JOIN categories c ON c.id = r.category_id
LEFT JOIN subcategories s ON s.id = r.subcategory_id
LEFT JOIN products p ON p.id = r.product_id
WHERE r.id = :id;
```

**Reviews filtered by category, subcategory, product, year:**
```sql
SELECT * FROM reviews
WHERE category_id = :category_id
  AND (:subcategory_id IS NULL OR subcategory_id = :subcategory_id)
  AND (:product_id IS NULL OR product_id = :product_id)
  AND (:year IS NULL OR year = :year)
ORDER BY created_at DESC;
```

---

## Summary

- **categories**: 9 rows (Cars, Laptops, Phones, Travel, Restaurants, Electronics, Food, Drink, Company).
- **subcategories**: One table; includes brands (Toyota, Apple, …) and countries for Company (US, Vietnam, …).
- **products**: One table; only for subcategories that have products (no products for Company).
- **users**: Auth; optional link from reviews via user_id.
- **reviews**: Required category_id; optional subcategory_id, product_id, year; supports get all, get by id, and publish (insert).

See `schema.sql` in this folder for PostgreSQL DDL and seed data aligned with the app.
