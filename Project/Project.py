# Project:
#1. Receives an email from the user
#2. Validate the email 
#3. If it is invalid log the error in the file
#4. if it is valid, clean and structure the email in the form of dictionary by splitting it into two parts: username and domain
print("-----------------------------------------")


#defining individual functions
def validate_email(email):
    return '@' in email and '.' in email


def write_log(message):
        with open(r"C:\Users\LENOVO\Desktop\Message log.txt","a") as file:
            file.write(message + "\n")
            print(f"Invalid Email: Log updated")
           

def clean_the_email(email):
         clean_email=email.strip().lower()
         username,domain=clean_email.split('@')
         return {"username": username,
                 "domain":domain}


#Data Pipeline
user_email=input("Please enter your email: ")
def pipeline(Email):
    if not validate_email(user_email):
     write_log("Invalid Email: Please enter a valid email")
    else:
     cleaned_Email=clean_the_email(user_email)
     print(cleaned_Email)


#Calling Data Pipeline
pipeline({user_email})
         
         
         

    

      
      