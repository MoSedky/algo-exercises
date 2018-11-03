def get_triplets(input_array):
    triplets_array = []
    arra_length = len(input_array)
    for num in range(arra_length-2):
        if((input_array[num]+input_array[num+1]+input_array[num+2])==0):
           print(input_array[num], input_array[num+1], input_array[num+2])







get_triplets([-5, 4, 8, 1, 1, -2])
