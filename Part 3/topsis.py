import pandas as pd
import numpy as np
import os


def run_topsis(input_file, weights, impacts, output_file):
    if not os.path.exists(input_file):
        raise Exception("Input file not found")

    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        raise Exception("Input file must contain at least 3 columns")

    data = df.iloc[:, 1:]

    if not all(np.issubdtype(dtype, np.number) for dtype in data.dtypes):
        raise Exception("Criteria columns must be numeric")

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        raise Exception("Weights/Impacts count mismatch")

    norm = data / np.sqrt((data ** 2).sum())
    weighted = norm * weights

    best = []
    worst = []

    for i in range(len(impacts)):
        col = weighted.iloc[:, i]
        if impacts[i] == "+":
            best.append(col.max())
            worst.append(col.min())
        else:
            best.append(col.min())
            worst.append(col.max())

    best = np.array(best)
    worst = np.array(worst)

    d_best = np.sqrt(((weighted - best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - worst) ** 2).sum(axis=1))

    score = d_worst / (d_best + d_worst)

    df["Topsis Score"] = score
    df["Rank"] = score.rank(ascending=False)

    df.to_csv(output_file, index=False)
