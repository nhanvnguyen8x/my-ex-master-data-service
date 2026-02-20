-- Create subcategories table (PostgreSQL)
-- Depends on: 001_create_category_table.sql (categories must exist).

CREATE TABLE subcategories (
  id          VARCHAR(50) PRIMARY KEY,
  category_id VARCHAR(50) NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
  name        VARCHAR(100) NOT NULL,
  slug        VARCHAR(100) NOT NULL,
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_subcategories_category_id ON subcategories(category_id);
