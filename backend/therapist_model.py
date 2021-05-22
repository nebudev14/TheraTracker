class Therapist:
    """Representation of a therapist
    
    Fields
    -----
    name : str
        Full name of the therapist
    phone : str
        Phone number of the therapist
    Address : str
        Location of the therapist's office
    url : str
        Link to the therapist's profile which contains more information about their services
    """
    def __init__(self, name, phone, address, url):
        self.name = name
        self.phone = phone 
        self.address = address
        self.url = url
