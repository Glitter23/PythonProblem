import sys
class Board:
    def __init__(self):
        self.a=[['X','X','X'],['X','X','X'],['X','X','X']]

    def get_board(self): 
        print(self.a) 

    def get_response(self):
        x=int(input("print x y"))
        y=int(input())
        z= input("enter either 0 or 1 choice")

        if self.a[x][y]=='X':
            self.a[x][y]=z

    def checkwon(self):
        
        if (self.a[0][0]==self.a[0][1]):
            if (self.a[0][2]==self.a[0][1]):
                if (self.a[0][2]!='X'):
                    print('won')
                    sys.exit()

        if (self.a[1][0]==self.a[1][1]):
            if (self.a[1][2]==self.a[1][1]):
                if (self.a[1][2]!='X'):
                    print('won')
                    sys.exit()
               

        if (self.a[2][0]==self.a[2][1]):
            if (self.a[2][2]==self.a[2][1]):
                 if (self.a[2][2]!='X'):
                    print('won')
                    sys.exit()
               

        if (self.a[0][0]==self.a[1][1]):
            if (self.a[2][2]==self.a[1][1]):
                if (self.a[2][2]!='X'):
                    print('won')
                    sys.exit()
             
    def checkfill(self,x,y):
        if self.a[x][y]!='X':
            return 1
        return 0


if __name__=="__main__":
    n= Board()
    n.get_board()
  
    n.get_board()
    n.__init__()
    n.get_board()
    while True:
        n.get_response()
        n.checkwon()
        n.get_board()

    
