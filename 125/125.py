import re


def temperature():
    # path C:\Users\Angel.Kostadinov\PycharmProjects\PythonCourse\input
    directory = input("Please insert the file's directory :")
    with open(directory, 'r') as f:
        temp = f.readlines()
    with open('output', 'w') as out:
        for i in temp:
            match = re.sub(r"-?\d+\.*?\d*(?!\d*F)", lambda x: str(float(x[0]) * (9/5) + 32)+'F', i)
            newmatch = match.replace('C', '')
            out.write(newmatch+'\n')
        out.close()


temperature()
