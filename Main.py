from SimulationController import SimulationController
from ArgumentManager import ArgumentManager
from Wolf import Wolf

if __name__ == '__main__':
    pars = ArgumentManager()
    args = pars.parser.parse_args()

    # parameters
    number_of_sheeps = args.sheep
    with_pause = args.wait
    xy_limit = 10
    sheep_step_length = 0.5
    wolf_step_length = 1
    max_round_num = args.rounds
    json = 'pos.json'
    csv = 'alive.csv'

    simulation = SimulationController(max_round_num, number_of_sheeps, xy_limit, sheep_step_length, wolf_step_length, json, csv)
    simulation.start_simulation(with_pause)
