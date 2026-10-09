# OpenAI SDK adapter with structured JSON classification and real tool calling.
import json
from openai import AsyncOpenAI
class OpenAIClassifier:
    def __init__(self, api_key: str, model: str) -> None:
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model

    async def classify(self, message: str) -> dict:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role":"system","content":"Return JSON: intent is billing/account_access/technical/general, priority is normal/urgent."},{"role":"user","content":message}],
            response_format={"type":"json_object"},
        )
        return json.loads(response.choices[0].message.content or "{}")

    async def propose_tool(self, validated_ticket: dict) -> dict:
        # The tool name is forced so the model cannot choose an unrelated action.
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role":"system","content":"Call create_ticket with EXACTLY the JSON fields supplied by the user; do not alter customer identity."},{"role":"user","content":json.dumps(validated_ticket)}],
            tools=[{"type":"function","function":{"name":"create_ticket","description":"Create a verified support ticket","parameters":{"type":"object","properties":{"subject":{"type":"string"},"message":{"type":"string"},"email":{"type":"string"}},"required":["subject","message","email"],"additionalProperties":False}}}],
            tool_choice={"type":"function","function":{"name":"create_ticket"}},
        )
        calls = response.choices[0].message.tool_calls or []
        if not calls:
            raise ValueError("model did not request create_ticket")
        return {"name":calls[0].function.name,"arguments":json.loads(calls[0].function.arguments)}
