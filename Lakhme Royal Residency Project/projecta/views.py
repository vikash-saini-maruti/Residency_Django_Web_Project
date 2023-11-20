from django.http import HttpResponse
from django.shortcuts import render


def contacts(request):
    return HttpResponse("Please contact us on 1800-xxxx-xxxx")

def home(request):
    return render(request,'home.html')

def achievements(request):
    return render(request,'achievements.html')

def name(request,name):
    return HttpResponse(name)

# def locationolder(request):
#     data ={
#         'locations':  [
        
#     "New York City, USA",
#     "Tokyo, Japan",
#     "London, United Kingdom",
#     "Shanghai, China",
#     "Beijing, China",
#     "Hong Kong, SAR",
#     "Singapore",
#     "San Francisco, USA",
#     "Los Angeles, USA",
#     "Chicago, USA",
#     "Dubai, United Arab Emirates",
#     "Riyadh, Saudi Arabia",
#     "Paris, France",
#     "Mumbai, India",
#     "Sydney, Australia",
#     "Toronto, Canada",
#     "Moscow, Russia",
#     "Seoul, South Korea",
#     "Zurich, Switzerland",
#     "Geneva, Switzerland",
#     "Oslo, Norway",
#     "Copenhagen, Denmark",
#     "Stockholm, Sweden",
#     "Amsterdam, Netherlands",
#     "Brussels, Belgium",
#     "Luxembourg City, Luxembourg",
#     "Abu Dhabi, United Arab Emirates",
#     "Doha, Qatar",
#     "Frankfurt, Germany",
#     "Munich, Germany",
#     "Hamburg, Germany",
#     "Istanbul, Turkey",
#     "Sao Paulo, Brazil",
#     "Rio de Janeiro, Brazil",
#     "Buenos Aires, Argentina",
#     "Vancouver, Canada",
#     "Melbourne, Australia",
#     "Auckland, New Zealand",
#     "San Jose, USA",
#     "Boston, USA",
#     "Seattle, USA",
#     "Washington, D.C., USA",
#     "Houston, USA",
#     "Dallas, USA",
#     "Atlanta, USA",
#     "Miami, USA",
#     "Stockholm, Sweden",
#     "Seoul, South Korea",
#     "Kuala Lumpur, Malaysia"
# ]}

#     return render(request,'ourlocations.html', data)

# def clientsolder(request):
#     clientdata= {
#             'clients' : [
#         "Apple Inc.",
#         "Microsoft Corporation",
#         "Amazon.com Inc.",
#         "Alphabet Inc. (Google)",
#         "Facebook Inc.",
#         "Tesla Inc.",
#         "Berkshire Hathaway Inc.",
#         "JPMorgan Chase & Co.",
#         "Johnson & Johnson",
#         "Walmart Inc.",
#         "Visa Inc.",
#         "Procter & Gamble Co.",
#         "Mastercard Inc.",
#         "Intel Corporation",
#         "Cisco Systems Inc.",
#         "Verizon Communications Inc.",
#         "AT&T Inc.",
#         "Walt Disney Co.",
#         "Netflix Inc.",
#         "Goldman Sachs Group Inc."

#             ]
#     }
#     return render(request,'ourclients.html',clientdata)


# def managementolder(request):
#     managementdata={
#         'table_data':[

