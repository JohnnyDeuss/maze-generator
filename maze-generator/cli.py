from argparse import ArgumentParser, ArgumentTypeError

from .generators import best_first, breadth_first


class MazeArgumentParser(ArgumentParser):
    def __init__(self):
        """
        Create a CLI parser for maze generation.
        """
        super().__init__(description="Generate a maze")
        # Generation arguments
        self.add_argument(
            "--size",
            "-s",
            nargs=2,
            metavar="W H",
            type=int,
            default=(30, 20),
            help="The size of the maze in squares",
        )
        self.add_argument(
            "--algorithm",
            "--algo",
            "-a",
            default="best",
            help="The generation algoritms to use",
            choices=["best", "breadth"],
        )
        # Rendering arguments
        self.add_argument(
            "--border",
            type=int,
            default=4,
            help="The outer border thickness in pixels",
        )
        self.add_argument(
            "--wall", type=int, default=2, help="The inner wall thickness in pixels"
        )
        self.add_argument(
            "--path", type=int, default=20, help="The width of the pathway in pixels"
        )
        self.add_argument("--output", "-o", default="maze.png", help="The output file")

    def parse_args(self, *args, **kwargs):
        args = super().parse_args(*args, **kwargs)
        args.algorithm = self._lookup_algorithm(args.algorithm)
        return args

    @staticmethod
    def _lookup_algorithm(algorithm_name):
        """
        Convert algorithm names to their corresponding functions.
        """
        mapping = {
            "best": best_first,
            "breadth": breadth_first,
        }
        try:
            return mapping[algorithm_name]
        except KeyError:
            raise ArgumentTypeError("The given algorithm could not be found")
