
#======================PRUEBA DE CLASS=====================
class Cliente:
    def __init__(self,ID,cuil,nombre,apellidos,telefono,email):
        #atributo = varialbe que se asigna al atributo de c/objeto de la clase
        self.ID = ID
        self.cuil = cuil
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email

    def __repr__(self):
        return str(self.__dict__)

    def presentar_cliente(self):
        print(f"{self.ID}\t{self.cuil}\t{self.nombre}\t{self.apellidos}\t{self.telefono}\t{self.email}")

    def mostrar_ID(self):
        print(f"{self.ID}\t\t{self.apellidos}")

    def encontrar_ID(self,indice):
        if indice == self.ID:
            return True
        else:
            return False

    def pasar_ID(self):
        return self.ID

    def pasar_cuil(self):
        return self.cuil
        
    def pasar_nombre(self):
        return self.nombre

    def pasar_apellidos(self):
        return self.apellidos

    def pasar_telefono(self):
        return self.telefono

    def pasar_email(self):
        return self.email

class Pedidos(Cliente):
    def __init__(self,ID,cuil,nombre,apellidos,telefono,email,fecha,producto,cantidad,importe):
        
        Cliente. __init__(self,ID,cuil,nombre,apellidos,telefono,email)
        self.fecha = fecha
        self.producto = producto
        self.cantidad = cantidad
        self.importe = importe
    

    def listar_pedidos(self):
        #Apellidos  Producto    Cantidad    Cobrar  Fecha
        print(f'{self.apellidos}\t\t{self.producto}\t\t{self.cantidad}\t\t{self.importe}\t\t{self.fecha}')


class Producto():
    def __init__(self,nombre,forma_venta,precio):
        self.nombre = nombre
        self.forma_venta = forma_venta
        self.precio = precio

    def mostrar_producto(self):
        if self.forma_venta==1:
            tipo = '[Kg]'
        else:
            tipo = '[Unidades]'
        print(f'{self.nombre}\t\t{tipo}\t\t{self.precio}')
    
    def encontrar_producto(self,x):
        if x == self.nombre:
            return True
        else:
            return False
    
    def pasar_precio(self):
        return self.precio

#========================LISTAS, TUPLAS O DICCIONARIOS==================
menu = {'1': '\n1-Agregar cliente', '2': '2-Borrar cliente', '3': '3-Agregr pedido',
        '4': '4-Marcar pedido como completado', '5': '5-Agregar producto', '6': '6-Borrar producto',
       'm':'m-Mostrar clientes','p':'p-Mostrar pedidos', 'F': 'F-Finalizar'}

lista_clientes = []
lista_pedidos = []
lista_productos = []
#====================FUNCIONES=============================
#==========================================================

#====================menu=============================
def funcion_menu():
    print('----------------MENU-------------------')
    for i in menu:
        print(menu[i])
    while True:
        try:
            opc = str(input("\nSu opcion: "))
            return opc
            
        except ValueError:
            print('Error de ingreso, vuelva a intentar.')

#====================eleccion en menu=============================
def determinar_eleccion(opc):
    if opc == '1':
        print("Creando cliente nuevo...")
        agregar_cliente()
        return False

    elif opc == '2':
        if (len(lista_clientes))<1:
            print('Todavia no se crearon clientes')
            pass
        else:
            print("Accediendo a borrar cliente...")
            borrar_cliente()
        return False
            
    elif opc == '3':
        if (len(lista_clientes))<1:
            print('Todavia no se crearon clientes')
            pass
        else:
            print("Accediendo a agregar pedido...")
            agregar_pedido()
        return False
    
    elif opc == '5':
        print("Accediendo a agregar producto...")
        crear_producto()
        return False

    elif opc == '6':
        if len(lista_productos)<1:
            print('Primero crea algun producto vithe')
            pass
        else:
            print("Accediendo a borrar producto...")
            borrar_producto()
        return False    

    elif opc == 'm':
        if len(lista_clientes)<1:
            print('\nTodavia no hay clientes.')
            pass
        else:
            print("\nListando clientes: ")
            print('ID\tCuil\tNombre\tApellidos\ttelefono\temail')
            for i in range(len(lista_clientes)):
                lista_clientes[i].presentar_cliente()
            return False

    elif opc == 'p':

        if len(lista_pedidos)<1:
            print('Todavia no hay pedidos.')
            pass
        else:
            #Apellidos  Producto    Cantidad    Cobrar  Fecha
            print("Listando pedidos: ")
            print("\nApellidos\tProducto\tCantidad\tCobrar\tFecha")
            for i in range(len(lista_pedidos)):
                lista_pedidos[i].listar_pedidos()
        return False

    elif opc == 'F':
        print('Saliendo...')
        return True
    else:
        print ('La opcion ingresada no es valida')
        return False

#====================agregar cliente=============================
def agregar_cliente():
    
    while True:
        try:
            nombre = str(input('\nIngrese nombre: '))
            break
        except ValueError:
            print('vuelva a tipear: ')

    while True:
        try:
            apellidos = str(input('Ingrese apellidos: '))
            break
        except ValueError:
            print('vuelva a tipear: ')

    while True:
        try:
            cuil = int(input('ingrese cuil: '))
            #se puede restringir longitud
            break
        except ValueError:
            print('vuelva a tipear: ')

    while True:
        try:
            telefono = int(input('ingrese telefono: '))
            break
        except ValueError:
            print('vuelva a tipear: ')
    
    while True:
        try:
            email = str(input('ingrese email: '))
            break
        except ValueError:
            print('vuelva a tipear: ')

    ID=apellidos[0]+'00'+str(len(lista_clientes))
    Persona = Cliente(ID, cuil, nombre, apellidos, telefono, email)
    lista_clientes.append(Persona)

