from fastapi import FastAPI

app = FastAPI(
    title="Research Paper Assistant API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Research Paper Assistant API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }