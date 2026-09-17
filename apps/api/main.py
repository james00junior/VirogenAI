from fastapi import FastAPI

from apps.api.schemas import HealthResponse

app = FastAPI(
    title="VirogenAI API",
    version="0.1.0",
    description="Production foundation for AI-assisted tumour research and simulation.",
)


@app.get("/health", response_model=HealthResponse, tags=["system"])
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="virogenai-api", version=app.version)


@app.get("/ready", response_model=HealthResponse, tags=["system"])
def ready() -> HealthResponse:
    return HealthResponse(status="ready", service="virogenai-api", version=app.version)
