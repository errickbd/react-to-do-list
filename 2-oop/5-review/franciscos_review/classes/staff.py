from person import Person

class Staff(Person): #Where is person coming from?
    def __init__(self,name,age,role,employee_id,password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id