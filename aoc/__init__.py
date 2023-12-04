import datetime
import sys

def today():
    return datetime.datetime.now().day

def run_script(func):
    test_mode = '-t' in sys.argv
    if test_mode:
        input_file = 'test.txt'
    elif len(sys.argv) > 1:
        input_file = sys.argv[1] 
    else:
        input_file = f'../inputs/day_{today():02}/input.txt'
    
    print(f"Reading from {input_file}")
    with open(input_file, 'r', encoding='ascii') as fh:
        lines = [l.strip() for l in fh.readlines()]
    
    func(lines)
        