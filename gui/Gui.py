import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import Sorter
import random
from visualization import plot
from algorithms import sorting
from visualization import sorting_visualizer

#define tkinter fonts for buttons and labels

buttonfont = ("Arial", 20)
labelfont = ("Arial", 40)

#controller class that holds the single pages of the gui

class Gui:

    def __init__(self):

        self.root = tk.Tk(className="Sorting Algorithm Analyzer")
        self.root.geometry("900x600")

        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TButton", font = buttonfont, borderwidth = 40, padding = 15)
        style.configure("TCheckbutton", font = buttonfont, borderwidth = 40, padding = 15)

        #"Masterframe" that will act as the root for all the pages

        container = tk.Frame(self.root)
        container.pack(fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Initialize all the pages and safe them in the frames dict

        self.frames = {}

        for F in (StartPage, AnalyzePage, AnalyzeSinglePage, AnalyzeMultiplePage, VisualizePage):
            page = F(container, self)
            self.frames[F] = page
            page.frame.grid(row = 0, column = 0, sticky = "nsew")

        #Show the Startpage and start the tkinter mainloop

        self.showFrame(StartPage)

        self.root.mainloop()

    #Function used to switch pages

    def showFrame(self, page_class):
        frame = self.frames[page_class]
        frame.frame.tkraise()

    #Function used to close the program

    def exit(self):
        warning = messagebox.askquestion("Exit", "Are you sure you want to close the program?")
        if warning == "yes":
            exit()
        else:
            return

class StartPage:

    def __init__(self, root, controller):

        self.controller = controller

        #initialize Frame and set a label

        self.frame = ttk.Frame(root)

        self.label = ttk.Label(self.frame, text = "Sorting Algorithm Analyzer", font = labelfont)
        self.label.pack(pady = 25, padx = 10)

        #Buttons used to go to another page by calling the showFrame method in the controller

        self.button_analyze = ttk.Button(self.frame, text = "Analyze", command = lambda: controller.showFrame(AnalyzePage))
        self.button_analyze.pack(pady = 10)

        self.button_visualize = ttk.Button(self.frame, text = "Visualize", command = lambda: controller.showFrame(VisualizePage))
        self.button_visualize.pack(pady = 10)

        #Button to close the program

        self.exit_button = ttk.Button(self.frame, text = "Exit", command = controller.exit)
        self.exit_button.pack(pady = 10)

class AnalyzePage:

    def __init__(self, root, controller):

        self.controller = controller

        #initialize Frame and set a label

        self.frame = ttk.Frame(root)

        self.label = ttk.Label(self.frame, text = "Analyze", font = labelfont)
        self.label.pack(pady = 25, padx = 10)

        #Buttons used to go to another page by calling the showFrame method in the controller

        self.button_analyze_single = ttk.Button(self.frame, text = "Analyze Single Algorithm", command = lambda: controller.showFrame(AnalyzeSinglePage))
        self.button_analyze_single.pack(pady = 10)

        self.button_analyze_multiple = ttk.Button(self.frame, text = "Compare Multiple Algorithms", command = lambda: controller.showFrame(AnalyzeMultiplePage))
        self.button_analyze_multiple.pack(pady = 10)

        #Button to go back to the startpage

        self.button_back = ttk.Button(self.frame, text = "Back", command = lambda: controller.showFrame(StartPage))
        self.button_back.pack(pady = 10)
        

class AnalyzeSinglePage:

    def __init__(self, root, controller):

        self.controller = controller

        #initialize Frame and set a label

        self.frame = ttk.Frame(root)

        self.label = ttk.Label(self.frame, text = "Choose an Algorithm", font = labelfont, anchor="center")
        self.label.grid(row = 0, column = 0, columnspan= 3, pady = 25, sticky = "nsew")
        self.frame.grid_columnconfigure(0, weight=1)

        #Place buttons representing the different algorithms in a 3x3 grid

        self.buttons = []

        row = 1
        col = 0

        for label in ("Bubblesort", "Bucketsort", "Countingsort", "Heapsort" ,"Insertionsort", "Mergesort", "Quicksort", "Selectionsort"):

            #call the choose_algorithm function on click with the algorithm string as parameter

            btn = ttk.Button(self.frame, text = label, command = lambda s = label: self.choose_algorithm(s))
            btn.grid(column = col, row = row, padx = 5, pady = 10, sticky = "nsew")
            self.buttons.append(btn)
            col += 1
            if col == 3:
                row += 1
                col = 0

        #Button to go back to the analyzepage

        self.button_back = ttk.Button(self.frame, text = "Back", command = lambda: controller.showFrame(AnalyzePage))
        self.button_back.grid(column = 2, row = 3, padx = 5, pady = 10, sticky = "nsew")

    def choose_algorithm(self, alg):

        #If Bucketsort was selected, we ask the user which algorithm should be used to sort the Buckets

        bucket_sort_alg = 0
        
        if alg == "Bucketsort":
            if (bucket_sort_alg := simpledialog.askinteger("Input", "Which algorithm do you want to use to sort the buckets? The input should be an integer between 1 (Bubblesort) and 8 (Selectionsort).",
                                                            minvalue=1, maxvalue=8, parent = self.frame)) is None:
                return
            
        #ask the user how many lists should be sorted
            
        iterations = 0

        if (iterations := simpledialog.askinteger("Input", "How many different inputs (between 1 and 20) should be sorted?", minvalue=1, maxvalue = 20, parent = self.frame)) is None:
            return
        
        #ask the user how long each input should be

        input_lengths = []

        for i in range(iterations):
            input_lengths.append(simpledialog.askinteger("Input", f"How many integers (between 1 and 10.000.000) should be sorted in iteration {i} (Warning: Values over 100.000 can lead to very long waiting times with Insertion-, Selection- and Bubblesort)", minvalue=1, maxvalue = 10000000, parent = self.frame))

            if input_lengths[i] is None:
                return
            
        #start the sorting and plot the results

        self.execute_single(alg, bucket_sort_alg, input_lengths)
    
    def execute_single(self, alg, bucketSortAlgInt, input_lengths):

        #convert the numeric input for the bucket_sort_alg into a string

        bucket_sort_alg = ""

        if bucketSortAlgInt != 0:
            bucket_sort_alg = ("Bubblesort", "Bucketsort", "Countingsort", "Heapsort" ,"Insertionsort", "Mergesort", "Quicksort", "Selectionsort")[bucketSortAlgInt-1]

        #sort the input lengths

        sorting.Quicksort(input_lengths)

        #in each iteration: create a random list and append the result of the measure function to times; Assertionerror is raised if the "sorted" list is not actually in ascending order

        times = []

        for i in range(len(input_lengths)):

            n = input_lengths[i]

            nums = []

            for _ in range(n):
                nums.append(random.randint(0, 1000000))

            if alg == "Countingsort":
                try:
                    times.append(Sorter.measure(alg, nums, 1000000))
                except RuntimeError:
                    del input_lengths[i]
                    messagebox.showinfo("Error", "An unknown error occured while sorting")
            elif alg == "Bucketsort":
                try:
                    times.append(Sorter.measure(alg, nums, bucket_sort_alg=bucket_sort_alg))
                except RuntimeError:
                    del input_lengths[i]
                    messagebox.showinfo("Error", "An unknown error occured while sorting")
            else:
                try:
                    times.append(Sorter.measure(alg, nums))
                except RuntimeError:
                    del input_lengths[i]
                    messagebox.showinfo("Error", "An unknown error occured while sorting")

        self.plot_results(times, input_lengths, alg)

    #call the plotting method

    def plot_results(self, times, iterations, alg):
        plot.barResultOneAlgorithmWithDifferentSIzes(alg, times, iterations)
        
class VisualizePage:

    def __init__(self, root, controller):

        self.controller = controller

        #initialize Frame and set a label

        self.frame = ttk.Frame(root)

        self.label = ttk.Label(self.frame, text = "Choose an Algorithm", font = labelfont, anchor="center")
        self.label.grid(row = 0, column = 0, columnspan= 3, pady = 25, sticky = "nsew")
        self.frame.grid_columnconfigure(0, weight=1)

        #Place buttons corresponding to all algorithms except Bucket- and countingsort in a 2x3 grid

        self.buttons = []

        row = 1
        col = 0

        for label in ("Bubblesort", "Heapsort" ,"Insertionsort", "Mergesort", "Quicksort", "Selectionsort"):

            #on click, call the execute method with the algorithm string as parameter

            btn = ttk.Button(self.frame, text = label, command = lambda s = label: self.execute(s))
            btn.grid(column = col, row = row, padx = 5, pady = 10, sticky = "nsew")
            self.buttons.append(btn)
            col += 1
            if col == 3:
                row += 1
                col = 0

        #button to go back to the Startpage

        self.button_back = ttk.Button(self.frame, text = "Back", command = lambda: controller.showFrame(StartPage))
        self.button_back.grid(column = 1, row = 3, padx = 5, pady = 10, sticky = "nsew")

    def execute(self, alg):

        #get the length of the list to be sorted

        length = 0

        if(length := simpledialog.askinteger("Input", "How many integers (between 1 and 100) should be sorted", minvalue=1, maxvalue=100)) is None:
            return
        
        #ask for the delay in-between steps

        delay = 0

        if(delay := simpledialog.askfloat("Input", "Choose the delay (at least 0.001) between steps while sorting", minvalue = 0.001, maxvalue = 1.0)) is None:
            return
        
        #create a randomized list
        
        nums = []

        for _ in range(length):
            nums.append(random.randint(1, 100))

        visual_list = sorting_visualizer.VisualizerList(nums, sorting_visualizer.draw_data, delay)

        #call the visualize method

        sorting_visualizer.visualize(visual_list, alg)

class AnalyzeMultiplePage:

    def __init__(self, root, controller):

        self.controller = controller

        #initialize Frame and set a label

        self.frame = ttk.Frame(root)

        self.label = ttk.Label(self.frame, text = "Choose your algorithms", font = labelfont, anchor = "center")
        self.label.grid(row = 0, column = 0, columnspan= 3, pady = 25, sticky = "nsew")
        self.frame.grid_columnconfigure(0, weight=1)

        #place checkbuttons for the different algorithms in a 3x3 grid

        self.algorithm_checkbuttons = []
        self.checkbutton_states = []

        row = 1
        col = 0

        for label in ("Bubblesort", "Bucketsort", "Countingsort", "Heapsort" ,"Insertionsort", "Mergesort", "Quicksort", "Selectionsort"):
            state = tk.IntVar()
            checkbtn = ttk.Checkbutton(self.frame, text = label, variable = state)
            checkbtn.grid(row = row, column= col, padx = 5, pady = 10, sticky = "nsew")
            self.algorithm_checkbuttons.append((checkbtn, label))
            self.checkbutton_states.append(state)

            col += 1
            if col == 3:
                col = 0
                row += 1

        #button to start the analysis with the checked algorithms

        self.button_start = ttk.Button(self.frame, text = "Start", command = lambda : self.execute_multiple())
        self.button_start.grid(row = row, column= col, padx = 5, pady = 10, sticky = "nsew")

        #button to go back to the analyzepage

        self.button_back = ttk.Button(self.frame, text = "Back", command = lambda: controller.showFrame(AnalyzePage))
        self.button_back.grid(row = 4, column= 1, padx = 5, pady = 10, sticky = "nsew")

    #function that returns the checked algorithms

    def get_chosen_algorithms(self):
        algorithms = []

        for i, state in enumerate(self.checkbutton_states):
            if state.get() == 1:
                algorithms.append(self.algorithm_checkbuttons[i][1])

        return algorithms
    
    def execute_multiple(self):
        times = []

        algorithms = self.get_chosen_algorithms()

        bucket_sort_alg = 0

        #get the length of the list that should be sorted

        n = 0

        if (n := simpledialog.askinteger("Input", "How many integers (between 1 and 10.000.000) should be sorted (Warning: Values over 100.000 can lead to very long waiting times with Insertion-, Selection- and Bubblesort)", minvalue=1, maxvalue=10000000)) is None:
            return
        
        #create the randomized list, each algorithm will be given a copy of this list for better comparison
        
        nums_base = []

        for _ in range(n):
            nums_base.append(random.randint(0, 1000000))

        #for eeach selected algorithm: create a copy of the list and append the result of measure to the times list

        for i in range(len(algorithms)):

            nums = nums_base.copy()

            #if Bucketsort was selected, ask for an algorithm to sort the buckets and convert it into a string

            alg = algorithms[i]

            if alg == "Bucketsort":
                if (bucket_sort_alg := simpledialog.askinteger("Input", "Which algorithm do you want to use to sort the buckets? The input should be an integer between 1 (Bubblesort) and 8 (Selectionsort).",
                                                            minvalue=1, maxvalue=8, parent = self.frame)) is None:
                        return    
                bucket_sort_alg = ("Bubblesort", "Bucketsort", "Countingsort", "Heapsort" ,"Insertionsort", "Mergesort", "Quicksort", "Selectionsort")[bucket_sort_alg-1]

            if alg == "Countingsort":
                try:
                    times.append(Sorter.measure(alg, nums, counting_sort_limit=1000000))
                except RuntimeError:
                    del algorithms[i]
                    messagebox.showinfo("Error", "An unknown error occured while sorting")
            elif alg == "Bucketsort":
                try:
                    times.append(Sorter.measure(alg, nums, bucket_sort_alg=bucket_sort_alg))
                except RuntimeError:
                    del algorithms[i]
                    messagebox.showinfo("Error", "An unknown error occured while sorting")
            else:
                try:
                    times.append(Sorter.measure(alg, nums))
                except RuntimeError:
                    del algorithms[i]
                    messagebox.showinfo("Error", "An unknown error occured while sorting")

        #sort the results in ascending order by time

        self.sort_algorithms_by_time(algorithms, times)

        #plot the results
                    
        self.plot_results(times, algorithms, n)

    def plot_results(self, times, algorithms, n):
        plot.barResultsOneInputSize(algorithms, times, n)

    def sort_algorithms_by_time(self, algorithms, times):

        #sort the algorithms with their corresponding times

        pairs = list(zip(algorithms, times))
        pairs.sort(key=lambda x: x[1])  # nach Zeit
        algorithms[:] = [alg for alg, t in pairs]
        times[:]      = [t   for alg, t in pairs]
