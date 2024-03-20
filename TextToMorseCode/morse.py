import pandas as pd
import tabulate
class Morse:
    def __init__(self):
        morse_code = """.- / -... / -.-. / -.. / . / ..-. / --. / .... / .. / .--- / -.- / .-.. / -- / -. / --- / .--. / --.- / .-. / ... / - / ..- / ...- / .-- / -..- / -.-- / --.. / .---- / ..--- / ...-- / ....- / ..... / -.... / --... / ---.. / ----. / -----"""
        alphanum = "abcdefghijklmnopqrstuvwxyz1234567890"
        self.key = {
            " ": " "
        }
        morse = morse_code.split('/')

        for i in range(0, 36):
            self.key[alphanum[i]] = morse[i].strip() + " "


    def to_morse(self, message: str)->str:
        data = []
        index = []
        for c in message.lower():
            if c in self.key:
                data.append(self.key[c])
                index.append(c)

        df = pd.DataFrame(data=data, index=index)
        return df.T.to_string(justify='left', index=False)


