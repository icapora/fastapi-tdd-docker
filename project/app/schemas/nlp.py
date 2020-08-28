from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class LanguageSchema(str, Enum):
    ES = "es"
    EN = "en"


class Entity(BaseModel):
    text: str = Field(..., example="Mateo")
    label: str = Field(..., example="Per")


class Verb(BaseModel):
    text: str = Field(..., example="trabaja")
    verb: str = Field(..., example="trabajar")


class SpacyPayloadSchema(BaseModel):
    text: str = Field(..., example="Mateo Caporusso trabajará en Google.")
    language: LanguageSchema = Field(..., example="es")


class NlpPayloadSchema(SpacyPayloadSchema):
    nlp: LanguageSchema


class EntityResponseSchema(SpacyPayloadSchema):
    entities: List[Entity]


class VerbResponseSchema(SpacyPayloadSchema):
    verbs: List[Verb]
