"""Database route isolation smoke: no seed flags, no database access or schema creation."""
import os
from pathlib import Path
from streamlit.testing.v1 import AppTest

assert "THE_HUB_DEMO_MODE" not in os.environ
assert "THE_HUB_ALLOW_SAMPLE_SEED" not in os.environ
db_url = os.environ["DATABASE_URL"]
assert db_url.startswith("sqlite:///")
database = Path(db_url[len("sqlite:///"):])
assert not database.exists()
app_path = Path(os.environ["GITHUB_WORKSPACE"]) / "app.py"
app = AppTest.from_file(str(app_path), default_timeout=30).run()
assert not app.exception, [str(x.message) for x in app.exception]
for route in [
    "manufacturing_dashboard", "order_style_management", "material_tracker",
    "production_timeline", "line_plan", "reports", "db_initialization",
    "supply_chain_visualization", "inventory_export",
]:
    app.session_state["page"] = route
    app = app.run()
    assert not app.exception, f"Route {route}: " + repr([str(x.message) for x in app.exception])
    assert any("database-backed demonstration area is unavailable" in str(w.message)
               for w in app.warning), f"Missing unavailable state on {route}"
    assert not database.exists(), f"Unexpected database creation on {route}"
print("All 9 database-dependent routes blocked safely without demo activation")
