import pandas as pd

input_file = 'Cp.csv'
output_file = 'output.csv'

df = pd.read_csv(input_file)

reshaped_df = pd.DataFrame(index=df['Assembly Accession'].unique())

for _, row in df.iterrows():
    attribute_name = row['Assembly BioSample Attribute Name']
    attribute_value = row['Assembly BioSample Attribute Value'] if pd.notna(row['Assembly BioSample Attribute Value']) else 'NA'
    reshaped_df.at[row['Assembly Accession'], attribute_name] = attribute_value

reshaped_df.reset_index(inplace=True)
reshaped_df.rename(columns={'index': 'Assembly Accession'}, inplace=True)

reshaped_df.fillna('NA', inplace=True)

reshaped_df.to_csv(output_file, index=False)
