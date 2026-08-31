# Maa Astrology — upgraded store

This build upgrades the previous single-product site into a 10-product gemstone bracelet store.

## Included now
- Dedicated reusable product detail page at `/product.html?id=<product-id>` with gallery, quantity controls, shared cart, related products, share action, dynamic SEO metadata and Product JSON-LD
- Homepage product cards now link to dedicated product pages while preserving direct Add to Cart
- 10 products × 5 optimized WebP images
- COD package pricing: 1 ₹399, 2 ₹699, 3 ₹999, 4 ₹1,299
- ₹50 prepaid discount per order, producing prepaid package prices of 1 ₹349, 2 ₹649, 3 ₹949, 4 ₹1,249
- WELCOME10 = 10% off when buying 2+ products
- Separate checkout page to reduce main-page lag
- Cart with quantities and coupon handling
- Razorpay server-side order creation + signature verification
- Existing Google Apps Script forwarding hook (set GOOGLE_SCRIPT_URL)
- Existing Gmail SMTP-style email integration (set EMAIL_APP_PASSWORD)
- Basic private admin dashboard at `/admin.html`
- Order statuses and local JSON order storage for the Node build
- Wishlist toggle, related-product-ready catalogue, energized labels, reviews section
- Mobile-first, lazy-loaded product imagery

## Run locally
1. Install Node.js 18+.
2. `npm install`
3. Copy `.env.example` to `.env` and fill credentials.
4. `npm start`
5. Open `http://localhost:3000`.
6. Admin: `http://localhost:3000/admin.html`

## Production / Cloudflare
This Node build is intentionally usable as a safe staging build. For the final Cloudflare deployment, move the API/storage layer to Workers + D1 + R2. Do not put Razorpay secrets in client code. Keep Netlify as the backup deployment until the Cloudflare version is tested.

## Important
The review cards currently say they are illustrative launch reviews. Replace them with genuine verified customer reviews before representing them as customer testimonials.
