class Product() :
    serial_num = 0
    def __init__(self):
        Product.serial_num += 1
        self.serial_num = Product.serial_num
        self.name = None
    
        print('생성자 호출')

print('h1 객체 생성 전')
h1 = Product()
print('h1 객체 생성 후')
print(h1.name)