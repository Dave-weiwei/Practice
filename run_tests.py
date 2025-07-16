import os
import pytest
import subprocess
from datetime import datetime
import webbrowser
from test_settings import BROWSERS, REPORT_ROOT

# 1. 建立主資料夾（日期命名）
timestamp = datetime.now().strftime("%Y-%m-%d")
timestamp_file = datetime.now().strftime("%H-%M-%S")
report_dir = os.path.join(REPORT_ROOT, timestamp)
os.makedirs(report_dir, exist_ok=True)

# 2. 建立 log 子資料夾
log_dir = os.path.join(report_dir, "logs")
os.makedirs(log_dir, exist_ok=True)

# 3. 設定 Allure 及測試結果輸出資料夾
allure_cli = os.path.expanduser("~/scoop/apps/allure/current/bin/allure.bat")

if not os.path.exists(allure_cli):
    print(f"❌ 找不到 Allure CLI：{allure_cli}")
    exit(1)



for browser in BROWSERS:
    print(f"\n🔍 執行 {browser} 測試...")

    log_file = os.path.join(log_dir, f"{timestamp_file}_{browser}_log.txt")
    
    allure_raw = os.path.join(report_dir, f"allure-results_{browser}")
    allure_html = os.path.join(report_dir, f"allure-report_{browser}")
    os.makedirs(allure_raw, exist_ok=True)
    
    pytest_args = [
        "tests",
        "-v",
        f"--mybrowser={browser}",
        f"--alluredir={allure_raw}",           # ✅ Allure 測試中繼結果
        "--cov-report=term-missing",
        f"--log-file={log_file}"
    ]

    pytest.main(pytest_args)

    # 4. 執行結束後，自動產生 Allure HTML 報告
    print("\n📊 產生 Allure 報告...")
    subprocess.run([allure_cli, "generate", allure_raw, "-o", allure_html, "--clean"], check=True)

    print(f"\n✅ Allure 報告已產生：{allure_html}")

index_file = os.path.join(allure_html, "index.html")
# subprocess.run([allure_cli, "serve", allure_raw])
webbrowser.open(f"file://{os.path.abspath(index_file)}")