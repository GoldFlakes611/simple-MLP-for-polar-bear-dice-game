#the game itself, used to generate data for dataset_generator.py

def polar_bear(d1,d2,d3,d4,d5):

    new_list = [d1,d2,d3,d4,d5]


    for i,var in enumerate(new_list):
        new_list[i] = int(var)

    dic_pb = {1:0,2:0,3:2,4:0,5:4,6:0}
    dic_fish={1:6,2:5,3:0,4:3,5:0,6:1}


    for i in range(len(new_list)):
        new_list[i] = dic_pb[new_list[i]]

    num_pb = sum(new_list)

    new_list = [d1,d2,d3,d4,d5]
    for i,var in enumerate(new_list):
        new_list[i] = int(var)


    for i in range(len(new_list)):
        new_list[i] = dic_fish[new_list[i]]

    num_fish = sum(new_list)
    new_list = [d1,d2,d3,d4,d5]

    for i,var in enumerate(new_list):
        new_list[i] = int(var)

    for i, var in enumerate(new_list):
        if var == 3 or var == 5:
            new_list[i] = 14
        else:
            new_list[i] = 0
    num_plankton = sum(new_list)
    new_list = [num_pb,num_fish,num_plankton]
    return num_pb, num_fish, num_plankton

num_pb,num_fish,num_plankton = polar_bear(1,2,3,4,5)
#print(f'number of polar bears: {num_pb}, number of fish: {num_fish}, number of plankton: {num_plankton}')

