print("sayı giriniz: ")
x , k = map(int,input().split(" "))
print("polinomun sonucu olacak sayı: ")
k = (int)(input())
y = k
i = 0
toplam = 0
for i in range(y):
        toplam += (x ** i)
        i += 1
        print(toplam)

if toplam == k:
    print(True)
else:
    print(False)

# x, k = map(int,input().split())
# p= eval(input())
# if(p == k):
#     print("True")
# else:
#     print("False")

