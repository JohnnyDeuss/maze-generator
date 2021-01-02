from PIL import Image, ImageDraw


def render_maze(g, path_width=20, wall_width=2, border_width=4, output_file="maze.png"):
    """
    Render a maze graph and output it to the given file.
    """
    w, h = list(g.nodes)[-1]
    w += 1
    h += 1
    img_w = w * path_width + (w - 1) * wall_width + 2 * border_width
    img_h = h * path_width + (h - 1) * wall_width + 2 * border_width
    img = Image.new("1", (img_w, img_h))
    draw = ImageDraw.Draw(img)
    # Draw entrance
    draw.rectangle(
        [0, border_width, border_width, border_width + path_width - 1], fill=1
    )
    # Draw exit
    draw.rectangle(
        [
            img_w - border_width,
            img_h - path_width - border_width,
            img_w,
            img_h - border_width - 1,
        ],
        fill=1,
    )

    def draw_line(a, b):
        # Ensure `a` is the upper left point.
        if b[0] < a[0] or b[1] < a[1]:
            a, b = b, a
        x_a, y_a = a
        x_b, y_b = b

        x_a = border_width + x_a * (path_width + wall_width)
        y_a = border_width + y_a * (path_width + wall_width)
        x_b = border_width + x_b * (path_width + wall_width) + path_width - 1
        y_b = border_width + y_b * (path_width + wall_width) + path_width - 1
        draw.rectangle([x_a, y_a, x_b, y_b], fill=1, outline=1)

    for e in g.edges:
        draw_line(*e)

    return img
