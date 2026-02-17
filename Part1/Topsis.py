import sys
import os
import pandas as pd
import numpy as np


def error(msg):
    print("Error:", msg)
    sys.exit(1)


def load_data(file):
    if not os.path.isfile(file):
        error("Input file not found")

    try:
        df = pd.read_csv(file)
    except Exception:
        error("Cannot read input file")

    if df.shape[1] < 3:
        error("Input file must have at least 3 columns")

    return df


def validate_numeric(df):
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            error("All criteria columns must be numeric")


def parse_weights(w_str, count):
    try:
        weights = list(map(float, w_str.split(",")))
    except Exception:
        error("Weights must be numeric and comma separated")

    if len(weights) != count:
        error("Weights count must match number of criteria")

    return np.array(weights)


def parse_impacts(i_str, count):
    impacts = i_str.split(",")

    if len(impacts) != count:
        error("Impacts count must match number of criteria")

    for val in impacts:
        if val not in ("+", "-"):
            error("Impacts must be + or -")

    return impacts


def vector_normalize(mat):
    denom = np.sqrt((mat ** 2).sum(axis=0))
    return mat / denom


def weight_matrix(norm_mat, weights):
    return norm_mat * weights


def ideal_points(weighted, impacts):
    best = []
    worst = []

    for j in range(weighted.shape[1]):
        col = weighted.iloc[:, j]
        if impacts[j] == "+":
            best.append(col.max())
            worst.append(col.min())
        else:
            best.append(col.min())
            worst.append(col.max())

    return np.array(best), np.array(worst)


def separation(weighted, best, worst):
    s_pos = np.sqrt(((weighted - best) ** 2).sum(axis=1))
    s_neg = np.sqrt(((weighted - worst) ** 2).sum(axis=1))
    return s_pos, s_neg


def topsis_score(s_pos, s_neg):
    return s_neg / (s_pos + s_neg)


def main():
    if len(sys.argv) != 5:
        error("Usage: python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>")

    input_file = sys.argv[1]
    weight_str = sys.argv[2]
    impact_str = sys.argv[3]
    output_file = sys.argv[4]

    df = load_data(input_file)
    criteria = df.iloc[:, 1:]

    validate_numeric(criteria)

    weights = parse_weights(weight_str, criteria.shape[1])
    impacts = parse_impacts(impact_str, criteria.shape[1])

    norm = vector_normalize(criteria)
    weighted = weight_matrix(norm, weights)

    best, worst = ideal_points(weighted, impacts)

    s_pos, s_neg = separation(weighted, best, worst)
    score = topsis_score(s_pos, s_neg)

    df["Topsis Score"] = score
    df["Rank"] = score.rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)

    print("TOPSIS computation finished successfully")


if __name__ == "__main__":
    main()
