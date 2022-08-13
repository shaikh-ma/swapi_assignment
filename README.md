## Task Objectives:
1. To get the data from the [The Star Wars API](https://swapi.dev/) server.
2. Extract the 10 characters appearing in most films.
3. Sort the data by height.
4. Create a csv file of the sorted data.
5. Upload the data on the [Httpbin.org](http://httpbin.org/) server.

<br>

### To clone the repository use this [link](https://github.com/shaikh-ma/swapi-assignment/)
```
git clone https://github.com/shaikh-ma/swapi-assignment/
```
<br>

## The script has been designed using two methods
* Using Standard libraries using builtin functions (in case the 3rd party packages are not installed).
* Using 3rd party libraries (like pandas, request) in case these packages are already installed.
<br>

## There are 3 scripts
1. assignment_with_non_std_libraries.py - This script uses the 3rd party modules.
2. assignment_with_std_libraries.py - This script uses the builtin modules.
3. main.py - This scripts detects the available libraries and selects the one based on it.

<br><br>

# Functions defined in the script(s)
* get_data(*url*) 
> * Extracting requreed data into a json object.
> * json_data : The json file containing the data from server.
> * max_characters : Number of characters for which the data should be filtered.
> * By default, extracts data for 10 characters if no value is passed.
> * Returns json format for the number of characters appearing in most films.

* write_data(_json_data_, _filename=None_) 
> * Storing the extracted data in a csv file.
> * If the file name is passed, it's named as "Exported.csv".
> * The file is saved in the same folder as the script.
> * Returns the filename.


* show_data(_selected_characters_, _max_characters=None_)
> * Prints out the json formatted data for exported data for max_characters passed. 


* post_data(_url_, _filename=''_)
> * Uploading the files to the server.
> * url      -> server URL.
> * filename -> Name of the file to be uploaded.
> * Returns the tuple containing response object from the request and the status code.

#### Testing
> * test_with_non_std_lib.py - For testing the script 'assignment_with_non_std_libraries.py'
> * assignment_with_std_libraries.py - For testing the script 'assignment_with_std_libraries.py'
---	

#### Author : [Shaikh Mohammed Aamir](https://github.com/shaikh-ma)
#### Date Created : 13-08-2022
#### Project Type : Test Assignment
