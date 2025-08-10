import matplotlib.pyplot as plt

#plots the result times for the chosen algorithms over the same input size

def barResultsOneInputSize(algs, times, n):

    x = range(len(algs))

    plt.figure(figsize=(12,8))
    plt.bar(x, times, tick_label = algs)
    plt.xlabel("Algorithms")
    plt.ylabel("Time in ms")
    plt.title(f"Number of elements: {n}")

    ymax = max(times) * 1.2 if max(times) > 0 else 1
    plt.ylim(0, ymax)

    plt.show()

#plots the result times for one chosen algorithm over different input sizes

def barResultOneAlgorithmWithDifferentSIzes(alg, times, sizes):
    x = range(len(sizes))
    plt.figure(figsize=(12,8))
    plt.bar(x, times, tick_label = sizes)
    plt.xlabel("Eingabegrößen")
    plt.ylabel("Zeit in ms")
    plt.title(f"{alg} für verschiedene Eingabegrößen")

    ymax = max(times) * 1.2 if max(times) > 0 else 1
    plt.ylim(0, ymax)
    
    plt.show()
