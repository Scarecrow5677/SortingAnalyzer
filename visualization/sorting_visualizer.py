import matplotlib.pyplot as plt
from algorithms import sorting

closed = False

#stop the visualization when the plt window is closed by the user

def on_close(event):
    global closed
    closed = True

#special list subclass that allows us to visualize the sorting process

class VisualizerList(list):

    def __init__(self, iterable, draw_function = None, delay = 0.0):
        super().__init__(iterable)

        #function that is used to visualize every step

        self.draw_function = draw_function

        #delay between the sorting steps

        self.delay = delay

    def __setitem__(self, index, value):
        super().__setitem__(index, value)

        #mark elements that are specifically set 

        if self.draw_function and not isinstance(index, slice):
            self.draw_function(self, index, -1)
            plt.pause(self.delay)

    def swap(self, i, j):

        #regular swap

        temp = self[i]
        self[i] = self[j]
        self[j] = temp

        #mark the elements which were swapped

        if self.draw_function:
            self.draw_function(self, i, j)

            #wait until the next step

            plt.pause(self.delay)
    
#function used for visualization of every step

def draw_data(data, idx1, idx2):

    if closed:
        raise RuntimeError("Visualization closed by the user")

    plt.clf()

    #initialize all bars as blue and set the changed ones to red

    colors = ['blue'] * len(data)
    if idx1 >= 0:
        colors[idx1] = 'red'
    if idx2 >= 0:
        colors[idx2] = 'red'
    plt.bar(range(len(data)), data, color=colors)
    plt.pause(0.001)

#starts the visualization and calls the sorting method

def visualize(data, alg):

    global closed
    closed = False

    plt.ion()
    fig = plt.figure()
    fig.canvas.mpl_connect("close_event", on_close)

    draw_data(data, -1, -1)

    #calls the sorting function "alg" in sorting.py

    try:
        getattr(sorting, alg)(data)
    except RuntimeError as _:
        pass

    plt.ioff()

    if not closed:
        plt.show()
