import re

def return_scratch_cards_total_winning_points(input):
    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')

        total_points = 0
    for line in all_input:
        winning_numbers = line.split('|')[0].split(':')[1].strip()
        winning_numbers = re.sub('\s+', ' ', winning_numbers).strip().split(' ')
        card_numbers = line.split('|')[1]
        card_numbers = re.sub('\s+', ' ', card_numbers).strip().split(' ')

        winning_numbers = set(winning_numbers)
        card_numbers = set(card_numbers)

        points = len(card_numbers.intersection(winning_numbers))

        if points > 0:
            total_points += pow(2, (len(card_numbers.intersection(winning_numbers))-1))
    
        
    return total_points

def return_total_scratch_cards(input):
    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')

        total_points = 0
    
    total_no_of_cards_map = dict()
    total_cards = len(all_input)

    for card_no, line in enumerate(all_input, 1):
        if not total_no_of_cards_map.get(card_no, None):
            total_no_of_cards_map[card_no] = 1
        card_count = total_no_of_cards_map.get(card_no)

        winning_numbers = line.split('|')[0].split(':')[1].strip()
        winning_numbers = re.sub('\s+', ' ', winning_numbers).strip().split(' ')
        card_numbers = line.split('|')[1]
        card_numbers = re.sub('\s+', ' ', card_numbers).strip().split(' ')

        winning_numbers = set(winning_numbers)
        card_numbers = set(card_numbers)

        points = len(card_numbers.intersection(winning_numbers))

        for i in range(1, points+1):
            if card_no+i > total_cards:
                break
            elif card_no+i in total_no_of_cards_map:
                total_no_of_cards_map[card_no+i] += card_count
            else:
                total_no_of_cards_map[card_no+i] = 1 + card_count
        # print()

    res = 0
    for card_count in total_no_of_cards_map.values():
        res += card_count
        
    
        
    return res

def calculate_cuumulative_sum():
    return None

if __name__=="__main__":
    input = './sample/sample4.txt'
    input = './input/advent_of_code_day4_input.txt'

    # res = return_scratch_cards_total_winning_points(input)
    res = return_total_scratch_cards(input)
    print(res)