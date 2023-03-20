from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def contact(self):
         print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.last_name}.")

    @property
    def label_length(self):
         return len(self.name) + len(self.last_name) + 1

    def __str__(self):
	    return f"{self.name} {self.last_name} {self.email}"
    
class BusinessContact(BaseContact):
     def __init__(self, job, company_name, work_phone, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.job = job
         self.company_name = company_name
         self.work_phone = work_phone

def create_contacts(count):
    names = [(fake.first_name(), fake.last_name(), fake.email()) for i in range(count)]
    base_contacts = [BaseContact(name, last_name, fake.phone_number(), email) for name, last_name, email in names]
    business_contacts = [BusinessContact(fake.job(), fake.company(), fake.phone_number(), name, last_name, fake.phone_number(), email) for name, last_name, email in names]
    return base_contacts, business_contacts

base_contacts, business_contacts = create_contacts(2)


#by_lastname_private = sorted(base_contacts, key=lambda person: person.last_name)
#by_lastname_work = sorted(business_contacts, key=lambda person: person.last_name)

for card in base_contacts:
    print(card)
    card.contact()
    print("")

for card in business_contacts:
    print(f"{card}; {card.company_name}")
    card.contact()
    print("")