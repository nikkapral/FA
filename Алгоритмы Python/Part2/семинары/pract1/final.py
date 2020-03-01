from random import randint
from faker import Faker
from time import sleep

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class CockroachClass():
    """
    Класс таракан
    """
    def __init__(self, name):
        self.name = name
        self.current_location = 0
        self.__speed_generator()

    def movement_changer(self):
        self.movement = bool(randint(0,1))
        #Если было перемещение
        if self.movement:
            self.current_location += self.speed
    
    def __speed_generator(self):
        #Генерация скорости
        self.speed = randint(1,10) #TODO 


class GamerClass():
    pass


class MainClass():
    
    def __init__(self):
        
        self.COCKROACH_ICON = "🐞"
        self.GRASS_ICON = "_"
        self.COCKROACH_COUNT = 4
        self.ITERATIONS_COUNT = 100
        #Хранит объекты тараканов
        self.cockroach_list = []
        fake = Faker(['ru_RU'])

        #Начальная матрица
        self.start_matrix_generator()
        #Генерируем тараканов
        for i in range(self.COCKROACH_COUNT):
            cockroach_obj = CockroachClass(fake.word())
            self.cockroach_list.append(cockroach_obj)
    
        for current_iteration in range(self.ITERATIONS_COUNT):

            self.drawer()
            sleep(1)
            try:
                self.cockroach_changer()

            #Если допрыгались до IndexError
            except IndexError:
                self.winner_detector()
                break

    def winner_detector(self):
        """
        Метод, определяющий то, какой таракан выиграл
        """
        print("winner_detector погнал")
        winner = sorted(self.cockroach_list,key=lambda e: e.current_location,reverse=True)[0]
        print("Победитель: {}".format(winner.name))
            

    def start_matrix_generator(self):
        """
        Метод генерации начальной матрицы
        """
        #Начальная матрица
        self.matrix = [[self.GRASS_ICON for c in range(self.ITERATIONS_COUNT)] for r in range(self.COCKROACH_COUNT)]
        for i in range(len(self.matrix)):
            self.matrix[i][0] = self.COCKROACH_ICON

        
    def cockroach_changer(self):
        """
        Осуществление перемещения таракана
        """
        self.matrix = [[self.GRASS_ICON for c in range(self.ITERATIONS_COUNT)] for r in range(self.COCKROACH_COUNT)]
        
        for i in range(len(self.cockroach_list)):
            
            cockroach = self.cockroach_list[i]
            cockroach.movement_changer()
            print("[Таракан "+str(cockroach.name)+"] находится на "+str(cockroach.current_location)+", перемещение: "+str(cockroach.movement))
            self.matrix[i][cockroach.current_location] = self.COCKROACH_ICON


    def drawer(self):
        """
        Отображение на экран
        """
        print("Забег:\n")
        for i in range(len(self.matrix)):
            print(i+1, end=" ")
            for j in range(len(self.matrix[i])):
                print('{}'.format(self.matrix[i][j]), end=" ")
            print("|   Таракан '{}'".format(self.cockroach_list[i].name))

        
if __name__ == "__main__":
    obj = MainClass()