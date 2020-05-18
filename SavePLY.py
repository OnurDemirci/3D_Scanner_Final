def SavePLY(X,Y,Z,filename):
    #function for saving the .ply file
    f=open("created_models/"+str(filename)+".ply","w+") #a file is opened for writing
    s=[]
    for i in range(9):
        s.append("0")
    #the header of the ply file is defined
    s[0]="ply"
    s[1]="format ascii 1.0"
    s[2]="element vertex "+ str(len(X))
    s[3]="property float32 x"
    s[4]="property float32 y"
    s[5]="property float32 z"
    s[6]="element face 0"
    s[7]="property list uint8 int32 vertex_indices"
    s[8]="end_header"


    for i in range(len(s)):
            f.write(s[i]+"\n") # writing defined values into generated .ply file

    #Creating a .ply file from the coordinates in the list X,Y,Z respectively
    for i in range(len(X)):
        f.write(str(X[i])+" ")
        f.write(str(Y[i])+" ")
        f.write(str(Z[i])+"\n")
    print("Model created.")
    f.close()
