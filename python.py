t = int(input())
for i in range(t):
  y,m,z,x = map(int,input().split())
  try:
    print((y*m)/(z*x))
  except:
    print("Don't enter the zero and negatives")
