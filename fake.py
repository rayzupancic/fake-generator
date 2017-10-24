from faker import Factory
from faker.providers import BaseProvider
import numpy as np

##############################################################
# name: fakeuserdata
# description: generate fake computer user data for analysis including
#              names, departments, cities, and models
##############################################################



class FakeUserData:
    'generate fake user data by object or record'

    def __init__(self,fake):
        self.name = fake.name()
        self.serial = fake.ean()
        self.city = fake.city()
        self.country_code = fake.country_code()
        self.manu = fake.makes()

    def printIt(self):
        print('{0:s},{1:s},{2:s},{3:s},{4:s}'.format(self.name, self.serial, self.city, self.country_code,self.manu))


class ComputerManufacturer(BaseProvider):
    '''Create a custom provider that inherits BaseProvider and provides manufacturer assignments weighted by ratio of ov       erall modles  to size of overal deployment'''

    def makes(self):
        manufacturer = ['Dell','HP','Lenovo','Apple','Toshiba']
        p_dist = [.4,.2,.3,.090,.010]
        return np.random.choice(manufacturer,size=1,p=p_dist)[0]

class Department(BaseProvider):
    '''Create a provider that inherits BaseProvider and provides Department assignments weighted by ratio of overall
       employees to size of department'''

    def dept(self):

        depts = ['Marketing','IT','Sales','Research','Warehouse']
        # weights of choices in order or depts
        p_dist = [.1,.2,.1,.2,.4]
        # return a weighted random choice
        return np.random.choice(depts,size=1,p=p_dist)[0]

def main():
    fake = Factory.create()
    datalist = []

    # Add the manufacturer
    fake.add_provider(ComputerManufacturer)
    fake.add_provider(Department)

    for i in range(40):
        datalist.append( FakeUserData(fake))
        datalist[-1].printIt()


if __name__ == "__main__":
    main()
