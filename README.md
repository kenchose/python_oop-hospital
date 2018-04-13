Patient:
Attributes:

• Id: an id number

• Name

• Allergies

• Bed number: should be none by default

Hospital
Attributes:

• Patients: an empty array

• Name: hospital name

• Capacity: an integer indicating the maximum number of patients the hospital can hold.

Methods:

• Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.

• Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
