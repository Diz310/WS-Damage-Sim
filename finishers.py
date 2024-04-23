def csm_choice():
    attack_damage = 0

    attack_damage += burn(1)
    attack_damage += swing(3)
    attack_damage += burn(2)
    opp_deck.insert(0, "DMG")

    return attack_damage


def csm_topdecker():
    attack_damage = 0

    opp_deck.insert(0, "DMG")
    opp_deck.insert(0, "DMG")
    attack_damage += swing(4)

    return attack_damage


def shana():
    attack_damage = 0
    global damage_canceled
    damage_canceled = False

    attack_damage += burn(4)
    if damage_canceled:
        attack_damage += shuffleback(4)
    attack_damage += swing(3)

    return attack_damage


def movie_ichika():
    attack_damage = 0
    global damage_canceled
    damage_canceled = False

    attack_damage += swing(3)
    if damage_canceled:
        attack_damage += shuffleback(4)
        attack_damage += burn(4)

    return attack_damage


def set1_ichika():
    attack_damage = 0
    refresh_penalty = 0
    global damage_canceled
    damage_canceled = False

    attack_damage += swing(3)
    if damage_canceled:
        attack_damage += burn(2)
        attack_damage += burn(2)

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    return attack_damage + refresh_penalty


def laplus():
    attack_damage = 0
    refresh_penalty = 0
    global damage_canceled
    damage_canceled = False

    attack_damage += swing(3)
    if damage_canceled:
        attack_damage += burn(1)
        attack_damage += burn(1)

    if len(opp_deck) == 0:
        refresh_penalty += refresh()

    return attack_damage + refresh_penalty


def marine():
    return burn(2) + swing(3)


def fourth_gen_event():
    return burn(4) + burn(4)


def lsp_ren():
    return burn(3) + swing(3)


def kaguya():
    return burn(1) + swing(3) + burn(1)


def dark_sakura():
    return icytail(6) + swing(3)


def sinon_icytail():
    return icytail(7) + swing(3)


def fubuki():
    return burn(2) + shuffleback(2) + swing(3)


def csm_aki():
    return ping_icytail(4) + swing(3)


def aegis_anna():
    return ping_icytail(6) + swing(3)


def bd_moca():
    return moca(2) + swing(3)


def movie_itsuki():
    return burn(3) + moca(2) + swing(3)