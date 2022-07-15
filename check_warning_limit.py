from Print import print_warning,German_pring_warning

def warning_function(value,min,max,function_name):
    warning_value = Warning_value_finder(min, max)
    feedback = warning_check_function(value,min,warning_value[0],warning_value[1],max)
    if(feedback == True):
        print_warning(function_name)
        German_pring_warning(function_name)

def Warning_value_finder(min,max):
    Warning_factor_value = max*0.05 
    if(min != None):
       warning_min_value = min + Warning_factor_value
    else:
        warning_min_value = min
    warning_max_value = max - Warning_factor_value
    return warning_min_value,warning_max_value

def warning_check_function(value,min_low_range,min_high_range,max_low_range,max_high_range):
    if(min_low_range == None):
        return check_warning_max_only(value,max_low_range,max_high_range)
    else:
       return check_warning_range(value,min_low_range,min_high_range,max_low_range,max_high_range)

def check_warning_max_only(value,max_low_range,max_high_range):
    if(max_low_range<=value) and (value < max_high_range):
        return True
    return False

def warning_check_function(value,min_low_range,min_high_range,max_low_range,max_high_range):
    if(min_low_range == None):
        return check_warning_max_only(value,max_low_range,max_high_range)
    else:
       return check_warning_range(value,min_low_range,min_high_range,max_low_range,max_high_range)

def check_warning_max_only(value,max_low_range,max_high_range):
    if(max_low_range<=value) and (value < max_high_range):
        return True
    return False

def check_warning_range(value,min_low_range,min_high_range,max_low_range,max_high_range):
    
    max_feedback = check_warning_max(value,max_low_range,max_high_range)
    min_feedback = check_warning_min(value,min_low_range,min_high_range)
    if(max_feedback and min_feedback):
        return True
    return False

def check_warning_max(value,max_low_range,max_high_range):
    if(((max_low_range<= value) and (value < max_high_range))):
        return True
    return False


def check_warning_min(value,min_low_range,min_high_range):
    if(((min_low_range< value) and (value <=min_high_range))):
        return True
    return False





