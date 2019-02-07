class file_c_r_c(object):
    def __init__(self, a, n):
        self.adress = a
        self.name = n
    def creation_f(self):
        b = open(str(self.adress) + str(self.name) + '.txt', 'w')
        c = input('Запись в файл: ')
        b.write(str(c))
        b.close
    def copy_r_c(self):
        ans = input("""Хотите ли вы скопировать файл?(Y / N)""")
        if ans.lower() == 'y':
            b_1 = open(str(self.adress) + str(self.name) + '.txt')
            copy = b_1.read()
            b_2 = open(str(self.adress) + str(self.name) + '_copy.txt', 'w')
            b_2.write(str(copy))
            b_1.close
            b_2.close
        else:
            print('Done')
a = input('Введите адрес файла: ')#D:\\MrCross Files\\Python\\Python\\Test\\
n = input('Введите название файла: ')#test
create_file = file_c_r_c(a, n)
create_file.creation_f()
create_file.copy_r_c()
