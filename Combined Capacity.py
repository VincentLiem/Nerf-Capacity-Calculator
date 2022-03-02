import glob

files = glob.glob('* Capacity.txt')
result_file_name = 'Combined Capacity.txt'
with open(result_file_name, 'w') as combined:
    for file in files:
        with open(file) as opened:
            if file != result_file_name:
                contents = opened.read()
                combined.write(contents +'\n')
        opened.close()
