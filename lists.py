nationalities = ['Algerian', 'American', 'Argentinian', 'Australian', 'Austrian', 'Bahraini', 'Bangladeshi',
                'Belarusian', 'Belgian', 'Beninese', 'Bolivian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian',
                'Burkinabe', 'Burmese', 'Cambodian', 'Cameroonian', 'Canadian', 'Chilean', 'Chinese', 'Colombian',
                'Congolese', 'Croatian', 'Cypriot', 'Czech', 'Danish', 'Dominican', 'Dutch', 'Egyptian', 'Emirati',
                'Eritrean', 'Estonian', 'Ethiopian', 'Filipino', 'Finnish', 'French', 'German', 'Ghanaian', 'Greek',
                'Haitian', 'Honduran', 'Hong Konger', 'Hungarian', 'Icelandic', 'Indian', 'Indonesian', 'Iranian',
                'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Japanese', 'Jordanian', 'Kazakh', 'Kenyan',
                'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner',
                'Lithuanian', 'Malagasy', 'Malaysian', 'Malian', 'Maltese', 'Mauritanian', 'Mauritian', 'Mexican',
                'Moldovan', 'Mongolian', 'Moroccan', 'Mozambican', 'Nepali', 'New Zealand', 'Nicaraguan', 'Nigerian',
                'Nigerien', 'North Korean', 'Norwegian', 'Omani', 'Pakistani', 'Palestinian', 'Panamanian',
                'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan',
                'Salvadoran', 'Saudi Arabian', 'Senegalese', 'Sierra Leonean', 'Singaporean', 'Slovak', 'Slovenian',
                'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Swedish', 'Swiss',
                'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Tunisian', 'Turkish', 'Ugandan', 'Ukrainian',
                'Uruguayan', 'Uzbek', 'Venezuelan', 'Vietnamese', 'Yemeni', 'Zimbabwean']

