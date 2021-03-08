import matplotlib.pyplot as plt
import pandas as pd


def plot_results():
    results = pd.read_csv("results/results.csv", sep=",", index_col=0)
    print(results)
    for c in results.columns:
        results[c] /= results[c].sum()
    results.pop("TOTAL")
    results = results.drop("TOTAL")

    ax = results.plot.bar()
    plt.show()
    return ax
