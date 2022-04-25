from user import User
import random

def main():
     while true:
         print("Welcome!")
         print('/n')
         print("Use short code To add a new user,kindlyselect'newuser' :To login into your account,kindly select 'login'.And to leave your account,kindly select 'x' to exit.Thankyou.")

         short_code = input().lower()
         print['z']

         if short_code == 'newuser':
             print('create username')
             created_user_name = input()

             print('create password')
             created_user_password= input()

             print('confirm password')
             confirm_password=input()

             while confirm_password != created_user_password:
             print("sorry!Password did not match")
             print("please re-enter password")
             created_user_password = input()
             print("confirm password")
             confirm_password= input()
             
            else:
                 print(f"congratulations {created_user_name},account successfully created!")
                 print('\n')
                 print("login")
                 print("Username")
                 entered_username = input()
                 print("your password")
                 entered_password=input()


            while entered_password!= created_user_name or entered_password!=created_user_password:
                     print("invalid username or password!Try again!")
                     print("Username")
                     entered_username = input()
                     print("your password")
                     entered_password=input()

                else:
                    print("welcome{created_username}to your account")
                    print('\n')

                    elif short_code == 'login':
                        print("Enter username")
                        default_user_name= input()

                        print("Enter password")
                        default_user_password= input()
                        print('\n')

                        while default_user_name!= 'testuser'or default_user_password!= 09876
                        print ("Your password/username did not match. username= 'testuser' and password= '09876'")
                        print ("please enter your username")
                        default_user_name = input()

                        print("please enter your password")
                        default_user_password = input()
                        print("\n")

                        else:
                            print("login successful!!")
                            print('\n')
                            print('\n')

                            elif short_code == 'x':
                                break
                            else:
                                print("please enter valid code")

                                if __name__ == '_main_':
                                    main()





