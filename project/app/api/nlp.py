from fastapi import APIRouter, Request

from app.schemas.nlp import EntityResponseSchema, SpacyPayloadSchema, VerbResponseSchema
from app.services.extractor import extract_entities, extract_verbs

router = APIRouter()


@router.post("/entities", response_model=EntityResponseSchema)
async def get_entities(
    request: Request, payload: SpacyPayloadSchema
) -> EntityResponseSchema:
    entities = await extract_entities(request, payload)
    return EntityResponseSchema(**payload.dict(), entities=entities)


@router.post("/verbs", response_model=VerbResponseSchema)
async def get_verbs(
    request: Request, payload: SpacyPayloadSchema
) -> VerbResponseSchema:
    verbs = await extract_verbs(request, payload)
    return VerbResponseSchema(**payload.dict(), verbs=verbs)
