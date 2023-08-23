import requests
from bs4 import BeautifulSoup
import re
import json

def get_first_paragraph(wikipedia_url, session):
    '''
    This function extract the first paragraph from the pages of all leaders, 
    cleans it using RegEx, puts it into the variable 'first_paragraph' 
    and returns it
    '''
    r = session.get(wikipedia_url).text               # makes request using a session object which is created in 'get_leader' function 
    soup = BeautifulSoup(r, 'lxml')                   
    paragraphs = soup.find_all('p')                   # finds all paragraphs
    first_paragraph = None                            # creates empty veriable 'first_paragraph' where data will be put
    regex_list = ["\ *\(/.+/\[e\].*\)", "\ *\(/.+/.*\)", "\[[0-9]+\]", "[\n]", "[\t]", "[\xa0]", "\[\w?\d?|\]"]          # makes a list of RegEx patterns 
    for x in paragraphs:   # loop which looks for text paragraphs in leaders pagesm cleans them with RegEx and stores them into 'first_paragraph' variable
        if x.find_parent(class_="bandeau-cell") or x.find_parent(class_="plainlist"):
            continue
        else:
            if x.text.strip():
                first_paragraph = x.text
                for n in range(len(regex_list)):
                    first_paragraph = re.sub(regex_list[n], '', first_paragraph)
                break
    return first_paragraph                              # returns 'first_paragraph' variable


def get_leaders():
    '''
    This function creats url for counries leaders, creates dictionary where stores data. 
    Keys in the dictionary are countriesm values are dictionaries with leader's names, 
    urls for the pages and text about leaders which was scraped in the function 'get_first_paragrap'
    '''
    root_url = 'https://country-leaders.onrender.com'   # creates urls
    cookie_url = root_url + '/cookie/'
    countries_url = root_url + '/countries'

    session = requests.Session()                        # creates a session object
    cookies = session.get(cookie_url).cookies           # makes cookies request using the session object
    countries = session.get(countries_url, cookies=cookies) # makes countries request using the session object  

    leaders_per_country = {}           # creates empty dictionary where data will be stored
    for country in countries.json():    # a loop  for establishing keys with country names in 'leaders_per_countries' dictionary
        leaders_url = root_url + '/leaders?country=' + country
        leaders_response = session.get(leaders_url, cookies=cookies)
        if leaders_response.status_code == 200:
            leader_data = leaders_response.json()
            leaders_per_country[country] = []

            for leader in leader_data:     # a loop for establishing values for 'leaders_per_countries' dictionary
                first_paragraph = get_first_paragraph(leader['wikipedia_url'], session)  # Pass the session object to the function 'get_first_paragraph'
                leaders_per_country[country].append({
                    'first_name': leader['first_name'],
                    'last_name': leader['last_name'],
                    'wikipedia_url': leader['wikipedia_url'],
                    'first_paragraph': first_paragraph
                })
        else:
            print(f"Error retrieving leaders for {country}")      # prints error message if coudn't retrieve data

    return leaders_per_country            # returns 'leaders_per_country' value

def save_json(leaders_per_country):
    '''
    This function saves results into json file
    '''
    with open('leaders.json', 'w') as fp:  # opens new json file
        json.dump(leaders_per_country, fp)  # stores resultd into the json file

result = get_leaders()          # calls for 'get leader' function
print(result)                   # prints results

save_json(result)                # calls for 'save_json' function

with open('leaders.json', 'r') as fp:      # opens saved file
    data = json.load(fp)                   # stores result into 'data' variable

print(data)                              # prints data variable






