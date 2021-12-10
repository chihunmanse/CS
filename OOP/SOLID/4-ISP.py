# 4. ISP(Interface Segregation Principle) 인터페이스 분리 원칙

from abc import *

class People(metaclass = ABCMeta):
    # 인터페이스 (추상 클래스)
    @abstractmethod
    def sleep(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def enjoy_adult_video(self):
        pass

class Adult(People):
    # 클라이언트 
    def sleep(self):
        return '잠 쿨쿨'
    
    def eat(self):
        return '먹는다'
    
    def enjoy_adult_video(self):
        return '즐긴다'

class Child(People):
    # 클라이언트
    def sleep(self):
        return '어린이라서 9시에 잔다'
    
    def eat(self):
        return '먹는다'
    
    def enjoy_adult_video(self):
        pass
    
    # 어린이는 enjoy_adult_video 메서드를 이용할 수 없다.

# People 인터페이스는 자신을 사용하는 클라이언트 기준으로 분리해야 한다. Child 클라이언트가 사용하지 않을 메서드에 의존할 것을 강요하면 안 된다.