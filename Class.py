# # 마린 : 공격 유닛, 군인이고 총을 쏠 수 있음.
# name = '마린' # name은 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0}유닛이 생성되었습니다.".format(name))
# print("체력 : {0}, 공격력 : {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크이며 포을 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = '탱크' # name은 유닛의 이름
# tank_hp = 150 # 유닛의 체력
# tank_damage = 35 # 유닛의 공격력

# # 탱크 : 공격 유닛, 탱크이며 포을 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank2_name = '탱크' # name은 유닛의 이름
# tank2_hp = 150 # 유닛의 체력
# tank2_damage = 35 # 유닛의 공격력

# print("{0}유닛이 생성되었습니다.".format(tank_name))
# print("체력 : {0}, 공격력 : {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다.[공격력{2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# # 이렇게 함수를 N개 이상 만들면 효율이 떨어지니 클래스를 사용하는 것이다.

class Unit:
    def __init__(self, name, hp, damage): # def하고 바로 __하는게 아니라 한칸 띄우고 함. init은 다음장에서 설명함.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
tank2 = Unit("탱크", 150, 35)