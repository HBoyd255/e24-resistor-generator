def read_file_to_string(file_path: str) -> str:
    """Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The content of the file as a string.
    """

    with open(file_path, "r") as file:
        content = file.read()
    return content


def save_string_to_file(content: str, output_file_path: str) -> None:
    """Saves a string to a file.

    Args:
        content (str): The content to save.
        output_file_path (str): The path to the file to save the content to.
    """

    with open(output_file_path, "w") as file:
        file.write(content)


def set_band_value(
    step_string: str,
    band_number: int,
    red_value: float,
    green_value: float,
    blue_value: float,
) -> str:
    """Sets the band values in a STEP file string, replacing placeholders with
    the actual values, and returns the updated string.

    Values should be floats between 0 and 1.

    Args:
        step_string (str): The STEP file content as a string.
        band_number (int): The band number to set the values for.
        red_value (float): The red value to set(from 0 to 1).
        green_value (float): The green value to set(from 0 to 1).
        blue_value (float): The blue value to set(from 0 to 1).

    Returns:
        str: The updated STEP file content as a string.
    """

    # Create placeholders for the band values.
    red_placeholder = "{{BAND_" + str(band_number) + "_RED}}"
    green_placeholder = "{{BAND_" + str(band_number) + "_GREEN}}"
    blue_placeholder = "{{BAND_" + str(band_number) + "_BLUE}}"

    # Replace the placeholders with the actual values.
    step_string = step_string.replace(red_placeholder, str(red_value))
    step_string = step_string.replace(green_placeholder, str(green_value))
    step_string = step_string.replace(blue_placeholder, str(blue_value))

    # Return the updated string.
    return step_string


BASE_VALUES = [
    10,
    11,
    12,
    13,
    15,
    16,
    18,
    20,
    22,
    24,
    27,
    30,
    33,
    36,
    39,
    43,
    47,
    51,
    56,
    62,
    68,
    75,
    82,
    91,
]
MULTIPLIERS = [10**i for i in range(-1, 6)]  # 10^-1 to 10^6

# Generate a list of all E24 values from 1 to 9M1.
e24_values = [
    round(base * multiplier, 2)
    for multiplier in MULTIPLIERS
    for base in BASE_VALUES
]

# Add 10M as a valid value.
e24_values.append(10**7)


def main():

    #     template_file_path = "Template/Template.step"
    #     output_file_path = "Output/test.step"
    #
    #     file_content = read_file_to_string(template_file_path)
    #
    #     file_content = set_band_value(file_content, 1, 1, 1, 1)
    #     file_content = set_band_value(file_content, 2, 0.8, 0.8, 0.8)
    #     file_content = set_band_value(file_content, 3, 0.6, 0.6, 0.6)
    #     file_content = set_band_value(file_content, 4, 0.4, 0.4, 0.4)
    #     file_content = set_band_value(file_content, 5, 0.2, 0.2, 0.2)
    #
    #     save_string_to_file(file_content, output_file_path)

    for value in e24_values:
        print(value)


if __name__ == "__main__":
    main()
