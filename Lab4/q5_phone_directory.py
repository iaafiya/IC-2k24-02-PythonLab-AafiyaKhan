"""Q5 - Phone directory with reverse lookup and grouping."""

contacts = {
    "Anita": {"phones": ["9876543210"], "email": "anita@mail.com", "city": "Pune"},
    "Manoj": {"phones": ["9123456780", "9988776655"],
              "email": "manoj@mail.com", "city": "Delhi"},
    "Zara": {"phones": ["9000011111"], "email": "zara@mail.com", "city": "Pune"},
}


def valid_phone(number):
    return len(number) == 10 and number.isdigit()


def number_owner(number):
    return {phone: name for name, data in contacts.items()
            for phone in data["phones"]}.get(number)


def add_contact():
    name = input("Name: ").strip()
    if not name or name in contacts:
        print("Name is empty or already exists.")
        return
    phone = input("10-digit phone: ").strip()
    if not valid_phone(phone):
        print("Phone number must contain exactly 10 digits.")
        return
    owner = number_owner(phone)
    if owner:
        print(f"Number already belongs to {owner}.")
        return
    email = input("Email: ").strip()
    city = input("City: ").strip()
    contacts[name] = {"phones": [phone], "email": email, "city": city}
    print("Contact added.")


def add_number():
    name = input("Existing contact name: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input("New 10-digit number: ").strip()
    if not valid_phone(phone):
        print("Phone number must contain exactly 10 digits.")
        return
    owner = number_owner(phone)
    if owner:
        print(f"Number already belongs to {owner}.")
        return
    contacts[name]["phones"].append(phone)
    print("Number added.")


def update_contact():
    name = input("Contact name: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    field = input("Update email or city? ").strip().lower()
    if field == "email":
        contacts[name]["email"] = input("New email: ").strip()
    elif field == "city":
        contacts[name]["city"] = input("New city: ").strip()
    else:
        print("Choose email or city.")
        return
    print("Contact updated.")


def reports():
    term = input("Partial name to search: ").strip().casefold()
    matches = {name: data for name, data in contacts.items()
               if term in name.casefold()}
    print("Partial-name search:", matches if matches else "No matches.")

    reverse = {phone: name for name, data in contacts.items()
               for phone in data["phones"]}
    number = input("Number for reverse lookup: ").strip()
    print("Number belongs to:", reverse.get(number, "not found"))

    by_city = {}
    for name, data in contacts.items():
        by_city.setdefault(data["city"], []).append(name)
    print("Contacts by city:", by_city)

    print("Contacts with multiple numbers:", {
        name: data["phones"] for name, data in contacts.items()
        if len(data["phones"]) > 1
    })
    print("Directory (alphabetical):")
    for name in sorted(contacts, key=str.casefold):
        print(name, contacts[name]["phones"], contacts[name]["email"],
              contacts[name]["city"])


def main():
    while True:
        print("\n--- PHONE DIRECTORY ---")
        print("1. Add contact\n2. Add another number\n3. Update email/city")
        print("4. Delete contact\n5. Search\n6. Reports\n7. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            add_number()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            name = input("Name to delete: ").strip()
            if contacts.pop(name, None) is None:
                print("Contact not found.")
            else:
                print("Contact deleted.")
        elif choice == "5":
            term = input("Name or part of name: ").strip().casefold()
            found = {name: data for name, data in contacts.items()
                     if term in name.casefold()}
            print(found if found else "No matching contact.")
        elif choice == "6":
            reports()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
