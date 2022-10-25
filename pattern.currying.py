#
#  curry with PyMonard
#
#
#
#

from functools import reduce
from re import I
from pymonad.tools import curry
from itertools import count

data = [
  {
    "_id": "63394ac3a188eff74384d94b",
    "guid": "b910ef0e-ddc2-464d-a6db-ab0d1898f9b4",
    "isActive": True,
    "age": 30,
    "firstname": "Wiggins",
    "surname": "Bray",
    "gender": "male",
    "email": "wigginsbray@martgo.com",
    "address": {
      "city": "Ola",
      "country": "Bulgaria"
    }
  },
  {
    "_id": "63394ac3bbb1d958a0958ff6",
    "guid": "322e1d55-b0b8-45d5-8e53-3eeca9483a80",
    "isActive": True,
    "age": 17,
    "firstname": "Whitley",
    "surname": "Villarreal",
    "gender": "male",
    "email": "whitleyvillarreal@martgo.com",
    "address": {
      "city": "Belvoir",
      "country": "Myanmar"
    }
  },
  {
    "_id": "63394ac33c0c39d7297d7344",
    "guid": "49fc22a5-9349-48d1-a341-8a31dcab5967",
    "isActive": True,
    "age": 26,
    "firstname": "Tonya",
    "surname": "Reid",
    "gender": "female",
    "email": "tonyareid@martgo.com",
    "address": {
      "city": "Coleville",
      "country": "Vatican City State (Holy See)"
    }
  },
  {
    "_id": "63394ac36501ef5acf574404",
    "guid": "f13dac0c-79b3-4f31-810e-2f5cd3111acc",
    "isActive": True,
    "age": 39,
    "firstname": "Tiffany",
    "surname": "Wallace",
    "gender": "female",
    "email": "tiffanywallace@martgo.com",
    "address": {
      "city": "Springdale",
      "country": "Sri Lanka"
    }
  },
  {
    "_id": "63394ac3d6d78b8fd94bf759",
    "guid": "2966d44f-1c9f-44e8-9dc9-217b53f87acf",
    "isActive": False,
    "age": 24,
    "firstname": "Tanisha",
    "surname": "Buckley",
    "gender": "female",
    "email": "tanishabuckley@martgo.com",
    "address": {
      "city": "Ola",
      "country": "Bulgaria"
    }
  },
  {
    "_id": "63394ac34954b769effeedde",
    "guid": "a1e0f80b-5ddf-4a40-a91c-762fb7ff45c2",
    "isActive": False,
    "age": 16,
    "firstname": "Thomas",
    "surname": "Singleton",
    "gender": "male",
    "email": "thomassingleton@martgo.com",
    "address": {
      "city": "Helen",
      "country": "Zimbabwe"
    }
  },
  {
    "_id": "63394ac393f4d47c8b1b669c",
    "guid": "dfcaaa56-f581-443d-b33e-0cc10956d252",
    "isActive": False,
    "age": 29,
    "firstname": "Melanie",
    "surname": "Briggs",
    "gender": "female",
    "email": "melaniebriggs@martgo.com",
    "address": {
      "city": "Sattley",
      "country": "Malaysia"
    }
  },
  {
    "_id": "63394ac342951a14e11509a4",
    "guid": "923d6c74-c0e1-4603-af39-a5b8b1441d8e",
    "isActive": False,
    "age": 19,
    "firstname": "Myra",
    "surname": "Todd",
    "gender": "female",
    "email": "myratodd@martgo.com",
    "address": {
      "city": "Robbins",
      "country": "Svalbard and Jan Mayen Islands"
    }
  },
  {
    "_id": "63394ac3b187c45848a771e9",
    "guid": "0d89824d-bc6a-41e9-878e-97eb66b01abd",
    "isActive": False,
    "age": 26,
    "firstname": "Abbott",
    "surname": "Avila",
    "gender": "male",
    "email": "abbottavila@martgo.com",
    "address": {
      "city": "Ola",
      "country": "Bulgaria"
    }
  },
  {
    "_id": "63394ac34c000dff82689d4a",
    "guid": "50e0c87b-a9e3-4369-9c42-31b0b2b5c2c5",
    "isActive": True,
    "age": 22,
    "firstname": "Lily",
    "surname": "Pittman",
    "gender": "female",
    "email": "lilypittman@martgo.com",
    "address": {
      "city": "Fannett",
      "country": "Bulgaria"
    }
  },
  {
    "_id": "63394ac3ac88ff4c08d0fbf5",
    "guid": "2975b1e3-7fc6-4c21-8906-dde794747e1b",
    "isActive": False,
    "age": 33,
    "firstname": "Roberson",
    "surname": "Sweeney",
    "gender": "male",
    "email": "robersonsweeney@martgo.com",
    "address": {
      "city": "Bakersville",
      "country": "Samoa"
    }
  },
  {
    "_id": "63394ac311095aef9b4c535d",
    "guid": "7f3fcfc1-5a8b-4e29-b5d2-cefd078f9c70",
    "isActive": True,
    "age": 22,
    "firstname": "Hannah",
    "surname": "Neal",
    "gender": "female",
    "email": "hannahneal@martgo.com",
    "address": {
      "city": "Bethany",
      "country": "Somalia"
    }
  },
  {
    "_id": "63394ac3ea5cb67d4cda4fa0",
    "guid": "b201f9f0-d3f1-4059-8ddd-c05fb3674eac",
    "isActive": False,
    "age": 37,
    "firstname": "Magdalena",
    "surname": "Simmons",
    "gender": "female",
    "email": "magdalenasimmons@martgo.com",
    "address": {
      "city": "Wakarusa",
      "country": "Indonesia"
    }
  },
  {
    "_id": "63394ac3a17ddbc3f3810794",
    "guid": "70b3715c-197b-448a-8965-e174017ae2fb",
    "isActive": False,
    "age": 24,
    "firstname": "Melton",
    "surname": "Jacobson",
    "gender": "male",
    "email": "meltonjacobson@martgo.com",
    "address": {
      "city": "Bergoo",
      "country": "Christmas Island"
    }
  },
  {
    "_id": "63394ac3e626124e6a3870dc",
    "guid": "aefd3e2e-c618-4409-be6f-eb9d531097cb",
    "isActive": True,
    "age": 14,
    "firstname": "Kelly",
    "surname": "Marshall",
    "gender": "female",
    "email": "kellymarshall@martgo.com",
    "address": {
      "city": "Weogufka",
      "country": "Suriname"
    }
  },
  {
    "_id": "63394ac39a053c85323e6149",
    "guid": "0030fd31-a7a1-45c4-942c-562f7edffa0d",
    "isActive": True,
    "age": 14,
    "firstname": "Conrad",
    "surname": "Brady",
    "gender": "male",
    "email": "conradbrady@martgo.com",
    "address": {
      "city": "Dalton",
      "country": "Bulgaria"
    }
  },
  {
    "_id": "63394ac3ecdd8fb11b240e6a",
    "guid": "f1a91478-b3ba-45e4-bb96-6fd0811d64c3",
    "isActive": False,
    "age": 30,
    "firstname": "Sloan",
    "surname": "Underwood",
    "gender": "male",
    "email": "sloanunderwood@martgo.com",
    "address": {
      "city": "Graniteville",
      "country": "Norway"
    }
  }
]

counter = lambda data: reduce( lambda a,x: a+1, data, 0)

@curry(4)
def mysearch( country, city, gender, data):
    return  filter( lambda item: item["address"]["country"] == country, 
            filter( lambda item: item["address"]["city"] == city,
            filter( lambda item: item["gender"] == gender, 
            data )))

print(counter(tuple(mysearch("Bulgaria", "Ola", "male", data))))

#curry the first parameter
mysearchInBulgaria = mysearch("Bulgaria")
print(counter(mysearchInBulgaria("Ola", "male", data)))
print(counter(mysearchInBulgaria("Dalton", "male", data)))

#curry the second parameter
mysearchInBulgariaOla = mysearchInBulgaria("Ola")
print(counter(mysearchInBulgariaOla("male", data)))

