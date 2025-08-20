# Program to read the .txt files
import os


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            yield file.read()
    except FileNotFoundError:
        return f'File not in location: {file_path}'
    except Exception as e:
        return f'An error occurred {e}'


if __name__ == '__main__':
    path = os.path.join(os.curdir, 'PACE_Patch.txt')
    for i in read_file(path):
        print(i)
