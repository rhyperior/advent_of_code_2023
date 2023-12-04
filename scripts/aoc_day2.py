def get_sum_of_possible_game_ids(input=None):
    blue_max , red_max, green_max = 14, 12, 13

    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')
    
    sum = 0
    for line in all_input:
        id, games = line.split(':')
        
        id = int(id.strip().split(" ")[1])



        for game in games.strip().split(';'):
            for color in game.strip().split(','):
                number, color = color.strip().split(' ')
                number = int(number)

                if color == 'blue' and number > blue_max:
                    id = 0
                    break
                elif color == 'red' and number > red_max:
                    id = 0
                    break
                elif color == 'green' and number > green_max:
                    id = 0
                    break
        
        sum += id

    return sum

def get_power_of_possible_game_ids(input=None):
    

    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')
    
    sum = 0
    for line in all_input:
        id, games = line.split(':')
        
        id = int(id.strip().split(" ")[1])


        blue_max , red_max, green_max = 0, 0, 0
        for game in games.strip().split(';'):
            

            for color in game.strip().split(','):
                number, color = color.strip().split(' ')
                number = int(number)

                if color == 'blue' and number > blue_max:
                    blue_max = number
                elif color == 'red' and number > red_max:
                    red_max = number
                elif color == 'green' and number > green_max:
                    green_max = number
        
        product = red_max * blue_max * green_max
        sum += product

    return sum


if __name__=="__main__":
    input = './sample/sample2.txt'
    input = './input/advent_of_code_day2_input.txt'

    res = get_sum_of_possible_game_ids(input)
    res = get_power_of_possible_game_ids(input)

    print(res)
