#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: February 2022
# This program uses user input
#   To calculate area and perimeter


def main():
    # This function calculates the area and perimeter

    # input
    length = int(input("Enter length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print("Area is {0} mm².".format(area))
    print("Perimeter is {0} mm.".format(perimeter))

    print("Done")


if __name__ == "__main__":
    main()
