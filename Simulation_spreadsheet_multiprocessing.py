import concurrent.futures
import sys
import timeit
import random
import winsound
duration = 1000  # milliseconds
freq = 440  # Hz
start = timeit.default_timer()

# Number of iterations (10000000)
iterations = 10000000

# Defining opponents deck-states
# First Deck
list_of_decksize_opp_first_deck = [30, 25, 20, 30, 25, 20]
list_of_cx_opp_first_deck = [8, 8, 8, 6, 6, 6]
# Second Deck
cx_opp_second_deck = 8
decksize_opp_second_deck = 30
dmg_opp_second_deck = decksize_opp_second_deck - cx_opp_second_deck

# Defining own deck-states
own_number_of_cards = 25
own_soul_triggers = 8
own_2soul_triggers = 0
own_empty_triggers = own_number_of_cards - own_soul_triggers - own_2soul_triggers
no_of_lv0 = 13  # includes number of climaxes
no_of_lv1 = 6
no_of_lv2 = 2
no_of_lv3 = 4


def sim(decksize, climaxes):
    dmg_opp_first_deck = decksize - climaxes

    # Setting up opp deck for Eren Titan or Saekano Megumi stuff
    # number_of_lvl1_or_higher = round(0.45 * decksize)
    # number_of_lvl0 = decksize - climaxes - number_of_lvl1_or_higher
    # number_of_lvl1_or_higher_second_deck = round(0.45 * decksize_opp_second_deck)
    # number_of_lvl0_second_deck = decksize_opp_second_deck - cx_opp_second_deck - number_of_lvl1_or_higher_second_deck

    results = []

    # Defining finishers
    # noinspection PyBroadException
    def special_week():
        soul = 3
        swing_damage = 0
        cards_clocked = 0
        refresh_penalty = 0

        # Top Checking opp 3, clocking 1 DMG and 1 CX
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        try:
            if opp_deck.index("CX") <= 2:
                cards_clocked += 1
        except:
            pass
        try:
            if opp_deck.index("DMG") <= 2:
                cards_clocked += 1
        except:
            pass
        del opp_deck[:3]

        # Vanilla Swing + Triggercheck
        soul += own_deck[0]
        own_deck.pop(0)
        for soul in range(soul):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                swing_damage += 1
                opp_deck.pop(0)
            else:
                swing_damage = 0
                opp_deck.pop(0)
                break

        if len(opp_deck) == 0:
            refresh_penalty += refresh()

        damage_of_attack = swing_damage + refresh_penalty + cards_clocked
        return damage_of_attack

    # Deck-Refresh function
    def refresh():
        for second_cx in range(cx_opp_second_deck):
            opp_deck.append("CX")
        for second_dmg in range(dmg_opp_second_deck):
            opp_deck.append("DMG")
        # for lvlone in range(number_of_lvl1_or_higher_second_deck):
        #     opp_deck.append("lvl1")
        # for lvlzero in range(number_of_lvl0_second_deck):
        #     opp_deck.append("lvl0")
        random.shuffle(opp_deck)
        opp_deck.pop(0)
        refresh_damage = 1
        return refresh_damage

    # Start Sim Loop
    i = 1
    while i <= iterations:
        opp_deck = []
        own_deck = []
        total_damage = 0

        # Setting up opponents deck
        for climax in range(climaxes):
            opp_deck.append("CX")
        for damage in range(dmg_opp_first_deck):
            opp_deck.append("DMG")
        # for lvl0 in range(number_of_lvl0):
        #     opp_deck.append("lvl0")
        # for lvl1 in range(number_of_lvl1_or_higher):
        #     opp_deck.append("lvl1")
        random.shuffle(opp_deck)

        # Setting up own deck
        for own_1soul in range(own_soul_triggers):
            own_deck.append(1)
        for own_empty in range(own_empty_triggers):
            own_deck.append(0)
        for own_2soul in range(own_2soul_triggers):
            own_deck.append(2)
        random.shuffle(own_deck)
        # for lvl0 in range(no_of_lv0):
        #     own_deck.append("lvl0")
        # for lvl1 in range(no_of_lv1):
        #     own_deck.append("lvl1")
        # for lvl2 in range(no_of_lv2):
        #     own_deck.append("lvl2")
        # for lvl3 in range(no_of_lv3):
        #     own_deck.append("lvl3")
        # random.shuffle(own_deck)

        # # Gilthunder Rearrange SDS
        # rearranged_deck = own_deck.copy()
        # del rearranged_deck[3:]
        # rearranged_deck.sort(reverse=True)
        # del own_deck[:3]
        # rearranged_deck.extend(own_deck)
        # own_deck = rearranged_deck

        # LRC Brainstorm Rearrange
        # if opp_deck[1] == "CX":
        #     opp_deck.pop(1)
        #     opp_deck.insert(0, "CX")
        # elif opp_deck[1] == "lvl0" and not opp_deck[0] == "CX":
        #     opp_deck.pop(1)
        #     opp_deck.insert(0, "lvl0")

        # LRC Attack Order
        # if opp_deck[0] == "CX" or opp_deck[0] == "lvl0":
        #     total_damage += chisato_single()
        #     total_damage += chisato_single()
        #     total_damage += vanilla3()
        # else:
        #     total_damage += vanilla3()
        #     total_damage += chisato_single()
        #     total_damage += chisato_single()

        # Defining finishing turn
        total_damage += special_week()
        total_damage += special_week()
        total_damage += special_week()

        results.append(int(total_damage))
        i += 1
    # End of Loop

    # Calculating percentages
    damage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    percentages = []
    for dmg in damage:
        larger_elements = [element for element in results if element >= dmg]
        percentage_of_elements = (len(larger_elements) / len(results)) * 100
        percentages.append((float(percentage_of_elements)))
    # Printing results
    print(str(climaxes) + " in " + str(decksize))
    percentages_rounded = ['%.1f' % elem for elem in percentages]
    print(percentages_rounded)


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sim, list_of_decksize_opp_first_deck, list_of_cx_opp_first_deck)

    stop = timeit.default_timer()
    total_time = stop - start
    # output running time in a nice format
    mins, secs = divmod(total_time, 60)
    hours, mins = divmod(mins, 60)
    sys.stdout.write("Total running time: %d:%d:%d.\n" % (hours, mins, secs))

    # Notification sound that the script is finished
    winsound.Beep(freq, duration)
