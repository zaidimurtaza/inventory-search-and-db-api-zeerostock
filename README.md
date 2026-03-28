# Inventory search & database API

**Part A:** `GET /search` over `part-a-search/backend/app/data.json` + React UI. 

**Part B:** PostgreSQL (`suppliers`, `inventory`) + FastAPI grouped value report.

## Setup

- Python 3.10+, Node 18+ (Part A UI), PostgreSQL (Part B).

```bash
pip install fastapi uvicorn[standard] pydantic python-dotenv "psycopg[binary]"
```

## Part A — run

**API** (keep on port 8000 for the Vite proxy):

```bash
cd part-a-search/backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Docs: `http://127.0.0.1:8000/docs`. Example: `http://127.0.0.1:8000/search?q=laptop&category=Electronics&minPrice=0&maxPrice=50000`

**UI** (second terminal):

```bash
cd part-a-search/frontend
npm install && npm run dev
```

Open the URL Vite prints (e.g. `http://localhost:5173`).

**Search logic:** Load JSON once into memory; filter in order: optional case-insensitive substring on name (`q`), optional category (case-insensitive exact), then min/max price. No params → all rows. `minPrice > maxPrice` → 400.

**Performance (large data):** Use DB indexes (e.g. on name/category/price) or full-text search; paginate. For JSON-only, pre-index or move to PostgreSQL/Elasticsearch instead of scanning every row each request.

## Part B — run

```bash
cd part-b-database/backend
cp .env.example .env   # Windows: copy .env.example .env — edit HOST, DB_*, etc.
uvicorn main:app --reload --host 127.0.0.1 --port 8001
```

Tables are created on startup. Docs: `http://127.0.0.1:8001/docs`


| Method | Path          | Notes                                                               |
| ------ | ------------- | ------------------------------------------------------------------- |
| POST   | `/supplier/`  | body: `name`, `city`                                                |
| POST   | `/inventory/` | body: `supplier_id`, `product_name`, `quantity`, `price`            |
| GET    | `/inventory/` | grouped by supplier, sorted by total value Σ(quantity × price) desc |


**Schema:** `suppliers(id, name, city)`; `inventory(id, supplier_id → suppliers, product_name, quantity, price)`; one-to-many.

**Why SQL:** FKs enforce valid supplier; joins fit the grouped report.

**Optimization:** Index `inventory(supplier_id)` for joins/inserts; optional materialized view if reporting is heavy.

Port **8001** avoids clashing with Part A on 8000.
