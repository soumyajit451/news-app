from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import Field, HttpUrl

from .base_schema import BaseModel


# Define Pydantic model
class Article(BaseModel):
    title: str
    description: Optional[str]       = None
    category: Optional[str] = None
    author: Optional[str] = None
    content: Optional[str] = None
    content_summary : Optional[str] = None
    locations: Optional[List[str]] = None
    language: Optional[List[str]] = None
    url: Optional[HttpUrl] = None
    images: Optional[List[Dict]] = None
    published_at: Optional[datetime] = Field(alias="publishedAt", default=None)
    source_name: Optional[str]=None
    keywords: Optional[List[str]] = None
    sentiment: Optional[float] = None
    meta_data: Optional[Dict[str, Any]] = {}

class NewsArticle(Article):
    pass
    
class NewsArticleList(BaseModel):
    status: str
    totalResults: int
    articles: List[NewsArticle]
    
class ShowArticle(BaseModel):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    author: Optional[str] = None
    content: Optional[str] = None
    locations: Optional[List[str]] = None
    language: Optional[List[str]] = None
    url: Optional[HttpUrl] = None
    images: Optional[List[Dict]] = None
    published_at: Optional[datetime] = Field(alias="publishedAt", default=None)
    source_name: Optional[str] = None
    keywords: Optional[List[str]] = None
    sentiment: Optional[float] = None
    meta_data: Optional[Dict[str, Union[str, List[str]]]] = {}
