import scrapy
import json
from json import JSONEncoder

dino = []
todosDinos = []
 
class ContactEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__

class Dino:
    def __init__(self, name=None, pronunciation=None, nameMeaning=None, type=None,  diet=None,  live=None,  found_in=None, length=None, weight=None, taxonomy=None, namedBy=None, species=None):
        self.name = name
        self.pronunciation = pronunciation
        self.nameMeaning = nameMeaning
        self.type = type
        self.diet = diet
        self.live = live
        self.found_in = found_in
        self.length = length
        self.weight = weight
        self.taxonomy = taxonomy
        self.namedBy = namedBy
        self.species = species

    # This function returns a dictionary
    def dinoDict(self):
        obj = dict()
        obj['name'] = self.name
        obj['pronunciation'] = self.pronunciation
        obj['nameMeaning'] = self.nameMeaning
        obj['type'] = self.type
        obj['diet'] = self.diet
        obj['live'] = self.live
        obj['foundIn'] = self.found_in
        obj['length'] = self.length
        obj['weight'] = self.weight
        obj['taxonomy'] = self.taxonomy
        obj['namedBy'] = self.namedBy
        obj['species'] = self.species
        return obj


class DinosaursList(scrapy.Spider):
    name = "dinosaurs_list"
    start_urls = ['https://www.nhm.ac.uk/discover/dino-directory/name/name-az-all.html']
    custom_settings = {
        'CONCURRENT_ITEMS': '1',
        'CONCURRENT_REQUESTS': '1',
        'CONCURRENT_REQUESTS_PER_DOMAIN': '1',
        'CONCURRENT_REQUESTS_PER_IP': '1',
    }
   
    def parse(self, response):
        SET_SELECTOR = '.dinosaurfilter--all-list'

        for dinoItem in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.dinosaurfilter--all-list > a > p ::text'
            URL_SELECTOR = 'a ::attr(href)'
            yield {
                'name': dinoItem.css(NAME_SELECTOR).extract_first(),
                'URL': dinoItem.css(URL_SELECTOR).extract_first(),
            }
            dinoName = dinoItem.css(NAME_SELECTOR).extract_first()
            dinoUrl = dinoItem.css(URL_SELECTOR).extract_first()
            dinoName = ((dinoName).replace('\n',"")).replace('\t',"")
            dinoUrl="https://www.nhm.ac.uk"+dinoUrl
            dino.append(dinoName)
            dino.append(dinoUrl)
            todosDinos.append(dino.copy())
            dino.clear()

            if "zuniceratops.html" in dinoUrl:
                print("Grava")
                print(response.url)
                contact_json=json.dumps(todosDinos, sort_keys=True, indent=2)
                my_file = r'urls.json'
                with open(my_file, 'w', encoding='utf-8') as file:
                        file.write(contact_json)
