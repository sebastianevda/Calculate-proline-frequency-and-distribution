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
for xyz in range(250):
    all_aa = ""
    newlist = ""
    for lines in splitrep:
        if len(lines)>0:
            #print (lines)
            split_entry = lines.split("\n")
            s = ""
            name = str(split_entry[0])
            entry = str(s.join(split_entry[1:]))
            randomise_entry = "".join(random.sample(entry,len(entry)))
            newlist = newlist + name + "\t" + randomise_entry + "\n"
            #here is to find all the Ps and find out what the next letter is
            all_aa = all_aa + randomise_entry + "ZXXXXXXXXXXXXX"


    #print (all_aa)
            
    for test in range (1,13):
        nplus = test
        A = 0
        C = 0
        D = 0
        E = 0
        F = 0
        G = 0
        H = 0
        I = 0
        K = 0
        L = 0
        M = 0
        N = 0
        P = 0
        Q = 0
        R = 0
        S = 0
        T = 0
        V = 0
        W = 0
        Y = 0
        Z = 0
        list_of_A_positions = set([pos for pos, char in enumerate(all_aa) if char == "A"])
        list_of_C_positions = set([pos for pos, char in enumerate(all_aa) if char == "C"])
        list_of_D_positions = set([pos for pos, char in enumerate(all_aa) if char == "D"])
        list_of_E_positions = set([pos for pos, char in enumerate(all_aa) if char == "E"])
        list_of_F_positions = set([pos for pos, char in enumerate(all_aa) if char == "F"])
        list_of_G_positions = set([pos for pos, char in enumerate(all_aa) if char == "G"])
        list_of_H_positions = set([pos for pos, char in enumerate(all_aa) if char == "H"])
        list_of_I_positions = set([pos for pos, char in enumerate(all_aa) if char == "I"])
        list_of_K_positions = set([pos for pos, char in enumerate(all_aa) if char == "K"])
        list_of_L_positions = set([pos for pos, char in enumerate(all_aa) if char == "L"])
        list_of_M_positions = set([pos for pos, char in enumerate(all_aa) if char == "M"])
        list_of_N_positions = set([pos for pos, char in enumerate(all_aa) if char == "N"])
        list_of_P_positions = set([pos for pos, char in enumerate(all_aa) if char == "P"])
        list_of_Q_positions = set([pos for pos, char in enumerate(all_aa) if char == "Q"])
        list_of_R_positions = set([pos for pos, char in enumerate(all_aa) if char == "R"])
        list_of_S_positions = set([pos for pos, char in enumerate(all_aa) if char == "S"])
        list_of_T_positions = set([pos for pos, char in enumerate(all_aa) if char == "T"])
        list_of_V_positions = set([pos for pos, char in enumerate(all_aa) if char == "V"])
        list_of_W_positions = set([pos for pos, char in enumerate(all_aa) if char == "W"])
        list_of_Y_positions = set([pos for pos, char in enumerate(all_aa) if char == "Y"])
        list_of_Z_positions = set([pos for pos, char in enumerate(all_aa) if char == "Z"])

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
        Ppct = int(round(float(P)/float(count)*100))
        #print (str(P) + "\t" + str(count) + "\t" + str(Ppct))        
        #Matrix = str(A) + "\t" +  str(C) + "\t" +  str(D) + "\t" +  str(E) + "\t" +  str(F) + "\t" +  str(G) + "\t" +  str(H) + "\t" +  str(I) + "\t" +  str(K) + "\t" +  str(L) + "\t" +  str(M) + "\t" +  str(N) + "\t" +  str(P) + "\t" +  str(Q) + "\t" +  str(R) + "\t" +  str(S) + "\t" +  str(T) + "\t" +  str(V) + "\t" +  str(W) + "\t" +  str(Y) +"\t"+ str(Z)+"\n"
        Matrix = Matrix + str(Ppct) + "\t"
        #print (Matrix)

        A = 0
        C = 0
        D = 0
        E = 0
        F = 0
        G = 0
        H = 0
        I = 0
        K = 0
        L = 0
        M = 0
        N = 0
        P = 0
        Q = 0
        R = 0
        S = 0
        T = 0
        V = 0
        W = 0
        Y = 0
        Z = 0
    P = 0    
    Matrix = Matrix + "\n"
print (Matrix)

print ("done")
