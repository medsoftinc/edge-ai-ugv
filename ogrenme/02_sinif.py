class Robot:
    def __init__(self, ad, max_hiz):
        self.ad = ad
        self.max_hiz = max_hiz
        self.hiz = 0.0
        self.x = 0.0

    def ilerle(self, hiz, sure):
        self.hiz = min(hiz, self.max_hiz)
        self.x += self.hiz * sure
        print(f"{self.ad}: {self.hiz} m/s ile {sure} sn gitti -> x = {self.x:.1f} m")

    def dur(self):
        self.hiz = 0.0
        print(f"{self.ad}: durdu")


ika = Robot("İKA-1", max_hiz=1.0)
drone = Robot("Drone-1", max_hiz=5.0)

ika.ilerle(0.5, 4)
ika.ilerle(3.0, 2)
drone.ilerle(3.0, 2)
ika.dur()
