
from check_main_limit import check_function
from check_warning_limit import warning_function

def battery_is_ok(temperature, soc, charge_rate,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max):
    
    values = [temperature,soc,charge_rate]
    min_array = [temp_min,soc_min,charge_rate_min]
    max_array = [temp_max,soc_max,charge_rate_max]
    Function_name = ["temperature","state_of_change","charge_rate"]
    j=0    
    while(j<3):       
        warning_function(values[j],min_array[j],max_array[j],Function_name[j])           
        feedback = check_function (values[j],min_array[j],max_array[j],Function_name[j])
        if(feedback == False):
            return False    
        j+=1
    return feedback

