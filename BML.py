class BML:
    def __init__(self,name,age,weight,high):
        self.name = name
        self.age = age
        self.weight = float(weight)
        self.high = float(high)
    def say_bml(self):
        print("Helo my bml is {n}".format(n=self.weight/self.high**2))
    def say_fit(self):
        if(self.weight-self.high*self.high>24):
            print("正常")
        if(self.weight-self.high*self.high<30):
            print("偏胖")
        if(self.weight-self.high*self.high<18.5):
            print("偏瘦")