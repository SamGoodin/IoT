import CatFeeder
import time

keepGoing = True

while keepGoing:
    CatFeeder.feedByGmail()
    CatFeeder.getTemp()
    time.sleep(5)