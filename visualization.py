import os

import numpy as np
import plotly.graph_objects as go


def plotParameterComparesonBigSmall(DirectoryName):
    outputDirectory1 = f"output/speedOfConvergenceBigPopulationLessSteps{DirectoryName}"
    array1 = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory1)
    outputDirectory2 = f"output/speedOfConvergenceSmallPopulationMoreSteps{DirectoryName}"
    array2 = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory2)

    arange1 = np.arange(array1.shape[0])
    # assert arange1 == np.array([i for i in range(array1.shape[0])])

    arange2 = np.arange(array2.shape[0])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=arange1, y=array1, name=f"BigPopulationLessSteps{DirectoryName}"))
    fig.add_trace(go.Scatter(x=arange2, y=array2, name=f"SmallPopulationMoreSteps{DirectoryName}"))
    fig.show()


def plotParameterComparesonMutation():
    outputDirectory1 = "output/speedOfConvergenceMutatorProbability0.1"
    array1 = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory1)
    outputDirectory2 = "output/speedOfConvergenceMutatorProbability0.5"
    array2 = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory2)
    outputDirectory3 = "output/speedOfConvergenceMutatorProbability1.0"
    array3 = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory3)

    arange1 = np.arange(array1.shape[0])
    arange2 = np.arange(array2.shape[0])
    arange3 = np.arange(array3.shape[0])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=arange1, y=array1, name="Population 10"))
    fig.add_trace(go.Scatter(x=arange2, y=array2, name="Population 50"))
    fig.add_trace(go.Scatter(x=arange3, y=array3, name="Population 100"))
    fig.show()


# def plotParameterCompareson(DirectoriesNameFragment):
#     fig = go.Figure()
#     rootdir = "output"
#     for subdir in os.walk(rootdir):
#         print(subdir)

def plotParameterCompareson():
    outputDirectory1 = "output/speedOfConvergencePopulationSize10"
    array1 = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory1)
    outputDirectory2 = "output/speedOfConvergencePopulationSize50"
    array2 = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory2)
    outputDirectory3 = "output/speedOfConvergencePopulationSize100"
    array3 = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory3)

    arange1 = np.arange(array1.shape[0])
    arange2 = np.arange(array2.shape[0])
    arange3 = np.arange(array3.shape[0])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=arange1, y=array1, name="Population 10"))
    fig.add_trace(go.Scatter(x=arange2, y=array2, name="Population 50"))
    fig.add_trace(go.Scatter(x=arange3, y=array3, name="Population 100"))
    fig.show()


def plotSpeedOfCovergence(DirectoryName):
    outputDirectory = f"output/{DirectoryName}"

    array = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory)

    one_run = getBestIndividualEvaluationAvrageOverNRuns(outputDirectory, isOneRun=True)

    arange = np.arange(array.shape[0])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=arange, y=array, name="Average"))
    # fig.add_trace(go.Scatter(x=arange, y=one_run, name="One run"))
    # find more on https://plotly.com/python/line-charts/
    fig.show()


def findSimulationSteps(dataDirectory):
    result = 0
    for filename in os.listdir(dataDirectory):
        if filename != "config.json":
            with open(os.path.join(dataDirectory, filename), 'r') as f:
                for line in f:
                    result += 1
            return result


def getBestIndividualEvaluationAvrageOverNRuns(dataDirectory, isAvrage: bool = True, isOneRun: bool = False):
    simulationSteps = findSimulationSteps(dataDirectory)
    sumEvaluationsInNRuns = np.zeros(simulationSteps)  # numpy array
    nSimulationRuns = 0

    for filename in os.listdir(dataDirectory):
        if "config" not in str(filename):
            with open(os.path.join(dataDirectory, filename), 'r') as f:
                for line in f:
                    step, evaluation = line.split(":")
                    sumEvaluationsInNRuns[int(step)] += float(evaluation)
            nSimulationRuns += 1
        if isOneRun:
            break
    if isAvrage:
        sumEvaluationsInNRuns /= nSimulationRuns
    return sumEvaluationsInNRuns


if __name__ == '__main__':
    # plotSpeedOfCovergence("test")
    # plotParameterCompareson("MutatorProbaility")
    # plotParameterComparesonMutation()
    # plotParameterComparesonBigSmall()

    # plotParameterComparesonBigSmall("ExpandedSchaffers")
    plotSpeedOfCovergence("test")
