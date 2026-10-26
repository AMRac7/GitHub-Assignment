
def main():
    Pass_Word = input("Enter Your Password: ")
    pass_check(Pass_Word)

def pass_check(Pass_Word):
    Num_Upper = 0
    Num_Numbers = 0
    Num_Lower = 0
    if(len(Pass_Word) < 8):
        print("Password must at least be 8 characters long")
        return False
    for i in Pass_Word:
        if (i.isupper()):
            Num_Upper +=1
        if (i.islower()):
            Num_Lower +=1
        if (i.isdigit()):
            Num_Numbers +=1
    
    if(Num_Upper < 1 or Num_Lower < 1 or Num_Numbers < 2):
        print("Password must at least contain")
        print("One Upper Case Letter")
        print("One Lower Case Letter")
        print("Two digits")
        return False
    print("Password is in correct format")



main()