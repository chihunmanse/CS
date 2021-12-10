# 2. OCP(Open-Closed Principle) 개방-폐쇄 원칙

from abc import *

class Coupon(metaclass = ABCMeta):
    # Coupon 추상 클래스
    price = '쿠폰액'

    @abstractmethod
    def show_coupon(self):
        pass
 
class FirstuseCoupon(Coupon):
    price = 5000
    
    @classmethod
    def show_coupon(cls):
        return cls.price

class ChristmasCoupon(Coupon):
    price = 3000

    @classmethod
    def show_coupon(cls):
        return cls.price

class CouponCalculation:
    def caculate(self):
        price   = 0
        coupons = [FirstuseCoupon(), ChristmasCoupon()]

        for coupon in coupons:
            price += coupon.show_coupon()
        
        return price

a = CouponCalculation()
print(a.caculate())
# 8000

# 동작에는 문제가 없지만 만약 새로운 쿠폰이 추가되었다고 했을 때 기존에 있던 CouponCalculation 클래스 coupons 리스트에 새로운 쿠폰의 인스턴스를 넣어주는 수정을 해주어야 한다. 
# 낮은 결합도란, 하나의 변경이 발생할 때 다른 모듈과 객체로 변경에 대한 요구가 전파되지 않는 상태라고 할 수 있다. 새로운 쿠폰이 생길 때마다 수정이 일어나는 CouponCalculation 클래스는 쿠폰 클래스들과 결합도가 높다고 볼 수 있다.

class NewCouponCalculation:
    def caculate(self):
        price = 0
        for coupon in Coupon.__subclasses__():
            price += coupon.show_coupon()
        
        return price

b = NewCouponCalculation()
print(b.caculate())
# 8000

# 위와 같이 CouponCalculation를 변경하면 새로운 쿠폰의 클래스가 생겨도 CouponCalculation에 수정을 할 필요가 없어진다.