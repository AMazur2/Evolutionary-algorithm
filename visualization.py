import os

import numpy as np
import plotly.graph_objects as go

if __name__ == '__main__':
    simulationSteps = 20  # TODO fix this
    outputDirectory = "output"

    array = np.zeros(simulationSteps)

    number_of_files = 0
    for filename in os.listdir(outputDirectory):
        with open(os.path.join(outputDirectory, filename), 'r') as f:
            for line in f:
                step, evaluation = line.split(":")
                array[int(step)] += float(evaluation)
        number_of_files += 1

    array /= number_of_files

    arange = np.arange(simulationSteps)
    fig = go.Figure(data=go.Scatter(x=arange, y=array))
    # find more on https://plotly.com/python/line-charts/
    fig.show()
