from app.formatter.basicFormatter import BasicFormater


class CensoredFormatter(BasicFormater):

    def format(code):
        hCode = str(code).upper()
        if hCode[-4] == '0' and hCode[-5] == '0':
            hCode = hCode[0:-5] + hCode[-3:]
        if hCode[-4] != "-":
            if hCode[-4] == " ":
                return hCode.replace(" ", "-")
            else:
                listCoed = list(hCode)
                listCoed.insert(len(hCode) - 3, "-")
                return "".join(listCoed)
        return hCode
