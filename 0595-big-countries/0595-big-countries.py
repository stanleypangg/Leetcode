import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    cols = ['name', 'population', 'area']
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[cols]