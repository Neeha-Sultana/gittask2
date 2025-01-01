'''
a, b, c, d = map(int, input().split(' '))
if a-c==0:
    print("YES")
    quit()
if d-b==0:
    print("NO")
    quit()
if ((a-c)%(d-b)==0 and (a-c)//(d-b)>=0):
    print("YES")
    quit()
print("NO")



def kangaroo(a, b, c, d):
    for n in range(10000):
        if((a+b)==(c+d)):
            print("YES")
        a+=b
        c+=d
    else:
        print("NO")

if __name__ == '__main__':

    x1,v1,x2,v2 = map(int, input().split(' '))
    result = kangaroo(x1, v1, x2, v2)



bl = False
x1,v1,x2,v2 = map(int, input().split(' '))
if ((x1>x2 and v1>v2) or (x1<x2 and v1<v2)):
  print("NO")
else:
  for i in range(100):
    x1 = x1 + v1
    x2 = x2 + v2
    if x1 == x2 :
      bl = True
      break
      
  if bl == True:
    print("YES")
  else:
    print("NO")



def kang_jump(x1,v1,x2,v2):
    if ((x1>x2 and v1>v2) or (x1<x2 and v1<v2)):
        print("NO")
    else:
        for i in range(100):
            x1 = x1 + v1
            x2 = x2 + v2
            if x1 == x2 :
                bl = True
                break
      
        if bl == True:
            print("YES")
        else:
            print("NO")

a,b,c,d = map(int, input().split(' '))
kang_jump(a,b,c,d)




def kangaroo_jump(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    else:
        jumps = (x2 - x1) / (v1 - v2)
        if jumps.is_integer() and jumps >= 0:
            return "YES"
        else:
            return "NO"


# Example usage
x1, v1, x2, v2 = map(int, input("Enter x1, v1, x2, v2: ").split())
result = kangaroo_jump(x1, v1, x2, v2)
print(result)
'''

def kang_jump(x1,v1,x2,v2):
    b1=False
    if ((x1>x2 and v1>v2) or (x1<x2 and v1<v2)):
        print("NO")
    else:
        for i in range(100):
            x1 = x1 + v1
            x2 = x2 + v2
            if x1 == x2 :
                bl = True
                break
      
        if bl == True:
            print("YES")
        else:
            print("NO")

a,b,c,d = map(int, input().split(' '))
kang_jump(a,b,c,d)
            print("NO")

a,b,c,d = map(int, input().split(' '))
kang_jump(a,b,c,d)

