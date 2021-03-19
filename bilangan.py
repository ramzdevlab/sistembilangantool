print('\nNUMERAL SYSTEM TOOL')
print('|----  BY FAHMI  ----|\n')
print('TOOL MENU :\n',
      '[1] NUMBER CONVERTION\n',
      '[2] ARITMATICS NUMBER\n')

inputmenu = input('SELECT MENU : ')

if int(inputmenu) == 1 :
      
      print('TOOL MENU :\n',
      '[1] DECIMAL\n',
      '[2] BINARY\n',
      '[3] OCTAL\n',
      '[4] HEXADECIMAL\n')
      
      menu = input('SELECT ONE : ')
      menuc = int(menu)

      if menuc == 1 :
            dec = input('ENTER DECIMAL NUMBER : ')
            hexs = hex(int(dec))[2:]
            binar = bin(int(dec))[2:]
            octal = oct(int(dec))[2:]
            print('\n=== RESULTS === \n')
            print('[1] BINARY : ')      
            print(binar)
            print('\n')
            print('[2] OCTAL : ')      
            print(octal)
            print('\n')
            print('[3] HEXADECIMAL : ')      
            print(hexs)
            print('\n')

      elif menuc == 2 :
            binar = input('ENTER BINARY NUMBER : ')
            hexs = hex(int(binar, 2))[2:]
            dec = int(binar, 2)
            octal = oct(int(binar, 2))[2:]

            print('\n=== RESULTS === \n')

            print('[1] DECIMAL : ')      
            print(dec)
            print('\n')
            print('[2] OCTAL : ')  
            print(octal)
            print('\n')
            print('[3] HEXADECIMAL : ')      
            print(hexs)
            print('\n')

      elif menuc == 3 :
            octal = input('ENTER OCTAL NUMBER : ')
            hexs = hex(int(octal, 8))[2:]
            dec = int(octal, 8)
            binar = bin(int(octal, 8))[2:]

            print('\n=== RESULTS === \n')

            print('[1] DECIMAL : ')      
            print(dec)
            print('\n')
            print('[2] BINARY : ')  
            print(binar)
            print('\n')
            print('[3] HEXADECIMAL : ')      
            print(hexs)
            print('\n')
      elif menuc == 4 :
            hexs = input('ENTER HEXADECIMAL NUMBER : ')
            octa = oct(int(hexs, 16))[2:]
            dec = int(hexs, 16)
            binar = bin(int(hexs, 16))[2:]

            print('\n=== RESULTS === \n')

            print('[1] DECIMAL : ')      
            print(dec)
            print('\n')
            print('[2] BINARY : ')  
            print(binar)
            print('\n')
            print('[3] OCTAL : ')      
            print(octa)
            print('\n')


            
elif int(inputmenu) == 2 :
      print(' [1] BINARY\n',
      '[2] OCTAL\n',
      '[3] HEXADECIMAL\n');

      menu = input('Select Menu :');
      menuc =  int(menu)

      #function-------------------------------
      def Aritmatics(menuapp, menuarit):
            if menuarit == 1 :
                        input1 = input('Enter First Number : ')
                        input2 = input('Enter Second Number : ')
                        if menuapp == 1 :
                              jumlahbiner = int(input1, 2) + int(input2, 2)
                              print('\nResult : ', bin(jumlahbiner)[2:])
                        elif menuapp == 2 :
                              jumlahoctal = int(input1, 8) + int(input2, 8)
                              print('\nResult : ', oct(jumlahoctal)[2:])
                        elif menuapp == 3 :
                              jumlahhexa = int(input1, 16) + int(input2, 16)
                              print('\nResult : ', hex(jumlahhexa)[2:])

            elif menuarit == 2 :
                        input1 = input('Enter First Number : ')
                        input2 = input('Enter Second Number : ')
                        if menuapp == 1 :
                              kurangbiner = int(input1, 2) - int(input2, 2)
                              print('\nResult : ', bin(kurangbiner)[2:])
                        elif menuapp == 2 :
                              kurangoctal = int(input1, 8) - int(input2, 8)
                              print('\nResult : ', oct(kurangoctal)[2:])
                        elif menuapp == 3 :
                              kuranghexa = int(input1, 16) - int(input2, 16)
                              print('\nResult : ', hex(kuranghexa)[2:])
            elif menuarit == 3 :
                        input1 = input('Enter First Number : ')
                        input2 = input('Enter Second Number : ')
                        if menuapp == 1 :
                              kalibiner = int(input1, 2) * int(input2, 2)
                              print('\nResult : ', bin(kalibiner)[2:])
                        elif menuapp == 2 :
                              kalioctal = int(input1, 8) * int(input2, 8)
                              print('\nResult : ', oct(kalioctal)[2:])
                        elif menuapp == 3 :
                              kalihexa = int(input1, 16) * int(input2, 16)
                              print('\nResult : ', hex(kalihexa)[2:])
            elif menuarit == 4 :
                        input1 = input('Enter First Number : ')
                        input2 = input('Enter Second Number : ')
                        if menuapp == 1 :
                              bagibiner = int(input1, 2) // int(input2, 2)
                              print('\nResult : ', bin(bagibiner)[2:])
                        elif menuapp == 2 :
                              bagioctal = int(input1, 8) // int(input2, 8)
                              print('\nResult : ', oct(bagioctal)[2:])
                        elif menuapp == 3 :
                              bagihexa = int(input1, 16) // int(input2, 16)
                              print('\nResult : ', hex(bagihexa)[2:])



      if menuc == 1 :
            print(' [1] Perjumlahan\n','[2] Pengurangan\n','[3] Perkalian\n' ,'[4] Pembagian\n ')
            menu2 = input('Select Aritmatic Menu : ')
            menuc2 = int(menu2)
            Aritmatics(menuc, menuc2)
            
      if menuc == 2 :
            print(' [1] Perjumlahan\n','[2] Pengurangan\n','[3] Perkalian\n' ,'[4] Pembagian\n ')
            menu2 = input('Select Aritmatic Menu : ')
            menuc2 = int(menu2)
            Aritmatics(menuc, menuc2)
      if menuc == 3 :
            print(' [1] Perjumlahan\n','[2] Pengurangan\n','[3] Perkalian\n' ,'[4] Pembagian\n ')
            menu2 = input('Select Aritmatic Menu : ')
            menuc2 = int(menu2)
            Aritmatics(menuc, menuc2)
      

