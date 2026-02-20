-- Insert mock subcategories (brands and countries)
-- Run after: 002_create_subcategory_table.sql, 006_insert_mock_categories.sql

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
