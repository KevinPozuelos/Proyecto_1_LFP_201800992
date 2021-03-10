import re
class automataMenu:

    def __init__(self):

        self.signs = {'=':"igual", ';': "puntoComa", ':': "dosPuntos", '[': "corcheteAbre", ']': "corcheteCierra"}
        self.flag = False
        self.lexeme = ""
        self.line = 1
        self.column = 0
        self.row = 0
        self.listTokens = []
        self.error = []




    def analizador(self, entry):

        state = 1
        index = 0
        while index < len(entry):
            if state == 1:
                if re.search(r"[a-z]", entry[index]):
                    self.lexeme += entry[index]

                    index += 1
                    state = 1
                else:
                    self.column += 1
                    self.listTokens.append([self.column,self.lexeme,"reservada"])
                    self.lexeme = ''
                    state = 2


            elif state == 2:
                if re.search(r"\=", entry[index]):
                    self.lexema = entry[index]
                    self.column += 1
                    self.listTokens.append([self.column,self.signs[entry[index]],self.lexema])
                    self.lexeme = ""
                    state = 3
                    index += 1


            elif state == 3:
                if re.search(r"'+[^']+'",entry[index]):
                    self.lexema += entry[index]
                    index += 1
                    state = 3
                else:
                    self.column += 1
                    self.listTokens.append([self.column, self.lexeme, "cadena"])
                    self.lexeme = ''
                    state = 4
                    break
        print(self.listTokens)