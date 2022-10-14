"""
Shopify Product Formatter

The purpose of this program is to use python to simplify the process of
reformatting an inventory/product list into something that
could be imported into shopify.

This script requires that `pandas` and 'tkinter' be installed within
the Python environment you are running this script in.
"""

from tkinter import *
from tkinter import filedialog
import pandas as pd
from tkinter import ttk


def main():
    """
    The main function.
    :return: Nothing
    """
    print("Hello, Welcome to the Product Formatter!")

    # Program Outline
    #
    # Load the tkinter GUI
    #
    # Provide GUI items required throughout the program:
    #   * top menu bar initially contains things like "File"
    #   * error bar
    #   * back button to exit to the main menu
    #
    # Call main menu where you can decide what you would like to do:
    #   1. Format a product list into a shopify list.
    #   2. Match lists by SKU numbers.
    #   3. Break a shopify list into 1000's of variants (daily upload).
    #
    # end with tkinter mainloop()


if __name__ == "__main__":
    main()
