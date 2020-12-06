def read_data_blank_line_separator(file):
    buffer = ""
    output_lines = []
    with open(file) as f:
        lines = f.read().splitlines()
        for line in lines:
            if line != "":
                buffer += line + " "
            else:
                output_lines.append(buffer.strip())
                buffer = ""
    output_lines.append(buffer.strip())
    buffer = ""
    return output_lines

def get_input(file):
    with open(file) as f:
        data = f.read().splitlines()
    return data