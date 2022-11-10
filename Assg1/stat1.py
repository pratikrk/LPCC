def extractSecretMessage(Str, Sub):
	Str= Str.replace(Sub, " ")
	return Str.strip()
	
Str = input()
Sub = ","
print(extractSecretMessage(Str, Sub))