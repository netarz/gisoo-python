from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Optional

from openai import OpenAI

BASE_URL = "https://gisoo.pro/api/v1"
IRAN_BASE_URL = "https://ir.gisoo.pro/api/v1"


class Gisoo(OpenAI):
    """An ``openai.OpenAI`` client that talks to Gisoo.

    ``api_key`` falls back to the ``GISOO_API_KEY`` environment variable.
    ``iran=True`` uses the Iran mirror (``ir.gisoo.pro``). An explicit
    ``base_url`` always wins. Every other keyword is passed to ``OpenAI``.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        iran: bool = False,
        **kwargs: Any,
    ) -> None:
        key = api_key or os.environ.get("GISOO_API_KEY")
        if not key:
            raise ValueError("Pass api_key or set GISOO_API_KEY (keys look like sk-gisoo-v1-...).")
        url = base_url or (IRAN_BASE_URL if iran else BASE_URL)
        super().__init__(api_key=key, base_url=url, **kwargs)


def list_models(
    type: Optional[str] = None,
    *,
    iran: bool = False,
    base_url: Optional[str] = None,
    timeout: float = 30.0,
) -> list:
    """Return the public model list (no API key needed).

    ``type`` filters by chat, image, audio, embedding, video or music.
    """
    url = (base_url or (IRAN_BASE_URL if iran else BASE_URL)).rstrip("/") + "/models"
    req = urllib.request.Request(
        url, headers={"Accept": "application/json", "User-Agent": "gisoo-python/0.1.0"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    models = payload.get("data", payload) if isinstance(payload, dict) else payload
    if type:
        models = [m for m in models if m.get("type") == type]
    return models