#         {
#             'Name': 'John Doe',
#             'Contacs': '+1-123-456-789',
#             'Department': 'Human Resources'
#         },
#         {
#             'Name': 'Jane Smith',
#             'Contacs': '+1-234-567-8900',
#             'Department': 'Finance'
#         },
#         {
#             'Name': 'Michael Johnson',
#             'Contacs': '+1-345-678-9001',
#             'Department': 'Operations'
#         },
#         {
#             'Name': 'Sarah Williams',
#             'Contacs': '+1-456-789-0012',
#             'Department': 'Marketing'
#         },
#         {
#             'Name': 'David Lee',
#             'Contacs': '+1-567-8900-123',
#             'Department': 'IT'
#         },
#         {
#             'Name': 'Emily Brown',
#             'Contacs': '+1-678-9001-234',
#             'Department': 'Sales'
#         },
#         {
#             'Name': 'Robert Davis',
#             'Contacs': '+1-789-0012-345',
#             'Department': 'Legal'
#         },
#         {
#             'Name': 'Laura White',
#             'Contacs': '+1-8900-123-456',
#             'Department': 'Human Resources'
#         },
#         {
#             'Name': 'Daniel Green',
#             'Contacs': '+1-9001-234-567',
#             'Department': 'Finance'
#         },
#         {
#             'Name': 'Olivia Johnson',
#             'Contacs': '+1-0012-345-678',
#             'Department': 'Operations'
#         },
#         {
#             'Name': 'Matthew Turner',
#             'Contacs': '+1-123-456-789',
#             'Department': 'Marketing'
#         },
#         {
#             'Name': 'Sophia Hall',
#             'Contacs': '+1-234-567-8900',
#             'Department': 'IT'
#         },
#         {
#             'Name': 'William Clark',
#             'Contacs': '+1-345-678-9001',
#             'Department': 'Sales'
#         },
#         {
#             'Name': 'Ava Lewis',
#             'Contacs': '+1-456-789-0012',
#             'Department': 'Legal'
#         },
#         {
#             'Name': 'Ethan Adams',
#             'Contacs': '+1-567-8900-123',
#             'Department': 'Human Resources'
#         },
#         {
#             'Name': 'Emma Baker',
#             'Contacs': '+1-678-9001-234',
#             'Department': 'Finance'
#         },
#         {
#             'Name': 'Liam Turner',
#             'Contacs': '+1-789-0012-345',
#             'Department': 'Operations'
#         },
#         {
#             'Name': 'Olivia King',
#             'Contacs': '+1-8900-123-456',
#             'Department': 'Marketing'
#         },
#         {
#             'Name': 'Noah Martin',
#             'Contacs': '+1-9001-234-567',
#             'Department': 'IT'
#         }

#         ]
#     }
#     return render(request,'management.html',managementdata)

def vote(request,ans):
    return render(request,'vote.html',ans)


# def filter1older(request):
#     filter1data={
#         'filter1table' : [
#         {
#             'Name': 'Sunny Beach Resort',
#             'Location': 'Beach Town',
#             'Contacts': '+1-123-456-789',
#             'Price': 12000
#         },
#         {
#             'Name': 'Mountain Retreat Lodge',
#             'Location': 'Mountain Village',
#             'Contacts': '+1-987-654-321',
#             'Price': 15500
#         },
#         {
#             'Name': 'Cityscape Hotel',
#             'Location': 'Downtown City',
#             'Contacts': '+1-555-123-456',
#             'Price': 10080
#         },
#         {
#             'Name': 'Oceanfront Paradise Resort',
#             'Location': 'Seaside City',
#             'Contacts': '+1-888-555-789',
#             'Price': 14200
#         },
#         {
#             'Name': 'Lakeside Inn',
#             'Location': 'Lakeside Retreat',
#             'Contacts': '+1-777-999-333',
#             'Price': 11750
#         },
#         {
#             'Name': 'Desert Oasis Hotel',
#             'Location': 'Desert Oasis',
#             'Contacts': '+1-456-789-0012',
#             'Price': 13900
#         },
#         {
#             'Name': 'Alpine Lodge & Spa',
#             'Location': 'Mountain Retreat',
#             'Contacts': '+1-321-987-654',
#             'Price': 16500
#         },
#         {
#             'Name': 'Luxury Heights Tower',
#             'Location': 'Metropolitan City',
#             'Contacts': '+1-555-555-555',
#             'Price': 18000
#         },
#         {
#             'Name': 'Riverside Mansion',
#             'Location': 'Riverside Estates',
#             'Contacts': '+1-999-888-777',
#             'Price': 20050
#         },
#         {
#             'Name': 'Tropical Hideaway Resort',
#             'Location': 'Tropical Paradise',
#             'Contacts': '+1-444-444-444',
#             'Price': 12800
#         },
#         {
#             'Name': 'Historical Elegance Inn',
#             'Location': 'Historic District',
#             'Contacts': '+1-333-333-333',
#             'Price': 17300
#         },
#         {
#             'Name': 'Urban Chic Boutique Hotel',
#             'Location': 'Downtown Trendy',
#             'Contacts': '+1-222-222-222',
#             'Price': 11200
#         },
#         {
#             'Name': 'Coastal Haven Villa',
#             'Location': 'Coastal Retreat',
#             'Contacts': '+1-111-111-111',
#             'Price': 19500
#         },
#         {
#             'Name': 'Skyline View Suites',
#             'Location': 'City Skyline',
#             'Contacts': '+1-666-777-888',
#             'Price': 14900
#         },
#         {
#             'Name': 'Wilderness Campsite',
#             'Location': 'Nature Reserve',
#             'Contacts': '+1-999-111-222',
#             'Price': 100200
#         },
#         {
#             'Name': 'Lakeside Cabin Retreat',
#             'Location': 'Lakeside Getaway',
#             'Contacts': '+1-123-987-456',
#             'Price': 130000
#         },
#         {
#             'Name': 'Royal Palace Hotel',
#             'Location': 'Palace District',
#             'Contacts': '+1-777-777-777',
#             'Price': 220000
#         },
#         {
#             'Name': 'Paradise Island Resort',
#             'Location': 'Island Paradise',
#             'Contacts': '+1-888-999-666',
#             'Price': 23500
#         },
#         {
#             'Name': 'Tranquil Garden Retreat',
#             'Location': 'Garden Oasis',
#             'Contacts': '+1-123-555-789',
#             'Price': 12500
#         },
#         {
#             'Name': 'Charming Cottage Inn',
#             'Location': 'Countryside Charm',
#             'Contacts': '+1-456-123-789',
#             'Price': 100500
#         }

