from ast import Return
from itertools import count
from pickle import TRUE
import scrapy
from scrapy import Selector
import json
from json import JSONEncoder

dino = []
todosDinos = []
data = {'Dinosaur':[]}

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

    def clearDino(self):
        self.name = None
        self.pronunciation = None
        self.nameMeaning = None
        self.type = None
        self.diet = None
        self.live = None
        self.found_in = None
        self.length = None
        self.weight = None
        self.taxonomy = None
        self.namedBy = None
        self.species = None

def WriteDinos():
    contact_json=json.dumps(data, sort_keys=True, indent=2)
    print(contact_json)
    my_file = r'dinosaursDB.json'
    with open(my_file, 'w', encoding='utf-8') as file:
        file.write(contact_json)
    return TRUE


dinosaur = Dino()
class DinosaursList(scrapy.Spider):
    name = "dinosaurs_list"
    start_urls = [
        'https://www.nhm.ac.uk/discover/dino-directory/aardonyx.html',
        'https://www.nhm.ac.uk/discover/dino-directory/abelisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/achelousaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/achillobator.html',
        'https://www.nhm.ac.uk/discover/dino-directory/acrocanthosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/aegyptosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/afrovenator.html',
        'https://www.nhm.ac.uk/discover/dino-directory/agilisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/alamosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/albertaceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/albertosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/alectrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/alioramus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/allosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/alvarezsaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/amargasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/ammosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/ampelosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/amygdalodon.html',
        'https://www.nhm.ac.uk/discover/dino-directory/anchiceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/anchisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/ankylosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/anserimimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/antarctosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/apatosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/aragosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/aralosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/archaeoceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/archaeopteryx.html',
        'https://www.nhm.ac.uk/discover/dino-directory/archaeornithomimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/argentinosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/arrhinoceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/atlascopcosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/aucasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/austrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/avaceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/avimimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/bactrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/bagaceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/bambiraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/barapasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/barosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/baryonyx.html',
        'https://www.nhm.ac.uk/discover/dino-directory/becklespinax.html',
        'https://www.nhm.ac.uk/discover/dino-directory/beipiaosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/bellusaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/borogovia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/brachiosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/brachylophosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/brachytrachelopan.html',
        'https://www.nhm.ac.uk/discover/dino-directory/buitreraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/camarasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/camptosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/carcharodontosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/carnotaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/caudipteryx.html',
        'https://www.nhm.ac.uk/discover/dino-directory/cedarpelta.html',
        'https://www.nhm.ac.uk/discover/dino-directory/centrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/ceratosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/cetiosauriscus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/cetiosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/chaoyangsaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/chasmosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/chindesaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/chinshakiangosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/chirostenotes.html',
        'https://www.nhm.ac.uk/discover/dino-directory/chubutisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/chungkingosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/citipati.html',
        'https://www.nhm.ac.uk/discover/dino-directory/coelophysis.html',
        'https://www.nhm.ac.uk/discover/dino-directory/coelurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/coloradisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/compsognathus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/conchoraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/confuciusornis.html',
        'https://www.nhm.ac.uk/discover/dino-directory/corythosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/cryolophosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/dacentrurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/daspletosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/datousaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/deinocheirus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/deinonychus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/deltadromeus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/dicraeosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/dilophosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/diplodocus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/dromaeosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/dromiceiomimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/dryosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/dryptosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/dubreuillosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/edmontonia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/edmontosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/einiosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/elaphrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/emausaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/eolambia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/eoraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/eotyrannus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/equijubus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/erketu.html',
        'https://www.nhm.ac.uk/discover/dino-directory/erlikosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/euhelopus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/euoplocephalus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/europasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/eustreptospondylus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/fukuiraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/fukuisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/gallimimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/gargoyleosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/garudimimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/gasosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/gasparinisaura.html',
        'https://www.nhm.ac.uk/discover/dino-directory/gastonia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/giganotosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/gilmoreosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/giraffatitan.html',
        'https://www.nhm.ac.uk/discover/dino-directory/gobisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/gorgosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/goyocephale.html',
        'https://www.nhm.ac.uk/discover/dino-directory/graciliceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/gryposaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/guaibasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/guanlong.html',
        'https://www.nhm.ac.uk/discover/dino-directory/hadrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/hagryphus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/haplocanthosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/harpymimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/herrerasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/hesperosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/heterodontosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/heyuannia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/homalocephale.html',
        'https://www.nhm.ac.uk/discover/dino-directory/huayangosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/hylaeosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/hypacrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/hypsilophodon.html',
        'https://www.nhm.ac.uk/discover/dino-directory/iguanodon.html',
        'https://www.nhm.ac.uk/discover/dino-directory/indosuchus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/irritator.html',
        'https://www.nhm.ac.uk/discover/dino-directory/isisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/janenschia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/jaxartosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/jingshanosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/jinzhousaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/jobaria.html',
        'https://www.nhm.ac.uk/discover/dino-directory/juravenator.html',
        'https://www.nhm.ac.uk/discover/dino-directory/kentrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/khaan.html',
        'https://www.nhm.ac.uk/discover/dino-directory/kotasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/kritosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/lambeosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/lapparentosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/leaellynasaura.html',
        'https://www.nhm.ac.uk/discover/dino-directory/leptoceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/lesothosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/liaoceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/ligabuesaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/liliensternus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/lophorhothon.html',
        'https://www.nhm.ac.uk/discover/dino-directory/lophostropheus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/lufengosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/lurdusaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/lycorhinus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/magyarosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/maiasaura.html',
        'https://www.nhm.ac.uk/discover/dino-directory/majungasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/malawisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/mamenchisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/mapusaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/marshosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/masiakasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/massospondylus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/maxakalisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/megalosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/melanorosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/metriacanthosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/microceratus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/micropachycephalosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/microraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/minmi.html',
        'https://www.nhm.ac.uk/discover/dino-directory/monolophosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/mononykus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/mussaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/muttaburrasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/nanshiungosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/nedoceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/nemegtosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/neovenator.html',
        'https://www.nhm.ac.uk/discover/dino-directory/neuquenosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/nigersaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/nipponosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/noasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/nodosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/nomingia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/nothronychus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/nqwebasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/omeisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/opisthocoelicaudia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/ornitholestes.html',
        'https://www.nhm.ac.uk/discover/dino-directory/ornithomimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/orodromeus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/oryctodromeus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/othnielia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/ouranosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/oviraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/pachycephalosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/pachyrhinosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/panoplosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/pantydraco.html',
        'https://www.nhm.ac.uk/discover/dino-directory/paralititan.html',
        'https://www.nhm.ac.uk/discover/dino-directory/parasaurolophus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/parksosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/patagosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/pelicanimimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/pelorosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/pentaceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/piatnitzkysaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/pinacosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/plateosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/podokesaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/poekilopleuron.html',
        'https://www.nhm.ac.uk/discover/dino-directory/polacanthus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/prenocephale.html',
        'https://www.nhm.ac.uk/discover/dino-directory/probactrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/proceratosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/procompsognathus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/prosaurolophus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/protarchaeopteryx.html',
        'https://www.nhm.ac.uk/discover/dino-directory/protoceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/protohadros.html',
        'https://www.nhm.ac.uk/discover/dino-directory/psittacosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/quaesitosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/rebbachisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/rhabdodon.html',
        'https://www.nhm.ac.uk/discover/dino-directory/rhoetosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/rinchenia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/riojasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/rugops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/saichania.html',
        'https://www.nhm.ac.uk/discover/dino-directory/saltasaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/saltopus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/sarcosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/saurolophus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/sauropelta.html',
        'https://www.nhm.ac.uk/discover/dino-directory/saurophaganax.html',
        'https://www.nhm.ac.uk/discover/dino-directory/saurornithoides.html',
        'https://www.nhm.ac.uk/discover/dino-directory/scelidosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/scutellosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/secernosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/segisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/segnosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/shamosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/shanag.html',
        'https://www.nhm.ac.uk/discover/dino-directory/shantungosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/shunosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/shuvuuia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/silvisaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/sinocalliopteryx.html',
        'https://www.nhm.ac.uk/discover/dino-directory/sinornithosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/sinosauropteryx.html',
        'https://www.nhm.ac.uk/discover/dino-directory/sinovenator.html',
        'https://www.nhm.ac.uk/discover/dino-directory/sinraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/sonidosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/spinosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/staurikosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/stegoceras.html',
        'https://www.nhm.ac.uk/discover/dino-directory/stegosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/stenopelix.html',
        'https://www.nhm.ac.uk/discover/dino-directory/struthiomimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/struthiosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/styracosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/suchomimus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/supersaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/talarurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/tanius.html',
        'https://www.nhm.ac.uk/discover/dino-directory/tarbosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/tarchia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/telmatosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/tenontosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/thecodontosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/therizinosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/thescelosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/torosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/torvosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/triceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/troodon.html',
        'https://www.nhm.ac.uk/discover/dino-directory/tsagantegia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/tsintaosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/tuojiangosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/tylocephale.html',
        'https://www.nhm.ac.uk/discover/dino-directory/tyrannosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/udanoceratops.html',
        'https://www.nhm.ac.uk/discover/dino-directory/unenlagia.html',
        'https://www.nhm.ac.uk/discover/dino-directory/urbacodon.html',
        'https://www.nhm.ac.uk/discover/dino-directory/utahraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/valdosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/velociraptor.html',
        'https://www.nhm.ac.uk/discover/dino-directory/vulcanodon.html',
        'https://www.nhm.ac.uk/discover/dino-directory/yandusaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/yangchuanosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/yimenosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/yingshanosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/yinlong.html',
        'https://www.nhm.ac.uk/discover/dino-directory/yuanmousaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/yunnanosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/zalmoxes.html',
        'https://www.nhm.ac.uk/discover/dino-directory/zephyrosaurus.html',
        'https://www.nhm.ac.uk/discover/dino-directory/zuniceratops.html'
    ]

    custom_settings = {
        'CONCURRENT_ITEMS': '1',
        'CONCURRENT_REQUESTS': '1',
        'CONCURRENT_REQUESTS_PER_DOMAIN': '1',
        'CONCURRENT_REQUESTS_PER_IP': '1',
    }

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        dd_value = ""
        DINO_NAME = '.dinosaur--name-unhyphenated ::text'
        name = response.css(DINO_NAME).get()
        dinosaur.name = ((name).replace('\n',"")).replace('\t',"")

        DINO_NAME_DESCRIPTION = '.dinosaur--name-description > dt'
        dt_list = response.css(DINO_NAME_DESCRIPTION)
        for dt in dt_list:
            dt_value = dt.css('::text').get()

            if "Pronunciation" in dt_value:
                dd_value = dt.xpath('./following-sibling::dd/text()').get()
                dinosaur.pronunciation = dd_value
                
            elif "Name meaning" in dt_value:
                dd_value = dt.xpath('./following-sibling::dd/text()').get()
                dinosaur.nameMeaning = dd_value

            else:
                dd_value = dt.xpath('./following-sibling::dd/text()').get()

            #print(dt_value)
            #print(dd_value) 

        #print("----------Dino Descriprion-------------")
        DINO_DESCRIPTION = '.dinosaur--description > dt'
        dt_list = response.css(DINO_DESCRIPTION)
        for dt in dt_list:
            dt_value = dt.css('::text').get()

            if "Type of dinosaur" in dt_value:
                dd_value = dt.xpath('./following-sibling::dd/a/text()').get()
                dinosaur.type = dd_value
                
            elif "Length" in dt_value:
                dd_value = dt.xpath('./following-sibling::dd/a/text()').get()
                dinosaur.length = dd_value

            elif "Weight" in dt_value:
                dd_value = dt.xpath('./following-sibling::dd/a/text()').get()
                dinosaur.weight = dd_value

            else:
                dd_value = dt.xpath('./following-sibling::dd/text()').get()
            #print(dt_value)
            #print(dd_value)            

        DINO_INFO = '.dinosaur--info > dt'
        dt_info_list = response.css(DINO_INFO)
        #print("----------Dino INFO-------------")
        for dt in dt_info_list:
            dt_value = dt.css('::text').get()

            if("Diet" in dt_value):
                dd_value_link = dt.xpath('./following-sibling::dd/a/text()').get()
                dd_value_text = dt.xpath('./following-sibling::dd').get()
                diet_List= Selector(text=((((dd_value_text).replace('<dd>',"")).replace('</dd>',"")).replace('\n',"")).replace('\t',""))
                dd_value=diet_List.xpath('//a/text()').extract()
                dinosaur.diet = dd_value
                
            elif("When it lived" in dt_value):
                dd_value_link = dt.xpath('./following-sibling::dd/a/text()').get()
                dd_value_text = dt.xpath('./following-sibling::dd/text()').get()
                if(len(dd_value_link.strip())):
                    dd_value = dd_value_link + dd_value_text
                else:
                    dd_value = dd_value_text

                dinosaur.live = dd_value 

            elif("Found in:" in dt_value):
                #print("----------FOUND------------")
                dd_value_link = dt.xpath('./following-sibling::dd/a/text()').get()
                dd_value_text = dt.xpath('./following-sibling::dd').get()
                found_Places_List= Selector(text=((((dd_value_text).replace('<dd>',"")).replace('</dd>',"")).replace('\n',"")).replace('\t',""))
                dd_value=found_Places_List.xpath('//a/text()').extract()
                dinosaur.found_in = dd_value

            else:
                dd_value = dt.xpath('./following-sibling::dd/text()').get()
            
            #print(dt_value)
            #print(dd_value)

        DINO_TAX = '.dinosaur--taxonomy > dt'
        dt_tax_list = response.css(DINO_TAX)
        #print("----------Dino TAXONOMY-------------")
        for dt in dt_tax_list:
            dt_value = dt.css('::text').get()
            
            if("Taxonomy:" in dt_value):
                dd_value = dt.xpath('./following-sibling::dd/text()').get()
                #dd_value = Selector(text=((((dd_value_taxonomy).replace('<dd>',"")).replace('</dd>',"")).replace('\n',"")).replace('\t',""))
                dinosaur.taxonomy = dd_value

            elif("Named by" in dt_value):
                dd_value = dt.xpath('./following-sibling::dd/text()').get()
                #dd_value = Selector(text=((((dd_value_named_by_list).replace('<dd>',"")).replace('</dd>',"")).replace('\n',"")).replace('\t',""))
                dinosaur.namedBy = dd_value
            
            elif("Type species" in dt_value):
                dd_value = dt.xpath('./following-sibling::dd/text()').get()
                #dd_value = Selector(text=((((dd_value_type_species).replace('<dd>',"")).replace('</dd>',"")).replace('\n',"")).replace('\t',""))
                dinosaur.species = dd_value
            else:
                dd_value = dt.xpath('./following-sibling::dd/text()').get()

       
        print(dinosaur.name)
        print("----------- Dino  "+ dinosaur.name +" - pronto ------------")
        x = dinosaur.dinoDict()
        data["Dinosaur"].append(x)
        dinosaur.clearDino()
        if "zuniceratops" in response.url:
            write = WriteDinos()
            print("----------- Dino  Write "+ write +"------------")
           

