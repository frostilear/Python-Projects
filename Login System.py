#login system
Choice=str(input("Do you want to login?(y/n)"))
if Choice.lower()=="y":
    Username=str(input("Username: "))
    Password=str(input("Password: "))
    passworddetected=False
    usernamedetected=False
    name="emtpy"
    with open("LoginInfo.rtf","r") as File_Read:
        File_list=str(File_Read.read()).split(",")
        #print(Written_Username+"-"+Written_Password)
        for item in File_list:
            if item==Username:
                usernamedetected=True
            if item==Password:
                passworddetected=True
        if(usernamedetected and passworddetected ==True):
            print("Welcome"+","+Username)
        else:
            print("Wrong Username or Password.")

if Choice.lower()=="n":
    choice2=input("Do you want to create a new account?(y/n)")
    if choice2.lower()=="y":
     WriteUsername=input("Please enter a username: ")
     WritePassword=input("Please enter a password: ")
     with open("LoginInfo.rtf","a") as File_Append:
         File_Append.write(WriteUsername+","+WritePassword+",")
         print("Your username and password have been added to the log file") 
    if choice2.lower()=="n":
     print("Well then this program has no function for you :(")