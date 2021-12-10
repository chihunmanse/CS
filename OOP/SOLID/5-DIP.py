# 5. DIP(Dependency Inversion Principle) 의존 역전 원칙

# 클래스가 있을 때 어떤 클래스가 다른 클래스를 사용하는 관계에 있으면 사용하는 클래스를 상위 모듈, 사용 당하는 클래스를 하위 모듈이라고 한다.
# 클래스는 가능한 추상적으로 의존해야 하며 구체적으로 의존하면 안 된다.
class Sword:
    def __init__(self, damage):
        self.damage = damage

    def slash(self, other_character):
        other_character.get_damage(self.damage)

class Character:
    def __init__(self, name, hp, sword: Sword):
        self.name  = name
        self.hp    = hp
        self.sword = sword

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.sword.slash(other_character)
        else:
            print(self.name + "님은 쓰러져서 공격할 수 없습니다.")

    def change_sword(self, new_sword):
        """검을 바꾸는 메소드"""
        self.sword = new_sword

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 쓰러졌습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        return f"{self.name}님은 hp: {self.hp}이(가) 남았습니다."

bad_sword  = Sword(100)
good_sword = Sword(200)

character_1 = Character("구본욱", 200, bad_sword)
character_2 = Character("김민호", 500, good_sword)

character_1.attack(character_2)
character_2.attack(character_1)

print(character_1)
print(character_2)

# 구본욱님은 쓰러졌습니다.
# 구본욱님은 hp: 0이(가) 남았습니다.
# 김민호님은 hp: 400이(가) 남았습니다.

# 상위 모듈인 Character가 하위 모듈인 Sword를 의존하고 있다. Sword의 메서드가 수정되거나 삭제되면 Character가 동작할 수 없게 된다.

class IWeapon(ABC):
    """무기 클래스"""
    @abstractmethod
    def use_on(self, other_character):
        pass

class Sword(IWeapon):
    """검 클래스"""
    def __init__(self, damage):
        self.damage = damage
        
    def use_on(self, other_character):
        other_character.get_damage(self.damage)

class Gun(IWeapon):
    """총 클래스"""
    def __init__(self, damage, num_rounds):
        self.damage = damage
        self.num_rounds = num_rounds
        
    def use_on(self, other_character):
        """총 사용 메소드"""
        if self.num_rounds > 0:
            other_character.get_damage(self.damage)
            self.num_rounds -= 1
        else:
            print("총알이 없어 공격할 수 없습니다")

class NewCharacter:
    def __init__(self, name, hp, weapon: IWeapon):
        self.name   = name
        self.hp     = hp
        self.weapon = weapon

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.weapon.use_on(other_character)
        else:
            print(self.name + "님은 쓰러져서 공격할 수 없습니다.")

    def change_sword(self, new_sword):
        """검을 바꾸는 메소드"""
        self.sword = new_sword

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 쓰러졌습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        return f"{self.name}님은 hp: {self.hp}이(가) 남았습니다."

sword = Sword(5)
gun   = Gun(200, 10)

game_character_1 = NewCharacter("구본욱", 200, sword)
game_character_2 = NewCharacter("김민호", 500, gun)

game_character_1.attack(game_character_2)
game_character_2.attack(game_character_1)

print(game_character_1)
print(game_character_2)

# 구본욱님은 쓰러졌습니다.
# 구본욱님은 hp: 0이(가) 남았습니다.
# 김민호님은 hp: 495이(가) 남았습니다.

# 상위 모듈이 하위 모듈을 사용할 때 직접 인스턴스를 가져다 쓰지 말아야 한다. 
# 하위 모듈의 구체적인 내용에 상위 모듈이 의존하게 되어 하위 모듈에 변화가 있을 때마다 상위 모듈의 코드를 자주 수정해야 되기 때문이다.