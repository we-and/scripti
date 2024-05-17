import os
import tkinter as tk
from tkinter import ttk, filedialog, Text,Menu
from script_parser import process_script, is_supported_extension
import pandas as pd
import chardet
import tkinter.font as tkFont
import subprocess
import platform
import re
import csv
countingMethods=[
    "LINE_COUNT",
    "WORD_COUNT",
    "ALL",
    "ALL_NOSPACE",
    "ALL_NOPUNC",
    "ALL_NOSPACE_NOPUNC",
    "ALL_NOAPOS",    
]

countingMethodNames={
    "LINE_COUNT":"Line count",
    "WORD_COUNT":"Word count",
    "ALL":"All characters",
    "ALL_NOSPACE":"No space",
    "ALL_NOPUNC":"No punctuation",
    "ALL_NOSPACE_NOPUNC":"No space, no punctuation",
    "ALL_NOAPOS":"No apostrophe",
}

countingMethod="ALL"
currentOutputFolder=""
currentFilePath=""
currentScriptFilename=""
outputFolder="tmp"
currentXlsxPath=""


if not os.path.exists(outputFolder):
    os.mkdir(outputFolder)


def compute_length_by_method(line,method):
    res=0
    if method=="ALL":
        res=len(line)
    elif method=="LINE_COUNT":
        res=1
    elif method=="ALL_NOSPACE":
        res= len(line.replace(" ",""))
    elif method=="ALL_NOPUNC":
        res= len(line.replace(",","").replace("?","").replace(".","").replace("!",""))
    elif method=="ALL_NOSPACE_NOPUNC":
        res= len(line.replace(" ","").replace(",","").replace("?","").replace(".","").replace("!",""))
    elif method=="ALL_NOAPOS":
        res= len(line.replace("'",""))
    elif method=="WORD_COUNT":
        res= len(line.split(" "))
    else:
        res= -1
    #print("compute_length_by_method METHOD "+method+" "+str(res))
    return res


def get_text_without_parentheses(input_string):
    pattern = r'\([^()]*\)'
    # Use re.sub() to replace the occurrences with an empty string
    result_string = re.sub(pattern, '', input_string)
    return result_string

