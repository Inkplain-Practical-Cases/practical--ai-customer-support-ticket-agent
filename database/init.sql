-- Bootstrap schema when running PostgreSQL with docker compose.
CREATE TABLE IF NOT EXISTS customers (
 id BIGSERIAL PRIMARY KEY,
 email TEXT UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS tickets (
 id BIGSERIAL PRIMARY KEY,
 customer_id BIGINT REFERENCES customers(id),
 subject TEXT NOT NULL,
 message TEXT NOT NULL,
 intent TEXT NOT NULL,
 priority TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'open',
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
