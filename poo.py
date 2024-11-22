# herencia
class Celular:
  def __init__(self,marca,modelo,precio):
    self.marca=marca
    self.modelo=modelo
    self.precio=precio
  
  def imprimir_datos(self):
    print(f"""
          Marca: {self.marca}
          Modelo: {self.modelo}
          Precio: {self.precio}
          """)

# marca = input("Ingrese la marca del celular: ")
# modelo = input("Ingrese el modelo del celular: ")
# precio = int(input("Ingrese el precio del celular: "))

# celular1 = Celular(marca,modelo,precio)
# celular1.imprimir_datos()


class GPS(Celular):
  def __init__(self,marca,modelo,precio,velocidad_maxima):
    super().__init__(marca,modelo,precio)
    self.velocidad_maxima=velocidad_maxima
  
  def imprimir_velocity(self):
    print(f"Velocidad Maxima: {self.velocidad_maxima}")

# velocidad_maxima = int(input("Ingrese la velocidad máxima del GPS: "))

# gps1 = GPS(marca,modelo,precio,velocidad_maxima)
# gps1.imprimir_datos()
# gps1.imprimir_velocity()


class Radio:
  def __init__(self, signal):
    self.signal=signal
    
  def imprimir_signal(self):
    print(f"Signal: {self.signal}")

# signal = input("Ingrese el signal del celular: ")

# radio1 = Radio(signal)
# radio1.imprimir_signal()


class PC(GPS, Radio):
    def __init__(self, marca, modelo, precio, velocidad_maxima, ram, disco_duro, signal):
        GPS.__init__(self, marca, modelo, precio, velocidad_maxima)
        Radio.__init__(self, signal)
        self.ram = ram
        self.disco_duro = disco_duro
    
    def imprimir_pc_info(self):
        print(f"""
        Ram: {self.ram}
        Disco Duro: {self.disco_duro}
        """)
    
# ram = int(input("Ingrese la cantidad de ram: "))
# disco_duro = input("Ingrese el tamaño del disco duro: ")

# pc1 = PC(marca, modelo, precio, velocidad_maxima, ram, disco_duro, signal)
# pc1.imprimir_datos()
# pc1.imprimir_velocity()
# pc1.imprimir_signal()
# pc1.imprimir_pc_info()


# encapsulamiento:
class Encapsulamiento:
  def __init__(self, marca, modelo, precio):
    self.__marca=marca
    self.__modelo=modelo
    self.__precio=precio
    #se puede acceder a los atributos encapsulados con el uso de getters y setters:
  
  def __get_phone(self):
    print(self.__marca, self.__modelo, self.__precio)
  
  # Getter for marca
  def get_marca(self):
      return self.__marca
  # Setter for marca
  def set_marca(self, marca):
      self.__marca = marca

  # Getter for modelo
  def get_modelo(self):
      return self.__modelo
  # Setter for modelo
  def set_modelo(self, modelo):
      self.__modelo = modelo

  # decorador property, convierte a la funcion en una propiedad:
  # Getter for precio
  @property
  def get_precio(self):
        return self.__precio
  # Setter for precio
  def set_precio(self, nuevo_precio):
      self.__precio = nuevo_precio
    
  # Método público para acceder al método privado
  def mostrar_phone(self):
      self.__get_phone()

encapsulamiento1 = Encapsulamiento("Samsung", "S20", 4000)

# print(encapsulamiento1.__marca)  # Error: No se puede acceder directamente a __marca
# print(encapsulamiento1.__modelo) # Error: No se puede acceder directamente a __modelo
# print(encapsulamiento1.__precio) # Error: No se puede acceder directamente a __precio

# encapsulamiento1.__get_phone()   # Error: No se puede acceder directamente a __get_phone()
# encapsulamiento1.mostrar_phone()


# # decoradores
# def decorador(funcion):
#     def envoltura():
#       print("Función antes de ejecutar...")
#       funcion()
#       print("Función después de ejecutar...")
#     return envoltura

# # 1ra variante:
# @decorador
# def saludar():
#   print("Hola mundo...")

# saludar()

# # 2da variante:
# saludo_decorado = decorador(saludar)
# saludo_decorado()

# diferencias entre getters sin y con @property:
marca1 = encapsulamiento1.get_marca()
modelo1 = encapsulamiento1.get_modelo()
precio1 = encapsulamiento1.get_precio

print(f"Marca: {marca1}, Modelo: {modelo1}, Precio: {precio1}")

# setters:
encapsulamiento1.set_marca("Huawei")
encapsulamiento1.set_modelo("Honor")
encapsulamiento1.set_precio(5000)

marca2 = encapsulamiento1.get_marca()
modelo2 = encapsulamiento1.get_modelo()
precio2 = encapsulamiento1.get_precio

print(f"Marca: {marca2}, Modelo: {modelo2}, Precio: {precio2}")

# setters:
encapsulamiento1.set_marca("Iphone")
encapsulamiento1.set_modelo("X")
encapsulamiento1.set_precio(6000)

marca3 = encapsulamiento1.get_marca()
modelo3 = encapsulamiento1.get_modelo()
precio3 = encapsulamiento1.get_precio

print(f"Marca: {marca3}, Modelo: {modelo3}, Precio: {precio3}")

# # delete:
# del encapsulamiento1.set_marca
# del encapsulamiento1.set_modelo
# del encapsulamiento1.set_precio

# print(f"Marca: {marca1}, Modelo: {modelo1}, Precio: {precio1}") # AttributeError: 'Encapsulamiento' object has not those attributes anymore.
