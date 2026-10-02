# dict={
#   "name":"aman",
#   "cgpa":7.9,
#   "marks":[85,90,95],
# }
# dict ["name"]="sharma "
# print(len(dict))
# print(dict["name"])
# print(dict["cgpa"])
# print(dict["marks"]) 
# dict["surname"]="kumar" 
# print(dict);
# print(dict.keys())
# print(dict.values()) 




#---------------nested dictionary----------------
student={
  "name":"aman",
  "cgpa":7.9,
  "subject":{
"physiscs":84,
"math":90,
"chemistry":95
  }
}

print(student["subject"]["math"])