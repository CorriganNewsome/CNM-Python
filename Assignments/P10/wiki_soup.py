sun_url = urlopen('https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration')
sun = BeautifulSoup(sun_url, 'html.parser')
tables = sun.find_all('table')

#Dictionary to hold the name of the country and its corresponding temperature
country_suns = {}

#Dictionary to hold the country and its frequency in the table
count = {}
for table in tables:
    if len(table) >1:
        rows = table.find_all('tr')
        
        #Skip the first row, which is the name of the columns
        for row in rows[1:]:
            cells = row.find_all('td')
            country = cells[0].text.strip()
            
            #If country in the list of country we found previously
            #append the country to the dictionary
            if country in countries:
                
                sun = cells[-2].text.strip()
                sun = process_num(sun)/10
                
                #If country is already in the dictionary
                #add to the existing sun hours of that country and the count to keep track of how many times we add
                if country in country_suns:
                    count[country] += 1
                    country_suns[country] += sun
                    
                else:
                    count[country] = 1
                    country_suns[country] = sun
                    

#Find the average temperature of each country
for country in country_suns:
    print(country_suns[country],count[country])
    country_suns[country] = round(country_suns[country]/count[country],2)
    print('Country: {}, Sunshine Hours: {}'.format(country,country_suns[country]))
                