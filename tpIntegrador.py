'''
Desarrollar un CRUD para gestionar los datos de los dispositivos mencionados en el
escenario anterior. Adaptar los datos para que cada dispositivo incorpore un sensor de
humedad asociado (como atributo deberá registrar el valor de humedad detectado, un
% de 0 a 100) y si se encuentra operativo o no (a través de un campo de estado). Los
demás objetos del escenario no deben ser implementados.
'''

class Dispositivos:
    ''' Clase para administrar los dispositivos '''

    def __init__ (self, ID, descripcion, zonaDespliegue, valorHumedad = 0, estado = 'None', ubicacion= []):
        self.ID = ID
        self.descripcion = descripcion
        self.zonaDespliegue = zonaDespliegue
        self.ubicacion = ubicacion
        self.valorHumedad = valorHumedad
        self.estado = estado

     
                       
    def __str__(self):
        unDispositivo = f'El dispositivo {self.ID} ({self.descripcion}). Zona de despliegue: {self.zonaDespliegue}. Ubicación: {self.ubicacion[0]} {self.ubicacion[1]}° {self.ubicacion[2]}\' {self.ubicacion[3]}" | {self.ubicacion[4]} {self.ubicacion[5]}° {self.ubicacion[6]}\' {self.ubicacion[7]}"' 
        return unDispositivo
    
    def getID(self):
        return self.ID

    def getDescripcion(self):
        return self.descripcion

    def getZonaDespliegue(self):
        return self.zonaDespliegue
    
    def getUbicacion(self):
        return self.ubicacion
    
    def getValorHumedad(self):
        return self.valorHumedad

    def getEstado(self):
        return self.estado

    def setEstado(self, asignacion):
        self.estado = asignacion
        
    def setHumedad(self, value):
        self.valorHumedad = value   
    
# Carga de los dispositivos
def cargarDispositivo(datos):
    if datos == 0:
        dispositivos = []  # Se inicializa una lista vacía
    else:
        dispositivos = (datos)  # continua de la lista existente
    opcion = True
    while opcion:
        print('-' * 50)
        # Se sigue cargando
        # ID, descripcion, zonaDespliegue, ubicacion, valorHumedad, estado
        idTemp = input('Ingrese el ID del dispositivo: ')
        descripcionTemp = input('Ingrese la descripción del dispositivo: ')
        zonaDespliegueTemp = input('Ingrese la zona de despliegue: ')
        ubicacionTemp = [] # Guardará los grados, minutos y segundos
        print('A continuación, ingrese las coordenadas de la ubicación:')
        print('*' * 30)
        tempLat = (input('Ingrese la LATITUD (N/S): '))
        tempLat = tempLat.upper()
        while tempLat != 'N' and tempLat != 'S':
            print('Debe ingresar la letra "N" (Norte) o la letra "S" (Sur)')
            tempLat = (input('Ingrese nuevamente la LATITUD (N/S): '))
        ubicacionTemp.append(tempLat)
        tempGradosLat = int(input('Ingrese los grados: '))
        ubicacionTemp.append(tempGradosLat)
        tempMinLat = int(input('Ingrese los minutos: '))
        ubicacionTemp.append(tempMinLat)
        tempSegLat = (input('Ingrese los segundos: '))
        ubicacionTemp.append(tempSegLat)
        print('*' * 30)
        tempLong = (input('Ingrese la LONGITUD (E/O): '))
        tempLong = tempLong.upper()
        while tempLong != 'E' and tempLong != 'O':
            print('Debe ingresar la letra "E" (Este) o la letra "O" (Oeste)')
            tempLong = (input('Ingrese nuevamente la LONGITUD (E/O): '))
        ubicacionTemp.append(tempLong)
        tempGradosLong = int(input('Ingrese los grados: '))
        ubicacionTemp.append(tempGradosLong)
        tempMinLong = int(input('Ingrese los minutos: '))
        ubicacionTemp.append(tempMinLong)
        tempSegLong = (input('Ingrese los segundos: '))
        ubicacionTemp.append(tempSegLong)
        unDispositivo = Dispositivos(ID=idTemp, descripcion=descripcionTemp,
                        zonaDespliegue=zonaDespliegueTemp, ubicacion=ubicacionTemp)
        dispositivos.append(unDispositivo)
        eleccion = input('¿Desea seguir cargando otro dispositivo? S/N: ') #instancia de verificacion para continuar con la carga
        eleccion = eleccion.upper()
        if (eleccion != 'S'):
            opcion = False
    return dispositivos  # Se devuelve el resultado de la carga

