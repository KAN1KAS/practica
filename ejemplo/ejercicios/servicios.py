import requests

def solicitar():
    response = requests.get('https://reqres.in/api/users')
    if response.status_code==200:
        respuesta = response.json()
        return respuesta.get('data')
    
    return ''

def solicitar2():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        respuesta = response.json()
        return respuesta[:5] 
    
    return []

def solicitudP():
         response = requests.get('https://swapi.dev/api/planets/1')
         if response.status_code == 200:
             respuesta = response.json()
             return respuesta
        
         return ''

