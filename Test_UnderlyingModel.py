import Utility.Schedule as Schedule
import UnderlyingModels

underlying_generator = UnderlyingModels.GeometricBrownianMotion(rate=0.0, sigma=0.2, dividend=None)

data1 = underlying_generator.generate_paths(schedule=Schedule.Linear(6), n=13)
data2 = underlying_generator.generate_lattice(schedule=Schedule.Linear(50))

data1.plot()
data2.plot()