# Reporte de los dispositivos
def imprimirDispositivos(dispositivos): # recibe la lista como argumento
    title = " Lista de dispositivos " 
    print('-' * 50)
    print (title.center(50, "="))
    print('-' * 50) #imprime 50 guiones para separar segmentos
    id = 0
    for unDispositivo in dispositivos: #recorre los objetos en la lista
        print(f'#{id} - {unDispositivo}')
        id += 1

# Seleccion de id y si actualiza o elimina
def seleccionarDispositivo(operacion, dispositivos): # me trae la lista y la opcion elegida (U o D)
    imprimirDispositivos(dispositivos) #imprime reporte de trabajos
    print('-' * 50)
    if (operacion == 'U'):
        while True:
            try:
                idDispositivo = int(input('Ingrese el número del dispositivo a modificar: '))
                dispositivos = modificarDispositivo(dispositivos, idDispositivo)
                break
            except ValueError:
                print ('Debe ingresar un número')
    elif (operacion == 'O'):
        while True:
            try:
                idDispositivo = int(input('Ingrese el número del dispositivo a cargar: '))
                dispositivos = cargaSensor(dispositivos, idDispositivo)
                break
            except ValueError:
                print ('Debe ingresar un número')
    else:
        while True:
            try:
                idDispositivo = int(input('Ingrese el número del dispositivo a eliminar: '))
                dispositivos = eliminarDispositivo(dispositivos, idDispositivo)
                break
            except ValueError:
                print ('Debe ingresar un número')
    return dispositivos

# Modificación
def modificarDispositivo(dispositivos, modificable): # recibe la lista y el id (argumentos en orden)
    print('-' * 50)
    print('Inicia actualización de datos:')
    if modificable <= (len(dispositivos)-1):
        temp = dispositivos[modificable] #Carga el item elegido
        idTemp = input(f'Ingrese el nuevo ID del dispositivo {temp.getID()}: ')
        descripcionTemp = input('Ingrese la nueva descripción del dispositivo: ')
        zonaDespliegueTemp = input('Ingrese la nueva zona de despliegue: ')
        ubicacionTemp = [] # Guardará los grados, minutos y segundos
        print('A continuación, ingrese las nuevas coordenadas de la ubicación:')
        print('*' * 30)
        tempLat = (input('Ingrese la LATITUD (N/S): '))
        tempLat = tempLat.upper()
        while tempLat != 'N' and tempLat != 'S':
            print('Debe ingresar la letra "N" (Norte) o la letra "S" (Sur)')
            tempLat = (input('Ingrese nuevamente la LATITUD (N/S): '))
        ubicacionTemp.append(tempLat)
        tempGradosLat = int(input('Ingrese los grados: '))
        ubicacionTemp.append(tempGradosLat)
        tempMinLat = int(input('Ingrese los minutos: '))
        ubicacionTemp.append(tempMinLat)
        tempSegLat = (input('Ingrese los segundos: '))
        ubicacionTemp.append(tempSegLat)
        print('*' * 30)
        tempLong = (input('Ingrese la LONGITUD (E/O): '))
        tempLong = tempLong.upper()
        while tempLong != 'E' and tempLong != 'O':
            print('Debe ingresar la letra "E" (Este) o la letra "O" (Oeste)')
            tempLong = (input('Ingrese nuevamente la LONGITUD (E/O): '))
        ubicacionTemp.append(tempLong)
        tempGradosLong = int(input('Ingrese los grados: '))
        ubicacionTemp.append(tempGradosLong)
        tempMinLong = int(input('Ingrese los minutos: '))
        ubicacionTemp.append(tempMinLong)
        tempSegLong = (input('Ingrese los segundos: '))
        ubicacionTemp.append(tempSegLong)
        unDispositivo = Dispositivos(ID=idTemp, descripcion=descripcionTemp,
                        zonaDespliegue=zonaDespliegueTemp, ubicacion=ubicacionTemp)
        dispositivos[modificable] = unDispositivo
        print('El dispositivo se ha modificado correctamente')
    else:
        print('** ATENCION ** - El dispositivo que desea modificar NO EXISTE')
    return dispositivos

