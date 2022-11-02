from lxml import html
import requests

def html_cleanup(string):
    updated_string = str.join(" ", string.split('\t'))
    updated_string = str.join("", updated_string.split('\r'))
    updated_string = updated_string.split(" ")
    return {updated_string[0]: updated_string[-1]}


def get_big_trio(user_details):

    url = (f"https://alabe.com/cgi-bin/chart/astrobot.cgi?INPUT1={user_details.get('username')}&INPUT2=&GENDER={user_details.get('gender')}&MONTH={user_details.get('month')}&DAY={user_details.get('day')}&YEAR={user_details.get('year')}&HOUR={user_details.get('hour')}&MINUTE={user_details.get('minute')}&AMPM={user_details.get('am_or_pm')}&TOWN={user_details.get('city')}&COUNTRY=USA&STATE={user_details.get('state')}&INPUT9=&Submit=Submit")

    r = requests.get(url)
    tree = html.fromstring(r.content)
    elements = tree.xpath('//*[@id="printReady"]/p[1]/strong/text()')
    big_trio = [html_cleanup(detail) for detail in elements if detail.find('Rising') > -1 or detail.find('Sun') > -1 or detail.find('Moon') > -1]

    big_trio = { k: v for item in big_trio for k, v in item.items()}
    return big_trio

my_details = {
    'username': 'tawnthanh',
    'gender': 'female',
    'month': 5,
    'day': 12,
    'year': 1989,
    'hour': 10,
    'minute': 24,
    'am_or_pm': 'pm',
    'city': 'Boston',
    'state': 'MA'
}

get_big_trio(my_details)