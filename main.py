from bs4 import BeautifulSoup
import requests


def subcars():

    soup = get_soup_from_url('https://www.reddit.com/r/cars/')

    for item in soup.select('.Post'):
        try:
            print('----------------------------------------')
            print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()) #Votes
            print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()) #Title
            print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text()) #Comments         
        except Exception as e:
            print('')

def submoto():

     soup = get_soup_from_url('https://www.reddit.com/r/motorcycles/')

     for item in soup.select('.Post'):
         try:
             print('----------------------------------------')
             print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()) #Votes
             print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()) #Title
             print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text()) #Comments         
         except Exception as e:
             print('')

def subtruck():

     soup = get_soup_from_url('https://www.reddit.com/r/Trucks/')

     for item in soup.select('.Post'):
         try:
             print('----------------------------------------')
             print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()) #Votes
             print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()) #Title
             print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text()) #Comments         
         except Exception as e:
             print('')

def get_soup_from_url(url):
     headers = ()
     response = requests.get(url, headers=headers)
     if response.status_code != 200:
       print('call to reddit failed!')
       return None
     soup = BeautifulSoup(response.content, 'lxml')
     return soup


def main():
    # I used previous acquired knowledge to create next lines.
     Car = 'Cars'
     Moto = 'Motorcycles'
     Truck = 'Trucks'



     name = input('Welcome, what is your name? ')
     print('')
     print(f'Hi {name}! Please type which subbreddit you want to visit.')
     print('')
     SR = input('Cars, Motorcycles, Trucks: ')



     if SR == Car:
       subcars()     
     elif SR == Moto:
       submoto()
     elif SR == Truck:
       subtruck()
  
if __name__ == '__main__':
     main()
  