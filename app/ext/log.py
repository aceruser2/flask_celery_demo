import logging
import os

# 設定 LOG 輸出格式
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')

# 設定 LOG 輸出位置
log_file = os.path.join('logs', 'app.log')

# 設定 LOG 處理器
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

# 設定 LOG 等級
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# 新增 LOG 處理器
logger.addHandler(file_handler)