# Task Objectives:
1. To get the data from the [The Star Wars API](https://swapi.dev/) server.
2. Extract the 10 characters appearing in most films.
3. Sort the data by height.
4. Create a csv file of the sorted data.
5. Upload the data on the [Httpbin.org](http://httpbin.org/) server.

<br>

# How to prepare the enviroment : 
## Clone the project:
```
git clone https://github.com/shaikh-ma/swapi_assignment/
```

<br>

# How to execute the program:
## Execute the program:
```
python main.py
```

<br>

# How to execute the test:
## Execute the tests:
```
python test_swapi_assignment.py
```

<br>

<br>

# About the script :
## The script has been designed using the below two approaches:
* Approach 1 : Using Python Standard libraries & builtin functions if in case the 3rd party packages are not installed.
* Approach 2 : Using 3rd party libraries (like pandas, requests) in case if these packages are already installed on the user system.

<br><br>

## There are total 3 scripts,
| Script name | What it does  |
| ---- | --- |
| main.py | This is the main script, it checks if the pandas, requests libraries are available or not and selects the script based on it, to run the program.|
| assignment_with_std_libraries.py  | This script uses the standard modules (urllib, json, csv) with builtin functions. |
| assignment_with_non_std_libraries.py  | This script uses the 3rd party modules (pandas and requests). |

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

# Output :

## Exported data  
![generated_csv](https://github.com/user-attachments/assets/bfa23098-811d-49de-9a9d-6f13132187e1)


## Generated CSV file content :
| Sr.no| Character name     | Species | Height | Appearances |
| ---- | -----------------  | ------- | ------ | ----------- |
|  1   | Darth Vader        |   -     |   202  |      4      |
|  2   | Biggs Darklighter  |   -     |   183  |      1      |
|  3   | Obi-Wan Kenobi     |   -     |   182  |      6      |
|  4   | Owen Lars          |   -     |   178  |      3      |
|  5   | Luke Skywalker     |   -     |   172  |      4      |
|  6   | C-3PO              |  Droid  |   167  |      6      |
|  7   | Beru Whitesun lars |   -     |   165  |      3      |
|  8   | Leia Organa        |   -     |   150  |      4      |
|  9   | R5-D4              |  Droid  |   97   |      1      |
|  10  | R2-D2              |  Droid  |   96   |      6      |
       
<!--Image:      
![generated_csv](https://github.com/shaikh-ma/swapi_assignment/blob/main/generated_csv.JPG) -->

## Response from HttpBin.org for POST request:
<!--![post_request_response](https://github.com/shaikh-ma/swapi_assignment/blob/main/results.JPG) -->
![results](https://github.com/user-attachments/assets/ace4c05f-6b5c-4590-a0d9-0d735b783aaa)

## Test Results :
<!-- ![test_results](https://github.com/shaikh-ma/swapi_assignment/blob/main/test_Result.JPG) -->
![test_Result](https://github.com/user-attachments/assets/a4cc0b8d-a5ea-40d1-b990-4258811240eb)

----

<br>

#### Author: [Shaikh Mohammed Aamir](https://github.com/shaikh-ma)
#### Date Created: 13-08-2022
