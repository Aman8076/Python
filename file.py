# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()



# f=open("demo.txt","a")
# data=f.write("\nHello, World! aman sharma")

# print(type(data))
# f.close()


# f=open("sample.txt","w")
# f.close()


# f=open("demo.txt","r+")
# f.write("abcdef")
# print(f.read() )
# f.close()


# import os
# os.remove("sample.txt")


with open("demo.txt","r") as f:
    data=f.read()

    new_data=data.replace("java", "python")
    print(new_data)

    with open("demo.txt","w") as f:
        f.write(new_data)