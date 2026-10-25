import pytest

import gisoo


def test_default_base_url():
    c = gisoo.Gisoo(api_key="sk-gisoo-v1-test")
    assert str(c.base_url).startswith("https://gisoo.pro/api/v1")


def test_iran_mirror():
    c = gisoo.Gisoo(api_key="sk-gisoo-v1-test", iran=True)
    assert str(c.base_url).startswith("https://ir.gisoo.pro/api/v1")


def test_env_key(monkeypatch):
    monkeypatch.setenv("GISOO_API_KEY", "sk-gisoo-v1-env")
    assert gisoo.Gisoo().api_key == "sk-gisoo-v1-env"


def test_missing_key(monkeypatch):
    monkeypatch.delenv("GISOO_API_KEY", raising=False)
    with pytest.raises(ValueError):
        gisoo.Gisoo()
