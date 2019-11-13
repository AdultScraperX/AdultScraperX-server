import re

from app.formatter.basicFormatter import BasicFormater


class HeyzoFormatter(BasicFormater):

    def format(code):
        codelist = re.findall(re.compile('\d{4}'), code)
        if len(codelist) > 0:
            code = 'Heyzo ' + codelist[0]
        return code
