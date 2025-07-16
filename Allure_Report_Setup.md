# ✅ Allure 測試報告安裝

## 一、安裝 Python 套件

請在命令列輸入以下指令：
pip install pytest selenium allure-pytest webdriver-manager flask pymysql

---

## 二、安裝 Java（Allure CLI 執行需要 Java）

### 方式一：使用 Scoop 安裝 Java（推薦）

1. 安裝 Scoop  
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser  
   irm get.scoop.sh | iex

2. 加入 Java bucket  
   scoop bucket add java

3. 安裝 openjdk17  
   scoop install openjdk17

4. 驗證 Java 安裝  
   java -version

---

## 三、安裝 Allure CLI

scoop install allure  
allure --version

---

## 四、執行測試並產生 Allure 報告

1. 產生測試結果資料  
   pytest tests --alluredir=allure-results

2. 啟動本地報告伺服器  
   allure serve allure-results

---

## 五、加入測試截圖到報告（可選）

在測試失敗時插入以下程式碼：

import allure  
allure.attach.file(file_path, name="失敗截圖", attachment_type=allure.attachment_type.PNG)
