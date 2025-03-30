class Board:
    def __init__(self):
       self.board=[i for i in range(1,101)]
       self.ladders={7:23, 13:43, 52:80}
       self.chutes={99:20, 76:40, 54:22}

    def createBoard(self):
        pass
    
    def displayBoard(self):
        print(self.board)

    def updateBoard(self):
        print("Board updated")
    
    def getBoard(self):
        return self.board

    def destroyBoard(self):
        pass

