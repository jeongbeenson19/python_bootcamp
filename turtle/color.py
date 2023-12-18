import colorgram


class ColorGram:
    def __init__(self):
        self.rgb_colors = []

    def rgb_color(self, image_file, number_of_color):
        colors = colorgram.extract(image_file, number_of_color)
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            new_color = (r, g, b)
            self.rgb_colors.append(new_color)
        return self.rgb_colors
