import requests


class Pokemon:

    def __init__(self, name):
        response = requests.get(url=f"https://pokeapi.co/api/v2/pokemon/{name}/")
        data = response.json()
        self.specie = data["name"].title()
        self.id = data["id"]
        self.height = data["height"]/10
        self.type = data["types"][0]["type"]["name"].title()
        self.sprite_url = data["forms"][0]["url"]
        if data["weight"]/10 < 1:
            self.weight = data["weight"]/10
        else:
            self.weight = int(data["weight"]/10)

    def get_sprite(self):
        poke_photo = requests.get(url=self.sprite_url)
        pokemon_form = poke_photo.json()
        url_front = pokemon_form["sprites"]["front_default"]
        return url_front

