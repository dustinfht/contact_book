def create(entry):
    return Contact(entry[0], entry[1], entry[2], entry[3], entry[4])


class Contact:

    def __init__(self, contact_id, last_name, first_name, phone_number, last_updated):
        self.contact_id = contact_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.last_updated = last_updated
