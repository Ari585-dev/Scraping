from scrapeo import scrp1
from scrapeo import scrp2
from scrapeo import scrp3

#scrp1()
#scrp2()
#scrp3()

menu= int(input('*******MENÚ DE SELECCIÓN*******: \n 1-GAMERSCOLOMBIA \n 2-ASYSCOMPUTADORES \n 3-PANAMERICANA \n 0-SALIR \n'))

while menu !=0:
  if menu == 1:
    print("GAMERS COLOMBIA \n")
    scrp1()

  elif menu == 2:
    print("ASYS COMPUTADORES \n")
    scrp2()

  elif menu == 3:
    print("PANAMERICANA \n")
    scrp3()
  
  else: 
    print("¡OPCIÓN INVÁLIDA!")

  menu= int(input('*******MENÚ DE SELECCIÓN*******: \n 1-GAMERSCOLOMBIA \n 2-ASYSCOMPUTADORES \n 3-PANAMERICANA \n 0-SALIR\n'))
  










