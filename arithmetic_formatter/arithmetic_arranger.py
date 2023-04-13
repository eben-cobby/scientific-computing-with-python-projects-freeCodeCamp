def arithmetic_arranger(problems, show_solution=False):
    # check for max of 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # initialize empty string for each line
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""

    for problem in problems:
        # split problem into operands and operator
        first_operand, operator, second_operand = problem.split()

        # check for errors
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not (first_operand.isdecimal() and second_operand.isdecimal()):
            return "Error: Numbers must only contain digits."
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        # determine the length of the longest operand and add padding
        max_operand_length = max(len(first_operand), len(second_operand))
        formatted_first_operand = first_operand.rjust(max_operand_length + 2)
        formatted_second_operand = operator + second_operand.rjust(
            max_operand_length + 1)

        # calculate the result and format the solution line
        result = str(eval(problem))
        formatted_result = result.rjust(max_operand_length + 2)

        # determine the length of the longest line
        max_length = max(len(formatted_first_operand),
                         len(formatted_second_operand), len(formatted_result))

        # add formatted lines to the empty strings
        line_1 += formatted_first_operand + "    "
        line_2 += formatted_second_operand + "    "
        line_3 += "-" * max_length + "    "
        line_4 += formatted_result + "    " if show_solution else ""

    # concatenate the formatted lines
    arranged_problems = line_1.rstrip() + "\n" + line_2.rstrip() + "\n" + line_3.rstrip()
    if show_solution:
        arranged_problems += "\n" + line_4.rstrip()

    return arranged_problems
