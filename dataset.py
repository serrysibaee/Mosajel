
class Loader:

    def loads(self):
        import json
        # Open the JSON file
        with open("poems.json", "r") as f:
            # Load the JSON data from the file
            dataset = json.load(f)
        
        return dataset
        


    def take_sample(self,dataset,letter):
        import random
        pem_list = dataset[letter]
        return random.choice(pem_list)

