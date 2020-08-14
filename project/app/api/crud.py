from typing import Dict, List, Optional

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="Dummy Dummy")
    await summary.save()
    return summary.id


async def get(id: int) -> Optional[Dict]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries
