def convert_chart(input_lines):
    # Define a dictionary to map note numbers to characters
    note_map = {
        1: 'd',
        2: 'f',
        3: 'j',
        4: 'k'
    }

    events = []

    # Parse input lines
    for line in input_lines:
        if line.startswith('note('):
            parts = line.strip()[5:-1].split(',')
            time = int(parts[0])
            note_num = int(parts[1])
            events.append((time, note_num, 'note'))
        elif line.startswith('hold('):
            parts = line.strip()[5:-1].split(',')
            start_time = int(parts[0])
            note_num = int(parts[1])
            duration = int(parts[2])
            end_time = start_time + duration
            events.append((start_time, note_num, 'start_hold'))
            events.append((end_time, note_num, 'end_hold'))

    # Sort events by time
    events.sort()

    # Convert events to the desired format
    converted_lines = []
    current_holds = {}

    for event in events:
        time_in_seconds = (event[0] - 1175) / 100
        note_num = event[1]
        event_type = event[2]

        if event_type == 'note':
            character = note_map.get(note_num, '')
            if character:
                converted_lines.append(f"{time_in_seconds:.1f} {character}")
        elif event_type == 'start_hold':
            character = note_map.get(note_num, '')
            if character:
                current_holds[note_num] = time_in_seconds
        elif event_type == 'end_hold':
            if note_num in current_holds:
                start_time = current_holds.pop(note_num)
                converted_lines.append(f"{start_time:.1f} {note_map[note_num]} {time_in_seconds - start_time:.1f}")

    return converted_lines

def main():
    input_file = 'input_chart.txt'

    # Read the input file
    with open(input_file, 'r') as file:
        input_lines = file.readlines()

    # Convert the chart
    converted_chart = convert_chart(input_lines)

    # Print the converted chart
    for line in converted_chart:
        print(line)

if __name__ == "__main__":
    main()
