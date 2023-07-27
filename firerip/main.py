import inquirer
from utils.download_course import download_course
from utils.get_courses import get_courses

courses = get_courses()
courses_title = [course["title"] for course in courses]


def main():
    ques = [
        inquirer.List(
            "course", message="Select a course", choices=courses_title
        ),
        inquirer.Path(
            "path",
            message="Select a path",
            path_type=inquirer.Path.DIRECTORY,
            default="./",
            normalize_to_absolute_path=True,
            exists=True,
        ),
    ]
    ans = inquirer.prompt(ques)
    selected_course = courses[courses_title.index(ans["course"])]
    selected_path = ans["path"]

    download_course(selected_course, selected_path)
    print(
        f"\nDownloaded {selected_course['title']} to \033[92m '{selected_path}'\033[0m"
    )


if __name__ == "__main__":
    main()
