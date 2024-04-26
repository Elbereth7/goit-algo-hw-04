from file_handler import write_to_file

def add_contact_validation(name, phone):
    while True:
        user_input = input('Enter yes/no: ').strip().lower()
        if user_input == 'yes':
            return name, phone
        elif user_input == 'no':
            new_name = input(f'Please enter a new name for the contact with a phone number {phone}: ').replace(' ', '_')
            return new_name, phone
        else:
            print("Invalid answer.")

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        print(f'Contact {name} already exists with a phone number {contacts[name]}. Should I rewrite it?')
        name, phone = add_contact_validation(name, phone)           
    contacts[name] = phone
    write_to_file(contacts)
    return "Contact added."

def change_contact_validation(name, phone, contacts):
    while True:
        user_input = input('Enter yes/no: ').strip().lower()
        if user_input == 'yes':
            contacts[name] = phone
            write_to_file(contacts)
            return "Contact added."
        elif user_input == 'no':
            return "Contact skipped."
        else:
            print("Invalid answer.")

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        print(f'Contact {name} does not exist in a phone book. Should I add it?')
        return change_contact_validation(name, phone, contacts)
    else:
        contacts[name] = phone
        write_to_file(contacts)
        return "Contact updated."    

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact {name} does not exist"
    
def show_all(contacts):
    output_string = ''
    for name in contacts:
        output_string = output_string + f'Contact name: {name}, phone number: {contacts[name]}\n'
    return output_string.strip()