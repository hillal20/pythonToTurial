# myFile = open('file.txt')
# print(myFile)

# for line in myFile:
#   print(line.rstrip())
# myFile.close()

# myFile.seek(0) ## we send the cursor to the beginning of the line 
###############################

# myFile.seek(10)  ## read the text partially 
# text = myFile.read(20)
# print(text)

# myFile.close()

#################
with open('file.txt') as myFile2:
  lines = myFile2.readlines()
  for l in lines:
        print(l.rstrip())


# myFile2.close()
