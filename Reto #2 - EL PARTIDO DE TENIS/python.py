
import random

def tennis_match_auto():
    print("""
          BIENVENIDO AL SIMULADOR AUTOMATICO DE JUEGOS DE TENNIS 
                by Adrian Guerra
          """)
    
    puntaje = {0:"Love", 1:15, 2:30, 3:40, 4:"Ventaja"}
    pp1 = 0
    pp2 = 0
    namep1 = input("ingles el nombre del jugador 1: ").lower()
    namep2 = input("ingles el nombre del jugador 2: ").lower()
    game = []
    
    while True:
        whoscored = random.randint(1, 2)
        
        match whoscored:
            case 1:
                pp1 += 1
            case 2: 
                pp2 += 1
                
        if pp1 >= 5:
            print(f"Ha ganado el jugador 1 {namep1}")
            break
        if pp2 >= 5:
            print(f"Ha ganado el jugador 2 {namep2}")
            break
               
        if pp1 == pp2:
            print(f"""
            Marcador actual:
              {namep1} {puntaje[pp1]} - {namep2} {puntaje[pp2]} "Deuce"
                )
            """)
            continue
        print(f"""
            Marcador actual:
                {namep1} {puntaje[pp1]} - {namep2} {puntaje[pp2]} 
                )
            """)

def tennis_match_manual():

    print("""
      BIENVENIDO AL SIMULADOR DE JUEGOS DE TENNIS 
                by Adrian Guerra
      """)
    
    #Variables 
    puntaje = {0:"Love", 1:15, 2:30, 3:40, 4:"Ventaja"}
    pp1 = 0
    pp2 = 0
    namep1 = input("ingles el nombre del jugador 1: ").lower()
    namep2 = input("ingles el nombre del jugador 2: ").lower()
    game = []


    while True:
        actualpoint = input(f"Quien anotó el punto ? [P1] ({namep1}) ó [P2] ({namep2}?)").lower()
        
        if actualpoint == "p1" or actualpoint == "p2":
            match actualpoint:
                case "p1":
                    pp1 +=1
                case "p2":
                    pp2 +=1
            if pp1 == pp2 :
                
                print(f"""
        Marcador actual:
              {namep1} {puntaje[pp1]} - {namep2} {puntaje[pp2]} "Deuce"
              """)
                
            elif pp1 == 5:
                print(f"Ha ganado el jugardor 1 {namep1}")
                break
            elif pp2 == 5:
                print(f"Ha ganado el jugardor 2: {namep2}")
                break

        else :
            print("Inpur Error")
            
            
        print(f"""
        Marcador actual:
              {namep1} {puntaje[pp1]} - {namep2} {puntaje[pp2]}
              """)
        
while True: 
    quest = input("Quieres que el juego sea automático [1] o manual [2]?")
    
    if quest == "1":
        tennis_match_auto()
    elif quest == "2":
        tennis_match_manual()
    else:
        print("input error")