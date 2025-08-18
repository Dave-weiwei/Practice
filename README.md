# 🧪 自動化測試練習專案（Flask + Selenium + Pytest + Docker + CI/CD）

本專案為練習用自動化測試框架，包含：

- 🌐 自建 Flask 測試網站（支援註冊、登入、表單互動）
- 🧪 Selenium + Pytest 撰寫 UI 自動化測試
- 📦 Docker 打包 web 與 test 環境
- 🌀 GitHub Actions CI 自動執行測試並部署 Allure 測試報告
- 📊 測試報告：Allure HTML 格式（支援多瀏覽器）
- 🔐 使用 `.env` 與 GitHub Secrets 管理測試變數與 DB 連線

## 📂 專案結構

```bash
.
├── web/                    # Flask 網站（可本機或容器啟動）
│   └── app.py
├── tests/                  # 測試案例與工具
│   ├── test_*.py
│   ├── fail_screenshots/
│   └── ...
├── json/                   # JSON 測試資料
├── reports/                # Allure 測試報告（CI/CD 會自動產出）
├── .github/workflows/      # GitHub Actions 自動化設定
│   └── python-ci.yml
├── docker-compose.yml      # 容器設定（web + tests）
├── requirements.txt        # 套件需求
├── pytest.ini              # Pytest 設定檔
├── Makefile                # 常用測試指令自動化
└── .env.example            # 環境變數樣板（請自行建立 .env）
```

## 🚀 快速啟動

### 1. 安裝套件（本機開發用）

```bash
pip install -r requirements.txt
```

### 2. 建立 `.env`

請參考 `.env.example`，建立自己的 `.env` 檔案：

```
BASE_URL=http://127.0.0.1:5000
PG_HOST=your-db-host
PG_PORT=5432
PG_USER=your-db-user
PG_PASSWORD=your-db-password
PG_DB=your-db-name
```

### 3. 常用指令（配合 Makefile）

```bash
make up           # 啟動 web 容器
make test         # 執行測試
make report       # 產生 Allure HTML 報告
make open         # 開啟本機報告
make clean        # 清除報告
```

## 🐳 Docker 整合

透過 `docker-compose.yml` 管理：

- `web`：Flask 測試網站
- `tests`：Pytest + Selenium 測試容器

## ⚙️ GitHub Actions 自動化流程（CI/CD）

- 觸發條件：`push` 到 `main` 分支
- 執行流程：
  1. 從 GitHub Secrets 產生 `.env`
  2. 啟動 Flask 容器
  3. 執行 Selenium 測試（Chrome / Firefox）
  4. 產出 Allure 測試報告
  5. 部署報告到 GitHub Pages (`gh-pages` 分支)

## 🔍 測試報告展示

GitHub Pages（自動部署）：  
👉 [Allure 測試報告](https://你的帳號.github.io/你的repo名/allure/chrome/)

## 🔒 GitHub Secrets 設定

請至 `Settings > Secrets > Actions` 新增以下參數：

| 名稱         | 說明                   |
| ------------ | ---------------------- |
| BASE_URL     | e.g. `http://web:5000` |
| PG_HOST      | 資料庫位址             |
| PG_PORT      | 5432                   |
| PG_USER      | 資料庫使用者           |
| PG_PASSWORD  | 密碼                   |
| PG_DB        | 資料庫名稱             |
| GITHUB_TOKEN | 預設已存在，無需更動   |

## 📌 備註

- 測試會自動截圖失敗案例，儲存於 `tests/fail_screenshots/YYYY-MM-DD/` 內。
- 所有測試案例皆支援多瀏覽器（Chrome / Firefox）。
- 測資集中管理於 `json/` 資料夾。
