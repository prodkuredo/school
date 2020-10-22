class animal():
    def __init__(self, name, hunger = 0, joy = 50):
        self.hunger = hunger
        self.joy = joy
        
    def feeding(self):
        food = int(input('Сколько еды вы хотите дать? '))
        self.hunger += 20*food
        self.joy += 10*food
        return True

    def walk(self, joyh = 20, hungerh = 30):
        way = int(input('Сколько часов вы xотите гулять? '))
        walk = way * hungerh
        if self.hunger >= walk:
            self.hunger -= walk
            self.joy += joyh*way
            return True
        else:
            self.joy -= joyh*way
            return False

    def care(self):
        self.joy += 20
        return True
    def specs(self):
        print('сытость -', self.hunger, 'счастье -', self.joy)
        
def main():
    name = input('Как зовут питомца? ')
    myanimal = animal(name)
    choise = None
    while choise != '0':
        print('''

            Взаимодействия:
                0 - закончить
                1 - покормить
                2 - пойти гулять
                3 - погладить
                4 - узнать состояние животного

                ''')
        choise = input('Выберите нужное взаимодействие ')
        if choise == '1':
            myanimal.feeding()
            print('Животное покушало')
            myanimal.specs()
        elif choise == '2':
            if myanimal.walk():
                print('Вы пошли гулять')
                myanimal.specs()
            else:
                print('Животное не настолько сыто, чтобы гулять так много :c')
                myanimal.specs()
        elif choise == '3':
            myanimal.care()
            print('Ты погладил зверька')
            myanimal.specs()
        elif choise == '4':
            myanimal.specs()
        elif choise == '0':
            print('Дал зверьку потдохнуть...')

        else:
            print('Такого действия не существует')  
main()

#tut vse maksimalno skuchno, ya prishel domoy pochti v 11 :c