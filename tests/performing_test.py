import cProfile
import pstats
from PyQt5.QtWidgets import QApplication
from main import Main


def main():
    app = QApplication([])
    window = Main()
    window.show()
    app.exec_()


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()
