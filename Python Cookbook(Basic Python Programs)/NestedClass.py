class Outer:
    def __init__(self):
        """Just initialization taking place here."""
        self.i = 0
        self.j = 0
        self.iobj = Inner()

    def fun(self):
        print("Inside instance")

    class Inner:
        def __init__(self):
            self.x = 0
