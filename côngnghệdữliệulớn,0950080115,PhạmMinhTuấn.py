#bài tập 1
def xuat():
  t = int(input("Nhập: "))
  if 0 < t <= 100:
    for i in range (1,t+1):
        c=input()
        print(f"Test{i}:\n{c.title()}")

   

xuat()

#bài tập 2
def xuat():
  t = int(input("Nhập: "))
  if 0 < t <= 100:
    for i in range (1,t+1):
        str1=input()
        nguyenam = 0
        phuam = 0
        str1.lower()
        for n in str1:
         if(n == 'a' or n == 'e' or n == 'i' or i == 'o' or n == 'u'):
          nguyenam = nguyenam + 1
        else:
         phuam = phuam + 1
         print(f"Test{i}:\n{nguyenam} \n{phuam}" )
                    

xuat()

##bài tập 3

def xuat():
  t = int(input("Nhập: "))
  if 0 < t <= 100:
    for i in range (1,t+1):
         str=input()
         print(f"Test{i}:" ,str.count(" "))
       

xuat()

#bài tập 4

def xuat():
    t = int(input("Nhập số lượng các dòng: "))
    if t > 0 and t <= 100:
        for i in range(1, t + 1):
            str_word = input("Nhập chữ: ")
            print(str_word.replace("\t", " "))

            
xuat()

#bài tập 6

def xuat(s1, s2, s3):
    print(s1.replace(s2, s3))


t = int(input("Nhập: "))
if 0 < t <= 100:
    for i in range(t):
        s1 = input("Nhập chuỗi: ")
        s2 = input("nhập từ cũ: ")
        s3 = input("Nhập từ mới: ")
        print(f"test {i + 1}:", end="\n")
        xuat(s1, s2, s3)

#bài tập 7

def xuat():
    t = int(input("Nhập: "))
    if 0 < t <= 100:
        for i in range(1, t + 1):
            nhap = input()
            tucu = nhap.split()
            tumoi = []
            j = 0

            for ii in range(len(tucu)):
                if tucu[ii] not in tumoi:
                    tumoi.insert(j, tucu[ii])
                    j = j + 1

            n = ""
            for ii in range(len(tumoi)):
                n = n + tumoi[ii] + " "

            print(f"Test{i}: {n}")


xuat()

#bài 10

def xuat():
    t = int(input("Nhập: "))
    if 0 < t <= 100:
        for i in range(1, t + 1):
            c = input()
            print(f"Test{i}:\n", c.strip().title().replace("\t", " ").replace(".",". ").replace(" .",".").replace("!",".").replace("?","."))


xuat()


          
          
         
