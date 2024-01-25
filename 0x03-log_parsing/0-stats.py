#!/usr/bin/python3
'''reads stdin line by line and computes metrics'''
from sys import stdin


def main():
    '''Reads logs from standard input and generates reports'''

    line = 0
    filesize = 0
    status_code = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for i in stdin:
            line += 1
            i = i.split()
            try:
                filesize += int(i[-1])
                if i[-2] in codes:
                    try:
                        status_code[i[-2]] += 1
                    except KeyError:
                        status_code[i[-2]] = 1
            except (IndexError, ValueError):
                pass
            if line == 10:
                _print(filesize, status_code)
                line = 0
        _print(filesize, status_code)
    except KeyboardInterrupt as e:
        _print(filesize, status_code)
        raise


def _print(filesize, status_code):
    '''prints output of main'''

    print(f'File size: {filesize}')
    for k, v in sorted(status_code.items()):
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
