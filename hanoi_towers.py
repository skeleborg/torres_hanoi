# Importamos módulos
import sys

# Declaramos e inicializamos tres listas. Cada lista será una de las torres del puzzle.
# El juego comienza con la torre formada en la torre de la izquierda. Las otras dos empiezan vacías.
# Los discos serán representados con números, cuanto más grande el número mayor el diámetro del disco:
# 1 -> disco más pequeño
# 4 -> disco más grande    
t_izq = [4, 3, 2, 1]   # Torre izquierda
t_cen = []             # Torre central
t_der = []             # Torre derecha
        
# Mostramos el estado de las torres después de cada movimiento.
# Finalizamos el juego si el jugador ha colocado todos los discos en la torre de la derecha, en el orden correcto.
def get_status(t_izq, t_cen, t_der):
    print("Torre izquierda: ", t_izq, "\nTorre central: ", t_cen, "\nTorre derecha: ", t_der, "\n")
    
    if len(t_izq) == 0 and len(t_cen) == 0 and t_der == [4, 3, 2, 1]:
        print("¡¡JUEGO TERMINADO!!\n")
        return 0    

# Obtenemos el input del usuario.
# Se comprobará que se ha introducido el tipo de dato que se espera (un número del 1 al 3)
# Si el dato no es correcto, se devolverá un mensaje de error y se volverá a pedir un input al usuario.
def get_input():        
    try :            
        src = int(input("1 - Selecciona una torre para coger un disco.\n(1 - izquierda, 2 - central, 3 - derecha)\n> "))
        dst = int(input("\n2 - Selecciona una torre para dejar el disco.\n(1 - izquierda, 2 - central, 3 - derecha)\n> "))
    except:
        print("¡No has escogido un número!\n")
        return -1
    else:
        if (src < 0 or src > 3) or (dst < 0 or dst > 3):
            print("¡No has escogido un número del 1 al 3!\n")
            return -1    
    return src, dst

# Evaluamos el estado de las torres después de cada movimiento, y enviamos un mensaje al usuario
# para indicarle si su movimiento ha sido correcto o si se está incumpliendo alguna de las reglas.
# Si el movimiento es correcto, lo aplicamos.
def make_move(src, dst, t_izq, t_cen, t_der):
    print("Has elegido dejar el disco de la torre ", src, " en la torre ", dst, ".")
    
    # Verificamos que la torre seleccionada como origen tiene algún disco
    if (src == 1 and len(t_izq) == 0) or (src == 2 and len(t_cen) == 0) or (src == 3 and len(t_der) == 0):
        print("ERROR - Has seleccionado como origen una torre vacía. Movimiento no permitido.\n")
        return -1
    # Verificamos que el jugador ha hecho un movimiento permitido
    elif abs(dst - src) != 1:
        print("ERROR - Estás intentando mover un disco entre torres no adyacentes o sobre la misma torre. Movimiento no permitido.\n")
        return -1
    else:            
        # Verificamos que se va a colocar el disco en una torre correcta;
        # es decir, que se va a montar sobre un disco de mayor valor o en una torre vacía
        # Si es correcto, hacemos efectivo el movimiento.
        if src == 1 and dst == 2:
            if len(t_cen) == 0 or t_izq[-1] < t_cen[-1]:
                t_cen.append(t_izq.pop())
                return
        elif src == 2 and dst == 3:
            if len(t_der) == 0 or t_cen[-1] < t_der[-1]:
                t_der.append(t_cen.pop())
                return
        elif src == 3 and dst == 2:
            if len(t_cen) == 0 or t_der[-1] < t_cen[-1]:
                t_cen.append(t_der.pop())
                return
        elif src == 2 and dst == 1:
            if len(t_izq) == 0 or t_cen[-1] < t_izq[-1]:
                t_izq.append(t_cen.pop())
                return        
        print("ERROR - Estás intentando colocar un disco de mayor tamaño sobre un disco de menor tamaño. Movimiento no permitido.\n")    
    
    
# BUCLE DEL JUEGO    
while True:
    # FASE 1 - Mostramos el estado de las torres
    if get_status(t_izq, t_cen, t_der) == 0:
        sys.exit()
    
    # FASE 2 - Obtenemos el input del usuario
    user_input = -1
    while user_input == -1:
        user_input = get_input()        
    src = user_input[0]
    dst = user_input[1]
    
    # FASE 3 - Una vez obtenido un input válido, comprobamos la validez del propio movimiento elegido
    # por el jugador y aplicamos el cambio de ser correcto
    make_move(src, dst, t_izq, t_cen, t_der)