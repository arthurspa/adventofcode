import os


folder = "2024"
os.makedirs(folder, exist_ok=True)

folder_input = os.path.join(folder, "input")
os.makedirs(folder_input, exist_ok=True)

template = """from io import TextIOWrapper


def solve(input: TextIOWrapper):
    pass

"""

for i in range(25):
    solution_file_1 = os.path.join(folder, f"day{i+1:02}_1.py")
    solution_file_2 = os.path.join(folder, f"day{i+1:02}_2.py")
    input_file = os.path.join(folder_input, f"day{i+1:02}")

    if not os.path.exists(solution_file_1):
        with open(solution_file_1, "w") as f:
            f.write(template)

    if not os.path.exists(solution_file_2):
        with open(solution_file_2, "w") as f:
            f.write(template)

    if not os.path.exists(input_file):
        with open(input_file, "w") as f:
            f.write("")
