---
toc: true
comments: true
layout: post
title: Measurement Converter
description: A tool that helps with measurement conversions.
courses: { CSP: {week: 4} }
type: hacks
---

# Define a dictionary for converting cups to ounces
cups_to_ounces = {
    1: 8,       # 1 cup = 8 ounces
    0.5: 4,     # 0.5 cups = 4 ounces
    0.25: 2,    # 0.25 cups = 2 ounces
    0.125: 1,   # 0.125 cups = 1 ounce
    # Add more conversions as needed
}


# Function to perform the cup to ounce conversion
def convert_cups_to_ounces(cups):
    if cups in cups_to_ounces:
        return cups * cups_to_ounces[cups]
    else:
        return "Conversion not available"


# Main program
if __name__ == "__main__":
    while True:
        try:
            cups_value = float(input("Enter the number of cups (or '0' to exit): "))
            if cups_value == 0:
                break
            ounces_value = convert_cups_to_ounces(cups_value)
            print(f"{cups_value} cups is equal to {ounces_value} ounces")
        except ValueError:
            print("Invalid input. Please enter a valid number of cups.")

