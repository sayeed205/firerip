from typing import Dict, List

import requests
from bs4 import BeautifulSoup


def get_courses() -> list[Dict[str, List[str] | str]]:
    """
    Scrapes the Fireship.io courses page
    and returns a list of dictionaries containing course data.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing course data,
        including title, description, tags, link, and image.
    """
    url = "https://fireship.io/courses/"
    response = requests.get(url)
    response.raise_for_status()

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    courses: List[Dict[str, List[str] | str]] = []
    articles = soup.find_all("article")
    for article in articles:
        title: str = article.find("h5").text
        description: str = article.find("p").text
        tags: List[str] = [tag.text.strip() for tag in article.find_all("span")]
        link: str = f"https://fireship.io{article.find('a')['href']}"
        image: str = f"https://fireship.io{article.find('img')['src']}"

        course_data: Dict[str, str | List[str]] = {
            "title": title,
            "description": description,
            "tags": tags,
            "link": link,
            "image": image,
        }
        courses.append(course_data)

    return courses
