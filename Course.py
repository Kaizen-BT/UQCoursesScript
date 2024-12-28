from support import CourseAPI
import sys

class Course:
    def __init__(self, course_code: str):
        """Generates a course with the proper information

        Args:
            course_code (str): UQ Course Code eg: MATH1051
        """

        self._course_code = course_code
        self._course_name, self._course_desc, self._nearest_offering = CourseAPI(
            course_code
        ).get_course_information()

    @property
    def course_name(self) -> str:
        return self._course_name

    @property
    def course_desc(self) -> str:
        return self._course_desc

    @property
    def nearest_offering(self) -> str:
        return self._nearest_offering

    def show_information(self) -> None:
        """Prints the course information in a neat minimal format"""

        print(self.course_name, self.course_desc, self.nearest_offering, sep="\n")


if __name__ == "__main__":
    course = Course(sys.argv[-1])
    course.show_information()