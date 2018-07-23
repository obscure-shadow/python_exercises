# Python Stock Dictionary Exercise 1

## References

* [Python dictionaries](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries)
* [Learn Python - Dictionaries](https://www.learnpython.org/en/Dictionaries)
* [Introducing Dictionaries](http://www.diveintopython.net/native_data_types/index.html#odbchelper.dict)

## Instructions

A block of publicly traded stock has a variety of attributes, we'll look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

### Example

```python
stockDict = { 'GM': 'General Motors',
    'CAT':'Caterpillar', 'EK':"Eastman Kodak" }
```

Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

### Example

```python
purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 ) ]
```

Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the `stockDict` to look up the full company name. This is the basic relational database join algorithm between two tables.

Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

# Python Car Sets Exersize 2

## References

* [Python sets](https://docs.python.org/3.6/tutorial/datastructures.html#sets)
* [Set intersection](https://docs.python.org/3.6/library/stdtypes.html?highlight=intersection#set.intersection)
* [Learn Python - Sets](http://www.learnpython.org/en/Sets)

## Instructions

1. Create an empty set named `showroom`.
1. Add four of your favorite car model names to the set.
1. Print the length of your set.
1. Pick one of the items in your show room and add it to the set again.
1. Print your showroom. Notice how there's still only one instance of that model in there.
1. Using `update()`, add two more car models to your showroom with another set.
1. You've sold one of your cars. Remove it from the set with the `discard()` method.

### Acquiring more cars

1. Now create another set of cars in a variable `junkyard`. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the `showroom` set.
1. Use the `intersection` method to see which cars exist in both the showroom and that junkyard.
1. Now you're ready to buy the cars in the junkyard. Use the `union` method to combine the junkyard into your showroom.
1. Use the `discard()` method to remove any cars that you acquired from the junkyard that you want in your showroom.

# Python Planet List Exersize 3
## Planet Lists
### Exercise:

1. Use `append()` to add Jupiter and Saturn at the end of the list.
2. Use the `extend()` method to add another list of the last two planets in our solar system to the end of the list.
3. Use `insert()` to add Earth, and Venus in the correct order.
4. Use `append()` again to add Pluto to the end of the list.
5. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
6. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the `del` operation to remove it from the end of planet_list.

# Python Tuples Exersize 4

Tuples are like lists, but are immutable. They can't be modified once defined. However, finding values in a tuple is faster than in a list.

## References

* [Python tuples](https://docs.python.org/3.6/tutorial/datastructures.html#tuples-and-sequences)
* [Introducing Tuples](http://www.diveintopython.net/native_data_types/tuples.html)

## Instructions

1. Create a tuple named `zoo` that contains your favorite animals.
1. Find one of your animals using the `.index(value)` method on the tuple.
1. Determine if an animal is in your tuple by using `for value in tuple`.
1. Create a variable for each of the animals in your tuple with this cool feature of Python.

    ```
    # example
    (lizard, fox, mammoth) = zoo
    print(lizard)
    ```

1. Convert your tuple into a list.
1. Use `extend()` to add three more animals to your zoo.
1. Convert the list back into a tuple.

# Classes Python Exercise 5


## Instructions

1. Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.

2. Copy this `Company` class into your module.

    ```
    class Company(object):
        """This represents a company in which people work"""

        def __init__(self, company_name, date_founded):
            self.company_name = company_name
            self.date_founded = date_founded

        def get_company_name(self):
            """Returns the name of the company"""

            return self.company_name

        # Add the remaining methods to fill the requirements above
    ```

3. Consider the concept of [aggregation](../FND_11_INHERIT_COMPOSE_AGGREGATE.md#aggregation), and modify the `Company` class so that you assign employees to a company.
4. Create a company, and three employees, and then assign the employees to the company.


# The Family Dictionary

## Instructions

1. Define a dictionary that contains information about several members of your family. Use the following example as a template.
    ```
    my_family = {
        'sister': {
            'name': 'Krista',
            'age': 42
        },
        'mother': {
            'name': 'Cathie',
            'age': 70
        }
    }
    ```
2. Using a dictionary comprehension, produce output that looks like the following example.
    ```
    Krista is my sister and is 42 years old
    ```

    > **Helpful hint:** To convert an integer into a string in Python, it's `str(integer_value)`

# Kill Nickelback

In this exercises, you're going to use a conditional statement inside a comprehension. Let's look at a basic example.

```python
nums = range(10)
small_numbers = [num for num in nums if num < 6]
# Only add numbers to the new list if the value is less than 6

words = ['big', 'red', 'dog', 'ate', 'his', 'food']
three_letters_words = [ word.title() for word in words if len(word) == 3 ]
# len(stringVariable) is equivalent to stringVariable.length in JavaScript
```


## Instructions

1. Define a set that contains tuples. Each tuple should contain two strings:
    1. The name of an artist
    1. A song by that artist

    Make sure that some of the songs are from the band Nickelback. You can see a [list of their greatest hits](https://www.amazon.com/Best-Nickelback-1/dp/B00FFERTUK/) on Amazon.
    ```
    # Example set
    songs = {
        ('Nickelback', 'How You Remind Me'),
        ('Will.i.am', 'That Power'),
        ('Miles Davis', 'Stella by Starlight'),
        ('Nickelback', 'Animals')
    }
    ```
2. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

# Squared Randoms

## References

* [Random module](https://docs.python.org/3.6/library/random.html)
* [Python Lists](https://docs.python.org/3.6/tutorial/datastructures.html)

## Instructions

1. Using the `random` module and the `range` method, generate a list of 20 random numbers between 0 and 49.
    ```
    import random

    random_numbers = [...insert awesome code here...]
    print(random_numbers)
    ```
2. With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is `[2, 5]`, the final list will be `[4, 25]`.

# Bangazon Data Model

## Overview

You need to build the ERD and initial data model for the Bangazon, LLC organization. This will be the base database schema that you will be using for many of the applications that will be built for the company.

## Instructions

### ERD

Build an ERD to define the properties of the following resources and the relationships between them. There are some properties defined for each resources, but they are the bare minimum. Use your own life skills and knowledge to add appropriate properties to each one where you see fit.

> **Technical Note:** These are the main resources that are needed in the database and is *not* an all-inclusive list of tables that should be created.

#### Employees
* An employee can only be assigned to one department
* An employee can sign up for one, or more, training programs

#### Departments
* A department has a supervisor, a specific kind of Employee
* A department has an expense budget

#### Computers
* Track when a computer was purchased by the company
* Track when a computer was decommissioned by the company
* A computer can only be assigned to one employee at a time

#### Training Programs
* A training program must have a start date
* A training program must have an end date
* A training program must have maximum attendees specified

#### Product Types
* These are categories of Products

#### Products
* A product can only have one type
* A product has a price
* A product has a title
* A product has a description
* Products will be created by customers, so make sure that you have the appropriate column on the Product table

#### Orders
* A customer can only have one active order at a time

#### Payment Types
* A customer can have multiple payment types (Visa, Amex, bank account, etc)
* A payment type must have an account number
* An order must be given a payment type before it is complete, but it not needed when order is created

#### Customers
* A customer's first and last name should be recorded separately
* The date that a customer created an account must be tracked
* If a customer does not interact with the system for over 240 days, they will be marked as inactive

### Create tables and data

Create a SQL script that is able to build the tables that you defined in your ERD. The script must also create a few rows in each table.

> **Pro tip:** Remember to ask the two questions when dealing with data relationships. Can X have many Y? Can Y have many X?


# fib

just having a little fun with the fibonacci sequence...


# lightningPy

lightning exercise 1

* Write a function that takes a list, a number, and a string as args.
* The string parameter should have a default value.
* In the function body, loop over the list and output the items.
* Use slice to loop through only the first n items in the array, where n = the value of the second argument.
* Each item should be prefaced by value of the string argument
  * One example output might then be "I have visited the city of San Francisco" if "San Francisco" was an item in the list, and the string argument was "I have visited the city of "
* Try it out! Execute the function both with and without passing in a value for the string parameter
