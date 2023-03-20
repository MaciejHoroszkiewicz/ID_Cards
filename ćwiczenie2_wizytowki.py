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

    #def __str__(self):
	    #return f"{self.name} {self.last_name} {self.email}"
    
class BusinessContact(BaseContact):
     def __init__(self, job, company_name, work_phone, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.job = job
         self.company_name = company_name
         self.work_phone = work_phone

def create_contacts(type, count):
    contacts = []
    for i in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        if type == "base":
            phone = fake.phone_number()
            contact = BaseContact(first_name, last_name, phone, email)
        elif type == "business":
            job = fake.job()
            company_name = fake.company()
            work_phone = fake.phone_number()
            contact = BusinessContact(job, company_name, work_phone, first_name, last_name, fake.phone_number(), email)
        contacts.append(contact)
    return contacts

base_contacts = create_contacts("base", 3)
business_contacts = create_contacts("business", 3)

#by_lastname_private = sorted(base_contacts, key=lambda person: person.last_name)
#by_lastname_work = sorted(business_contacts, key=lambda person: person.last_name)

for card in base_contacts:
    card.contact()
    print(card.label_length)

for card in business_contacts:
    card.contact()
    print(card.label_length)