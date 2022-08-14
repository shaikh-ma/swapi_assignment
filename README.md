# Task Objectives:
1. To get the data from the [The Star Wars API](https://swapi.dev/) server.
2. Extract the 10 characters appearing in most films.
3. Sort the data by height.
4. Create a csv file of the sorted data.
5. Upload the data on the [Httpbin.org](http://httpbin.org/) server.

<br>

# How to prepare the enviroment : 
##  To clone the project use the below:
```
git clone https://github.com/shaikh-ma/swapi_assignment/
```

<br>

# How to execute the program:
##  To execute the program, run the script 'main.py'
```
python main.py
```

<br>

# How to execute the test:
##  To execute the tests, run the script 'test_swapi_assignment.py'
```
python test_swapi_assignment.py
```

<br>

<br>

# About the script :
## The script has been designed using the below two approaches:
* Approach 1 : Using Python Standard libraries & builtin functions if in case the 3rd party packages are not installed.
* Approach 2 : Using 3rd party libraries (like pandas, request) in case if these packages are already installed on the user system.

## There are total 3 scripts,
1. main.py - This is the main script, it checks if the pandas, request libraries are available or not and selects the script based on it, to run the program.
2. assignment_with_std_libraries.py  - This script uses the standard modules (urllib, json, csv) with builtin functions.
3. assignment_with_non_std_libraries.py  - This script uses the 3rd party modules (pandas and requests).

<br><br>

# Functions defined in the script(s)
* get_data(*url*) 
> *  Retrieves data from the server.
> *  parameter: url -> url of the server from which to get the data.
> *  returns the data if received, otherwise None.

* get_top_characters(_json_data_, _max_characters=10_)
> * Extractes the requred data into a json object.
> * Parameters :
> * json_data : The json file containing the data from server.
> * max_characters : Number of characters for which the data should be filtered.
> * By default, extracts data for 10 characters if no value is passed.
> * Returns json format for the number of characters appearing in most films.

* write_data(_json_data_, _filename=None_) 
> * Stores the extracted data in a csv file.
> * If the file name is passed, otherwise it's named as "Exported.csv".
> * The file is saved in the same folder as the script.
> * Returns the filename.


* show_data(_selected_characters_, _max_characters=None_)
> * Prints out the json formatted data for exported data for max_characters passed. 


* post_data(_url_, _filename=''_)
> * Uploading the files to the server.
> * url      -> server URL.
> * filename -> Name of the file to be uploaded.
> * Returns the tuple containing response object from the request and the status code.

<br>


#### Author : [Shaikh Mohammed Aamir](https://github.com/shaikh-ma)
#### Date Created : 13-08-2022
#### Project Type : Test Assignment
