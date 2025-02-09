import json

class TestDataExtractor:
    def get_data_from_test_data(self):
        with open("C:\\Projects\\OldProjects\\myrepo_3rdFeb\\test_config_pet_store.json", "r") as file:
            self.config = json.load(file)
        return self.config

    def get_pet_test_data(self):
        self.config = self.get_data_from_test_data()
        self.pet_config = self.config["Pets"]
        return self.pet_config

    def get_users_test_data(self):
        self.config = self.get_data_from_test_data()
        self.users_config = self.config["Users"]
        return self.users_config

    def get_orders_test_data(self):
        self.config = self.get_data_from_test_data()
        self.order_config = self.config["Orders"]
        return self.order_config

