import re


def clean_line(line):
    line = line.strip()  # remove leading/trailing spaces

    # remove unwanted symbols
    line = re.sub(r"[#*\-]{2,}", "", line)

    # replace multiple spaces with one space
    line = re.sub(r"\s+", " ", line)

    # remove space before punctuation
    line = re.sub(r"\s+([.,!?])", r"\1", line)

    return line


def clean_text(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = []

    for line in lines:
        cleaned = clean_line(line)
        if cleaned:  # ignore empty lines
            cleaned_lines.append(cleaned)

    with open(output_file, "w", encoding="utf-8") as f:
        for line in cleaned_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    clean_text("input.txt", "output.txt")
    print("Text cleaned successfully.")

