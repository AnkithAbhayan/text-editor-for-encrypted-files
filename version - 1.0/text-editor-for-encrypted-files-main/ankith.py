from datetime import *
import os
class date_time:
    def time():
        now = datetime.now()
        current_time = now.strftime("%H/%M/%S")
        indexes = []
        letter_list = []
        for item in current_time:
            letter_list.append(item)
        for item in letter_list:
            if item == "/":
                indexes.append(letter_list.index(item))
                letter_list[letter_list.index(item)] = "a"
        hours = current_time[0:indexes[0]]
        minutes = current_time[indexes[0]+1:indexes[1]]
        seconds = current_time[indexes[1]+1:len(current_time)]
        if len(str(seconds)) != 2:
            seconds = str(0) + str(seconds)
        if len(str(minutes)) != 2:
            minutes = str(0) + str(minutes)
        if int(hours) > 12:
            mode = "PM"
        elif int(hours) <= 12:
            mode = "AM"
        return_string = ""
        current_hours = int(hours)
        if int(hours) > 12:
            current_hours -= 12
        elif int(hours) == 0:
            current_hours += 12
        return str(current_hours)+":"+str(minutes)+":"+str(seconds)+" "+mode
    def date():
        today = datetime.today()
        date = today.strftime("%d")
        datea = []
        for item in date:
            datea.append(item)
        if datea[0] == "0":
           date = datea[1]
        month = today.strftime("%m")
        year = today.strftime("%y")
        return_value = ""
        date_v = {
            "1":"st",
            "2":"nd",
            "3":"rd",
        }
        if date == "11" or date == "12" or date == "13":
            date_m = "th"
        else:
            if date[-1] in date_v:
                date_m = date_v.get(date[-1])
            else:
                date_m = "th"
        month_conv = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
        month_d = month_conv.get(month)
        year_d = "20"+str(year)
        return date+date_m+" "+month_d+" "+year_d
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
class math_functions:
    def commonfactors(number1,number2):
       item_list = []
       item_list2 = []
       multiplication_list = []
       multiplication_list2 = []
       factor_list = []
       factor_list2 = []
       common_factor_list = []
       for i in range(number1 + 1):
           if i == 0:
               pass
           else:
               item_list.append(i)
       length = len(item_list) + 1
       for i in range(len(item_list)):
           length -= 1
           for a in range(len(item_list)):
               if item_list[a] * length == number1:
                   multiplication_list.append(str(item_list[a])+" X "+str(length)+" = "+str(number1))
                   factor_list.append(item_list[a])
       for i in range(number2 + 1):
           if i == 0:
               pass
           else:
               item_list2.append(i)
       length = len(item_list2) + 1
       for i in range(len(item_list2)):
           length -= 1
           for a in range(len(item_list2)):
               if item_list2[a] * length == number2:
                   multiplication_list2.append(str(item_list2[a])+" X "+str(length)+" = "+str(number2))
                   factor_list2.append(item_list2[a])
       if len(factor_list) > len(factor_list2):
           main = factor_list.copy()
           other = factor_list2.copy()
       elif len(factor_list) < len(factor_list2):
           main = factor_list2.copy()
           other = factor_list.copy()
       else:
           main = factor_list2.copy()
           other = factor_list.copy()
       for i in range(len(other)):
          if main.count(other[i]) != 0:
             common_factor_list.append(other[i])
       return common_factor_list
    def factors(number):
        item_list = []
        multiplication_list = []
        factor_list = []
        for i in range(number + 1):
            if i == 0:
                pass
            else:
                item_list.append(i)
        length = len(item_list) + 1
        for i in range(len(item_list)):
            length -= 1
            for a in range(len(item_list)):
                if item_list[a] * length == number:
                    multiplication_list.append(str(item_list[a])+" X "+str(length)+" = "+str(number))
                    factor_list.append(item_list[a])
                else:
                    pass
        return factor_list
    def isPrime(number):
        item_list = []
        factor_list = []
        for i in range(number + 1):
            if i == 0:
                pass
            else:
                item_list.append(i)
        length = len(item_list) + 1
        for i in range(len(item_list)):
            length -= 1
            for a in range(len(item_list)):
                if item_list[a] * length == number:
                    factor_list.append(item_list[a])
                else:
                    pass
        print("the factors of "+str(number)+" are: "+str(factor_list))
        if len(factor_list) == 2:
            return True
        else:
            return False
    def highestCommonFactor(number1,number2):
       item_list = []
       item_list2 = []
       multiplication_list = []
       multiplication_list2 = []
       factor_list = []
       factor_list2 = []
       common_factor_list = []
       for i in range(number1 + 1):
           if i == 0:
               pass
           else:
               item_list.append(i)
       length = len(item_list) + 1
       for i in range(len(item_list)):
           length -= 1
           for a in range(len(item_list)):
               if item_list[a] * length == number1:
                   multiplication_list.append(str(item_list[a])+" X "+str(length)+" = "+str(number1))
                   factor_list.append(item_list[a])
       for i in range(number2 + 1):
           if i == 0:
               pass
           else:
               item_list2.append(i)
       length = len(item_list2) + 1
       for i in range(len(item_list2)):
           length -= 1
           for a in range(len(item_list2)):
               if item_list2[a] * length == number2:
                   multiplication_list2.append(str(item_list2[a])+" X "+str(length)+" = "+str(number2))
                   factor_list2.append(item_list2[a])
       if len(factor_list) > len(factor_list2):
           main = factor_list.copy()
           other = factor_list2.copy()
       elif len(factor_list) < len(factor_list2):
           main = factor_list2.copy()
           other = factor_list.copy()
       else:
           main = factor_list2.copy()
           other = factor_list.copy()
       for i in range(len(other)):
          if main.count(other[i]) != 0:
             common_factor_list.append(other[i])
       if len(common_factor_list) == 1:
          return common_factor_list[0]
       else:
          return max(common_factor_list)
    def multiples(number,times):
        multiples = []
        for i in range(times):
            answer = number * i
            multiples.append(answer)
        return multiples
    def NearestPerfectSquare(number):
        number = int(number)
        perfect_square_list = []
        nearest_perfect_square = []
        multiplication_values = []
        for i in range(number):
            answer = i * i
            perfect_square_list.append(answer)
            multiplication_values.append(str(i)+" X "+str(i)+" = "+str(answer))
            if answer > number:
                break
        if len(perfect_square_list) == 1:
            nearest_perfect_square = perfect_square_list.copy()
            nearest_perfect_square.append(multiplication_values[0])
        if number in perfect_square_list:
            num = perfect_square_list.index(number)
            perfect_square_list.remove(number)
            del multiplication_values[num]
        for i in range(len(perfect_square_list)):
            if len(perfect_square_list) == 2:
                break
            else:
                del perfect_square_list[0]
                del multiplication_values[0]
        if perfect_square_list[0] < number:
            if number - perfect_square_list[0] < perfect_square_list[1] - answer:
                nearest_perfect_square.append(perfect_square_list[1])
            else:
                nearest_perfect_square.append(perfect_square_list[0]) 
        elif perfect_square_list[0] > number:
            if perfect_square_list[0] - number > number - perfect_square_list[1]:
                nearest_perfect_square.append(perfect_square_list[1])
            else:
                nearest_perfect_square.append(perfect_square_list[0])
        return nearest_perfect_square
    def IsPerfectSquare(number):
        number = int(number)
        final = []
        for i in range(number):
            if i * i == number:
                final.append(str(number)+" is a perfect square\n"+str(i)+" X "+str(i)+" = "+str(number))
                break
            elif i * i > number:
                final.append(str(number)+" is not perfect square")
                break
        if len(final) == 0:
           return False
        else:
            return True
    def LowestCommonMultiple(number1,number2):
        number1 = int(number1)
        number2 = int(number2)
        if number1 > number2:
            big_num = number1
            small_num = number2
        elif number2 > number1:
            big_num = number2
            small_num = number1
        lcm_not_found = True
        a = 2
        i = 2
        lcm = []
        test_small_num = small_num
        test_big_num = big_num
        while lcm_not_found:
            if test_small_num < test_big_num:
                test_small_num = small_num * i
                i += 1
            elif test_small_num == test_big_num:
                i -= 1
                lcm.append("the lowest common multiple is "+str(test_small_num))
                lcm.append(""+str(small_num)+" X "+str(i)+" is "+str(test_small_num))
                lcm.append(""+str(big_num)+" X "+str(a)+" is "+str(test_small_num))
                lcm_not_found = False
            elif test_small_num > test_big_num:
                while test_small_num > test_big_num:
                    test_big_num = big_num * a
                    a += 1
        return test_small_num
    def lowestForm(numerator,denominator):
        final_nums = []
        if numerator > denominator:
            num = denominator
        elif denominator > numerator:
            num = numerator
        elif denominator == numerator:
            num = numerator
        for i in range(num + 1):
            if i == 0 or i == 1:
                pass
            else:
                lower1 = numerator / i
                lower2 = denominator / i
                if len(str(lower1)) <= len(str(numerator)) + 2 and len(str(lower2)) <= len(str(denominator)) + 2:
                    lower1 = str(lower1)
                    lower2 = str(lower2)
                    if int(lower1[-1]) == 0 and int(lower2[-1]) == 0:
                       final_nums.append([lower1,lower2])
                    else:
                        pass
        if len(final_nums) == 0:
            return [numerator,denominator]
        else:
            return [final_nums[-2],final_nums[-1]]
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