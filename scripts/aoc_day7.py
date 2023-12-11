from collections import Counter

def return_sum_of_card_winning_bids(input = None):
    

    rank_map = dict()

    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')
         
        line_count = 1
    for hand in all_input:
        print(line_count)
        line_count +=1 
        count = len(all_input)
        cards, bid = hand.strip().split(' ')
        for second_hand in all_input:
            second_cards, bids_2 = second_hand.split(' ')
            if second_cards == cards:
                continue
            else:
                comparison = find_relative_order(cards, second_cards)

                if comparison < 0:
                    count -= 1
        rank_map[(cards, int(bid))] = count
    
    res = 0
    for key, value in rank_map.items():
        res += key[1]* value

    return res

def return_sum_of_card_winning_bids_joker_switch(input = None):
    

    rank_map = dict()

    with open(input, 'r+') as f:
        all_input = f.read().strip().split('\n')
         
        line_count = 1
    for hand in all_input:
        print(line_count)
        line_count +=1 
        count = len(all_input)
        cards, bid = hand.strip().split(' ')
        for second_hand in all_input:
            second_cards, bids_2 = second_hand.split(' ')
            if second_cards == cards:
                continue
            else:
                comparison = find_relative_order(cards, second_cards)

                if comparison < 0:
                    count -= 1
        rank_map[(cards, int(bid))] = count
    
    res = 0
    for key, value in rank_map.items():
        res += key[1]* value

    return res


def find_relative_order(card_a, card_b):
    card_rank_map = {'A': 1, 'K': 2, 'Q':3, 'J': 13,  'T':4, '9': 5, '8': 6, '7': 7, '6':8, '5': 9, '4': 10, '3': 11, '2': 12}
    hand_rank_a = get_card_type_joker_switch(card_a)
    hand_rank_b = get_card_type_joker_switch(card_b)

    if hand_rank_a > hand_rank_b:
        return 1                        # First Hand is stronger.
    elif hand_rank_a < hand_rank_b:
        return -1                       # Second Hand is stronger.
    else:
        for index, _ in enumerate(card_a):
            if card_rank_map[card_a[index]] < card_rank_map[card_b[index]]:
                return 1
            elif card_rank_map[card_a[index]] > card_rank_map[card_b[index]]:
                return -1
        return 0
    
def get_card_type_joker_switch(card):
    card_count = Counter(card)

    if len(card_count.keys()) == 5:       # High Card
        if 'J' in card_count.keys():
            return 2
        return 1
    elif len(card_count.keys()) == 4:       # One Pair
        if 'J' in card_count.keys():
            return 3
        return 2
    elif len(card_count.keys()) == 3 and (2 in card_count.values()): # Two Pair
        if card_count['J'] == 1:
            return 5
        elif card_count['J'] == 2:
            return 6
        return 3
    
    elif len(card_count.keys()) == 3 and (3 in card_count.values()):  # Three of a kind
        if 'J' in card_count.keys():
            return 6
        return 4
    
    elif len(card_count.keys()) == 2 and (3 in card_count.values()): # Full House
        if 'J' in card_count.keys():
            return 7
        return 5
    elif len(card_count.keys()) == 2 and (4 in card_count.values()): # Four Of a kind.
        if 'J' in card_count.keys():
            return 7
        return 6
    else:
        return 7  # Five of a kind.
       
def get_card_type(card):
    card_count = Counter(card)

    if len(card_count.keys()) == 5:
        return 1
    elif len(card_count.keys()) == 4:
        return 2
    elif len(card_count.keys()) == 3 and (2 in card_count.values()):
        return 3
    elif len(card_count.keys()) == 3 and (3 in card_count.values()):
        return 4
    elif len(card_count.keys()) == 2 and (3 in card_count.values()):
        return 5
    elif len(card_count.keys()) == 2 and (4 in card_count.values()):
        return 6
    else:
        return 7




if __name__=="__main__":
    input = './sample/sample7.txt'
    input = './input/advent_of_code_day7_input.txt'
    
    # res = return_sum_of_card_winning_bids(input)
    res = return_sum_of_card_winning_bids_joker_switch(input)

    print(res)