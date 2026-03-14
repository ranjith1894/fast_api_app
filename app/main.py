from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

votes = {
    "Python": 0,
    "Java": 0,
    "Go": 0,
    "Rust": 0
}

@app.get("/results")
def results():
    return votes

@app.post("/vote/{lang}")
def vote(lang: str):
    if lang in votes:
        votes[lang] += 1
    return votes

# mount frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")