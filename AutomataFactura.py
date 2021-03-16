import re


class AutomataFactura:

    def __init__(self):

        self.signs = {',': "coma"}
        self.listTokens = []
        self.error = []


    def analizadorF(self, entry):

        linea = 1
        columna = 0
        lexema = ""
        state = 1
        indice = 0
        while indice < len(entry):
            if state == 1:
                if re.search(r"[\']", entry[indice]):
                    lexema += entry[indice]
                    indice += 1
                    columna += 1
                    state = 3
                elif re.search(r"[0-9]", entry[indice]):
                    lexema += entry[indice]
                    indice += 1
                    columna += 1
                    state = 5
                elif re.search(r"[a-zA-Z]", entry[indice]):
                    lexema += entry[indice]
                    indice += 1
                    columna += 1
                    state = 6
                elif re.search(r"[\n]", entry[indice]):
                    linea += 1
                    columna = 0
                    indice += 1

                elif re.search(r"[\t]", entry[indice]):
                    columna += 1
                    indice += 1

                else:
                    if re.search(r"[\,]", entry[indice]):
                        lexema = entry[indice]
                        #self.listTokens.append([linea, columna, self.signs[entry[indice]], lexema])
                        lexema = ""
                        indice += 1
                        columna += 1
                    else:
                        self.error.append([linea, columna, entry[indice], "No se esperaba caracter <----- "])
                        indice += 1
                        columna += 1

            elif state == 3:
                if re.search(r"[^']", entry[indice]):
                    lexema += entry[indice]
                    columna += 1
                    indice += 1
                    state = 3
                else:
                    state = 8

            elif state == 8:
                if re.search(r"[\']", entry[indice]):
                    self.listTokens.append([linea, columna, "cadena", lexema + entry[indice]])
                    indice += 1
                    lexema = ""
                    state = 1
                else:
                    lexema += entry[indice]
                    state = 1

            elif state == 5:
                if re.search(r"[0-9]", entry[indice]) or re.search(r"\%", entry[indice]):
                    lexema += entry[indice]
                    indice += 1
                    columna += 1
                    state = 5

                else:
                    self.listTokens.append([linea, columna, "numero", lexema])
                    lexema = ''
                    state = 1

            elif state == 6:
                if re.search(r"[a-zA-Z0-9_]", entry[indice]):
                    lexema += entry[indice]
                    indice += 1
                    columna += 1
                    state = 6
                else:
                    self.listTokens.append([linea, columna, 'Orden', lexema])
                    lexema = ""
                    state = 1

        print(self.listTokens)