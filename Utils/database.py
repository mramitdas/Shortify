import pymongo


class Database:
    def __init__(self):
        client = pymongo.MongoClient(
            "Database URL")

        db = client['Db_name']
        self.collection = db["Table_name"]

    def insertion(self, data):
        self.collection.insert_one(data)

    def search(self):
        entire_data = list(self.collection.find())
        latest_url = entire_data[-1].get("url")

        return latest_url, entire_data

    def delete(self):

        data_list = self.collection.find()

        for data in data_list:
            id = data.get("_id")
            self.collection.delete_one({"_id": id})