class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age): ## 자바에서의 생성자로 객체를 생성할 때 자동으로 호출되는 일종의 초기 설계도)
        """Initialize name and age attributes.""" # name과 age의 값을 instance(메모리 객체)에 저장하기 위해 초기 속성의 저장위치(주소값) 부여
        self.name = name # name 변수의 속성(실제는 주소값)을 self.name에 저장(자기 자신의 주소값)
        self.age = age # age 변수의 속성(실제는 주소값)을 self.age에 저장(자기 자신의 주소값)

    def sit(self):
        """Stimulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Stimulate a dog rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog("멍멍이", 2)
your_dog = Dog("진돗개", 4)
my_dog.sit()
my_dog.roll_over()
my_dog.name
my_dog.age
print(str(my_dog.sit()) + "and" + str(your_dog.roll_over()))

print(my_dog.name, my_dog.age)
