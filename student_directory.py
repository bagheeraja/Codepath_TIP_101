def student_directory(student_names: list[str]) -> dict[str,int]:
    #create and empty dictionary
    # # iterate through the list of students
    # assign a numerical value based on index + 1 as they value for the name key
    # use i to track the index and base numerical assignments on i
    student_table = {}

    for i, name in enumerate(student_names, start=1):
        student_table[name] = i
    return student_table

def student_directory_dict_comp(student_names: list[str]) -> dict[str,int]:
    return {name: i for i, name in enumerate(student_names, start=1)}

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
student_names2 = ["Charlie Parker", "Miles Davis", "Louis Prima", "Fats Domino", "Benny Goodman"]
                 
print(student_directory(student_names))
print(student_directory_dict_comp(student_names2))