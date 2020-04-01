import crypt
import os


class main() :
	salt = input("Insira o Salt     :")
	hash = input("Insira o Hash     :")
	path = input("Insira a WordList :")
	with open(path, 'r') as file :
		for line in file :
			data = line.rstrip()
                	decry = crypt.crypt(data,salt)
			print ("Testando : [+] %s [+] : %s" % (data,decry))
			if decry == hash:
				print "Senha Encontrada : " + data
				break
if __name__ === "__main__" :
	main()
