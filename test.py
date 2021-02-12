import unittest
from unittest import mock
from main import get_soup_from_url

truck_html = """<html><head><title>Truck Subreddit</title></head>
<body>
<p class="Post"><b>Big truck</b></p>
<p class="Post"><b>Small truck</b></p>
</body>
</html>
"""

class MyTests(unittest.TestCase):

  def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, content, status_code):
            byte_content = str.encode(content)
            self.content = byte_content
            self.status_code = status_code

    if args[0] == 'https://localhost:1234/r/Trucks/':
        return MockResponse(truck_html, 200)
    # TODO: add more URLs and HTML responses to test all your subreddit calls!
    # elif args[0] == 'http://someotherurl.com/anothertest':
    #     return MockResponse('some html', 200)

    return MockResponse(None, 404)
    
  @mock.patch('requests.get', side_effect=mocked_requests_get)
  def test_truck_subreddit(self, mock_get):
    reddit_truck_url = 'https://localhost:1234/r/Trucks/'
    soup = get_soup_from_url(reddit_truck_url)
    self.assertIsNotNone(soup)
    posts = soup.select('.Post')
    self.assertEqual(2, len(posts))
    # We can even assert that our mocked method was called with the right parameters
    self.assertIn(mock.call(reddit_truck_url), mock_get.call_args_list)

if __name__ == '__main__':
  unittest.main()