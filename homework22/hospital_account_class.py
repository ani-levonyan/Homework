# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule.

class HospitalAccount:
    schedule = []

    def __init__(self, patient_name, patient_surname):
        self.patient_name = patient_name
        self.patient_surname = patient_surname

    def schedule_visit(self, visit_date, visit_time):
        visit = (visit_date, visit_time)
        self.schedule.append(visit)
        print(f"Visit scheduled for {visit_date} at {visit_time}")

    def remove_visit(self, visit_date, visit_time):
        visit = (visit_date, visit_time)
        if visit in self.schedule:
            self.schedule.remove(visit)
        print(f"Visit scheduled for {visit_date} at {visit_time} has been removed")


patient_1 = HospitalAccount("John", "Brown")

patient_1.schedule_visit("05/27/2024", "11:00")
patient_1.schedule_visit("05/29/2024", "11:00")
patient_1.remove_visit("05/27/2024", "11:00")
