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

# lightningPy

lightning exercise 1

* Write a function that takes a list, a number, and a string as args.
* The string parameter should have a default value.
* In the function body, loop over the list and output the items.
* Use slice to loop through only the first n items in the array, where n = the value of the second argument.
* Each item should be prefaced by value of the string argument
  * One example output might then be "I have visited the city of San Francisco" if "San Francisco" was an item in the list, and the string argument was "I have visited the city of "
* Try it out! Execute the function both with and without passing in a value for the string parameter