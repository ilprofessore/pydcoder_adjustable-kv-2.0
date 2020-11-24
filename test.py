class FirstOne:
    def __init__(self):
        self.name = "zain"

    def funk(self):
        self.name = "zain khan"

class SecondOne(FirstOne):
    def __init__(self):
        super().__init__()
        FirstOne().funk
        print(self.name)

SecondOne()