-- Insert mock categories (9 categories)
-- Run after: 001_create_category_table.sql

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
