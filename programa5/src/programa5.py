# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":

 A = int(raw_input ("Escriba su calificacion"))
 if A >= 9.5:
  print ("A+")
 elif A >= 9.0 and A <= 9.4:
  print ("A-")
 elif A >= 8.5 and A <= 8.9:
  print ("B+")
 elif A >= 8.0 and A <= 4.4:
  print ("B-")
 elif A < 4.3:
  print ("reprobado")   
  