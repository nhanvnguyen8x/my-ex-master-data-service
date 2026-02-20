-- Experience Review Platform - Database Schema (updated)
-- PostgreSQL. Aligned with app: 9 categories, subcategories (brands + Company countries), products, users, reviews (with year).

-- ============== CATEGORIES ==============
CREATE TABLE categories (
  id          VARCHAR(50) PRIMARY KEY,
  name        VARCHAR(100) NOT NULL,
  slug        VARCHAR(100) NOT NULL UNIQUE,
  icon        VARCHAR(10),
  description TEXT,
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============== SUBCATEGORIES (Category → Subcategory: brands or countries for Company) ==============
CREATE TABLE subcategories (
  id          VARCHAR(50) PRIMARY KEY,
  category_id VARCHAR(50) NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
  name        VARCHAR(100) NOT NULL,
  slug        VARCHAR(100) NOT NULL,
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_subcategories_category_id ON subcategories(category_id);

-- ============== PRODUCTS (Subcategory → Product; not all subcategories have products) ==============
CREATE TABLE products (
  id             VARCHAR(50) PRIMARY KEY,
  subcategory_id VARCHAR(50) NOT NULL REFERENCES subcategories(id) ON DELETE CASCADE,
  name           VARCHAR(100) NOT NULL,
  slug           VARCHAR(100) NOT NULL,
  created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_products_subcategory_id ON products(subcategory_id);

-- ============== USERS (auth) ==============
CREATE TABLE users (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username      VARCHAR(50) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============== REVIEWS ==============
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

-- ============== SEED: CATEGORIES (9) ==============
INSERT INTO categories (id, name, slug, icon, description) VALUES
  ('cars', 'Cars', 'cars', '🚗', 'Vehicle reviews and experiences'),
  ('laptops', 'Laptops', 'laptops', '💻', 'Laptop and computer reviews'),
  ('phones', 'Phones', 'phones', '📱', 'Smartphone reviews'),
  ('travel', 'Travel', 'travel', '✈️', 'Destinations and travel experiences'),
  ('restaurants', 'Restaurants', 'restaurants', '🍽️', 'Dining and food reviews'),
  ('electronics', 'Electronics', 'electronics', '🔌', 'Gadgets and electronics'),
  ('food', 'Food', 'food', '🍳', 'Food experiences and dishes'),
  ('drink', 'Drink', 'drink', '🍺', 'Beers, coffee, and beverages'),
  ('company', 'Company', 'company', '🏢', 'Company reviews by country');

-- ============== SEED: SUBCATEGORIES ==============
-- Cars
INSERT INTO subcategories (id, category_id, name, slug) VALUES
  ('cars-toyota', 'cars', 'Toyota', 'toyota'),
  ('cars-hyundai', 'cars', 'Hyundai', 'hyundai'),
  ('cars-bmw', 'cars', 'BMW', 'bmw'),
  ('cars-honda', 'cars', 'Honda', 'honda'),
  ('cars-ford', 'cars', 'Ford', 'ford');
-- Laptops
INSERT INTO subcategories (id, category_id, name, slug) VALUES
  ('laptops-apple', 'laptops', 'Apple', 'apple'),
  ('laptops-dell', 'laptops', 'Dell', 'dell'),
  ('laptops-hp', 'laptops', 'HP', 'hp'),
  ('laptops-lenovo', 'laptops', 'Lenovo', 'lenovo'),
  ('laptops-asus', 'laptops', 'Asus', 'asus');
-- Phones
INSERT INTO subcategories (id, category_id, name, slug) VALUES
  ('phones-apple', 'phones', 'Apple', 'apple'),
  ('phones-samsung', 'phones', 'Samsung', 'samsung'),
  ('phones-google', 'phones', 'Google', 'google'),
  ('phones-oneplus', 'phones', 'OnePlus', 'oneplus'),
  ('phones-xiaomi', 'phones', 'Xiaomi', 'xiaomi');
-- Travel
INSERT INTO subcategories (id, category_id, name, slug) VALUES
  ('travel-beach', 'travel', 'Beach', 'beach'),
  ('travel-city', 'travel', 'City', 'city'),
  ('travel-adventure', 'travel', 'Adventure', 'adventure');
-- Restaurants
INSERT INTO subcategories (id, category_id, name, slug) VALUES
  ('restaurants-italian', 'restaurants', 'Italian', 'italian'),
  ('restaurants-japanese', 'restaurants', 'Japanese', 'japanese'),
  ('restaurants-vietnamese', 'restaurants', 'Vietnamese', 'vietnamese');
-- Electronics
INSERT INTO subcategories (id, category_id, name, slug) VALUES
  ('electronics-headphones', 'electronics', 'Headphones', 'headphones'),
  ('electronics-cameras', 'electronics', 'Cameras', 'cameras'),
  ('electronics-tvs', 'electronics', 'TVs', 'tvs');
-- Food
INSERT INTO subcategories (id, category_id, name, slug) VALUES
  ('food-street', 'food', 'Street food', 'street-food'),
  ('food-fast', 'food', 'Fast food', 'fast-food'),
  ('food-vietnamese', 'food', 'Vietnamese', 'vietnamese'),
  ('food-asian', 'food', 'Asian', 'asian'),
  ('food-western', 'food', 'Western', 'western'),
  ('food-desserts', 'food', 'Desserts', 'desserts');
-- Drink
INSERT INTO subcategories (id, category_id, name, slug) VALUES
  ('drink-tiger', 'drink', 'Tiger Beer', 'tiger-beer'),
  ('drink-corona', 'drink', 'Corona', 'corona'),
  ('drink-heineken', 'drink', 'Heineken', 'heineken'),
  ('drink-sapporo', 'drink', 'Sapporo', 'sapporo'),
  ('drink-craft', 'drink', 'Craft beer', 'craft-beer'),
  ('drink-coffee', 'drink', 'Coffee', 'coffee'),
  ('drink-bubble-tea', 'drink', 'Bubble tea', 'bubble-tea');
-- Company (countries)
INSERT INTO subcategories (id, category_id, name, slug) VALUES
  ('company-us', 'company', 'United States', 'us'),
  ('company-vietnam', 'company', 'Vietnam', 'vietnam'),
  ('company-japan', 'company', 'Japan', 'japan'),
  ('company-uk', 'company', 'United Kingdom', 'uk'),
  ('company-germany', 'company', 'Germany', 'germany'),
  ('company-singapore', 'company', 'Singapore', 'singapore'),
  ('company-korea', 'company', 'South Korea', 'south-korea'),
  ('company-india', 'company', 'India', 'india'),
  ('company-france', 'company', 'France', 'france'),
  ('company-australia', 'company', 'Australia', 'australia');

-- ============== SEED: PRODUCTS (only for subcategories that have products) ==============
-- Cars - Toyota
INSERT INTO products (id, subcategory_id, name, slug) VALUES
  ('cars-toyota-innova', 'cars-toyota', 'Innova', 'innova'),
  ('cars-toyota-fortuner', 'cars-toyota', 'Fortuner', 'fortuner'),
  ('cars-toyota-vios', 'cars-toyota', 'Vios', 'vios'),
  ('cars-toyota-camry', 'cars-toyota', 'Camry', 'camry'),
  ('cars-toyota-hilux', 'cars-toyota', 'Hilux', 'hilux');
-- Cars - Hyundai
INSERT INTO products (id, subcategory_id, name, slug) VALUES
  ('cars-hyundai-tucson', 'cars-hyundai', 'Tucson', 'tucson'),
  ('cars-hyundai-santa-fe', 'cars-hyundai', 'Santa Fe', 'santa-fe'),
  ('cars-hyundai-kona', 'cars-hyundai', 'Kona', 'kona'),
  ('cars-hyundai-elantra', 'cars-hyundai', 'Elantra', 'elantra');
-- Cars - Honda
INSERT INTO products (id, subcategory_id, name, slug) VALUES
  ('cars-honda-civic', 'cars-honda', 'Civic', 'civic'),
  ('cars-honda-cr-v', 'cars-honda', 'CR-V', 'cr-v'),
  ('cars-honda-accord', 'cars-honda', 'Accord', 'accord');
-- Cars - BMW
INSERT INTO products (id, subcategory_id, name, slug) VALUES
  ('cars-bmw-3-series', 'cars-bmw', '3 Series', '3-series'),
  ('cars-bmw-5-series', 'cars-bmw', '5 Series', '5-series'),
  ('cars-bmw-x5', 'cars-bmw', 'X5', 'x5');
-- Laptops - Apple
INSERT INTO products (id, subcategory_id, name, slug) VALUES
  ('laptops-apple-macbook-pro', 'laptops-apple', 'MacBook Pro', 'macbook-pro'),
  ('laptops-apple-macbook-air', 'laptops-apple', 'MacBook Air', 'macbook-air'),
  ('laptops-apple-macbook', 'laptops-apple', 'MacBook', 'macbook');
-- Laptops - Dell
INSERT INTO products (id, subcategory_id, name, slug) VALUES
  ('laptops-dell-xps-13', 'laptops-dell', 'XPS 13', 'xps-13'),
  ('laptops-dell-xps-15', 'laptops-dell', 'XPS 15', 'xps-15'),
  ('laptops-dell-inspiron', 'laptops-dell', 'Inspiron', 'inspiron');
-- Phones - Apple
INSERT INTO products (id, subcategory_id, name, slug) VALUES
  ('phones-apple-iphone-15', 'phones-apple', 'iPhone 15', 'iphone-15'),
  ('phones-apple-iphone-14', 'phones-apple', 'iPhone 14', 'iphone-14'),
  ('phones-apple-iphone-se', 'phones-apple', 'iPhone SE', 'iphone-se'),
  ('phones-apple-iphone-pro', 'phones-apple', 'iPhone 15 Pro', 'iphone-15-pro');
-- Phones - Samsung
INSERT INTO products (id, subcategory_id, name, slug) VALUES
  ('phones-samsung-galaxy-s24', 'phones-samsung', 'Galaxy S24', 'galaxy-s24'),
  ('phones-samsung-galaxy-a', 'phones-samsung', 'Galaxy A series', 'galaxy-a'),
  ('phones-samsung-galaxy-z', 'phones-samsung', 'Galaxy Z Flip', 'galaxy-z-flip');
-- Phones - Google
INSERT INTO products (id, subcategory_id, name, slug) VALUES
  ('phones-google-pixel-8', 'phones-google', 'Pixel 8', 'pixel-8'),
  ('phones-google-pixel-7', 'phones-google', 'Pixel 7', 'pixel-7');
