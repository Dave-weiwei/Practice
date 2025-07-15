import os
import pytest
from datetime import datetime
from test_settings import BROWSERS, REPORT_ROOT

# 建立以日期時間為名的資料夾
timestamp = datetime.now().strftime("%Y-%m-%d")
timestamp_file = datetime.now().strftime("%H-%M-%S")
report_dir = os.path.join(REPORT_ROOT, timestamp)
os.makedirs(report_dir, exist_ok=True)
log_dir = os.path.join(report_dir, "logs")  # ✅ log 子目錄
os.makedirs(log_dir, exist_ok=True)         # ✅ log 資料夾先建立

for browser in BROWSERS:
    # 為每種瀏覽器建立獨立報告
    report_file = f"{timestamp_file}_{browser}_report.html"
    report_path = os.path.join(report_dir, report_file)
    log_file = os.path.join(log_dir, f"{timestamp_file}_{browser}_log.txt")
    
    print(f"\n🔍 執行 {browser} 測試...")
    
    pytest_args = [
        "tests",
        "-v",
        f"--mybrowser={browser}",  # ✅ 關鍵：把 browser 傳給 pytest
        f"--html={report_path}",
        "--self-contained-html",
        "--cov-report=term-missing"
        f"--log-file={log_file}",
    ]

    pytest.main(pytest_args)