Step 1: Install Redis system wide, as well as postgres and python (though it's assumed these already exist)

Step 2: Install the Python requirements (pip install -Ur requirements.txt)

Step 3: Create the modmail database and user and apply schema.sql

Step 4: Do the configuration step (copying config.example.py to config.py), filling in the appropriate fields:

```
token = "the bot's token goes here"
database info
default_prefix = "m!"
default_server = server to be proxied to
owner = me
owners = the rest of the bot dev team
main_server = default_server
```
Step 5: Run `m!setup`

Step 6: Open the proxy_guild table in your database editor and set "original" to the server ID needing to be proxied 
and "new" to the server ID where tickets will actually go. 

Step 7: Assign yourself premium and assign the backend server a slot.

Step 8: Enable advanced logging, pingrole, and access roles.
