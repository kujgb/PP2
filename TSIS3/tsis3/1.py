class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("")

    def printString(self):
        print(self.string.upper())

manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()