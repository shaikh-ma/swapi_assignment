import csv
import json
from pprint import pprint
from urllib import request


def get_data(url):
    """
    Retriveing data from the server.

    Parameters
    ----------
    url : str
    URL of the server from which to get the data.

    Returns
    -------
    The data if received, otherwise None.
    """

    try:
        response = request.urlopen(url=url, context=False)
    except Exception as e:
        print("Error : Couldn't reach the URL", end="\n")
        print(e, end="\n")
        return None
    else:
        if response.status == 200:
            print(
                "Success: Data retrieved successfully! - Status code: "
                + str(response.status),
                end="\n",
            )
            data = response.read().decode()
            json_data = json.loads(data)
        else:
            print(f"Error: {response.status} - Couldn't find the data", end="\n")
    return json_data


def get_top_characters(json_data, max_characters=10):
    """
    Extracting required data into a json object.

    Parameters
    ----------
    json_data : file
    The json file containing the data from server.

    max_characters : int
    Number of characters for which the data should be filtered.
    By default, extracts data for 10 characters if no value is passed.

    Returns
    --------
    json format for the number of characters appearing in most films.
    """
    try:
        int(max_characters)
    except Exception:
        print(
            "Error: Max characters should be entered as a integer number",
            end="\n",
        )
        return None

    try:
        characters = json_data["results"]
    except Exception:
        print('"Error: Required fields not found.', end="\n")
        return None
    else:
        characters.sort(key=lambda x: len(x["films"]), reverse=True)
        selected_characters = characters[:max_characters]
        selected_characters.sort(key=lambda x: int(x["height"]), reverse=True)

        species_type = []
        for character in selected_characters:
            link = character["species"]
            if link:
                link = link[0]
                sp_type = json.loads(request.urlopen(link).read().decode())
                species_type.append(sp_type["name"])
            else:
                species_type.append("")

        appearances = [len(x["films"]) for x in selected_characters]

        for ind, character in enumerate(selected_characters):
            character["species_name"] = species_type[ind]
            character["appearances"] = appearances[ind]
    return selected_characters


def write_data(selected_characters, filename="Exported.csv"):
    """
    Storing the extracted data in a csv file.
    If the file name is passed, it's named as "Exported.csv".
    The file is saved in the same folder as the script.

    Parameters
    ----------
    selected_characters:
    The DataFrame object

    filename: str
    Name of the file with which it needs to be saved.
    If not passed, it is saved as "Exported.csv"

    Returns
    -------
    Filename
    """
    with open(filename, "w", newline="") as export:
        csv_writer = csv.writer(export)
        for row in selected_characters:
            line = [
                row["name"],
                row["species_name"],
                row["height"],
                row["appearances"],
            ]
            csv_writer.writerow(line)
    print(f"Success: File Saved as {filename}", end="\n")
    return filename


def post_data(url, filename=""):
    """
    Uploading the files to the server.

    Parameters
    ----------
    url      : server URL.
    filename : Name of the file to be uploaded.

    Returns
    -------
    A tuple containing response object from the request and the status code.
    """
    if not filename:
        return None

    files = {}
    files["file"] = json.dumps(open(filename).read())

    post_data = {
        "title": "10 Characters that appeared in most Star Wars movie",
        "files": files,
    }

    try:
        json_string = json.dumps(post_data)
        post_data = json_string.encode("utf-8")
        headers = {"Content-Type": "applicatoin/json"}

        the_request = request.Request(url, data=post_data, headers=headers)
        response = request.urlopen(the_request)
    except Exception as e:
        print("Error: Couldn't reach URL", end="\n")
        print(e, end="\n")
        return None
    else:
        if response.status == 200:
            response_text = json.loads(response.read().decode("utf-8"))
            pprint(response_text)
            print(
                f"Success: File uploaded sucessfully! status: {response.status}",
                end="\n",
            )
        else:
            print(
                "Error :{response.status}: Couldn't upload file(s)!",
                end="\n",
            )
    return response_text, response.status


def show_data(selected_characters, max_characters=None):
    """
    Prints out the json formatted data for exported data.
    """

    if not max_characters:
        max_characters = len(selected_characters)

    for num, character in enumerate(selected_characters):
        if num >= max_characters:
            break
        print("-" * 50, end="\n")
        print("Character " + str(num + 1) + ":     " + character["name"])
        print("-" * 50, end="\n")
        pprint(character)
        print("-" * 50, end="\n")
    return


if __name__ == "__main__":
    from const import server, url

    using_std_lib = True

    if json_data := get_data(url):
        selected_characters = get_top_characters(json_data)
        if selected_characters is not None:
            show_data(selected_characters)
            filename = write_data(selected_characters)
            post_data(server, filename)
