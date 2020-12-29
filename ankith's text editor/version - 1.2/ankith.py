from datetime import *
class cryptography:
    def encrypt(string):
        encryption_algorithm = {"a":"9n","b":"Vp","c":"rg","d":"3r","e":"8v","f":"oV","g":"6n","h":"mT","i":"Er","j":"Vq","k":"gG","l":"nG","m":"Z7","n":"nD","o":"Z0","p":"9w","q":"T6","r":"cP","s":"e0","t":"w2","u":"Mf","v":"j7","w":"8Y","x":"3n","y":"7f","z":"Tp","1":"ln","2":"zR","3":"47","4":"3y","5":"iQ","6":"r0","7":"vf","8":"ji","9":"IS","0":"fq","A":"qX","B":"pk","C":"4a","D":"JG","E":"Sz","F":"n3","G":"gr","H":"Xp","I":"6b","J":"dL","K":"3b","L":"DR","M":"0q","N":"i0","O":"0c","P":"Kq","Q":"mz","R":"E1","S":"vG","T":"pF","U":"wr","V":"2e","W":"Xv","X":"Dt","Y":"4Y","Z":"8f"," ":"tg",",":"er",";":"gr","[":"%H","]":"ui","{":"fr","}":"&H","|":"!#",":":"6y","/":"7u","?":"34",">":"r4","<":"t3","!":"GY","@":"fH","#":")j","$":"i9","%":"^G","^":"{J","&":"HU","*":"G3","(":"$J",")":"*j","~":"$r",".":"tt","=":"th","-":"4h","_":"ht","+":"3z"}
        encrypted_string = []
        letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","(",")",".","_","-","+","=","{","}","[","]","(",")",":",";","<",",",">","/","?","~"," "]
        for letter in string:
            if letter in letter_list:
                a = encryption_algorithm.get(letter)
                encrypted_string.append(a)
            else:
                print("something else happened")
        encrypted_word = ""
        for letter in encrypted_string:
            encrypted_word += str(letter)
        return encrypted_word
    def decrypt(string):
        encryption_algorithm = {"a":"9n","b":"Vp","c":"rg","d":"3r","e":"8v","f":"oV","g":"6n","h":"mT","i":"Er","j":"Vq","k":"gG","l":"nG","m":"Z7","n":"nD","o":"Z0","p":"9w","q":"T6","r":"cP","s":"e0","t":"w2","u":"Mf","v":"j7","w":"8Y","x":"3n","y":"7f","z":"Tp","1":"ln","2":"zR","3":"47","4":"3y","5":"iQ","6":"r0","7":"vf","8":"ji","9":"IS","0":"fq","A":"qX","B":"pk","C":"4a","D":"JG","E":"Sz","F":"n3","G":"gr","H":"Xp","I":"6b","J":"dL","K":"3b","L":"DR","M":"0q","N":"i0","O":"0c","P":"Kq","Q":"mz","R":"E1","S":"vG","T":"pF","U":"wr","V":"2e","W":"Xv","X":"Dt","Y":"4Y","Z":"8f"," ":"tg",",":"er",";":"gr","[":"%H","]":"ui","{":"fr","}":"&H","|":"!#",":":"6y","/":"7u","?":"34",">":"r4","<":"t3","!":"GY","@":"fH","#":")j","$":"i9","%":"^G","^":"{J","&":"HU","*":"G3","(":"$J",")":"*j","~":"$r",".":"tt","=":"th","-":"4h","_":"ht","+":"3z"}
        decoder_algorithm = {value:key for (key,value) in encryption_algorithm.items()}        
        iterator = 0
        length = len(string)
        multiples_of_two = ["0","2","4","6","8"]
        if str(length)[-1] in multiples_of_two:
            decode_list = []
            letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","(",")",".","_","-","+","=","{","}","[","]","(",")",":",";","<",",",">","/","?","~"," "]
            for letter in string:
                if letter not in letter_list:
                    print("invalid string: "+letter)
                else:
                    while iterator != length:
                        index = iterator + 1
                        num = ""
                        num += str(string[iterator])
                        num += str(string[index])
                        iterator += 2
                        decode_list.append(num)
            decrypted_message = ""
            for item in decode_list:
                inventory = decoder_algorithm.get(item)
                decrypted_message += inventory
            return decrypted_message
    def findsize(bytesc):
        def strip(bytesc):
            bytesc = str(bytesc)
            array = [item for item in bytesc]
            index = array.index(".")
            del array[index+3:len(array)]
            string = ""
            for item in array:
                string += item
            string = float(string)
            return string
        def findindex(string):
            string = str(string)
            array = [item for item in string]
            if "." not in array:
                return [4,"doit"]
            else:
                return [array.index("."),"1"]
        state = "bytes"
        index = ["kb","mb","gb","tb"]
        length = len(str(bytesc))
        buffer1 = 4 
        for item in index:
            if length >= buffer1:
                n = str(bytesc)[0:findindex(bytesc)[0]]
                if int(n) > 1024 or findindex(bytesc)[1] == "doit":
                    bytesc /= 1024
                    bytesc = strip(bytesc)
                    state = item
                    length = len(str(bytesc))
                else:
                    break
            else:
                break
            buffer1 = 6
        return str(bytesc)+" "+state