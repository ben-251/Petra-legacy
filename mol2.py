def error(errorType,line):
    if errorType == "no_var_error":
        print("Line",line,"No variable with This name.")
    elif errorType == "val_error":
        print("Line",line,"This is not a String or an int or a float, so idk what to do with it")
def pre_run(file):
    run(file)

def is_say(line):
    open_position = line.find("say(")
    close_position = line.find(")",open_position)

    if open_position != -1 and close_position != -1:
        return True,open_position
    return False,open_position

def is_var(line):
    open_position_var = line.find("var(")
    open_position_say = line.find("say(")
    if open_position_var > open_position_say:
        pass
    elif open_position_var < open_position_say:
        pass
    elif open_position_say == -1 and open_position_var == -1:
        pass
    comma_position = line.find(",",open_position)
    close_position = line.find(")",comma_position)
    #alex is there a point doing that here?
    if open_position == -1 or comma_position == -1 or close_position == -1:
        return False,open_position	
    return True,open_position

def find_keyword():
    var_bool,var_position = is_var(line)
    say_bool,say_position = is_say(line)

    if var_bool and say_bool:
        if say_position > var_position:
            run_vars(line)
        if say_position < var_position:
            run_prints(line,line_count)
    elif var_bool:
        run_vars(line)
    elif say_bool:
        run_prints(line,line_count)

def run(file):
    with open(file,"r") as f:
        for line in f:
            find_keyword(line)
            #read through the 
