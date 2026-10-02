# Author: Salah Eddine | Python Developer (in progress)
# Stack: Python  / HTML / CSS / JS |  PHP / SQL
# Motto: I don't let AI code for me, I suffer to understand.
# 
# Dear Programmer:
# When I wrote this code, only God and I knew how it worked.
# Now, only God knows it!
#
# Therefore, if you are trying to optimize this routine
# and it fails (most surely), please increase this counter
# as a warning for the next person:
# 
# total_hours_wasted_here = 173 ITS WOKED NEW FINALY







print("===================| TO==DO==LIST |===================") #hhh just semple designe
print("    ==================|(●'◡'●)|===================")
taskes=[] # the most important list it has all taskes
while True : # main while
    # menu
  print("                  +================+")
  print("                  ||1  Add task   ||")
  print("                  +================+")
  print("                  ||2  View task  ||")
  print("                  +================+")
  print("                  ||3  Mark task  ||")
  print("                  +================+")
  print("                  ||4  Delete task||")
  print("                  +================+")
  print("                  ||5 Save & Exite||")
  print("                  +================+") 

  chouse=(int(input("        Choose  :... "))) # input taskes
  if chouse>5 or chouse <=0 :
       print("this number is not anvariable in the above menu")
  elif chouse == 1:
      while True:
         task=input("    weaite the taske : ")
         taskes.append(task)
         more= input("dio need to raite anhother task y/n ; ").strip().upper()
         if more== "N" :
          break
# print all taskes
            
  elif chouse == 2 :
   print("                 =====| your taskes |====")
   print("                   ===||(～￣▽￣)～||===")
   print(taskes)
   
# marke task as done ✅
  elif chouse == 3:
    while True:
      if taskes :
       for i , task in enumerate(taskes):
         print(f"{i+1} , {task}")
      try:
           task_num=int(input("enter number by the done task : ")) -1
           if 0<= task_num <len(taskes): 
               taskes[task_num] += " ✅"
               print(f"the task{task_num +1} was done secsufuly ✅")
           else :
               print("the number is false ")
      except ValueError:
          print("enter true number")
          
      more1= input("dio need to mark anhother task y/n ; ").upper()
      if more1== "N":
             break
            
# delet taskes by the index using fonction "pop"         
  elif chouse == 4:
     print("==================================================")
     print("==================================================")
     
     num_delet_task=int(input("entre num of the task you want to delet it ; ")).strip() -1
     if 0<= num_delet_task <len(taskes) :
               taskes.pop(num_delet_task)
     print("==================================================")
     print("==================================================")
     
# save 
  elif chouse == 5:
        taskesss= taskes
        taskesss= "|".join(taskes)
        with open ("Taskes.txt" , "a" , encoding="utf-8") as f:
             f.write(taskesss + "\n")
        print("your taskes was saved sucsifily ✅")
        print("===========Goodbye!===================")
        break

             
             