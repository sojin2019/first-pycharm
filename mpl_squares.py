import matplotlib.pyplot as plt


class testplot:

    def __init__(self):
        squares = [1, 4, 9, 16, 25]

        plt.plot(squares)
        plt.savefig('example_plot_1.png')
        print('plot test')
        plt.show()




