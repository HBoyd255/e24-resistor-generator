from enum import Enum
import math

BAND_COLOURS = [
    "Black",
    "Brown",
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Violet",
    "Grey",
    "White",
    "Gold",
    "Silver",
]


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


def generate_e24_values() -> list:
    """Generates a list of all 169 E24 values from 1 to 10M.

    Returns:
        list: A list of all 169 E24 values from 1 to 10M.
    """

    # List of base values for E24 series.
    bases = [
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

    # List of multipliers from 10^-1 to 10^6.
    multipliers = [10**i for i in range(-1, 6)]

    # Generate a list of all E24 values from 1 to 9M1.
    e24_values = [
        round(base * multiplier, 2)
        for multiplier in multipliers
        for base in bases
    ]

    # Add 10M as a valid value.
    e24_values.append(10**7)

    return e24_values


def to_engineering_notation(value: float) -> str:
    """Converts a value to engineering notation with SI prefix.

    Args:
        value (float): The value to convert.

    Returns:
        str: The value represented by engineering notation as a string.
    """

    # If the value is less than 1000, use the value as is.
    if value < 1e3:
        si_prefix = "R"
        digits = value

    # If the value is less than 1000000, use K as SI prefix.
    elif value < 1e6:
        si_prefix = "K"
        digits = value / 1e3

    # If the value is greater than or equal to 1000000, use M as SI prefix.
    else:
        si_prefix = "M"
        digits = value / 1e6

    # Format the digits as a string without trailing zeros.
    digits = "{:g}".format(float(digits))

    # If the value contains a decimal point, replace it with the SI prefix.
    if "." in digits:
        engineering_notation = digits.replace(".", si_prefix)
    # If the value is an integer, append the SI prefix.
    else:
        engineering_notation = digits + si_prefix

    return engineering_notation


def value_to_first_four_of_five_bands(value: float) -> tuple:
    """Converts a value to a tuple of band colours.

    Args:
        value (float): The value to convert.

    Returns:
        tuple: The band colours of the first 4 bands in a 5 band resistor, as a
        tuple of strings.
    """

    # Calculate the multiplier exponent for the value, which is the power of 10
    # to multiply the first 3 digits of the value by, to get the actual value.
    multiplier_exponent = math.floor(math.log10(value) - 2)

    # Tale the first 3 digits of the value.
    three_digit_value = "{:g}".format(float(value / 10**multiplier_exponent))

    # Separate the first 3 digits into individual digits.
    first_digit = int(three_digit_value[0])
    second_digit = int(three_digit_value[1])
    third_digit = int(three_digit_value[2])

    # Get the band colours for the first 3 digits.
    first_colour = BAND_COLOURS[first_digit]
    second_colour = BAND_COLOURS[second_digit]
    third_colour = BAND_COLOURS[third_digit]

    # If the multiplier is 0.01, use silver.
    if multiplier_exponent == -2:
        multiplier_colour = BAND_COLOURS[11]  # Silver
    # If the multiplier is 0.1, use gold.
    elif multiplier_exponent == -1:
        multiplier_colour = BAND_COLOURS[10]  # Gold
    # Otherwise, get the band colour for the multiplier exponent.
    else:
        multiplier_colour = BAND_COLOURS[multiplier_exponent]

    # Return the first 4 band colours as a tuple.
    return (first_colour, second_colour, third_colour, multiplier_colour)


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

    e24_values = generate_e24_values()

    for value in e24_values:
        name = to_engineering_notation(value)

        colours = value_to_first_four_of_five_bands(value)

        print(f"{name}: {colours}")


if __name__ == "__main__":
    main()
