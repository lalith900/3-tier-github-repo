import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app  # noqa:E402

client = app.test_client()


def test_home():
    response = client.get("/")
    assert response.status_code == 200  # nosec B101


def test_health():
    response = client.get("/health")
    assert response.status_code == 200  # nosec B101
