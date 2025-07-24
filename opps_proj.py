class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin='False'
        self.menu()

    def menu(self):
        user_input=input(""""welcome to chat book !! How would you like to proceeed?
                         1. Press 1 for signup
                         2. Press 2 to Sign in
                         3. Press 3 to write a post
                         4. Press 4 to message as friend
                         5. Press any other key to exit \n""")
        if user_input=='1':
            self.signup()           
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            self.my_post()
        elif user_input=='4':
            self.send_message()
        else:
            exit()

    def signup(self):
        email=input("Enter your email here --> ")
        pwd=input("Enter the password here -->")
        self.username=email
        self.password=pwd
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup by pressing 1 in main menu")
        else:
            uname=input("Enter the email id and password")
            pwd=input("Setup your password here")
            if self.username==uname and self.password==pwd:
                print("You have singed in successfully")
                self.loggedin=True
            else:
                print("Please enter correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin=="True":
            txt=input("Enter your message here")
            print(f"Following content has been posted --> {txt}")
        else:
            print("You need to sign in first to post something")
        print("\n")
        self.menu()

    def send_message(self):
        if self.loggedin==True:
            txt=input("Please enter the message here")
            frend=input("Whom to send the msg")
            print(f"Your message has been sent to {frend}")     
        else:
            print("Please sigin first to send the message")
        print("\n")
        self.menu()
obj=chatbook()
