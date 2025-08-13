# 自動化測試專案

本專案使用 **Python + Pytest + Selenium** 進行 UI 自動化測試，並搭配 **PostgreSQL** 進行資料驗證。  
測試對象為練習用網頁（含註冊、登入、按鈕點擊、下拉選單、表單提交等功能）。

## 🌐 測試網頁位置

- [https://autotest-deploy.onrender.com/]

## 📂 專案結構

```bash
.
├── Index_page.py # 頁面操作封裝 (Page Object)
├── for_try.py # 測試失敗截圖工具
├── pic_name.py # 測試 ID 擷取工具
├── db_util.py # 資料庫連線與查詢
├── json_use.py # 測資讀取工具
├── test_settings.py # 測試設定 (瀏覽器、報告路徑)
├── conftest.py # pytest fixture 與瀏覽器初始化
├── run_tests.py # 測試批次執行與 Allure 報告產生
├── requirements.txt # 依賴套件
├── pytest.ini # pytest 設定
└── tests/ # 測試案例目錄
```

## 📦 環境需求

- Python 3.10+
- Google Chrome / Mozilla Firefox
- 安裝套件：

```bash
pip install -r requirements.txt
安裝 Allure 產生測試報告
▶️ 執行測試
1. 單一瀏覽器執行
pytest --mybrowser=chrome
pytest --mybrowser=firefox
2. 產生 Allure 報告
pytest --alluredir=./reports/allure-results
allure serve ./reports/allure-results
3. 批次執行（Chrome + Firefox）
python run_tests.py
```

| 類別           | 測試 ID                         | 測試資料 (username, password, confirm)            | 預期結果 | 說明                               |
| -------------- | ------------------------------- | ------------------------------------------------- | -------- | ---------------------------------- |
| Email 格式錯誤 | `invalid-email-str-user`        | `"68443841", "testtest", "testtest"`              | False    | 帳號非 Email 格式                  |
| 密碼格式錯誤   | `non-string-password`           | `"test@test", "35438438438", "35438438438"`       | False    | 密碼全為數字，缺少大寫字母         |
| Email 格式錯誤 | `invalid-email-at-start`        | `"@asdasd@gmail.com", "OK123123ok", "OK123123ok"` | False    | Email 開頭為 @                     |
| Email 格式錯誤 | `invalid-email-at-end`          | `"asdasd@gmail.com@", "OK123123ok", "OK123123ok"` | False    | Email 結尾為 @                     |
| Email 格式錯誤 | `missing-at-symbol`             | `"asdasdgmail.com", "OK123123ok", "OK123123ok"`   | False    | 缺少 @ 符號                        |
| 密碼格式錯誤   | `missing-number-in-password`    | `"a@a.com", "OKOKOKok", "OKOKOKok"`               | False    | 密碼缺少數字                       |
| 密碼格式錯誤   | `missing-uppercase-in-password` | `"a@a.com", "ok123123", "ok123123"`               | False    | 密碼缺少大寫字母                   |
| 密碼長度不足   | `too-short-password`            | `"a@a.com", "Ok123", "Ok123"`                     | False    | 密碼少於 6 碼                      |
| 密碼缺少大寫   | `no-uppercase-password`         | `"a@a.com", "ok123123", "ok123123"`               | False    | 無大寫字母（與上面類似但 id 不同） |
| 密碼不一致     | `password-confirm-mismatch`     | `"a@a.com", "OK123123ok", "OK123456ok"`           | False    | 確認密碼與密碼不同                 |
| Email 已存在   | `existing-email`                | `已註冊帳號, 正確密碼格式`                        | False    | 測試資料庫中已有此帳號             |
| 正確註冊       | `valid-register`                | `"abc@test.com", "OK123123ok", "OK123123ok"`      | True     | 所有格式正確，註冊成功             |

📌 功能覆蓋範圍
UI 測試
.按鈕點擊
.標題點擊
.下拉選單
.表單提交
.註冊與登入
.驗證層
.前端欄位驗證（HTML pattern / minlength）
.後端 API 驗證
.資料庫查詢驗證
.錯誤追蹤
.測試失敗自動截圖（use_try）

Report link:
https://dave-weiwei.github.io/Practice/allure/chrome/index.html
https://dave-weiwei.github.io/Practice/allure/firefox/index.html

💡 專案價值與實務應用
本專案雖為練習性質，但設計時已盡量模擬實務中的自動化測試流程：

測試設計思維：採用多組有效與無效輸入資料，覆蓋常見錯誤情境與邊界條件。

分層結構：以 Page Object 模式封裝操作邏輯，便於維護與擴充。

多層驗證：

前端欄位驗證（HTML5 pattern、長度限制）

後端 API 回應訊息

資料庫狀態檢查

錯誤處理與除錯機制：失敗時自動截圖保存，方便問題追蹤。

跨瀏覽器測試：可在 Chrome / Firefox 執行，模擬不同使用者環境。

持續整合概念：可搭配 GitHub Actions + Allure 產出測試報告，方便團隊查看結果。

這份專案展示了我從測試案例設計、腳本撰寫，到報告產出的完整測試流程能力，並可依需求調整至不同專案場景。
