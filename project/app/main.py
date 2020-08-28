import logging

import spacy
from fastapi import FastAPI

from app.api import nlp, ping, summaries
from app.db import init_db

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI(
        title="NLP with FastAPI",
        description="Application of NLP techniques made with ♥ and FastAPI",
        version="0.0.1",
    )
    application.include_router(ping.router, tags=["ping"])
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )
    application.include_router(nlp.router, prefix="/nlp", tags=["nlp"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting  up...")
    init_db(app)
    app.state.NLP_ES = spacy.load("es_core_news_md")
    app.state.NLP_EN = spacy.load("en_core_web_md")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
