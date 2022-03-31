from operator import truediv


is_male = True
is_tall = True

if is_male and is_tall:
    print("You are both male and tall")
elif is_male and not (is_tall): 
    print("You are a short male")
elif not(is_male) and (is_tall):
    print("You are not male but are tall")
else:
    print("You are either not tall or male or both")