import re

from app.formatter.basicFormatter import BasicFormater


class HeyzoOfficialFormatter(BasicFormater):

    def format(code):
        codes = re.finditer(r'[0-9]{4}',code)
        for item in codes:
            code = item.group()
        return code
