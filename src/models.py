from dataclasses import dataclass
from datetime import datetime


@dataclass
class Job:
    title: str  # v
    description: str  # v
    img_link: str  # v
    slug_url: str  # v
    requirements: list  # v
    date: datetime = datetime.now()
