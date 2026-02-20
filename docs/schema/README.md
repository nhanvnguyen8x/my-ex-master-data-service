# Schema SQL scripts

PostgreSQL schema and seed scripts, one file per purpose. Run in numeric order.

## Table creation (run first)

| File | Purpose |
|------|---------|
| `001_create_category_table.sql` | Create `categories` table |
| `002_create_subcategory_table.sql` | Create `subcategories` table (FK → categories) |
| `003_create_products_table.sql` | Create `products` table (FK → subcategories) |
| `004_create_users_table.sql` | Create `users` table |
| `005_create_reviews_table.sql` | Create `reviews` table (FK → categories, subcategories, products, users) |

## Mock data (run after tables exist)

| File | Purpose |
|------|---------|
| `006_insert_mock_categories.sql` | Insert 9 categories |
| `007_insert_mock_subcategories.sql` | Insert subcategories (brands + countries) |
| `008_insert_mock_products.sql` | Insert sample products |

## Run all (example)

```bash
# From project root, with DATABASE_URL or connection params set
for f in docs/schema/00*.sql; do
  psql "$DATABASE_URL" -f "$f"
done
```

Or run files individually in order (001 → 008).
