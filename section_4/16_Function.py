# Function Work On The Idea Of DRY(Do Not repeat Your Self)

def say_hello():
    print('hellllooooo')


say_hello()

picture=[
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

def show_tree():
    for image in picture:
        for pixel in image:
            if (pixel):
                print('*', end="")
            else:
                print(' ', end="")
        print('')

show_tree()