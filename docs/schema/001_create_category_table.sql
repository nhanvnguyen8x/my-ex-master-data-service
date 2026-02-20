-- Create categories table (PostgreSQL)
-- Run first: no dependencies.

CREATE TABLE categories (
  id          VARCHAR(50) PRIMARY KEY,
  name        VARCHAR(100) NOT NULL,
  slug        VARCHAR(100) NOT NULL UNIQUE,
  icon        VARCHAR(10),
  description TEXT,
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
