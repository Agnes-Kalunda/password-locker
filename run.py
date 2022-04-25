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
                 



