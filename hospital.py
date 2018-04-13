class Patient(object):
    id_num = 0
    def __init__(self, name, allergies = "None", bed_num = "None"):
        Patient.id_num += 1
        self.id_num = Patient.id_num
        self.bed_num = bed_num
        self.name = name
        self.allergies = allergies

    def display(self):
        print 'ID num: {}. Name: {}. Allergies: {}. Bed number: {}'.format(self.id_num, self.name, self.allergies, self.bed_num)
        return self

class Hospital(Patient):
    def __init__(self, hospital_name, capacity):
        self.hospital_name = hospital_name
        self.patient_list = []
        self.capacity = capacity

    def admit(self, new_patient):
        if len(self.patient_list) <= self.capacity:
            self.patient_list.append(new_patient)
            new_patient.bed_num = self.patient_list.index(new_patient)
            print "{} has been admiteed into {} Hospital to bed number {}".format(new_patient.name, self.hospital_name, new_patient.bed_num)
        else:
            print "{} cannot be admitted because {} has reached capacity".format(new_patient.name, self.hospital_name)
        return self

    def discharge(self, old_patient):
    #     for patient in patient_list:
    #         if patient == self.old_patient.name:
    #             patient.indexOf 

    #     return self


 
patient1 = Patient('Kenny')
hospital1 = Hospital('Jude', 5)
hospital1.admit(patient1)