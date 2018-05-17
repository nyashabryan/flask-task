Flask-Task
==========

This is a pre-interview task for the position of **junior front-end and integration engineer** at BusinessOptics.

The goal of these tasks is to build a very simple banking app that displays your bank balance over time, allows you to update it, and then also shows the equivalent bitcoin value. It is broken up into 5 stages. Once you have completed each stage. Store it in the folder named "stage-X", then create a copy and move on.

This is a simple task and should not take you too long to do. We are interested in the clarity and simplicity of your code. Please include a README on how to run this, a requirements.txt file would be nice to. At a minimum this expects that you can get the python components completed, if you are not comfortable with the javascript sections you submit in a any case.

Fork this repository and when completed send a message to "jobs@businessoptics.biz" with the relevant github repo address.
# Requirements

Check the requirements.txt

# Running flask App


Start the Flask server for each stage using the following commands:

1. export FLASK_APP=server.py
2. flask run

Visit the local server IP address as defined by flask. http://127.0.0.1:5000/

Visiting this link should render the page.


## Notes

### Stage 1
The route to see the bank the balance is set at "/". Also, the rendered page uses Google Font's so, it looks better when used with internet access. The page is being rendered using the Jinja2 template engine and is called base.html.


### Stage 2

For a quick aesthetic design, bootstrap4 was used in the design to make it look better. Be sure to use the templates with an active internet connection to access the necessary stylesheets and JS.


### Stage 4

The values of the BitCoin were calculated using the "ask" rate not the bid rate. 


### (5)
Now instead of doing a page reload to add a new balance, use Javascript to do an asynchronous request. This should save the result to the server and adds a new row to the balances table. You may use any javascript library or framework you want (but don't go over board, this should be simple, probably use jquery). I suggest you create a single new endpoint "api/update" that take a Rand figure and returns the full balance history until now, and then you re-render the balance table.
