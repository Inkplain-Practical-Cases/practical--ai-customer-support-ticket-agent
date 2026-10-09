# Step 5 of 6 — Invoke ticket tools
## What you build in this step
The model suggests a create_ticket function call, but server code validates the exact arguments before invoking the trusted backend ticket service.
## What you learn
- Structured tool definitions and tool-call results
- Validation of untrusted model-proposed arguments
- Separating AI intent from authorized database operations
## What changed since step 4
service_execute_ticket_tool, service_validate_tool_args, ToolRequest and tool_create_ticket are added.
## Run it
```bash
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```
## Verify it
Run tests/test_tool_execution.py. A matching model tool proposal creates one ticket; an altered customer email or unrecognized tool name is rejected.
## Diagram
STEP-5 is added to the .inkp during Stage 3.
## Next
Step 6 adds failure recovery, structured logging and end-to-end checks.
