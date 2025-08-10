# SortingAnalyzer
Tool for comparing some sorting algorithms regarding their time complexity and visualizing the sorting process

A small, educational Tkinter GUI that lets you benchmark classic sorting algorithms and animate single sorting runs with Matplotlib. Built to be clear and extendable — good for learning algorithm behaviour, benchmarking, and creating visual demos.

---

## Features
- Interactive GUI (Tkinter) for:
  - Visualizing single sorting runs with step-by-step animation
  - Comparing runtime of multiple algorithms on the same input and plotting bar charts
  - Comparing the runtime of a single algorithm on different inputs
- Implemented algorithms:
  - Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, Bucket Sort, Counting Sort
- Adjustable visualization speed (delay)
- Simple benchmark plotting (Matplotlib) for quick comparisons

---

Installation

  Clone the repository:

    git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git 

    cd YOUR_REPO

  Install dependencies:

    pip install -r requirements.txt

---

Starting the program

python Sorter.py

Use the GUI to:

  -Analyze the runtime of a single algorithm with different input sizes by choosing Analyze -> Analyze Single Algorithm and then choose your algorithm
  -Analyze and compare the runtime of multiple algorithms on the same input by choosing Analyze -> Analyze Multiple Algorithms and then choose your algorithms
  -Visualize a single algorithm by choosing Visualize and then choose your algorithm

---
