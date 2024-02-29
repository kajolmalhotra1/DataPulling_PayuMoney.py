from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/")
async def root():
    print("this is the number")


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")