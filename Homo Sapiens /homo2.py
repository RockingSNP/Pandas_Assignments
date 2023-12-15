import pandas as pd
import time
start = time.time()

df=pd.read_csv('homosapiens.csv')


df= df.ffill(axis = 0)


homo_df = df[df['Source Organism'].str.contains('Homo sapiens')]

unique_eid_list = homo_df['Entry ID'].unique().tolist() 

acd_list =[]


for i in unique_eid_list: 
     acd_list.append(homo_df[homo_df['Entry ID'].str.contains(i)]['Accession Code(s)'].tolist()) 
     
acd_seri = pd.Series(acd_list,name = 'Accession Code(s)')
organism_seri = pd.Series('Homo sapiens',name = 'Soure Organism')
unique_eid_seri = pd.Series(unique_eid_list,name = 'Entry ID')

first = pd.concat([acd_seri,organism_seri,unique_eid_seri],axis = 1)

first= first.ffill(axis = 0)  

second = pd.Series(first.to_dict('records'))

final= second.to_dict()

#print(final)

stop = time.time()

print("Time taken to Execute "+ str(stop-start))


#firtry = pd.DataFrame(data
