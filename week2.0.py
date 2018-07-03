
UserTable = []

# 유저 정의
'''
User = {
    'Name' : '',
    'Id' : '',
    'Pass' : '',
    'BuyList' : [],
}
'''

ItemList = [
    'A상품',
    'B상품',
    'C상품',
    'D상품',
    'E상품',
]

class User :
    def __init__(self, NAME, ID, PASS):
        self.Name = NAME
        self.Id = ID
        self.Pass = PASS
        self.BuyList = []

    def BuyItem(self):
        for idx, item in enumerate(ItemList):
            print('%d : %s' % (idx, item))

        print('구매 : ', end="")

        buying = int(input())

        if buying >= 0 and buying <= 5:
            self.BuyList.append(ItemList[buying])
        else:
            print('없는 상품입니다')


    def CheckBuyList(self):
        print("장바구니 : ")
        for idx, item in enumerate(self.BuyList):
            print("%d : %s" % (idx, item))
        print('')

class UserManager :
    def __init__(self):
        self.UserTable = []
        self.isLogin = False
        self.LoginIdx = -1

        self.ManagerStart()

    def ManagerStart(self):
        while True:
            if self.isLogin :
                print("/****************************/")
                print("     [로그인]%s님 반갑습니다       " % (self.UserTable[self.LoginIdx].Name))
                print("/****************************/")
                print("1. 장바구니 확인")
                print("2. 상품 장바구니에 넣기")
                print("3. 돌아가기")

                selection = int(input())

                if selection == 1:
                    self.UserTable[self.LoginIdx].CheckBuyList()
                elif selection == 2:
                    self.UserTable[self.LoginIdx].BuyItem()
                else:
                    self.isLogin = False
                    self.LoginIdx = -1

            else :
                print("/****************************/")
                print("          쇼핑몰 프로그램         ")
                print("/****************************/")
                print("1. 회원 가입")
                print("2. 회원 리스트 확인")
                print("3. 회원 로그인")
                print("커맨드 : ", end="")
                selection = int(input())

                if selection == 1:
                    self.UserRegister()
                elif selection == 2:
                    self.CheckUserList()
                elif selection == 3:
                    self.UserLogIn()
                else:
                    break

    def UserRegister(self):
        print("이름 : ", end="")
        NAME = input()
        print("아이디 : ", end="")
        ID = input()
        print("패스워드 : ", end="")
        PASS = input()
        print("패스워드 확인 : ", end="")
        PASS_CONFIRM = input()

        if PASS_CONFIRM != PASS:
            print("패스워드가 다릅니다")
            return

        newUser = User(NAME, ID, PASS)

        self.UserTable.append(newUser)

    def CheckUserList(self):
        for user in self.UserTable:
            print("[ 이름 : %s, 아이디 : %s, 비밀번호 : %s ]" % (user.Name, user.Id, user.Pass))

    def UserLogIn(self):
        print("아이디 : ", end="")
        ID = input()
        print("패스워드 : ", end="")
        PASS = input()

        for idx, user in enumerate(self.UserTable):
            if user.Id == ID and user.Pass == PASS:
                self.LoginIdx = idx
                self.isLogin = True

        if self.isLogin:
            print("로그인 성공")
        else:
            print("로그인 실패")
            return

manager = UserManager()
