# PythonAutoTest 測試自動化專案

本專案是使用 **Selenium + Pytest** 進行網頁自動化測試的範例，結合自建的 HTML 測試頁與 Flask 模擬 API 後端，並使用 JSON 管理測試資料，提升測試模組化與可維護性。

---

PythonAutoTest/
├── web/ # 測試網站與 Flask 模擬後端
│ ├── app.py # Flask API 應用（/register, /login, /）
│ └── templates/
│ └── testweb.html # 測試用 HTML 頁面，Flask 透過 render_template 載入
│
├── scr/ # 自訂 Python 模組（PageObject、工具等）
│ ├── Index_page.py # 封裝頁面操作的 Page Object 類別
│ ├── for_try.py # 例外處理包裝（自動截圖等）
│ ├── pic_name.py # 擷取 parametrize ID 為檔名用
│ └── json_use.py # 讀取 JSON 測試資料的工具
│
├── tests/ # Pytest 測試腳本
│ └── test_*.py # 各項功能測試腳本
│
├── json/ # JSON 格式的測試資料集中管理
│ └── *.json # 各測試模組所用的參數資料
│
├── tools/ # 測試開發輔助工具
│ └── param_to_json.py # 將 pytest.param(...) 自動轉換為 JSON 檔案
│
└── README.md

## 🚀 使用方式

### 1️⃣ 安裝必要套件
pip install selenium flask pytest mysql-connector-python

2️⃣ 啟動 Flask 測試伺服器
cd web
python app.py
伺服器啟動後，打開測試網頁：
http://127.0.0.1:5000/

執行測試：
pytest tests/

✅ 功能特點
🔧 使用 Page Object Pattern 管理 Selenium 操作流程
📦 測試資料與邏輯分離，支援 @pytest.mark.parametrize + JSON
🧪 支援驗證：
    元素是否存在
    點擊更新顯示區
    下拉選單選項切換
    表單提交（姓名 / 註冊 / 登入）
    placeholder/value/text 檢查


⚠️ 注意事項
    測試網頁為本地 testweb.html，不需部署伺服器，但建議透過 Flask 提供入口 (http://127.0.0.1:5000/)。
    app.py 使用 Flask + MySQL 模擬 /register、/login API，請確認資料庫已啟動。
    mysql.connector.connect() 中的帳密請自行修改為本機可連接的設定。

