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


def coco():
    soul = 3
    icy_tail_value = 3
    number_of_icy_tails = 6
    burn_damage = 0
    refresh_penalty = 0
    swing_damage = 0

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

    # Icy Tails
    for icy_tails in range(number_of_icy_tails):
        cx_hits = 0
        for value in range(icy_tail_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[-1] == "CX":
                cx_hits += 1
                opp_deck.pop(-1)
            else:
                opp_deck.pop(-1)
        if cx_hits != 0:
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                opp_deck.pop(0)
                burn_damage += 1
            else:
                opp_deck.pop(0)

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = burn_damage + refresh_penalty + swing_damage
    return damage_of_attack


def takina_single():
    swing_damage = 0
    mill_burn = 0
    number_of_mills = 1
    soul = 3
    refresh_penalty = 0

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    # Mill topdeck, if lvl0 burn
    for mill in range(number_of_mills):
        if opp_deck[0] == "CX" or opp_deck[0] == "lvl0":
            opp_deck.pop(0)
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
                mill_burn += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
        else:
            opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    soul += own_deck[0]
    own_deck.pop(0)
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + refresh_penalty + mill_burn
    return damage_of_attack


def chisato_double():
    restand_soul = 3
    second_swing_damage = 0
    swing_damage = 0
    mill_burn = 0
    number_of_mills = 2
    soul = 3
    refresh_penalty = 0

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    # Mill topdeck, if lvl0 burn
    for mill in range(number_of_mills):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "CX" or opp_deck[0] == "lvl0":
            opp_deck.pop(0)
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
                mill_burn += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
        else:
            opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    soul += own_deck[0]
    restand_soul += own_deck[0]
    own_deck.pop(0)
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    # Mill topdeck, if lvl0 burn
    for mill in range(number_of_mills):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "CX" or opp_deck[0] == "lvl0":
            opp_deck.pop(0)
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
                mill_burn += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
        else:
            opp_deck.pop(0)

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    # Restand Swing + Triggercheck
    restand_soul += own_deck[0]
    own_deck.pop(0)
    for soul in range(restand_soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            second_swing_damage += 1
            opp_deck.pop(0)
        else:
            second_swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + second_swing_damage + refresh_penalty + mill_burn
    return damage_of_attack


def chisato_single():
    restand_soul = 3
    second_swing_damage = 0
    swing_damage = 0
    mill_burn = 0
    number_of_mills = 1
    soul = 3
    refresh_penalty = 0

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    # Mill topdeck, if lvl0 burn
    for mill in range(number_of_mills):
        if opp_deck[0] == "CX" or opp_deck[0] == "lvl0":
            opp_deck.pop(0)
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
                mill_burn += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
        else:
            opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    soul += own_deck[0]
    restand_soul += own_deck[0]
    own_deck.pop(0)
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    # Mill topdeck, if lvl0 burn
    for mill in range(number_of_mills):
        if opp_deck[0] == "CX" or opp_deck[0] == "lvl0":
            opp_deck.pop(0)
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
                mill_burn += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
        else:
            opp_deck.pop(0)

    # Restand Swing + Triggercheck
    restand_soul += own_deck[0]
    own_deck.pop(0)
    for soul in range(restand_soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            second_swing_damage += 1
            opp_deck.pop(0)
        else:
            second_swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + second_swing_damage + refresh_penalty + mill_burn
    return damage_of_attack


def gura():
    swing_damage = 0
    on_attack_burn_damage = 0
    mill_burn = 0
    number_of_mills = 2
    burn_value = 2
    soul = 3
    refresh_penalty = 0

    # On Attack Burn
    for burn in range(burn_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            on_attack_burn_damage = 0
            break

    # Mill topdeck, if Soul Trigger burn
    for mill in range(number_of_mills):
        if own_deck[0] != 0:
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                mill_burn += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
        own_deck.pop(0)

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

    damage_of_attack = swing_damage + refresh_penalty + on_attack_burn_damage + mill_burn
    return damage_of_attack


def laplus():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0
    cancel_burn_damage = 0
    damage_canceled = False

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
            damage_canceled = True
            break

    # 2x Cancel Burn 1
    if damage_canceled:
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            cancel_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)

        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            cancel_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = cancel_burn_damage + refresh_penalty + swing_damage
    return damage_of_attack


def towa_icytail():
    soul = 3
    swing_damage = 0
    icy_tail_value = 3
    refresh_penalty = 0
    icy_tail_damage = 0
    cx_hits = 0

    # Scry
    if opp_deck[0] == "CX":
        opp_deck.pop(0)
        opp_deck.append("CX")
    # elif opp_deck[0] == "lvl0":
    #     opp_deck.pop(0)
    #     opp_deck.append("lvl0")

    # # Icy-Tail effect
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX" or opp_deck[-1] == "lvl0":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)

    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            opp_deck.pop(0)
            icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            icy_tail_damage = 0
            break

    # Vanilla Swing + Triggercheck
    soul += own_deck[0]
    own_deck.pop(0)
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = icy_tail_damage + refresh_penalty + swing_damage
    return damage_of_attack


def chika_musashi():
    swing_damage = 0
    soul = 3
    burn_value = 3
    burn_damage = 0
    refresh_penalty = 0
    on_reverse_burns = 2
    number_of_musashi_burns = 3
    musashi_burn_damage = 0
    musashi_burn_primed = False
    musashi_burn_resolved = False

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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
            musashi_burn_primed = True
            break

    # First musashi burn check
    if musashi_burn_primed:
        for musashis in range(number_of_musashi_burns):
            intermediate_burn_value = 0
            if own_deck[0] == "lvl0":
                musashi_burn_value = 1
                own_deck.pop(0)
            elif own_deck[0] == "lvl1":
                musashi_burn_value = 2
                own_deck.pop(0)
            elif own_deck[0] == "lvl2":
                musashi_burn_value = 3
                own_deck.pop(0)
            else:
                musashi_burn_value = 4
                own_deck.pop(0)
            for musashi_burn in range(musashi_burn_value):
                if len(opp_deck) == 0:
                    refresh_penalty += refresh()
                if opp_deck[0] == "DMG":
                    intermediate_burn_value += 1
                    opp_deck.pop(0)
                else:
                    intermediate_burn_value = 0
                    opp_deck.pop(0)
                    break
            if intermediate_burn_value == musashi_burn_value:
                burn_damage += musashi_burn_value
        musashi_burn_resolved = True

    # On Reverse burns
    for burns in range(on_reverse_burns):
        intermediate_burn_value = 0
        for burn in range(burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                opp_deck.pop(0)
                intermediate_burn_value += 1
            else:
                opp_deck.pop(0)
                intermediate_burn_value = 0
                musashi_burn_primed = True
                break
        if intermediate_burn_value == burn_value:
            burn_damage += burn_value

    # Second musashi burn check
    if musashi_burn_primed and not musashi_burn_resolved:
        for musashis in range(number_of_musashi_burns):
            intermediate_burn_value = 0
            if own_deck[0] == "lvl0":
                musashi_burn_value = 1
                own_deck.pop(0)
            elif own_deck[0] == "lvl1":
                musashi_burn_value = 2
                own_deck.pop(0)
            elif own_deck[0] == "lvl2":
                musashi_burn_value = 3
                own_deck.pop(0)
            else:
                musashi_burn_value = 4
                own_deck.pop(0)
            for musashi_burn in range(musashi_burn_value):
                if len(opp_deck) == 0:
                    refresh_penalty += refresh()
                if opp_deck[0] == "DMG":
                    intermediate_burn_value += 1
                    opp_deck.pop(0)
                else:
                    intermediate_burn_value = 0
                    opp_deck.pop(0)
                    break
            if intermediate_burn_value == musashi_burn_value:
                burn_damage += musashi_burn_value

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + burn_damage + musashi_burn_damage + refresh_penalty
    return damage_of_attack


def moca_restand():
    soul = 3
    restand_soul = 3
    swing_damage = 0
    second_swing_damage = 0
    refresh_penalty = 0

    # Top 2 check opponents deck
    if len(opp_deck) == 0:
        refresh_penalty += refresh()
    if len(opp_deck) >= 2:
        if opp_deck[1] == "CX":
            opp_deck.pop(1)
    if opp_deck[0] == "CX":
        opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    soul += own_deck[0]
    restand_soul += own_deck[0]
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

    # Top 2 check opponents deck
    if len(opp_deck) == 0:
        refresh_penalty += refresh()
    if len(opp_deck) >= 2:
        if opp_deck[1] == "CX":
            opp_deck.pop(1)
    if opp_deck[0] == "CX":
        opp_deck.pop(0)

    # Restand Swing + Triggercheck
    restand_soul += own_deck[0]
    own_deck.pop(0)
    for soul in range(restand_soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            second_swing_damage += 1
            opp_deck.pop(0)
        else:
            second_swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + second_swing_damage + refresh_penalty
    return damage_of_attack


def argo():
    soul = 3
    burn_value = 3
    on_attack_burn_damage = 0
    musashi_burn_damage = 0
    musashi_burn_primed = False
    musashi_burn_resolved = False
    swing_damage = 0
    refresh_penalty = 0

    # On Attack Burn
    for burn in range(burn_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            on_attack_burn_damage = 0
            musashi_burn_primed = True
            break

    # First musashi burn check
    if musashi_burn_primed:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break
        musashi_burn_resolved = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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
            musashi_burn_primed = True
            break

    # Second Musashi Burn check
    if musashi_burn_primed and not musashi_burn_resolved:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + musashi_burn_damage + on_attack_burn_damage + refresh_penalty
    return damage_of_attack


def rina3():
    soul = 3
    restand_soul = 3
    musashi_burn_damage = 0
    musashi_burn_primed = False
    musashi_burn_resolved = False
    swing_damage = 0
    second_swing_damage = 0
    refresh_penalty = 0

    # First Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
        restand_soul += 1
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
            musashi_burn_primed = True
            break
    # First musashi burn check
    if musashi_burn_primed:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break
        musashi_burn_resolved = True

    # Restand Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        restand_soul += 1
    own_deck.pop(0)
    for restand_soul in range(restand_soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            second_swing_damage += 1
            opp_deck.pop(0)
        else:
            second_swing_damage = 0
            opp_deck.pop(0)
            musashi_burn_primed = True
            break
    # Second Musashi Burn check
    if musashi_burn_primed and not musashi_burn_resolved:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + musashi_burn_damage + second_swing_damage + refresh_penalty
    return damage_of_attack


def silica_anniv():
    swing_damage = 0
    on_attack_burn_damage = 0
    burn_value = 2
    soul = 3
    reshuffled_cards = 2
    refresh_penalty = 0

    # On Attack Burn
    for burn in range(burn_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            on_attack_burn_damage = 0
            break

    # Shuffling back damage
    for char in range(reshuffled_cards):
        opp_deck.append("DMG")
    random.shuffle(opp_deck)

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

    damage_of_attack = swing_damage + refresh_penalty + on_attack_burn_damage
    return damage_of_attack


def makoto_key_icytail():
    soul = 3
    swing_damage = 0
    icy_tail_value = 4
    refresh_penalty = 0
    icy_tail_damage = 0
    cx_hits = 0

    # Icy-Tail effect
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)
    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            icy_tail_damage = 0
            break

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

    damage_of_attack = icy_tail_damage + refresh_penalty + swing_damage
    return damage_of_attack


def makoto_key_icytail_with_restand_event():
    soul = 3
    restand_soul = 3
    swing_damage = 0
    second_swing_damage = 0
    icy_tail_value = 4
    first_icy_tail_damage = 0
    second_icy_tail_damage = 0
    damage_canceled = False
    refresh_penalty = 0

    # First Icy-Tail effect
    cx_hits = 0
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)
    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            first_icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            first_icy_tail_damage = 0
            damage_canceled = True
            break

    # Vanilla Swing + Triggercheck
    soul += own_deck[0]
    restand_soul += own_deck[0]
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
            damage_canceled = True
            break

    if damage_canceled:
        # Second Icy-Tail effect
        cx_hits = 0
        for value in range(icy_tail_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[-1] == "CX":
                cx_hits += 1
                opp_deck.pop(-1)
            else:
                opp_deck.pop(-1)
        for icy_tail_cx in range(cx_hits):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                opp_deck.pop(0)
                second_icy_tail_damage += 1
            else:
                opp_deck.pop(0)
                second_icy_tail_damage = 0
                break

        # Restand Swing + Triggercheck
        restand_soul += own_deck[0]
        own_deck.pop(0)
        for soul in range(restand_soul):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                second_swing_damage += 1
                opp_deck.pop(0)
            else:
                second_swing_damage = 0
                opp_deck.pop(0)
                break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    total_icy_tail_damage = first_icy_tail_damage + second_icy_tail_damage
    damage_of_attack = swing_damage + second_swing_damage + total_icy_tail_damage + refresh_penalty
    return damage_of_attack


def escanor_direct():
    soul = 4
    burn_damage = 0
    refresh_penalty = 0

    # Triggercheck
    soul += own_deck[0]
    own_deck.pop(0)
    # Deal 1 Damage X times
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            burn_damage += 1
        else:
            opp_deck.pop(0)

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = burn_damage + refresh_penalty
    return damage_of_attack


def escanor_front():
    soul = 3
    burn_damage = 0
    refresh_penalty = 0

    # Triggercheck
    soul += own_deck[0]
    own_deck.pop(0)
    # Deal 1 Damage X times
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            burn_damage += 1
        else:
            opp_deck.pop(0)

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = burn_damage + refresh_penalty
    return damage_of_attack


def vanilla3():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0

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

    damage_of_attack = swing_damage + refresh_penalty
    return damage_of_attack


def kyoko_d4dj():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0
    burn_damage = 0
    clock_kick = 1

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    # Damage dealing loop
    for burn_effect in range(3, 0, -1):
        burn_value = burn_effect
        intermediate_value = 0
        for burn in range(burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                opp_deck.pop(0)
                intermediate_value += 1
            else:
                opp_deck.pop(0)
                intermediate_value = 0
                break
        if intermediate_value == burn_value:
            burn_damage += burn_value

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + burn_damage + refresh_penalty + clock_kick
    return damage_of_attack


def burn1_rinku():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0

    # On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage = 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage = 0
        opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = swing_damage + on_attack_burn_damage + refresh_penalty
    return damage_of_attack


def nagisa():
    soul = 3
    swing_damage = 0
    top_deck_clock_kick = 0
    top_deck_clock_kick_value = 2
    refresh_penalty = 0

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    # Climax Combo
    if opp_deck[0] == "DMG":
        opp_deck.pop(0)
        for value in range(top_deck_clock_kick_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            opp_deck.pop(0)
        top_deck_clock_kick = top_deck_clock_kick_value
    else:
        opp_deck.pop(0)

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + top_deck_clock_kick + refresh_penalty
    return damage_of_attack


def eren_titan():
    soul = 3
    swing_damage = 0
    icy_tail_value = 4
    refresh_penalty = 0
    icy_tail_damage = 0
    cx_hits = 0

    # Icy-Tail effect
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX" or opp_deck[-1] == "lvl0":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)

    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            opp_deck.pop(0)
            icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            icy_tail_damage = 0
            break

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = icy_tail_damage + refresh_penalty + swing_damage
    return damage_of_attack


def vanilla2():
    soul = 2
    swing_damage = 0
    refresh_penalty = 0

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = swing_damage + refresh_penalty
    return damage_of_attack


def icy_tail_4():
    soul = 3
    swing_damage = 0
    icy_tail_value = 4
    refresh_penalty = 0
    icy_tail_damage = 0
    cx_hits = 0

    # Icy-Tail effect
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)

    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            icy_tail_damage = 0
            break

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = icy_tail_damage + refresh_penalty + swing_damage
    return damage_of_attack


def buzz_clockkick():
    soul = 3
    restand_soul = 3
    swing_damage = 0
    second_swing_damage = 0
    refresh_penalty = 0
    clockkicks = 2

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
        restand_soul += 1
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
    # Restand Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        restand_soul += 1
    for restand_soul in range(restand_soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            second_swing_damage += 1
            opp_deck.pop(0)
        else:
            second_swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + second_swing_damage + refresh_penalty + clockkicks
    return damage_of_attack


def misuzu_key():
    soul = 2
    swing_damage = 0
    refresh_penalty = 0
    burn_damage = 0

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    # Damage dealing loop
    for burn_effect in range(1, 8):
        burn_value = burn_effect
        intermediate_value = 0
        for burn in range(burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                opp_deck.pop(0)
                intermediate_value += 1
            else:
                opp_deck.pop(0)
                intermediate_value = 0
                break
        if intermediate_value == burn_value:
            burn_damage += burn_value

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + burn_damage + refresh_penalty
    return damage_of_attack


def iruru_bar():
    soul = 4
    swing_damage = 0
    refresh_penalty = 0
    cancel_burn_damage = 0
    on_attack_burn_damage = 0
    attack_canceled = False

    # On Attack Burn
    if own_deck[0] != "CX":
        if opp_deck[0] == "DMG":
            on_attack_burn_damage = 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    if own_deck[0] == "soul":
        soul += 1
        own_deck.pop(0)
    elif own_deck[0] == "CX":
        own_deck.pop(0)
        own_deck.pop(0)
    else:
        own_deck.pop(0)
    cancel_burn_value = soul
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            attack_canceled = True
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    # Cancel burn
    if attack_canceled:
        for cancel in range(cancel_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                cancel_burn_damage = 0
                opp_deck.pop(0)
                break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + cancel_burn_damage + refresh_penalty + on_attack_burn_damage
    return damage_of_attack


def tohru_icy_tail():
    soul = 3
    swing_damage = 0
    icy_tail_value = 4
    refresh_penalty = 0
    icy_tail_damage = 0
    cx_hits = 0

    # Icy-Tail effect
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)

    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            icy_tail_damage = 0
            break

    # Vanilla Swing + Triggercheck
    if own_deck[0] == "soul":
        soul += 1
        own_deck.pop(0)
    elif own_deck[0] == "CX":
        own_deck.pop(0)
        own_deck.pop(0)
    else:
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

    damage_of_attack = icy_tail_damage + refresh_penalty + swing_damage
    return damage_of_attack


def armored_titan():
    revealed_cards = 9
    burn_damage = 0
    number_of_burns = 2
    soul = 3
    swing_damage = 0
    refresh_penalty = 0

    # Checking Pants Triggers
    burn_value = own_deck[:revealed_cards].count("CX")
    random.shuffle(own_deck)

    # Damage dealing loop
    for burns in range(number_of_burns):
        intermediate_burn_value = 0
        for burn in range(burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                opp_deck.pop(0)
                intermediate_burn_value += 1
            else:
                opp_deck.pop(0)
                intermediate_burn_value = 0
                break
        if intermediate_burn_value == burn_value:
            burn_damage += burn_value

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    # Vanilla Swing + Triggercheck
    if own_deck[0] == "soul" or own_deck[0] == "CX":
        soul += 1
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

    damage_of_attack = swing_damage + burn_damage + refresh_penalty
    return damage_of_attack


def futaba_set1():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0

    # On Attack Burn 1
    if len(opp_deck) == 0:
        refresh_penalty += refresh()
    if opp_deck[0] == "DMG":
        on_attack_burn_damage = 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage = 0
        opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = swing_damage + on_attack_burn_damage + refresh_penalty
    return damage_of_attack


def kaoruko_choice_cxc():
    burn_1_damage = 0
    burn_2_damage = 0
    burn_value = 2

    # Burn 1
    if opp_deck[0] == "DMG":
        burn_1_damage += 1
        opp_deck.pop(0)
    else:
        opp_deck.pop(0)

    # Burn 2
    for burn in range(burn_value):
        if opp_deck[0] == "DMG":
            burn_2_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            burn_2_damage = 0
            break

    damage_of_attack = burn_2_damage + burn_1_damage
    return damage_of_attack


def kaoruko_wind():
    soul = 4
    cancel_burn_value = 2
    swing_damage = 0
    cancel_burn_damage_1 = 0
    cancel_burn_damage_2 = 0
    attack_canceled = False
    refresh_penalty = 0

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            attack_canceled = True
            break

    # Cancel Burn 2 No.1
    if attack_canceled:
        for cancel_burn in range(cancel_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                cancel_burn_damage_1 += 1
                opp_deck.pop(0)
            elif attack_canceled:
                opp_deck.pop(0)
                cancel_burn_damage_1 = 0
                break

    # Cancel Burn 2 No.2
    if attack_canceled:
        for cancel_burn in range(cancel_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                cancel_burn_damage_2 += 1
                opp_deck.pop(0)
            elif attack_canceled:
                opp_deck.pop(0)
                cancel_burn_damage_2 = 0
                break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + cancel_burn_damage_1 + cancel_burn_damage_2 + refresh_penalty
    return damage_of_attack


def kaguya_musashi():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0
    musashi_burn_damage = 0
    musashi_burn_primed = False
    musashi_burn_resolved = False

    # On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage = 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage = 0
        opp_deck.pop(0)
        musashi_burn_primed = True

    if musashi_burn_primed:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break
        musashi_burn_resolved = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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
            musashi_burn_primed = True
            break

    if musashi_burn_primed and not musashi_burn_resolved:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break
        musashi_burn_resolved = True

    # On Reverse Burn 1
    if len(opp_deck) == 0:
        refresh_penalty += refresh()
    if opp_deck[0] == "DMG":
        on_reverse_burn_damage = 1
        opp_deck.pop(0)
    else:
        on_reverse_burn_damage = 0
        opp_deck.pop(0)
        musashi_burn_primed = True

    if musashi_burn_primed and not musashi_burn_resolved:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + on_attack_burn_damage + on_reverse_burn_damage + refresh_penalty + musashi_burn_damage
    return damage_of_attack


def kaguya_2musashi():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0
    musashi_stacks = 2
    musashi_burn_damage = 0
    musashi_burn_primed = False
    musashi_burn_resolved = False

    # On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage = 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage = 0
        opp_deck.pop(0)
        musashi_burn_primed = True

    if musashi_burn_primed:
        for stack in range(musashi_stacks):
            intermediate_burn_value = 0
            if own_deck[0] == "lvl0":
                musashi_burn_value = 1
                own_deck.pop(0)
            elif own_deck[0] == "lvl1":
                musashi_burn_value = 2
                own_deck.pop(0)
            elif own_deck[0] == "lvl2":
                musashi_burn_value = 3
                own_deck.pop(0)
            else:
                musashi_burn_value = 4
                own_deck.pop(0)
            for musashi_burn in range(musashi_burn_value):
                if len(opp_deck) == 0:
                    refresh_penalty += refresh()
                if opp_deck[0] == "DMG":
                    intermediate_burn_value += 1
                    opp_deck.pop(0)
                else:
                    intermediate_burn_value = 0
                    opp_deck.pop(0)
                    break
            if intermediate_burn_value == musashi_burn_value:
                musashi_burn_damage += musashi_burn_value
        musashi_burn_resolved = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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
            musashi_burn_primed = True
            break

    if musashi_burn_primed and not musashi_burn_resolved:
        for stack in range(musashi_stacks):
            intermediate_burn_value = 0
            if own_deck[0] == "lvl0":
                musashi_burn_value = 1
                own_deck.pop(0)
            elif own_deck[0] == "lvl1":
                musashi_burn_value = 2
                own_deck.pop(0)
            elif own_deck[0] == "lvl2":
                musashi_burn_value = 3
                own_deck.pop(0)
            else:
                musashi_burn_value = 4
                own_deck.pop(0)
            for musashi_burn in range(musashi_burn_value):
                if len(opp_deck) == 0:
                    refresh_penalty += refresh()
                if opp_deck[0] == "DMG":
                    intermediate_burn_value += 1
                    opp_deck.pop(0)
                else:
                    intermediate_burn_value = 0
                    opp_deck.pop(0)
                    break
            if intermediate_burn_value == musashi_burn_value:
                musashi_burn_damage += musashi_burn_value
        musashi_burn_resolved = True

    # On Reverse Burn 1
    if len(opp_deck) == 0:
        refresh_penalty += refresh()
    if opp_deck[0] == "DMG":
        on_reverse_burn_damage = 1
        opp_deck.pop(0)
    else:
        on_reverse_burn_damage = 0
        opp_deck.pop(0)
        musashi_burn_primed = True

    if musashi_burn_primed and not musashi_burn_resolved:
        for stack in range(musashi_stacks):
            intermediate_burn_value = 0
            if own_deck[0] == "lvl0":
                musashi_burn_value = 1
                own_deck.pop(0)
            elif own_deck[0] == "lvl1":
                musashi_burn_value = 2
                own_deck.pop(0)
            elif own_deck[0] == "lvl2":
                musashi_burn_value = 3
                own_deck.pop(0)
            else:
                musashi_burn_value = 4
                own_deck.pop(0)
            for musashi_burn in range(musashi_burn_value):
                if len(opp_deck) == 0:
                    refresh_penalty += refresh()
                if opp_deck[0] == "DMG":
                    intermediate_burn_value += 1
                    opp_deck.pop(0)
                else:
                    intermediate_burn_value = 0
                    opp_deck.pop(0)
                    break
            if intermediate_burn_value == musashi_burn_value:
                musashi_burn_damage += musashi_burn_value

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + on_attack_burn_damage + on_reverse_burn_damage + refresh_penalty + musashi_burn_damage
    return damage_of_attack


def mitsuya_cip():
    burn_damage = 0
    burn_value = 0
    milled_cards = 2
    refresh_penalty = 0

    # CIP Burn
    for card in range(milled_cards):
        if own_deck[0] == "2soul":
            burn_value += 2
        elif own_deck[0] == "1soul":
            burn_value += 1
        own_deck.pop(0)

    for burn in range(burn_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            burn_damage = 0
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = refresh_penalty + burn_damage
    return damage_of_attack


def mikey5_2soul():
    soul = 2
    swing_damage = 0
    refresh_penalty = 0
    number_of_markers = 5
    on_attack_burn_damage = 0

    for marker in range(number_of_markers):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)

    # Triggercheck
    if own_deck[0] == "2soul":
        soul += 2
    elif own_deck[0] == "1soul":
        soul += 1
    own_deck.pop(0)
    # Vanilla Swing
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

    damage_of_attack = swing_damage + on_attack_burn_damage + refresh_penalty
    return damage_of_attack


def mikey1_3soul():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0
    number_of_markers = 1
    on_attack_burn_damage = 0

    for marker in range(number_of_markers):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)

    # Triggercheck
    if own_deck[0] == "2soul":
        soul += 2
    elif own_deck[0] == "1soul":
        soul += 1
    own_deck.pop(0)
    # Vanilla Swing
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

    damage_of_attack = swing_damage + on_attack_burn_damage + refresh_penalty
    return damage_of_attack


def mitsuya_cxc_3soul():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0

    # Putting 1 dmg on top of opp deck
    opp_deck.insert(0, "DMG")

    # Triggercheck
    if own_deck[0] == "2soul":
        soul += 2
    elif own_deck[0] == "1soul":
        soul += 1
    own_deck.pop(0)
    # Vanilla Swing
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

    damage_of_attack = swing_damage + refresh_penalty
    return damage_of_attack


def mitsuya_cxc_2soul():
    soul = 2
    swing_damage = 0
    refresh_penalty = 0

    # Putting 1 dmg on top of opp deck
    opp_deck.insert(0, "DMG")

    # Triggercheck
    if own_deck[0] == "2soul":
        soul += 2
    elif own_deck[0] == "1soul":
        soul += 1
    own_deck.pop(0)
    # Vanilla Swing
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

    damage_of_attack = swing_damage + refresh_penalty
    return damage_of_attack


def movie_ichika():
    swing_damage = 0
    cancel_burn_damage = 0
    no_of_your_other_characters = 4
    soul = 3
    attack_canceled = False
    refresh_penalty = 0

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            attack_canceled = True
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    if attack_canceled:
        # Shuffling back damage
        for char in range(no_of_your_other_characters):
            opp_deck.append("DMG")
        random.shuffle(opp_deck)
        # Burn for the number of your other characters
        for char in range(no_of_your_other_characters):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                cancel_burn_damage = 0
                opp_deck.pop(0)
                break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + cancel_burn_damage + refresh_penalty
    return damage_of_attack


def burn2():
    burn_damage = 0
    burn_value = 2
    refresh_penalty = 0

    # On Attack Burn
    for burn in range(burn_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            burn_damage = 0
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = burn_damage + refresh_penalty
    return damage_of_attack


def subaru():
    swing_damage = 0
    on_attack_burn_damage = 0
    burn_value = 2
    soul = 3
    refresh_penalty = 0

    # On Attack Burn
    if own_deck[0] != "CX":
        for burn in range(burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                on_attack_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                on_attack_burn_damage = 0
                break

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = swing_damage + refresh_penalty + on_attack_burn_damage
    return damage_of_attack


def rushia_shuffleback():
    shuffle_back = 4

    # Shuffling back damage
    for char in range(shuffle_back):
        opp_deck.append("DMG")
    random.shuffle(opp_deck)

    return 0


def musashi3():
    soul = 3
    swing_damage = 0
    musashi_burn_value = 0
    musashi_burn_damage = 0
    musashi_burn_primed = False
    refresh_penalty = 0

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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
            musashi_burn_primed = True
            break

    if musashi_burn_primed:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        elif own_deck[0] == "lvl3":
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = musashi_burn_damage + swing_damage + refresh_penalty
    return damage_of_attack


def marine():
    swing_damage = 0
    on_attack_burn_damage = 0
    burn_value = 2
    soul = 3
    refresh_penalty = 0

    # On Attack Burn
    for burn in range(burn_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            on_attack_burn_damage = 0
            break

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = swing_damage + refresh_penalty + on_attack_burn_damage
    return damage_of_attack


def fourth_gen_event():
    burn_value = 4
    burn_damage = 0
    refresh_penalty = 0
    number_of_burns = 2

    # Burn 4 twice
    for icy_tail_cx in range(number_of_burns):
        intermediate_burn_value = 0
        for burn in range(burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                opp_deck.pop(0)
                intermediate_burn_value += 1
            else:
                opp_deck.pop(0)
                intermediate_burn_value = 0
                break
        if intermediate_burn_value == burn_value:
            burn_damage += burn_value

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = burn_damage + refresh_penalty
    return damage_of_attack


def lsp_ren():
    swing_damage = 0
    on_attack_burn_damage = 0
    burn_value = 3
    soul = 3
    refresh_penalty = 0

    # On Attack Burn
    for burn in range(burn_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            on_attack_burn_damage = 0
            break

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = swing_damage + refresh_penalty + on_attack_burn_damage
    return damage_of_attack


def kaguya():
    soul = 3
    swing_damage = 0
    refresh_penalty = 0

    # On Attack Burn 1
    if len(opp_deck) == 0:
        refresh_penalty += refresh()
    if opp_deck[0] == "DMG":
        on_attack_burn_damage = 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage = 0
        opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    # On Reverse Burn 1
    if len(opp_deck) == 0:
        refresh_penalty += refresh()
    if opp_deck[0] == "DMG":
        on_reverse_burn_damage = 1
        opp_deck.pop(0)
    else:
        on_reverse_burn_damage = 0
        opp_deck.pop(0)

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + on_attack_burn_damage + on_reverse_burn_damage + refresh_penalty
    return damage_of_attack


def niji_kanata():
    burn_value = 3
    icy_tail_value = 7
    burn_damage = 0
    refresh_penalty = 0
    cx_hits = 0

    # Icy-Tail mill
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)

    # Damage dealing loop
    for icy_tail_cx in range(cx_hits):
        intermediate_burn_value = 0
        for burn in range(burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                opp_deck.pop(0)
                intermediate_burn_value += 1
            else:
                opp_deck.pop(0)
                intermediate_burn_value = 0
                break
        if intermediate_burn_value == burn_value:
            burn_damage += burn_value

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = burn_damage + refresh_penalty
    return damage_of_attack


def dark_sakura():
    soul = 3
    swing_damage = 0
    icy_tail_value = 6
    refresh_penalty = 0
    icy_tail_damage = 0
    cx_hits = 0

    # Icy-Tail effect
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)

    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            icy_tail_damage = 0
            break

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

    damage_of_attack = icy_tail_damage + refresh_penalty + swing_damage
    return damage_of_attack


def sinon_icytail():
    soul = 3
    swing_damage = 0
    icy_tail_value = 7
    refresh_penalty = 0
    icy_tail_damage = 0
    cx_hits = 0

    # Icy-Tail effect
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)

    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            icy_tail_damage = 0
            break

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = icy_tail_damage + refresh_penalty + swing_damage
    return damage_of_attack


def drago_buster6():
    revealed_cards = 6

    # Draco Buster effect for 6
    cx_hits = opp_deck[:revealed_cards].count("CX")
    random.shuffle(opp_deck)
    for climax in range(cx_hits):
        opp_deck.pop(0)

    return cx_hits


def set1_ichika():
    soul = 3
    cancel_burn_value = 2
    swing_damage = 0
    cancel_burn_damage_1 = 0
    cancel_burn_damage_2 = 0
    attack_canceled = False
    refresh_penalty = 0

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            attack_canceled = True
            break

    # Cancel Burn 2 No.1
    if attack_canceled:
        for cancel_burn in range(cancel_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                cancel_burn_damage_1 += 1
                opp_deck.pop(0)
            elif attack_canceled:
                opp_deck.pop(0)
                cancel_burn_damage_1 = 0
                break

    # Cancel Burn 2 No.2
    if attack_canceled:
        for cancel_burn in range(cancel_burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                cancel_burn_damage_2 += 1
                opp_deck.pop(0)
            elif attack_canceled:
                opp_deck.pop(0)
                cancel_burn_damage_2 = 0
                break

    damage_of_attack = swing_damage + cancel_burn_damage_1 + cancel_burn_damage_2 + refresh_penalty
    return damage_of_attack


def movie_itsuki():
    swing_damage = 0
    on_attack_burn_damage = 0
    burn_value = 3
    soul = 3
    refresh_penalty = 0

    # On Attack Burn
    for burn in range(burn_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            on_attack_burn_damage = 0
            break

    # Top 2 check opponents deck
    if len(opp_deck) == 0:
        refresh_penalty += refresh()
    if len(opp_deck) >= 2:
        if opp_deck[1] == "CX":
            opp_deck.pop(1)
    if opp_deck[0] == "CX":
        opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = swing_damage + refresh_penalty + on_attack_burn_damage
    return damage_of_attack


def single_riri_icytail():
    soul = 3
    swing_damage = 0
    icy_tail_value = 3
    refresh_penalty = 0
    icy_tail_damage = 0
    cx_hits = 0

    # Icy-Tail effect
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)

    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            icy_tail_damage = 0
            break

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = icy_tail_damage + refresh_penalty + swing_damage
    return damage_of_attack


def restand_yuyu_with_double_icytail():
    soul = 3
    restand_soul = 3
    swing_damage = 0
    second_swing_damage = 0
    icy_tail_value = 3
    first_icy_tail_damage = 0
    second_icy_tail_damage = 0
    third_icy_tail_damage = 0
    fourth_icy_tail_damage = 0
    refresh_penalty = 0

    # First Icy-Tail effect
    cx_hits = 0
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)
    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            first_icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            first_icy_tail_damage = 0
            break

    # Second Icy-Tail effect
    cx_hits = 0
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)
    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            second_icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            second_icy_tail_damage = 0
            break

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
        restand_soul += 1
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

    # Third Icy-Tail effect
    cx_hits = 0
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)
    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            third_icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            third_icy_tail_damage = 0
            break

    # Fourth Icy-Tail effect
    cx_hits = 0
    for value in range(icy_tail_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[-1] == "CX":
            cx_hits += 1
            opp_deck.pop(-1)
        else:
            opp_deck.pop(-1)
    for icy_tail_cx in range(cx_hits):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            fourth_icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            fourth_icy_tail_damage = 0
            break

    # Restand Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        restand_soul += 1
    for restand_soul in range(restand_soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            second_swing_damage += 1
            opp_deck.pop(0)
        else:
            second_swing_damage = 0
            opp_deck.pop(0)
            break

    total_icy_tail_damage = first_icy_tail_damage + second_icy_tail_damage + third_icy_tail_damage + fourth_icy_tail_damage
    damage_of_attack = swing_damage + second_swing_damage + total_icy_tail_damage + refresh_penalty
    return damage_of_attack


def moca():
    swing_damage = 0
    soul = 3
    refresh_penalty = 0

    # Top 2 check opponents deck
    if len(opp_deck) == 0:
        refresh_penalty += refresh()
    if len(opp_deck) >= 2:
        if opp_deck[1] == "CX":
            opp_deck.pop(1)
    if opp_deck[0] == "CX":
        opp_deck.pop(0)

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = swing_damage + refresh_penalty
    return damage_of_attack


def restand():
    soul = 3
    restand_soul = 3
    swing_damage = 0
    second_swing_damage = 0
    refresh_penalty = 0

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
        restand_soul += 1
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

    # Restand Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        restand_soul += 1
    for restand_soul in range(restand_soul):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            second_swing_damage += 1
            opp_deck.pop(0)
        else:
            second_swing_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + second_swing_damage + refresh_penalty
    return damage_of_attack


def burn1():
    if opp_deck[0] == "DMG":
        burn_damage = 1
        opp_deck.pop(0)
    else:
        burn_damage = 0
        opp_deck.pop(0)

    return burn_damage


def woody_and_buzz():
    drago_buster = 6
    soul = 3
    swing_damage = 0
    refresh_penalty = 0

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    # Drago Buster effect
    cx_hits = opp_deck[:drago_buster].count("CX")
    random.shuffle(opp_deck)
    for cxes in range(cx_hits):
        opp_deck.pop(0)
    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = swing_damage + cx_hits + refresh_penalty
    return damage_of_attack


def ims_red_event():
    burn_value = 2
    number_of_burns = 3
    burn_damage = 0
    refresh_penalty = 0

    # Damage dealing loop
    for burns in range(number_of_burns):
        intermediate_burn_value = 0
        for burn in range(burn_value):
            if len(opp_deck) == 0:
                refresh_penalty += refresh()
            if opp_deck[0] == "DMG":
                opp_deck.pop(0)
                intermediate_burn_value += 1
            else:
                opp_deck.pop(0)
                intermediate_burn_value = 0
                break
        if intermediate_burn_value == burn_value:
            burn_damage += burn_value

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    damage_of_attack = burn_damage + refresh_penalty
    return damage_of_attack


def ims_minako():
    soul = 3
    burn_value = 3
    swing_damage = 0
    burn_damage = 1
    refresh_penalty = 0

    # On Attack burn
    for first_burn in range(burn_value):
        if len(opp_deck) == 0:
            refresh_penalty += refresh()
        if opp_deck[0] == "DMG":
            burn_damage += 1
            opp_deck.pop(0)
        else:
            burn_damage = 0
            opp_deck.pop(0)
            break

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
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

    damage_of_attack = swing_damage + burn_damage + refresh_penalty
    return damage_of_attack

  
# Stuff below here has been written before the Refresh rule change was implemented and therefore uses an older (and worse) method for how to implement the refresh process
# Therefore everything below here will not work in the current script and needs to be rewritten
# It is only here for archival purposes


def vanilla4():
    soul = 4
    swing_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + refresh_penalty
    return damage_of_attack


def kotoha():
    soul = 2
    swing_damage = 0
    burn_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # On Reverse Burn 1 - 3 times
    if opp_deck[0] == "DMG":
        burn_damage += 1
        opp_deck.pop(0)
    else:
        opp_deck.pop(0)
    if opp_deck[0] == "DMG":
        burn_damage += 1
        opp_deck.pop(0)
    else:
        opp_deck.pop(0)
    if opp_deck[0] == "DMG":
        burn_damage += 1
        opp_deck.pop(0)
    else:
        opp_deck.pop(0)
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + burn_damage + refresh_penalty
    return damage_of_attack


def randou3():
    soul = 3
    swing_damage = 0
    burn_value = 4
    on_attack_burn_damage = 0
    on_reverse_burn_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # On Attack Burn 4
    for burn_value in range(burn_value):
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            on_attack_burn_damage = 0
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # On Reverse Burn 1
    if opp_deck[0] == "DMG":
        on_reverse_burn_damage += 1
        opp_deck.pop(0)
    else:
        on_reverse_burn_damage = 0
        opp_deck.pop(0)
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + on_attack_burn_damage + on_reverse_burn_damage + refresh_penalty
    return damage_of_attack


def hibiki3():
    soul = 3
    cancel_burn_value = 3
    swing_damage = 0
    cancel_burn_damage_1 = 0
    cancel_burn_damage_2 = 0
    attack_canceled = False
    cancel_burn_canceled = False
    refresh_penalty = 0
    global deck_refreshed

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            attack_canceled = True
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Cancel Burn for 3
    for soul in range(cancel_burn_value):
        if opp_deck[0] == "DMG" and attack_canceled:
            cancel_burn_damage_1 += 1
            opp_deck.pop(0)
        elif attack_canceled:
            opp_deck.pop(0)
            cancel_burn_damage_1 = 0
            cancel_burn_canceled = True
            break
    # Cancel Burn for 1
    if opp_deck[0] == "DMG" and cancel_burn_canceled:
        cancel_burn_damage_2 += 1
        opp_deck.pop(0)
    elif cancel_burn_canceled:
        opp_deck.pop(0)
        cancel_burn_damage_2 = 0
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + cancel_burn_damage_1 + cancel_burn_damage_2 + refresh_penalty
    return damage_of_attack


def finn_and_jake3():
    soul = 3
    eoa_burn_value = 2
    swing_damage = 0
    cancel_burn_damage = 0
    eoa_burn_damage = 0
    attack_canceled = False
    eoa_burn_canceled = False
    cancel_burn_resolved = False
    refresh_penalty = 0
    global deck_refreshed

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            attack_canceled = True
            break
    # Cancel Burn for 1
    if opp_deck[0] == "DMG" and attack_canceled:
        cancel_burn_damage = 1
        opp_deck.pop(0)
        cancel_burn_resolved = True
    elif attack_canceled:
        opp_deck.pop(0)
        cancel_burn_damage = 0
        cancel_burn_resolved = True
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # End of Attack burn
    for burn_value in range(eoa_burn_value):
        if opp_deck[0] == "DMG":
            eoa_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            eoa_burn_damage = 0
            eoa_burn_canceled = True
            break
    # Cancel Burn for 1
    if opp_deck[0] == "DMG" and eoa_burn_canceled and not cancel_burn_resolved:
        cancel_burn_damage = 1
        opp_deck.pop(0)
    elif eoa_burn_canceled and not cancel_burn_resolved:
        opp_deck.pop(0)
        cancel_burn_damage = 0
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + cancel_burn_damage + eoa_burn_damage + refresh_penalty
    return damage_of_attack


def cocochino3():
    soul = 3
    swing_damage = 0
    on_attack_burn_damage_1 = 0
    on_attack_burn_damage_2 = 0
    refresh_penalty = 0
    global deck_refreshed

    # On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage_1 += 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage_1 = 0
        opp_deck.pop(0)
    # On Attack Burn 2
    if opp_deck[0] == "DMG":
        on_attack_burn_damage_2 += 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage_2 = 0
        opp_deck.pop(0)
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + on_attack_burn_damage_1 + on_attack_burn_damage_2 + refresh_penalty
    return damage_of_attack


def single_kaori_3():
    soul = 3
    cancel_burn_value = 2
    on_attack_burn_damage_canceled = False
    swing_damage_canceled = False
    swing_damage = 0
    on_attack_burn_damage = 0
    cancel_burn_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage = 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage_canceled = True
        opp_deck.pop(0)
    # Cancel Burn for 2
    for value in range(cancel_burn_value):
        if opp_deck[0] == "DMG" and on_attack_burn_damage_canceled:
            cancel_burn_damage += 1
            opp_deck.pop(0)
        elif on_attack_burn_damage_canceled:
            opp_deck.pop(0)
            cancel_burn_damage = 0
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            swing_damage_canceled = True
            break
    # Cancel Burn for 2
    if swing_damage_canceled and not on_attack_burn_damage_canceled:
        for value in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                cancel_burn_damage = 0
                break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + on_attack_burn_damage + cancel_burn_damage + refresh_penalty
    return damage_of_attack


def double_kaori_3():
    soul = 3
    cancel_burn_value = 2
    swing_damage_canceled = False
    burn_damage_canceled = False
    swing_damage = 0
    first_on_attack_burn_damage = 0
    second_on_attack_burn_damage = 0
    first_cancel_burn_damage = 0
    second_cancel_burn_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # First On Attack Burn 1
    if opp_deck[0] == "DMG":
        first_on_attack_burn_damage = 1
        opp_deck.pop(0)
    else:
        burn_damage_canceled = True
        opp_deck.pop(0)
    # Second On Attack Burn 1
    if opp_deck[0] == "DMG":
        second_on_attack_burn_damage = 1
        opp_deck.pop(0)
    else:
        burn_damage_canceled = True
        opp_deck.pop(0)
    # First Cancel Burn for 2
    if burn_damage_canceled:
        for value in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                first_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                first_cancel_burn_damage = 0
                break
    # Second Cancel Burn for 2
    if burn_damage_canceled:
        for value in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                second_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                second_cancel_burn_damage = 0
                break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            swing_damage_canceled = True
            break
    # First Cancel Burn for 2
    if swing_damage_canceled and not burn_damage_canceled:
        for value in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                first_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                first_cancel_burn_damage = 0
                break
    # Second Cancel Burn for 2
    if swing_damage_canceled and not burn_damage_canceled:
        for value in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                second_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                second_cancel_burn_damage = 0
                break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = first_on_attack_burn_damage + second_on_attack_burn_damage + first_cancel_burn_damage + second_cancel_burn_damage + swing_damage + refresh_penalty
    return damage_of_attack


def azusa_with_double_kaori():
    soul = 3
    restand_soul = 3
    cancel_burn_value = 2
    damage_canceled = False
    cancel_burn_resolved = False
    swing_1_damage = 0
    swing_2_damage = 0
    on_attack_burn_damage = 0
    first_cancel_burn_damage = 0
    second_cancel_burn_damage = 0

    # First On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage += 1
        opp_deck.pop(0)
    else:
        damage_canceled = True
        opp_deck.pop(0)
    # Second On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage += 1
        opp_deck.pop(0)
    else:
        damage_canceled = True
        opp_deck.pop(0)

    # First Cancel Burn for 2
    if damage_canceled:
        for cancel in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                first_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                first_cancel_burn_damage = 0
                break
    # Second Cancel Burn for 2
    if damage_canceled:
        for cancel in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                second_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                second_cancel_burn_damage = 0
                break
        cancel_burn_resolved = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
        restand_soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_1_damage += 1
            opp_deck.pop(0)
        else:
            swing_1_damage = 0
            opp_deck.pop(0)
            damage_canceled = True
            break

    # First Cancel Burn for 2
    if damage_canceled and not cancel_burn_resolved:
        for cancel in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                first_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                first_cancel_burn_damage = 0
                break
    # Second Cancel Burn for 2
    if damage_canceled and not cancel_burn_resolved:
        for cancel in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                second_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                second_cancel_burn_damage = 0
                break
        cancel_burn_resolved = True

    # Third On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage += 1
        opp_deck.pop(0)
    else:
        damage_canceled = True
        opp_deck.pop(0)

    # First Cancel Burn for 2
    if damage_canceled and not cancel_burn_resolved:
        for value in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                first_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                first_cancel_burn_damage = 0
                break
    # Second Cancel Burn for 2
    if damage_canceled and not cancel_burn_resolved:
        for value in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                second_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                second_cancel_burn_damage = 0
                break
        cancel_burn_resolved = True

    # Restand Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        restand_soul += 1
    for restand_soul in range(restand_soul):
        if opp_deck[0] == "DMG":
            swing_2_damage += 1
            opp_deck.pop(0)
        else:
            swing_2_damage = 0
            opp_deck.pop(0)
            damage_canceled = True
            break

    # First Cancel Burn for 2
    if damage_canceled and not cancel_burn_resolved:
        for value in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                first_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                first_cancel_burn_damage = 0
                break
    # Second Cancel Burn for 2
    if damage_canceled and not cancel_burn_resolved:
        for value in range(cancel_burn_value):
            if opp_deck[0] == "DMG":
                second_cancel_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                second_cancel_burn_damage = 0
                break

    damage_of_attack = on_attack_burn_damage + first_cancel_burn_damage + second_cancel_burn_damage + swing_1_damage + swing_2_damage
    return damage_of_attack


def aoyama3():
    swing_1_damage = 0
    swing_2_damage = 0
    soul = 3
    restand_soul = 3
    refresh_penalty = 0
    global deck_refreshed

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
        restand_soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_1_damage += 1
            opp_deck.pop(0)
        else:
            swing_1_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Top 2 check opponents deck
    if opp_deck[1] == "CX":
        opp_deck.pop(1)
    if opp_deck[0] == "CX":
        opp_deck.pop(0)
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        restand_soul += 1
    for restand_soul in range(restand_soul):
        if opp_deck[0] == "DMG":
            swing_2_damage += 1
            opp_deck.pop(0)
        else:
            swing_2_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_1_damage + swing_2_damage + refresh_penalty
    return damage_of_attack


def ayumu3():
    soul = 3
    swing_damage = 0
    damage_of_attack = 0
    refresh_penalty = 0
    global deck_refreshed

    # On Attack mill 3 for burns (Order Red>Yellow>Blue)
    index = own_deck.index("Red")
    if index <= 2:
        if opp_deck[0] == "DMG":
            damage_of_attack += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
    index = own_deck.index("Yellow")
    if index <= 2:
        if opp_deck[0] == "DMG":
            damage_of_attack += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
    index = own_deck.index("Blue")
    if index <= 2:
        if opp_deck[0] == "DMG":
            damage_of_attack += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
    del own_deck[:3]

    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    own_deck.pop(0)
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break

    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack += swing_damage + refresh_penalty
    return damage_of_attack


def yuuji3():
    soul = 3
    swing_damage = 0
    on_attack_burn_damage_1 = 0
    on_attack_burn_damage_2 = 0
    musashi_burn_value = 0
    musashi_burn_damage = 0
    musashi_burn_primed = False
    musashi_burn_resolved = False
    refresh_penalty = 0
    global deck_refreshed

    # On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage_1 += 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage_1 = 0
        musashi_burn_primed = True
        opp_deck.pop(0)
    # On Attack Burn 2
    if opp_deck[0] == "DMG":
        on_attack_burn_damage_2 += 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage_2 = 0
        musashi_burn_primed = True
        opp_deck.pop(0)
    # First musashi burn check
    if musashi_burn_primed:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break
        musashi_burn_resolved = True
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    own_deck.pop(0)
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            musashi_burn_primed = True
            break
    # Second Musashi Burn check
    if musashi_burn_primed and not musashi_burn_resolved:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = on_attack_burn_damage_1 + on_attack_burn_damage_2 + musashi_burn_damage + swing_damage + refresh_penalty
    return damage_of_attack


def zls_sakura3():
    soul = 3
    second_burn_value = 2
    first_burn_canceled = False
    second_burn_canceled = False
    swing_damage = 0
    first_burn_damage = 0
    second_burn_damage = 0
    top_deck_clock_kick = 0
    refresh_penalty = 0
    global deck_refreshed

    # First Burn
    if opp_deck[0] == "DMG":
        first_burn_damage = 1
        opp_deck.pop(0)
    else:
        first_burn_canceled = True
        opp_deck.pop(0)
    # Second Burn
    if first_burn_canceled:
        for burn in range(second_burn_value):
            if opp_deck[0] == "DMG":
                second_burn_damage += 1
                opp_deck.pop(0)
            else:
                opp_deck.pop(0)
                second_burn_damage = 0
                second_burn_canceled = True
                break
    # Clock kick top 3 cards of opp deck
    if second_burn_canceled:
        del opp_deck[:3]
        top_deck_clock_kick = 3
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + first_burn_damage + second_burn_damage + top_deck_clock_kick + refresh_penalty
    return damage_of_attack


def zls_sakura_assist():
    damage_of_attack = 0

    # Check top 3 of opponents deck for cx/dmg on CX-Play (removing DMG)
    if opp_deck[2] == "DMG":
        opp_deck.pop(2)
    if opp_deck[1] == "DMG":
        opp_deck.pop(1)
    if opp_deck[0] == "DMG":
        opp_deck.pop(0)

    return damage_of_attack


def shiki2():
    soul = 2
    damage_of_attack = 0
    refresh_penalty = 0
    global deck_refreshed

    # Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    # Deal 1 Damage X times
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            damage_of_attack += 1
        else:
            opp_deck.pop(0)
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = damage_of_attack + refresh_penalty
    return damage_of_attack


def shiki3():
    soul = 3
    damage_of_attack = 0
    refresh_penalty = 0
    global deck_refreshed

    # Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    # Deal 1 Damage X times
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            damage_of_attack += 1
        else:
            opp_deck.pop(0)
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = damage_of_attack + refresh_penalty
    return damage_of_attack


def alicization_kirito3():
    soul = 3
    swing_damage = 0
    burn_value = 3
    on_reverse_burn_damage_1 = 0
    on_reverse_burn_damage_2 = 0
    refresh_penalty = 0
    global deck_refreshed

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # On Reverse Burn 1
    if opp_deck[0] == "DMG":
        on_reverse_burn_damage_1 += 1
        opp_deck.pop(0)
    else:
        on_reverse_burn_damage_1 = 0
        opp_deck.pop(0)
    # On Reverse Burn 3
    for burn_value in range(burn_value):
        if opp_deck[0] == "DMG":
            on_reverse_burn_damage_2 += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            on_reverse_burn_damage_2 = 0
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + on_reverse_burn_damage_1 + on_reverse_burn_damage_2 + refresh_penalty
    return damage_of_attack


def alice_musashi3():
    soul = 3
    swing_damage = 0
    on_attack_burn_damage = 0
    musashi_burn_value = 0
    musashi_burn_damage = 0
    musashi_burn_primed = False
    musashi_burn_resolved = False
    refresh_penalty = 0
    global deck_refreshed

    # On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage += 1
        opp_deck.pop(0)
    else:
        on_attack_burn_damage = 0
        musashi_burn_primed = True
        opp_deck.pop(0)
    # First musashi burn check
    if musashi_burn_primed:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break
        musashi_burn_resolved = True
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    own_deck.pop(0)
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            musashi_burn_primed = True
            break
    # Second Musashi Burn check
    if musashi_burn_primed and not musashi_burn_resolved:
        if own_deck[0] == "lvl0":
            musashi_burn_value = 1
            own_deck.pop(0)
        elif own_deck[0] == "lvl1":
            musashi_burn_value = 2
            own_deck.pop(0)
        elif own_deck[0] == "lvl2":
            musashi_burn_value = 3
            own_deck.pop(0)
        else:
            musashi_burn_value = 4
            own_deck.pop(0)
        for musashi_burn in range(musashi_burn_value):
            if opp_deck[0] == "DMG":
                musashi_burn_damage += 1
                opp_deck.pop(0)
            else:
                musashi_burn_damage = 0
                opp_deck.pop(0)
                break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = on_attack_burn_damage + musashi_burn_damage + swing_damage + refresh_penalty
    return damage_of_attack


def saekano_megumi3():
    soul = 3
    swing_damage = 0
    on_attack_burn_value = 3
    on_attack_burn_damage = 0
    on_attack_burn_damage_guaranteed = 0
    refresh_penalty = 0
    global deck_refreshed

    # On Attack Burn 3
    for burn in range(on_attack_burn_value):
        if opp_deck[0] == "lvl0":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        elif opp_deck[0] == "lvl1":
            on_attack_burn_damage_guaranteed += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            on_attack_burn_damage = 0
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "lvl0" or opp_deck[0] == "lvl1":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = on_attack_burn_damage + swing_damage + on_attack_burn_damage_guaranteed + refresh_penalty
    return damage_of_attack


def kanaho_and_takame3():
    kanaho_soul = 3
    takame_soul = 3
    takame_burn_value = 2
    kanaho_swing_damage = 0
    takame_swing_damage = 0
    takame_burn_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # Kanaho Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        kanaho_soul += 1
    for soul in range(kanaho_soul):
        if opp_deck[0] == "DMG":
            kanaho_swing_damage += 1
            opp_deck.pop(0)
        else:
            kanaho_swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Takame on attack burn
    for burn_value in range(takame_burn_value):
        if opp_deck[0] == "DMG":
            takame_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            takame_burn_damage = 0
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Takame Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        takame_soul += 1
    for soul in range(takame_soul):
        if opp_deck[0] == "DMG":
            takame_swing_damage += 1
            opp_deck.pop(0)
        else:
            takame_swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = kanaho_swing_damage + takame_burn_damage + takame_swing_damage + refresh_penalty
    return damage_of_attack


def restand_yuyu3():
    soul = 3
    restand_soul = 3
    swing_damage = 0
    second_swing_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # First Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
        restand_soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Restand Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        restand_soul += 1
    for restand_soul in range(restand_soul):
        if opp_deck[0] == "DMG":
            second_swing_damage += 1
            opp_deck.pop(0)
        else:
            second_swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + second_swing_damage + refresh_penalty
    return damage_of_attack


def burn_yuyu3():
    soul = 3
    first_burn_value = 3
    second_burn_value = 3
    swing_damage = 0
    first_burn_damage = 1
    second_burn_damage = 1
    refresh_penalty = 0
    global deck_refreshed

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # First burn
    for first_burn in range(first_burn_value):
        if opp_deck[0] == "DMG":
            first_burn_damage += 1
            opp_deck.pop(0)
        else:
            first_burn_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Second burn
    for second_burn in range(second_burn_value):
        if opp_deck[0] == "DMG":
            second_burn_damage += 1
            opp_deck.pop(0)
        else:
            second_burn_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + first_burn_damage + second_burn_damage + refresh_penalty
    return damage_of_attack


def quints_set2_itsuki():
    soul = 3
    swing_damage = 0
    burn_value = 4
    burn_1_damage = 0
    burn_2_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # Burn 1
    if opp_deck[0] == "DMG":
        burn_1_damage += 1
        opp_deck.pop(0)
    else:
        burn_1_damage = 0
        opp_deck.pop(0)
    # Burn 4
    for burn_value in range(burn_value):
        if opp_deck[0] == "DMG":
            burn_2_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
            burn_2_damage = 0
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + burn_1_damage + burn_2_damage + refresh_penalty
    return damage_of_attack


def pecorine():
    soul = 3
    swing_damage = 0
    icy_tail_value = 2
    first_icy_tail_damage = 0
    second_icy_tail_damage = 0
    third_icy_tail_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # Icy-Tail for 2 from top
    cx_hits = opp_deck[:icy_tail_value].count("CX")
    del opp_deck[:icy_tail_value]
    for climax in range(cx_hits):
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            first_icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            first_icy_tail_damage = 0
            break
    # Icy-Tail for 2 from top
    cx_hits = opp_deck[:icy_tail_value].count("CX")
    del opp_deck[:icy_tail_value]
    for climax in range(cx_hits):
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            second_icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            second_icy_tail_damage = 0
            break
    # Icy-Tail for 2 from top
    cx_hits = opp_deck[:icy_tail_value].count("CX")
    del opp_deck[:icy_tail_value]
    for climax in range(cx_hits):
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            third_icy_tail_damage += 1
        else:
            opp_deck.pop(0)
            third_icy_tail_damage = 0
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + refresh_penalty + first_icy_tail_damage + second_icy_tail_damage + third_icy_tail_damage
    return damage_of_attack


def yuni():
    swing_damage = 0
    soul = 3
    refresh_penalty = 0
    global deck_refreshed

    # Top 3 check opponents deck
    if opp_deck[2] == "CX":
        opp_deck.pop(2)
    if opp_deck[1] == "CX":
        opp_deck.pop(1)
    if opp_deck[0] == "CX":
        opp_deck.pop(0)
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_damage += 1
            opp_deck.pop(0)
        else:
            swing_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = swing_damage + refresh_penalty
    return damage_of_attack


def cip_llenn():
    cip_burn_damage = 0

    # CIP Mill 3 for burn, if 0 whiffs
    whiffs = own_deck[:3].count("CX")
    del own_deck[:3]
    if whiffs == 0:
        if opp_deck[0] == "DMG":
            opp_deck.pop(0)
            cip_burn_damage += 1
        else:
            opp_deck.pop(0)
            cip_burn_damage = 0

    damage_of_attack = cip_burn_damage
    return damage_of_attack


def llenn_plus_event():
    soul = 3
    restand_soul = 3
    swing_1_damage = 0
    swing_2_damage = 0
    on_attack_burn_damage = 0
    damage_canceled = False
    refresh_penalty = 0
    global deck_refreshed

    # On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage += 1
        opp_deck.pop(0)
    else:
        opp_deck.pop(0)
        damage_canceled = True
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
        restand_soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_1_damage += 1
            opp_deck.pop(0)
        else:
            swing_1_damage = 0
            opp_deck.pop(0)
            damage_canceled = True
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Restand through event, if damage got canceled
    if damage_canceled:
        # On Attack Burn 1
        if opp_deck[0] == "DMG":
            on_attack_burn_damage += 1
            opp_deck.pop(0)
        else:
            opp_deck.pop(0)
        # Refresh-Check
        if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
            opp_deck.pop(0)
            refresh_penalty = 1
            deck_refreshed = True

        # Vanilla Swing + Triggercheck
        trigger = random.randint(1, int(own_number_of_cards))
        if trigger <= own_soul_triggers:
            restand_soul += 1
        for soul in range(restand_soul):
            if opp_deck[0] == "DMG":
                swing_2_damage += 1
                opp_deck.pop(0)
            else:
                swing_2_damage = 0
                opp_deck.pop(0)
                break
        # Refresh-Check
        if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
            opp_deck.pop(0)
            refresh_penalty = 1
            deck_refreshed = True

    damage_of_attack = on_attack_burn_damage + swing_1_damage + swing_2_damage + refresh_penalty
    return damage_of_attack


def llenn3():
    soul = 3
    swing_1_damage = 0
    on_attack_burn_damage = 0
    refresh_penalty = 0
    global deck_refreshed

    # On Attack Burn 1
    if opp_deck[0] == "DMG":
        on_attack_burn_damage += 1
        opp_deck.pop(0)
    else:
        opp_deck.pop(0)
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_1_damage += 1
            opp_deck.pop(0)
        else:
            swing_1_damage = 0
            opp_deck.pop(0)
            break
    # Refresh-Check
    if len(opp_deck) <= decksize_opp_second_deck and not deck_refreshed:
        opp_deck.pop(0)
        refresh_penalty = 1
        deck_refreshed = True

    damage_of_attack = on_attack_burn_damage + swing_1_damage + refresh_penalty
    return damage_of_attack


def ias_yayoi():
    swing_1_damage = 0
    swing_2_damage = 0
    soul = 3
    restand_soul = 3
    shuffle_back = 3

    # Vanilla Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        soul += 1
        restand_soul += 1
    for soul in range(soul):
        if opp_deck[0] == "DMG":
            swing_1_damage += 1
            opp_deck.pop(0)
        else:
            swing_1_damage = 0
            opp_deck.pop(0)
            break

    # Shuffling back damage
    for char in range(shuffle_back):
        opp_deck.append("DMG")
    random.shuffle(opp_deck)

    # Restand Swing + Triggercheck
    trigger = random.randint(1, int(own_number_of_cards))
    if trigger <= own_soul_triggers:
        restand_soul += 1
    for restand_soul in range(restand_soul):
        if opp_deck[0] == "DMG":
            swing_2_damage += 1
            opp_deck.pop(0)
        else:
            swing_2_damage = 0
            opp_deck.pop(0)
            break

    damage_of_attack = swing_1_damage + swing_2_damage
    return damage_of_attack
