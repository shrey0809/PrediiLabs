import pandas as pd
columns=['RECORD_ID','CAMPNO','MAKETXT','MODELTXT','YEARTXT','MFGCAMPNO','COMPNAME','MFGNAME','BGMAN','ENDMAN','RCLTYPECD','POTAFF',
        'ODATE','INFLUENCED_BY','MFGTXT','RCDATE','DATEA','RPNO','FMVSS','DESC_DEFECT','CONEQUENCE_DEFECT','CORRECTIVE_ACTION','NOTES'
         ,'RCL_CMPT_ID','MFR_COMP_NAME','MFR_COMP_DESC','MFR_COMP_PTNO']
req_columns=['DESC_DEFECT','CONEQUENCE_DEFECT','CORRECTIVE_ACTION','NOTES']
def get_Index(columns,req):
    indices=[]
    for i in range(len(columns)):
        if(columns[i] in req):
            indices.append(i)
    return indices
indices=[]
indices=get_Index(columns,req_columns)
text=[]
with open('FLAT_RCL.txt') as f:
    text=f.readlines()
print("The total number of records is {} \n".format(len(text)))
records=[]
for i in range(len(text)):
    record=text[i].split('\t')
    temp=[]
    for j in indices:
        temp.append(record[j])
    records.append(temp)
try:
    df=pd.DataFrame(records,columns=req_columns)
    print("DataFrame created")
except Exception as e:
    print("Could not create DataFrame")
df['final_col']=df['DESC_DEFECT']+df['CONSEQUENCE_DEFECT']+df['CORRECTIVE_ACTION']+df['NOTES']
df.to_csv('Extracted.csv')



