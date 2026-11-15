"""Interaction-level Streamlit smoke test. Run only with disposable DATABASE_URL."""
import os
from pathlib import Path
from streamlit.testing.v1 import AppTest

assert os.environ.get("DATABASE_URL", "").startswith("sqlite:///"), "Run with disposable SQLite"
app_path = Path(os.environ["GITHUB_WORKSPACE"]) / "app.py"
app = AppTest.from_file(str(app_path), default_timeout=35).run()
assert not app.exception, [str(x.message) for x in app.exception]
buttons = [x for x in app.button if x.label == "Enter Demo View (no authentication)"]
assert len(buttons) == 1, "Expected demonstration entry control"
app.selectbox[0].set_value("Voi Jeans Retail India")
app.selectbox[1].set_value("Marketing Director")
app = app.run()
assert not app.exception, [str(x.message) for x in app.exception]
[x for x in app.button if x.label == "Enter Demo View (no authentication)"][0].click()
app = app.run()
assert not app.exception, [str(x.message) for x in app.exception]
assert app.session_state["demo_mode"] is True
assert app.session_state["page"] == "voi_jeans_demo"
try:
    claim = app.session_state["authenticated"]
except KeyError:
    claim = False
assert claim is not True, "Demo must never assert authenticated principal"
print("Demo navigation smoke OK: demo_mode only, no authenticated principal")
