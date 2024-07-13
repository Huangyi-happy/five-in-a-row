class Referee:
    def __init__(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def __judgeRow(self,board):
        for i in range(0,15,1):
            blackCount=0
            whiteCount=0
            for j in range(0,15,1):
                if board.getGrid()[i][j]==None:
                    blackCount=0
                    whiteCount=0
                elif board.getGrid()[i][j].getColor()=="black":
                    blackCount+=1
                    whiteCount=0
                    if blackCount==5:
                        return "black win"
                else:
                    whiteCount+=1
                    blackCount=0
                    if whiteCount==5:
                        return "white win"
        return "NO winner"

    def __judgeCol(self,board):
        for j in range(0,15,1):
            blackCount = 0
            whiteCount = 0
            for i in range(0,15,1):
                if board.getGrid()[i][j] == None:
                    blackCount = 0
                    whiteCount = 0
                elif board.getGrid()[i][j].getColor() == "black":
                    blackCount += 1
                    whiteCount = 0
                    if blackCount == 5:
                        return "black win"
                else:
                    whiteCount += 1
                    blackCount = 0
                    if whiteCount == 5:
                        return "white win"
        return "NO winner"

    def __judgeTopLeftTriangle(self,board):

        for sum in range(0,11,1):
            blackCount=0
            whiteCount=0
            for i in range(sum,15,1):
                if board.getGrid()[i][sum-i]==None:
                    blackCount=0
                    whiteCount=0
                elif board.getGrid()[i][sum-i].getColor()=="black":
                    blackCount+=1
                    whiteCount=0
                    if blackCount==5:
                        return "black win"
                else:
                    whiteCount+=1
                    blackCount=0
                    if whiteCount==5:
                        return "white win"
        return "NO winner"
    def __bottomRightTriangle(self, board):
        for sum in range(14,25,1):
            blackCount=0
            whiteCount=0
            for i in range(sum-14,15,1):
                # print("({},{})".format(i,sum-i),end="")
                if board.getGrid()[i][sum-i]==None:
                   blackCount=0
                   whiteCount=0
                elif board.getGrid()[i][sum-i].getColor()=="black":
                    blackCount+=1
                    whiteCount=0
                    if blackCount==5:
                        return "black win"
                else:
                    whiteCount+=1
                    blackCount=0
                    if whiteCount==5:
                        return "white win"

        return "NO winner"

    def __bottomLeftTriangle(self,board):

        for sum in range(0,11,1):
            blackCount=0
            whiteCount=0
            for i in range(sum,15,1):
                # print("({},{})".format(i,i-sum),end="")
                if board.getGrid()[i][i-sum]==None:
                   blackCount=0
                   whiteCount=0
                elif board.getGrid()[i][i-sum].getColor()=="black":
                    blackCount+=1
                    whiteCount=0
                    if blackCount==5:
                        return "black win"
                else:
                    whiteCount+=1
                    blackCount=0
                    if whiteCount==5:
                        return "white win"

        return "NO winner"

    def __judgeTopRightTriangle(self,board):

        for sum in range(0,11,1):
            blackCount=0
            whiteCount=0
            for i in range(0,15-sum,1):
                # print("({},{})".format(i,sum+i),end="")
                if board.getGrid()[i][sum+i]==None:
                   blackCount=0
                   whiteCount=0
                elif board.getGrid()[i][sum+i].getColor()=="black":
                    blackCount+=1
                    whiteCount=0
                    if blackCount==5:
                        return "black win"
                else:
                    whiteCount+=1
                    blackCount=0
                    if whiteCount==5:
                        return "white win"

        return "NO winner"

    def judge(self,board):
        if self.__judgeRow(board)=="white win" or self.__judgeCol(board)=="white win" or self.__judgeTopLeftTriangle(board)=="white win" or self.__bottomRightTriangle(board)=="white win" or self.__bottomLeftTriangle(board)=="white win" or self.__judgeTopRightTriangle(board)=="white win":
            return "white win"
        elif self.__judgeRow(board)=="black win" or self.__judgeCol(board)=="black win" or self.__judgeTopLeftTriangle(board)=="black win" or self.__bottomRightTriangle(board)=="black win" or self.__bottomLeftTriangle(board)=="black win" or self.__judgeTopRightTriangle(board)=="black win":
            return "black win"
        else:
            return "NO winner"