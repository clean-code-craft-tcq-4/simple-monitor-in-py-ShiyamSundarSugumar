from battery_check import battery_is_ok



class Battery:
      
      def __init__(self) -> None:
          super().__init__()
          self.Language = "En"
          self.temp_min = 0
          self.temp_max = 45
          self.soc_min = 20
          self.soc_max = 80
          self.charge_rate_min = None
          self.charge_rate_max = 0.8


      def battery_check_warning_assert(self):
          
          #warning Assert
          assert(battery_is_ok(44, 50, 0.8,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is True)
          assert(battery_is_ok(25, 78, 0.8,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is True)
          assert(battery_is_ok(25, 50, 0.79,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is True)

      def battery_check_Error_assert(self):
                  
          #Error Assert
          assert(battery_is_ok(25, 70, 0.7,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is True)
          assert(battery_is_ok(50, 90, 0.9,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is False)
          assert(battery_is_ok(50, 80, 0.5,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is False)
          assert(battery_is_ok(40, 90, 0.5,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is False)
          assert(battery_is_ok(40, 75, 0.9,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is False)
          assert(battery_is_ok(55, 90, 0.5,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is False)
          assert(battery_is_ok(55, 70, 1.0,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is False)
          assert(battery_is_ok(40, 90, 0.9,self.temp_min,self.temp_max,self.soc_min,self.soc_max,self.charge_rate_min,self.charge_rate_max) is False)
          
                  


if __name__ == '__main__':
      bat = Battery()
      bat.battery_check_warning_assert()
      bat.battery_check_Error_assert()
