from pathlib import Path
import pandas as pd


class SimulationConfig:
    mainPath = Path("simulationResults")
    resultFileName = "result.csv"

    def __init__(self, size=50, timeStep=1e-5, duration=1.2):
        self.size = size
        self.timeStep = timeStep
        self.duration = duration

    @property
    def name(self):
        return f"L_{self.size}_dt_{self.timeStep}_d_{self.duration}"

    @property
    def path(self):
        return SimulationConfig.mainPath / Path(self.name)

    @property
    def resultPath(self):
        return self.path / SimulationConfig.resultFileName


def sizeExperiment(sizes, timeStep=1e-5, duration=1) -> list[SimulationConfig]:
    simulations = []
    for size in sizes:
        simulations.append(SimulationConfig(size, timeStep=timeStep, duration=duration))
    return simulations


def sizeExperiment1():
    sizes = [50, 500, 5000]
    return sizeExperiment(sizes, 1e-5, 1)


def runSimulations(simulations: list[SimulationConfig]):
    for s in simulations:
        # Ensure the output directory exists (including parents) and don't fail if it already exists
        s.path.mkdir(parents=True, exist_ok=True)
        # Run simulation
        result = pd.DataFrame([[1, 1.2, 2]], columns=["nr", "energy", "time"])
        result.to_csv(s.resultPath, index=False)


def plotResult(simulation: SimulationConfig):
    result = pd.read_csv(simulation.resultPath)
    print(result)


if __name__ == "__main__":
    sims = sizeExperiment1()

    #runSimulations(sims)

    plotResult(sims[0])
