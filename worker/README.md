# Cloudflare migration scaffold

The included Node/Express build is the staging implementation. For production, migrate these responsibilities to Cloudflare Workers + D1 + R2:

- `products.json` → D1 `products`
- `orders.json` → D1 `orders`
- `/public/products/*` → R2 with a public custom domain
- `/api/*` → Worker routes
- admin session/auth → Worker + secure session cookie
- Razorpay secrets → Worker secrets

Run the D1 schema from `schema.sql` during the Cloudflare deployment phase. Do not put Razorpay secrets or admin passwords in frontend code.
