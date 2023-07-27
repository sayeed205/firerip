import os
from typing import Dict

from utils.get_chapters import get_chapters
from utils.get_ytdl_link import get_ytdl_link
from utils.logger import Ytdl_logger
from yt_dlp import YoutubeDL

exists = os.path.exists


def download_course(course: Dict[str, str], path: str):
    if not exists(path):
        os.makedirs(path)

    chapters = get_chapters(course["link"])
    directory = os.path.abspath(path)
    print(f"Downloading {course['title']} to \033[92m '{directory}'\033[0m")
    print(f"Total chapters: {len(chapters)}\n")

    for chapter in chapters:
        ytdl = get_ytdl_link(chapter["link"])

        ytdl_options = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "merge_output_format": "mp4",
            "outtmpl": (
                f"{path}/{course['title']}/{chapter['number']}. {chapter['emoji']}"
                + f" - {chapter['name'].replace('/', ' ')}.mp4"
            ),
            "embed_thumbnail": True,
            "logger": Ytdl_logger(),
            "console_title": True,
        }
        if ytdl.get("link_type") == "vimeo":
            ytdl_options["http_headers"] = {"Referer": "https://fireship.io"}
        with YoutubeDL(ytdl_options) as ydl:
            ydl.download([ytdl["link"]])
