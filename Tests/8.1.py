class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    pass
class Mammals(Animals):
    pass
class Giraffes(Mammals):
    pass
class Animals(Animate):
    def breathe(self):
        print('Дышит')
    def move(self):
        print('Двигается')
    def eat_food(self):
        print('Ест')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('Кормит детенышей молоком')
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('Ест листья')
    def find_food(self):
        self.move()
        print('Я нашел еду!')
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
    def left_foot_forward(self):
        print('левая нога вперед')
    def left_foot_back(self):
        print('левая нога назад')
    def right_foot_forward(self):
        print('правая нога вперед')
    def right_foot_back(self):
        print('правая нога назад')
    def __init__(self, spots):
        self.giraffe_spots = spots
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()
