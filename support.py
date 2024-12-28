import requests, bs4

class CourseAPI:
    TARGET_URL = "https://programs-courses.uq.edu.au/course.html"
    QUERY_PARAMETERS = {"course_code": None}

    # Site Constants (subject to change)
    COURSE_NAME_SELECTOR = "#course-title"
    COURSE_DESC_SELECTOR = "#course-summary"
    OFFERINGS_TABLE_SELECTOR = "#course-current-offerings > tbody"

    def __init__(self, course_code: str):
        CourseAPI.QUERY_PARAMETERS["course_code"] = course_code
        course_page = requests.get(
            url=CourseAPI.TARGET_URL, params=CourseAPI.QUERY_PARAMETERS
        )
        self._course_page = bs4.BeautifulSoup(course_page.text, "html.parser")

    @property
    def page(self) -> bs4.BeautifulSoup:
        return self._course_page

    def get_course_name(self) -> str:
        """Returns the course name"""

        return self.page.select_one(CourseAPI.COURSE_NAME_SELECTOR).text.strip()

    def get_course_desc(self) -> str:
        """Returns the course description"""

        return self.page.select_one(CourseAPI.COURSE_DESC_SELECTOR).text.strip()

    def get_nearest_offer(self) -> str:
        """Returns the nearest offering"""

        offerings_table = self.page.select_one(CourseAPI.OFFERINGS_TABLE_SELECTOR)

        current_offer_row = offerings_table.find("tr", attrs={"class": "current"})

        year_column = current_offer_row.find(
            "a", attrs={"class": "course-offering-year"}
        )
        return year_column.text.strip()
    
    def get_course_information(self) -> tuple[str, str, str]:
        """Returnns the course name, desc, nearest offering

        Returns:
            tuple[str, str, str]: CourseName, CourseDesc, NearestOffering
        """

        return (self.get_course_name(), self.get_course_desc(), self.get_nearest_offer())


if __name__ == "__main__":
    # Run as script to test 
    api = CourseAPI("CSSE1001")
    print(api.get_course_name(), api.get_course_desc(), api.get_nearest_offer(), sep="\n")