countries = ['Algeria', 'Argentina', 'Australia', 'Austria', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Benin',
            'Bolivia', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Cambodia', 'Cameroon', 'Canada', 'China',
            'Colombia', 'Croatia', 'Cyprus', 'Czech Republic', "Côte d'Ivoire", 'DR Congo', 'Denmark',
            'Dominican Republic', 'Egypt', 'El Salvador', 'Eritrea', 'Estonia', 'Ethiopia', 'Finland', 'France',
            'Germany', 'Ghana', 'Greece', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia',
            'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait',
            'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Madagascar',
            'Malaysia', 'Mali', 'Malta', 'Mauritania', 'Mexico', 'Moldova', 'Mongolia', 'Morocco', 'Mozambique',
            'Myanmar', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Norway',
            'Oman', 'Pakistan', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
            'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Sierra Leone', 'Singapore', 'Slovakia',
            'Slovenia', 'Somalia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'Sudan', 'Sweden',
            'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tunisia', 'Turkey', 'Turkmenistan',
            'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan',
            'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

cities = {
    'Algeria': ['Algiers', 'Oran', 'Constantine'],
    'Argentina': ['Buenos Aires', 'Cordoba', 'Rosario', 'Mendoza', 'La Plata', 'San Miguel de Tucuman'],
    'Australia': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Gold Coast', 'Newcastle', 'Canberra', 'Sunshine Coast', 'Wollongong', 'Hobart', 'Geelong', 'Townsville', 'Cairns', 'Darwin', 'Launceston'],
    'Austria': ['Vienna', 'Graz', 'Linz', 'Salzburg', 'Innsbruck', 'Klagenfurt', 'Villach', 'Wels', 'Steyr'],
    'Bahrain': ['Manama', 'Muharraq', 'Riffa', 'Hamad Town'],
    'Bangladesh': ['Dhaka', 'Chittagong', 'Khulna', 'Rajshahi', 'Comilla'],
    'Belarus': ['Minsk', 'Gomel', 'Mogilev'],
    'Belgium': ['Brussels', 'Antwerp', 'Ghent', 'Charleroi', 'Liege', 'Bruges', 'Namur'],
    'Benin': ['Cotonou', 'Porto-Novo', 'Parakou'],
    'Bolivia': ['Santa Cruz de la Sierra', 'El Alto', 'La Paz', 'Cochabamba', 'Oruro', 'Sucre', 'Tarija', 'Potosi'],
    'Brazil': ['Sao Paulo', 'Rio de Janeiro', 'Salvador', 'Brasilia', 'Fortaleza', 'Belo Horizonte'],
    'Brunei': ['Bandar Seri Begawan', 'Kuala Belait', 'Seria', 'Tutong', 'Bangar'],
    'Bulgaria': ['Sofia', 'Plovdiv', 'Varna'],
    'Burkina Faso': ['Ouagadougou', 'Bobo-Dioulasso', 'Koudougou'],
    'Cambodia': ['Phnom Penh', 'Battambang', 'Siem Reap', 'Sihanoukville', 'Poipet', 'Kampong Cham', 'Kampong Speu', 'Kampot'],
    'Cameroon': ['Douala', 'Yaounde', 'Garoua'],
    'Canada': ['Toronto', 'Montreal', 'Vancouver', 'Calgary', 'Edmonton', 'Ottawa', 'Mississauga', 'Winnipeg', 'Quebec City', 'Hamilton', 'Brampton', 'Surrey', 'Laval', 'Halifax', 'London'],
    'China': ['Shanghai', 'Beijing', 'Tianjin', 'Guangzhou', 'Shenzhen', 'Wuhan', 'Dongguan', 'Hong Kong', 'Chongqing', 'Chengdu', 'Nanjing', 'Taipei', 'Nanchong', 'Xi\'an', 'Shenyang', 'Hangzhou', 'Harbin', 'Taiyuan', 'Suzhou', 'Zhengzhou', 'Changsha', 'Dalian'],
    'Colombia': ['Bogota', 'Medellin', 'Cali'],
    'Croatia': ['Zagreb', 'Split', 'Rijeka', 'Osijek', 'Zadar'],
    'Cyprus': ['Nicosia', 'Limassol', 'Larnaca'],
    'Czech Republic': ['Prague', 'Brno', 'Ostrava'],
    "Côte d'Ivoire": ['Abidjan', 'Bouaké', 'Daloa'],
    'DR Congo': ['Kinshasa', 'Lubumbashi', 'Mbuji-Mayi'],
    'Denmark': ['Copenhagen', 'Aarhus', 'Odense', 'Aalborg', 'Frederiksberg', 'Esbjerg', 'Randers'],
    'Dominican Republic': ['Santo Domingo', 'Santiago de los Caballeros', 'Santo Domingo Oeste', 'Santo Domingo Este', 'Santo Domingo Norte', 'San Pedro de Macoris'],
    'Egypt': ['Cairo', 'Alexandria', 'Giza', 'Shubra El-Kheima', 'Port Said', 'Suez', 'Luxor', 'El-Mahalla El-Kubra', 'Tanta', 'Asyut'],
    'El Salvador': ['San Salvador', 'Soyapango', 'Santa Ana', 'San Miguel'],
    'Eritrea': ['Asmara'],
    'Estonia': ['Tallinn', 'Tartu', 'Narva'],
    'Ethiopia': ['Addis Ababa', 'Dire Dawa', 'Mekele'],
    'Finland': ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu', 'Turku', 'Jyvaskyla', 'Lahti', 'Kuopio', 'Pori'],
    'France': ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille', 'Rennes', 'Reims', 'Le Havre', 'Saint-Etienne', 'Toulon', 'Grenoble', 'Dijon', 'Nimes', 'Angers', 'Villeurbanne'],
    'Germany': ['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Frankfurt', 'Stuttgart', 'Dusseldorf', 'Dortmund', 'Essen', 'Leipzig', 'Bremen', 'Dresden', 'Hanover', 'Nuremberg', 'Duisburg', 'Bochum', 'Wuppertal', 'Bielefeld', 'Bonn', 'Mannheim'],
    'Ghana': ['Accra', 'Kumasi', 'Tamale'],
    'Greece': ['Athens', 'Thessaloniki', 'Patras', 'Heraklion', 'Larissa', 'Volos', 'Rhodes', 'Ioannina', 'Chania', 'Chalcis'],
    'Haiti': ['Port-au-Prince', 'Carrefour', 'Delmas'],
    'Honduras': ['Tegucigalpa', 'San Pedro Sula', 'Choloma'],
    'Hungary': ['Budapest', 'Debrecen', 'Szeged', 'Miskolc', 'Pecs', 'Gyor'],
    'Iceland': ['Reykjavik', 'Kopavogur', 'Hafnarfjordur', 'Akureyri', 'Reykjanesbaer'],
    'India': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Visakhapatnam', 'Indore', 'Thane', 'Bhopal', 'Pimpri-Chinchwad', 'Patna', 'Vadodara'],
    'Indonesia': ['Jakarta', 'Surabaya', 'Medan', 'Bandung', 'Bekasi', 'Palembang', 'Tangerang', 'Makassar', 'South Tangerang', 'Semarang', 'Depok', 'Padang', 'Denpasar', 'Bandar Lampung', 'Bogor', 'Malang', 'Pekanbaru', 'Batam', 'Banten', 'Surakarta'],
    'Iran': ['Tehran', 'Mashhad', 'Isfahan'],
    'Iraq': ['Baghdad', 'Basra', 'Mosul'],
    'Ireland': ['Dublin', 'Cork', 'Limerick', 'Galway', 'Waterford', 'Drogheda', 'Dundalk', 'Swords', 'Bray', 'Navan'],
    'Israel': ['Jerusalem', 'Tel Aviv', 'Haifa'],
    'Italy': ['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice', 'Verona', 'Messina', 'Padua', 'Trieste', 'Brescia', 'Parma', 'Taranto', 'Prato', 'Modena'],
    'Japan': ['Tokyo', 'Yokohama', 'Osaka', 'Nagoya', 'Sapporo', 'Kobe', 'Kyoto', 'Fukuoka', 'Kawasaki', 'Saitama', 'Hiroshima', 'Sendai', 'Kitakyushu', 'Chiba', 'Sakai', 'Niigata', 'Hamamatsu', 'Shizuoka', 'Sagamihara', 'Okayama'],
    'Jordan': ['Amman', 'Zarqa', 'Irbid', 'Russeifa', 'Al Quwaysimah', 'Aqaba', 'As Salt', 'Ar Ramtha', 'Al Mafraq', 'Madaba'],
    'Kazakhstan': ['Almaty', 'Karaganda', 'Shymkent', 'Taraz', 'Nur-Sultan', 'Kyzylorda', 'Semey', 'Aktobe', 'Uralsk', 'Pavlodar'],
    'Kenya': ['Nairobi', 'Mombasa', 'Nakuru', 'Eldoret', 'Kisumu', 'Thika', 'Malindi', 'Kitale', 'Garissa', 'Kakamega'],
    'Kuwait': ['Kuwait City', 'Al Ahmadi', 'Hawalli'],
    'Kyrgyzstan': ['Bishkek', 'Osh', 'Jalal-Abad', 'Karakol', 'Tokmok'],
    'Laos': ['Vientiane', 'Pakse', 'Savannakhet', 'Luang Prabang'],
    'Latvia': ['Riga', 'Daugavpils', 'Liepaja'],
    'Lebanon': ['Beirut', 'Tripoli', 'Sidon'],
    'Liberia': ['Monrovia', 'Gbarnga', 'Bensonville'],
    'Libya': ['Tripoli', 'Benghazi', 'Misrata'],
    'Lithuania': ['Vilnius', 'Kaunas', 'Klaipeda'],
    'Luxembourg': ['Luxembourg City', 'Esch-sur-Alzette', 'Dudelange'],
    'Madagascar': ['Antananarivo'],
    'Malaysia': ['Kuala Lumpur', 'Johor Bahru', 'Ipoh', 'Kuching', 'Petaling Jaya', 'Shah Alam', 'Kota Kinabalu', 'Sandakan', 'Seremban', 'Kuantan'],
    'Mali': ['Bamako', 'Sikasso', 'Mopti'],
    'Malta': ['Birkirkara', 'Qormi', 'Mosta', 'Zabbar', 'San Pawl il-Bahar', 'Saint John'],
    'Mauritania': ['Nouakchott', 'Nouadhibou', 'Nema'],
    'Mexico': ['Mexico City', 'Ecatepec', 'Guadalajara', 'Puebla', 'Ciudad Juarez', 'Tijuana', 'Ciudad Nezahualcoyotl', 'Monterrey', 'Leon', 'Zapopan', 'Naucalpan', 'Merida', 'Tlalnepantla', 'Chihuahua', 'San Luis Potosi', 'Aguascalientes', 'Hermosillo', 'Saltillo', 'Mexicali', 'Culiacan'],
    'Moldova': ['Chisinau', 'Tiraspol', 'Balti', 'Bender', 'Ribnita'],
    'Mongolia': ['Ulaanbaatar', 'Erdenet', 'Darhan', 'Khovd', 'Olgii', 'Ulaangom', 'Moron', 'Suhbaatar', 'Bayankhongor', 'Dzuunharaa'],
    'Morocco': ['Casablanca', 'Rabat', 'Fes', 'Sale', 'Marrakesh', 'Agadir', 'Tangier', 'Meknes', 'Oujda', 'Kenitra'],
    'Mozambique': ['Maputo', 'Matola', 'Beira', 'Nampula', 'Chimoio'],
    'Myanmar': ['Yangon', 'Mandalay', 'Naypyidaw', 'Mawlamyine', 'Bago'],
    'Nepal': ['Kathmandu', 'Pokhara', 'Patan', 'Biratnagar', 'Birganj', 'Dharan', 'Bharatpur', 'Janakpur', 'Dhangadhi', 'Butwal'],
    'Netherlands': ['Amsterdam', 'Rotterdam', 'The Hague', 'Utrecht', 'Eindhoven', 'Tilburg'],
    'New Zealand': ['Auckland', 'Wellington', 'Christchurch', 'Manukau', 'Waitakere', 'North Shore', 'Hamilton', 'Dunedin', 'Tauranga', 'Lower Hutt'],
    'Nicaragua': ['Managua', 'Leon', 'Masaya', 'Tipitapa', 'Chinandega'],
    'Niger': ['Niamey', 'Zinder', 'Maradi'],
    'Nigeria': ['Lagos', 'Kano', 'Ibadan', 'Kaduna', 'Port Harcourt', 'Benin City', 'Maiduguri', 'Zaria', 'Aba', 'Jos'],
    'North Korea': ['Pyongyang'],
    'Norway': ['Oslo', 'Bergen', 'Trondheim', 'Stavanger', 'Drammen', 'Fredrikstad', 'Kristiansand', 'Sandnes', 'Tromso', 'Sarpsborg'],
    'Oman': ['Muscat', 'Seeb', 'Salalah', 'Bawshar', 'Suhar', 'As Suwayq', 'Ibri', 'Saham', 'Barka', 'Rustaq'],
    'Pakistan': ['Karachi', 'Lahore', 'Faisalabad', 'Rawalpindi', 'Multan', 'Hyderabad', 'Gujranwala', 'Peshawar', 'Rahim Yar Khan', 'Quetta'],
    'Panama': ['Panama City', 'San Miguelito', 'Tocumen', 'David', 'Arraijan', 'Colon', 'Las Cumbres', 'La Chorrera', 'Pacora', 'Santiago'],
    'Paraguay': ['Asuncion', 'Ciudad del Este', 'San Lorenzo', 'Luque', 'Capiata'],
    'Peru': ['Lima', 'Arequipa', 'Callao', 'Trujillo', 'Chiclayo', 'Iquitos', 'Huancayo', 'Piura', 'Chimbote', 'Cusco'],
    'Philippines': ['Quezon City', 'Manila', 'Caloocan', 'Budta', 'Davao', 'Malingao', 'Cebu City', 'General Santos', 'Taguig', 'Pasig'],
    'Poland': ['Warsaw', 'Lodz', 'Krakow', 'Wroclaw', 'Poznan', 'Gdansk', 'Szczecin', 'Bydgoszcz', 'Lublin', 'Katowice'],
    'Portugal': ['Lisbon', 'Porto', 'Amadora', 'Braga', 'Setubal', 'Coimbra', 'Queluz', 'Funchal', 'Cacem', 'Vila Nova de Gaia'],
    'Qatar': ['Doha', 'Ar Rayyan', 'Umm Salal Muhammad'],
    'Romania': ['Bucharest', 'Iasi', 'Cluj-Napoca', 'Timisoara', 'Craiova', 'Constanta'],
    'Russia': ['Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Nizhny Novgorod', 'Samara', 'Omsk', 'Kazan', 'Chelyabinsk', 'Rostov-on-Don'],
    'Rwanda': ['Kigali', 'Butare', 'Gitarama', 'Ruhengeri', 'Gisenyi', 'Byumba', 'Cyangugu', 'Kibuye', 'Kibungo', 'Nzega'],
    'Saudi Arabia': ['Riyadh', 'Jeddah', 'Mecca', 'Medina', 'Al-Ahsa', 'Ta\'if', 'Dammam', 'Buraydah', 'Khobar', 'Tabuk'],
    'Senegal': ['Dakar', 'Grand Dakar', 'Thies Nones', 'Saint-Louis', 'Ziguinchor'],
    'Sierra Leone': ['Freetown', 'Bo', 'Kenema', 'Koidu', 'Makeni', 'Lunsar', 'Port Loko', 'Waterloo', 'Kabala', 'Magburaka'],
    'Singapore': ['Singapore'],
    'Slovakia': ['Bratislava', 'Kosice', 'Presov', 'Nitra', 'Zilina', 'Banska Bystrica', 'Poprad'],
    'Slovenia': ['Ljubljana', 'Maribor', 'Celje', 'Kranj', 'Velenje'],
    'Somalia': ['Mogadishu'],
    'South Africa': ['Cape Town', 'Durban', 'Johannesburg', 'Soweto', 'Pretoria', 'Port Elizabeth', 'Pietermaritzburg', 'Benoni', 'Tembisa', 'Vereeniging'],
    'South Korea': ['Seoul', 'Busan', 'Incheon', 'Daegu', 'Daejeon', 'Gwangju', 'Suwon', 'Ulsan', 'Goyang', 'Seongnam'],
    'Spain': ['Madrid', 'Barcelona', 'Valencia', 'Seville', 'Zaragoza', 'Malaga', 'Murcia', 'Palma', 'Las Palmas de Gran Canaria', 'Bilbao'],
    'Sri Lanka': ['Colombo', 'Galkissa', 'Moratuwa', 'Jaffna', 'Negombo', 'Pita Kotte', 'Sri Jayewardenepura Kotte', 'Kandy', 'Trincomalee', 'Kalmunai'],
    'Sudan': ['Khartoum', 'Omdurman', 'Port Sudan', 'Kassala', 'Al-Ubayyid', 'Kusti', 'Wad Madani', 'El Obeid', 'El Geneina', 'Ad-Damazin'],
    'Sweden': ['Stockholm', 'Gothenburg', 'Malmo', 'Uppsala', 'Vasteras'],
    'Switzerland': ['Zurich', 'Geneva', 'Basel', 'Lausanne', 'Bern', 'Winterthur', 'Lucerne', 'St. Gallen', 'Lugano', 'Biel/Bienne'],
    'Syria': ['Aleppo', 'Damascus', 'Homs', 'Hama', 'Latakia'],
    'Tajikistan': ['Dushanbe', 'Khujand', 'Kulob', 'Qurghonteppa', 'Istaravshan'],
    'Tanzania': ['Dar es Salaam', 'Mwanza', 'Zanzibar', 'Arusha'],
    'Thailand': ["Bangkok", "Nonthaburi", "Samut Prakan", "Chiang Mai", "Udon Thani", "Nakhon Ratchasima", "Hat Yai", "Pak Kret", "Si Racha", "Phra Pradaeng", "Lampang", "Khon Kaen", "Surat Thani", "Nakhon Si Thammarat", "Ubon Ratchathani", "Pattaya", "Nakhon Sawan", "Chiang Rai", "Songkhla", "Phitsanulok"],
    'Togo': ['Lome', 'Sokode', 'Kara'],
    'Tunisia': ['Tunis', 'Sfax', 'Sousse'],
    'Turkey': ['Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Adana', 'Gaziantep', 'Konya', 'Cankaya', 'Antalya', 'Bagcilar'],
    'Turkmenistan': ['Ashgabat', 'Turkmenabat', 'Dasoguz', 'Mary', 'Balkanabat'],
    'Uganda': ['Kampala', 'Gulu', 'Lira', 'Mbarara', 'Jinja', 'Bwizibwera'],
    'Ukraine': ['Kiev', 'Kharkiv', 'Dnipro', 'Odessa', 'Donetsk', 'Zaporizhia', 'Lviv', 'Kryvyi Rih', 'Mykolaiv', 'Mariupol'],
    'United Arab Emirates': ['Dubai', 'Abu Dhabi', 'Sharjah', 'Al Ain'],
    'United Kingdom': ['London', 'Birmingham', 'Glasgow', 'Liverpool', 'Leeds', 'Sheffield', 'Edinburgh', 'Bristol', 'Manchester', 'Leicester', 'Coventry', 'Kingston upon Hull', 'Bradford', 'Cardiff', 'Belfast', 'Stoke-on-Trent', 'Wolverhampton', 'Plymouth', 'Nottingham', 'Southampton', 'Reading', 'Derby', 'Dudley', 'Newcastle upon Tyne', 'Northampton', 'Portsmouth', 'Luton', 'Preston', 'Aberdeen', 'Milton Keynes', 'Sunderland', 'Norwich', 'Walsall', 'Swansea', 'Bournemouth', 'Southend-on-Sea', 'Swindon', 'Oxford', 'Dundee', 'Poole', 'Huddersfield', 'York', 'Ipswich', 'Blackpool', 'Middlesbrough', 'Bolton', 'Peterborough', 'Stockport', 'Brighton', 'Telford', 'West Bromwich', 'Slough', 'Gloucester', 'Cambridge', 'Watford', 'Rotherham', 'Newport', 'Exeter', 'Eastbourne', 'Colchester', 'Crawley', 'Sutton Coldfield', 'Blackburn', 'Oldham', 'Woking', 'Cheltenham', 'Chelmsford', 'Saint Helens', 'Basildon', 'Gillingham', 'Worcester', 'Worthing', 'Rochdale', 'Basingstoke', 'Solihull', 'Harlow', 'Bath', 'Southport', 'Maidstone', 'Lincoln', 'Hastings', 'Darlington', 'Londonderry County Borough', 'Harrogate', 'Hartlepool', 'Bedford', 'Hemel Hempstead', 'Stevenage', 'Saint Albans', 'South Shields', 'Weston-super-Mare', 'Halifax', 'Birkenhead', 'Chester', 'Warrington', 'Wigan', 'High Wycombe', 'Stockton-on-Tees', 'Wakefield', 'Gateshead', 'Lisburn', 'Reigate', 'Chatham', 'Bury', 'Royal Tunbridge Wells', 'Runcorn', 'Bognor Regis', 'Bracknell', 'Saint Helier', 'Aylesbury', 'East Kilbride', 'Acton', 'Farnborough'],
    'United States': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'San Francisco', 'Charlotte', 'Indianapolis', 'Seattle', 'Denver', 'Washington', 'Boston', 'El Paso', 'Nashville', 'Detroit', 'Oklahoma City', 'Portland', 'Las Vegas', 'Memphis', 'Louisville', 'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Mesa', 'Kansas City', 'Atlanta', 'Long Beach', 'Omaha', 'Raleigh', 'Colorado Springs', 'Miami', 'Virginia Beach', 'Oakland', 'Minneapolis', 'Tulsa', 'Arlington', 'New Orleans', 'Wichita'],
    'Uruguay': ['Montevideo', 'Salto', 'Paysandu', 'Las Piedras'],
    'Uzbekistan': ['Tashkent', 'Namangan', 'Samarkand', 'Andijan', 'Nukus'],
    'Venezuela': ['Caracas', 'Maracaibo', 'Maracay', 'Valencia', 'Puerto La Cruz', 'Petare'],
    'Vietnam': ['Ho Chi Minh City', 'Hanoi', 'Haiphong', 'Da Nang', 'Bien Hoa', 'Hue', 'Nha Trang', 'Can Tho', 'Rach Gia', 'Quy Nhon'],
    'Yemen': ['Sanaa', 'Al Hudaydah'],
    'Zambia': ['Lusaka', 'Kitwe', 'Ndola'],
    'Zimbabwe': ['Harare', 'Bulawayo', 'Chitungwiza', 'Mutare', 'Epworth', 'Gweru']
}

