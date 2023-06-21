# Flask Docker サンプルアプリケーション

このリポジトリは、FlaskアプリケーションをDockerコンテナ内で実行するためのサンプルです。

## 前提条件

- Dockerがインストールされていること
- Docker Composeがインストールされていること

## 使用方法

1. Dockerコンテナをビルドして実行します:

   ```bash
   docker-compose up --build
アプリケーションは、ポート8080で実行されます。

Webブラウザで http://localhost:8080 にアクセスして、アプリケーションを確認します。

アプリケーションの実行を停止するには、Ctrl + C を押してDockerコンテナを停止します。

追加の設定
ポート番号を変更する場合は、docker-compose.yml ファイルの 8080 を適切なポート番号に変更します。

デバッグモードを有効にする場合は、docker-compose.yml ファイルの FLASK_ENV 環境変数を development に設定します。

その他のカスタム設定や依存関係の変更が必要な場合は、Dockerfileやdocker-compose.ymlファイルを編集します。
