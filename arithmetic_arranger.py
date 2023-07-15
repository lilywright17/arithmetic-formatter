def arithmetic_arranger(problems, solutions=False):

  first_line = ""
  second_line = ""
  third_line = ""
  fourth_line = ""
  
 #error if more tham 5 problems "Error: Too many problems."
  if (len(problems) > 5):
    return "Error: Too many problems."
  
  #split strings into numbers and operator
  for problem in problems:
    first_number, operator, second_number = problem.split(" ")
    
    
  #each number must be max 4 digits
    if len(first_number) > 4 or len(second_number) > 4:
      return "Error: Numbers cannot be more than four digits."
    
  #only addition or subtraction
    if not (operator == '+' or operator == '-'):
      return "Error: Operator must be '+' or '-'."
      
  #check that each number contains only digits
    if second_number.isnumeric() == False or first_number.isnumeric() == False:
      return "Error: Numbers must only contain digits."
    
  #single space between the operator and the longest of the two operands 
    problem_length = max(len(first_number) + 2, len(second_number) + 2)
    first = " " * (problem_length - len(first_number)) + first_number
    second = operator + " " * (problem_length - 1 - len(second_number)) + second_number
    third = "-" * problem_length
    fourth = " " * (problem_length - len(str(eval(problem)))) + str(eval(problem)) 

    first_line += first + " " * 4
    second_line += second + " " * 4
    third_line += third + " " * 4
    fourth_line += fourth + " " * 4

  first_line = first_line.rstrip()
  second_line = second_line.rstrip()
  third_line = third_line.rstrip()
  fourth_line = fourth_line.rstrip()
    
  if solutions:
    return f"{first_line }\n{second_line}\n{third_line}\n{fourth_line}"
  else:
    return f"{first_line }\n{second_line}\n{third_line}"
