'''
This script calculates residuals for a screen compared to the control arm
Author: Mudra Hegde
Email: mhegde@broadinstitute.org
'''
import pandas as pd
import csv, argparse, os
import statsmodels.api as sm

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file',
        type=str,
        help='Input file with LFCs for 6T arm and anchor arms; first column sgRNAs, LFCs 2nd column onwards')
    parser.add_argument('--chip-file',
        type=str,
        default='CP0041_20170705_compat.chip')
    parser.add_argument('--control',
        type=str,
        help='Control arm column name')
    parser.add_argument('--outputfolder',
        type=str,
        help='Folder name for all outputs')
    return parser
'''
Extracts the average residuals and p-values for all anchor arms in input file
'''
def get_avg(foldername):
    files = os.listdir(foldername)
    files = [f for f in files if all(['.pdf' not in f, 'chip' not in f, 'README' not in f])]
    avgs = pd.DataFrame()
    for i,f in enumerate(files):
        df = pd.read_table(foldername+'/'+f)
        df = df.sort(columns='Gene Symbol')
        if i == 0:
            avgs['Gene Symbol'] = df['Gene Symbol']
            avgs['Number of perturbations'] = df['Number of perturbations']
        avgs[f[:-23]+'_Avg_res'] = df['Average LFC']
        avgs[f[:-23]+'_Avg_pval'] = df['Average -log(p-values)']
    return avgs
'''
Calculates residuals
'''
def get_residuals(df,y,x):
    df_res = sm.OLS(df[y],df[x]).fit()
    df_resid = pd.DataFrame({'sgRNA Sequence':df['Construct Barcode'],y:df_res.resid})
    return df_resid

'''
Runs hypergeometric code for sgRNA residuals of each anchor arm
'''
def run_hypergeom(input_df,chip,control):
    colnames = list(input_df.columns)[1:]
    colnames = [c for c in colnames if control not in c]
    lognorm_resid = pd.DataFrame({'sgRNA Sequence':input_df['Construct Barcode']})
    for i,c in enumerate(colnames):
        col_resid = get_residuals(input_df,c,control)
        lognorm_resid[c] = col_resid[c]
    lognorm_resid.to_csv('temp_files/'+args.input_file.split('/')[-1][:-4]+'_residuals_volcanoinput.txt',sep='\t',index=False)
    cmd = 'anapython hypergeom_2.3.1.py --input-file temp_files/'+args.input_file.split('/')[-1][:-4]+'_residuals_volcanoinput.txt --chip-file '+chip_file
    print 'Running hypergeometric analysis on lfc sgRNA residuals..'
    os.system(cmd)
    sub_folders = os.listdir(os.curdir)
    lognorm_folder = [s for s in sub_folders if 'residuals' in s][0]
    lognorm_avg = get_avg(lognorm_folder)
    lognorm_avg.to_csv(args.input_file.split('/')[-1][:-4]+'lognorm_residuals.txt',sep='\t',index=False)
    return 1

'''
Creates the output folder and changes current directory to output folder
'''
def setup_o_folder(outputfolder):
    print 'Creating output folder ...'
    os.system('mkdir '+outputfolder)
    cwd = os.getcwd()
    os.chdir(cwd+'/'+outputfolder)
    new_cwd = os.getcwd()
    print 'In output folder: '+new_cwd
    os.system('mkdir temp_files')
    return 1

if __name__ == '__main__':
    args = get_parser().parse_args()
    input_df = pd.read_table(args.input_file)
    chip_file = args.chip_file
    outputfolder = args.outputfolder
    val = setup_o_folder(outputfolder)
    print os.getcwd()
    control = args.control
    val = run_hypergeom(input_df,chip_file,control)

