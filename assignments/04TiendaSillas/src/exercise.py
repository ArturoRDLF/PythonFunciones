# Escribe tus funciones abajo de esta línea
def precio_tipo_silla(tipo):
    if tipo == 'B':
        return 700
    elif tipo == 'E':
        return 900
    elif tipo == 'L':
        return 1500
def descuento(total,cliente):
    if cliente == 'F':
        return total*0.2
    elif cliente == 'N':
        if total >= 10000 and total < 20000:
            return total*0.10
        elif total >= 20000:
            return total*0.15
        else:
            return total*0
def main():
    # Escribe tu código abajo de esta línea
    tipo_silla = input('Tipo silla: ')
    p = precio_tipo_silla(tipo_silla)
    
    tipo_cliente = input('Tipo cliente: ')
    
    cantidad = int(input('Cantidad de sillas: '))
    sin_descuento = float(p * cantidad)
    descuent0 = descuento(sin_descuento,tipo_cliente)
    
    print(f'Total sin dcto. ${sin_descuento:>7}')
    print(f'Descuento       ${descuent0:>7}')
    
    total_a_pagar = sin_descuento - descuent0
    print(f'Total a pagar    ${total_a_pagar:>7}')

if __name__ == '__main__':
    main()
