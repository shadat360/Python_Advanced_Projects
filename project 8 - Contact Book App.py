contacts = {}

while True:
    print('\nContact Book App')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Count contact')
    print('7. Exit')

    choice = input("Enter your choice = ")

    if choice == '1':
        name = input('Enter your name = ')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            while True:
                age = input('Enter age = ')
                if age.isdigit():
                    age = int(age)
                    break
                else:
                    print("Invalid age! Please enter a number.")

            while True:
                mobile = input('Enter mobile number = ')
                if mobile.isdigit():
                    break
                else:
                    print("Invalid mobile number! Please enter digits only.")
    
            
            email = input('Enter email = ')
            contacts[name] = {'age':age, 'email':email, 'mobile':mobile}
            print(f'Contact name {name} has been created successfully!') 


    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f"Name:{name}, Age:{contact['age']}, Mobile Number:{contact['mobile']}, Email:{contact['email']}")
        else:
            print('Contact not found!')


    elif choice == '3':
        name = input('Enter name to update contact = ')
        if name in contacts:
            while True:
                 age = input('Enter updated age = ')
                 if age.isdigit():
                    age = int(age)
                    break
                 else:
                    print("Invalid age! Please enter a number.")

            while True:
                 mobile = input('Enter updated mobile number = ')
                 if mobile.isdigit():
                    break
                 else:
                    print("Invalid mobile number! Please enter digits only.")        

            email = input('Enter updated email = ')
            contacts[name] = {'age':age, 'email':email, 'mobile':mobile}  
            print(f'Contact name {name} has been updated successfully!')

        else:
            print('Contact not found!')


    elif choice == '4':
        name = input('Enter contact name to delete = ')   
        if name in contacts:
            del contacts[name] 
            print(f'Contact name {name} has been deleted successfully!')
        else:
            print('Contact not found!')


    elif choice == '5':
        search_name = input("Enter contact name to search = ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name:{name}, Age:{contact['age']}, Mobile Number:{contact['mobile']}, Email:{contact['email']}")
                found = True
        if not found:
            print('No contact found with that name')

 
    elif choice == '6':
        if len(contacts) == 0: 
            print("No contacts in the book yet!")
        else:
            print(f'Total contacts in your book : {len(contacts)}')

 
    elif choice == '7':
        print('Good bye...Closing the program')
        break

 
    else:
        print('Invalid input!')                  

    