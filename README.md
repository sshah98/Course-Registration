# Course Registration Automation

### About:
GWU uses BanWeb to register for courses. When 10,000 students log in at the same time, it can be difficult to sign up for the courses you want. This python script saves time by automatically logging in and entering the courses, minimizing the amount of time spent to sign in. 

### For Those Without Python:
* Install Python 3.6.5 for:
[Mac](https://www.python.org/ftp/python/3.6.5/python-3.6.5-macosx10.6.pkg), [Windows](https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe), [Linux](https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz)

* `pip install virtualenv` or `pip3 install virtualenv`

### To Use:
* Create a virtual environment:
`virtualenv -p python3 env`

* Source the environment
`source env/bin/activate`

* Install the necessary pip packages
`pip install -r requirements.txt`

* Run the python script in your terminal
`python registration.py`
