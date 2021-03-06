## based on: https://www.w3schools.com/python/python_ref_string.asp

## prompts user to input a string; counts elements in the string and groups elements by this categories: 

## * number of elements (total & unique)
## * number of non-alphanumeric characters (total & unique)
## * number of alphabetical characters (total & unique)
## * number of numeric characters (total & unique)
## * number of uppercase letters (total & unique)
## * number of lowercase letters (total & unique)
## * total for each element counted 

def string():
    total_elements = input("Paste a string of text here! ")
    
    print()
    print("##########################")
    print()
    
    print("Sorted elements:", sorted(total_elements))   
    print()
    print("Number of elements:", len(total_elements))
    nonalnum = int(len(total_elements)) - int(sum(map(str.isalpha, total_elements))) - int(sum(map(str.isnumeric, total_elements)))
    print("Number of non-alphanumeric characters:", nonalnum)          
    print("Number of alphabetical characters:", sum(map(str.isalpha, total_elements)))
    print("Number of numeric characters:", sum(map(str.isnumeric, total_elements)))
    print()
    print("Number of uppercase letters:", sum(map(str.isupper, total_elements)))
    print("Number of lowercase letters:", sum(map(str.islower, total_elements))) 
    print()
    
    unique_elements = []
    for char in total_elements[::]:
        if char not in unique_elements:
            unique_elements.append(char)
    
    for i in sorted(unique_elements): 
        print ("Number of '", i, "': ", total_elements.count(i), sep="")
    
    print()
    print("##########################")
    print()  
        
    print("Sorted unique elements:", sorted(unique_elements))
    print()    
    print("Number of unique elements:", len(unique_elements))
    nonalnum = int(len(unique_elements)) - int(sum(map(str.isalpha, unique_elements))) - int(sum(map(str.isnumeric, unique_elements)))
    print("Number of unique non-alphanumeric characters:", nonalnum)          
    print("Number of unique alphabetical characters:", sum(map(str.isalpha, unique_elements)))
    print("Number of unique numeric characters:", sum(map(str.isnumeric, unique_elements)))
    print()
    print("Number of unique uppercase letters:", sum(map(str.isupper, unique_elements)))
    print("Number of unique lowercase letters:", sum(map(str.islower, unique_elements))) 
    print()
       
string()