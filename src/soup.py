from bs4 import BeautifulSoup, Tag
from datetime import datetime
import re
from .models import Job
from db.db import JobSQLAlchemy


class Soup(BeautifulSoup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def scrape(self, url: str):
        url = (
            url.replace("-", "_")
            .removeprefix("https://karirpurwokerto.id/")
            .removesuffix("/")
        )
        title = self.find("h1", class_="entry-title").get_text()
        img_link = self.find("img", class_="wp-post-image")["src"]
        description = self.find(
            "div", class_="entry-content entry-content-single clearfix"
        )
        job_split = description.find("strong").get_text()
        requirements = self.get_requirements(description)
        description = self.get_job_intro(description.get_text(), job_split=job_split)
        job = JobSQLAlchemy(
            title=title,
            description=description,
            img_link=img_link,
            slug_url=url,
            date=datetime.now(),
        )
        return job

    def scrape_job_location_url(self):
        job_location_url = self.find("ul", id="primary-menu").find_all("li")[:4]
        job_location_url = [j.find("a")["href"] for j in job_location_url]
        return job_location_url

    def scrape_job_url(self):
        job_url = self.find("div", id="infinite-container").find_all(
            "article", class_="post type-post hentry"
        )
        job_url = [j.find("a")["href"] for j in job_url]
        return job_url

    def get_job_intro(self, text: str, job_split: str):
        modified_text = re.split(r"{job_split}.*".format(job_split=job_split), text)
        output = ""
        for t in modified_text:
            if "Saat in" in t:
                break
            output += t
        return output

    def get_requirements(self, tag: Tag):
        requirements = tag.find_all("li")
        return [r.get_text() for r in requirements]
