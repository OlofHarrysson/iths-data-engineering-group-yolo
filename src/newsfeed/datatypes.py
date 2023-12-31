from datetime import date, datetime

import pydantic


# Note: The code below uses Python type hints to clarify the variable types.
# More info: https://realpython.com/lessons/type-hinting/
class BlogInfo(pydantic.BaseModel):
    unique_id: str
    title: str
    description: str
    link: str
    blog_text: str
    published: date
    timestamp: datetime

    def get_filename(self):
        filename = f'{self.title.replace(" ", "_")}.json'
        return filename


class BlogSummary(pydantic.BaseModel):
    unique_id: str  # This should be same as for BlogInfo so that they can be linked
    title: str
    text: str
    simple: str
    swedish: str
    swe_title: str
    link: str
    published: date

    def get_filename(self):
        return f'{self.title.replace(" ", "_")}.json'
