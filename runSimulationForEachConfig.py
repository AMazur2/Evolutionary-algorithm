import os

if __name__ == '__main__':
    simulationConfigDirectory = "simulationConfigs"
    for filename in os.listdir(simulationConfigDirectory):
        configFile = os.path.join(simulationConfigDirectory, filename)
        print(f"Run simulation for {configFile}")
        os.system(f'./runSimulation.py {configFile}')
