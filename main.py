import re
import random


def convert_chart(input_file, output_file):
    output_chart = []

    with open(input_file, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("note"):
                match = re.match(r"note\((\d+),(\d+)\)", line)
                if match:
                    time = int(match.group(1)) / 1000.0  # Convert to seconds
                    lane = random.randint(
                        0, 900)  # Random lane number between 0 and 900
                    duration = 0  # Note has duration 0
                    output_chart.append(f"{time} {lane} {duration}")
            elif line.startswith("hold"):
                match = re.match(r"hold\((\d+),(\d+)\)", line)
                if match:
                    time = int(match.group(1)) / 1000.0  # Convert to seconds
                    lane = random.randint(
                        0, 900)  # Random lane number between 0 and 900
                    duration = int(
                        match.group(3)) / 1000.0  # Convert to seconds
                    output_chart.append(f"{time} {lane} {duration}")

    with open(output_file, 'w') as outfile:
        for line in output_chart:
            outfile.write(line + '\n')


# Example usage
input_file = 'input_chart.txt'
output_file = 'chart.txt'
convert_chart(input_file, output_file)
