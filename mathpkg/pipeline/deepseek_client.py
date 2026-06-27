"""
DeepSeek V4 API client for the mathpkg pipeline.

Uses OpenAI-compatible API format.
Flash: ¥1/M in, ¥2/M out (concept extraction, dependency analysis)
Pro:   ¥3/M in, ¥6/M out (gap-filling, Lean translation)
"""

import os
import json
import logging
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

logger = logging.getLogger(__name__)

BASE_URL = "https://api.deepseek.com"
DEFAULT_API_KEY = "os.environ.get("DEEPSEEK_API_KEY", "")"


@dataclass
class LLMResponse:
    content: str
    model: str
    tokens_in: int
    tokens_out: int
    cost_yuan: float


class DeepSeekClient:
    """Minimal OpenAI-compatible client for DeepSeek V4."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("DEEPSEEK_API_KEY") or DEFAULT_API_KEY
        self.base_url = BASE_URL

    def chat(self, messages: List[Dict[str, str]],
             model: str = "deepseek-v4-flash",
             temperature: float = 0.1,
             max_tokens: int = 393216,  # DeepSeek V4 Pro max output = 384K
             json_mode: bool = False) -> LLMResponse:
        """
        Send a chat completion request to DeepSeek.

        Parameters
        ----------
        messages : list of {role, content}
        model : "deepseek-v4-flash" or "deepseek-v4-pro"
        temperature : 0-2, lower = more deterministic
        max_tokens : max output tokens
        json_mode : if True, force JSON output format
        """
        import urllib.request
        import urllib.error

        body: Dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if json_mode:
            body["response_format"] = {"type": "json_object"}

        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            f"{self.base_url}/v1/chat/completions",
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )

        import time
        last_error = None
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req, timeout=1200) as resp:
                    raw = resp.read()
                    if not raw:
                        raise RuntimeError("Empty API response body")
                    result = json.loads(raw.decode("utf-8"))
                break
            except urllib.error.HTTPError as e:
                error_body = e.read().decode("utf-8") if e.fp else ""
                raise RuntimeError(f"DeepSeek API error {e.code}: {error_body}")
            except Exception as e:
                last_error = e
                if attempt < 4:
                    wait = 5 * (2 ** attempt)  # 5, 10, 20, 40 seconds
                    logger.warning(f"API attempt {attempt+1} failed: {e}. Retrying in {wait}s...")
                    time.sleep(wait)
        else:
            raise RuntimeError(f"DeepSeek API unreachable after 5 attempts: {last_error}")

        choice = result["choices"][0]
        message = choice.get("message", {})
        content = message.get("content", "")

        if not content:
            raise RuntimeError("API returned empty content")

        usage = result.get("usage", {})

        tokens_in = usage.get("prompt_tokens", 0)
        tokens_out = usage.get("completion_tokens", 0)

        # Cost calculation (DeepSeek V4 pricing)
        if "pro" in model:
            cost = (tokens_in * 3 + tokens_out * 6) / 1_000_000
        else:
            cost = (tokens_in * 1 + tokens_out * 2) / 1_000_000

        return LLMResponse(
            content=content,
            model=model,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            cost_yuan=cost,
        )

    def chat_with_schema(self, messages: List[Dict[str, str]],
                         schema: Dict[str, Any],
                         model: str = "deepseek-v4-flash",
                         temperature: float = 0.1,
                         max_tokens: int = 393216) -> LLMResponse:
        """Chat with JSON schema enforcement (DeepSeek supports json_object)."""
        # Add schema instruction to system message
        schema_instruction = (
            f"Return your response as a JSON object matching this schema:\n"
            f"{json.dumps(schema, indent=2)}\n"
            f"Do NOT include any text outside the JSON object."
        )
        msgs = list(messages)
        if msgs and msgs[0]["role"] == "system":
            msgs[0]["content"] += "\n\n" + schema_instruction
        else:
            msgs.insert(0, {"role": "system", "content": schema_instruction})

        return self.chat(msgs, model=model, temperature=temperature,
                         max_tokens=max_tokens, json_mode=True)


# Singleton
_client: Optional[DeepSeekClient] = None


def get_client() -> DeepSeekClient:
    global _client
    if _client is None:
        _client = DeepSeekClient()
    return _client
