# 1. Create a class that contains information about employees of a company
#    define methods to get/set employee name, job title, and start date.
class Employee():
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date


# 2. Copy this `Company` class into your module.

class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

    def get_company_name(self):
        """Returns the name of the company"""
        return self.company_name

    def set_new_employee(self, employee):



# Add the remaining methods to fill the requirements above


# 3. Consider the concept of [aggregation](../FND_11_INHERIT_COMPOSE_AGGREGATE.md#aggregation),
#    modify the `Company` class so that you assign employees to a company.

# 4. Create a company, and three employees, and then assign the employees to the company.
