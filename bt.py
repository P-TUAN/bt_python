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

#bài tập 6
def xuat():
    t = int(input("Nhập: "))
    if 0 < t <= 100:
        for i in range(1, t + 1):
            a = input()
            print(f"Test{i}:" )
            print(a.replace("TNMT","BBBB").replace("Relax","  ").replace("Sleeping","  "))
           
       
xuat()

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



          
          
         
