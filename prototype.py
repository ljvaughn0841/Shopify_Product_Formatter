"""
Shopify Product Formatter Prototype
This is a small prototype created to teach myself pandas and the tkinter GUI.
The purpose of this program is to demonstrate how one might use python
to reformat an inventory/product list into something that could be imported
into shopify.
"""
from tkinter import *
from tkinter import filedialog
import pandas as pd
from tkinter import ttk

global df
df = pd.DataFrame()

# For more information on headers in shopify see here
# https://help.shopify.com/en/manual/products/import-export/using-csv#product-csv-file-format
shopify_header = ["Title", "Body (HTML)", "Vendor", "Tags", "Published",
                  "Option1 Name", "Option1 Value", "Variant SKU",
                  "Variant Inventory Tracker", "Variant Inventory Policy",
                  "Variant Fulfillment Service", "Variant Price", "Status"]

root = Tk()
root.title('Product Formatter')
root.geometry("800x600")

my_menu = Menu(root)
root.config(menu=my_menu)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_tree = ttk.Treeview(my_frame)


# Opens a file
def open_file():
    """
    This function opens a .csv file then displays it on the screen
    as a spreadsheet.

    :return: None
    """
    global df
    file = filedialog.askopenfilenames(
        initialdir="E:/Ram4Global/ProductFormatter",
        title="Open File"
    )
    if file:
        try:
            df = pd.read_csv(str(file[0]))
            print("df is")
            print(df)

            # Clears the old treeview
            clear_tree()

            # Sets up new treeview
            my_tree["column"] = list(df.columns)
            my_tree["show"] = "headings"

            # Loop through column list for headers
            for column in my_tree["column"]:
                my_tree.heading(column, text=column)

            # Put data in treeview
            df_rows = df.to_numpy().tolist()
            for row in df_rows:
                my_tree.insert("", "end", values=row)

            # Pack the treeview onto the screen
            my_tree.pack()

            return

        except ValueError:
            error_label.config(text="ERROR: The File Couldn't be Opened")

        except FileNotFoundError:
            error_label.config(text="ERROR: The File Couldn't be Found")


def clear_tree():
    """
    clears the tree
    """
    my_tree.delete(*my_tree.get_children())


def test_funciton():
    """
    Test function doesn't actually do what the name implies.
    Simply prints the shopify table links.
    """
    print("apply format button")
    print(df)
    print("hello!")
    for i in range(len(DropDownLinks.req_array)):
        print(DropDownLinks.tbl_array[i].get(), " links to ",
              DropDownLinks.req_array[i].get())


class DropDownLinks:
    """
    DropDownLinks contains two arrays from the "linked" dropdowns
    These dropdowns are linked together by index
    (i.e. requirement 3 links to table variable 3)
    The elements of the array are pointers to strings created w/ StringVar()
    The elements value can be retrieved with .get()
    """

    # A list of the requirements that have been selected by the user
    req_array = []
    # A list of columns from the table the user imported that the user selected
    tbl_array = []


def add_link():
    """
    Creates two dropdown tables and adds the pointer to their input to
    the DropDownLinks arrays.
    It then packs the dropdowns onto the GUI.

    :return: None
    """
    print("Add link")

    # creates two dropdowns
    req = StringVar()
    req.set("Shopify Requirement")

    tbl = StringVar()
    tbl.set("Table Input")

    # stores the link information in a list
    DropDownLinks.req_array.append(req)
    DropDownLinks.tbl_array.append(tbl)

    # link_frame = LabelFrame(root, text="Mapping Links")

    row_num = len(DropDownLinks.req_array)

    tbl_drop = OptionMenu(link_frame, tbl, *df.columns)
    tbl_drop.grid(row=row_num, column=0, padx=10, pady=10)

    req_drop = OptionMenu(link_frame, req, *shopify_header)
    req_drop.grid(row=row_num, column=1, padx=10, pady=10)

    link_frame.pack(fill="x", expand=0, padx=20)


def remove_link():
    """
    Removes the last dropdown from the GUI and
    pops them off of the DropDownLinks lists.
    """
    print("removes a link")

    # removes the bottom two dropdowns from the link frame
    slaves = link_frame.grid_slaves()
    slaves[0].destroy()
    slaves[1].destroy()

    # Pops off the ends of the req and tbl array
    # ( removes the dropdowns values from storage )
    DropDownLinks.req_array.pop()
    DropDownLinks.tbl_array.pop()


def export_file():
    """
    Formats the file for shopify adding in the defaults then exports.
    :return:
    """
    # TODO seperate export and formating of file into different functions
    print("Exporting Shopify Formatted File")
    new_shopify_df = pd.DataFrame(columns=shopify_header)
    print(new_shopify_df)

    # Adding data to the new shopify list from the
    # dropdown linked columns in imported file
    for i in range(len(DropDownLinks.req_array)):
        new_shopify_df[DropDownLinks.req_array[i].get()] = \
            df[DropDownLinks.tbl_array[i].get()]
    print(new_shopify_df)

    # Adding in the default variables
    # TODO make an array for defaults and make this into a loop

    if "Vendor" not in DropDownLinks.req_array:
        new_shopify_df["Vendor"] = "CleanMax"
    if "Published" not in DropDownLinks.req_array:
        new_shopify_df["Published"] = "TRUE"
    if "Variant Inventory Policy" not in DropDownLinks.req_array:
        new_shopify_df["Variant Inventory Policy"] = "deny"
    if "Variant Fulfillment Service" not in DropDownLinks.req_array:
        new_shopify_df["Variant Fulfillment Service"] = "manual"
    if "Status" not in DropDownLinks.req_array:
        new_shopify_df["Status"] = "draft"

    # Exporting the new shopify df to a csv file
    new_shopify_df.to_csv('ShopifyFormatExport.csv', index=False)


# Adding a menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Export File", command=export_file)

# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand=0, padx=20)

# Adds the add link button
link_button = Button(button_frame, text="Add Link", command=lambda: add_link())
link_button.grid(row=0, column=0, padx=10, pady=10)

# Adds the remove link button
link_button = Button(button_frame, text="Remove Link",
                     command=lambda: remove_link())
link_button.grid(row=0, column=1, padx=10, pady=10)

# Adds the test sheet button
format_button = Button(button_frame, text="Test Sheet",
                       command=lambda: test_funciton())
format_button.grid(row=0, column=2, padx=10, pady=10)

# Makes a frame for the map links
link_frame = LabelFrame(root, text="Mapping Links")
link_frame.pack(fill="x", expand=0, padx=20)

# TODO make an area where users can select
#  default variables and assign them valid values

# Label for errors
error_label = Label(root, text='')
error_label.pack(pady=20, padx=20, side="bottom", anchor="se")

# the main loop for the program
root.mainloop()
