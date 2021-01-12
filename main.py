from bs4 import BeautifulSoup
import requests
import lxml


input('Welcome, here are the latest post from subreddits: Cars, motorcycles, and Trucks. Enter any button to continue.')

class subcars():
  
    headers = ()
    url_c = 'https://www.reddit.com/r/cars/'
    response = requests.get(url_c, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')


    for item in soup.select('.Post'):
        try:
            print('----------------------------------------')
            print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())
            print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
            print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())          
            print(item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])
        except Exception as e:
            print('')

class submoto(): 

    headers = ()
    url_m = 'https://www.reddit.com/r/motorcycles/'
    response = requests.get(url_m, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')


    for item in soup.select('.Post'):
        try:
          print('----------------------------------------')
          print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())
          print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
          print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())          
          print(item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])
        except Exception as e:
           print('')


class subtruck():

    headers = ()
    url = 'https://www.reddit.com/r/Trucks/'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')


    for item in soup.select('.Post'):
        try:
            print('----------------------------------------')
            print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())
            print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
            print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())          
            print(item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])
        except Exception as e:
            print('')