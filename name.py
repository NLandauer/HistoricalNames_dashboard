# Module has accessors for each attribute, gets data from Database.readNames()

# declare class Name with 6 private attributes
class Name:
    def __init__(self, name, sex, year, count, total, rank):
        self.__name = name
        self.__sex = sex
        self.__year = year
        self.__count = count
        self.__total = total
        self.__rank = rank

# Accessors for 6 pieces of data
    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def get_year(self):
        return self.__year

    def get_count(self):
        return self.__count

    def get_total(self):
        return self.__total

    def get_rank(self):
        return self.__rank


# Pass user input name, sex to database query
# Call Database.readNames to fetch data
# Return data as list of name objects
    @staticmethod
    def readNames(name, sex):
        from database import Database
        return Database.readNames(name, sex)

