# 3. LSP(Liskov Substitution Principle) 리스코프 치환 원칙
class People:
    def __init__(self, name, gender, age):
        self.name   = name
        self.gender = gender
        self.age    = age

    def get_toilet(self):
        if self.gender == 'male':
            return "남자 화장실"
        
        elif self.gender == 'female':
            return "여자 화장실"

class Child(People):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
    
    def get_toilet(self):
        if self.gender == 'male':
            if self.age <= 5:
                return '엄마 따라서 여자 화장실'
            return "남자 화장실"
        
        elif self.gender == 'female':
            return "여자 화장실"

yeongrok = People('송영록', 'male', 30)
print(yeongrok.get_toilet())
# 남자 화장실
minho    = Child('김민호', 'male', 5)
print(minho.get_toilet())
# 엄마 따라서 여자 화장실

# 상위 타입의 객체를 하위 타입의 객체로 치환해도 상위 타입을 사용하는 프로그램은 정상적으로 동작해야 한다. 
# 부모 클래스의 인스턴스인 영록이는 남자 화장실을 가지만 자식 클래스인 민호로 치환하면 여자 화장실을 간다. LSP 위반

class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
    
    def set_width(self, value):
        self.width = value
    
    def set_height(self, value):
        self.height = value
    
    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, value):
        self.width  = value
        self.height = value
    
    def set_width(self, value):
        self.width  = value
        self.height = value
    
    def set_height(self, value):
        self.height = value
        self.width  = value

rectangle1 = Rectangle(2, 5)
rectangle2 = Square(5)

rectangle1.set_width(3)
rectangle1.set_height(10)
print(rectangle1.get_area())
# 30

rectangle2.set_width(3)
rectangle2.set_height(10)
print(rectangle2.get_area())
# 100


# 1. 하위 클래스는 부모 클래스에 정의된 것보다 사전조건을 엄격하게 만들면 안 된다.
# 2. 하위 클래스는 부모 클래스에 정의된 것보다 약한 사후조건을 만들면 안된다