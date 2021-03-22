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
                        self.error.append([linea, columna, entry[indice], " <----- No se esperaba caracter"])
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
                    self.listTokens.append([linea, columna, "NUMERO", lexema])
                    lexema = ''
                    state = 1

            elif state == 6:
                if re.search(r"[a-zA-Z0-9_]", entry[indice]):
                    lexema += entry[indice]
                    indice += 1
                    columna += 1
                    state = 6
                else:
                    self.listTokens.append([linea, columna, 'identificador', lexema])
                    lexema = ""
                    state = 1

    def reporteToken(self):
        contenido = ''
        htmFile = open("Reporte_Factura" + ".html", "w", encoding='utf8')
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

    def reporterror(self):
        contenido = ''
        htmFile = open("Reporte_error_factura" + ".html", "w", encoding='utf8')
        htmFile.write("""<!DOCTYPE HTML PUBLIC"

            <html>

            <head>
                <title>Reporte de errores</title>
             <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
            </head>
            <body>
            <div class="container">
          <h2>Reporte de errores</h2>
          <p>Lista de errores</p>            
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
        for i in range(len(self.error)):
            contenido += (" <tbody>"
                          "<td>" + str(self.error[i][0]) + "</td>"

                           "<td>" + str(self.error[i][1]) + "</td>"
                           "<td>" + str(self.error[i][2]) + "</td>"
                           "<td>" + str(self.error[i][3]) + "</td>"
                           "</tbody>")
        htmFile.write(contenido)
        htmFile.write("""
         </table>
    </div>
        </body>
        </html>""")
        htmFile.close

    def vistaFactura(self):
        contenido = ''
        htmFile = open("VistaFactura" + ".html", "w", encoding='utf8')
        htmFile.write("""<!DOCTYPE html>
                                <html lang="es">
                                <head>
                                <meta charset="UTF-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <title>Bootstrap 4. Tablas</title>
                                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
                                </head>
                                <body>
                                <div class="container">
        		                <div class="row">
        			            <div class="col">
        				        <table class="table table-striped table-bordered table-hover table-dark">
        					    <thead>
        						<tr>
        							<th>Factura</th>

        						</tr>
        					</thead>
        					""")

        contenido += "<tbody>" + "<tr>" + "<td>" + "Nombre: " +str(self.listTokens[0][3]) + "</td >" + "</tr>" + "</tbody>"
        contenido += "<tbody>" + "<tr>" + "<td>" + "NIT: "+str(self.listTokens[1][3]) + "</td >" + "</tr>" + "</tbody>"
        contenido += "<tbody>" + "<tr>" + "<td>" +"Direccion"+ str(self.listTokens[2][3]) + "</td >" + "</tr>" + "</tbody>"
        htmFile.write(contenido)
        htmFile.write("""
        				</table>
        			</div>
        		</div>
            <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
        </body>
        </html>""")
        htmFile.close