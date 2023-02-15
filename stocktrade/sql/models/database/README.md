# テーブル定義

## 会社のマスタ・概要など
### 上場企業一覧テーブル(m_symbol)
そもそもどの企業の銘柄コードが取得できるのかという情報を保持する。<br>
EDINETからCSVを取得し、そのCSVからDBを更新する予定。
|Column     |Explanation |Type         |Option     |
|-----------|------------|-------------|-----------|
|SymbolID   |銘柄コード   |Int          |null: false|
|isDeleted  |削除フラグ   |Bool         |null: false|
|CreatedTime|作成日       |DateTime    |null: false|
|UpdatedTime|更新日       |DateTime    |null: false|

### 会社のマスタ情報(m_company)
* 下記のいずれかの方法により取得
    1. 株コムのAPIを実行する
    2. オンライン四季報をスクレイピング

|Column     |Explanation |Type         |Option     |
|-----------|------------|-------------|-----------|
|SymbolID   |銘柄コード   |Int          |null: false|
|isDeleted  |削除フラグ   |Bool         |null: false|
|CreatedTime|作成日       |DateTime    |null: false|
|UpdatedTime|更新日       |DateTime    |null: false|

### 企業の業績(t_company_performance)
* 下記のいずれかの方法により取得
    1. 株コムのAPIを実行する
    2. オンライン四季報をスクレイピング

|Column     |Explanation |Type         |Option     |
|-----------|------------|-------------|-----------|
|SymbolID   |銘柄コード   |Int          |null: false|
|isDeleted  |削除フラグ   |Bool         |null: false|
|CreatedTime|作成日       |DateTime    |null: false|
|UpdatedTime|更新日       |DateTime    |null: false|

---

## ファンダメンタル分析した結果の情報
### 優良株(t_excellent_stock)
|Column     |Explanation |Type         |Option     |
|-----------|------------|-------------|-----------|
|SymbolID   |銘柄コード   |Int          |null: false|
|Kind       |優良株の種類 |Int          |1: 成長株, 2: 割安株, 3: 復活株|
|isDeleted  |削除フラグ   |Bool         |null: false|
|CreatedTime|作成日       |DateTime    |null: false|
|UpdatedTime|更新日       |DateTime    |null: false|

---

## 板情報
### 時価情報・板情報
|Column     |Explanation |Type         |Option     |
|-----------|------------|-------------|-----------|
|SymbolID   |銘柄コード   |Int          |null: false|
|isDeleted  |削除フラグ   |Bool         |null: false|
|CreatedTime|作成日       |DateTime    |null: false|
|UpdatedTime|更新日       |DateTime    |null: false|

---

## 個人の口座情報
### 取引余力
|Column     |Explanation |Type         |Option     |
|-----------|------------|-------------|-----------|
|SymbolID   |銘柄コード   |Int          |null: false|
|isDeleted  |削除フラグ   |Bool         |null: false|
|CreatedTime|作成日       |DateTime    |null: false|
|UpdatedTime|更新日       |DateTime    |null: false|

### 保有株(t_holding_stock)
|Column     |Explanation |Type         |Option     |
|-----------|------------|-------------|-----------|
|SymbolID   |銘柄コード   |Int          |null: false|
|Amount     |保有株数     |Int          |null: false|
|BoughtPrice|買ったときの株価|Double     |null: false|
|isDeleted  |削除フラグ   |Bool         |null: false|
|CreatedTime|作成日       |DateTime    |null: false|
|UpdatedTime|更新日       |DateTime    |null: false|

### 売り注文(t_reserve_sell)
|Column     |Explanation |Type         |Option     |
|-----------|------------|-------------|-----------|
|SymbolID   |銘柄コード   |Int          |null: false|
|TradeTime    |取引日       |DateTime    |null: false|
|SoldPrice    |売却価格     |Double      |null: false|
|ProfitLoss   |利確・損切り区分|String    |"利確", "損切り"|
|OCOTradeFlg|OCO注文の有無|Bool          |null: false|
|isDeleted  |削除フラグ   |Bool         |null: false|
|CreatedTime|作成日       |DateTime    |null: false|
|UpdatedTime|更新日       |DateTime    |null: false|

### 売り約定(t_execute_sell)
|Column     |Explanation |Type         |Option     |
|-----------|------------|-------------|-----------|
|SymbolID   |銘柄コード   |Int          |null: false|
|TradeTime    |取引日       |DateTime    |null: false|
|SoldPrice    |売却価格     |Double      |null: false|
|ProfitLoss   |利確・損切り区分|String    |"利確", "損切り"|
|OCOTradeFlg|OCO注文の有無|Bool          |null: false|
|Result     |売買の結果   |Bool          |null: false, default: false|
|isDeleted  |削除フラグ   |Bool         |null: false|
|CreatedTime|作成日       |DateTime    |null: false|
|UpdatedTime|更新日       |DateTime    |null: false|
