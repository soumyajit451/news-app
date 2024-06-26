from typing import List, Any, Union
from pydantic import BaseModel, Field, validator

class ArticleSummary(BaseModel):
    ai_title: str = Field(description="Catching title for an article")
    summary: str = Field(alias="article_summary",description="Summary of an article in 100 words only")
    tags: List[str] | None = Field(description="tags related to the article")
    category: List[str] | None = Field(description="Category of an article. should be from Politics, Economics, Business, Technology, Science, Health, Entertainment, Sports, Education, Environment, Lifestyle, Travel")
    locations: List[str] | None = Field(description="Location this article is about")

    @validator('summary', pre=True)
    def extract_summary(cls, v, values):
        # sourcery skip: assign-if-exp, reintroduce-else
        # Extract the summary from any key that contains the word "summary"
        summary_keys = [key for key in values if "summary" in key.lower()]
        if summary_keys:
            return "\n".join(values[key] for key in summary_keys)
        return v

    @validator('summary')
    def validate_summary(cls, v):
        if not v:
            raise ValueError("Summary is required")
        return v
    
    class Config:
        populate_by_name = True


class ShowArticleSummary(BaseModel):
    ai_title:str
    summary:str
    tags:list[str] | None = None
    category:list[str] | None =None
    locations:list[str] | None =None
    news_article: Any | None = None
    images:list[dict] | None =None
    original_title:str | None =None
    source_url: str|None = None
    
    def __init__(self, **data):
        super().__init__(**data)

        self.images = self.news_article.images
        self.original_title=self.news_article.title
        self.source_url=self.news_article.url
        del self.news_article