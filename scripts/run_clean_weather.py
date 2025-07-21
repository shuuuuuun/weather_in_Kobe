import os
import logging
from dotenv import load_dotenv
from src.preprocess.clean_weather import clean_weather_data

# ログの設定
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    # .envの読み込み
    load_dotenv()
    
    # 環境変数からパスを取得
    raw_path = os.getenv("RAW_WEATHER_PATH", "data/raw/kobe_weather.csv")
    output_path = os.getenv("OUTPUT_PATH", "data/processed/kobe_weather_cleaned.csv")
    target_year = int(os.getenv("TARGET_YEAR", "2015"))
    
    logging.info(f"📥 Loading raw data from: {raw_path}")
    cleaned_df = clean_weather_data(raw_path, target_year)
    logging.info(f"📊 Filtered data for the year: {target_year}: {len(cleaned_df)} rows")
    
    # 出力フォルダがない場合、作成
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cleaned_df.to_csv(output_path, index=False)
    logging.info(f"📤 Cleaned data saved to: {output_path}")
    
if __name__ == "__main__":
    main()