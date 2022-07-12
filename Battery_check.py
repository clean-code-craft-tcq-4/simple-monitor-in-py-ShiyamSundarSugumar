from check_limit import check_function

def battery_is_ok(temperature, soc, charge_rate,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max):
    #function_pointer = [temp_is_ok,soc_is_ok,charge_rate_is_ok]
    values = [temperature,soc,charge_rate]
    min_array = [temp_min,soc_min,charge_rate_min]
    max_array = [temp_max,soc_max,charge_rate_max]
    Function_name = ["temperature","state_of_change","charge_rate"]
    j=0
    while(j<3):
        feedback = check_function(values[j],min_array[j],max_array[j])
        if(feedback == False ):
            print_console(Function_name[j])
            return False        
        j+=1
    return True
