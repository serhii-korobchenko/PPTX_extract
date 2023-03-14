import os
import pandas as pd
import textractplus as tp


files_csv=[]
your_dir='/home/serhii/Desktop/pptx_files'

with open('result.txt', 'w') as wr:
    for f in os.listdir(your_dir):
        if f.endswith('pptx') or f.endswith('pptm'):
            text=tp.process(os.path.join(your_dir,f))
            text_parsed = text.decode("utf-8")
            splited_list = text_parsed.split('\n')
            for item in splited_list:
                print(item)
                wr.write(item)
                wr.write('\n')

            files_csv.append([f,text])
    pd.DataFrame(files_csv,columns=['filename','text']).to_csv('output_result.csv')