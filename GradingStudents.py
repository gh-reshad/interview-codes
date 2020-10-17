import numpy as np
import os


def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            grades[i] = grades[i]
        
        else:
            if grades[i] % 10 < 5:
                num = (int(grades[i] / 10)) * 10 + 5
                if num - grades[i] < 3:
                    grades[i] = num
              
            
            else:
                num = (int(grades[i] / 10) + 1) * 10
                if num - grades[i] < 3:
                    grades[i] = num
               
    
    return grades


studentGrades = [73, 67, 38, 33]
result = gradingStudents(studentGrades)
print(result)



