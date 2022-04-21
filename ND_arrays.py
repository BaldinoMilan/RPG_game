from random import randint

# Classe Nd_array(fonctionne comme un dictionnaire)
class Nd_array(dict):
    def __init__(self, shape, dtype=int) -> None:
        self.shape = shape
        self.dtype = dtype
        self = {}
        
    def ones(self): # rempli la matrice de uns
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self[i, j] = 1
    
    def zeros(self): # rempli la matrice de zeros
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self[i, j] = 0

    def instore(self, constant): # rempli la matrice par une constante
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self[i, j] = constant
    
    def randin(self, a=0, b=9): # rempli la matrice d'entiers aléatoires
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self[i, j] = randint(a, b)
    
    def binary(self): # rempli la matrice de zeros et uns
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self[i, j] = randint(0, 1)

    def arrange(self, axis=0, start=1, reverse=False): # rempli la matrice d'entiers consécutifs (point de départ défini)
        if reverse == False:
            bounty = start
            if axis == 0:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self[i, j] = bounty
                        bounty += 1
            elif axis == 1:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self[j, i] = bounty
                        bounty += 1
            else:
                raise TypeError("Axis argument must be one or zero.")
        
        elif reverse == True:
            bounty = start - 1
            if axis == 0:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self[i, j] = self.shape[0]*self.shape[1] - bounty
                        bounty += 1
            
            elif axis == 1:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self[j, i] = self.shape[0]*self.shape[1] - bounty
                        bounty += 1
            
            else:
                raise TypeError("Axis Argument must be one or zero.")
    
    def fit(self): # génere la liste à partir du dict
        array_list = []
        for i in range(self.shape[0]):
            array_axis0 = []
            for k in range(self.shape[1]):
                array_axis0.append(self[i, k])
            array_list.append(array_axis0)
        self.list = array_list
        
    def __str__(self):  # texte (print())
        self.fit()
        string = f"Nd_array({self.list[0]}\n"
        for i in range(self.shape[0] - 1):
            string += f"         {self.list[i+1]}\n"
        return string

    def __repr__(self) -> str: # représentation dans la console
        self.config()
        return f"Nd_array(object_:{self.config['object_']}, shape_:{self.config['shape_']}, dtype_:{self.config['dtype_']}\nlooklike_:{self.config['array_'][0]})"

    def config(self): # configuration (dict)
        self.fit()
        self.config = {'object_': Nd_array, 'shape_': self.shape, 'dtype_': self.dtype, 'array_': self.list}
        return self.config

    def __add__(self, other): # addition d'une constante à une matrice
        if isinstance(other, int):
            self2 = Nd_array(self.shape, dtype=int)
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    self2[i, k] = other + self[i, k]
            self2.fit()
            return self2

        elif isinstance(other, float): 
            self2 = Nd_array(self.shape, dtype=float)
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    self2[i, k] = other + self[i, k]
                    self2.fit()
                    return self2  
        
        elif isinstance(other, Nd_array):
            if self.shape[0] >= other.shape[0] and self.shape[1] >= other.shape[1]:
                
                array = Nd_array((self.shape[0], self.shape[1]), dtype=self.dtype)
                for i in range(self.shape[0]):
                    
                    for k in range(self.shape[1]):
                        
                        if k >= other.shape[1] or i >= other.shape[0]:
                            array[i, k] = self[i, k]    
                        
                        else:    
                            array[i, k] = self[i, k] + other[i, k]

                return array
                
            elif self.shape[0] <= other.shape[0] and self.shape[1] <= other.shape[1]:
                
                array = Nd_array((other.shape[0], other.shape[1]), dtype=self.dtype)
                for i in range(other.shape[0]):
                    
                    for k in range(other.shape[1]):
                        
                        if k >= self.shape[1] or i >= self.shape[0]:
                            array[i, k] = other[i, k]    
                        
                        else:    
                            array[i, k] = self[i, k] + other[i, k]

                return array
            
            else:
                raise TypeError("One over two array have to bigger or equal in its two dimensions.")
        else:
            raise TypeError("Operant must be integer or float (you can also add two arrays).")
        
    def __sub__(self, other): # même chose pour la soustraction
        if isinstance(other, int):
            self2 = Nd_array(self.shape, dtype=int)
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    self2[i, k] = self[i, k] - other
            self2.fit()
            return self2

        elif isinstance(other, float):
            self2 = Nd_array(self.shape, dtype=float)
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    self2[i, k] = self[i, k] - other
                    self2.fit()
                    return self2
        
        elif isinstance(other, Nd_array):
            if self.shape[0] >= other.shape[0] and self.shape[1] >= other.shape[1]:
                
                array = Nd_array((self.shape[0], self.shape[1]), dtype=self.dtype)
                for i in range(self.shape[0]):
                    
                    for k in range(self.shape[1]):
                        
                        if k >= other.shape[1] or i >= other.shape[0]:
                            array[i, k] = self[i, k]    
                        
                        else:    
                            array[i, k] = self[i, k] - other[i, k]

                return array
                
            elif self.shape[0] <= other.shape[0] and self.shape[1] <= other.shape[1]:
                
                array = Nd_array((other.shape[0], other.shape[1]), dtype=self.dtype)
                for i in range(other.shape[0]):
                    
                    for k in range(other.shape[1]):
                        
                        if k >= self.shape[1] or i >= self.shape[0]:
                            array[i, k] = - other[i, k]    
                        
                        else:    
                            array[i, k] = self[i, k] - other[i, k]

                return array
            
            else:
                raise TypeError("One over two array have to be bigger or equal in its two dimensions.")
        else:
            raise TypeError("Operant must be integer or float (you can also soustract twoo arrays).")

    def __mul__(self, other): # même chose pour multiplication
        if isinstance(other, int):
            self2 = Nd_array(self.shape, dtype=int)
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    self2[i, k] = self[i, k] * other
            self2.fit()
            return self2

        elif isinstance(other, float):
            self2 = Nd_array(self.shape, dtype=float)
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    self2[i, k] = self[i, k] * other
                    self2.fit()
                    return self2
        
        elif isinstance(other, Nd_array):
            if self.shape[0] >= other.shape[0] and self.shape[1] >= other.shape[1]:
                
                array = Nd_array((self.shape[0], self.shape[1]), dtype=self.dtype)
                for i in range(self.shape[0]):
                    
                    for k in range(self.shape[1]):
                        
                        if k >= other.shape[1] or i >= other.shape[0]:
                            array[i, k] = self[i, k]    
                        
                        else:    
                            array[i, k] = self[i, k] * other[i, k]

                return array
                
            elif self.shape[0] <= other.shape[0] and self.shape[1] <= other.shape[1]:
                
                array = Nd_array((other.shape[0], other.shape[1]), dtype=self.dtype)
                for i in range(other.shape[0]):
                    
                    for k in range(other.shape[1]):
                        
                        if k >= self.shape[1] or i >= self.shape[0]:
                            array[i, k] = other[i, k]    
                        
                        else:    
                            array[i, k] = self[i, k] * other[i, k]

                return array
            
            else:
                raise TypeError("One over two array must be larger or equal in its to dimensions.")
        else:
            raise TypeError("Operant must be integer or float (you can also multiply two arrays).")
    
    def __pow__(self, other):
        if isinstance(other, int):
            self2 = Nd_array(self.shape, dtype=int)
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    self2[i, k] = self[i, k] ** other
            self2.fit()
            return self2

        elif isinstance(other, float):
            self2 = Nd_array(self.shape, dtype=float)
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    self2[i, k] = self[i, k] ** other
            self2.fit()
            return self2
        
        else:
            raise TypeError("Operant must be integer or float")
    
    def reshape(self, reshape): # redimensionne la matrice (garde le même nombre de valeurs)
        if self.shape[0] * self.shape[1] == reshape[0] * reshape[1]:
            self.fit()
            value = []
            for i in self.list:
                for u in i:
                    value.append(u)
            self.shape = reshape
            count = 0
            for k in range(reshape[0]):
                for m in range(reshape[1]):
                    self[k, m] = value[count]
                    count += 1
            self.fit()
        else:
            raise TypeError("New shape must contain the same place as before")

    def in_put(self, listarray): # valeurs entrées à la main dans une liste
        count = 0
        for u in listarray:
            for i in u:
                count += 1

        if len(listarray) == self.shape[0]:
            if (count / self.shape[0]) == self.shape[1]:
                for i in range(self.shape[0]):
                    for k in range(self.shape[1]):
                        self[i, k] = listarray[i][k]
                
                self.fit()

            else:
                raise TypeError("your input must respect the initial shape")    
        
        else:
            raise TypeError("your input must respect the initial shape")

    def flatten(self): # redimensionne le tableau sur une ligne
        self.reshape((1, self.shape[1] * self.shape[0]))

    def T(self, axis=None): # transposée d'une matrice
        if axis == None:
            if self.shape[1] > self.shape[0]:
                array = Nd_array((self.shape[1], self.shape[0]), dtype=self.dtype)
                self.fit()
                for i in range(self.shape[1]):
                    for k in range(self.shape[0]):
                        array[i, k] = self[k, i]
            
            else:
                array = Nd_array((self.shape[1], self.shape[0]), dtype=self.dtype)
                self.fit()
                listarray = []

                for i in range(self.shape[1]):
                    for k in range(self.shape[0]):
                        listarray.append(self[k, i])
                count = 0
                for i in range(array.shape[1]):
                    for k in range(array.shape[0]):
                        array[k, i] = listarray[count]
                        count += 1
        
        elif axis == 0:        
            array = Nd_array((self.shape[1], self.shape[0]), dtype=self.dtype)
            self.fit()
            for i in range(self.shape[1]):
                for k in range(self.shape[0]):
                    array[i, k] = self[k, i]
        
        elif axis == 1:
            array = Nd_array((self.shape[1], self.shape[0]), dtype=self.dtype)
            self.fit()
            listarray = []
            for i in range(self.shape[1]):
                for k in range(self.shape[0]):
                    listarray.append(self[k, i])
            count = 0
            for i in range(array.shape[1]):
                for k in range(array.shape[0]):
                    array[k, i] = listarray[count]
                    count += 1
            
        return array

    def sum_(self, axis=None):
        if axis == None:
            array_axisnone = Nd_array((1, 1), dtype=self.dtype)
            total = 0
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    total += self[i, k]
            array_axisnone[0, 0] = total
            return array_axisnone
        
        elif axis == 1:
            
            total =  0
            array_axis1 = Nd_array((self.shape[0], 1), dtype=self.dtype)
            for i in range(self.shape[0]):
                total = 0
                for k in range(self.shape[1]):
                    total += self[i, k]
                array_axis1[i, 0] = total

            return array_axis1

        elif axis == 0:

            total = 0
            array_axis0 = Nd_array((1, self.shape[1]), dtype=self.dtype)
            for k in range(self.shape[1]):
                total = 0
                for i in range(self.shape[0]):
                    total += self[i, k]
                array_axis0[0, k] = total
            
            return array_axis0

    def mean(self, axis=None):
        if axis == None:
                    array_axisnone = Nd_array((1, 1), dtype=self.dtype)
                    total = 0
                    for i in range(self.shape[0]):
                        for k in range(self.shape[1]):
                            total += self[i, k]
                    array_axisnone[0, 0] = total / (self.shape[0] * self.shape[1])
                    return array_axisnone
                
        elif axis == 1:
            
            total =  0
            array_axis1 = Nd_array((self.shape[0], 1), dtype=self.dtype)
            for i in range(self.shape[0]):
                total = 0
                for k in range(self.shape[1]):
                    total += self[i, k]
                array_axis1[i, 0] = total / self.shape[1]

            return array_axis1

        elif axis == 0:

            total = 0
            array_axis0 = Nd_array((1, self.shape[1]), dtype=self.dtype)
            for k in range(self.shape[1]):
                total = 0
                for i in range(self.shape[0]):
                    total += self[i, k]
                array_axis0[0, k] = total / self.shape[0]
            
            return array_axis0

    def dot(self, matrice):
        if isinstance(matrice, Nd_array):
            if matrice.shape[0] == self.shape[1]:
                array = Nd_array((self.shape[0], matrice.shape[1]))
                
                for i in range(array.shape[0]):
                    for k in range(array.shape[1]):
                        
                        if i < matrice.shape[0] and k < matrice.shape[1]:
                    
                            if i < self.shape[0] and k < self.shape[1]:
                                array[i, k] = self[i, k] * matrice[i, k]
                            
                            else:
                                array[i, k] = matrice[i, k]

                        else:
                            if i < self.shape[0] and k < self.shape[1]:
                                array[i, k] = self[i, k]
                            
                            else:
                                array[i, k] = 1

                return array
            
            elif matrice.shape[1] == self.shape[0]:
                
                array = Nd_array((matrice.shape[0], self.shape[1]))
                
                for i in range(array.shape[0]):
                    for k in range(array.shape[1]):
                        
                        if i < matrice.shape[0] and k < matrice.shape[1]:
                    
                            if i < self.shape[0] and k < self.shape[1]:
                                array[i, k] = self[i, k] * matrice[i, k]
                            
                            else:
                                array[i, k] = matrice[i, k]

                        else:
                            if i < self.shape[0] and k < self.shape[1]:
                                array[i, k] = self[i, k]
                            
                            else:
                                array[i, k] = 1
                return array
            else:
                TypeError("Both arrays must have a commun dimension")
        else:
            raise TypeError("Function argument must be an object from the class Nd_array")
    
    def insert(self, value, shape = None):
        if shape == None:
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    self[i, k] = value

        elif isinstance(shape, tuple):
            for i in range(shape[0]):
                for k in range(shape[1]):
                    self[i, k] = value

        else:
            raise TypeError(f"Chosen shape must be a tuple with 2 arguments")
    def replace(self, base_value, new_value, shape = None):
        if shape == None:
            for i in range(self.shape[0]):
                for k in range(self.shape[1]):
                    if self[i, k] == base_value:  
                        self[i, k] = new_value
                    else:
                        pass

        elif isinstance(shape, tuple):
            for i in range(shape[0]):
                for k in range(shape[1]):
                    if self[i, k] == base_value:
                        self[i, k] = new_value
                    else:
                        pass
        else:
            raise TypeError(f"Chosen shape must be a tuple with 2 arguments")

