# Optional live model adapter: OpenAI is never called by an HTTP door.
# Without it: no production-style provider can replace the deterministic fake.
import asyncio
import json
from openai import AsyncOpenAI
class OpenAIClassifier:
    def __init__(self, api_key: str, model: str) -> None:
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model

    async def classify(self, message: str) -> dict:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role":"system","content":"Classify support messages. Return JSON with intent (billing/account_access/technical/general) and priority (normal/urgent) only."},
                {"role":"user","content":message},
            ],
            response_format={"type":"json_object"},
        )
        return json.loads(response.choices[0].message.content or "{}")
