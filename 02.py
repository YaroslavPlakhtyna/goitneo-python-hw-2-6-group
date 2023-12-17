from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value
    
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        max_length = 10
        if len(value) == max_length and all([d.isdigit() for d in value]):
            self.__value = value 


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        new_phone = Phone(value=phone)
        self.phones.append(new_phone)
        print("Phone number was added.")
    
    def edit_phone(self, old_phone, new_phone):
        for ph in self.phones:
            if ph.value == old_phone:
                ph.value = new_phone
                print("Phone number was changed.")

    def remove_phone(self, phone):
        self.phones = [ph for ph in self.phones if ph.value != phone]
        print("Phone number was removed.")

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                print(f"Here is your phone:{ph}")
                return ph
        return None
    
    def __repr__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
        print("Record was added to book.")
    
    def find(self, name):
        record = self.data.get(name)
        return record
    
    def delete(self, name):
        self.data.pop(name)
        