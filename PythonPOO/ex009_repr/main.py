# Funções decoradoras e decoradores com classes
class myRepr:
    def __repr__(self):
        class_name = self.__class__.__name__                                                                           
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

class Time:
     
    def __init__(self, nome):
        self.nome = nome

    __repr__ = myRepr.__repr__
    
 


class Planeta:
    def __init__(self, nome):
        self.nome = nome
        self._repr = myRepr()
    def __repr__(self):
        self._repr.nome = self.nome
        return self._repr.__repr__()
brasil = Time('Brasil')
portugal = Time('Portugal')
argentina = Time('Argentina')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)
