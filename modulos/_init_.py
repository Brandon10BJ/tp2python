def crearestructura(jugadores,nombres,goals,goals_avoided,assists):     
     for nom,goles,golessalvados,asistencias in zip(nombres,goals,goals_avoided,assists):
         jugadores[nom]=(goles,golessalvados,asistencias)#esta tupla contiene 4 elementos
      #el nom[:-1] lo que hace es tomar el nombre del judor/a salvo el ultimo elemento que es la coma
     print(jugadores)#imprimimos para ver los resultados de como nos queda la lista momentaneameamente
     return jugadores