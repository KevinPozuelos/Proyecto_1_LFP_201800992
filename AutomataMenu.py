import re
import os

class automataMenu:

    def __init__(self):

        self.signs = {'=': "igual", ';': "puntoComa", ':': "dosPuntos", '[': "corcheteAbre", ']': "corcheteCierra"}
        self.listTokens = []
        self.error = []
        self.tokens = []

    def analizador(self, entry):

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
                elif re.search(r"[ \t]", entry[indice]):

                    columna += 1
                    indice += 1
                else:
                    if re.search(r"[\=\[\]\;\:]", entry[indice]):
                        lexema = entry[indice]
                        self.tokens.append([linea, columna, self.signs[entry[indice]], lexema])
                        lexema = ""
                        indice += 1
                        columna += 1
                    else:
                        self.error.append([linea, columna, entry[indice],"No se esperaba caracter <----- "])
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
            elif state == 5:
                if re.search(r"[0-9]", entry[indice]) or re.search(r"\.", entry[indice]):
                    lexema += entry[indice]
                    indice += 1
                    columna += 1
                    state = 5
                elif re.search(r"\.", entry[indice]):
                    state = 11
                else:
                    self.listTokens.append([linea, columna, "Numero", lexema])
                    self.tokens.append([linea, columna, "Numero", lexema])
                    state = 1
            elif state == 6:
                if re.search(r"[a-zA-Z0-9_]", entry[indice]):
                    lexema += entry[indice]
                    indice += 1
                    columna += 1
                    state = 6
                else:
                    self.listTokens.append([linea, columna, self.verificaLexema(lexema), lexema])
                    self.tokens.append([linea, columna, self.verificaLexema(lexema), lexema])
                    lexema = ""
                    state = 1
            elif state == 8:
                if re.search(r"[\']", entry[indice]):
                    self.listTokens.append([linea, columna, "cadena", lexema + entry[indice]])
                    self.tokens.append([linea, columna, "cadena", lexema + entry[indice]])
                    indice += 1
                    lexema = ""
                    state = 1
                else:
                    lexema += entry[indice]
                    state = 1
            elif state == 11:
                if re.search(r"[\.]", entry[indice]):
                    lexema += entry[indice]
                    state = 14
                else:
                    self.listTokens.append([linea, columna, "entero", lexema])
                    self.tokens.append([linea, columna, "entero", lexema])
                    lexema = ""
                    state = 1
            elif state == 14:
                if re.search(r"[0-9]", entry[indice]):
                    lexema += entry[indice]
                    indice += 1
                    columna += 1
                    state = 14

                else:
                    #self.listTokens.append([linea, columna, "decimal", lexema])

                    state = 1



    def verificaLexema(self, lexxe):
        if lexxe.lower() == "restaurante":
            return "reservada"
        else:
            return "identificador"


    def reporteToken(self):
        contenido = ''
        htmFile = open("Reporte_Menu" + ".html", "w",encoding='utf8')
        htmFile.write("""<!DOCTYPE HTML PUBLIC"

            <html>

            <head>
                <title>Reporte de tokens Menu</title>
             <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
            </head>
            <body>
            <div class="container">
          <h2>Reporte de tokens</h2>
          <p>Lista de tokens</p>            
          <table class="table">
            <thead>
              <tr>
               <th>Fila</th>
                <th>Columna</th>
                <th>Token</th>
                <th>Lexemna</th>
              </tr>
            </thead>

            """)
        for i in range(len(self.listTokens)):
            contenido += (" <tbody>"
                          "<td>" + str(self.listTokens[i][0]) + "</td>"
                            
                          "<td>" + str(self.listTokens[i][1]) + "</td>"
                          "<td>" + str(self.listTokens[i][2]) + "</td>"
                          "<td>" + str(self.listTokens[i][3]) + "</td>"
                          "</tbody>")
        htmFile.write(contenido)
        htmFile.write("""
         </table>
    </div>
        </body>
        </html>""")
        htmFile.close


    def generarMenu(self):
        contenido = ''
        htmFile = open("Menu" + ".html", "w", encoding='utf8')
        htmFile.write("""<!DOCTYPE HTML PUBLIC"

                    <html>

                    <head>
                        <title>Menu</title>
                     <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1">
                  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
                    </head>
                    <body>
                    
                    
                    
                    """
                      " ")
        titulo = "<h1>"+str(self.listTokens[1][3])+"</h1>"
        htmFile.write(titulo)
        for i in range(len(self.listTokens)):
            if self.listTokens[i][2] == 'cadena' and self.listTokens[i][3] != self.listTokens[1][3] :

                contenido += ("<div class=""col-lg-12""> <h4>"+str(self.listTokens[i][3])+"</h2> </div>")
            if self.listTokens[i][2] == 'identificador':
                contenido += ("<div class=""col-lg-4""> <h4>" + str(self.listTokens[i][3]) + "</h3> </div>")

            if self.listTokens[i][2] == 'Numero':
                contenido += ("<div class=""col-lg-4""> <h5>" + "Q" + str(self.listTokens[i][3]) + "</h3> </div>")


        htmFile.write(contenido)
        htmFile.write(""""
                 </table>
            </div>
                </body>
                </html>""")
        htmFile.close



    def ordenarSecciones(self):
        listaSecc = []
        listaCuerpo = []
        seccion = ""

        for i in range(0,len(self.tokens)):
            if self.tokens[i][2] == 'reservada':
                listaSecc.append(self.tokens[i+2][3])
            elif self.tokens[i][2] == 'dosPuntos':
                seccion = self.tokens[i-1][3]
            elif self.tokens[i][2] == 'corcheteAbre':
                listaCuerpo.append(self.ordenarCuerpo(i+1,self.tokens))
            elif i+2 < len(self.tokens) and self.tokens[i][2] == 'corcheteCierra' and self.tokens[i+2][2] == 'dosPuntos':
                listaSecc.append([seccion,listaCuerpo])
                listaCuerpo = []
            elif i + 1 == len(self.tokens):
                listaSecc.append([seccion,listaCuerpo])
        return listaSecc

    def ordenarCuerpo(self,indice,lista):
        listCuerpo = []
        for i in range(indice,len(lista)):
            if lista[i][2] != 'corcheteCierra':
                if lista[i][2] != 'puntoComa':
                    listCuerpo.append(lista[i][3])
            else:
                return listCuerpo


    def generarGraph(self,listaSecc):
        aux = 0
        dot = "digraph G { \n"
        dot += "Inicio[label=\"Nombre\"]\n"
        dot += "Nombre[label=\"" + str(listaSecc[0]) + "\"]\n"
        dot += "Inicio -> Nombre \n"
        for i in range(1,len(listaSecc)):
            dot += "sec"+str(i)+"[label=\"" + str(listaSecc[i][0]) + "\"]\n"
            dot += "Nombre -> sec"+ str(i)+"\n"
            listCuerpo = listaSecc[i][1]
            for x in range(0,len(listCuerpo)):
                dot += "son"+str(aux)+"[label=\"" + str(listCuerpo[x][0])+" : Q"+ str(listCuerpo[x][2]) +"\n"+str(listCuerpo[x][3])+ "\"]\n"
                dot += "sec"+str(i)+ "-> son" + str(aux) + "\n"
                aux += 1
        try:


            dot += "}"
            archivo = open("grafico.dot", 'w',encoding='utf8')
            archivo.write(dot)
            archivo.close()

            os.system("dot -Tpdf grafico.dot -o grafico.pdf")
            os.startfile("grafico.pdf")
        except Exception:

                return False