#         ]
#     }
#     return render(request,'filter1.html',filter1data)

def gallary(request):
    return render(request,'gallery.html')


def userform(request):
    try:
        nameget=request.GET['name']
        print(nameget)
    except:
        pass
    return render(request,'userform.html')


def locdemo2(request):
    data ={
        'title' : " Our Locations ",
        'locations':  [
    "location"    
    "New York City, USA",
    "Tokyo, Japan",
    "London, United Kingdom",
    "Shanghai, China",
    "Beijing, China",
    "Hong Kong, SAR",
    "Singapore",
    "San Francisco, USA",
    "Los Angeles, USA",
    "Chicago, USA",
    "Dubai, United Arab Emirates",
    "Riyadh, Saudi Arabia",
    "Paris, France",
    "Mumbai, India",
    "Sydney, Australia",
    "Toronto, Canada",
    "Moscow, Russia",
    "Seoul, South Korea",
    "Zurich, Switzerland",
    "Geneva, Switzerland",
    "Oslo, Norway",
    "Copenhagen, Denmark",
    "Stockholm, Sweden",
    "Amsterdam, Netherlands",
    "Brussels, Belgium",
    "Luxembourg City, Luxembourg",
    "Abu Dhabi, United Arab Emirates",
    "Doha, Qatar",
    "Frankfurt, Germany",
    "Munich, Germany",
    "Hamburg, Germany",
    "Istanbul, Turkey",
    "Sao Paulo, Brazil",
    "Rio de Janeiro, Brazil",
    "Buenos Aires, Argentina",
    "Vancouver, Canada",
    "Melbourne, Australia",
    "Auckland, New Zealand",
    "San Jose, USA",
    "Boston, USA",
    "Seattle, USA",
    "Washington, D.C., USA",
    "Houston, USA",
    "Dallas, USA",
    "Atlanta, USA",
    "Miami, USA",
    "Stockholm, Sweden",
    "Seoul, South Korea",
    "Kuala Lumpur, Malaysia"
]}
    return render(request,'locdemo.html', data)




