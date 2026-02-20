-- Create products table (PostgreSQL)
-- Depends on: 002_create_subcategory_table.sql (subcategories must exist).

CREATE TABLE products (
  id             VARCHAR(50) PRIMARY KEY,
  subcategory_id VARCHAR(50) NOT NULL REFERENCES subcategories(id) ON DELETE CASCADE,
  name           VARCHAR(100) NOT NULL,
  slug           VARCHAR(100) NOT NULL,
  created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_products_subcategory_id ON products(subcategory_id);
