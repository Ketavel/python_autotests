import requests 

response = requests.post("https://pokemonbattle.me:9104/pokemons",
                        json ={
                          'name':"ashee", 
                          'photo':'https://dolnikov.ru/pokemons/albums/005.png'
                             },
                        headers={
                            'trainer_token' : 'eb78be79c5c3a7a1960ade302202f68e', 
                            'Content-Type' : 'application/json'
                                 })
print(response.text)

response_change_name = requests.put("https://pokemonbattle.me:9104/pokemons", 
                                    headers={
                                        'trainer_token' : 'eb78be79c5c3a7a1960ade302202f68e', 
                                        'Content-Type' : 'application/json'},
                                    json={
                                        "pokemon_id":"12599", 
                                        "name":"asdfd"
                                          })
print(response_change_name.text)


response_add_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
                                    headers={
                                          'trainer_token' : 'eb78be79c5c3a7a1960ade302202f68e',
                                          'Content-Type' : 'application/json'},
                                    json={
                                         "pokemon_id":"12599"
                                         })
print(response_add_pokeball.text)