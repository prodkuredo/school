class Car():
    def __init__(self, name, gaz=0):
        self.name = name
        self.gaz = gaz

    def fill(self):
       # self.gaz =  self.gaz + 100
         self.gaz += 100
         return True

    def go(self, gazkm = 10):
        way = int(input('Сколько километров вы хотите проехать: '))
        gaz = way*gazkm
        if self.gaz >= gaz:
            self.gaz -= gaz
            return True
        else:
            return False

    def fuel(self):
        print('уровень топлива: ',self.gaz)
def main():
    name = input('Введите марку машины: ')
    myCar = Car(name)
    choice = None
    while choice != '0':
        print('''

        Автомобиль:
            0 - выйти
            1 - заправить автомобиль
            2 - поехать
            3 - уровень бензина в баке
                
                ''')
        choice = input('Введите команду: ')
        if choice == '1':
            myCar.fill()
            print('Машина заправлена.')
            myCar.fuel()
        elif choice == '2':
            if myCar.go():
                print('Машина поехала.')
                myCar.fuel()
            else:
                print('Машина не поехала. Мало бензина')
        elif  choice == '3':
            myCar.fuel()
        
        elif choice == '0':
            print('Пока!')
            break
        else:
             print('Либо ты учишься читать, либо ...')

main()