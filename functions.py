
# Checks if number can be converted into int
def int_checker(num):
    result = False
    try:
        int(num)
        result = True
    except ValueError:
        pass
    return result

def float_checker(num):
    result = False
    try:
        float(num)
        result = True
    except ValueError:
        pass
    return result

def length_checker(var, needed_len):
    return len(var) == needed_len

def max_length(var, maxi):
    return len(var) <= maxi

def float41_checker(num):
    if float_checker(num) and max_length(num, 5) and max_length(num.split('.')[1], 1):
        return True
    else:
        return False

def time_checker(var):
    if int_checker(var) and length_checker(var, 2):
        return True
    else:
        return False

def get_time(w_r):
    while True:
        try:
            hours = input('Input number of hours (hh): ')
            minutes = input('Input number of minutes(mm): ')
            if w_r == 'w':
                if time_checker(hours) and time_checker(minutes):
                    time = hours + ':' + minutes + ':00'
                    return time
                else:
                    raise ValueError
            seconds = input('Input number of seconds(ss): ')
            times = []
            times.extend([hours, minutes, seconds])
            for t in times:
                if time_checker(t):
                    continue
                else:
                    raise ValueError
            return times
        except ValueError:
            print('Input again, using only numbers and two digits for each\n')
            continue

def run_time():
    times = get_time('r')
    time = ':'.join(times)
    return time

def get_time_of_day():
    ap = 4
    while True:
        try:
            ampm = input('AM or PM? ')
            if ampm == 'AM' or ampm == 'am':
                ap = 0
                break
            elif ampm == 'PM' or ampm == 'pm':
                ap = 1
                break
            else:
                raise ValueError
        except ValueError:
            print('\nSelect AM, am, PM, or pm:\n')
            continue
    time = get_time('w')
    if ap == 0:
        return time
    times = time.split(':')
    hours = str(int(times[0]) + 12)
    minutes = times[1]
    seconds = '00'
    times = [hours, minutes, seconds]
    time = ':'.join(times)
    return time

def get_miles():
    while True:
        try:
            miles = input('How many miles (xxx.x): ')
            if float41_checker(miles):
                return str(miles)
            else:
                raise ValueError
        except ValueError:
            print('Input again, using only numbers in xxx.x format:\n')
            continue

def get_yn():
    while True:
        try:
            y_n = input('Enter y/n: ')
            if y_n == 'y' or 'n':
                return y_n
            else:
                raise ValueError
        except ValueError:
            print('\nEnter only y/n\n')
            continue

def get_weight():
    while True:
        try:
            weight = input('Enter the weight: ')
            if float41_checker(weight):
                return str(weight)
            else:
                raise ValueError
        except ValueError:
            print('Input again, using only numbers in xxx.x format:\n')
            continue

def get_bf():
    while True:
        try:
            bf = input('Enter the body fat % in xx.x format: ')
            if float41_checker(bf):
                return str(bf)
            else:
                raise ValueError
        except ValueError:
            print('Input again, using only numbers in xxx.x format:\n')
            continue