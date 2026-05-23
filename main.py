import pprint

using_std_libraries = False

from const import server, url

try:
    import assignment_with_non_std_libraries
except ModuleNotFoundError:
    import assignment_with_std_libraries

    using_std_libraries = True
    print("No 3rd party libraries found!\n\nUsing standard modules.\n\n")

upload_status = None
if using_std_libraries:
    if json_data := assignment_with_std_libraries.get_data(url):
        selected_characters = assignment_with_std_libraries.get_top_characters(
            json_data
        )
        if selected_characters is not None:
            print("\n Showing data summary :")
            assignment_with_std_libraries.show_data(selected_characters)
            filename = assignment_with_std_libraries.write_data(selected_characters)
            response, upload_status = assignment_with_std_libraries.post_data(
                server, filename
            )
else:
    if json_data := assignment_with_non_std_libraries.get_data(url):
        selected_characters = assignment_with_non_std_libraries.get_top_characters(
            json_data
        )
        if selected_characters is not None:
            assignment_with_non_std_libraries.show_data(selected_characters)
            filename = assignment_with_non_std_libraries.write_data(selected_characters)
            response, upload_status = assignment_with_non_std_libraries.post_data(
                server, filename
            )


print()
if upload_status == 200:
    print("-" * 50)
    print("File has been uploaded successfully!")
    print("-" * 50)
    print("\n")
    print("-" * 50)
    print("Response from HttpBin.org")
    print("-" * 50)
    print()
    pprint.pprint(response)
    print("\n\n")
    print("-" * 50)

else:
    print("-" * 50)
    print("Error: Encountered an error - status code :" + str(upload_status))
    print("-" * 50)


print("\n\n\n")

exit_app = ""

while exit_app.strip().lower() not in ("q", "quit", "exit"):
    exit_app = input("To exit enter 'q','quit','exit' :")
