import glob

files = glob.glob('* Capacity.txt')
with open("Combined Capacity.txt", "w") as combined:
    for file in files:
        with open(file) as opened:
            contents = opened.read()
            combined.write(contents)
