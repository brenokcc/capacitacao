"""
Project 5
Suppose we are writing an application that uses exceptions and we want our exception messages (and type) to be very consistent, as well as provide some way to easily list out all the possible exceptions used in our app.

Although there are many other approaches to doing this (as with any problem), let's use enumerations specifically to implement this functionality.

What we want is a mechanism whereby we can raise an exception this way:

AppException.Timeout.throw()
which will raise a custom exception ConnectionException('100 - Timeout connecting to resource')

And something like this as well:

AppException.NotAnInteger.throw()
which will raise a ValueError('200 - Value is not an integer')

This means our exception will need to contain the exception key (such as Timeout or NotAnInteger) as well as the exception class we want to raise, and the default message itself. We also want to have consistent error codes (integer values) for each exception.

We'll need to implement a throw method (we can't use the reserved name raise) that will raise the exception with the default message. In addition we'd like to be able to override the default message with a custom one if we prefer:

AppException.Timeout.throw('Timeout connecting to database')
We'll also need to implement some properties for the exception code, class (type), and message.
"""