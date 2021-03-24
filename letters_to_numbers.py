# Helper function to convert a letter to its numerical equivalent (1-26)
def l_t_n(letter):
    number = ord(letter) - 64
    return number


def n_t_l(number):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
    letter = letters[number-1]
    return letter
