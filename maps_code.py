import urllib.request, json


def show_trip():
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?' #This is where the request goes
    api_key = 'AIzaSyBNq9gXinD2pLsoUmXVo5uWLllGj-BdvYc'
    #Asks the user to input Where they are and where they want to go.
    origin = input('What is your location?: ').replace(' ','+')
    destination = input('Where do you wish to go?: ').replace(' ','+')
    mode = input('What is your preferred travel method?')
    #Build the URL for the request
    navigate =  'origin={}&destination={}&mode{}&key={}'.format(origin,destination,mode,api_key)
    request = endpoint + navigate
    #Send the request and get the response
    response = urllib.request.urlopen(request).read()
    #Load response as JSON
    directions = json.loads(response)
    #print(directions)
    directions.keys()
    routes = directions['routes']
    routes[0].keys()
    legs = routes[0]['legs']

    
    for i in range (0, len (directions['routes'][0]['legs'][0]['steps'])):
        dist = directions['routes'][0]['legs'][0]['steps'][i]['distance']['text']
        j =directions['routes'][0]['legs'][0]['steps'][i]['html_instructions'] 
        print("In",dist, j)
        time= directions['routes'][0]['legs'][0]['steps'][i]['duration']
        print("This should take you:",time )

show_trip()
