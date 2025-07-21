import pandas as pd

def load_weather_csv(path: str) -> pd.DataFrame:
    """ 
    指定されたCSVファイルを読み込み、Dateカラムを日付型に変換して返す関数。
    Args:
        path (str): 読み込むCSVファイルのパス。
    """
    df = pd.read_csv(path)
    df["Date"] = pd.to_datetime(df["Date"],format="%Y/%m/%d")
    return df

def filter_year(df: pd.DataFrame, year: int) -> pd.DataFrame:
    """
    指定された年のデータのみを抽出する関数。
    Args:
        df (pd.DataFrame): 元のデータフレーム。
        year (int): 抽出する年。
    """
    return df[df["Date"].dt.year == year]

def drop_missing_temperature(df: pd.DataFrame) -> pd.DataFrame:
    """
    気温が欠損している行を削除する関数。
    Args:
        df (pd.DataFrame): 元のデータフレーム。
    """
    return df.dropna(subset=["Temperature"])

def clean_weather_data(path: str, year: int) -> pd.DataFrame:
    """
    天気データを読み込み、指定された年のデータを抽出し、気温が欠損している行を削除する関数。
    Args:
        path (str): 読み込むCSVファイルのパス。
        year (int): 抽出する年。
    """
    df = load_weather_csv(path)
    df = filter_year(df, year)
    df = drop_missing_temperature(df)
    return df