import requests
import pytest

def test_status_code():
    answer = requests.get('https://pokemonbattle.me:9104/trainers',
                          headers={'trainer_token' : 'eb78be79c5c3a7a1960ade302202f68e', 
                                    'Content-Type' : 'application/json'},
                        params={'trainer_id':4628})
    print(answer.text)
    assert answer.status_code == 200
   

def test_name(): 
    answer_body = requests.get('https://pokemonbattle.me:9104/trainers',
                          headers={'trainer_token' : 'eb78be79c5c3a7a1960ade302202f68e', 
                                    'Content-Type' : 'application/json'},
                        params={'trainer_id':4628})  
    assert answer_body.json()['trainer_name'] == 'Ket'