common_baby_names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte',
                    'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Mila', 'Ella', 'Avery', 'Sofia',
                    'Camila', 'Aria', 'Scarlett', 'Victoria', 'Madison', 'Luna', 'Grace', 'Chloe', 'Penelope', 'Lily',
                    'Zoey', 'Riley', 'Nora', 'Aubrey', 'Hannah', 'Layla', 'Lillian', 'Addison', 'Eleanor', 'Natalie',
                    'Zoe', 'Stella', 'Hazel', 'Ellie', 'Paisley', 'Audrey', 'Skylar', 'Violet', 'Claire', 'Bella',
                    'Aurora', 'Lucy', 'Anna', 'Savannah', 'Maya', 'Genesis', 'Naomi', 'Valentina', 'Nova', 'Ruby',
                    'Eva', 'Alice', 'Lucia', 'Isabelle', 'Rose', 'Alyssa', 'Lyla', 'Ariana', 'Adeline', 'Mackenzie',
                    'Kylie', 'Gabriella', 'Autumn', 'Piper', 'Serenity', 'Allison', 'Arianna', 'Sarah', 'Taylor',
                    'Eliana', 'Maria', 'Gianna', 'Willow', 'Cora', 'Katherine', 'Emery', 'Adalynn', 'Kaylee', 'Brielle',
                    'Faith', 'Leah', 'Annabelle', 'Alexa', 'Madeline', 'Aubree', 'Jocelyn', 'Aaliyah', 'Londyn',
                    'Morgan', 'Harmony', 'Melanie', 'Diana', 'Liliana', 'Makayla', 'Laila', 'Daniela', 'Jade', 'Adalyn',
                    'Ashley', 'Alexandra', 'Amina', 'Elise', 'Jasmine', 'Amara', 'Daisy', 'Kimberly', 'Valerie',
                    'Melody', 'Alina', 'Ariella', 'Molly', 'Amanda', 'Sage', 'Kinsley', 'Lia', 'Nicole', 'Zara',
                    'Brooke', 'Noelle', 'Sara', 'Elliana', 'Skyler', 'Danielle', 'Mckenzie', 'Nadia', 'Hope', 'Erin',
                    'Nina', 'Raegan', 'Daniella', 'Jordyn', 'Maddison', 'Jennifer', 'Gracie', 'Keira', 'Harley',
                    'Amy', 'Kaitlyn', 'Camilla', 'Lena', 'Lucille', 'Eliza', 'Kate', 'Isabel', 'Summer', 'Maggie',
                    'Hayden', 'Makenzie', 'Amiyah', 'Kennedy', 'Miranda', 'Catherine', 'Paris', 'Sienna', 'Lilliana',
                    'Joanna', 'Dream', 'Rory', 'Arielle', 'Liana']

