from Battery_check import*

if __name__ == '__main__':

  temp_min = 0
  temp_max = 45
  soc_min = 20
  soc_max = 80
  charge_rate_min = None
  charge_rate_max = 0.8


  assert(battery_is_ok(25, 70, 0.7,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is True)
  assert(battery_is_ok(50, 90, 0.9,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(50, 80, 0.5,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(40, 90, 0.5,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(40, 75, 0.9,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(55, 90, 0.5,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(55, 70, 1.0,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(40, 90, 0.9,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  
