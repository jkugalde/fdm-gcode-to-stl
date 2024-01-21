def nline(writer,line): #function to write lines in the txt
    s=str(line)
    writer.write(s)
    writer.write('\n')

def coords(line): #returns c and y coordinates of the line
    s=str(line)
    x=s[s.index("X")+1:s.index("Y")-1]
    if "E" in s:
        y=s[s.index("Y")+1:s.index("E")-1]
    else:
        y=s[s.index("Y")+1:]
    return "["+x+","+y+"]"

#reads the gcode file

filename = "cube" #remember to change the name of the file here

with open(filename+".gcode",'r') as stl:
    
    with open(filename+"gcodestl.txt",'w') as gcodestl: #the text to paste in openscad

        currentpoint="[0,0]"
        newpoint="[0,0]"
        currentlayer="0.3" #this has to be modified depending on your piece

        for linea in stl: #looks for the line where the printing of the part starts

            substring=";TYPE:WALL-INNER"
            if substring in linea:
                break

        for linea in stl: #identifies layer change, G1s and G0s

            if "Z" in linea:

                currentlayer=linea[linea.index("Z")+1:]

            elif "G1" in linea and "X" in linea:

                newpoint=coords(linea)
                if currentpoint!="[0,0]":
                    nline(gcodestl,"line("+currentpoint+","+newpoint+","+currentlayer+",linewidth);")
                currentpoint=newpoint
            
            elif "G0" in linea:

                newpoint=coords(linea)
                currentpoint=newpoint

            elif "M140" in linea: #the print ends

                break

        gcodestl.close()
    
stl.close()




