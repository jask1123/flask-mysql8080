# flask_mysql Docker Compose

このリポジトリは、MyAppアプリケーションをDocker Composeを使用して簡単に実行するための設定ファイルと関連ファイルを含んでいます。

## 必要条件

以下のソフトウェアがローカルマシンにインストールされていることを確認してください:

- Docker
- Docker Compose

## インストールと実行

1. このリポジトリをクローンします:

   ```shell
   git clone https://github.com/jask1123/flask-mysql8080.git
リポジトリのディレクトリに移動します:

    
    cd myapp-docker-compose
Docker Composeを使用してアプリケーションを起動します:


    docker-compose up --build
アプリケーションのコンテナがビルドされ、appサービスがホストの8080ポートにマッピングされます。また、dbサービスがホストの32000ポートにマッピングされます。

ブラウザで http://localhost:8080 にアクセスしてアプリケーションを使用します。

アプリケーションの使用後は、以下のコマンドでコンテナを停止します:


    docker-compose down
カスタマイズ
アプリケーションの設定や環境変数の変更が必要な場合は、docker-compose.ymlファイルを編集してください。

注意:docker-compose.ymlはAppleのARMアーキテクチャ向けに作っています。
それ以外の方は下の項目を削除して使ってください。

      platform: linux/amd64

初期化スクリプトやデータベースの設定の変更が必要な場合は、dbディレクトリ内のファイルを編集してください。