def location(request):
    data={
        'title' : " Our Worldwide Reach ",
        'cola' : 'City',
        'colb' : 'Country',
        'table_data':[

        {'a': 'New York a', 'b': 'USA'},
        {'a': 'Tokyo', 'b': 'Japan'},
        {'a': 'London', 'b': 'United Kingdom'},
        {'a': 'Shanghai', 'b': 'China'},
        {'a': 'Beijing', 'b': 'China'},
        {'a': 'Hong Kong', 'b': 'SAR'},
        {'a': 'Singapore', 'b': 'Singapore'},
        {'a': 'San Francisco', 'b': 'USA'},
        {'a': 'Los Angeles', 'b': 'USA'},
        {'a': 'Chicago', 'b': 'USA'},
        {'a': 'Dubai', 'b': 'United Arab Emirates'},
        {'a': 'Riyadh', 'b': 'Saudi Arabia'},
        {'a': 'Paris', 'b': 'France'},
        {'a': 'Mumbai', 'b': 'India'},
        {'a': 'Sydney', 'b': 'Australia'},
        {'a': 'Toronto', 'b': 'Canada'},
        {'a': 'Moscow', 'b': 'Russia'},
        {'a': 'Seoul', 'b': 'South Korea'},
        {'a': 'Zurich', 'b': 'Switzerland'},
        {'a': 'Geneva', 'b': 'Switzerland'},
        {'a': 'Oslo', 'b': 'Norway'},
        {'a': 'Copenhagen', 'b': 'Denmark'},
        {'a': 'Stockholm', 'b': 'Sweden'},
        {'a': 'Amsterdam', 'b': 'Netherlands'},
        {'a': 'Brussels', 'b': 'Belgium'},
        {'a': 'Luxembourg a', 'b': 'Luxembourg'},
        {'a': 'Abu Dhabi', 'b': 'United Arab Emirates'},
        {'a': 'Doha', 'b': 'Qatar'},
        {'a': 'Frankfurt', 'b': 'Germany'},
        {'a': 'Munich', 'b': 'Germany'},
        {'a': 'Hamburg', 'b': 'Germany'},
        {'a': 'Istanbul', 'b': 'Turkey'},
        {'a': 'Sao Paulo', 'b': 'Brazil'},
        {'a': 'Rio de Janeiro', 'b': 'Brazil'},
        {'a': 'Buenos Aires', 'b': 'Argentina'},
        {'a': 'Vancouver', 'b': 'Canada'},
        {'a': 'Melbourne', 'b': 'Australia'},
        {'a': 'Auckland', 'b': 'New Zealand'},
        {'a': 'San Jose', 'b': 'USA'},
        {'a': 'Boston', 'b': 'USA'},
        {'a': 'Seattle', 'b': 'USA'},
        {'a': 'Washington', 'b': 'D.C.'},
        {'a': 'Houston', 'b': 'USA'},
        {'a': 'Dallas', 'b': 'USA'},
        {'a': 'Atlanta', 'b': 'USA'},
        {'a': 'Miami', 'b': 'USA'},
        {'a': 'Stockholm', 'b': 'Sweden'},
        {'a': 'Seoul', 'b': 'South Korea'},
        {'a': 'Kuala Lumpur', 'b': 'Malaysia'},


        ]
    }
    return render(request,'locdemo.html',data)


def management(request):
    data={
        'title': " Our MANAGEMENT ",
        'cola' : 'Name',
        'colb' : 'Contacts',
        'colc' : 'Department',
        'table_data':[

        {
            
			'a': 'Robert Davis',
            'b': '+1-123-456-789',
            'c': 'Human Resources'
        },
        {
            'a': 'Jane Smith',
            'b': '+1-234-567-8900',
            'c': 'Finance'
        },
        {
            'a': 'Michael Johnson',
            'b': '+1-345-678-9001',
            'c': 'Operations'
        },
        {
            'a': 'Sarah Williams',
            'b': '+1-456-789-0012',
            'c': 'Marketing'
        },
        {
            'a': 'David Lee',
            'b': '+1-567-8900-123',
            'c': 'IT'
        },
        {
            'a': 'Emily Brown',
            'b': '+1-678-9001-234',
            'c': 'Sales'
        },
        {
            'a': 'Robert Davis',
            'b': '+1-789-0012-345',
            'c': 'Legal'
        },
        {
            'a': 'Laura White',
            'b': '+1-8900-123-456',
            'c': 'Human Resources'
        },
        {
            'a': 'Daniel Green',
            'b': '+1-9001-234-567',
            'c': 'Finance'
        },
        {
            'a': 'Olivia Johnson',
            'b': '+1-0012-345-678',
            'c': 'Operations'
        },
        {
            'a': 'Matthew Turner',
            'b': '+1-123-456-789',
            'c': 'Marketing'
        },
        {
            'a': 'Sophia Hall',
            'b': '+1-234-567-8900',
            'c': 'IT'
        },
        {
            'a': 'William Clark',
            'b': '+1-345-678-9001',
            'c': 'Sales'
        },
        {
            'a': 'Ava Lewis',
            'b': '+1-456-789-0012',
            'c': 'Legal'
        },
        {
            'a': 'Ethan Adams',
            'b': '+1-567-8900-123',
            'c': 'Human Resources'
        },
        {
            'a': 'Emma Baker',
            'b': '+1-678-9001-234',
            'c': 'Finance'
        },
        {
            'a': 'Liam Turner',
            'b': '+1-789-0012-345',
            'c': 'Operations'
        },
        {
            'a': 'Olivia King',
            'b': '+1-8900-123-456',
            'c': 'Marketing'
        },
        {
            'a': 'Noah Martin',
            'b': '+1-9001-234-567',
            'c': 'IT'
        }

        ]
    }
    return render(request,'locdemo.html',data)

