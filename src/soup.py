from bs4 import BeautifulSoup
from .models import Job
from bs4 import Tag


class Soup(BeautifulSoup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def scrape(self):
        title = self.find("h1", class_="entry-title").get_text()
        img_link = self.find("img", class_="wp-post-image")["src"]
        description = self.find(
            "div", class_="entry-content entry-content-single clearfix"
        )
        print(description.p)
        return None
