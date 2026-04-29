from os import urandom
from math import floor


def die(sides=10):
    return floor((int.from_bytes(urandom(1)) / 256) * sides) + 1


def roll(sides=10, explodes=False, count=1, drop_lowest=False, difficulty=0, max_count_twice=False,
         ones_clear_only_nominal=True, pattern="", modifier=0):
    """
    RPG dice simulation function. Default is 1d10
    :param sides: Number of sides of the die
    :param explodes: When max is rolled, do we reroll and add (or same in the other direction when min (1) is rolled). FICS system.
    :param count: Number of dice (by default the total will be returned)
    :param max_count_twice: For WtA20 Specialization, where each 10 is 2 successes
    :param difficulty: The difficulty to reach to mark successes. If equals to 0, the sum is computed
    :param ones_clear_only_nominal: Standard 1 remove 1 success. At True, makes this happens only to nominal difficulty scores.
    :param pattern: Pass a dice pattern among those: Sum of three 6-sided dice"3d6" "5d10/6" "4d6_" "2d4+4"
    :param drop_lowest: Typical use for D&D character creation (roll 4d6 and drop the lowest)
    :param modifier: modifier to apply to the total
    :return: the result of the roll
    """
    total = 0
    dice = []
    ones = []
    summary = []
    for i in range(count):
        score = die(sides=sides)
        if explodes:
            if score == sides:
                explosion = score
                while explosion == sides:
                    explosion = die(sides=sides)
                    score += explosion
            if score == 1:
                explosion = sides
                while explosion == sides:
                    explosion = die(sides=sides)
                    score -= explosion
        dice.append(score)
    if difficulty > 0:
        for d in dice:
            if d == 1:
                ones.append(1)
            if d >= difficulty:
                total += 1
                if max_count_twice:
                    if d == sides:
                        total += 1
        cnt1 = len(ones)
        for d in dice:
            if cnt1 > 0:
                if ones_clear_only_nominal:
                    if d == difficulty:
                        total -= 1
                        cnt1 -= 1
                else:
                    if d >= difficulty:
                        total -= 1
                        cnt1 -= 1
        if ones_clear_only_nominal:
            if total <= 0:
                total -= cnt1
        else:
            total -= cnt1
    elif drop_lowest:
        dice.sort()
        total = sum(dice[1:]) + modifier
    else:
        total = sum(dice) + modifier
    summary.append(f"Dice...... {dice}")
    summary.append(f"Botches... {ones}")
    # print("\n".join(summary))
    return total, summary
