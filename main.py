from tkinter import *
from tkinter import filedialog
import pandas as pd
from tkinter import ttk

global df
df = pd.DataFrame()

# For more information on headers in shopify see here
# https://help.shopify.com/en/manual/products/import-export/using-csv#product-csv-file-format
shopify_header = ["Title", "Body (HTML)", "Vendor", "Tags", "Published", "Option1 Name", "Option1 Value", "Variant SKU",
                  "Variant Inventory Tracker", "Variant Inventory Policy", "Variant Fulfillment Service",
                  "Variant Price", "Variant Requires Shipping", "Variant Taxable", "Status"]

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

            return df

        except ValueError:
            error_label.config(text="ERROR: The File Couldn't be Opened")

        except FileNotFoundError:
            error_label.config(text="ERROR: The File Couldn't be Found")


def clear_tree():
    my_tree.delete(*my_tree.get_children())


def apply_shopify_format():
    print("apply format button")
    print(df)
    print("hello!")
    for i in range(len(DropDownLinks.req_array)):
        print(DropDownLinks.req_array[i].get())


class DropDownLinks:
    req_array = []
    tbl_array = []


def add_link():
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

    tbl_drop = OptionMenu(link_frame, tbl, *shopify_header)
    tbl_drop.grid(row=row_num, column=0, padx=10, pady=10)

    req_drop = OptionMenu(link_frame, req, *shopify_header)
    req_drop.grid(row=row_num, column=1, padx=10, pady=10)

    link_frame.pack(fill="x", expand=0, padx=20)


def remove_link():
    print("removes a link")


# Adding a menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)

# Add Buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand=0, padx=20)

# Adds the add link button
link_button = Button(button_frame, text="Add Link", command=lambda: add_link())
link_button.grid(row=0, column=0, padx=10, pady=10)

# Adds the format sheet button
format_button = Button(button_frame, text="Format Sheet", command=lambda: apply_shopify_format())
format_button.grid(row=0, column=1, padx=10, pady=10)

link_frame = LabelFrame(root, text="Mapping Links")
link_frame.pack(fill="x", expand=0, padx=20)

# Label for errors
error_label = Label(root, text='')
error_label.pack(pady=20, padx=20, side="bottom", anchor="se")

# the main loop for the program
root.mainloop()
