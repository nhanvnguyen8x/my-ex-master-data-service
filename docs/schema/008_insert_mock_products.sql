-- Insert mock products (only for subcategories that have products)
-- Run after: 003_create_products_table.sql, 007_insert_mock_subcategories.sql

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