common_last_names = ['Adams', 'Aguilar', 'Aguirre', 'Aksornvithayakul', 'Alatorre', 'Alexander', 'Allen', 'Alvarez',
                    'Anderson', 'Andersson', 'Andrade', 'Andreev', 'Baek', 'Bailey', 'Baker', 'Barajas', 'Barnes',
                    'Barrios', 'Bauer', 'Becker', 'Bell', 'Beltran', 'Bengtsson', 'Benitez', 'Bennett', 'Berg',
                    'Bermudez', 'Black', 'Bogdanov', 'Boonkum', 'Boyd', 'Brooks', 'Brown', 'Bryant', 'Burns', 'Bustos',
                    'Butler', 'Cabello', 'Cabrera', 'Calderon', 'Campbell', 'Campos', 'Carrillo', 'Carter', 'Castillo',
                    'Castro', 'Cavazos', 'Cedillo', 'Cervantes', 'Chaiyachet', 'Chaiyaporn', 'Chalermphong',
                    'Chantanapong', 'Chantanapongwanit', 'Chavez', 'Chen', 'Chirathivat', 'Cho', 'Choi',
                    'Choothamanivong', 'Chotanaphan', 'Cisneros', 'Clark', 'Cole', 'Coleman', 'Collins', 'Contreras',
                    'Cook', 'Cooper', 'Cordova', 'Coronado', 'Cortez', 'Cox', 'Crawford', 'Cruz', 'Daniels', 'Davis',
                    'Delgado', 'Deng', 'Diaz', 'Dixon', 'Duarte', 'Dunn', 'Dąbrowski', 'Edwards', 'Egorov', 'Ellis',
                    'Eriksson', 'Espinosa', 'Espinoza', 'Esquivel', 'Estrada', 'Evans', 'Ferguson', 'Fernandez',
                    'Figueroa', 'Fischer', 'Fisher', 'Flores', 'Ford', 'Foster', 'Freeman', 'Fuentes', 'Galindo',
                    'Gallardo', 'Gao', 'Garcia', 'Gibson', 'Gomez', 'Gonzalez', 'Gordon', 'Grabowski', 'Graham',
                    'Granados', 'Grant', 'Gray', 'Green', 'Griffin', 'Guerra', 'Guerrero', 'Guo', 'Gustafsson',
                    'Gutierrez', 'Guzman', 'Hall', 'Hamilton', 'Han', 'Hansson', 'Harris', 'Harrison', 'Hartmann',
                    'Hawkins', 'Hayashi', 'Hayes', 'He', 'Henderson', 'Henry', 'Hernandez', 'Herrera', 'Hicks',
                    'Hidalgo', 'Hill', 'Hoffmann', 'Holmes', 'Howard', 'Hu', 'Huang', 'Hughes', 'Hunt', 'Hunter',
                    'Hurtado', 'Hwang', 'Ibarra', 'Inoue', 'Ito', 'Ivanov', 'Jackson', 'James', 'Jang', 'Jankowski',
                    'Jansson', 'Jaramillo', 'Jareonvithayakul', 'Jenkins', 'Jeong', 'Jimenez', 'Johansson', 'Johnson',
                    'Jones', 'Jonsson', 'Jordan', 'Kaczmarek', 'Kamiński', 'Kang', 'Karlsson', 'Karpov', 'Kato', 'Kelly',
                    'Kennedy', 'Kim', 'Kimura', 'King', 'Klein', 'Knight', 'Ko', 'Kobayashi', 'Koch', 'Kowalczyk',
                    'Kowalski', 'Kozlov', 'Kozłowski', 'Krause', 'Krawczyk', 'Kuznetsov', 'Kwiatkowski', 'Kwon', 'Lara',
                    'Larsson', 'Lebedev', 'Lee', 'Leon', 'Lewis', 'Li', 'Lim', 'Lin', 'Lindberg', 'Lira', 'Liu', 'Loera',
                    'Lomeli', 'Long', 'Lopez', 'Luna', 'Lundberg', 'Ma', 'Madrigal', 'Magana', 'Maldonado', 'Marshall',
                    'Martin', 'Martinez', 'Mason', 'Matsumoto', 'Mattsson', 'Mazur', 'McDonald', 'Medina', 'Medrano',
                    'Mejia', 'Melendez', 'Mendez', 'Mendoza', 'Mikhailov', 'Miller', 'Mills', 'Miramontes', 'Miranda',
                    'Mireles', 'Mitchell', 'Molina', 'Montes', 'Montoya', 'Moore', 'Morales', 'Moreno', 'Morgan',
                    'Morozov', 'Morris', 'Munoz', 'Murphy', 'Murray', 'Myers', 'Müller', 'Nakamura', 'Narongdej',
                    'Navarro', 'Nelson', 'Neumann', 'Nichols', 'Nikolaev', 'Nilsson', 'Nim-anong', 'Novikov', 'Nowak',
                    'Nowakowski', 'Nunez', 'Ochoa', 'Oh', 'Olivares', 'Olivarez', 'Olofsson', 'Olsson', 'Orlov', 'Ortiz',
                    'Owens', 'Pacheco', 'Palacios', 'Palmer', 'Park', 'Parker', 'Patterson', 'Pawłowski', 'Pena', 'Perez',
                    'Perkins', 'Perry', 'Persson', 'Peterson', 'Petrov', 'Pettersson', 'Phillips', 'Phrommala', 'Pineda',
                    'Piotrowski', 'Pizarro', 'Popov', 'Porter', 'Powell', 'Price', 'Quinones', 'Quintero', 'Ramirez',
                    'Ramos', 'Rangel', 'Rattanapong', 'Reed', 'Reyes', 'Reyna', 'Reynolds', 'Rice', 'Richardson',
                    'Richter', 'Rincon', 'Rios', 'Rivera', 'Roberts', 'Robertson', 'Robinson', 'Rocha', 'Rodriguez',
                    'Rogers', 'Rojas', 'Rosales', 'Rose', 'Ross', 'Ruiz', 'Russell', 'Ryu', 'Saldana', 'Salgado',
                    'Sanchez', 'Sanders', 'Sandoval', 'Santana', 'Santillan', 'Santos', 'Sasaki', 'Sato', 'Saucedo',
                    'Schmid', 'Schmidt', 'Schneider', 'Schubert', 'Schulz', 'Schumacher', 'Scott', 'Segura', 'Sepulveda',
                    'Serrano', 'Shaw', 'Shibata', 'Shimizu', 'Shin', 'Silva', 'Simmons', 'Simpson', 'Smirnov', 'Smith',
                    'Sokolov', 'Solis', 'Song', 'Sonthichai', 'Soto', 'Sriporn', 'Stepanov', 'Stevens', 'Stewart', 'Stone',
                    'Sukchareon', 'Sullivan', 'Sun', 'Sustaita', 'Suzuki', 'Svensson', 'Szymański', 'Takahashi', 'Tamez',
                    'Tanaka', 'Taylor', 'Thomas', 'Thompson', 'Thongchareon', 'Thongkam', 'Torres', 'Tovar', 'Trevino',
                    'Trujillo', 'Tucker', 'Turner', 'Valdez', 'Valencia', 'Valenzuela', 'Valle', 'Varela', 'Vargas',
                    'Vasquez', 'Velasquez', 'Vergara', 'Villa', 'Villalobos', 'Villanueva', 'Villareal', 'Villegas',
                    'Volkov', 'Wagner', 'Walker', 'Wallace', 'Wang', 'Ward', 'Warren', 'Washington', 'Watanabe', 'Watson',
                    'Webb', 'Weber', 'Wells', 'West', 'White', 'Williams', 'Wilson', 'Wiśniewski', 'Wojciechowski', 'Wood',
                    'Woods', 'Wright', 'Wu', 'Wójcik', 'Xu', 'Yamada', 'Yamaguchi', 'Yamamoto', 'Yang', 'Yoo', 'Yoon',
                    'Yoshida', 'Young', 'Zaitsev', 'Zamora', 'Zavala', 'Zhang', 'Zhao', 'Zhou', 'Zieliński']

