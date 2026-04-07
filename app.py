from pathlib import Path

from google.adk.cli.fast_api import get_fast_api_app


AGENTS_DIR = str(Path(__file__).resolve().parent)

# Vercel requires an ASGI object named `app` in a recognized entrypoint file.
# Use in-memory services for serverless compatibility.
app = get_fast_api_app(
    agents_dir=AGENTS_DIR,
    web=True,
    host="0.0.0.0",
    port=8000,
    use_local_storage=False,
    session_service_uri="memory://",
    artifact_service_uri="memory://",
    memory_service_uri="memory://",
    allow_origins=["*"],
    auto_create_session=True,
)
