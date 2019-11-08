from app.formatter.basicFormatter import BasicFormater


class TenMusumeFormatter(BasicFormater):

    def format(code):
        if code[-3] != "-":
            if code[-3] == " ":
                return code.replace(" ", "_")
        return code