from requests_html import HTMLSession

s = HTMLSession()

query = 'redondo beach'
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={
          "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'})

# print(r.html.find('title', first=True))

# Hashtag = id,
weather_info = {'Fahrenheit': 'wob_tm',
                'Humidity': 'wob_hm ',
                'Wind': 'wob_ws',
                }

setting = {
    'Location': 'wob_loc',
    'Date/Time':  'wob_dts',
    'Condition': 'wob_dcp'}

for data in weather_info:
    tag = 'span#' + weather_info[data]
    content = (r.html.find(tag, first=True))
    print(data + ' ' + content.text)

for data in setting:
    tag = 'div#' + setting[data]
    content = (r.html.find(tag, first=True))
    print(data + ' ' + content.text)
