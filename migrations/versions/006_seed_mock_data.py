"""seed mock data (categories, subcategories, products)

Revision ID: 006
Revises: 005
Create Date: 2025-02-20

"""
from alembic import op

revision = "006"
down_revision = "005"
branch_labels = None
depends_on = None


def upgrade():
    # Categories (matches app schema: id, name, slug, product_count, status)
    op.execute("""
        INSERT INTO categories (id, name, slug, product_count, status) VALUES
        ('cars', 'Cars', 'cars', 0, 'active'),
        ('laptops', 'Laptops', 'laptops', 0, 'active'),
        ('phones', 'Phones', 'phones', 0, 'active'),
        ('travel', 'Travel', 'travel', 0, 'active'),
        ('restaurants', 'Restaurants', 'restaurants', 0, 'active'),
        ('electronics', 'Electronics', 'electronics', 0, 'active'),
        ('food', 'Food', 'food', 0, 'active'),
        ('drink', 'Drink', 'drink', 0, 'active'),
        ('company', 'Company', 'company', 0, 'active')
        ON CONFLICT (id) DO NOTHING
    """)

    # Subcategories
    op.execute("""
        INSERT INTO subcategories (id, category_id, name, slug) VALUES
        ('cars-toyota', 'cars', 'Toyota', 'toyota'),
        ('cars-hyundai', 'cars', 'Hyundai', 'hyundai'),
        ('cars-bmw', 'cars', 'BMW', 'bmw'),
        ('cars-honda', 'cars', 'Honda', 'honda'),
        ('cars-ford', 'cars', 'Ford', 'ford')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO subcategories (id, category_id, name, slug) VALUES
        ('laptops-apple', 'laptops', 'Apple', 'apple'),
        ('laptops-dell', 'laptops', 'Dell', 'dell'),
        ('laptops-hp', 'laptops', 'HP', 'hp'),
        ('laptops-lenovo', 'laptops', 'Lenovo', 'lenovo'),
        ('laptops-asus', 'laptops', 'Asus', 'asus')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO subcategories (id, category_id, name, slug) VALUES
        ('phones-apple', 'phones', 'Apple', 'apple'),
        ('phones-samsung', 'phones', 'Samsung', 'samsung'),
        ('phones-google', 'phones', 'Google', 'google'),
        ('phones-oneplus', 'phones', 'OnePlus', 'oneplus'),
        ('phones-xiaomi', 'phones', 'Xiaomi', 'xiaomi')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO subcategories (id, category_id, name, slug) VALUES
        ('travel-beach', 'travel', 'Beach', 'beach'),
        ('travel-city', 'travel', 'City', 'city'),
        ('travel-adventure', 'travel', 'Adventure', 'adventure')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO subcategories (id, category_id, name, slug) VALUES
        ('restaurants-italian', 'restaurants', 'Italian', 'italian'),
        ('restaurants-japanese', 'restaurants', 'Japanese', 'japanese'),
        ('restaurants-vietnamese', 'restaurants', 'Vietnamese', 'vietnamese')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO subcategories (id, category_id, name, slug) VALUES
        ('electronics-headphones', 'electronics', 'Headphones', 'headphones'),
        ('electronics-cameras', 'electronics', 'Cameras', 'cameras'),
        ('electronics-tvs', 'electronics', 'TVs', 'tvs')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO subcategories (id, category_id, name, slug) VALUES
        ('food-street', 'food', 'Street food', 'street-food'),
        ('food-fast', 'food', 'Fast food', 'fast-food'),
        ('food-vietnamese', 'food', 'Vietnamese', 'vietnamese'),
        ('food-asian', 'food', 'Asian', 'asian'),
        ('food-western', 'food', 'Western', 'western'),
        ('food-desserts', 'food', 'Desserts', 'desserts')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO subcategories (id, category_id, name, slug) VALUES
        ('drink-tiger', 'drink', 'Tiger Beer', 'tiger-beer'),
        ('drink-corona', 'drink', 'Corona', 'corona'),
        ('drink-heineken', 'drink', 'Heineken', 'heineken'),
        ('drink-sapporo', 'drink', 'Sapporo', 'sapporo'),
        ('drink-craft', 'drink', 'Craft beer', 'craft-beer'),
        ('drink-coffee', 'drink', 'Coffee', 'coffee'),
        ('drink-bubble-tea', 'drink', 'Bubble tea', 'bubble-tea')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
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
        ('company-australia', 'company', 'Australia', 'australia')
        ON CONFLICT (id) DO NOTHING
    """)

    # Products
    op.execute("""
        INSERT INTO products (id, subcategory_id, name, slug) VALUES
        ('cars-toyota-innova', 'cars-toyota', 'Innova', 'innova'),
        ('cars-toyota-fortuner', 'cars-toyota', 'Fortuner', 'fortuner'),
        ('cars-toyota-vios', 'cars-toyota', 'Vios', 'vios'),
        ('cars-toyota-camry', 'cars-toyota', 'Camry', 'camry'),
        ('cars-toyota-hilux', 'cars-toyota', 'Hilux', 'hilux')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO products (id, subcategory_id, name, slug) VALUES
        ('cars-hyundai-tucson', 'cars-hyundai', 'Tucson', 'tucson'),
        ('cars-hyundai-santa-fe', 'cars-hyundai', 'Santa Fe', 'santa-fe'),
        ('cars-hyundai-kona', 'cars-hyundai', 'Kona', 'kona'),
        ('cars-hyundai-elantra', 'cars-hyundai', 'Elantra', 'elantra')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO products (id, subcategory_id, name, slug) VALUES
        ('cars-honda-civic', 'cars-honda', 'Civic', 'civic'),
        ('cars-honda-cr-v', 'cars-honda', 'CR-V', 'cr-v'),
        ('cars-honda-accord', 'cars-honda', 'Accord', 'accord')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO products (id, subcategory_id, name, slug) VALUES
        ('cars-bmw-3-series', 'cars-bmw', '3 Series', '3-series'),
        ('cars-bmw-5-series', 'cars-bmw', '5 Series', '5-series'),
        ('cars-bmw-x5', 'cars-bmw', 'X5', 'x5')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO products (id, subcategory_id, name, slug) VALUES
        ('laptops-apple-macbook-pro', 'laptops-apple', 'MacBook Pro', 'macbook-pro'),
        ('laptops-apple-macbook-air', 'laptops-apple', 'MacBook Air', 'macbook-air'),
        ('laptops-apple-macbook', 'laptops-apple', 'MacBook', 'macbook')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO products (id, subcategory_id, name, slug) VALUES
        ('laptops-dell-xps-13', 'laptops-dell', 'XPS 13', 'xps-13'),
        ('laptops-dell-xps-15', 'laptops-dell', 'XPS 15', 'xps-15'),
        ('laptops-dell-inspiron', 'laptops-dell', 'Inspiron', 'inspiron')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO products (id, subcategory_id, name, slug) VALUES
        ('phones-apple-iphone-15', 'phones-apple', 'iPhone 15', 'iphone-15'),
        ('phones-apple-iphone-14', 'phones-apple', 'iPhone 14', 'iphone-14'),
        ('phones-apple-iphone-se', 'phones-apple', 'iPhone SE', 'iphone-se'),
        ('phones-apple-iphone-pro', 'phones-apple', 'iPhone 15 Pro', 'iphone-15-pro')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO products (id, subcategory_id, name, slug) VALUES
        ('phones-samsung-galaxy-s24', 'phones-samsung', 'Galaxy S24', 'galaxy-s24'),
        ('phones-samsung-galaxy-a', 'phones-samsung', 'Galaxy A series', 'galaxy-a'),
        ('phones-samsung-galaxy-z', 'phones-samsung', 'Galaxy Z Flip', 'galaxy-z-flip')
        ON CONFLICT (id) DO NOTHING
    """)
    op.execute("""
        INSERT INTO products (id, subcategory_id, name, slug) VALUES
        ('phones-google-pixel-8', 'phones-google', 'Pixel 8', 'pixel-8'),
        ('phones-google-pixel-7', 'phones-google', 'Pixel 7', 'pixel-7')
        ON CONFLICT (id) DO NOTHING
    """)


def downgrade():
    op.execute("DELETE FROM products")
    op.execute("DELETE FROM subcategories")
    op.execute("DELETE FROM categories")
