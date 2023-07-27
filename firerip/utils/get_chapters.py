import requests
from bs4 import BeautifulSoup


def get_chapters(url: str):
    # response = requests.get(course["link"])
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any failed request

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    chapters = []
    links = soup.select("div ul a")
    # print(links)
    for link in links:  # type: ignore
        chapter_info = link.find("li")  # type: ignore
        # print(chapter_info)
        name = chapter_info.find("h5").text.replace(r"\d{2}", "").strip()  # type: ignore
        description = chapter_info.find("p").text  # type: ignore
        number = chapter_info.find("h5").find("span").text  # type: ignore
        emoji = chapter_info.find("span").text.strip()  # type: ignore
        link = f"https://fireship.io{link['href']}"

        chapter_data = {
            "name": name.strip(),
            "description": description,
            "number": number.strip(),
            "emoji": emoji.strip(),
            "link": link.strip(),
        }
        chapters.append(chapter_data)
    return chapters


get_chapters("https://fireship.io/courses/supabase/")
