import re

from app.formatter.basicFormatter import BasicFormater


class Fc2ppvFormater(BasicFormater):

    def format(code):
        codeList = re.findall(re.compile('\d{6}'), code)
        if len(codeList) > 0:
            code = codeList[0]
        return code
