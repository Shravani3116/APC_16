from patient.patient import patient_details
from doctor.doctor import doctor_details
from billling.bill import calculate_bill
from medical_records.record import add_record

patient = input("Enter patient name: ")
age = int(input("Enter patient age: "))

doctor = input("Enter doctor name: ")
specialization = input("Enter specialization: ")

disease = input("Enter disease: ")

consultation = float(input("Enter consultation fee: "))
medicine = float(input("Enter medicine cost: "))

print("\n--- Hospital Management ---")

patient_details(patient, age)

doctor_details(doctor, specialization)

add_record(patient, disease)

bill = calculate_bill(consultation, medicine)
print("Total Bill:", bill)