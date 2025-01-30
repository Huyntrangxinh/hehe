# 1. Encapsulation - Đóng gói
class Car:
    def __init__(self, make, model):
        self.__make = make  # Đóng gói dữ liệu
        self.__model = model

    def get_car_info(self):  # Phương thức để truy xuất thông tin
        return f"Car make: {self.__make}, Model: {self.__model}"

# 2. Abstraction - Trừu tượng hóa
class Shape:
    def area(self):
        pass  # Phương thức trừu tượng

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius  # Tính diện tích hình tròn

# 3. Inheritance - Kế thừa
class ElectricCar(Car):  # Kế thừa từ lớp Car
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)  # Gọi phương thức khởi tạo của lớp cha
        self.battery_size = battery_size

    def get_battery_info(self):
        return f"Battery size: {self.battery_size} kWh"

# 4. Polymorphism - Đa hình
def print_area(shape: Shape):
    print(f"Area: {shape.area()}")  # Phương thức đa hình

# Sử dụng các lớp trên:
my_car = Car("Toyota", "Camry")
print(my_car.get_car_info())

my_circle = Circle(5)
print_area(my_circle)

my_electric_car = ElectricCar("Tesla", "Model S", 75)
print(my_electric_car.get_car_info())
print(my_electric_car.get_battery_info())
