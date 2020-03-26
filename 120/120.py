import re


def temperature():
    directory = input("Please insert the file's directory :")
    with open(directory, 'r') as f:
        temp = f.readlines()

    with open('output', 'w') as out:
        for i in temp:
            # Extracting values as float from temp list
            a = [float(s) for s in re.findall(r'-?\d+\.?\d*', i)]
            tf = a[1] * (9/5) + 32
            out.write(f'{a[0]}F of {tf}C \n')
        out.close()

temperature()

#path C:\Users\Ivaylo.Lambrev\PycharmProjects\Python-foundations-new-course\120\input
