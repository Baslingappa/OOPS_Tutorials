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
                         5. Press any other key to exit """)
        if user_input=='1':
            self.signup()           
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()
    def signup(self):
        email=input("Enter your email here --> ")
        pwd=input("Enter the password here -->")
        self.username=email
        self.password=pwd
        print("You have signed up successfully")
        self.menu()

obj=chatbook()
