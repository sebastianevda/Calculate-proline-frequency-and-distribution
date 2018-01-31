import sys
import re
import random
import textwrap
#input_filename = "Pp_all proteins_ORF_minus_proline_rich.fa"
input_filename = "Pioneer rich in proline.fa"
#input_filename = "Pp_SP no THMM_1330.names.aa"
infile = open(input_filename)

#outfile = open(output_filename,"w")

read = infile.read()

newlist = ""
all_aa = ""
#cleaninfile = read.replace("\n","")
#rep = cleaninfile.replace (">","\n>")
splitrep = read.split(">")
Matrix = ""
for xyz in range(1):
    all_aa = ""
    newlist = ""
    for lines in splitrep:
        if len(lines)>0:
            #print (lines)
            split_entry = lines.split("\n")
            s = ""
            name = str(split_entry[0])
            entry = str(s.join(split_entry[1:]))
            #randomise_entry = "".join(random.sample(entry,len(entry)))
            #newlist = newlist + name + "\t" + randomise_entry + "\n"
            #here is to find all the Ps and find out what the next letter is
            all_aa = all_aa + entry + "ZXXXXXXXXXXXXX"


    #print (all_aa)
            
    for test in range (1,13):
        nplus = test

        P = 0
        list_of_P_positions = set([pos for pos, char in enumerate(all_aa) if char == "P"])


        #this is for all the Ps, what are the next chars.
        count = 0
        Ppct = 0
        for line in list_of_P_positions:
            #print (all_aa[line+nplus:line+nplus+1])

            if all_aa[line+nplus:line+nplus+1] is not "X":
                count = count + 1
            #if all_aa[line:line+1] is "X":
                #print("X")
            if line+nplus in list_of_P_positions:
                P = P + 1
        Ppct = (float(P)/float(count)*100)
        #print (str(P) + "\t" + str(count) + "\t" + str(Ppct))        
        #Matrix = str(A) + "\t" +  str(C) + "\t" +  str(D) + "\t" +  str(E) + "\t" +  str(F) + "\t" +  str(G) + "\t" +  str(H) + "\t" +  str(I) + "\t" +  str(K) + "\t" +  str(L) + "\t" +  str(M) + "\t" +  str(N) + "\t" +  str(P) + "\t" +  str(Q) + "\t" +  str(R) + "\t" +  str(S) + "\t" +  str(T) + "\t" +  str(V) + "\t" +  str(W) + "\t" +  str(Y) +"\t"+ str(Z)+"\n"
        Matrix = Matrix + str(Ppct) + "\t"
        #print (Matrix)

        P = 0
    P = 0    
    Matrix = Matrix + "\n"
print (Matrix)

print ("done")
