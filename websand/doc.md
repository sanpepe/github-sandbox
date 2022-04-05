context global static object that will hold the gateway
gateway is the database

You can't really think about high level structure unlesss you have an implementation to reference it to

### Use cases
1. Licenses are data objects that store, type of license, user and a codecast. These objects are store in database
1. Assuming user and codecast are already stored in DB, when you want to know if a user is licensed to view a codecast it searches all the stored licenses (each has a user and codecast) trying to find a match for the given user adn codecast