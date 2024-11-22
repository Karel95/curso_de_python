# SRP (Single Responsability Principle)

# # sin aplicar el principio de SRP:
# class Auto():
#   def __init__(self):
#     self.position = 0
#     self.combustible = 100

#   def avanzar(self, distancia):
#     if self.combustible >= distancia/2:
#       self.position += distancia
#       self.combustible -= distancia/2
    
#     else:
#       print("No hay combustible suficiente para avanzar")
  
#   def repostar(self, cantidad):
#     self.combustible += cantidad
  
#   def mostrar_estado(self):
#     print(f"Posicion: {self.position}")
#     print(f"Combustible: {self.combustible}")


# aplicando el principio de SRP:
class Auto():
  def __init__(self, tanque):
    self.position = 0
    self.tanque = tanque

  def avanzar(self, distancia):
    if self.tanque.get_fuel() > distancia/5:
      self.position += distancia
      self.tanque.use_fuel(distancia/5)
      print(f"El auto ha avanzado {self.position} kilometros.")
      
    
    
    else:
      print("No hay combustible suficiente para avanzar.")
  
  def mostrar_estado(self):
    print(f"Posicion: {self.position} kilometros")
    print(f"Combustible: {self.tanque.get_fuel()} litros")

class TanqueDeCombustible():
  def __init__(self, cantidad):
    self.combustible = cantidad

  def repostar(self, cantidad):
    self.combustible += cantidad
  
  def get_fuel(self):
    return self.combustible
  
  def use_fuel(self, cantidad):
    self.combustible -= cantidad
    if self.combustible < 0:
      self.combustible = 0

# # ejemplos:
# tanque1 = TanqueDeCombustible(100)
# auto1 = Auto(tanque1)
# auto1.mostrar_estado()
# auto1.avanzar(200)
# auto1.mostrar_estado()
# auto1.avanzar(200)
# auto1.mostrar_estado()
# auto1.avanzar(100)
# auto1.mostrar_estado()
# auto1.avanzar(1)
# auto1.mostrar_estado()
# tanque1.repostar(50)
# auto1.mostrar_estado()


# OCP (Open/Closed Principle)

class Notificador:
  def __init__(self, usuario, mensaje):
    self.usuario = usuario
    self.mensaje = mensaje
    
  def notificar(self):
    raise NotImplementedError("La clase debe implementar el método notificar")
  
class EmailNotificador(Notificador):
  def notificar(self):
    print(f"Enviando correo a {self.usuario}: {self.mensaje}")

class SMSNotificador(Notificador):
  def notificar(self):
    print(f"Enviando SMS a {self.usuario}: {self.mensaje}")
    
class WhatsappNotificador(Notificador):
  def notificar(self):
    print(f"Enviando Whatsapp a {self.usuario}: {self.mensaje}")
    
# # Ejemplos:
# notificacion1 = EmailNotificador('John Doe', 'Hola johndoe@mail.test')

# notificacion1.notificar()


# LSP (Liskov's Substitution Principle)

# Ejemplos:
class Mamifero:
  pass # caracteristicas comunes de todos los mamiferos

class MamiferoTerrestre(Mamifero):
  # caracteristicas especificas de esta clase de mamiferos
  def correr(self):
    print("Corriendo")

class MamiferoAcuatico(Mamifero):
  # caracteristicas especificas de esta clase de mamiferos
  def nadar(self):
    print("Nadando")

class MamiferoVolador(Mamifero):
  # caracteristicas especificas de esta clase de mamiferos
  def volar(self):
    print("Volando")

# # Ejemplos:
# perro = MamiferoTerrestre()
# murcielago = MamiferoVolador()
# ballena = MamiferoAcuatico()

# perro.correr()
# murcielago.volar()
# ballena.nadar()


# ISP (Interface Segregation Principle)

# Tarea


# DIP (Dependency Inversion Principle)

# Tarea