def Resorts(request):
    data={
        'title' : " Our Global Resorts ",
        'cola' : 'Resort Name',
        'colb' : 'Resort Type',
        'colc' : 'Contacts',
        'cold' : 'Price (INR )',
        'table_data':[
        {
            'a': 'Sunny Beach Resort',
            'b': 'Beach Town',
            'c': '+1-123-456-789',
            'd': 12000
        },
        {
            'a': 'Mountain Retreat Lodge',
            'b': 'Mountain Village',
            'c': '+1-987-654-321',
            'd': 15500
        },
        {
            'a': 'Cityscape Hotel',
            'b': 'Downtown City',
            'c': '+1-555-123-456',
            'd': 10080
        },
        {
            'a': 'Oceanfront Paradise Resort',
            'b': 'Seaside City',
            'c': '+1-888-555-789',
            'd': 14200
        },
        {
            'a': 'Lakeside Inn',
            'b': 'Lakeside Retreat',
            'c': '+1-777-999-333',
            'd': 11750
        },
        {
            'a': 'Desert Oasis Hotel',
            'b': 'Desert Oasis',
            'c': '+1-456-789-0012',
            'd': 13900
        },
        {
            'a': 'Alpine Lodge & Spa',
            'b': 'Mountain Retreat',
            'c': '+1-321-987-654',
            'd': 16500
        },
        {
            'a': 'Luxury Heights Tower',
            'b': 'Metropolitan City',
            'c': '+1-555-555-555',
            'd': 18000
        },
        {
            'a': 'Riverside Mansion',
            'b': 'Riverside Estates',
            'c': '+1-999-888-777',
            'd': 20050
        },
        {
            'a': 'Tropical Hideaway Resort',
            'b': 'Tropical Paradise',
            'c': '+1-444-444-444',
            'd': 12800
        },
        {
            'a': 'Historical Elegance Inn',
            'b': 'Historic District',
            'c': '+1-333-333-333',
            'd': 17300
        },
        {
            'a': 'Urban Chic Boutique Hotel',
            'b': 'Downtown Trendy',
            'c': '+1-222-222-222',
            'd': 11200
        },
        {
            'a': 'Coastal Haven Villa',
            'b': 'Coastal Retreat',
            'c': '+1-111-111-111',
            'd': 19500
        },
        {
            'a': 'Skyline View Suites',
            'b': 'City Skyline',
            'c': '+1-666-777-888',
            'd': 14900
        },
        {
            'a': 'Wilderness Campsite',
            'b': 'Nature Reserve',
            'c': '+1-999-111-222',
            'd': 100200
        },
        {
            'a': 'Lakeside Cabin Retreat',
            'b': 'Lakeside Getaway',
            'c': '+1-123-987-456',
            'd': 130000
        },
        {
            'a': 'Royal Palace Hotel',
            'b': 'Palace District',
            'c': '+1-777-777-777',
            'd': 220000
        },
        {
            'a': 'Paradise Island Resort',
            'b': 'Island Paradise',
            'c': '+1-888-999-666',
            'd': 23500
        },
        {
            'a': 'Tranquil Garden Retreat',
            'b': 'Garden Oasis',
            'c': '+1-123-555-789',
            'd': 12500
        },
        {
            'a': 'Charming Cottage Inn',
            'b': 'Countryside Charm',
            'c': '+1-456-123-789',
            'd': 100500
        }

        ]
    }
    return render(request,'locdemo.html',data)

def clients(request):
    
    data= {
        'title' : " Our Worldwide Clients ",
        'cola' : 'Clients',
        'table_data':[
            
        { "a": "Microsoft Corporation",	},
        { "a": "Amazon.com Inc.",	},
        { "a": "Alphabet Inc. (Google)",	},
        { "a": "Facebook Inc.",	},
        { "a": "Tesla Inc.",	},
        { "a": "Berkshire Hathaway Inc.",	},
        { "a": "JPMorgan Chase & Co.",	},
        { "a": "Johnson & Johnson",	},
        { "a": "Walmart Inc.",	},
        { "a": "Visa Inc.",	},
        { "a": "Procter & Gamble Co.",	},
        { "a": "Mastercard Inc.",	},
        { "a": "Intel Corporation",	},
        { "a": "Cisco Systems Inc.",	},
        { "a": "Verizon Communications Inc.",	},
        { "a": "AT&T Inc.",	},
        { "a": "Walt Disney Co.",	},
        { "a": "Netflix Inc.",	},
        { "a": "Goldman Sachs Group Inc."	},

        ]
    }
    return render(request,'locdemo.html',data)