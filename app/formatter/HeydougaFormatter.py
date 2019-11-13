import re

from app.formatter.basicFormatter import BasicFormater


class HeydougaFormatter(BasicFormater):

    def format(code):
        codelist = re.findall(re.compile('\d+'), code)
        if len(codelist) >= 2:
            code = codelist[0]
            ppv = codelist[1]
            pt = ''
            if len(codelist) == 3:
                pt = '-PART' + codelist[2]
            if len(codelist) > 0:
                code = 'Heydouga ' + code + '-PPV'+ppv + pt
        return code
