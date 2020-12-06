import os

import numpy as np
import plotly.graph_objects as go

if __name__ == '__main__':
    simulationSteps = 20  # TODO fix this
    outputDirectory = "output/minFitnessFunctionInGeneration"

    array = np.zeros(simulationSteps)
    one_run = np.zeros(simulationSteps)

    number_of_files = 0
    for filename in os.listdir(outputDirectory):
        if filename != "config.json":
            with open(os.path.join(outputDirectory, filename), 'r') as f:
                for line in f:
                    step, evaluation = line.split(":")
                    array[int(step)] += float(evaluation)
            number_of_files += 1

    for filename in os.listdir(outputDirectory):
        if filename != "config.json":
            with open(os.path.join(outputDirectory, filename), 'r') as f:
                for line in f:
                    step, evaluation = line.split(":")
                    one_run[int(step)] += float(evaluation)
            break

    array /= number_of_files

    arange = np.arange(simulationSteps)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=arange, y=array, name="Average"))
    fig.add_trace(go.Scatter(x=arange, y=one_run, name="One run"))

    # find more on https://plotly.com/python/line-charts/
    fig.show()
