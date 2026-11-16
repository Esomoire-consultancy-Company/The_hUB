# The_hUB — preliminary database effect and exposure inventory (R0.5)

**Scope:** Code-level investigation of the branch in PR #2. This is not a dynamic security audit, full endpoint inventory, migration review, legal review or production approval. Do not attach a production DATABASE_URL to this demonstration.

| Source | Observed effect surface | R0.5 disposition |
|---|---|---|
| \`app.py\` | Prior automatic \`initialize_database()\` on opening application | Sample insertion requires explicit demo flags and configured SQLite; normal startup does not seed |
| \`init_db.py\` | \`create_tables()\`, insert synthetic buyers/orders/styles/production lines and allocations, commit | Controlled by strict \`sample_seed_permitted()\` before seeding; browser reset removed |
| \`manufacturing_dashboard.py\` | Calls \`create_tables()\` on entry | Route unavailable without demo setup |
| \`db_operations.py\` | \`add_buyer\`, \`add_order\`, \`update_order_status\`, \`add_style\`, \`update_style_status\`, \`add_material\`, \`update_material_status\`, \`add_production_line\`, \`allocate_style_to_line\`, \`add_production_entry\`, \`import_orders_from_excel\`, \`import_materials_from_excel\`, \`import_production_from_excel\` | Functional DB mutation library, **not** an authorization engine. Only invoked through prototype app routes; no per-actor entitlement verification identified |
| \`order_style_management.py\` | Direct \`db.commit()\` and operations-library writers | Route unavailable without demo setup |
| \`material_tracker.py\` | Operations-library mutations and DB reads | Route unavailable without demo setup |
| \`line_plan.py\` | Direct \`db.commit()\`, \`db.delete()\` plus operations library | Route unavailable without demo setup |
| \`production_timeline.py\` | Operations library and database queries | Route unavailable without demo setup |
| \`reports.py\` | DB queries and exports | Route unavailable without demo setup |
| \`supply_chain_visualization.py\` | Database-backed visualizations | Route unavailable without demo setup |
| \`inventory_export.py\` | Database-backed PowerPoint data extraction | Route unavailable without demo setup |
| \`database.py\` | SQLAlchemy engine and session factory, \`create_tables()\` | Generic driver layer; presence of a DB connection URL is not permission to access a business database |
| \`order_booking.py\` and other Streamlit forms | May modify Streamlit session state; no SQLAlchemy access observed in direct import scan | Client-side demo only; no production-order authority |

## Controls and non-controls

The new page gate is only a **front-end safety guard** for this demonstration. It does not enforce permission for direct Python imports or calls to \`db_operations\`. No real identity provider, tenant-specific row isolation, verified Warden authority, or legally valid licence has been established. Do not deploy the prototype with real customer records.

The sample seeding policy requires two explicit opt-ins and a SQLite URL. It does **not prove the configured SQLite path is disposable**, so use only an isolated temporary test file and never a real business database.

## Next independent production work package

1. Design a single service-level authorization and transactional write boundary for every database mutation, with real identity, role, record ownership and audit receipts.
2. Add verified client/tenant authorization, migrations, DB permissions and safe retries.
3. Independently test user flows, schema integrity, data retention, and backup/restore against synthetic staging data.
4. Keep marketing approval, recipient consent and daily notification delivery in separate activation gates.
