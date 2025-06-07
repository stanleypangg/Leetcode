import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    cols = ['product_id']
    df = products[(products.low_fats == 'Y') & (products.recyclable == 'Y')]
    return df[cols]