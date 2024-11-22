from abc import ABC, abstractmethod # para crear clases abstractas


# Las clases abstractas tienen al menos una función abstracta
# para ser usada como base de otras clases

class MyClass(ABC):
  @classmethod # para indicar que es un metodo de clase
  @abstractmethod # para indicar que es una funcion abstracta
  def __init__(self, name, email):
    self._name = name
    self._email = email
  
  @classmethod
  def my_method(cls):
    pass
  
  def hello_world(self):
    print('Hello World')

# Una clase abstracta puede tener atributos y métodos normales,
# pero todas las funciones abstractas deben ser implementadas en las clases heredadas.
# Una clase abstracta no puede ser instanciada directamente,
# solo se puede usar como base de otras clases.

class User(MyClass):
  def __init__(self, name, email, age):
    super().__init__(name, email)
    self._age = age
  
  def my_method(self):
    print('My Method')

# # ej 1:
# user1 = User('John Doe', 'john.doe@example.com', 30)

# print('User 1 Name:', user1._name)
# print('User 1 Email:', user1._email)
# print('User 1 Age:', user1._age)

# user1.hello_world()
# user1.my_method()

# # ej 2:
# user2 = User('Jane Doe', 'jane.doe@example.com', 25)

# print('User 2 Name:', user2._name)
# print('User 2 Email:', user2._email)
# print('User 2 Age:', user2._age)

# user2.hello_world()
# user2.my_method()


# Metodos Dunder:
class Servicio:
  # constructor
  def __init__(self, id, servicio):
    self._id = id
    self._servicio = servicio

  # returns a string representation of the object
  def __str__(self):
    return f"ID: {self._id}, Servicio: {self._servicio}"
  
  # returns a string representation of an object
  def __repr__(self):
    return f"Servicio({self._id}, '{self._servicio}')"
  
  # returns a hash value for an object
  def __hash__(self):
    return hash(self._id)
  
  # returns the length
  def __len__(self):
    return len(self._servicio)

  # allows indexing
  def __getitem__(self, key):
    return self._servicio[key]
  
  # aritmeticos
  def __add__(self, other):
    return self._id + other._id
  def __sub__(self, other):
    return self._id - other._id
  def __mul__(self, other):
    return self._id * other._id
  def __div__(self, other):
    return self._id / other._id
  def __mod__(self, other):
    return self._id % other._id
  def __pow__(self, other):
    return self._id ** other._id
  
  
  # comparaciones
  def __eq__(self, other):
    return self._id == other._id
  def __ne__(self, other):
    return self._id != other._id
  def __gt__(self, other):
    return self._id > other._id
  def __lt__(self, other):
    return self._id < other._id
  def __ge__(self, other):
    return self._id >= other._id
  def __le__(self, other):
    return self._id <= other._id
  
  # asignaciones
  def __iadd__(self, other):
    self._id += other._id
    return self._id
  def __isub__(self, other):
    self._id -= other._id
    return self._id
  def __imul__(self, other):
    self._id *= other._id
    return self._id
  def __idiv__(self, other):
    self._id /= other._id
    return self._id
  def __imod__(self, other):
    self._id %= other._id
    return self._id
  def __ipow__(self, other):
    self._id **= other._id
    return self._id

servicio1 = Servicio(1, 'Barberia')
servicio2 = Servicio(2, 'Peluqueria')
servicio3 = Servicio(3, 'Manicurie')

print('Servicio 1:', servicio1)
print('Servicio 2:', servicio2)
print('Servicio 3:', servicio3)

# operaciones entre objetos
suma1y2 = servicio1 + servicio2
mul2y3 = servicio2 * servicio3
resta3y1 = servicio3 - servicio1

print(f'Suma 1 y 2: {suma1y2}') # printa 3 porque al ejecutar __add__ se suman ambos IDs
print(f'Multiplicacion 2 y 3: {mul2y3}') # printa 6 porque al ejecutar __add__ se suman ambos IDs
print(f'Resta 3 y 1: {resta3y1}') # printa 2 porque al ejecutar __add__ se suman ambos IDs