#Name - Harry Patel
#NSID-ozc189
#Student Number-11358887
#Instructor-Lauressa Stilling
def initialRead_state(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    initialState = [list(line.strip()) for line in lines]
    return initialState