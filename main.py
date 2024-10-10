import requests
from src.soup import Soup


def main():
    resp = requests.get(
        "https://karirpurwokerto.id/lowongan-bpr-bank-surya-yudha-purbalingga-terbaru/"
    )
    soup = Soup(resp.content, "html.parser")
    output = soup.scrape()

    print(output)


if __name__ == "__main__":
    main()
