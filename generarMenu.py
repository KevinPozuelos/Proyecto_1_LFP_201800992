def reporte(lista):
    contenido = ''
    htmFile = open("Menu" + ".html", "w")
    htmFile.write("""<!DOCTYPE HTML PUBLIC"

    <html>

    <head>
        <title>REPORTE</title>
     <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
    </head>
    <body>
    <div class="container">
  <h2>Reporte de datos</h2>
  <p>Lista de arreglos</p>            
  <table class="table">
    <thead>
      <tr>
       <th>NOMBRE</th>
        <th>ARREGLO ORDENADO</th>
        <th>Palabra Reservada</th>
        <th>Numero a Buscar</th>
      </tr>
    </thead>

    """)

    for data in lista:
        aux = data[1]

        aux_parametro = None
        for option in data[2]:
            if "buscar" == option.lower():
                aux_parametro = aux.pop(len(data[1])-1)
        if aux_parametro != None:
                print("dato_a_buscar=" + str(aux_parametro))


        aux.sort()
        contenido += ("<tbody>"
                      "<td>" + data[0] + "</td>"
                                             "<td>" + str(aux) + "</td>"
                                                                       "<td>" + str(data[2]) + "</td>"
                                                                                                   "<td>" + str(aux_parametro) + "</td>"
                             "</tbody>")
    htmFile.write(contenido)

    htmFile.write("""






      </table>
    </div>
        </body>
        </html>""")

    htmFile.close