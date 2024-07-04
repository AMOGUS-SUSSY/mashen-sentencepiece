import os
import numpy as np
import argparse
#import sentencepiece as spm
from tqdm import tqdm

# Run from mashen-data
IN = "big_data"
NPY = "filenames"
NEW_DOC_TOKEN = b"<D>"
TMP_FILENAME = "concat.txt"

# Save paths into a list and returns said list
def get_contents(file_absolute_paths):   
    contents = []
    for filename in file_absolute_paths:
        with open(filename, "rb") as f:
            content = f.read()
        # replace all the \r\n with \n 
        content = content.replace(b"\r\n", b"\n")
        # trim the text to remove empty space at the beginning and end
        content = content.strip()

        contents.append(content)
    print(f"Loaded {len(contents)} files!")
    return contents

def get_data_from_dir(dir):
    """
    Walks through the dir folder.

    Args:
        dir (str): Path to the data folder.
    """
    all_files = []
    for root, dirs, files in tqdm(list(os.walk(dir))):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    
    return list(all_files)

def get_books3_file_paths(books3_dir, file_names):
    """
    Walks through the raw books3 folder and checks if the filenames exist.

    Args:
        books3_dir (str): Path to the books3 root folder.
        file_names (list): List of the file names.

    Raises>
        ValueError: If a file name is not found.
    """
    all_files = {}
    for root, dirs, files in tqdm(list(os.walk(books3_dir))):
        for file_name in files:
            all_files[os.path.splitext(file_name)[0]] = os.path.join(root, file_name)
    
    books3_paths = []
    for fn in file_names:
        if not fn in all_files.keys():
            raise ValueError(f"Filename {fn} not found when walking through {books3_dir}")
        else:
            books3_paths.append(all_files[fn])
    
    return list(books3_paths)

def main(is_books3):

    contents = []

    if (is_books3):
        for root, dirs, files in os.walk(NPY):
            for file in files:
                print(os.path.join(root, file))
                load_in = np.load(os.path.join(root, file))
                names = [fn[0] for fn in load_in]
                contents += get_contents(get_books3_file_paths(IN, names))
        
    else:
        contents = get_contents(get_data_from_dir(IN))
        
    concat_contents = NEW_DOC_TOKEN + NEW_DOC_TOKEN.join(contents)
    if os.path.exists(TMP_FILENAME):
        os.remove(TMP_FILENAME)
    with open(TMP_FILENAME, 'wb') as f:
        f.write(concat_contents)

if __name__ == "__main__":
    # Use argparse to get command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--is_books3", action=argparse.BooleanOptionalAction, help="Is input-data books3")
    args = parser.parse_args()

main(args.is_books3)