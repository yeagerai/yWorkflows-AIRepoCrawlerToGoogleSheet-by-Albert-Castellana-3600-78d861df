
import typing
from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow

class SearchKeywordsIn(BaseModel):
    keywords: List[str]

class SearchResultsOut(BaseModel):
    results: List[dict]
    spreadsheet_url: str

class AIRepoCrawlerToGoogleSheet(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: SearchKeywordsIn, callbacks: typing.Any
    ) -> SearchResultsOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        search_results = results_dict[0].results
        spreadsheet_url = results_dict[1].spreadsheet_url
        out = SearchResultsOut(
            results=search_results,
            spreadsheet_url=spreadsheet_url,
        )
        return out

load_dotenv()
ai_repo_crawler_to_google_sheet_app = FastAPI()

@ai_repo_crawler_to_google_sheet_app.post("/transform/")
async def transform(
    args: SearchKeywordsIn,
) -> SearchResultsOut:
    ai_repo_crawler_to_google_sheet = AIRepoCrawlerToGoogleSheet()
    return await ai_repo_crawler_to_google_sheet.transform(args, callbacks=None)
