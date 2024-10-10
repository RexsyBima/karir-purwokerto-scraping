import requests
from src.soup import Soup
from db import session
from db.db import JobSQLAlchemy


def scrape_main(url: str):
    resp = requests.get(url)
    soup = Soup(
        resp.content,
        "html.parser",
    )
    job = soup.scrape(url=url)
    isJobExist = session.query(JobSQLAlchemy).filter_by(title=job.title).first()
    if isJobExist:
        pass
    else:
        session.add(job)
        session.commit()
    return job


def scrape_job_location_url() -> list[str]:
    url = "https://karirpurwokerto.id/"
    resp = requests.get(url)
    soup = Soup(resp.content, "html.parser")
    output = soup.scrape_job_location_url()
    return output


def scrape_job_url(url: str):
    resp = requests.get(url)
    soup = Soup(resp.content, "html.parser")
    output = soup.scrape_job_url()
    return output


def main():
    job_location_urls = scrape_job_location_url()
    job_urls_output = []
    for url in job_location_urls:
        print(f"scraping {url}")
        job_urls = scrape_job_url(url)
        job_urls_output.extend(job_urls)

    for url in job_urls_output:
        print(f"scraping {url}")
        job = scrape_main(url)


if __name__ == "__main__":
    main()
