# Foundry Café — Odoo 17 ERP Project

Odoo 17 Community ERP system for a take-away coffee shop. Built as a BA/BC portfolio showcase — reverse-engineering and rationalizing a working system to demonstrate business analysis competency.

---

## System Overview

| Item | Detail |
|------|--------|
| Stack | Odoo 17 Community + PostgreSQL 15 |
| Deployment | Docker Compose on local Windows laptop |
| Database | `coffee_shop_clean` (clean install, no demo data) |
| Locale | UI = English, Country = Vietnam, Currency = VND |
| Access URL | http://localhost:8069 |
| Project path | `D:\odoo-lab\coffee-shop` |

> **Note:** An earlier database `coffee_shop` (created 22/4/2026 with Odoo demo data) was replaced by `coffee_shop_clean` (created 7/5/2026) to start with a clean product catalog.

---

## Project Structure

```
coffee-shop/
├── .gitignore
├── README.md
├── docker-compose.yml
├── config/
│   └── odoo.conf                  # Odoo server config (mounted to /etc/odoo)
├── addons/                        # Custom modules (mounted to /mnt/extra-addons)
│   ├── pos_kot/                   # Kitchen Order Ticket module
│   │   ├── __manifest__.py
│   │   ├── __init__.py
│   │   └── static/src/xml/
│   │       └── kot_receipt.xml
│   └── pos_vietqr_config/        # VietQR payment integration
├── order_receipt_original.xml     # POS receipt template (working version)
├── order_receipt_backup.xml       # Receipt template backup
└── order_receipt_check.xml        # Receipt template checkpoint
```

---

## Custom Modules

### pos_kot — Kitchen Order Ticket (v1.1)

Extends the POS receipt to print 3 sections in a single print job:

1. **Customer receipt** — standard Odoo POS receipt (prices, payment, VietQR code)
2. **Bản lưu kế toán** — accounting copy with order summary and cashier info
3. **KOT (Pha Chế)** — barista ticket with item quantities and customer notes only

Depends on: `point_of_sale`

### pos_vietqr_config — VietQR Payment

VietQR integration for Vietnamese bank transfer payments via QR code on receipts.

---

## Docker Setup

### Containers

| Container | Image | Purpose |
|-----------|-------|---------|
| `odoo17_app` | odoo:17 | Odoo application server |
| `odoo17_postgres` | postgres:15 | PostgreSQL database |

### Volumes

- `postgres-data` — database persistence
- `odoo-web-data` — Odoo filestore (attachments, images)

### Common Commands

```powershell
# Start
docker compose up -d

# Stop
docker compose down

# View logs
docker logs odoo17_app

# Restart
docker compose restart
```

First run downloads ~1.5GB of images (5–15 minutes). Subsequent starts take ~30 seconds.

---

## Credentials

Stored in password manager. **Do not commit credentials to version control.**

---

## Backup & Restore

### Backup

1. Go to http://localhost:8069/web/database/manager
2. Click **Backup**
3. Enter master password
4. Select database: `coffee_shop_clean`
5. Download the `.zip` file

### Restore

1. Go to http://localhost:8069/web/database/manager
2. Click **Restore Database**
3. Enter master password
4. Upload backup `.zip`
5. Check **"This database is a copy"**
6. Click **Continue**

---

## Troubleshooting

**Port 8069 in use** — Stop other apps on that port, or change the mapping in `docker-compose.yml`.

**Containers not starting** — Ensure Docker Desktop is running, then `docker compose down` followed by `docker compose up -d`.

**"This site can't be reached"** — Wait 30 seconds after starting containers, then refresh.

---

## Notes

- This is a **development/learning environment**, not production
- Do not commit `config/odoo.conf` with real passwords to public repos
- Always backup the database before major changes

---

**Last Updated:** 2026-05-21  
**Odoo Version:** 17.0
