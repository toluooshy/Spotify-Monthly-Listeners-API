from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from algorithm import ArtistScraper

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"Root Request": 200}


@app.get("/grab/{uri}")
def grab_listeners(uri: Optional[str] = None):
    urilisteners = ArtistScraper("https://open.spotify.com/artist/" + uri)
    urilisteners.get_html()
    return urilisteners.get_monthlyListeners()
