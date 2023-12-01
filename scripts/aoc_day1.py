import re

def return_sum_of_calibration_values(input=None):
    
    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')
    
    sum = 0
    for line in all_input:
        left_digit = re.search(r'\d', line)
        right_digit = re.search(r'\d', line[::-1])

        if left_digit:
            left_digit = left_digit.group(0)
        else:
            left_digit = '0'

        if right_digit:
            right_digit = right_digit.group(0)
        else:
            right_digit = '0'
        sum += int(left_digit+right_digit)
    
    return sum

def return_sum_by_words(input=None):
    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')
    
    words_digit_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine':'9'}

    sum = 0
    for line in all_input:
        all_digits_forward = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line)
        all_digits_backward = re.findall(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line[::-1])

        first_digit = 0
        last_digit = 0
        if all_digits_forward:
            first_digit = words_digit_map.get(all_digits_forward[0], None)
            if not first_digit:
                first_digit = all_digits_forward[0]
        if all_digits_backward:
            last_digit = words_digit_map.get(all_digits_backward[0][::-1], None)
            if not last_digit:
                last_digit = all_digits_backward[0]

        term =  int(first_digit+last_digit)
        print(term, line)
        sum += term
    return sum

if __name__=="__main__":
    input = './sample/sample.txt'
    input = './sample/sample_1_b.txt'
    input = './input/advent_of_code_day1_input.txt'
    res = return_sum_of_calibration_values(input)
    print(res)
    res = return_sum_by_words(input)
    print(res)
    