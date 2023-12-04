import re

def return_sum_of_engine_parts(input=None):
    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')
    
    all_lines = []
    result = []
    set_char = set()
    for line in all_input:
        line = line.strip()
        
        for i in line:
            set_char.add(i)

        entries = re.findall(r'\d+|[#@\$\^\*\(\)\+\-\.\%\/\\\=\&]', line)

        parsed_row = []
        for value in entries:
            if re.search('\d+', value):
                parsed_row.append(int(value))
                parsed_row.extend(['.']*(len(value)-1))

            elif re.search(r'[#@\$\^\*\(\)\+\-\%\/\\\=\&]', value):
                parsed_row.append('*')
            else:
                parsed_row.append('.')
        all_lines.append(parsed_row)

    for row_index, row in enumerate(all_lines):
        for col_index, col in enumerate(row):
            if type(col) is int:
                print()
                for y in (-1,0,1):
                    length = len(str(col))
                    for x in range(-1, length+1):
                        try:
                            if (row_index+y) < 0 or col_index+x < 0:
                                pass
                            elif all_lines[row_index+y][col_index+x] == '*':
                                result.append(col)
                                break
                        except IndexError:
                            pass
    return sum(result)

def return_sum_of_gear_ratios(input=None):
    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')
    
    all_lines = []

    for line in all_input:
        line = line.strip()
        
        entries = re.findall(r'\d+|[#@\$\^\*\(\)\+\-\.\%\/\\\=\&]', line)

        parsed_row = []
        for value in entries:
            if re.search('\d+', value):
                parsed_row.append(int(value))
                parsed_row.extend(['.']*(len(value)-1))

            elif re.search(r'[#@\$\^\*\(\)\+\-\%\/\\\=\&]', value):
                parsed_row.append('*')
            else:
                parsed_row.append('.')
        all_lines.append(parsed_row)

    special_char_map = dict()

    for row_index, row in enumerate(all_lines):
        for col_index, col in enumerate(row):
            if type(col) is int:
                print()
                for y in (-1,0,1):
                    length = len(str(col))
                    for x in range(-1, length+1):
                        try:
                            if (row_index+y) < 0 or col_index+x < 0:
                                pass
                            elif all_lines[row_index+y][col_index+x] == '*':
                                if special_char_map.get((row_index+y, col_index+x), None):
                                    special_char_map.get((row_index+y, col_index+x)).append(col)
                                else:
                                    special_char_map[(row_index+y, col_index+x)] = [col]
                        except IndexError:
                            pass
    result = 0
    for key, value in special_char_map.items():
         if len(value) == 2:
             result += value[0]*value[1]
    return result


if __name__=="__main__":
    input = './sample/sample3.txt'
    input = './input/advent_of_code_day3_input.txt'

    # res = return_sum_of_engine_parts(input)
    res = return_sum_of_gear_ratios(input)
    print(res)