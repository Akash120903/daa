def generate_timetable(subjects):
    clashes = {}
    for subject in subjects:
        subject_code = subject[1]
        clashes[subject_code] = set(subject[2])  # Fix: Use subject[2] for the list of neighbors

    timetable = {}
    colors = {}

    for subject in subjects:
        subject_code = subject[1]
        available_colors = set(colors.get(neighbour, 0) for neighbour in clashes[subject_code])  # Fix: Use colors.get(neighbour, 0) to default to 0

        color = 1
        while color in available_colors:
            color += 1
        colors[subject_code] = color

        if color not in timetable:
            timetable[color] = []
        timetable[color].append(subject_code)

    return timetable

subjects = [
    ("A", "C1", ["C2", "C3"]),
    ("B", "C2", ["C1"]),
    ("C", "C3", ["C1", "C4"]),
    ("D", "C4", ["C3"]),
    ("E", "C5", []),
]

timetable = generate_timetable(subjects)

for color, subjects in timetable.items():
    print(f"Timetable {color}:")
    for subject in subjects:
        print(subject)
    print()
