CREATE TABLE IF NOT EXISTS products (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  price INTEGER NOT NULL DEFAULT 399,
  tag TEXT,
  stock INTEGER NOT NULL DEFAULT 0,
  images_json TEXT NOT NULL,
  benefits_json TEXT NOT NULL,
  description TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS orders (
  id TEXT PRIMARY KEY,
  created_at TEXT NOT NULL,
  customer_name TEXT,
  mobile TEXT,
  email TEXT,
  address TEXT,
  city TEXT,
  state TEXT,
  pincode TEXT,
  items_json TEXT NOT NULL,
  subtotal REAL NOT NULL,
  coupon_discount REAL NOT NULL DEFAULT 0,
  prepaid_discount REAL NOT NULL DEFAULT 0,
  amount REAL NOT NULL,
  payment TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'NEW',
  razorpay_order_id TEXT,
  razorpay_payment_id TEXT
);
CREATE TABLE IF NOT EXISTS admins (
  id TEXT PRIMARY KEY,
  password_hash TEXT NOT NULL
);
