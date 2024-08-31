import unittest

USING_STD_LIBS = False
swapi_url = r"http://swapi.dev/api/people"
upload_server = r"http://httpbin.org/anything"
try:
    import pandas
    import requests

    import assignment_with_non_std_libraries as script
except ModuleNotFoundError:
    import assignment_with_std_libraries as script

    USING_STD_LIBS = True


class TestSwapi(unittest.TestCase):
    def setUp(self):
        self.json_data = script.get_data(swapi_url)
        if self.json_data:
            self.selected_characters = script.get_top_characters(self.json_data)
        if self.selected_characters:
            # script.show_data(self.selected_characters)
            self.filename = script.write_data(self.selected_characters)
            self.response, self.upload_status = script.post_data(
                upload_server, self.filename
            )

    def test_get_data(self):
        self.assertNotEqual(self.json_data, None)

    def test_get_top_characters(self):
        self.assertNotEqual(len(self.selected_characters), 0)

    def test_write_data(self):
        self.assertNotEqual(self.filename, None)

    def test_post_data(self):
        self.assertNotEqual(self.response, None)
        self.assertNotEqual(upload_server, 200)


if __name__ == "__main__":
    unittest.main()
