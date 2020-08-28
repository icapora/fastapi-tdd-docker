from typing import List, Dict

from fastapi import Request
from spacy.language import Language

from app.schemas.nlp import SpacyPayloadSchema, LanguageSchema


async def get_nlp(request: Request, language: str) -> Language:
    if language == LanguageSchema.ES:
        return request.app.state.NLP_ES
    if language == LanguageSchema.EN:
        return request.app.state.NLP_EN


async def extract_entities(request: Request, payload: SpacyPayloadSchema) -> List[Dict]:
    nlp = await get_nlp(request, payload.language)
    doc = nlp(payload.text)
    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]


async def extract_verbs(request: Request, payload: SpacyPayloadSchema) -> List[Dict]:
    nlp = await get_nlp(request, payload.language)
    doc = nlp(payload.text)
    return [
        {"text": token.text, "verb": token.lemma_}
        for token in doc
        if token.pos_ == "VERB"
    ]
