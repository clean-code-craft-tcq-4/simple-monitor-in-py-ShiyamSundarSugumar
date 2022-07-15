

from Print import print_Error,German_Print_Error

def check_function(value,min,max,function_name):
    if(min == None):
        feedback =  check_the_max_only(value, max)
    else:
        feedback = check_the_range(value, min,max)
    
    if(feedback == False):
        print_Error(function_name)
        German_Print_Error(function_name)
        

    return feedback

def check_the_range(value,min,max):
    if(value< min or value > max):
        return False
    return True
def check_the_max_only(value,max):
    if( value > max ):
        return False
    return True

