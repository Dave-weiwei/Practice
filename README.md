# 🧪 Web 自動化測試練習平台

![CI Status](https://github.com/Dave-weiwei/Practice/actions/workflows/python-ci.yml/badge.svg)
本專案為 Selenium + Pytest + Allure 的自動化測試練習平台，模擬本地測試網頁的各項互動功能（如註冊、登入、輸入、點擊、下拉選單等），並整合 GitHub Actions 持續整合與報告部署。

---

## 📦 安裝與執行

### 1️⃣ 安裝 Python 套件

pip install -r requirements.txt

2️⃣ 安裝 Allure CLI

Windows（使用 Scoop）：
scoop install allure

Linux / Ubuntu：
sudo apt install allure

3️⃣ 執行測試與產出報告

python run_tests.py
測試完成後，Allure 報告會輸出至：
reports/YYYY-MM-DD/allure-report_chrome/
reports/YYYY-MM-DD/allure-report_firefox/
🌐 GitHub Pages 報告連結
瀏覽器 線上報告連結
Chrome 📊 查看報告
Firefox 📊 查看報告

每次 CI/CD 完成，會自動更新這些頁面

🧪 多瀏覽器支援
你可以在 test_settings.py 中控制測試瀏覽器：
BROWSERS = ["chrome", "firefox"]
CI 會根據這個清單逐一執行並產出對應報告。

🔁 CI/CD 自動化流程說明（GitHub Actions）
功能包含： -啟動本地 Flask 測試伺服器 -連接 MySQL 測試資料庫 -自動執行 pytest 測試（Chrome / Firefox）
-Allure 報告自動產出 -上傳測試報告至 GitHub Artifact -上傳 Allure HTML 報告至 GitHub Pages（並提供固定連結） -工作流程檔案：.github/workflows/python-ci.yml

📂 專案結構摘要
.
├── tests/ # 測試案例（pytest）
├── scr/ # 封裝模組（PageObject、錯誤截圖等）
├── json/ # 測試資料 JSON
├── web/ # 測試目標 Flask 本地網頁
├── run_tests.py # 一鍵測試與報告主腳本
├── pytest.ini # pytest 設定檔
├── requirements.txt # 相依套件清單
├── .github/workflows/ # CI 設定檔
└── reports/ # 測試報告輸出目錄
🖼️ 錯誤截圖自動儲存
測試失敗時，自動截圖儲存至：

tests/fail_screenshots/YYYY-MM-DD/
便於後續除錯與報告擴充。

Report link:
https://dave-weiwei.github.io/Practice/allure/chrome/index.html
https://dave-weiwei.github.io/Practice/allure/firefox/index.html

👤 作者
Dave Chen（GitHub Actions x 自動化測試整合練習）

```

```
