import re

from app.formatter.basicFormatter import BasicFormater


class TokyoHotFormatter(BasicFormater):

    def format(code):
        codelist = re.findall(re.compile('[A-Za-z]+[\ -]?\d+'), code)
        if len(codelist) > 0:
            code = codelist[0]
        return code
