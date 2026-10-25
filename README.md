# gisoo-python

A tiny helper that gives you the official [`openai`](https://pypi.org/project/openai/) Python client already pointed at [Gisoo](https://gisoo.pro), a Persian AI app with an OpenAI-compatible API (chat, responses, embeddings, images, speech, music, video). It adds no new abstractions: `Gisoo` is an `openai.OpenAI` subclass.

## Install

```bash
pip install gisoo
```

## Use

Create a key in the Gisoo app (keys look like `sk-gisoo-v1-...`) and export it:

```bash
export GISOO_API_KEY=sk-gisoo-v1-...
```

```python
from gisoo import Gisoo

client = Gisoo()  # or Gisoo(api_key="sk-gisoo-v1-...")
r = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[{"role": "user", "content": "سلام! یک جملهٔ کوتاه دربارهٔ تهران بگو."}],
)
print(r.choices[0].message.content)
```

Streaming works as in the OpenAI client (`stream=True`). Other model IDs include `gpt-5-mini`, `deepseek-flash` and `openrouter/anthropic/claude-sonnet-4.5`.

### Iran mirror

```python
client = Gisoo(iran=True)  # https://ir.gisoo.pro/api/v1
```

### List models (no key needed)

```python
from gisoo import list_models

for m in list_models(type="image"):
    print(m["id"])
```

`type` is one of `chat`, `image`, `audio`, `embedding`, `video`, `music`.

## Good to know

- Pricing is pay-as-you-go through an Iranian bank card. There is no free tier and no signup credit.
- Default rate limit is 60 requests per minute per key.
- The API stores metadata, not request or response bodies.
- Gisoo also has an Anthropic-compatible endpoint (`https://gisoo.pro/api`) and a remote MCP server (`https://gisoo.pro/api/mcp`).

Docs (Persian): <https://gisoo.pro/docs> · App: <https://gisoo.pro> · Models: <https://gisoo.pro/models>

MIT licensed. Source: <https://github.com/netarz/gisoo-python>
