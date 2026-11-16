class SpaceMission:
    def set_details(self):
        self.mission = "Chandrayaan-3"
        self.destination = "Moon"
        self.status = "Successful"

    def get_details(self):
        print("Mission:", self.mission)
        print("Destination:", self.destination)
        print("Status:", self.status)


m1 = SpaceMission()

m1.set_details()
m1.get_details()
