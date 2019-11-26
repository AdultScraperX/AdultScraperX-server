import re

from app.formatter.basicFormatter import BasicFormater


class HeydougaOfficialFormatter(BasicFormater):

    def format(code):
        code = 'heydouga-%s' % code
        return code