common_adjectives_for_people = ['adaptable', 'adventurous', 'aloof', 'ambitious', 'anti-social', 'anxious', 'apathetic',
                                'arrogant', 'attentive', 'blunt', 'boring', 'calm', 'caring', 'cautious', 'charismatic',
                                'cheerful', 'clever', 'closed-minded', 'compassionate', 'confident', 'conventional',
                                'cooperative', 'courageous', 'courteous', 'cowardly', 'creative', 'cruel', 'curious',
                                'daring', 'deceitful', 'dependent', 'depressed', 'determined', 'diligent', 'dishonest',
                                'disloyal', 'disrespectful', 'distracted', 'distrustful', 'eager', 'egotistical',
                                'eloquent', 'empathetic', 'energetic', 'enthusiastic', 'fake', 'foolish', 'forgetful',
                                'fragile', 'friendly', 'generous', 'gentle', 'genuine', 'gloomy', 'grateful', 'greedy',
                                'gregarious', 'harsh', 'helpful', 'helpless', 'honest', 'hostile', 'humble', 'idealistic',
                                'immature', 'impatient', 'inarticulate', 'inconsiderate', 'indecisive', 'independent',
                                'indifferent', 'innovative', 'insecure', 'insensitive', 'intolerant', 'introverted',
                                'irrational', 'irresponsible', 'kind', 'lazy', 'lethargic', 'lively', 'loyal', 'mature',
                                'modest', 'negative', 'neglectful', 'negligent', 'nervous', 'observant', 'obstinate',
                                'open-minded', 'optimistic', 'outgoing', 'passionate', 'patient', 'pessimistic', 'polite',
                                'positive', 'practical', 'reckless', 'reliable', 'reserved', 'resilient', 'resourceful',
                                'respectful', 'responsible', 'rough', 'rude', 'self-motivated', 'selfish', 'sensible',
                                'sensitive', 'shy', 'simple-minded', 'sincere', 'sluggish', 'sociable', 'stubborn',
                                'sympathetic', 'tactful', 'talented', 'thoughtful', 'timid', 'tolerant', 'treacherous',
                                'trustworthy', 'unfeeling', 'ungrateful', 'unhelpful', 'unimaginative', 'unobservant',
                                'unreliable', 'unsympathetic', 'untalented', 'vain', 'wise']

