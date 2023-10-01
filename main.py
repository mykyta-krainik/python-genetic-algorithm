from modules.classes.GeneticAlgorithm import GeneticAlgorithm
from modules.classes.InputUI import InputUI
from modules.classes.MapUI import MapUI
from modules.types.InputData import InputData


def main():
    def handle_click(input_data: InputData):
        GeneticAlgorithm(MapUI(), **input_data).run()

    input_ui = InputUI()

    input_ui.start(handle_click)


if __name__ == "__main__":
    main()
