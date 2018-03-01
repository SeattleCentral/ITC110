import random
import time


class Cat:

    def __init__(self):
        self.cat_lives = 9

    def begin_cats_life(self):
        while True:
            if self.cat_is_fed() and not self.lost_a_life():
                print ('The Cat is doing well.')
            else:
                print ('The Cat is not doing so great.')
            time.sleep(3)

    def cat_is_fed(self):
        if random.random() > 0.5:
            print ('Cat is fed')
            return True
        print('Cat is not fed')
        return False

    def lost_a_life(self):
        if random.random() > 0.25:
            print('Cat landed on all four')
            return False
        else:
            self.cat_lives = self.cat_lives - 1
            print('Cat lost a life')
            print('The Cat now has {0} lives left.'.format(self.cat_lives))
            return True


cat = Cat()
cat.begin_cats_life()



