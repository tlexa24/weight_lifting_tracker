import main
import functions
import weight_log_class
import datetime
import lift_log_class

def get_program():
    with main.connection.cursor() as cursor:
        sql = "SELECT program_ID, program_name FROM programs;"
        cursor.execute(sql)
        result = cursor.fetchall()
        choices = [str(row[0]) for row in result]
        while True:
            try:
                for row in result:
                    print(str(row[0]) + '. ' + str(row[1]))
                program = input('Which program are you using? Enter one of the above numbers: ')
                if functions.check_in_list(program, choices):
                    return program
                else:
                    print('\n\nChoose only one of the given numbers.')
                    raise ValueError
            except ValueError:
                continue

def get_routine():
    with main.connection.cursor() as cursor:
        program = get_program()
        sql = "SELECT routine_ID, routine_name FROM routines WHERE program_id = '{}';".format(program)
        cursor.execute(sql)
        result = cursor.fetchall()
        choices = [str(row[0]) for row in result]
        while True:
            try:
                for row in result:
                    print(str(row[0]) + '. ' + functions.name_converter(str(row[1])))
                routine = input('Which routine are you logging results for? Enter one of the above numbers: ')
                if functions.check_in_list(routine, choices):
                    return routine
                else:
                    print('\n\nChoose only one of the given numbers.')
                    raise ValueError
            except ValueError:
                continue

def get_exercises():
    dictconn = main.connectiondict
    with dictconn.cursor() as cursor:
        routine = get_routine()
        sql = "SELECT exercise_name, exercises.exercise_ID, reps, sets, current_weight, weight_progressor " \
              "FROM exercises_in_routines " \
              "LEFT JOIN exercises ON exercises.exercise_ID = exercises_in_routines.exercise_ID " \
              "WHERE routine_id = '{}';".format(routine)
        cursor.execute(sql)
        result = cursor.fetchall()
        dictconn.close()
        log_template = []
        for d in result:
            num_sets = d['sets']
            exercise_dict = {'name': d['exercise_name'], 'ID': d['exercise_ID'], 'progressor': d['weight_progressor'],
                             'sets': d['sets'], 'current': d['current_weight'], 'reps': d['reps']}
            for n in range(1, num_sets + 1):
                exercise_dict['Set {}'.format(n)] = {}
            log_template.append(exercise_dict)
        return log_template

def update_weight(exercise, new):
    sql = "UPDATE exercises SET current_weight = '{}' WHERE exercise_ID = '{}';".format(new, exercise)
    with main.connection.cursor() as cursor:
        cursor.execute(sql)
        main.connection.commit()

def get_results():
    template = get_exercises()
    for exercise in template:
        print('Did you use {} lbs. for {}? '.format(exercise['current'], functions.name_converter(exercise['name'])))
        confirm = functions.get_yn()
        log_weight = exercise['current']
        if confirm == 'n':
            exercise['current'] = weight_log_class.get_weight()
        # if dict['current'] != 0:
        #     print('Did you use {} lbs. for {}? '.format(dict['current'], dict['name']))
        #     confirm = functions.get_yn()
        #     log_weight = dict['current']
        #     if confirm == 'n':
        #         log_weight = weight_log_class.get_weight()
        num_sets = exercise['sets']
        successful_sets = 0
        reps_to_hit = exercise['reps']
        for n in range(1, num_sets + 1):
            while True:
                try:
                    reps = input('Input reps for {} Set #{}: '.format(exercise['name'], str(n)))
                    if functions.int_checker(reps):
                        if int(reps) >= reps_to_hit:
                            successful_sets += 1
                        exercise['Set {}'.format(str(n))] = reps
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('\nEnter only numbers.\n')
                    continue
        if successful_sets < int(num_sets) and confirm == 'n':
            update_weight(exercise['ID'], exercise['current'])
        if successful_sets == int(num_sets):
            if confirm == 'y':
                update_weight(exercise['ID'], float(exercise['current']) + int(exercise['progressor']))
            if confirm == 'n':
                update_weight(exercise['ID'], float(exercise['current']) + int(exercise['progressor']))
    return template

def create_insert_lift():
    day = str(datetime.date.today())
    lift_inputs = get_results()
    for lift in lift_inputs:
        for n in range(1, lift['sets'] + 1):
            lift_obj = lift_log_class.Lift(day, lift['ID'], lift['current'], n, lift['Set {}'.format(n)])
            lift_obj.insert()
    main.connection.close()




# lift_log = date, exerciseID, setno, reps, weight
# need to go from exercise with set numbers, to dict for each set of each exercise
# print(get_results())
