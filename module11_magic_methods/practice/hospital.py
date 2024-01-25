from datetime import datetime
from collections import UserList, deque

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class NoRight(Exception):    
    pass

class Desiese:
    def __init__(self, name, doctor):
        self.name = name
        self.doctor = doctor
        self.treatment = list()
        self.time = datetime.now()
        self.cured = False
        self.cure_time = None

    def cure(self):
        self.cured = True
        self.cure_time = datetime.now()

    def treat(self, treatment):
        self.treatment.append(treatment)

class Story(UserList):
    story_size = 10

    def __init__(self):
        self.__data = deque([], self.story_size)
        self.__data__dict = dict()
        self.data = list()


    def __getitem__(self, key=None):
        if key is None:
            return list(self.__data)
        if isinstance(key, int):
            return self.__data[key]
        elif isinstance(key, str):
            return self.__data__dict.get(key)
        
    def __len__(self):
        return len(self.__data)
    
    def add(self, *_):
        raise NoRight
    
    def __add(self, disease):
        self.__data.append(disease)
        self.__data__dict = {des.name: des for des in self.__data}
        self.data = [des from des in self.__data]

    @property
    def healthy(self):
        return all([disease.cured for disease in self.__data])
    

class Patient(Person):
    def __init__(self, name, surname, polis):
        super().__init__(name, surname)
        self.polis = polis
        self.story = Story()

    @property
    def healthy(self):
        return self.story.healthy
    

class Doctor(Person):
    def __init__(self, name, surname, position):
        super().__init__(name, surname)
        self.position = position

    def add(self, patient, disease_name):
        des = Desiese(disease_name, ' '.join((self.name, self.surname)))
        patient.story._Story__add(des)


    def treat(self, patient, disease_name, treatment):
        patient.story[disease_name].treat(treatment)


# TODO add checks
    
    


