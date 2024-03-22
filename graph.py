import re
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
}

allowed_words = [
    'abs',
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
]
def graphit(eq):
    def string2func(string):
        ''' evaluates the string and returns a function of x '''
        # find all words and check if all are allowed:
        for word in re.findall('[a-zA-Z_]+', string):
            if word not in allowed_words:
                raise ValueError(
                    '"{}" is forbidden to use in math expression'.format(word)
                )

        for old, new in replacements.items():
            string = string.replace(old, new)

        def func(x):
            return eval(string)

        return func



    func = string2func(eq)

    fig, ax = plt.subplots()
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    x = np.linspace(-100, 100, 1000)
    plt.xlim(-30, 30)
    plt.ylim(-30, 30)
    plt.plot(x, func(x))
    ax.minorticks_on()
    ax.grid(which='major', linewidth='0.15', color='black')
    ax.grid(which='minor', linewidth='0.1', color='black')
    plt.show()