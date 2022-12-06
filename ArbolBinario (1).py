
class Nodo():
  #Constructor
  def __init__(self, elemento):
    #atributos
    self.elemento = elemento
    self.punteroderecho = None
    self.punteroizquierdo = None
    #Posición del nodo padre
    self.punteropadre = None

    self.esraiz = False
    self.esderecho = False
    self.esizquierdo = False

    self.altura = 1

  #Función para contar los hijos de un arbol binario
  def ContarHijos(self, raiz):
    x = 0
    if raiz.punteroizquierdo != None:
      x += 1

    if raiz.punteroderecho != None:
      x += 1

    return x


class Arbol():
  #Constructor
  def __init__(self):
    #Atributos
    self.raiz = None
    self.peso = 0

  #Función para saber si el arbol esta vacío
  def GetVacio(self):
    if self.raiz == None:
      return True
    else:
      return False

  #Función para agregar un nodo nuevo
  def AgregarNodo(self, elemento):
    nuevo_nodo = Nodo(elemento)
    #En el caso donde el arbol esta vacío
    if self.GetVacio():
      #El nuevo nodo sera la raíz
      self.raiz = nuevo_nodo
      #este nodo sera el único que tendrá la etiqueta de raíz
      nuevo_nodo.esraiz = True
    else:
      #Los datos que regresa la función Posición sera el nodo padre del nuevo nodo que se quiere agregar
      #Y el lado a la que se va el nodo
      nodo_padre, side = self.Posicion(elemento)
      #En el caso donde se vaya al lado derecho el nodo padre
      if side == "derecho":
        nodo_padre.punteroderecho = nuevo_nodo
        nuevo_nodo.esderecho = True
      #En el caso contrario, se apunta al lado izquierdo

      else:
        nodo_padre.punteroizquierdo = nuevo_nodo
        nuevo_nodo.esizquierdo = True
      #Como es un arbol binario, solo puede haber dos lados a los que se puede ir

      #Al final el puntero del nuevo nodo que se acaba de agregar será igual al nodo padre el mismo
      nuevo_nodo.punteropadre = nodo_padre

    #Aprovechando que agregamos un nuevo nodo sumamos 1 al peso y a la altura del arbol
    self.peso += 1
    nuevo_nodo.altura += 1

  #Función para saber si la posición del elemento
  def Posicion(self, elemento):
    #Vamos a guardar el valor de la raíz en el aux
    aux = self.raiz
    #Side es para guardar hacia donde se va el nodo
    side = None
    #Mientras aux tenga valor va a continuar el while
    while aux:
      #previo va a tener el valor del aux con el que empieza el while
      previo = aux
      #Vamos a comparar si el valor del nodo que se va a agregar es mayor o menor a la raíz
      #En el caso donde sea menor o igual, se irá hacía la izquierda
      if elemento <= aux.elemento:
        aux = aux.punteroizquierdo
        side = "izquierda"
      #Caso contrario se irá hacia la derecha
      else:
        aux = aux.punteroderecho
        side = "derecho"
    #Lo que se va a regresar es el valor previo del aux, que es lo equivalente al nodo padre del nuevo elemento
    #Y el texto que indica si se fué a la derecha o izquierda
    return (previo, side)

  #Función para hacer el recorrido del arbol en "Orden"
  #izquierda - raíz - derecha
  #Como parametro recibe un nodo del arbol
  def ImprimirOrden(self, nodo):
    #Esta función es recursiva
    #Si el nodo que recibe como parámetro existe se hará lo siguiente
    if nodo:
      #Primero se llamará a sí misma la función pero ahora con el nodo hijo que está a la izquierda
      self.ImprimirOrden(nodo.punteroizquierdo)
      #La condición no se cumpla se imprimira el nodo que recibió como parametro
      print(nodo.elemento)
      #Después se llamará la misma función pero ahora con el nodo hijo que estará a la derecha
      self.ImprimirOrden(nodo.punteroderecho)

  #Función para recorrer el arbol en "Pos-orden"
  #izquierda - derecha - raíz
  #Como parámetro recibe un nodo del arbol
  def ImprimirPosOrden(self, nodo):
    #Esta función es recursiva
    #Si existe el nodo se hará lo siguiente
    if nodo:
      #La función se va a llamar así misma con el puntero de cada lado del nodo hasta que la condición no se cumpla
      self.ImprimirPosOrden(nodo.punteroizquierdo)
      self.ImprimirPosOrden(nodo.punteroderecho)
      #Al final de que se termine de hablar cada función se imprimira el valor del nodo que este como parámetro
      print(nodo.elemento)

  #Función para recorrer el arbol en "Pre-orden"
  #raíz - izquierda - derecha
  #Como parámetro recibe un nodo del arból
  def ImprimirPreOrden(self, nodo):
    #Esta función es recursiva
    #Si exise el nodo se hará lo siguiente
    if nodo:
      #Primero se imprimirá el nodo que recibe como parámetro
      print(nodo.elemento)
      #Despues se llamarán la misma función pero ahora con los punteros del nodo
      self.ImprimirPreOrden(nodo.punteroizquierdo)
      self.ImprimirPreOrden(nodo.punteroderecho)

  #Función para busquar elemento en el arbol
  def Busqueda(self, nodo, elemento):
    #En el caso donde el nodo tenga un valor de none, se regresara none como valor
    if nodo == None:
      return None
    #En el caso donde el nodo si tenga un valor como elemento se hará lo siguiente
    else:
      #Si el nodo contiene el valor que estamos buscando se regresará el nodo completo
      if nodo.elemento == elemento:
        return nodo
      #Sino es el nodo que estamos buscando, se comparara el valor buscado si es menor o igual al nodo actual
      elif elemento <= nodo.elemento:
        #Lo que se hará es el puntero izquierda del nodo sera el nuevo nodo y el elemento es el mismo que estamos buscando
        #Es recursiva
        return self.Busqueda(nodo.punteroizquierdo, elemento)
      else:
        #En el otro caso es la misma dinámica pero con el puntero derecho
        #Es recursiva
        return self.Busqueda(nodo.punteroderecho, elemento)

  #Función para eliminar un nodo del arbol
  def EliminarNodo(self, elemento):
    #Primero hay que evaluar si existe un arbol como primer caso
    if self.GetVacio():
      #En el caso donde el arbol este vacío se regresará el siguiente mensaje
      print("El arbol esta vacío")
    #En el caso donde si exista un arbol deberemos buscar el elemento en el arbol usando la función de busqueda
    nodo_borrar = self.Busqueda(self.raiz, elemento)
    #Una vez encontrado el elemento a eliminar hay que evaluar múltiples casos que pueden existir antes de eliminarlo
    #En el caso donde el nodo no exista se regresara el siguiente mensaje
    if nodo_borrar == None:
      print("El elemento no existe")
    #En el caso donde si exista el elemento se evaluara las siguientres condiciones
    else:
      #En el caso donde el nodo a eliminar sea la raíz, en otras palabras sea el único elemento, simplemente se le otorgara el valor de none
      #Esto porque si el valor del peso del arbol es 1, significa que el arbol solo tiene un elemento
      if self.peso == 1:
        self.raiz = None

      #Para las siguientes condiciones necesitaremos la función de contar hijos de un nodo para evaluar las siguientes condiciones
      #Se guardara en una variable aparte para poder usarla más comodamente
      numerohijos = nodo_borrar.ContarHijos(nodo_borrar)
      #Solo puede haber 3 casos, que el nodo no tenga hijos, que tenga un solo hijo y que tenga 2 hijos, esto porque es un arbol binario

      #En el caso donde el nodo a borrar no tenga hijos se hara lo siguiente
      if numerohijos == 0:
        #Primer tenemos que ver si el nodo a borrar es izquierdo o derecho, esto porque al ser arbol binario un padre puede tener dos nodos
        #En el caso donde sea el izquierdo vamos a borrar el puntero del padre que este apuntando al izquiedo, osea asignarle un valor de none
        #Por si acaso eliminamos el nodo a borrar asignandole el valor de none
        if nodo_borrar.esizquierdo:
          nodo_borrar.punteropadre.punteroizquierdo = None
          nodo_borrar = None
        #Es exactamente el mismo procedimiento con el derecho, solo que ahora con el puntero derecho
        else:
          nodo_borrar.punteropadre.punteroderecho = None
          nodo_borrar = None

      #En el caso donde sea un solo hijo vamos a usar las mismas condiciones pero agregando 4 condiciones más
      if numerohijos == 1:
        if nodo_borrar.esraiz:  # si el nodo borrar es raiz
          if nodo_borrar.punteroizquierdo:  # si el nodo borrar
            nodo_borrar.punteroizquierdo.punteropadre = None  # el padre del nodo borrar del puntero izquierdo sera igual a None
            nodo_borrar.punteroizquierdo.esraiz = True  #  la raiz del nodo borrar puntero izquierdo va a ser igual a verdadero
            nodo_borrar.punteroizquierdo.esizquierdo = False  #el punteroizquierdo del nodo borrar es igual a falso
            self.raiz = nodo_borrar.punteroizquierdo  # la raiz es igual al puntero izquierdo del nodo borrar
          else:  # si no , lo mismo pero con el lado derecho
            nodo_borrar.punteroderecho.punteropadre = None
            nodo_borrar.punteroderecho.esraiz = True
            nodo_borrar.punteroderecho.esderecho = False
            self.raiz = nodo_borrar.punteroderecho
        else:
          #Evaluamos si el nodo a borrar esta a la izquieda
          if nodo_borrar.esizquierdo:
            #En este caso debemos evaluar si el hijo del nodo a borrar esta a la izquierda o derecha para eso son las dos condiciones
            #Cuando sepamos de que lado esta el hijo se lo asignaremos al padre del nodo a borrar
            if nodo_borrar.punteroizquierdo:
              nodo_borrar.punteropadre.punteroizquierdo = nodo_borrar.punteroizquierdo
              nodo_borrar.punteropadre.punteroizquierdo.punteropadre = nodo_borrar.punteropadre

            else:
              nodo_borrar.punteropadre.punteroizquierdo = nodo_borrar.punteroderecho
              nodo_borrar.punteropadre.punteroizquierdo.punteropadre = nodo_borrar.punteropadre
            ##Después le asignaremos si es el izquierdo o derecho sea el caso
            nodo_borrar.punteropadre.punteroizquierdo.esizquierdo = True
            nodo_borrar.punteropadre.punteroizquierdo.esderecho = False

          #Mismo procedimiento pero con el lado derecho
          else:
            if nodo_borrar.punteroizquierdo:
              nodo_borrar.punteropadre.punteroderecho = nodo_borrar.punteroizquierdo
              nodo_borrar.punteropadre.punteroderecho.punteropadre = nodo_borrar.punteropadre

            else:
              nodo_borrar.punteropadre.punteroderecho = nodo_borrar.punteroderecho
              nodo_borrar.punteropadre.punteroderecho.punteropadre = nodo_borrar.punteropadre

            nodo_borrar.punteropadre.punteroderecho.esizquierdo = False
            nodo_borrar.punteropadre.punteroderecho.esderecho = True
          #Al final de todo borraremos el dato borrado
          nodo_borrar = None
      #Al final de la función se restara 1 al peso porque se elimino un elemento

    #En el caso donde tengamos dos hijos se hará lo siguiente
    if numerohijos == 2:
      sucesor = self.Sucesor(nodo_borrar)

      #En el caso que se va a borrar la raíz hay que hacer lo siguiente
      if nodo_borrar.esraiz:
        #Si el sucesor es izquierdo se va a hacer lo siguiente
        if sucesor.esizquierdo:
          #Asignamos el puntero derecho del sucesor con el nodo que tenia el nodo que queremos borrar a la derecha
          sucesor.punteroderecho = nodo_borrar.punteroderecho
          #El valor que tenía el valor
          sucesor.punteropadre = None  # El puntero padre del sucesor sera igual a None
          sucesor.esizquierdo = False  # el sucesor no es izquierdo
          sucesor.esderecho = False
          sucesor.esraiz = True  # ese sucesor ahora sera raiz del arbol
          self.raiz = sucesor  # la raiz del arbol es el sucesor
          nodo_borrar.punteroderecho.punteropadre = sucesor  # el puntero padre del puntero  derecho del nodo borrar es igual al sucesor
          nodo_borrar.punteroderecho = nodo_borrar.punteroizquierdo = None  # el nodo borrar izquierdo y derecho son igual a None
          nodo_borrar = None  # nodo borrar es igual a None
        else:  # Si no
          self.raiz = sucesor  #  la raiz del arbol es el sucesor
          if sucesor.punteroizquierdo != None:  # si el puntero izquierdo del sucesor es diferente a none
            sucesor.punteropadre.punteroderecho = sucesor.punteroizquierdo  # el puntero derecho del puntero padre del sucesor es igual al puntero izquierdo del sucesor
            sucesor.punteroizquierdo.punteropadre = sucesor.punteropadre  # el puntero padre del puntero izquierdo del sucesor es igual al sucesor puntero padre
            sucesor.punteroderecha = nodo_borrar.punteroderecha  # el puntero derecho del sucesor es igual al puntero ziquierod del nodo borrar
            sucesor.punteroizquierda = nodo_borrar.punteroizquierdo  # el puntero izquierdo del sucesor es igual al puntero izquierdo del nodo borrar
            sucesor.esderecho = False  # el sucesor no es derecho
            sucesor.esizquierdo = False
            sucesor.esraiz = True  # el sucesor es raiz
            nodo_borrar.punteroderecho.punteropadre = sucesor  # el  puntero padre del puntero derecho del nodo borrar es igual al sucesor
            nodo_borrar.punteroizquierdo.punteropadre = sucesor  # el puntero padre del puntero izquierdo del nodo borrar es igual al sucesor
            sucesor.punteroizquierdo.esizquierdo = False  # el puntero izquierdo del sucesor no es izquierdo
            sucesor.punteroizquierdo.esderecho = True  #  el puntero izquierdo del sucesor es derecho
            nodo_borrar.punteroderecho = nodo_borrar.punteroizquierdo = None  # el puntero derecho y izquierdo del nodo borrar es igual a none
            nodo_borrar = None  # el nodo borrar es igual a none

          else:  # si no
            sucesor.punteroderecho = nodo_borrar.punteroderecho  # el puntero derecho del sucesor es igual al puntero derecho del nodo borrar
            sucesor.punteroizquierdo = nodo_borrar.punteroizquierdo  # el puntero izquierdo del sucesor es igual al puntero izquierdo del nodo borrar
            sucesor.esderecho = False  # el sucesor no es derecho
            sucesor.esraiz = True  #el sucesor es raiz
            nodo_borrar.punteroderecho.punteropadre = sucesor  # el puntero derecho del nodo borrar, su papa va a ser el sucesor ahora
            nodo_borrar.punteroizquierdo.punteropadre = sucesor  # el puntero izquierdo  del nodo borrar, su papa va a ser el sucesor ahora

            nodo_borrar.punteroderecho = nodo_borrar.punteroizquierdo = None  # el puntero derecho y izquierdo del nodo borrar es igual a none
            sucesor.punteropadre.punteroderecho = None  # El puntero derecho del sucesor puntero padre es igual a none

            nodo_borrar = None  # el nodo borrar es igual None

      else:  # si no
        if sucesor.esderecho == True:  # si el sucesor es derecho
          if sucesor.punteroizquierdo != None:  # si el puntero izquierdo del sucesor es diferente a none
            sucesor.punteropadre.punteroderecho = sucesor.punteroizquierdo  # el puntero derecho del padre del sucesor es igual al puntero izquierdo del sucesor
            sucesor.punteroizquierdo.punteropadre = sucesor.punteropadre  # el puntero padre del puntero izquierdo del sucesor es igual al puntero padre del sucesor
            sucesor.punteroderecho = nodo_borrar.punteroderecho  #el puntero derecho del sucesor es igual al puntero derecho del nodo borrar
            sucesor.punteroizquierdo = nodo_borrar.punteroizquierdo  # el punteor izquierdo del sucesor es igual al punteroizquierdo del nodo borrar

            if nodo_borrar.esderecho == True:  # si el nodo borrar es derecho
              nodo_borrar.punteropadre.punteroderecho = sucesor  # el puntero derecho del puntero padre del nodo borrar es igual al sucesor
              sucesor.punteropadre = nodo_borrar.punteropadre  # puntero padre del sucesor es igual al puntero padre del nodo borrar
              sucesor.esderecho = True  #  el sucesor es derecho
              sucesor.esizquierdo = False  # el sucesor no es izquierdo
            else:
              nodo_borrar.punteropadre.punteroizquierdo = sucesor  # el puntero izquierdo del puntero padre del nodo borrar es igual al sucesor
              sucesor.punteropadre = nodo_borrar.punteropadre  #el puntero padre del sucesor es igual al puntero padre del nodo borrar
              sucesor.esderecho = False  # el sucesor no es derecho
              sucesor.esizquierdo = True  # es sucesor es izquierdo
          else:
            sucesor.punteropadre = None  # el puntero padre del sucesor es igual a none
            if sucesor.esizquierdo:
                sucesor.punteroderecho = nodo_borrar.punteroderecho
              # el puntero derecho del sucesor es igual al puntero derecho del nodo borrar
            else:
                sucesor.punteroizquierdo = nodo_borrar.punteroizquierdo  #el puntero izquierdo del sucesor = puntero izquierdo del nodo borrar
                sucesor.punteroderecho = nodo_borrar.punteroderecho
            if nodo_borrar.esderecho:  # si el nodo borrar es derecho
              nodo_borrar.punteropadre.punteroderecho = sucesor  # el puntero derecho del puntero padre del nodo borrar es igual al sucesor
              sucesor.punteropadre = nodo_borrar.punteropadre  # el puntero padre del sucesor es igual al puntero padre del nodo borrar
              sucesor.esderecho = True  # el sucesor es derecho
              sucesor.esizquierdo = False  # el sucesor no es izquierdo
            else:
              nodo_borrar.punteropadre.punteroizquierdo = sucesor  # el puntero izquierdo dle punteor padre del nodo borrar es igual al sucesor
              sucesor.punteropadre = nodo_borrar.punteropadre  # el puntero padre del sucesor es igual al puntero padre del nodo borrar
              sucesor.esderecho = False  # el sucesor no es derecho
              sucesor.esizquierdo = True  # el sucesor es izquierdp
          nodo_borrar = None  #el nodo borrar es igual a none
          #nodo_borrar.punteroderecho = nodo_borrar.punteroizquierdo = None

        else:
            
            if sucesor.esizquierdo:
                sucesor.punteroderecho = nodo_borrar.punteroderecho
                
              # el puntero derecho del sucesor es igual al puntero derecho del nodo borrar
            else:
                sucesor.punteroizquierdo = nodo_borrar.punteroizquierdo  #el puntero izquierdo del sucesor = puntero izquierdo del nodo borrar
                sucesor.punteroderecho = nodo_borrar.punteroderecho
            #sucesor.punteroderecho = nodo_borrar.punteroderecho  # el puntero derecho del sucesor es igual al puntero derecho del nodo borrar
        
            if nodo_borrar.esderecho == True:  # si el nodo borrar es derecho
                nodo_borrar.punteropadre.punteroderecho = sucesor  # el puntero derecho del puntero padre del nodo borrar es igual al sucesor
                sucesor.punteropadre = nodo_borrar.punteropadre  # el puntero padre del sucesor es igual al puntero padre del nodo borrar
                sucesor.esderecho = True  # el sucesor es derecho
                sucesor.esizquierdo = False  # el sucesor no es izquierdo
            else:
                
                nodo_borrar.punteropadre.punteroizquierdo = sucesor  # el puntero izquierdo del puntero padre del nodo borrar es igual al sucesor
                sucesor.punteroderecho.punteropadre = sucesor
                sucesor.punteropadre = nodo_borrar.punteropadre  # el puntero padre del sucesor es igual al puntero padre del nodo borrar
                sucesor.esderecho = False  # el sucesor no es derecho
                sucesor.esizquierdo = True  # el sucesor es izquierdo
            nodo_borrar.punteroderecho = nodo_borrar.punteroizquierdo = None
            nodo_borrar = None  #el nodo borrar es igual a none
          
    self.peso -= 1  # se le resta 1 al peso

  #Función para encotrar el sucesor
  def Sucesor(self, nodo_borrar):

    valor_borrar = nodo_borrar  # el valor borrar es igual al nodo que queremos borrar
    nodo_hijo = valor_borrar.punteroizquierdo  # el nodo hijo es igual al puntero izquierdo del valor a borrar

    while nodo_hijo != None:  # mientras que el nodo hijo sea diferente a none
      valor_borrar = nodo_hijo  # valor borrar es igual al nodo hijo
      nodo_hijo = nodo_hijo.punteroderecho  # nodo hijo es igual al puntero derecho del nodo hijo

    return valor_borrar

  def printTree(self, node, level=0):
      #En el caso donde el nodo exista
      if node != None:
          #Se va a llamar la función pero ahora con el puntero derecho y se le va a sumar 1 al level
          self.printTree(node.punteroderecho, level + 1)
          #El level es el piso del arbol horizontal, y se imprime el nodo actual
          print(' ' * 4 * level , '-> ' , node.elemento)
          #Se va a llamar la funcion pero ahiora con el puntero izquierdo e igual se le va a suamr 1 al level
          self.printTree(node.punteroizquierdo, level + 1)
  
  def __str__(self):
    self.printTree(self.raiz)
    return ""

#Inicio
Arbolito = Arbol()
#Agregamos los elementos
Arbolito.AgregarNodo(10)
Arbolito.AgregarNodo(6)
Arbolito.AgregarNodo(15)
Arbolito.AgregarNodo(4)
Arbolito.AgregarNodo(7)
Arbolito.AgregarNodo(13)
Arbolito.AgregarNodo(18)
Arbolito.AgregarNodo(3)
Arbolito.AgregarNodo(12)
Arbolito.AgregarNodo(17)
Arbolito.AgregarNodo(19)
Arbolito.AgregarNodo(21)
Arbolito.EliminarNodo(21)
Arbolito.EliminarNodo(13)
Arbolito.EliminarNodo(6)
Arbolito.EliminarNodo(10)


print("Arbol original: \n")
#Arbolito.ImprimirOrden(Arbolito.raiz)
#Arbolito.ImprimirPosOrden(Arbolito.raiz)
print(Arbolito)

Arbolito.ImprimirPosOrden(Arbolito.raiz)
