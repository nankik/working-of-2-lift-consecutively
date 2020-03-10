#2 lifts:present location(l1,l2)
#6 floors(0,1,2,3,4,5)
#last used lift(l)
#direction(d),    d=0 -->up

def move(lift,begi,end,floor=[]):
      if begi>end:
            motion=-1
      else:
            motion=1
      from time import sleep
      print(lift," is on the way")
      for i in range(begi+motion,end+motion,motion):
            print("x")
            sleep(3)
            begi=i
            print(lift,"=",i)
            if i in floor:
                  print("On requested floor",i)
      print(lift," is here")

c=1
n=0
l1=0
l2=0
l=1
while(c): #calling lift
      while(True):
            try:
                  f=int(input("Enter floor number:"))
                  if f not in range(0,6):
                        print("Invalid input")
                        continue
                  else:
                        break
            except:
                  print("Invalid input")
      if f==0:
            ch="u"
      elif f==5:
            ch="d"
      else:
            while(True):
                  try:
                        ch=input("Up(U) or Down(D)")
                        if ch not in {"u","U","D","d"}:
                              print("Invalid input")
                              continue
                        else:
                              break
                  except:
                       print("Invalid input")
                        continue 
        
      if l1>l2:#case 1
            if f>l1:#called from higher floor
                  move("L1",l1,f)
                  l=1
                  l1=f
            elif f<l2:#called from lower floor
                  move("L2",l2,f)
                  l=2
                  l2=f
            elif ch in {"u","U"}:#called from a central floor for up
                  move("L2",l2,f)
                  l2=f
                  l=2
            else:#called from a central floor for down
                  move("L1",l1,f)
                  l1=f
                  l=1
                  
      elif l2>l1:#case 2
            if f>l2:#called from higher floor
                  move("L2",l2,f)
                  l=2
                  l2=f
            elif f<l1:#called from lower floor
                  move("L1",l1,f)
                  l=1
                  l1=f
            elif ch in {"u","U"}:#called from a central floor for up
                  move("L1",l1,f)
                  l1=f
                  l=1
            else:#called from a central floor for down
                  move("L2",l2,f)
                  l2=f
                  l=2
      elif f==l1:
            l=1
      elif f==l2:
            l=2
      else:#last case l1=l2
            if l==1:
                  move("L1",l1,f)
                  l1=f
                  l=1
            else:
                  move("L2",l2,f)
                  l2=f
                  l=2

      floor=[]
      #inside lift
      print("\t\tINSIDE LIFT L",l)
      try:
            while(1):
                  while(True):
                        try:
                              x=int(input("Enter floor number:"))
                              if x not in range(0,6):
                                    print("Invalid input")
                                    continue
                              else:
                                    floor.append(x)
                                    break
                        except:
                              print("Invalid input")
      except:
            pass

      if l==1:#in l1
            if ch in ["u","U"]:
                  f=max(floor)
                  if f<l1:
                        f=min(floor)
            else:
                  f=min(floor)
                  if f>l1:
                        f=max(floor)
            move("L1",l1,f,floor)
            l1=f
            
      else:#in l2
            if ch in ["u","U"]:
                  f=max(floor)
                  if f<l2:
                        f=min(floor)
            else:
                  f=min(floor)
                  if f>l2:
                        f=max(floor)
            move("L2",l2,f,floor)
            l2=f
            

      try:
            c=int(input("\nPress 1 if you wish to continue"))
      except:
            c=0
      print("\n")
      
