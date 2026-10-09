# Environment-backed timeout settings validated once per call.
# Only settings, never secrets, are returned by this helper.
import os
def get_timeout_seconds() -> float:
    value = float(os.getenv("MODEL_TIMEOUT_SECONDS","15"))
    if value <= 0 or value > 120:
        raise ValueError("MODEL_TIMEOUT_SECONDS must be between 0 and 120")
    return value
