class user:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}

        self.loadUser()

    def loadUser():
        pass

    def register(self, user:eUser):
        self.users.append(user)
        print('Kullanici olusturuldu.')

    def login(self):
        pass

    def saveToFile(self):
        pass

repository=UserRepository()


while True:
    print('Menu'.center(50,'*'))
    secim=input('2-Register\n2-Login\n3-Logout\n4-identity\n5-exit\nseciminiz: ')

    if secim=='5':
        break
    elif secim=='1':
        username=input('username: ')
        password=input('password: ')
        email=input('email')

        user=User(username=username,password=password,email=email)
        repository.register(user)
    elif secim=='2':
        pass
    elif secim=='3':
        pass
    elif secim=='4':
        pass
    else:
        print("yanlis secim!!")