import pandas as pd
import os
import glob


folder_path = r'data/raw'

excel_files = glob.glob(os.path.join(folder_path, '*xlsx'))


if not excel_files:
    print('Nenhum arquivo encontrado!')
else:
    dfs = []

    for excel_file in excel_files:
        try:
            df_temp = pd.read_excel(excel_file)

            file_name = os.path.basename(excel_file)

            df_temp['file_name'] = file_name

            if 'brasil' in file_name.lower():
                df_temp['country'] = 'Brasil'
            elif 'france' in file_name.lower():
                df_temp['country'] = 'França'
            elif 'italian' in file_name.lower():
                df_temp['country'] = 'Italia'

            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
            dfs.append(df_temp)

        except Exception as e:
            print(f'Erro ao ler o arquivo {excel_file} : {e}')

    if dfs:

        result = pd.concat(dfs, ignore_index=True)

        output_file = os.path.join('data', 'ready', 'clean.xlsx')

        writer = pd.ExcelWriter(output_file)

        result.to_excel(writer, index=False)

        writer._save()
    else:
        print('Nenhum arquivo encontrado!')

