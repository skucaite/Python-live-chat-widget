# Python live chat widget

## Introduction
This TravelBook site lets to chat for user and admin in real time. Users can start chat from the home page chatbox and admin can chat with different users from his dashboard at `http://localhost:5000/admin`.

## Getting Started

### Installing Dependencies

#### Python 3.7
Install the latest version of python for your platform in the python docs `(https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)`.

#### PIP Dependencies
First ensure you are working using your created virtual environment. Once you have your virtual environment setup and running, install dependencies by running: ```pip install -r requirements.txt```
This will install all of the required packages within the `requirements.txt` file.

### Running the server
To run the server, execute:

```bash
export FLASK_APP=main.py
flask run
```
Setting the `FLASK_APP` variable to `main.py` directs flask to use `main.py` file to run the application.

Navigate to Home page `http://localhost:5000` and `http://localhost:5000/admin` and start to chat. Have fun!
