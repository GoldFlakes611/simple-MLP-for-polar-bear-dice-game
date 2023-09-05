#use the follwing code to generate a dataset for training the neural network
from game import polar_bear
import random
import pandas as pd

nme = ["d1","d2","d3","d4","d5","pb","fish","plankton"]
d1,d2,d3,d4,d5, pb, fish, plankton, = [],[],[],[],[],[],[],[],
for i in range(100000):
    random_list = []
    for r in range(5):
        random_list.append(random.randint(1,6))

    num_pb,num_fish,num_plankton = polar_bear(random_list[0],random_list[1],random_list[2],random_list[3],random_list[4])
    d1.append(random_list[0]),d2.append(random_list[1]),d3.append(random_list[2]),d4.append(random_list[3]),d5.append(random_list[4]),pb.append(num_pb),fish.append(num_fish),plankton.append(num_plankton)


dict = {'x1': d1, 'x2': d2, 'x3': d3, 'x4': d4, 'x5': d5,'pb':pb,'fish':fish,'plankton':plankton}
df = pd.DataFrame(dict)
print(df)
df.to_csv("output.csv")