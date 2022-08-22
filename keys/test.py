import functions
class main:
    def execute(self, key):
        if functions.test(key, "backspace"):
            print("testing")
        if functions.test(key, "up"):
            print("kkk")
        pass

functions.run(main, wasd="False", keys=4) 