def convert_csv_to_xlsx(csv_file_path, xlsx_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Write the DataFrame to an Excel file
    df.to_excel(xlsx_file_path, index=False, engine='openpyxl')

def load_tree(parent, root_path):
    # Clear the tree view if root_path is the starting directory
    if parent == "":
        folders.delete(*folders.get_children())
        parent = folders.insert('', 'end', text=os.path.basename(root_path), open=True, values=[root_path])

    # List all entries in the directory
    try:
        dir_entries = os.listdir(root_path)
    except PermissionError:
        return  # Skip directories without permission

    # Separate and sort directories and files
    dirs = sorted([entry for entry in dir_entries if os.path.isdir(os.path.join(root_path, entry))])
    files = sorted([entry for entry in dir_entries if not os.path.isdir(os.path.join(root_path, entry))])

    # Insert directories first
    for entry in dirs:
        entry_path = os.path.join(root_path, entry)

        dir_id = folders.insert(parent, 'end', text=entry, open=False, values=[entry_path],tags=('folder'))
        load_tree(dir_id, entry_path)  # Recursively load subdirectories

    # Insert files
    for entry in files:
        entry_path = os.path.join(root_path, entry)
        supported_tag="not_supported"

        name, extension = os.path.splitext(entry)
    
        if is_supported_extension(extension):
            supported_tag="supported" 
        folders.insert(parent, 'end', text=entry, values=[entry_path],tags=(supported_tag))

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as file:  # Open the file in binary mode
        raw_data = file.read(10000)  # Read the first 10000 bytes to guess the encoding
        result = chardet.detect(raw_data)
        return result
def get_encoding(enc):
    #print("Guess encoding from"+str(enc))
    if enc=="ascii":
        return "ISO-8859-1"
    elif enc=="ISO-8859-1":
        return "ISO-8859-1"
    elif enc=="Windows-1252":
        return "Windows-1252"       
    return "utf-8"

def reset_tables(): 
    print("reset_tables")
    for item in breakdown_table.get_children():
        breakdown_table.delete(item)
    for item in character_table.get_children():
        character_table.delete(item)

def runJob(file_path,method):
    global currentFilePath
    global currentScriptFilename
    global currentOutputFolder
    currentFilePath=file_path
    reset_tables()
    # Check if the selected item is a file and display its content
    if os.path.isfile(file_path):
        try:
            file_name = os.path.basename(file_path)
            currentScriptFilename=file_name
            name, extension = os.path.splitext(file_name)
            if is_supported_extension(extension):
                print(" > Supported")

                encoding_info = detect_file_encoding(file_path)
                encoding=encoding_info['encoding']
                print("Encoding detected  : "+str(encoding))
                print("Encoding confidence : "+str(encoding_info['confidence']))

                enc=get_encoding(encoding)
                print("Encoding used       : "+str(enc))
    #            encodings = ['windows-1252', 'iso-8859-1', 'utf-16','utf-8']
     #           for encod in encodings:
     #               print("try encoding"+encod)
                with open(file_path, 'r', encoding=enc) as file:
                    content = file.read()

                    file_preview.delete(1.0, tk.END)
                    file_preview.insert(tk.END, content)
                    
                    currentOutputFolder=outputFolder+"/"+name+"/"
                    breakdown,character_scene_map,scene_characters_map,character_linecount_map,character_order_map,character_textlength_map=process_script(file_path,currentOutputFolder,name,method)
                    fill_breakdown_table(breakdown)
                    fill_character_stats_table(character_order_map,breakdown)
                    fill_stats_table(breakdown)
                    fill_character_table(character_order_map, breakdown,character_linecount_map,scene_characters_map)
                    update_statistics(content)
            else:
                print(" > Not supported")
                stats_label.config(text=f"Format {extension} not supported")

        except Exception as e:
            file_preview.delete(1.0, tk.END)
            file_preview.insert(tk.END, f"Error opening file: {e}")

def on_folder_select(event):
    global currentOutputFolder
    print("FOLDER SELECT")
    selected_item = folders.selection()[0]
    file_path = folders.item(selected_item, 'values')[0]
    runJob(file_path,countingMethod)

def update_statistics(content):
    words = len(content.split())
    chars = len(content)
    stats_label.config(text=f"Words: {words} Characters: {chars}")
  #  stats_text.insert(0,f"Words: {words} Characters: {chars}")

def open_folder():
    directory = filedialog.askdirectory(initialdir=os.getcwd())
    if directory:
        load_tree(directory)


def exit_app():
    app.quit()


def center_window():
    app.update_idletasks()
    width = app.winfo_width()
    height = app.winfo_height()
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
     # Calculate width and height as 80% of screen dimensions
    width = int(screen_width * 0.8)
    height = int(screen_height * 0.8)
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    app.geometry(f'{width}x{height}+{x}+{y}')


def stats_per_character(breakdown,character_name):
    line_count=0
    word_count=0
    character_count=0
    
    for item in breakdown:
        if item['type']=="SPEECH":
            if item['character']==character_name:
                t=item['speech']
                line_count=line_count+1
                le=compute_length_by_method(t,"ALL")
                character_count=character_count+le
                word_count=word_count+len(t.split(" "))
    #print(character_name,character_count)
            
    replica_count=round(character_count/40)
    return line_count,word_count,character_count,replica_count

def fill_character_table(character_order_map, breakdown,character_linecount_map,scene_characters_map):
    for item in character_order_map:
        lines=character_linecount_map[item]
        line_count,word_count,character_count,replica_count=stats_per_character(breakdown,item)
        scenes=scene_characters_map[item]
        scenes=', '.join(scenes)
        character_table.insert('','end',values=(str(character_order_map[item]),item,str(line_count),str(character_count),str(word_count),str(replica_count),scenes))
        

def compute_length(method,line):
    if method=="ALL":
        return len(line);
    return len(line);


def fill_character_stats_table(character_order_map, breakdown):
    print("fill_character_stats_table")

    total_by_character_by_method={}
    for character_name in character_order_map:
        character_order=character_order_map[character_name]
        #print("CHAR"+str(character_name))
        rowtotal=("-",character_name,"TOTAL")
        total_by_method={}
        for m in countingMethods:
            total_by_method[m]=0
        
        for item in breakdown:
            line_idx=item['line_idx']
            type_=item['type']
            if(type_=="SPEECH"):

                speech=item['speech']
                character=item['character']
                character_raw=item['character_raw']
                
                filtered_speech=get_text_without_parentheses(speech)

                if character==character_name:
                    #print("    MATCH"+str(speech))

                    row=(str(line_idx),character,character_raw, speech)
                    for m in countingMethods: 
                        #print("add"+str(m))
                        le=compute_length_by_method(filtered_speech,m)
                        row=row+(str(le),)
                        total_by_method[m]=total_by_method[m]+le
                    #print("add"+str(row))
                    character_stats_table.insert('','end',values=row)
        
        for m in countingMethods:
            rowtotal=rowtotal+(total_by_method[m],)
        character_stats_table.insert('','end',values=rowtotal,tags=['total'])
        
        total_by_character_by_method[str(character_order)+" - "+character_name]=total_by_method
    totalcsvpath=currentOutputFolder+"/"+currentScriptFilename+"-total-recap.csv"
    generate_total_csv(total_by_character_by_method,totalcsvpath)


def save_string_to_file(text, filename):
        """Saves a given string `text` to a file named `filename`."""
        print(" > Write to "+filename)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
def get_excel_column_name(column_index):
    """Convert a 1-based column index to an Excel column name (e.g., 1 -> A, 27 -> AA)."""
    column_name = ""
    while column_index > 0:
        column_index, remainder = divmod(column_index - 1, 26)
        column_name = chr(65 + remainder) + column_name
    return column_name
def convert_csv_to_xlsx2(csv_file_path, xlsx_file_path, n):
    print("generate_total_xlsx "+xlsx_file_path)

    # Read the CSV file
    df = pd.read_csv(csv_file_path,header=None)

    # Convert columns explicitly to numeric where appropriate
    for col in df.columns[1:]:  # Skip the first column if it's non-numeric (e.g., names)
        df[col] = pd.to_numeric(df[col], errors='ignore')

    # Write the DataFrame to an Excel file
    print(" > Write to "+xlsx_file_path)

    header1=["SCRIPT_NAME"]
    header2=["Role"]
    for i in countingMethods:
        header1.append("?")
        header2.append(countingMethodNames[i])
        
    header_rows = pd.DataFrame([
        header1,
        header2
    ])
    
    # Concatenate the header rows and the original data
    # The ignore_index=True option reindexes the new DataFrame
    df = pd.concat([header_rows, df], ignore_index=True)

    # Write the DataFrame to an Excel file
    with pd.ExcelWriter(xlsx_file_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        # Load the workbook and sheet for modification
        workbook = writer.book
        sheet = workbook['Sheet1']

        # Merge cells in the first and second new rows
        # Assuming you want to merge from the first to the last column
        col=get_excel_column_name(n)
        sheet.merge_cells("A1:"+col+"1")  # Modify range according to your number of columns
        sheet.merge_cells("A2:"+col+"2")  # Modify range according to your number of columns
 #       sheet.merge_cells('A2:D2')  # Modify this as needed
        sheet['A1'] = currentScriptFilename
        sheet['A2'] = "Length: "
 # Load the workbook and get the active sheet
      



def generate_total_csv(total,csv_path):
    global currentXlsxPath
    print("Total csv path          : "+csv_path)
    #header
    s=""
    showHeader=False
    if showHeader:
        s="Role,"
        for m in countingMethods:
            s=s+str(m)+","
        s=s[0:len(s)-1]
        s=s+"\n"

    data = [
    ]
    for character in total:
        datarow=[str(character)];
        for method in total[character]:
            print(str(character)+": Add method "+method+" = "+str(total[character][method]))
            datarow.append(str(total[character][method]))
        data.append(datarow)
    print("data"+str(data))
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Write data to the CSV file
        for row in data:
            print("Write "+str(row))
            writer.writerow(row)

    if False:   
        for character in total:
            s+=str(character)+","
            for method in total[character]:
                s=s+str(total[character][method])+","
            s=s[0:len(s)-1]
            s=s+"\n"
        save_string_to_file(s,csv_path)


    xlsx_path=csv_path.replace(".csv",".xlsx")
    currentXlsxPath=xlsx_path
    n=len(countingMethods)+1
    print("Total xlsx path          : "+xlsx_path)
    convert_csv_to_xlsx2(csv_path,xlsx_path,n)

def on_button_click():
    print("Button clicked!")
def export_csv():
    print("Export")

def fill_breakdown_table(breakdown):
    for item in breakdown:
        type_=item['type']
        line_idx=item['line_idx']
        if(type_=="SCENE_SEP"):
            scene_id=item['scene_id']
            breakdown_table.insert('','end',values=("","","",""), tags=('border'))
            breakdown_table.insert('','end',values=(str(line_idx),"New scene",scene_id,""), tags=('scene','bold'))
        elif(type_=="SPEECH"):
            speech=item['speech']
            character=item['character']
            breakdown_table.insert('','end',values=(str(line_idx),"Speech",character,speech))
        elif(type_=="NONSPEECH"):         
            text=item['text']
            breakdown_table.insert('','end',values=(str(line_idx),"Other",text,""), tags=('nonspeech',))
    print("NB ROWS = "+str(len(breakdown_table.get_children())))
    breakdown_table.update_idletasks()

def fill_stats_table(breakdown):
    for item in breakdown:
        type_=item['type']
        line_idx=item['line_idx']
        if(type_=="SPEECH"):
            speech=item['speech']
            filtered_speech=get_text_without_parentheses(speech)
            character=item['character']
            tout=len(filtered_speech)
            nospace=len(filtered_speech.replace(" ",""))
            stats_table.insert('','end',values=(str(line_idx),character,speech,str(tout),str(nospace)))
    print("NB ROWS = "+str(len(breakdown_table.get_children())))
    breakdown_table.update_idletasks()


def clear_table(treeview):
    """
    Clears all rows from the given Treeview table.
    
    Args:
        treeview (ttk.Treeview): The Treeview widget instance.
    """
    for item in treeview.get_children():
        treeview.delete(item)

app = tk.Tk()
app.title('Script Analyzer')


# Menu bar
menu_bar = Menu(app)
app.config(menu=menu_bar)


# File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open Folder...", command=open_folder)
file_menu.add_command(label="Export csv...", command=export_csv)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

def get_os():
    if os.name == 'nt':
        return 'Windows'
    elif os.name == 'posix':
        if 'darwin' in platform.system().lower():
            return 'macOS'
        elif 'linux' in platform.system().lower():
            return 'Linux'
    else:
        return 'Unknown'
    
def open_xlsx_recap():
    os_=get_os()
    if os_=="Windows":
        try:
            os.startfile(currentXlsxPath)
        except Exception as e:
            print(f"Failed to open file: {e}")
    else:
        try:
            subprocess.run(['open', currentXlsxPath], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to open file: {e}")

def set_counting_method(i):
    print("set method "+i)
    global countingMethod
    countingMethod=i

def show_popup_counting_method():
    popup = tk.Toplevel()
    popup.title("Popup") 

    for i in countingMethods:
        button = ttk.Button(popup, text=i, command=set_counting_method(i))
        button.pack(side=tk.TOP, fill=tk.X)


    dropdown = ttk.Combobox(popup, values=countingMethods)
    dropdown.pack(pady=20)
    dropdown.current(0)
    dropdown.bind('<<ComboboxSelected>>', on_value_change)


settings_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Change counting method...", command=show_popup_counting_method)
settings_menu.add_command(label="Set block length...", command=open_folder)



# Layout configuration
left_frame = ttk.Frame(app)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = ttk.Frame(app)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Folder tree
folders = ttk.Treeview(left_frame, columns=())
folders.tag_configure('not_supported', foreground='#cccccc')
folders.tag_configure('supported', foreground='#444444')
folders.tag_configure('folder', foreground='#6666cc')

folders.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
folders.bind('<<TreeviewSelect>>', on_folder_select)

# Notebook (tabbed interface)
notebook = ttk.Notebook(right_frame)
notebook.pack(fill=tk.BOTH, expand=True)

def on_tab_selected(event):
    print("Tab selected:", event.widget.select())

notebook.bind("<<NotebookTabChanged>>", on_tab_selected)
# File preview tab
preview_tab = ttk.Frame(notebook)
notebook.add(preview_tab, text='Original text')
file_preview = Text(preview_tab)
file_preview.pack(fill=tk.BOTH, expand=True)

# Statistics tab
character_tab = ttk.Frame(notebook)

# Create a Treeview widget within the stats_frame for the table
character_table = ttk.Treeview(character_tab, columns=('Order', 'Character', 'Lines','Character Count','Word Count','Blocks','Scenes'), show='headings')
# Define the column headings
character_table.heading('Order', text='Order')
character_table.heading('Character', text='Character')
character_table.heading('Lines', text='Lines')
character_table.heading('Character Count', text='Character Count')
character_table.heading('Word Count', text='Word Count')
character_table.heading('Blocks', text='Blocks')
character_table.heading('Scenes', text='Scenes')

# Define the column width and alignment
character_table.column('Order', width=25, anchor='center')
character_table.column('Character', width=200, anchor='w')
character_table.column('Lines', width=50, anchor='w')
character_table.column('Character Count', width=50, anchor='w')
character_table.column('Word Count', width=50, anchor='w')
character_table.column('Blocks', width=50, anchor='w')
character_table.column('Scenes', width=50, anchor='w')

# Pack the Treeview widget with enough space
character_table.pack(fill='both', expand=True)
notebook.add(character_tab, text='Characters')

breakdown_tab = ttk.Frame(notebook)
# Create a Treeview widget within the stats_frame for the table
breakdown_table = ttk.Treeview(breakdown_tab, columns=('Line', 'Type', 'Character','Text'), show='headings')
# Define the column headings
breakdown_table.heading('Line', text='Line')
breakdown_table.heading('Type', text='Type')
breakdown_table.heading('Character', text='Character')
breakdown_table.heading('Text', text='Text')

# Define the column width and alignment
breakdown_table.column('Line', width=25, anchor='w')
breakdown_table.column('Type', width=25, anchor='w')
breakdown_table.column('Character', width=50, anchor='w')
breakdown_table.column('Text', width=200, anchor='w')
# Pack the Treeview widget with enough space
breakdown_table.pack(fill='both', expand=True)
# Configure the tag to change the background color
breakdown_table.tag_configure('nonspeech', background='#fafafa')
breakdown_table.tag_configure('scene', background='#fffec8')
bold_font = tkFont.Font( weight="bold")
breakdown_table.tag_configure('border', background='#444444')  # A lighter shade to simulate space
breakdown_table.tag_configure('bold', font=bold_font)
notebook.add(breakdown_tab, text='Dialog')
        












def open_result_folder():
    # Open a folder in Finder using the `open` command
    print("Opening "+currentOutputFolder)
    try:
        subprocess.run(["open", currentOutputFolder], check=True)
        print("Folder successfully opened in Finder.")
    except subprocess.CalledProcessError:
        print("Failed to open the folder in Finder.")


#scene_tab = ttk.Frame(notebook)
#notebook.add(scene_tab, text='Scenes')

stats_tab = ttk.Frame(notebook)
# Create a Treeview widget within the stats_frame for the table
stats_table = ttk.Treeview(stats_tab, columns=('Line',  'Character','Text','Tout','Sans espace'), show='headings')
# Define the column headings
stats_table.heading('Line', text='Line')
stats_table.heading('Character', text='Character')
stats_table.heading('Text', text='Text')
stats_table.heading('Tout', text='Tout')
stats_table.heading('Sans espace', text='Sans espace')

# Define the column width and alignment
stats_table.column('Line', width=25, anchor='center')
stats_table.column('Character', width=100, anchor='w')
stats_table.column('Text', width=200, anchor='w')
stats_table.column('Tout', width=50, anchor='w')
stats_table.column('Sans espace', width=50, anchor='w')

# Pack the Treeview widget with enough space
stats_table.pack(fill='both', expand=True)
# Configure the tag to change the background color
stats_table.tag_configure('nonspeech', background='#fafafa')
stats_table.tag_configure('scene', background='#fffec8')
bold_font = tkFont.Font( weight="bold")
stats_table.tag_configure('border', background='#444444')  # A lighter shade to simulate space
stats_table.tag_configure('bold', font=bold_font)

notebook.add(stats_tab, text='Stats by line')


# Statistics tab
character_stats_tab = ttk.Frame(notebook)

# Create a Treeview widget within the stats_frame for the table
cols=('Line #', 'Character','Character (raw)','Line')
for i in countingMethods:
    cols= cols+(i,)
print(cols)
character_stats_table = ttk.Treeview(character_stats_tab, columns=cols, show='headings')
# Define the column headings
character_stats_table.heading('Line #', text='Line #')
character_stats_table.heading('Character', text='Character')
character_stats_table.heading('Character (raw)', text='Character (raw)')
character_stats_table.heading('Line', text='Line')
for i in countingMethods:
    character_stats_table.heading(i, text=i)


# Define the column width and alignment
character_stats_table.column('Line #', width=25, anchor='center')
character_stats_table.column('Character', width=50, anchor='w')
character_stats_table.column('Character (raw)', width=50, anchor='w')
character_stats_table.column('Line', width=100, anchor='w')
for i in countingMethods:
    character_stats_table.column(i, width=50, anchor='w')

# Pack the Treeview widget with enough space
character_stats_table.pack(fill='both', expand=True)
character_stats_table.tag_configure('total', background='#444444',foreground="#ffffff")

notebook.add(character_stats_tab, text='Stats by character')


# Statistics label
stats_label = ttk.Label(right_frame, text="Words: 0 Characters: 0", font=('Arial', 12))
stats_label.pack(side=tk.BOTTOM, fill=tk.X)

export_tab = ttk.Frame(notebook)
# Load folder button
load_button = ttk.Button(export_tab, text="Open result folder...", command=open_result_folder)
load_button.pack(side=tk.TOP, fill=tk.X)

# Load folder button
load_button = ttk.Button(export_tab, text="Open XLSX recap...", command=open_xlsx_recap)
load_button.pack(side=tk.TOP, fill=tk.X)

dropdown = ttk.Combobox(export_tab, values=countingMethods)
dropdown.pack(pady=20)
dropdown.current(0)

update_button = ttk.Button(export_tab, text="Recompute", command=reset_tables)
update_button.pack(side=tk.TOP, fill=tk.X)


method_label = ttk.Label(export_tab, text="Current Method"+countingMethod, font=('Arial', 12))
method_label.pack(side=tk.BOTTOM, fill=tk.X)


def on_value_change(event):
    reset_tables
    """ Handle changes in dropdown selection. """
    selected_value = dropdown.get()
    print("Selected:", selected_value)
    global countingMethod
    countingMethod=selected_value
    runJob(currentFilePath,selected_value)
# Bind the change event
dropdown.bind('<<ComboboxSelected>>', on_value_change)

notebook.add(export_tab, text='Export')


# Load folder button
#load_button = ttk.Button(left_frame, text="Open Folder", command=open_folder)
#load_button.pack(side=tk.TOP, fill=tk.X)

load_tree("",os.getcwd())

center_window()  # Center the window

app.mainloop()