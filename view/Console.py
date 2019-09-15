from datetime import datetime


class Console:

    def __init__(self):
        pass

    def Print(self, message):
        print(message)

    def PrintBooleanRow(self, content, boolResult, boolOutput = ["SUCCESS", "MISTAKE"], allowTime = True):
        currentDate = ""
        booloutput = "'\x1b[0;30;47m' + '[ERROR]' + '\x1b[0m'"

        if allowTime == True:
            currentDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " --- "

        if boolResult == True:
            booloutput = "\x1b[0;30;42m["+boolOutput[0]+"]\x1b[0m"
        else:
            booloutput = "\x1b[0;30;41m["+boolOutput[1]+"]\x1b[0m"


        output = "\x1b[0;30;47m[> "+currentDate+content+" --- ]\x1b[0m" + booloutput
        print(output)

