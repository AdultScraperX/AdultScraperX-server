from app.formatter.basicFormatter import BasicFormater


class OnePondoFormatter(BasicFormater):

    def format(code):
        if code[-4] != "-":
            if code[-4] == " ":
                return code.replace(" ", "_")
        return code