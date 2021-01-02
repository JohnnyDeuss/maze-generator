from .cli import MazeArgumentParser
from .render import render_maze

if __name__ == "__main__":
    parser = MazeArgumentParser()
    args = parser.parse_args()
    g = args.algorithm(*args.size)
    img = render_maze(
        g,
        path_width=args.path,
        wall_width=args.wall,
        border_width=args.border,
    )
    img.save(args.output, "PNG")
