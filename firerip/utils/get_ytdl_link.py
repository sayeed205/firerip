import requests
from bs4 import BeautifulSoup


def get_ytdl_link(url: str):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any failed request

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    vimeo_id = soup.find("global-data")["vimeo"]
    youtube_id = soup.find("global-data")["youtube"]

    if not vimeo_id and not youtube_id:
        return None
    if not vimeo_id and youtube_id:
        return {
            "link_type": "youtube",
            "link": f"https://www.youtube.com/watch?v={youtube_id}",
        }
    else:
        return {
            "link_type": "vimeo",
            "link": (
                requests.get(
                    f"https://vimeo.com/api/oembed.json?url=https%3A%2F%2Fvimeo.com%2F{vimeo_id}&id={vimeo_id}"
                )
                .json()["html"]
                .split('src="')[1]
                .split('"')[0]
            ),
        }
