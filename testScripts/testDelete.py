test_list = [{"id" : 1, "data" : "HappY"}, 
             {"id" : 2, "data" : "BirthDaY"}, 
             {"id" : 3, "data" : "Rash"}] 
  
# printing original list  
print ("The original list is : " + str(test_list)) 
  
# using filter() + lambda 
# to delete dictionary in list 
res = list(filter(lambda i: i['id'] != 2, test_list)) 
  
# printing result 
print ("List after deletion of dictionary : " +  str(res)) 