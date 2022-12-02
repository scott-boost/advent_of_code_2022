from enum import Enum
from pathlib import Path


class Weapon(str, Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"


class MyOutcome(str, Enum):
    LOSE = "LOSE"
    TIE = "TIE"
    WIN = "WIN"


MY_WEAPON_TO_POINTS = {
    Weapon.ROCK: 1,
    Weapon.PAPER: 2,
    Weapon.SCISSORS: 3,
}

OUTCOME_TO_POINTS = {
    MyOutcome.LOSE: 0,
    MyOutcome.TIE: 3,
    MyOutcome.WIN: 6,
}

ENCRYPTED_OPPONENT_WEAPON_TO_WEAPON = {
    "A": Weapon.ROCK,
    "B": Weapon.PAPER,
    "C": Weapon.SCISSORS,
}


def part_a(input_contents: str):
    encrypted_my_weapon_to_weapon = {
        "X": Weapon.ROCK,
        "Y": Weapon.PAPER,
        "Z": Weapon.SCISSORS,
    }
    weapons_to_outcome = {
        # Opponent        Me                My Outcome
        (Weapon.ROCK,     Weapon.ROCK):     MyOutcome.TIE,
        (Weapon.PAPER,    Weapon.PAPER):    MyOutcome.TIE,
        (Weapon.SCISSORS, Weapon.SCISSORS): MyOutcome.TIE,

        (Weapon.ROCK,     Weapon.SCISSORS): MyOutcome.LOSE,
        (Weapon.PAPER,    Weapon.ROCK):     MyOutcome.LOSE,
        (Weapon.SCISSORS, Weapon.PAPER):    MyOutcome.LOSE,

        (Weapon.ROCK,     Weapon.PAPER):    MyOutcome.WIN,
        (Weapon.PAPER,    Weapon.SCISSORS): MyOutcome.WIN,
        (Weapon.SCISSORS, Weapon.ROCK):     MyOutcome.WIN,
    }
    total = 0
    for rpc_round in input_contents.split("\n"):
        encrypted_opponent_weapon, encrypted_my_weapon = rpc_round.split(" ")

        opponent_weapon = ENCRYPTED_OPPONENT_WEAPON_TO_WEAPON[encrypted_opponent_weapon]
        my_weapon = encrypted_my_weapon_to_weapon[encrypted_my_weapon]

        outcome = weapons_to_outcome[(opponent_weapon, my_weapon)]

        score = MY_WEAPON_TO_POINTS[my_weapon] + OUTCOME_TO_POINTS[outcome]
        total += score

    return total


def part_b(input_contents: str):
    encrypted_outcome_to_outcome = {
        "X": MyOutcome.LOSE,
        "Y": MyOutcome.TIE,
        "Z": MyOutcome.WIN,
    }
    opponent_weapon_outcome_to_my_weapon = {
        (Weapon.ROCK, MyOutcome.TIE): Weapon.ROCK,
        (Weapon.PAPER, MyOutcome.TIE): Weapon.PAPER,
        (Weapon.SCISSORS, MyOutcome.TIE): Weapon.SCISSORS,

        (Weapon.ROCK, MyOutcome.WIN): Weapon.PAPER,
        (Weapon.PAPER, MyOutcome.WIN): Weapon.SCISSORS,
        (Weapon.SCISSORS, MyOutcome.WIN): Weapon.ROCK,

        (Weapon.ROCK, MyOutcome.LOSE): Weapon.SCISSORS,
        (Weapon.PAPER, MyOutcome.LOSE): Weapon.ROCK,
        (Weapon.SCISSORS, MyOutcome.LOSE): Weapon.PAPER,
    }
    total = 0
    for rpc_round in input_contents.split("\n"):
        encrypted_opponent_weapon, encrypted_outcome = rpc_round.split(" ")

        opponent_weapon = ENCRYPTED_OPPONENT_WEAPON_TO_WEAPON[encrypted_opponent_weapon]
        outcome = encrypted_outcome_to_outcome[encrypted_outcome]

        my_weapon = opponent_weapon_outcome_to_my_weapon[(opponent_weapon, outcome)]

        score = MY_WEAPON_TO_POINTS[my_weapon] + OUTCOME_TO_POINTS[outcome]
        total += score

    return total


if __name__ == "__main__":
    contents = Path("02_input.txt").read_text().strip()
    print(part_a(contents))
    print(part_b(contents))
