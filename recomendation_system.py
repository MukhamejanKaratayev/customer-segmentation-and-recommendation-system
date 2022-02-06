import sys
import pandas as pd


def find_recomendations(df, product_id):
    recomendation = []
    df['product_combination'] = [x.strip('[]').replace(' ', "").replace("'", "").split(',') for x in df['product_combination']]
    results = df[df['product_combination'].apply(lambda x: product_id in x)]
    for i in results['product_combination']:
        for j in i:
            if j not in recomendation and j != product_id:
                recomendation.append(j)
                if len(recomendation) == 10:
                    break
        else:
            continue
        break
    return recomendation 


if len(sys.argv)<3:
    print('Error, incorrect number of arguments!')
else:
    args = sys.argv
    file_path = args[1]
    product_id = args[2]
    data = pd.read_csv(file_path)
    res = find_recomendations(data,str(product_id))
    
    if len(res) == 0:
        print('There is no results for this product')
    else:
        print('The list of products can be recomended with this product: ' + str(res))