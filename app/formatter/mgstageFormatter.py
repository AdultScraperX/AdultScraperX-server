from app.formatter.basicFormatter import BasicFormater


class MGStageFormatter(BasicFormater):

    def format(code):
        code = code.replace(' ','-')
        return code