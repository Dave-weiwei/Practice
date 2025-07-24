# 🧪 Web 自動化測試練習平台

![CI Status](https://github.com/Dave-weiwei/Practice/actions/workflows/python-ci.yml/badge.svg)

AutoTest Practice Project (Repo A)
Flask + pytest + GitHub Actions + Render 自動化測試與部署練習專案

---

## 📌 專案簡介
此專案為完整的自動化測試實作練習，包含：
- 使用 Python + Selenium + pytest 撰寫網頁互動測試
- 整合 GitHub Actions 自動化測試流程（CI）
- 測試通過後自動同步 Web 檔案至部署用 Repo（CD）
- Flask 提供簡易註冊／登入功能（含資料庫驗證）
- 使用 PostgreSQL 作為後端資料庫

---

## 🏗️ 專案架構（多 Repo 分工）
| Repo | 內容 | 用途 |
|------|------|------|
| ✅ Repo A（本專案） | 全部原始碼與測試程式碼<br>含 CI 自動測試 + 同步腳本 | 開發、測試、CI |
| ✅ Repo B           | 僅包含部署用 Web 檔案<br>含 `render.yaml` 設定 | 自動部署到 Render |

---

## 🌐 Demo 網站（自動部署）
https://autotest-deploy.onrender.com/
使用 Render 免費服務部署 Flask Web，支援註冊 / 登入功能與驗證

---

## 🧪 測試技術（pytest）
- 使用 `pytest.mark.parametrize` 搭配 `JSON` 測資自動化測試輸入行為
- 自訂 `conftest.py` 實作瀏覽器啟動（chrome/firefox）
- 自動化失敗時截圖功能 `use_try(...)`
- 每日自動產出 Allure 測試報告

---

## ⚙️ CI/CD 流程
1. Push 到 Repo A（main 分支）
2. 執行 pytest + Allure + Coverage 測試（CI）
3. 測試成功時，自動將 Web 檔案（`app.py`、`templates/`、`requirements.txt`）推送到 Repo B（CD）
4. Repo B 包含 `render.yaml`，Render 偵測後自動重新部署網站

---

## 🧰 使用技術
- Python 3.13
- Flask
- Selenium + pytest
- PostgreSQL
- GitHub Actions
- Render (雲端部署)

---

## 🗂️ 目錄結構（Repo A）
.
├── app.py                   # Flask 應用主程式
├── templates/testweb.html   # 網頁 HTML 前端
├── tests/                   # 自動化測試腳本
├── scr/                     # 測試封裝邏輯（Page Object）
├── json/                    # 測試用資料集（JSON）
├── requirements.txt
├── .github/workflows/
│   ├── python-ci.yml        # CI 測試流程
│   └── deploy-to-repo-b.yml # 測試成功後自動同步到 Repo B
└──（render.yaml 僅存在於 Repo B）

Report link:
https://dave-weiwei.github.io/Practice/allure/chrome/index.html
https://dave-weiwei.github.io/Practice/allure/firefox/index.html

作者：[@Dave-weiwei](https://github.com/Dave-weiwei)