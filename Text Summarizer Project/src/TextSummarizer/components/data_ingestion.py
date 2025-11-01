import os
import urllib.request as request
import zipfile
import TextSummarizer.logging as logger
from TextSummarizer.utils.common import get_size
from pathlib import Path
from TextSummarizer.entity import DataIngestionConfig

# rerunning our ingestion, delete the old bad file so it can redownload properly
import os
bad_zip = "artifacts/data_ingestion/data.zip"
if os.path.exists(bad_zip):
    os.remove(bad_zip)
    print("🗑️ Deleted old invalid ZIP file.")

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> Path:
        logger.info("Starting data download...")
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(
                f"Data downloaded successfully! and is saved at {self.config.local_data_file} "
                f"and the file size is {get_size(Path(filename))}"
            )
        else:
            logger.info(f"File already exists of size {get_size(self.config.local_data_file)}")

        return self.config.local_data_file

    def extract_zip_file(self, zip_file_path: Path, unzip_dir: Path) -> None:
        logger.info("Starting data extraction...")
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)
        logger.info(f"Data extracted successfully at {unzip_dir}")