common_email_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com", "icloud.com", "protonmail.com",
                        "yandex.com", "zoho.com", "mail.com", "gmx.com", "inbox.com", "mail.ru", "qq.com", "163.com",
                        "126.com", "sina.com", "outlook.jp", "naver.com", "daum.net", "naver.jp", "rocketmail.com",
                        "live.com", "me.com", "fastmail.com", "disposable.com", "apple.com", "msn.com", "earthlink.net"]

adjectives_for_places = ['ancient', 'beautiful', 'bohemian', 'breathtaking', 'buzzing', 'captivating', 'charming',
                        'coastal', 'colorful', 'compact', 'cosmopolitan', 'cozy', 'crowded', 'cultural', 'deserted',
                        'enchanting', 'exotic', 'flat', 'foggy', 'green', 'happening', 'hidden', 'hilly', 'historic',
                        'idyllic', 'industrial', 'lakefront', 'lively', 'lush', 'majestic', 'modern', 'mountainous',
                        'peaceful', 'picturesque', 'pristine', 'quaint', 'quiescent', 'rainy', 'remote', 'riverfront',
                        'romantic', 'rural', 'scenic', 'secluded', 'serene', 'snowy', 'sprawling', 'stunning', 'sunny',
                        'touristy', 'tranquil', 'unspoiled', 'up-and-coming', 'urban', 'vibrant', 'vintage', 'windy']

# unique_names = []
# repeated_names = []

# for name in adjectives_for_places:
#     if name not in unique_names:
#         unique_names.append(name)
#     else:
#         repeated_names.append(name)

# unique_names.sort()

# print([name.lower() for name in unique_names])
# print()
# print(repeated_names)