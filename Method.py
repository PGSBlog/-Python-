class Unit:
    def __init__(self, name, hp, damage): # def하고 바로 __하는게 아니라 한칸 띄우고 함. init은 다음장에서 설명함.
        self.name = name # 맴버변수 : 클래스 내에서 정의된 변수. self.으로 되는 "name, hp, damage"이 맴버 변수다.
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

# 공격 유닛(클래스)
class AttackUnit:
    def __init__(self, name, hp, damage): # def하고 바로 __하는게 아니라 한칸 띄우고 함. init은 다음장에서 설명함.
        self.name = name # 여기서 = 다음에 나오는 name은 위에(def __init__(self, name, hp, damage)) 전달받은 인자를 바로 사용하겠다는 뜻이다.
        self.hp = hp
        self.damage = damage
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
# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파벳", 50, 16)
firebat1.attack("5시") # def attack(self, location)로 지정되고 괄호 안에 (self, location)이지만 self는 항상 안해도 된다. 
                       # 즉, location만 작성해주면 된다.

# 파이어뱃이 공격 받았을 때, 총 체력은 50인데 0이 되었을 때 문구도 실행되는지 확인 
firebat1.damaged(25)
firebat1.damaged(25)

# 실수 조심! damage는 공격이고 damaged는 공격을 받는거니까 주의할것!
# damage로하면 damage는 self.damage로 맴버 변수임으로 지정할 수 없다.