#====================borrar cliente=============================
def borrar_cliente():  
    result,i=busqueda_por_ID()
 
    if result == True:
         print("\nSe esta eliminando elemento...")
         lista_clientes.pop(i)
    else:
        print("\nNo se encontro el ID buscado")  

#====================agregar pedido=============================
def agregar_pedido():
    result=i=0
    result,i=busqueda_por_ID()
 
    if result == True:
        print('Producto\tVentaX\t\tPrecio')
        for j in range(len(lista_productos)):
            lista_productos[j].mostrar_producto()

        while True:
            print('\nElija nombre valido de producto: ')
            try:
                nombre_producto = str(input())
                #verificando si producto ya existe:
                Coincidencia = False
                for k in range(len(lista_productos)):
                    Coincidencia = lista_productos[k].encontrar_producto(nombre_producto)
                    if Coincidencia == True:
                        break 
                if Coincidencia == True:
                    break
                else:
                    print('no se encontro el producto tipeado.')
            except ValueError:
                print('Debe ingresar un nombre correcto de producto;')

        while True:
            try:
                cantidad_producto = float(input('Inserte cantidad [kg] o [unidades] de producto: '))
                break
            except ValueError:
                print('Error! ingrese un numero indicativo de la cantidad')

        while True:
            try:
                fecha = str(input('Inserte fecha de entrega [ej: 23/06/2021]: '))
                if (len(fecha))==10:
                    break
                else:
                    print('Error, debe tener formato [dd/mm/aaaa]')
            except ValueError:
                print('Error! debe ser un string, debe tener formato [dd/mm/aaaa].')

        importe = cantidad_producto * lista_productos[i].pasar_precio()

        id_cliente = lista_clientes[i].pasar_ID()
        cuil_cliente = lista_clientes[i].pasar_cuil()
        nombre_cliente = lista_clientes[i].pasar_nombre()
        apellidos_cliente = lista_clientes[i].pasar_apellidos()
        telefono_cliente = lista_clientes[i].pasar_telefono()
        email_cliente = lista_clientes[i].pasar_email()
        print("\nPedido nuevo agendado.")
        
        
        # (ID,cuil,nombre,apellidos,telefono,email,fecha,producto,cantidad):

        pedido = Pedidos(id_cliente,cuil_cliente,nombre_cliente,apellidos_cliente,telefono_cliente,email_cliente,fecha, nombre_producto, cantidad_producto,importe)      
         #ver tema de herencia, puede ser la solucion
         #tengo que lograr vincular los dos objetos
        lista_pedidos.append(pedido)
         
    else:
        print("\nNo se encontro el ID buscado")
#====================agregar un nuevo producto=============================
def crear_producto():
    while True:  
        print('Ingrese nombre de producto: ')  
        try:
            nombre_producto = str(input())

            #verificando si producto ya existe:
            Coincidencia = False
            for i in range(len(lista_productos)):
                Coincidencia = lista_productos[i].encontrar_producto(nombre_producto)

            if Coincidencia == True:
                print('El producto ya existe. Vuelva a intentar')      
            else:
                break                  

        except ValueError:
            print('Error! ingrese nombre de producto. Ej: poroto')

    while True:  
        print('\nIngrese el tipo de unidad de venta: ')
        print('1)Kg\t2)Unidades') 

        try:
            forma_venta = int(input())
            if (forma_venta < 1) or (forma_venta > 2):
                print('Opcion invalida, vuelva a a intentar.')
            else:
                break 
            #   break
        except ValueError:
            print('Error! debe ingresar 1 o 2')

    while True:  
        print('\nIngrese el precio: ')
        try:
            precio = float(input())
            if precio < 0.0:
                print('Opcion invalida, vuelva a a intentar.')
            else:
                break 
            #   break
        except ValueError:
            print('Error! debe ingresar un valor en pesos mayor a cero')
        
    producto = Producto(nombre_producto, forma_venta,precio)

    lista_productos.append(producto)
#====================borrar producto=============================
def borrar_producto():
        print('\n********************************************')
        print('productos disponibles: ')   
        for i in range(len(lista_productos)):
            lista_productos[i].mostrar_producto()
        
        while True:  
            print('\nIngrese nombre valido de producto a eliminar: ')
            try:
                nombre_producto = str(input())

                #verificando si producto ya existe:
                Coincidencia = False
                for i in range(len(lista_productos)):
                    Coincidencia = lista_productos[i].encontrar_producto(nombre_producto)
                    if Coincidencia == True:
                        lista_productos.pop(i)
                        break
                if Coincidencia == True:
                    print('El producto se elimino con exito')
                    break      
                else:
                    print('El producto ingresado no existe. Intente de nuevo!')                  

            except ValueError:
                print('Error! ingrese nombre de producto. Ej: poroto')


#====================buscar cliente por ID=============================
def busqueda_por_ID():
    bandera_1=False
    i=0
    print('ID\t\tApellidos')
    for i in range(len(lista_clientes)): #mostramos los clientes disponibles
            lista_clientes[i].mostrar_ID()
    print('Por favor, ingrese un ID valido: ')

    indice=str(input())
    for i in range(len(lista_clientes)):
            bandera_1=lista_clientes[i].encontrar_ID(indice) #el metodo encontrar_ID compara
                                                #el string ingresado con el
                                                #atributo ID del objeto
                                                #si se encuentra retorna true
            if bandera_1 == True:
                break

    return bandera_1,i

#===================SUPERLOOP=============================
#=========================================================
print("Este es un programa experto para verduleros. \n")
Finalizar = False

while Finalizar == False:
    opc = funcion_menu()
    Finalizar = determinar_eleccion(opc) 

    
#===========================================================


