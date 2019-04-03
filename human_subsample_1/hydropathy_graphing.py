#!/usr/bin/env python

#Modified code for GITHUB in-class exercise 
#Comment every line 

#Import modules

import sys

#Usage statement with for loop

if (len(sys.argv)) < 6: 
	print ""
	print "usage: hydropathyEDC.py -i <input file> -o <output file> -v <threshold value> -w <window size>"
	print "-i: .fasta file"
	print "-v: threshold value"
	print "-w: window size"
	#print "-o: output file" 
	print ""
	sys.exit()

#For loop for arguments 

for i in range(len(sys.argv)): 
	if sys.argv[i] == "-i"
		InSeqFileName = sys.argv[i+1]
	elif sys.argv[i] == "-v"
		thresholdvalue = int(float(sys.argv[i+1]))
	elif sys.argv[i] == "-w"
		window_size = int(float(sys.argv[i+1]))
		OutFileName = sys.argv[i+1]

InFileName = "amino_acid_hydropathy_values.txt"
InFile = open(InFileName, 'r')
Data=[]
Hydropathy={}
LineNumber = 0

for Line in InFile:
    if(LineNumber>0):
        Line = Line.strip("\n")
        Data = Line.split(",")
        Hydropathy[Data[1]]=float(Data[2])
    LineNumber = LineNumber + 1
InFile.close()

#window = raw_input("Window size?")
window=int(window)
Value=0
window_counter=0
#InSeqFileName = raw_input("Name of sequence file to analyze?\n")
InSeqFile = open(InSeqFileName, 'r')
LineNumber = 0

for Line in InSeqFile:
    if(LineNumber>0):
        ProtSeq=Line.strip('\n')
    LineNumber = LineNumber + 1
InSeqFile.close()

OutFileName = InSeqFileName.strip('.fasta') + ".output.csv"
OutFile = open(OutFileName,"w")

#Initialize lists to write to for window counter and value 

window_counters=[]
Values=[]


for i in range(len(ProtSeq)):
    Value+=Hydropathy[ProtSeq[i]]
    if(i>(window-1) and i<=(len(ProtSeq)-window)):
        Value=Value-Hydropathy[ProtSeq[i-window]]

	#
	window_counters.append(window_counter)

	#
	Values.append(Value)

        #OutString = "%d,%.2f" % (window_counter, Value)
        #OutFile.write(OutString + "\n")

    window_counter+=1

OutFile.close()
