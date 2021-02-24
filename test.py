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

moto_html = """<html><head><title>Truck Subreddit</title></head>
<body><p class="Post"><b>Motorcycles</b></p></body>
</html>
"""

car_html = """<html><head><title>Truck Subreddit</title></head>
<body>Cars</body>
</html>
"""

class MyTests(unittest.TestCase):

  def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, content, status_code):
            byte_content = str.encode(content)
            self.content = byte_content
            self.status_code = status_code

    if args[0] == 'https://localhost:1234.com/r/Trucks/':
        return MockResponse(truck_html, 200)
    elif args[0] == 'https://fakeurl.com/r/Motos/':
        return MockResponse(moto_html, 200)
    elif args[0] == 'https://anotherfakeurl.com/r/Cars/':
        return MockResponse(car_html, 200)   

    return MockResponse(None, 404)
    
  @mock.patch('requests.get', side_effect=mocked_requests_get)
  def test_truck_subreddit(self, mock_get):
    reddit_truck_url = 'https://localhost:1234.com/r/Trucks/'
    soup = get_soup_from_url(reddit_truck_url)
    self.assertIsNotNone(soup)
    posts = soup.select('.Post')
    self.assertEqual(2, len(posts))

  @mock.patch('requests.get', side_effect=mocked_requests_get)
  def test_moto_subreddit(self, mock_get):
    reddit_moto_url = 'https://fakeurl.com/r/Motos/'
    soup = get_soup_from_url(reddit_moto_url)
    self.assertIsNotNone(soup)
    posts = soup.select('.Post')
    self.assertEqual(1, len(posts))

  @mock.patch('requests.get', side_effect=mocked_requests_get)
  def test_car_subreddit(self, mock_get):
    reddit_car_url = 'https://anotherfakeurl.com/r/Cars/'
    soup = get_soup_from_url(reddit_car_url)
    self.assertIsNotNone(soup)
    posts = soup.select('.Post')
    self.assertEqual(0, len(posts))

if __name__ == '__main__':
  unittest.main()
