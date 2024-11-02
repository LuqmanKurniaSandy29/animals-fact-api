from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Initial data for 25 animals with names and interesting facts
animals = {
    "1": {"name": "Elephant", "fact": "Elephants are the largest land animals on Earth."},
    "2": {"name": "Giraffe", "fact": "Giraffes have the longest necks of any animal, reaching up to 6 feet."},
    "3": {"name": "Blue Whale", "fact": "Blue whales are the largest animals ever known to have lived on Earth."},
    "4": {"name": "Cheetah", "fact": "Cheetahs are the fastest land animals, reaching speeds up to 70 mph."},
    "5": {"name": "Octopus", "fact": "Octopuses have three hearts and blue blood."},
    "6": {"name": "Honey Bee", "fact": "Honey bees can recognize human faces."},
    "7": {"name": "Dolphin", "fact": "Dolphins sleep with one eye open."},
    "8": {"name": "Penguin", "fact": "Penguins can jump as high as 9 feet in a single leap."},
    "9": {"name": "Kangaroo", "fact": "Kangaroos can't walk backwards."},
    "10": {"name": "Sloth", "fact": "Sloths move so slowly that algae can grow on their fur."},
    "11": {"name": "Frog", "fact": "Some frogs can freeze without dying."},
    "12": {"name": "Shark", "fact": "Sharks have been around for over 400 million years."},
    "13": {"name": "Koala", "fact": "Koalas sleep up to 22 hours a day."},
    "14": {"name": "Owl", "fact": "Owls can rotate their heads up to 270 degrees."},
    "15": {"name": "Camel", "fact": "Camels can go for weeks without water."},
    "16": {"name": "Bat", "fact": "Bats are the only mammals that can fly."},
    "17": {"name": "Butterfly", "fact": "Butterflies taste with their feet."},
    "18": {"name": "Panda", "fact": "Pandas spend about 14 hours a day eating bamboo."},
    "19": {"name": "Tiger", "fact": "No two tigers have the same stripes."},
    "20": {"name": "Wolf", "fact": "Wolves have strong family bonds and live in packs."},
    "21": {"name": "Rabbit", "fact": "Rabbits' teeth never stop growing."},
    "22": {"name": "Parrot", "fact": "Parrots can live for over 50 years."},
    "23": {"name": "Hippopotamus", "fact": "Hippos can hold their breath underwater for up to 5 minutes."},
    "24": {"name": "Ant", "fact": "Ants can lift objects up to 50 times their own body weight."},
    "25": {"name": "Seahorse", "fact": "Male seahorses are the ones who carry and give birth to the young."}
}

# Route dasar
@app.route('/')
def home():
    return jsonify({"message": "Selamat datang di API hewan!"})

# Classes for CRUD functionality
class AnimalList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(animals),
            "animals": animals
        }

class AnimalDetail(Resource):
    def get(self, animal_id):
        animal = animals.get(animal_id)
        if animal:
            return {
                "error": False,
                "message": "Success",
                "animal": animal
            }
        return {"error": True, "message": "Animal not found"}, 404

class AddAnimal(Resource):
    def post(self):
        data = request.get_json()
        if not data or "name" not in data or "fact" not in data:
            return {"error": True, "message": "Invalid data"}, 400

        animal_id = str(len(animals) + 1)
        new_animal = {
            "name": data["name"],
            "fact": data["fact"]
        }
        animals[animal_id] = new_animal
        return {
            "error": False,
            "message": "Animal added successfully",
            "animal": new_animal
        }, 201

class UpdateAnimal(Resource):
    def put(self, animal_id):
        animal = animals.get(animal_id)
        if animal:
            data = request.get_json()
            if data:
                animal["name"] = data.get("name", animal["name"])
                animal["fact"] = data.get("fact", animal["fact"])
            return {
                "error": False,
                "message": "Animal updated successfully",
                "animal": animal
            }
        return {"error": True, "message": "Animal not found"}, 404

class DeleteAnimal(Resource):
    def delete(self, animal_id):
        animal = animals.pop(animal_id, None)
        if animal:
            return {
                "error": False,
                "message": "Animal deleted successfully",
                "animal": animal
            }
        return {"error": True, "message": "Animal not found"}, 404

# Adding resources to API
api.add_resource(AnimalList, '/animals')
api.add_resource(AnimalDetail, '/animals/<string:animal_id>')
api.add_resource(AddAnimal, '/animals/add')
api.add_resource(UpdateAnimal, '/animals/update/<string:animal_id>')
api.add_resource(DeleteAnimal, '/animals/delete/<string:animal_id>')

if __name__ == '__main__':
    app.run(debug=True)
