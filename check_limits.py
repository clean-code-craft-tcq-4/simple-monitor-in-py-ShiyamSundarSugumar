
def Temperature_check(temperature):
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
        return False

def State_of_charge_check(soc):
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
        return False

def charge_rate_check(charge_rate):
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False

def battery(temperature,soc,charge_rate):
    ftpr = [Temperature_check, State_of_charge_check, charge_rate_check ]
    values = [temperature,soc,charge_rate]
    i=0
    for condition in ftpr:
        check = condition(values[i])
        if(check == False):
            return False
        i+=1

    return True




if __name__ == '__main__':


  assert(battery(25, 70, 0.7) is True)
  assert(battery(50, 85, 0) is False)
