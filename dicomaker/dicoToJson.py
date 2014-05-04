

inputDico = open('cmudict_modif', 'r');
outputJson = open('cmudict.json', 'w');

consideredEntries = 0;
irrelevantEntries = 0;
firstLine = True;


outputJson.write("{\n");

for line in inputDico:
    
    consideredEntries = consideredEntries + 1;
    if "(0)" in line or "(1)" in line or "(2)" in line:
        #ignore it
        irrelevantEntries = irrelevantEntries + 1;
    else:
        if firstLine:
            firstLine = False
            
        else:
            outputJson.write(",\n");
            
        line = line.replace("(0)", "").replace("(1)", "").replace("(2)", "").replace("(3)", "").replace("(4)", "").replace("\n","").replace("  ", " ");    
        lineArr = line.split(" ");
        outputJson.write("\"" + lineArr[0] + "\" : [");
        
        for phonemeIdx in range(len(lineArr) - 1):
            
            if phonemeIdx > 0:
                outputJson.write(", ");
            
            outputJson.write("\"" + lineArr[phonemeIdx + 1].replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "") + "\"");
        outputJson.write("]");
            
        
outputJson.write("\n}");
inputDico.close();
outputJson.close();
print(str(irrelevantEntries) + " entries over " + str(consideredEntries) + " elements.");