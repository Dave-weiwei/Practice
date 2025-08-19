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
```

## ✅ 測試項目與覆蓋範圍

目前自動化測試已涵蓋以下功能區塊，並針對「正確流程」與「錯誤情境」皆有撰寫驗證：

### 🧪 UI 功能測試（Selenium）

| 功能區塊 | 驗證項目說明                                                        |
| -------- | ------------------------------------------------------------------- |
| 首頁顯示 | 驗證主標題、次標題、按鈕點擊是否正常反應                            |
| 表單填寫 | 測試輸入欄位的值是否能正確顯示與提交                                |
| 下拉選單 | 驗證下拉選項選取後顯示正確結果                                      |
| 註冊功能 | ✅ 成功註冊流程 / ❌ 錯誤格式帳號、密碼、密碼不一致 / ❌ 已註冊帳號 |
| 登入功能 | ✅ 正確帳密登入 / ❌ 錯誤帳號/密碼、未註冊帳號                      |

- 所有測試皆支援多瀏覽器（Chrome / Firefox）
- 錯誤案例將自動截圖並儲存於 `tests/fail_screenshots/` 下

### 📡 API 層級測試（[可擴充]）

目前尚未加入，但規劃可針對 `/register`、`/login` 做獨立 API 驗證（使用 `requests + pytest` 實作）

### 🔍 資料驗證（資料庫）

部分測試案例會搭配 PostgreSQL 檢查以下項目：

| 項目             | 驗證說明                                   |
| ---------------- | ------------------------------------------ |
| 帳號是否成功註冊 | 驗證 DB 中是否建立對應 username/password   |
| 登入帳密是否存在 | 驗證輸入帳密與資料庫是否一致               |
| 清除測試資料     | 測試結束自動刪除測試帳號（避免污染資料庫） |

### 📊 覆蓋度與設計策略

- 採用 `pytest.mark.parametrize` 搭配 JSON 檔案統一管理測資
- 每筆測試皆具備 ID 名稱，利於失敗診斷與報告標示
- 使用 `pytest-cov` 可顯示測試覆蓋率（若未來加入模組內邏輯測試）
  """

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
👉 [Allure 測試報告- chrome](https://dave-weiwei.github.io/Practice/allure/chrome/index.html)
👉 [Allure 測試報告- firefox](https://dave-weiwei.github.io/Practice/allure/firefox/index.html)

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
