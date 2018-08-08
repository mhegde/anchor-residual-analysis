# Analysis of anchor screens
<b>This script calculates residuals for anchor arms compared to the control arm</b>  <br/>
<b>Author</b>: Mudra Hegde  <br/>
<b>Email</b>: mhegde@broadinstitute.org <br/>
<b>Version: 1.0 </b>  <br/>

<b> Required packages </b>
1. pandas <= 0.16.2
2. statsmodels

<b>The code to run the hypergeometric analysis and the relevant chip file should be in the current working directory. </b>

<b>Inputs</b>
1. <b>Input File</b>: File with sgRNAs in first column, LFCs of control arm and anchor arms in following columns
2. <b>Chip File</b>: File mapping sgRNAs to gene symbols; Default chip file: Brunello, CP0041
3. <b>Control</b>: Column name of control arm
4. <b>Outputfolder</b>: Folder to store all output files

<b>To run this script, type the following on the terminal:</b> <br/>
python anchor_analysis_v1.0 --input-file \<Path to inputfile\> --chip-file \<Path to chip file\> --control \<Control column name\> --outputfolder \<Path to outputfolder\>

Output file is a .txt file in the user-specified output folder with average residuals and average p-values per gene per anchor arm