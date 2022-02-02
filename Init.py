# __init__은 파이썬에서 사용하는 생성자이다.

class Unit:
    def __init__(self, name, hp, damage): # def하고 바로 __하는게 아니라 한칸 띄우고 함. init은 다음장에서 설명함.
        self.name = name # 맴버변수 : 클래스 내에서 정의된 변수. self.으로 되는 "name, hp, damage"이 맴버 변수다.
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # self를 제외하고 name, hp, damage를 정의했으면 동일한 갯수만큼 선언해야한다.
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
tank2 = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기. 클로킹(은신)
wraith = Unit("레이스", 82, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith.name, wraith.damage)) 
# 맴버 변수인 name, hp, damage를 정의하면 변수.하면 자동으로 맴버 변수 사용할 수 있는 유닛들이 나온다.

# 다크아칸 마인드 컨트롤 : 상대방 유닛을 빼앗음.

wraith2 = Unit("레이스", 82, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 입니다.".format(wraith2.name))