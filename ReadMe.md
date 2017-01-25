# このソフトウェアについて

GitHubのPagenationを仮実装した。

複数ページの回数分だけリクエストし、その結果をまとめたjsonを返す。

# 開発環境

* Windows XP Pro SP3 32bit
    * cmd.exe
* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
    * [dataset](https://github.com/pudo/dataset)
    * [furl](https://github.com/gruns/furl)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

## 必要なデータベースを作成する

* [GitHub.Accounts.Database](https://github.com/ytyaru/GitHub.Accounts.Database.20170107081237765)
    * [GiHubApi.Authorizations.Create](https://github.com/ytyaru/GiHubApi.Authorizations.Create.20170113141429500)
* [GitHub.ApiEndpoint.Database.Create](https://github.com/ytyaru/GitHub.ApiEndpoint.Database.Create.20170124085656531)

## パラメータ設定

`src/Main.py`にある以下の変数や引数を任意に設定する。

```python
username = "github_username"
db_path_account = "C:/GitHub.Accounts.sqlite3"
db_path_api = "C:/GitHub.Apis.sqlite3"

res = g.repo.list(type='all', sort='created', direction='asc', per_page=100)
```

# 実行

```dosbatch
python Main.py
```

# 結果

リポジトリ取得した結果を`src/GiHubApi.Repositories.{username}.json`ファイルに保存する。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
