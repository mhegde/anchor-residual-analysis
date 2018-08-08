# Analysis of anchor screens
<b>This script calculates residuals for an anchor arm compared to the control arm</b>  
<b>Author</b>: Mudra Hegde  
<b>Email</b>: mhegde@broadinstitute.org
<b>Version: 1.0 </b>  

<b> Required packages </b>
1. pandas <= 0.16.2
2. statsmodels

<b>Inputs</b>
1. <b>Input File: File with sgRNAs in first column, LFCs of control arm and anchor arms in following columns</b>
2. <b>Chip File: File mapping sgRNAs to gene symbols; Default chip file: Brunello, CP0041</b>
3. <b>Control: Column name of control arm</b>
4. <b>Outputfolder: Folder to store all output files </b>

<b>To run this script, type the following on the terminal:</b>
python anchor_analysis_v1.0 --input-file \<Path to inputfile\> --chip-file \<Path to chip file\> --control \<Control column name\> --outputfolder \<Path to outputfolder\>

Output file is a .txt file in the user-specified output folder with average residuals and average p-values per gene per anchor arm