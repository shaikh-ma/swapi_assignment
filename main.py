using_std_libraries = False

try:
    import requests
    import pandas as pd
    import assignment_with_non_std_libraries
except ModuleNotFoundError:
    import assignment_with_std_libraries 
    using_std_libraries = True
    print('No 3rd party libraries found!\nUsing standard modules.')


download_url     = r'https://swapi.dev/api/people/'
upload_server    = r'http://httpbin.org/anything'


upload_status = None
if using_std_libraries:
    json_data = assignment_with_std_libraries.get_data(download_url)
    if json_data is not None:
       selected_characters = assignment_with_std_libraries.get_top_characters(json_data)
       if selected_characters is not None:
           assignment_with_std_libraries.show_data(selected_characters)
           assignment_with_std_libraries.write_data(selected_characters)
           response, upload_status = assignment_with_std_libraries.post_data(upload_server, selected_characters)
else:
    json_data = assignment_with_non_std_libraries.get_data(download_url)
    if json_data is not None:
       selected_characters = assignment_with_non_std_libraries.get_top_characters(json_data)
       if selected_characters is not None:
           assignment_with_non_std_libraries.show_data(selected_characters)
           filename = assignment_with_non_std_libraries.write_data(selected_characters)
           response, upload_status = assignment_with_non_std_libraries.post_data(upload_server, filename)


if upload_status == 200:
    print('File has been uploaded successfully!') 
    print(response) 

else:
    print('Error: Encountered an error - status code :' + str(upload_status))
