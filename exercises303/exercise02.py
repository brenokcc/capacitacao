from collections import Counter


class Person:
    def __init__(self, eye_color):
        self.eye_color = eye_color


def count_eye_colors(persons, colors):
    counts = Counter({color: 0 for color in colors})
    counts.update(p.eye_color for p in persons)
    return counts
