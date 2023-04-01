# FARM Stack Boiler plates

A Repository to house a collection of FARM stack boiler plates to speed up project kickoff.


FARM Stack:
    * Fast API
    * React.js
    * Mongo DB



## FARM-auth

### Configuration
You will need to create a .env file for the server of the farm-auth project containing:
    * MONGO_DETAILS = <mongo_connection_string>
    * SECRET_KEY = <secret_key>

The MONGO_DETAILS string is the connection string for your Mongo database, while the SECRET_KEY is the salt for our JWT Handler