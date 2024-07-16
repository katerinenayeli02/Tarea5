def main():
    while True:
        print('Por favor seleccione el proceso que desea realizar.')
        print('1:Ingrese puntos de calificación y comentarios.')
        print('2:Consulta los resultados hasta el momento.')
        print('3:Finalizar')
        num = input()

        if num.isdecimal():
            num = int(num)

            if num == 1:
                ingresar_calificacion()
                # while True:
                #     print('Por favor ingresa tu calificación del 1 al 5')
                #     point = input()
                #     if point.isdecimal():
                #         point = int(point)
                #         if  point <= 0 or point > 5: # Expresión condicional menor o igual a 0 o mayor que 5
                #             print('Por favor ingresa del 1 al 5')
                #             point = input()
                #         else:
                #             print('Por favor ingresa tu comentario')
                #             comment = input()
                #             post = f'punto: {point} comentario: {comment}'
                #             file_pc = open("data.txt", 'a')
                #             file_pc.write(f'{ post } \n')
                #             file_pc.close()
                #             break
                #     else:
                #         print('Por favor ingrese los puntos de evaluación en números.')
            elif num == 2:
                consultar_resultados()
            #   print('Resultados hasta ahora')
            #   read_file = open("data.txt", "r")
            #   print( read_file.read() )
            #   read_file.close()
            elif num == 3:
                print('Terminado.')
                break  # Sintaxis para finalizar el procesamiento repetido
            else:
                print('Por favor ingresa del 1 al 3')
        else:
            print('Por favor ingresa del 1 al 3')


def ingresar_calificacion():
    while True:
        print('Por favor ingresa tu calificación del 1 al 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Por favor ingresa del 1 al 5')
            else:
                print('Por favor ingresa tu comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Por favor ingrese los puntos de evaluación en números.')


def consultar_resultados():
    print('Resultados hasta ahora')
    with open("data.txt", "r") as read_file:
        print(read_file.read())


if __name__ == "__main__":
    main()