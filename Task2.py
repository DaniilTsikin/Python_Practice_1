#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def CheckTruth(X, Y, Z):

    print(f'X = {X}, Y = {Y}, Z = {Z} ' )
    if(not(X or Y or Z)==(not X and not Y and not Z)):
        return print(True)
    else: return print(False)

def TrueOrFalse(A, B, C, D, F, G, H, I):
    if(A==B==C==D==F==G==H==I):
        return print("Утверждение истинно")
    else: return print("Утверждение ложно")


firstCheck = CheckTruth(X = bool(0), Y = bool(0), Z = bool(0))
SecondCheck = CheckTruth(X = bool(1), Y = bool(0), Z = bool(0))
ThirdCheck = CheckTruth(X = bool(0), Y = bool(1), Z = bool(0))
FourthCheck = CheckTruth(X = bool(0), Y = bool(0), Z = bool(1))
FifthCheck = CheckTruth(X = bool(1), Y = bool(1), Z = bool(0))
SixthCheck = CheckTruth(X = bool(0), Y = bool(1), Z = bool(1))
SeventhCheck = CheckTruth(X = bool(1), Y = bool(0), Z = bool(1))
EighthCheck = CheckTruth(X = bool(1), Y = bool(1), Z = bool(1))

truth = TrueOrFalse(firstCheck,SecondCheck,ThirdCheck,FourthCheck,FifthCheck,SixthCheck,SeventhCheck,EighthCheck)