def hstack(ndarray1, ndarray2): # rassemble horizontalement les deux matrices -> nd_array(())
    if isinstance(ndarray1, Nd_array) and isinstance(ndarray2, Nd_array):
        
        if ndarray1.shape[0] == ndarray2.shape[0]:
            
            finalarray = Nd_array((ndarray1.shape[0], ndarray1.shape[1] + ndarray2.shape[1]), dtype=ndarray1.dtype)
            finalarray.update(ndarray1)
            
            for i in range(ndarray1.shape[0]):
                
                for k in range(ndarray2.shape[1]):
                    finalarray[i, ndarray1.shape[1] + k] = ndarray2[i, k]
            
            return finalarray
        else:
            TypeError("Both array must have the same number of rows")
    else:
        raise TypeError("Function argument must be an array")

def vstack(ndarray1, ndarray2): # rassemble verticalement les deux matrices -> nd_array(())
    if isinstance(ndarray1, Nd_array) and isinstance(ndarray2, Nd_array):
        
        if ndarray1.shape[1] == ndarray2.shape[1]:
            
            finalarray = Nd_array((ndarray1.shape[0] + ndarray2.shape[0], ndarray1.shape[1]), dtype=ndarray1.dtype)
            finalarray.update(ndarray1)
            
            for i in range(ndarray2.shape[0]):
                
                for k in range(ndarray1.shape[1]):
                    finalarray[ndarray1.shape[0] + i, k] = ndarray2[i, k]
            
            return finalarray
        else:
            raise TypeError("Both array must have the same number of columns")
    else:
        raise TypeError("Function argument must be an array")
