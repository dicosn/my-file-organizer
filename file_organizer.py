import os
import sys
import shutil

#Put the files in there
def file_sort(filenames, series, exclusions):
    count = 0
    for file in filenames:
        if os.path.isfile(os.path.join(path, file)):
            skip = False
            for unwanted in exclusions:
                if unwanted.upper() in file.upper():
                    skip = True
                    break
            if skip == False:
                if series.upper() in file.upper():
                    sourcePath = path+"/"+file
                    destinationPath = path+"/"+series+"/"+file
                    shutil.move(sourcePath, destinationPath)
                    count += 1 
    print("All done! "+ str(count) +" file(s) moved.")

def create_new_dir(path, series="", directories=None):
    if directories == None:
        directories = []
    
    while series == "":
        series = input("Enter the keyword of the files you would like to make a directory for.\n"
                    "(e.g. if you have pictures of dogs and each file has the word \"Dog\" in it, you would enter Dog): ")

        directories = next(os.walk(path))[1] #list of directories

        for directory in directories:
            if series.upper() in directory.upper():
                if input("Directory " + directory +  " already exists. Do you want to add to a previously existing directory (Y/N)? ").upper() == "Y":
                    sort_old_dir(path, series, directories)
                    return
                series = ""
                break
    
    os.mkdir(path+"/"+series)

    exclude = input("Very good. If you would like to exclude any keywords, enter them seperated with /'s\n" 
                    "(e.g. if you want to make an album of images from the year, but exclude pics from the months of June and May\n"
                    ", you would enter: \"June/May\"), otherwise enter \"N\": ")

    print("Working...")
    exclusions = []

    if not exclude.upper() == "N":
        exclusions = exclude.strip().split('/')

    filenames = os.listdir(path)

    file_sort(filenames, series, exclusions)

    if(input("Would you like to keep working in this directory (Y/N)? ").upper() == "Y"):
        create_new_dir(path)

def sort_old_dir(path, series="", directories=None):
    if directories == None:
        directories = []
    while series == "":
        series = input("Enter the keyword of the files you would like to put in an existing directory\n"
                       "(e.g. if you have pictures of dogs and each file has the word \"Dog\" in it, you would enter Dog): ")
        directories = next(os.walk(path))[1] #list of directories
        found = False
        for directory in directories:
            if series.upper() in directory.upper():
                found = True
                break
        if found == False:
            if input("Directory " + series +  " does not exist. Do you want to make a brand new directory (Y/N)?").upper() == "Y":
                create_new_dir(path, series, directories)
                return
            series = ""
    exclude = input("Very good. If you would like to exclude any keywords, enter them seperated with /'s\n" 
                    "(e.g. if you want to make an album of images from the year, but exclude pics from the months of June and May\n"
                    ", you would enter: \"June/May\"), otherwise enter \"N\": ")

    print("Working...")
    exclusions = []

    if not exclude.upper() == "N":
        exclusions = exclude.strip().split('/')

    filenames = os.listdir(path)

    file_sort(filenames, series, exclusions)

    if(input("Would you like to keep working in this directory (Y/N)? ").upper() == "Y"):
        sort_old_dir(path)


if __name__ == "__main__":
    path = input("Enter the directory you would like to work in: ")

    if os.path.exists(path):
        print("Path is valid.")
        if not os.path.isdir(path):
            print("However, path is not a directory.")
            sys.exit()
    which_sort = 0
    while not (which_sort == '1' or which_sort == '2'):
        which_sort = input("Would you like to:\n"
                            "1. Make a new folder.\n"
                            "2. Add new files into a prexisting directory.\n"
                            "Select an option (Enter 1 or 2): ")
        if not (which_sort == '1' or which_sort == '2'):
            print("Invalid response. Enter 1 or 2.")
    if which_sort == '1':
        create_new_dir(path)
    if which_sort == '2':
        sort_old_dir(path)

    print("Goodbye!")
    sys.exit