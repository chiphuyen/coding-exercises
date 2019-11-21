""" Ghost is a word game in which players take turns adding letters to a
growing word fragment, trying not to be the one to complete a valid word.

You lose if you have made a complete word or the letter you added
makes the current word fragment a prefix that doesn't exist.

This algorithm uses min max strategy with alpha-beta pruning to always
beat humans in the game of Ghost.

This is a fun exercise to use Trie.

I wrote this in my 2nd year in college for fun so
please don't judge me too harsh.
"""

import random
import sys

from trie import Trie

HUMAN = 0
COMP = 1
DISCOUNT = 2
REWARD = 100


class Ghost:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.curr_word = ''

    def reset(self):
        self.curr_word = ''

    def human_play(self):
        char = input("Enter your letter: ").strip()
        while not char or len(char) > 1 or not char.isalpha():
            char = input("Please enter a valid character: ").strip()
        self.curr_word += char

    def computer_play(self):
        char = self.get_char()
        print(f'Current string: {self.curr_word}\nComputer picked {char}')
        self.curr_word += char

    def get_char(self):
        """ Pick the most promising next character to play for computer
        """
        def recurse(curr_word, dictionary, player, alpha, beta):
            if self.must_end(curr_word):
                if player == HUMAN:
                    return (-REWARD, None)
                return (REWARD, None)

            legal_chars = dictionary.get_children(curr_word)
            if not legal_chars:
                if player == HUMAN:
                    return (REWARD, None)
                return (-REWARD, None)

            best_indices = []
            # This is where the min max happens
            if player == COMP:  # maximize the computer's utility
                next_word = curr_word + legal_chars[0]
                alpha = recurse(next_word, dictionary, HUMAN, alpha, beta)[0]
                best_indices.append(0)
                for index in range(1, len(legal_chars)):
                    next_word = curr_word + legal_chars[index]
                    score = recurse(next_word, dictionary,
                                    HUMAN, alpha, beta)[0]
                    if score > alpha:
                        best_indices = [index]
                        alpha = score
                        if alpha > beta:
                            break
                    if score == alpha:
                        best_indices.append(index)
                best_idx = random.choice(best_indices)
                return (alpha, legal_chars[best_idx])
            else:  # minimize the computer's utility
                next_word = ''.join((curr_word, legal_chars[0]))
                """ add DISCOUNT to score so that if computer must lose,
                it would take more steps to lose (make it harder for users to win)
                """
                beta = DISCOUNT + recurse(next_word,
                                          dictionary,
                                          COMP,
                                          alpha,
                                          beta)[0]
                best_indices.append(0)
                for index in range(1, len(legal_chars)):
                    next_word = curr_word + legal_chars[index]
                    score = DISCOUNT + recurse(next_word,
                                               dictionary,
                                               COMP,
                                               alpha,
                                               beta)[0]
                    if score < beta:
                        best_indices = [index]
                        beta = score
                        if alpha > beta:
                            break
                    if score == beta:
                        best_indices.append(index)
                best_idx = random.choice(best_indices)
                return (beta, legal_chars[best_idx])

        _, char = recurse(self.curr_word,
                          self.dictionary,
                          COMP,
                          -float('inf'),
                          float('inf'))
        return char

    def check_result(self, prefix, player):
        result = self.must_end(prefix)
        if not result:
            return 0
        if result == -1:
            print(f'No word starts with {prefix}.')
        elif result == 1:
            print(f'{prefix} is a legitimate word.')
        if player == HUMAN:
            print('Puny human you lost!')
        else:
            print('This is impossible. You won!')
        return result

    def must_end(self, prefix):
        if not self.dictionary.has_prefix(prefix):
            return -1
        if len(prefix) > 2 and self.dictionary.has_word(prefix):
            return 1
        return 0


def intro():
    print("Welcome to the game of Ghost.\n"
          "Players take turns adding letters to a growing word fragment, "
          "trying not to be the first one to complete a valid word.\n"
          "You lose if you have made a complete word or the letter you added "
          "makes the current word fragment a prefix that doesn't exist.")


def main():
    dictionary = Trie('data/dictionary.txt')
    intro()
    replay = True
    ghost = Ghost(dictionary)

    while replay:
        print('-' * 60)
        print("Let's start!\nYou go first.")
        ghost.human_play()
        while True:
            ghost.computer_play()
            if ghost.check_result(ghost.curr_word, COMP):
                break

            print("------------------------")
            print("Your turn\nCurrent string:", ghost.curr_word)
            ghost.human_play()
            if ghost.check_result(ghost.curr_word, HUMAN):
                break

        # Enter nothing or anything starts with 'n' to quit.
        ans = input('Do you want to play another game? (Y/N) ').lower().strip()
        if not ans or ans[0] == 'n':
            print('Thanks for playing!')
            replay = False
        ghost.reset()


# run the program
if __name__ == '__main__':
    main()