# Eliminación del dispositivo
def eliminarDispositivo(dispositivos, eliminable): # recibe la lista y el id (argumentos en orden)
    print('-' * 50)
    if eliminable <= (len(dispositivos)-1):
        print('Confirma que desea eliminar el siguiente dispositivo?')
        unDispositivo = dispositivos[eliminable] # llama al item elegido
        print(f'{unDispositivo}')
        confirmar = input('Confirma eliminación? S / N ')
        confirmar = confirmar.upper()
        while confirmar != 'S' and confirmar != 'N':
                print('por favor elijan entre las opciones S/N')
                confirmar = input('Confirma eliminación? S / N ')
                confirmar = confirmar.upper()
        if (confirmar == 'S'):
            dispositivos.remove(unDispositivo) # el .remove procede a eliminar un item de la lista.
            print('La eliminación se ha realizado correctamente')
        elif (confirmar == 'N'):
            print('No se ha borrado ningún elemento')
            pass
    else:
        print('** ATENCION ** - El dispositivo seleccionado NO EXISTE')
    return dispositivos

# Proceso de carga de valores de humedad y estado del dispositivo
def cargaSensor(dispositivos, elegido): # recibe la lista y el id (argumentos en orden)
    print('-' * 50)
    print('CARGA DE VALORES DEL SENSOR DE HUMEDAD')
    opcion = 'O'
    print('-' * 50)
    if elegido <= (len(dispositivos)-1):
        unDispositivo = dispositivos[elegido] # llama al item elegido
        print('Ingrese el estado actual del dispositivo')
        estadoTemp = input('\"A\" para ACTIVO o \"I\" para INACTIVO: ')
        estadoTemp = estadoTemp.upper()
        unDispositivo.setEstado(estadoTemp)
        if estadoTemp == 'A':
            while True:
                try:
                    valueSensor = int(input('Ingrese el valor del sensor: '))
                    unDispositivo.setHumedad(valueSensor)
                    print('El valor se ha cargado correctamente.')
                    break
                except ValueError:
                    print('Por favor ingrese un valor numérico entre 0 y 100')
        else:
            print('El dispositivo seleccionado no se encuentra Activo')
            print('debe cambiar el estado para cargar los valores')
    else:
        print('El número del dispositivo solicitado NO EXISTE')
    eleccion = input('¿Desea seguir cargando otro dispositivo? S/N: ') #instancia de verificacion para continuar con la carga
    eleccion = eleccion.upper()
    if eleccion == 'S':
        dispositivos = seleccionarDispositivo(opcion, dispositivos)
    return dispositivos

# Informar dispositivos debajo del valor de humedad solicitado
def informarDispositivos(dispositivos):
    print('-' * 50)
    listaTemp = []
    limiteTemp = int(input('Ingrese el valor límite: '))
    for unDispositivo in dispositivos:
        if unDispositivo.getEstado() == 'A':
            if unDispositivo.getValorHumedad() < limiteTemp:
                listaTemp.append(unDispositivo)
            else:
                pass
    print('Los dispositivos por debajo del límite dispuestos son:')
    for unDispositivo in listaTemp:
        print(unDispositivo)
    return dispositivos


def menu():
    datos = []
    titulo = " Menú de Inicio ".upper() 
    print('-' * 50)
    print (titulo.center(50, "="))
    opcion = 'P'
    while (opcion != 'X'):
        print('-' * 50)
        print('Seleccione la opción a ejecutar:')
        print('[C] Agregar un dispositivo')
        print('[R] Obtener listado de dispositivos')
        print('[U] Modificar valores de un dispositivo')
        print('[D] Eliminar un dispositivo')
        print('[O] Cargar valores del sensor de Humedad')
        print('[S] Informar censados inferiores')
        print('[X] Salir')
        opcion = input('Opción elegida: ')
        opcion = opcion.upper() # devuelve el input en mayúscula
        if (opcion == 'C'):
            datos = cargarDispositivo(datos)
        elif (opcion == 'R'):
            imprimirDispositivos(datos)
        elif (opcion == 'U' or opcion == 'D' or opcion == 'O'):
            datos = seleccionarDispositivo(opcion, datos)
        elif (opcion == 'S'):
           informarDispositivos(datos)


menu()