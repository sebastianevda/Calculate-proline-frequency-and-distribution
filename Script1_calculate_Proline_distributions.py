import sys
import re
import random
import textwrap
#input_filename = "Pp_all proteins_ORF_minus_proline_rich.fa"
#input_filename = "Pioneer rich in proline.fa"
#input_filename = "Pp_SP no THMM_1330.names.aa"
#input_filename = "those_with_inistu_in_glands_inc_proline_rich.names.aa"
input_filename = "Pp_all proteins_ORF_minus_proline_rich.fap_more_than19.9.tab"
infile = open(input_filename)

#outfile = open(output_filename,"w")

read = infile.read()

newlist = ""
#cleaninfile = read.replace("\n","")
#rep = cleaninfile.replace (">","\n>")
splitrep = read.split(">")
for lines in splitrep:
    if len(lines)>0:
        #print (lines)
        split_entry = lines.split("\n")
        s = ""
        name = str(split_entry[0])
        entry = str(s.join(split_entry[1:]))
        newlist = newlist + name + "\t" + entry + "\n"
        #print (str(split_entry[0]) + "\t" + str(len(s.join(split_entry[1:]))))
#print (newlist)
newlist2 = newlist[:-1]
#outfile.close()            


#will make one line per random (so 250 lines) - each line 5 columns of pcts
output_pcts = ""
string_numbers = ""
string_names = ""
distribution_string_per_gene = ""
distribution_string_per_five = ""
distribution_string3 = ""
for i in range(250):
    newlistsplit = newlist2.split("\n")
    newlist222 = random.sample(newlistsplit,5)#this is the number to randomly choose
    #newlist2222 = newlist222.split("\n")
    #print i+1
    for line in newlist222:
        linesplit = line.split ("\t")
        name = linesplit[0]
        entry = linesplit[1]
        number_of_p = float(len(re.findall("P",entry)))
        number_of_aa = float(len(entry))
        pct_of_p = number_of_p/number_of_aa *100
        #print (str((len(re.findall("P",entry)))))
        #print (str(len(entry)))
        #print (str(int((round(pct_of_p)))))
        string_numbers = string_numbers + (str(int((round(pct_of_p))))) + "\t"
        string_names = string_names + name + "\t"


        #now for each gene - what is the distribution like across 10% bins so will divide each seq in 10% window, and then get numnber of p.
        length_of_entry = len(entry)
        #print (entry)
        
        number_of_parts = 10
        if len(entry)> 50:# number_of_parts:  #or could use > number_of_parts
            split_into_parts = textwrap.wrap(entry,int(round(length_of_entry/number_of_parts)))#this is the number of bins - can try 10 or 5 and 20?
            
            for x in range(number_of_parts):
                #print (x+1)
                len_of_segment = float(len(split_into_parts[x]))
                #print (str(len_of_segment))
                number_of_p_in_segment = float(len(re.findall("P",split_into_parts[x])))
                pct_of_p_in_segement = (int(round(number_of_p_in_segment/len_of_segment *100)))
                #print (str(pct_of_p_in_segement))
                distribution_string_per_gene = distribution_string_per_gene + str(pct_of_p_in_segement) + "\t"
            #print (distribution_string)

            distribution_string_per_five = distribution_string_per_five + distribution_string_per_gene + "\t\t"
            distribution_string_per_gene = ""

    distribution_string_per_five = distribution_string_per_five + "\n"
    #print (distribution_string_per_five)


        
    output_pcts = output_pcts + string_names + "\t\t" + string_numbers + "\n"
    string_numbers = ""
    string_names = ""

#print (output_pcts)

out_pct_file = open(input_filename + "out_put_pct_250_rand_for_" + str(number_of_parts)+"_parts.tab","w")
out_pct_file.write(output_pcts)
out_pct_file.close()

out_dist_file = open(input_filename + "out_put_distribution_250_rand_for_5_for_" + str(number_of_parts)+"_parts.tab","w")
out_dist_file.write(distribution_string_per_five)
out_dist_file.close()





print ("done")






