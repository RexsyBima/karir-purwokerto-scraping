from dataclasses import dataclass
from datetime import datetime


@dataclass
class Job:
    title: str  # v
    description: str
    img_link: str  # v
    slug_url: str
    date: datetime = datetime.now()


def foo(a, b, c, d):
    pass
