import pytest

USING_STD_LIBS = False

swapi_url = r"https://swapi.dev/api/people"
upload_server = r"https://httpbin.org/anything"
try:
    import assignment_with_non_std_libraries as script
except ModuleNotFoundError:
    import assignment_with_std_libraries as script

    USING_STD_LIBS = True


@pytest.mark.skip
def test_get_data():
    json_data = script.get_data(swapi_url)
    assert json_data

    selected_characters = script.get_top_characters(json_data)
    assert selected_characters

    filename = script.write_data(selected_characters)
    response, upload_status = script.post_data(upload_server, filename)

    assert filename is not None
    assert response is not None
    assert upload_server != 200
