from .database import Database


class UserData:

    def __init__(self, data: dict):
        """ Initialization \n
        Keyword Arguments: \n
        `data` -- User data received from the form on the site
        """
        self.first_name = data['first_name']
        self.last_name = data['last_name']

        date_birth = data['date_birth']
        if date_birth:
            self.birth_day = date_birth.timetuple()[2]
            self.birth_month = date_birth.timetuple()[1]
            self.birth_year = date_birth.timetuple()[0]

        city = data['city']
        if city:
            self.city = Database.get_city_id(city)
        
    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'
