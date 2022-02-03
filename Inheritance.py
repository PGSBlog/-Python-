#일반 유닛(상속)
class Unit:
    def __init__(self, name, hp): # def하고 바로 __하는게 아니라 한칸 띄우고 함. init은 다음장에서 설명함.
        self.name = name # 맴버변수 : 클래스 내에서 정의된 변수. self.으로 되는 "name, hp, damage"이 맴버 변수다.
        self.hp = hp
 
# 공격 유닛(클래스) - 상속받아짐(Unit)
class AttackUnit(Unit):
    def __init__(self, name, hp, damage): # def하고 바로 __하는게 아니라 한칸 띄우고 함. init은 다음장에서 설명함.
        Unit.__init__(self, name, hp) # 위에 Unit 클래스에서 상속 받음
        self.damage = damage # AttackUnit에서 직접 전달받음.
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))
    # (location 메소드)
    def attack(self, location): # 클래스를 사용할때는 self을 항상 사용해줘야한다.
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
        # 위에 self.name, self.damage는 상단 def __init__에서 정의된 것들을 사용하는 것이고 location 값은 def attack(self, location)인,
        # location에게 받는다는 뜻이다.
    
    # (damaged 메소드)
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0 :
            print("{0}의 체력이 없기에 파괴되었습니다.".format(self.name))
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# 다중 상속

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격X

class Flyable: # 공중유닛에 스피드 생성.
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(seld, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스(다중 상속)
class FlyableAttacUnit(AttackUnit, Flyable): # AttackUnit, Flyable 두개를 상속 받는다.  
    def __init__(self, name, hp, damage, flying_speed): # Attack클래스에 정의된 name, hp, damage와 
                                                        # 새로 Flyable 클래스에서 정의된 flying_speed를 상속받기 위해 초기화를 진행한다.
        AttackUnit.__init__(self, name, hp, damage) # Attack클래스에 정의된 name, hp, damage를 상속한다.
        Flyable.__init__(self, flying_speed) # Flyable 클래스에서 정의된 flying_speed를 상속한다.


# 발키리 : 공중 공격 유닛, 한번에 14발을 미사일을 발사한다.
valkirie = FlyableAttacUnit("발키리", 200, 6, 5) # name, hp, damage, flying_speed를 기입한다.
valkirie.fly(valkirie.name, "15시") # Flyable에서 Fly변수는 은 따로 맴버 변수가 없고 기능(속도 정보)만 있기에 name에 valkirie.name으로 선언해준다.


# Unit, AttackUnit, FlyableAttacUnit, Flyable이 있을 때, 

# AttackUnit--->Unit

# FlyableAttacUnit ---> Flyable
#                  ---> AttackUnit

# 이런식으로 AttackUnit은 Unit을 상속받고 FlyableAttacUnit은 다중 상속을 받고있는 상태이다.