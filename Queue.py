#coding task, set to work with lists.

# based on a queue for a ladies toilet. Task instructions in comments.

# 5 women initially waiting
line = ["Claire", "Hannah", "Pippa", "Laura", "Christine"]        
print(line[0])
print(line[1])
print(line[2])
print(line[3])
print(line[4])
print("")

# Jenny joins front of line
line.insert(0, "Jenny")     	
print(line[0])
print(line[1])
print(line[2])
print(line[3])
print(line[4])
print(line[5])
print("")

# woman third in line leaves
line.pop(2)    		
print(line[0])
print(line[1])
print(line[2])
print(line[3])
print(line[4])
print("")

# Alice joins the line
line.append("Alice")		
print(line[0])
print(line[1])
print(line[2])
print(line[3])
print(line[4])
print(line[5])
