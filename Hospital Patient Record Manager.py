# Initialize empty dictionary to store patient records
patients = {}

# Function to create a new patient
def create_patient():
    patient_id = input("Enter Patient ID: ")
    if patient_id in patients:
        print("Patient ID already exists!")
        return
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    condition = input("Enter Medical Condition: ")
    doctor = input("Enter Doctor's Name: ")
    
    patients[patient_id] = [name, age, condition, doctor]
    print(f"Patient {name} has been added successfully!\n")

# Function to display all patients
def display_patients():
    if not patients:
        print("No patients found!")
    else:
        print("\nID\tName\tAge\tCondition\tDoctor")
        for patient_id, details in patients.items():
            print(f"{patient_id}\t{details[0]}\t{details[1]}\t{details[2]}\t\t{details[3]}")
    print()

# Function to update a patient
def update_patient():
    patient_id = input("Enter Patient ID to update: ")
    if patient_id not in patients:
        print("Patient not found!")
    else:
        print(f"Updating details for {patients[patient_id][0]}")
        patients[patient_id][0] = input("Enter new name: ") or patients[patient_id][0]
        patients[patient_id][1] = input("Enter new age: ") or patients[patient_id][1]
        patients[patient_id][2] = input("Enter new condition: ") or patients[patient_id][2]
        patients[patient_id][3] = input("Enter new doctor: ") or patients[patient_id][3]
        print("Patient updated successfully!\n")

# Function to delete a patient
def delete_patient():
    patient_id = input("Enter Patient ID to delete: ")
    if patient_id in patients:
        del patients[patient_id]
        print(f"Patient {patient_id} deleted successfully!\n")
    else:
        print("Patient not found!\n")

# Function to filter patients
def filter_patients():
    query = input("Enter Patient Name, ID, or Condition to search: ").lower()
    found = False
    
    for patient_id, details in patients.items():
        if (query in patient_id.lower() or 
            query in details[0].lower() or 
            query in details[2].lower()):
            print(f"ID: {patient_id}, Name: {details[0]}, Age: {details[1]}, Condition: {details[2]}, Doctor: {details[3]}")
            found = True
            
    if not found:
        print("No matching patients found!\n")

# Function to sort patients by name or age
def sort_patients():
    choice = input("Sort by (1) Name or (2) Age: ")
    if choice == '1':
        sorted_patients = sorted(patients.items(), key=lambda x: x[1][0])  # Sort by name
    elif choice == '2':
        sorted_patients = sorted(patients.items(), key=lambda x: x[1][1])  # Sort by age
    else:
        print("Invalid option!\n")
        return
    
    print("\nSorted Patients:")
    for patient_id, details in sorted_patients:
        print(f"ID: {patient_id}, Name: {details[0]}, Age: {details[1]}")
    print()

# Main function to run the program
def main():
    while True:
        print("\n--- Hospital Patient Record Manager ---")
        print("1. Add New Patient")
        print("2. View All Patients")
        print("3. Update Patient Information")
        print("4. Delete Patient Record")
        print("5. Search Patient")
        print("6. Sort Patients")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            create_patient()
        elif choice == '2':
            display_patients()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            filter_patients()
        elif choice == '6':
            sort_patients()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option!\n")

# Run the main function

main()
