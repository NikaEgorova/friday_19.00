from random import randint
 
class Hero():
    def __init__(self, name, health, armor, power):
       self.name = name
       self.health = health
       self.armor = armor
       self.power = power
       self.new = True
    #друк інфо про персонажа:
    def print_info(self):
       print("Рівень здоров'я:", self.health)
       print('Клас броні:', self.armor)
   
    #перевірка, чи живий персонаж
    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False
   
    #нанесення удару:
    def strike(self, enemy):
       enemy.armor -= self.power
       if enemy.armor < 0:
           enemy.health += enemy.armor
           enemy.armor = 0
 
class Warrior(Hero):
    def hello(self):
        if self.new:
            print("-> НОВИЙ ГЕРОЙ! З глибини лісу з'являється вправний воїн", self.name)
            self.new = False
        else:
            print(" з'являється войовничий", self.name)
   
    #метод для виведення на екран текстового опису атаки
    def attack(self, enemy):
        print(self.name, 'безстрашно накидається на', enemy.name)
        print('Результат сутички для', self.name)
        self.print_info()
        print('Результат сутички для', enemy.name)
        enemy.print_info()
 
class Dragon(Hero):
    def hello(self):
        if self.new:
            print('-> НОВИЙ ГЕРОЙ! З неба спускається лютий дракон', self.name)
            self.new = False
        else:
            print('І знову перед нами розлючений дракон', self.name)
   
    def attack(self, enemy):
        print(self.name, 'направляє потік смертельного вогню на', enemy.name)
        print('Результат сутички для', self.name)
        self.print_info()
        print('Результат сутички для', enemy.name)
        enemy.print_info()
 
knight = Warrior('Річард', 50, 25, 20)
print('Вітаємо тебе, славний лицар', knight.name)
print('Ти стоїш біля входу в ліс, повний смертельних небезпек. Чи готовий ти увійти всередину і битися з ворогами (так/ні)?')
answer = input()
if answer == 'так':
    play = True
    print('\n***Так почнеться битва!*** \n')
else:
    play = False

enemies = list()
enemies.append(Warrior('Пітер', 15, 0, 10))
enemies.append(Warrior('Сержіо', 10, 15, 5))
enemies.append(Dragon('Дрогон', 1, 25, 60))
enemies.append(Dragon('Візеріон', 1, 10, 30))
 
while play:
    #Визначаємо, з ким буде битися лицар
    #як індекс беремо довжину списку, т.к. після вбивства ворогів список скорочуватиметься
    a=randint(0,len(enemies)-1)
    enemy = enemies[a]
    enemy.hello()
    enemy.print_info()
 
    is_attack = input('Вступити в бій (так/ні)?')
    if is_attack == 'так':
        if randint(0,1) == 1:
            figthers = [knight, enemy]
        else:
            figthers = [enemy, knight]
        figthers[0].strike(figthers[1])
        figthers[0].attack(figthers[1])
    print('---')
 
    #перевіряємо, чи загинули поточний ворог і якщо так, то видаляємо його зі списку
    if enemy.check_alive() == False:
        print(enemy.name, 'загинув від руки', knight.name, '\n')
        enemies.remove(enemy)
   
    #перевіряємо умови завершення гри (загинув лицар або вбито всіх ворогів)
    if knight.check_alive() == False:
        print('Хоробрий лицар', knight.name, 'загинув у бою з ворогами')
        play = False
    if len(enemies) == 0:
        print('Хоробрий лицар', knight.name, 'переміг усіх ворогів!')
        play = False
print('Тут і казці кінець')
