-- Create reviews table (PostgreSQL)
-- Depends on: 001 categories, 002 subcategories, 003 products, 004 users.

CREATE TABLE reviews (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id        UUID REFERENCES users(id) ON DELETE SET NULL,
  category_id    VARCHAR(50) NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
  subcategory_id VARCHAR(50) REFERENCES subcategories(id) ON DELETE SET NULL,
  product_id     VARCHAR(50) REFERENCES products(id) ON DELETE SET NULL,
  year           SMALLINT,
  title          VARCHAR(255) NOT NULL,
  body           TEXT NOT NULL,
  rating         SMALLINT CHECK (rating >= 1 AND rating <= 5),
  created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_reviews_category_id    ON reviews(category_id);
CREATE INDEX idx_reviews_subcategory_id ON reviews(subcategory_id);
CREATE INDEX idx_reviews_product_id     ON reviews(product_id);
CREATE INDEX idx_reviews_year           ON reviews(year);
CREATE INDEX idx_reviews_created_at     ON reviews(created_at DESC);
CREATE INDEX idx_reviews_user_id        ON reviews(user_id);
