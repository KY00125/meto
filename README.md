メトロノームアプリ
・概要
退屈な基礎練習を少しでも楽しくするためのメトロノームアプリ。
iOS、Androidのスマホおよびタブレットに対応。
楽譜を写真に撮ると自動的に各種設定を反映。
ロングトーンやタンギングなどのデイリータスクを提供し、練習のモチベーションを向上させる。

・技術要件
言語：python
フレームワーク: kivy
パフォーマンス要件:
アプリ起動時間は3秒以内。
OCR処理は5秒以内で完了。
メトロノームのテンポ変更や設定変更はリアルタイムで反映。
サウンド再生の遅延は50ms以下。
・機能要件
1. 通常のメトロノーム機能
表示:
針とおもりのアニメーション。
チューニング用の音程表示（440Hz～442Hz）。
選択要素:
リズム（4分音符、8分音符、16分音符など）。
テンポ（40～240 BPM）。
ビート（2拍子、3拍子、4拍子など）。
ボリューム調整。
周波数設定（440Hz～442Hz）。
2. 特異要素
表示の変更:
カラー変更（テーマカラーの選択）。
表現変更（クラシックデザイン、モダンデザインなど）。
サウンド:
和音を鳴らせない楽器: ハイハット、電子音、拍子木、ベース、和太鼓。
和音を鳴らせる楽器: ギター、ピアノ。
設定の簡易化:
楽譜の写真からOCRで情報を抽出し、テンポやリズムなどの設定に反映。
抽出された値は手動で修正や変更可能。
3. デイリータスク
基礎練習内容をデイリータスクとしてクエスト化:
ロングトーン、タンギング、スケール練習などをリスト化。
練習完了時に達成感を得られるUI（進捗バーや達成通知）。
練習履歴を記録し、過去の進捗を確認可能。
4. 広告表示
無料版では広告を表示。
サブスクリプションプラン（月額/年額）または買い切りプランで広告非表示。
・追加機能案
ソーシャル機能:
他のユーザーと練習進捗を共有。
練習ランキングやグループ機能。
ダークモード対応:
夜間練習時に目に優しい表示モード。
カスタムサウンド:
ユーザーが独自のサウンドをアップロードして使用可能。
練習リマインダー:
指定した時間に練習を促す通知機能。
・開発スケジュール案
フェーズ1: 基本メトロノーム機能の実装（3ヶ月）。
フェーズ2: OCR機能とデイリータスク機能の追加（2ヶ月）。
フェーズ3: 広告表示とサブスクリプション機能の実装（1ヶ月）。
フェーズ4: UI/UXの改善と追加機能（2ヶ月）。
