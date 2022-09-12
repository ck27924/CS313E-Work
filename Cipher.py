
import math
import sys
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
  a= len(strng)
  while int(math.sqrt(len(a))) % 1 != 0:
    strng += "*"
  k = int (math.sqrt(len(strng)))

  index=0
  table= [[0 for i in range(k)] for j in range(k)] #create an empty table
  for i in range(len(table)-1, -1, -1):
    for j in range (len(table)): 
      table[j][i]= strng[index]
      index +=1

  newList=[] 
  for i in range(len(table)): #traverses through the table and adds the encrypted string in to a string
    for j in range(len(table)):
      if table[i][j] != "*":
        newList.append(table[i][j])
        encryptStr= "".join(newList)

  return (encryptStr)

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
	pass

def main():
  input=sys.stdin.read() #reads an input of integers on separate lines
  split_input=input.split("\n") #adds the input into a single line list
  strP= split_input[1]
  strQ= split_input[2]

  print (encrypt(strP))   # encrypts and prints the string P
  print (decrypt(strQ)) # decrypts and prints the string P
  # read the strings P and Q from standard input

if __name__ == "__main__":
  main()


