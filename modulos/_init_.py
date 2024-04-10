def crearestructura(jugadores,nombres,goals,goals_avoided,assists):     
     for nom,goles,golessalvados,asistencias in zip(nombres,goals,goals_avoided,assists):
         jugadores[nom]=(goles,golessalvados,asistencias)#esta tupla contiene 4 elementos
      #el nom[:-1] lo que hace es tomar el nombre del judor/a salvo el ultimo elemento que es la coma
     print(jugadores)#imprimimos para ver los resultados de como nos queda la lista momentaneameamente
     return jugadores


def maximogoleador(jugadores):
       return max(jugadores.items(), key=lambda j: j[1][0])


def jugadormasinfluyente(jugadores):
       masinfluyente=-1 # lo usamos como sumtario para sacar guardar el maximo
       nommasinflu=""
       for jugador,estadistica in jugadores.items():
             total = lambda datos: (estadistica[0]*1.5)+(estadistica[1]*1.25)+(estadistica[2])
             if total(estadistica) > masinfluyente:
                   masinfluyente=total(estadistica)
                   nommasinflu=jugador
       return   nommasinflu,masinfluyente


def golestotalespromedio(jugadores):
       return sum(gol[0] for  gol in jugadores.values())

