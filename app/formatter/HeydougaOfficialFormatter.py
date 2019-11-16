import re

from app.formatter.basicFormatter import BasicFormater


class HeydougaOfficialFormatter(BasicFormater):

    def format(code):
        
        if len(code) == 8:
            code = code.replace(code[4],'/')
        elif len(code) == 10:
            code = code.replace(code[4],'/')
        elif len(code) == 13:            
            code = code.replace(code[4],'/').replace(code[9],'-')
        elif len(code) == 19:
            code = code.replace(code[4],'/').replace(code[9],'-').replace(code[16],'_')
        else:
            pass

        return code
