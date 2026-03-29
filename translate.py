#!/usr/bin/env python3
"""
Tower Networking Inc. Japanese Translation Script
Translates the ja.po file from English to Japanese
"""
import re
import sys

INPUT_FILE = r"D:\Program Files (x86)\Steam\steamapps\common\Tower Networking Inc\localizations\ja.po"
EN_FILE = r"D:\Program Files (x86)\Steam\steamapps\common\Tower Networking Inc\localizations\en.po"
OUTPUT_FILE = r"Y:\02_Create\Tower Networking Inc.JapanseseMod\ja.po"

# Translation dictionary: (msgctxt or None, msgid) -> msgstr
# For entries without msgctxt, use None as the key
TRANSLATIONS = {}

def t(msgid, msgstr, ctx=None):
    """Register a translation"""
    TRANSLATIONS[(ctx, msgid)] = msgstr

# ============================================================
# FINANCES
# ============================================================
t("Dolphin Dosh", "ドルフィンローン")
t("Expand your network with this medium sized loan.", "この中規模ローンでネットワークを拡張しましょう。")
t("{loan_title} daily interest", "{loan_title} 日次利息", ctx="accounting_item")
t("{loan_title} disbursement", "{loan_title} 融資実行", ctx="accounting_item")
t("{loan_title} final interest", "{loan_title} 最終利息", ctx="accounting_item")
t("{loan_title} repayment", "{loan_title} 返済", ctx="accounting_item")
t("Shrimpy Savings", "シュリンプローン")
t("Cheap and small loans for your everyday.", "日常のための格安小口ローン。")
t("Whale Wallet", "ホエールウォレット")
t("Big loans for big ambitions.", "大きな野望のための大口ローン。")

# ============================================================
# LINKS / CABLES
# ============================================================
t("link setup: {link_descript}", "リンク設定: {link_descript}", ctx="accounting_item")
t("Copper", "銅線")
t("Fiber", "光ファイバー")
t("basic copper", "基本銅線")
t("basic fiber", "基本光ファイバー")
t("multicore copper", "マルチコア銅線")
t("standard copper", "標準銅線")
t("Yellow", "黄色")
t("Red", "赤")
t("Green", "緑")
t("Blue", "青")
t("Purple", "紫")
t("SC Fiber", "SC光ファイバー")
t("RJ45 Copper", "RJ45銅線")

# ============================================================
# TUTORIAL / DEMO
# ============================================================
t("Tutorial", "チュートリアル")
t("Content1 \nContent2\nContent3\nContent4\nContent5",
  "内容1 \n内容2\n内容3\n内容4\n内容5")
t("Continue", "続ける")
t("Cancel", "キャンセル")

# ============================================================
# ONBOARDING
# ============================================================
t("early-build bonus", "早期建設ボーナス", ctx="accounting_item")
t("New floor onboardings from The Secretariat", "事務局からの新フロアのオンボーディング")

# ============================================================
# PLAYER HOSTINGS
# ============================================================
t("{fqdn} ppu marketing", "{fqdn} 従量課金マーケティング", ctx="accounting_item")
t("income from '{fqdn}'", "'{fqdn}' からの収入", ctx="accounting_item")
t("domain registration '{fqdn}'", "ドメイン登録 '{fqdn}'", ctx="accounting_item")

# ============================================================
# RANDOM EVENTS
# ============================================================
t("{devtitle} auto replacement", "{devtitle} 自動交換", ctx="accounting_item")
t("{devtitle} auto replaced on floor {floor_num}.", "{devtitle} がフロア {floor_num} で自動交換されました。")
t("tenabolt power outage reimbursement", "テナボルト停電補償金", ctx="accounting_item")
t("Unscheduled power outage (Floor {floor_num})", "予定外の停電 (フロア {floor_num})")
t("Dear tower residents,\n\nThe tower is experiencing power failure on floor {floor_num}.\n\nRecovery is expected on {datetime}.\n\nWe are terribly sorry for the inconvenience caused.\n\nTenabolt Power Corporation",
  "タワー住民の皆様へ\n\nフロア {floor_num} にて停電が発生しています。\n\n復旧予定: {datetime}\n\nご不便をおかけし大変申し訳ございません。\n\nテナボルト電力株式会社")
t("Scheduled power outage (Floor {floor_num})", "計画停電 (フロア {floor_num})")
t("Dear tower residents,\n\nThis is a scheduled power maintenance notice for floor {floor_num}.\n\nExpect power outage to start on {start} and end on {end}.\n\nTenabolt Power Corporation",
  "タワー住民の皆様へ\n\nフロア {floor_num} の計画停電のお知らせです。\n\n停電開始: {start}、終了: {end}\n\nテナボルト電力株式会社")
t("Power outage on floor {floor_num}.", "フロア {floor_num} で停電が発生しました。")
t("Power restored on floor {floor_num}.", "フロア {floor_num} の電力が復旧しました。")
t("tenabolt power surge reimbursement", "テナボルト電力サージ補償金", ctx="accounting_item")
t("Power surge alert (Floor {floor_num})", "電力サージ警報 (フロア {floor_num})")
t("Dear tower residents,\n\nReports indicate of an imminent power surge on floor {floor_num} to start on {start} and end on {end}.\n\nEnsure all electrical devices are disconnected on the affected floor or they will be damaged (even if they are on warranty).\n\nTenabolt Power Corporation will not be liable for any asset loss incurred.\n\nTenabolt Power Corporation",
  "タワー住民の皆様へ\n\nフロア {floor_num} にて電力サージが発生する見込みです。開始: {start}、終了: {end}\n\n該当フロアのすべての電気機器を切断してください。切断しない場合、保証期間中であっても損傷します。\n\nテナボルト電力株式会社は発生した資産損失について責任を負いません。\n\nテナボルト電力株式会社")
t("Power surge on floor {floor_num}.", "フロア {floor_num} で電力サージが発生しました。")

# Floor
t("Floor {n}", "フロア {n}")

# Worm events
t("Network worm activity alerts", "ネットワークワーム活動警報")
t("Greetings Tower Admins,\n\t\t\nOur threat intel network shows signs of a network worm on these floors:\n{floors}\n\nInitial forensics report indicates the worm is of signature [u]{worm_signature}[/u], and could begin spreading from the victim's network by {start}.\n\t\n[i]{worm_descript}[/i]\n\nInformation brought to you courtesy of Fortypoint Global",
  "タワー管理者の皆様へ\n\t\t\n脅威インテリジェンスにより、以下のフロアでネットワークワームの兆候が検出されました:\n{floors}\n\n初期フォレンジック調査の結果、ワームのシグネチャは [u]{worm_signature}[/u] であり、{start} までに被害者のネットワークから拡散を開始する可能性があります。\n\t\n[i]{worm_descript}[/i]\n\nFortypoint Global提供の情報です")
t("{wormsig} spread from victim {username}.", "{wormsig} が被害者 {username} から拡散しました。")
t("{username} successfully contained {wormsig}.", "{username} が {wormsig} の封じ込めに成功しました。")

# ============================================================
# CABLES
# ============================================================
t("RJ45 CAT5, {pxlen} pixels long.", "RJ45 CAT5、長さ {pxlen} ピクセル。")
t("SC double core glass fiber, {pxlen} pixels in length.", "SCダブルコアガラスファイバー、長さ {pxlen} ピクセル。")
t("DC Supply, cable length {pxlen} pixels.", "DC電源、ケーブル長 {pxlen} ピクセル。")
t("Power cable, {pxlen} pixels in length.\n\nAC power plug for various devices.",
  "電源ケーブル、長さ {pxlen} ピクセル。\n\n各種機器用AC電源プラグ。")
t("Audio cable, 200 pixels long", "オーディオケーブル、長さ200ピクセル")
t("HDMI, 1500 pixels long", "HDMI、長さ1500ピクセル")
t("USB C cable, 1000 pixels long", "USB Cケーブル、長さ1000ピクセル")

# ============================================================
# COMPONENTS
# ============================================================
t("When plugged into a powered-on device, the Data Wiper wipes all data on the device. Useful for factory-resetting devices. ",
  "電源が入っている機器に接続すると、データワイパーは機器のすべてのデータを消去します。機器の初期化に便利です。")
t("WIPER", "ワイパー")
t("DATA", "データ")
t('Compatible with SATA3.5"', 'SATA3.5"対応')
t('HDD 3.5" STO: 4', 'HDD 3.5" ストレージ: 4')
t("Provides extra {storage} storage to attached devices.", "接続された機器に追加の {storage} ストレージを提供します。")
t('SATA 3.5"', 'SATA 3.5"')
t("power switch", "電源スイッチ")
t("hdd lock", "HDDロック")

# ============================================================
# CORE / MOBILE OS
# ============================================================
t("Middle-click to slide MobileOS to opposite side.", "中クリックでMobileOSを反対側にスライドします。")
t("Close application", "アプリケーションを閉じる")
t("Close MobileOS", "MobileOSを閉じる")
t("View MobileOS", "MobileOSを表示")
t("Close second monitor", "セカンドモニターを閉じる")
t("View second monitor", "セカンドモニターを表示")

# ============================================================
# ELEVATORS
# ============================================================
t("Cargo count", "貨物数")
t("No cargo", "貨物なし")
t("{n} items", "{n} 個")
t("Delivery Failure Notice", "配送失敗通知")
t("Unable to deliver {product} to floor {floor_num} because there is no space in front of the elevator.\n\nDelivery will be attempted again once the area is cleared.\n\n- SKYLINE deliveries",
  "エレベーター前にスペースがないため、{product} をフロア {floor_num} に配送できません。\n\nエリアが空き次第、再配送を試みます。\n\n- SKYLINE配送")
t("FLOOR 32", "フロア 32")
t("CARGO COUNT\n1", "貨物数\n1")
t("Enter elevator and bring cargo along.", "エレベーターに入り、貨物を持って移動します。")
t("Send cargo only.", "貨物のみ送る。")
t("Press to enter elevator", "クリックしてエレベーターに入る")
t("Call cabin", "キャビンを呼ぶ")
t("Call elevator.", "エレベーターを呼ぶ。")
t("Floor select", "フロア選択")
t("Powered by Skyline Elevators", "Skyline Elevators提供")

# ============================================================
# OUTLETS / LINKS
# ============================================================
t("Unlinked", "未接続")
t("Link state", "リンク状態")
t("Caution", "注意")
t("Linked", "接続済み")

# ============================================================
# GAME WORLD
# ============================================================
t("NO DESCRIPTION FOR WORLD", "ワールドの説明なし")
t("No description for this game world...\n\n", "このゲームワールドの説明はありません...\n\n")
t("It is a work in progress...", "現在開発中です...")
t("Debt Warning", "債務警告")
t("Floor {floor_num} is now built", "フロア {floor_num} が建設されました")
t("Overloaded!", "過負荷！", ctx="warning")
t("initial capital", "初期資本", ctx="accounting_item")
t("Day {n}", "日目 {n}")
t("Daily admin expenses", "日次管理費")
t("hardware auto-replace fee x {n}", "ハードウェア自動交換費用 × {n}")
t("Maximum debt limit reached", "最大債務限度額に到達")
t("FINAL WARNING!\n\nYou have over-drafted your accounts. Settle your debts by today or the finance department will replace your administration.\n\nTogether we build towards new heights.\nBabel Secretariat",
  "最終警告！\n\n口座が超過引き落としされています。本日中に債務を清算してください。さもなければ、財務部門があなたの管理権を剥奪します。\n\n共に新たな高みへ。\nバベル事務局")
t("You have over-drafted your accounts. Settle your debts in {days_left} day(s) time or the finance department will replace your administration.\n\nTogether we build towards new heights.\nBabel Secretariat",
  "口座が超過引き落としされています。{days_left} 日以内に債務を清算してください。さもなければ、財務部門があなたの管理権を剥奪します。\n\n共に新たな高みへ。\nバベル事務局")
t("Game Over: Free Play", "ゲームオーバー: フリープレイ")
t("The game is over. You can still continue playing as this is a free play mode.", "ゲームオーバーです。フリープレイモードなので、引き続きプレイできます。")
t("Liability insurance premium", "賠償責任保険料")
t("SLA violation for user {sla_violated_username}", "ユーザー {sla_violated_username} のSLA違反")
t("Business liability insurance coverage has prevented your dismissal by The Secretariat.\n\t\t\t\nThe adjusted penalty of {penalty} is debited from your accounts.\n\nPlease see that the user {sla_violated_username} has their SLA fulfilled immediately.",
  "事業賠償責任保険により、事務局による解任が回避されました。\n\t\t\t\n調整後の罰金 {penalty} が口座から引き落とされました。\n\nユーザー {sla_violated_username} のSLAを直ちに履行してください。")
t("SLA breach penalty", "SLA違反ペナルティ", ctx="accounting_item")
t("app license ({app_title})", "アプリライセンス ({app_title})", ctx="accounting_item")

# ============================================================
# SCENARIOS
# ============================================================
t("Demo", "デモ")
t("Let's explore the Tower Networking Inc. demo.\n\nAs the days go by, you'll unlock new programs, devices, end-users, and floors (maximum until Floor 5). \n\nThe demo is set to end on day 10, but you can adjust the day period in Advanced Options if you need more time to explore each day.\n\nThe outcome of the demo will vary depending on the network setup:\n\n1. Normal switch setup: The residents' satisfaction might be partially fulfilled due to network traversal limitations within the switch.\n\n2. Advanced router setup: When routing rules and device connections are properly configured, the residents can experience higher satisfaction due to optimal network traversal.\n\nNotes: To explore the demo with minimal setup (no DNS mapping required), without concerns about bandwidth management or electricity costs, enable Easy mode in Difficulty Preset to try our demo.\n\nEnjoy!",
  "Tower Networking Inc.のデモを探索しましょう。\n\n日が経つにつれ、新しいプログラム、デバイス、エンドユーザー、フロア（最大フロア5まで）がアンロックされます。\n\nデモは10日目に終了しますが、各日をもっと探索したい場合は詳細設定で日数を調整できます。\n\nデモの結果はネットワーク構成によって異なります：\n\n1. 通常のスイッチ構成: スイッチ内のネットワーク通信の制約により、住民の満足度が部分的にしか満たされない場合があります。\n\n2. 高度なルーター構成: ルーティングルールとデバイス接続が適切に設定されている場合、最適なネットワーク通信により住民の満足度が高くなります。\n\n注意: 最小限のセットアップ（DNSマッピング不要）で帯域幅管理や電気代を気にせずデモを探索するには、難易度プリセットでイージーモードを有効にしてください。\n\nお楽しみください！")

t("Cable NewsLetter Issue 781", "ケーブルニュースレター 第781号")
t("Greetings cablers around the tall world.\n\nDid you know that you can use a measuring tape to approximate the distance between 2 points?\n\nSimply hold 'T' and move your mouse around.",
  "タワー界のケーブラーの皆さん、こんにちは。\n\n2点間の距離を測定するためにメジャーを使えることをご存知ですか？\n\n'T'キーを押しながらマウスを動かすだけです。")
t("The demo ended on day 10. See you in early access!", "デモは10日目に終了しました。アーリーアクセスでお会いしましょう！")
t("Welcome, Tower Network Admin", "ようこそ、タワーネットワーク管理者")
t("Congratulations on getting appointed as our new tower network administrator.\n\nYour role as the administrator is to ensure all tower tenants (including future ones) has their SLA met. You can check this with the 'Surveyor' on your MobileOS.\n\nWhen a new floor is built, they will be put under your network's jurisdiction. Please ensure the new floor residents/offices has their SLA's met within their allotted grace period.\n\nYou may accept floor builds earlier then their scheduled build times using 'The Secretariat' on MobileOS.\n\nThe finance department will allow up to {max_days_in_debt} day(s) in debt.\n\nShould you fail to meet any financial obligations or breach any tenant SLA, you will be replaced.\n\nTogether we build towards new heights.\nBabel Secretariat",
  "新しいタワーネットワーク管理者への就任おめでとうございます。\n\n管理者としての役割は、すべてのタワーテナント（将来のテナントを含む）のSLAを満たすことです。MobileOSの「サーベイヤー」で確認できます。\n\n新しいフロアが建設されると、あなたのネットワーク管轄下に置かれます。新しいフロアの住民/オフィスのSLAが猶予期間内に満たされるようにしてください。\n\nMobileOSの「事務局」を使って、予定より早くフロアの建設を承認できます。\n\n財務部門は最大 {max_days_in_debt} 日間の債務を許容します。\n\n財務上の義務を果たせなかったり、テナントのSLAに違反した場合、あなたは解任されます。\n\n共に新たな高みへ。\nバベル事務局")

t("Endless Babel", "エンドレスバベル")
t("Run a network for a tower that will randomly spawn floors endlessly. As the days go by, you'll unlock new devices, end-users, programs and face new problems. Your goal is to operate and expand the network for as long as you can.\n\nIf you happen to survive to day 40, a new floor type will be unlocked for subsequent runs.\n\nYou can change the difficulty presets to better suit your play-style, or use the advance game option menu to tweak the game however you want.\n\nEnjoy!",
  "ランダムにフロアが無限に生成されるタワーのネットワークを運営します。日が経つにつれ、新しいデバイス、エンドユーザー、プログラムがアンロックされ、新たな問題に直面します。できるだけ長くネットワークを運営・拡張することが目標です。\n\n40日目まで生き残ると、次回のプレイで新しいフロアタイプがアンロックされます。\n\n難易度プリセットを変更してプレイスタイルに合わせたり、詳細ゲーム設定メニューで自由に調整できます。\n\nお楽しみください！")

t("Interchange Compute Corporation DMarket opening.", "Interchange Compute Corporation のDマーケット出店。")
t("We are pleased to announce the grand opening the ICC store on the DMarket.", "DマーケットへのICCストアのグランドオープンをお知らせいたします。")
t("Cable NewsLetter Issue 500", "ケーブルニュースレター 第500号")
t("Greetings cablers around the tall world.\n\nWe've received reports from Tenabolt corporation that power outages/surges could start occuring in the Tower.\n\nDuring an outage on a floor, the entire floor is without power. Put devices behind UPS to keep them running.\n\nUnplug devices or put them behind a surge protector/UPS to prevent damage to the device during surge events.\n\nYou can get UPS and surge protectors from the licensed Tenabolt merchant on the DMarket.",
  "タワー界のケーブラーの皆さん、こんにちは。\n\nテナボルト社より、タワー内で停電やサージが発生する可能性があるとの報告を受けました。\n\nフロアが停電すると、フロア全体が電力を失います。UPSの背後にデバイスを置いて稼働を維持しましょう。\n\nサージ発生時のデバイス損傷を防ぐため、デバイスを抜くかサージプロテクター/UPSの背後に配置してください。\n\nUPSとサージプロテクターはDマーケットの認定テナボルト販売店で購入できます。")
t("CISO's digest", "CISOダイジェスト")
t("Greetings,\n\t\t\nNew threat intel suggests cyberattacks such as network worms and co-ordinated denial-of-service may start occurring soon.\n\nWe pledge to share information of such activities ahead of time so that you can be prepared.\n\nConsistently ranking in the leaders segment of the prestigious Partner's Magic Circle for network security infrastructure, Fortypoint security offers industry grade firewalls which can help block such attacks.\n\nIf any of your device has been infected by the malware, you can remove the malware program using the \"program\" routine or the \"sftp\" routine.\n\nInformation brought to you courtesy of Fortypoint Global",
  "ご挨拶申し上げます。\n\t\t\n新たな脅威インテリジェンスにより、ネットワークワームや協調型DoS攻撃などのサイバー攻撃がまもなく発生する可能性が示唆されています。\n\n事前に情報を共有し、備えていただけるよう努めます。\n\n名門Partner's Magic Circleのネットワークセキュリティ部門で常にリーダーセグメントにランクインするFortypoint Securityは、このような攻撃をブロックできる業界グレードのファイアウォールを提供しています。\n\nデバイスがマルウェアに感染した場合、「program」ルーチンまたは「sftp」ルーチンでマルウェアプログラムを除去できます。\n\nFortypoint Global提供の情報です")

# Lab
t("Lab", "ラボ")
t("In this sandbox scenario, you can use this space to test device setups, programming, and more, before entering the actual game. ",
  "このサンドボックスシナリオでは、実際のゲームに入る前にデバイスのセットアップやプログラミングなどをテストできます。")

# ============================================================
# TUTORIALS
# ============================================================
t("Basic Game Control", "基本操作")
t("Welcome to tower networking Inc. Tutorial\n\nExpectations:\n\n1. Basic mouse movement.\n1. Connect cables from wall socket to devices.\n2. Turn on/off devices in the current floor.",
  "Tower Networking Inc. チュートリアルへようこそ\n\n学習内容：\n\n1. マウスの基本操作\n1. 壁のコンセントからデバイスへケーブルを接続\n2. 現在のフロアでデバイスの電源オン/オフ")
t("Basic Networking", "ネットワーク基礎")
t("Expectations:\n\n1. Learn how to use the debugger.\n2. Learn network scan commands.\n3. Learn ping/trace commands.",
  "学習内容：\n\n1. デバッガーの使い方を学ぶ\n2. ネットワークスキャンコマンドを学ぶ\n3. ping/traceコマンドを学ぶ")
t("Riser Setup Across Floor", "フロア間ライザー設定")
t("Expectations:\n\n1. Complete the riser connection across different floors.\n2. Use number pad beside elevator to travel between floors.\n\nNote: A riser in networking connects different floors of tower, enabling network communication between them.",
  "学習内容：\n\n1. 異なるフロア間のライザー接続を完了する\n2. エレベーター横のテンキーでフロア間を移動する\n\n注意: ネットワーキングにおけるライザーは、タワーの異なるフロアを接続し、フロア間のネットワーク通信を可能にします。")
t("Online Store Item Purchase", "オンラインストアでのアイテム購入")
t("Expectations:\n\n1. Checkout d-market app.\n2. Checkout credit stack app.\n3. Apply loan.\n\nNote: this tutorial focus more on finances (Purchase and expenses). Don't need to setup the connections.",
  "学習内容：\n\n1. Dマーケットアプリを確認する\n2. クレジットスタックアプリを確認する\n3. ローンを申請する\n\n注意: このチュートリアルは財務（購入と経費）に重点を置いています。接続の設定は不要です。")
t("Basic Domain Name System (DNS)", "基本ドメインネームシステム（DNS）")
t("Expectations:\n\n1. Install and start basic program through netsh.\n2. Learn dns-mapping.",
  "学習内容：\n\n1. netshを通じて基本プログラムをインストール・起動する\n2. DNSマッピングを学ぶ")
t("Router Configuration", "ルーター設定")
t("Expectations:\n\n1. Learn how to use the router.\n2. Learn route commands.\n3. Learn how to designate dns address to user.",
  "学習内容：\n\n1. ルーターの使い方を学ぶ\n2. routeコマンドを学ぶ\n3. ユーザーにDNSアドレスを指定する方法を学ぶ")
t("Rocket Store and Register Domain Name", "ロケットストアとドメイン名の登録")
t("Expectations:\n\n1. Use rocketstore to purchase more apps.\n2. Use registry app to register domain.",
  "学習内容：\n\n1. ロケットストアで追加アプリを購入する\n2. レジストリアプリでドメインを登録する")
t("Certified Tower Networking Admin (CTNA)", "認定タワーネットワーク管理者（CTNA）")
t("Expectations:\n\n1. Apply all tutorial knowledge to experience the actual gameplay flow before entering endless mode",
  "学習内容：\n\n1. エンドレスモードに入る前に、すべてのチュートリアルの知識を活用して実際のゲームプレイを体験する")
t("Firewall Configuration", "ファイアウォール設定")
t("Expectations:\n\n1. Use network tap to inspect traffic passing through a device. (pcap routine)\n2. Use network firewall to filter unwanted traffic (e.g., text-scraping) from malicious users. (firewall routine)\n",
  "学習内容：\n\n1. ネットワークタップを使ってデバイスを通過するトラフィックを検査する（pcapルーチン）\n2. ネットワークファイアウォールを使って悪意のあるユーザーからの不要なトラフィック（テキストスクレイピングなど）をフィルタリングする（firewallルーチン）\n")

# ============================================================
# NETWORK MESSAGES
# ============================================================
t("connection timeout", "接続タイムアウト")
t("bad destination address: {dst}.", "不正な宛先アドレス: {dst}")
t("source bandwidth exhausted.", "送信元の帯域幅が枯渇しました。")
t("source has no network address configured.", "送信元にネットワークアドレスが設定されていません。")
t("no DNS entry configured for '{fqdn}'.", "'{fqdn}' のDNSエントリが設定されていません。")
t("Cannot reach DNS server with broadcasts", "ブロードキャストでDNSサーバーに到達できません")
t("Cannot reach DNS server at {dns_addr}", "DNSサーバー {dns_addr} に到達できません")
t("insufficient storage ({required}/{available}) to install '{prog}' on {dev}.", "'{prog}' を {dev} にインストールするためのストレージが不足しています ({required}/{available})。")
t("insufficient total CPU ({prg_cpu_load}/{total_cpu}) on {dev}.", "{dev} のCPUが不足しています ({prg_cpu_load}/{total_cpu})。")
t("'{prog}' already installed on {dev}.", "'{prog}' は {dev} に既にインストールされています。")
t("'{prog}' installed successfully on {dev}.", "'{prog}' が {dev} に正常にインストールされました。")
t("bypassed", "バイパス済み")
t("permission denied.", "アクセス拒否。")
t("program '{prog}' not installed on {dev}.", "プログラム '{prog}' は {dev} にインストールされていません。")
t("insufficient memory ({required}/{available}) to start '{prog}' on {dev}.", "'{prog}' を {dev} で起動するためのメモリが不足しています ({required}/{available})。")
t("'{prog}' started on {dev}.", "'{prog}' が {dev} で起動しました。")
t("program '{prog}' not running on {dev}.", "プログラム '{prog}' は {dev} で実行されていません。")
t("process '{prog}' stopped on {dev}.", "プロセス '{prog}' が {dev} で停止しました。")
t("programs {prog} successfully uninstalled on {dev}.", "プログラム {prog} が {dev} から正常にアンインストールされました。")
t("no programs installed on {dev}.", "{dev} にプログラムがインストールされていません。")
t("program '{prog}' successfully uninstalled on {dev}.", "プログラム '{prog}' が {dev} から正常にアンインストールされました。")

# DHCP
t("received DHCP error from {dst}: conflict.", "{dst} からDHCPエラーを受信: 競合。")
t("received DHCP options from {dst}.", "{dst} からDHCPオプションを受信しました。")

# File descriptions
t("user file.", "ユーザーファイル。", ctx="file_description")
t("virtual machine.", "仮想マシン。", ctx="file_description")
t("program binary.", "プログラムバイナリ。", ctx="file_description")
t("router config.", "ルーター設定。", ctx="file_description")
t("dhcp server config.", "DHCPサーバー設定。", ctx="file_description")
t("firewall config.", "ファイアウォール設定。", ctx="file_description")
t("dns zone mapping", "DNSゾーンマッピング", ctx="file_description")
t("vlan tag config", "VLANタグ設定", ctx="file_description")
t("data storage.", "データストレージ。", ctx="file_description")

# Network control
t("source is offline.", "送信元がオフラインです。")
t("DHCP address conflict.", "DHCPアドレス競合。", ctx="surveyor_msg")
t("No dhcp servers for auto setup.", "自動設定用のDHCPサーバーがありません。", ctx="surveyor_msg")
t("no DHCP response from any host.", "どのホストからもDHCP応答がありません。")
t("network overload", "ネットワーク過負荷")
t("ttl expired", "TTL期限切れ")

# ============================================================
# PROGRAMS - BASE CLASSES
# ============================================================
t("Production is limited to {factor} compatible uses per device's installed storage.", "生産はデバイスのインストール済みストレージごとに {factor} 互換ユースに制限されます。", ctx="converter_description")
t("Production is limited to {factor} compatible uses per device's installed memory.", "生産はデバイスのインストール済みメモリごとに {factor} 互換ユースに制限されます。", ctx="converter_description")
t("Production is limited to {factor} compatible uses per device's installed CPU.", "生産はデバイスのインストール済みCPUごとに {factor} 互換ユースに制限されます。", ctx="converter_description")
t("Production is limited to {factor} compatible uses on the device's use stack per free memory.", "生産はデバイスの空きメモリごとのユーススタック上で {factor} 互換ユースに制限されます。", ctx="converter_description")
t("Production is limited to {factor} compatible uses on the device's use stack.", "生産はデバイスのユーススタック上で {factor} 互換ユースに制限されます。", ctx="converter_description")
t("At program capacity", "プログラム容量上限")
t("Idling", "アイドリング")
t("Visitor bot ({traffic}) to {dst}", "ビジターボット ({traffic}) → {dst}")
t("Config error", "設定エラー")
t("Insufficient support-bots use to function.", "動作に必要なサポートボットのユースが不足しています。")
t("Successful visit to {dst}.", "{dst} への訪問成功。")
t("Destination is not a user.", "宛先はユーザーではありません。")
t("Failed visit to {dst} because: {reason}.", "{dst} への訪問失敗。理由: {reason}")
t("{n} decentro sold at {p} (arbitrage={f})", "{n} デセントロを {p} で売却 (アービトラージ={f})", ctx="accounting_item")
t("Meter error", "メーターエラー")

# Traversal consume descriptions
t("Produce target's use stack limit is {factor} compatible uses per target's installed storage.", "ターゲットのユーススタック上限はターゲットのインストール済みストレージごとに {factor} 互換ユースです。", ctx="converter_description")
t("Produce target's use stack limit is {factor} compatible uses per target's installed memory.", "ターゲットのユーススタック上限はターゲットのインストール済みメモリごとに {factor} 互換ユースです。", ctx="converter_description")
t("Produce target's use stack limit is {factor} compatible uses per target's installed CPU.", "ターゲットのユーススタック上限はターゲットのインストール済みCPUごとに {factor} 互換ユースです。", ctx="converter_description")
t("Produce target's use stack limit is {factor} compatible uses per target's free memory.", "ターゲットのユーススタック上限はターゲットの空きメモリごとに {factor} 互換ユースです。", ctx="converter_description")
t("Produce target's use stack limit is {factor} compatible uses.", "ターゲットのユーススタック上限は {factor} 互換ユースです。", ctx="converter_description")
t("Skips consuming from destination if produce target's use stack limit is reached.", "ターゲットのユーススタック上限に達した場合、宛先からの消費をスキップします。", ctx="converter_description")
t("insufficient use on dest.", "宛先のユースが不足しています。")
t("This program stores up to {count} '{use_config}' compatible uses per free storage on device. Stored uses persists across device reboots.",
  "このプログラムはデバイスの空きストレージごとに最大 {count} 個の '{use_config}' 互換ユースを保存します。保存されたユースはデバイスの再起動後も維持されます。")

# Surveyor messages
t("No DNS servers for '{dstfqdn}' to '{action}'.", "'{action}' のための '{dstfqdn}' 用DNSサーバーがありません。", ctx="surveyor_msg")
t("No DNS entries for '{dstfqdn}' to '{action}'.", "'{action}' のための '{dstfqdn}' のDNSエントリがありません。", ctx="surveyor_msg")
t("Cannot '{action}' on '{dstfqdn}' ({dstaddr}).", "'{dstfqdn}' ({dstaddr}) で '{action}' を実行できません。", ctx="surveyor_msg")
t("No network address assigned to make requests.", "リクエストを送信するためのネットワークアドレスが割り当てられていません。", ctx="surveyor_msg")
t("network overload?", "ネットワーク過負荷？")
t("any", "任意", ctx="surveyor_msg")
t("any", "任意")  # without context
t("Cannot connect to {dstaddr} for '{action}'. {possible_reasons}", "{dstaddr} に接続できません。アクション: '{action}'。{possible_reasons}", ctx="surveyor_msg")
t("Price-per-use of '{phfqdn}' is too expensive.", "'{phfqdn}' の利用単価が高すぎます。", ctx="surveyor_msg")
t("No suitable providers for '{action}'.", "'{action}' の適切なプロバイダーがありません。", ctx="surveyor_msg")
t("I'd like to {action} on {site_fqdn} by day {nday}.", "{nday} 日目までに {site_fqdn} で {action} したいです。", ctx="surveyor_msg")
t("No acceptable upstream for '{action}'.", "'{action}' の許容可能なアップストリームがありません。", ctx="surveyor_msg")
t("We're in the process of migrating our back-end for '{frontend_fqdn}' to '{new_backend}' in {days_left} days.", "'{frontend_fqdn}' のバックエンドを {days_left} 日後に '{new_backend}' に移行中です。", ctx="surveyor_msg")
t("Our service '{fqdn}' is at {perc} capacity due to issues with '{desc}'.", "サービス '{fqdn}' は '{desc}' の問題により {perc} の容量で稼働中です。", ctx="surveyor_msg")
t("No suitable facilitators for peer-to-peer '{action}'.", "P2P '{action}' の適切なファシリテーターがありません。", ctx="surveyor_msg")
t("No peer for '{action}'.", "'{action}' のピアがありません。", ctx="surveyor_msg")
t("Worm activity", "ワーム活動", ctx="warning")
t("{program} replication", "{program} 複製")
t("We need more proper visitors.", "適切な訪問者がもっと必要です。", ctx="surveyor_msg")

# ============================================================
# PROGRAMS - EARLY ACCESS
# ============================================================
t("enable b2b banking", "B2Bバンキングを有効化")
t("Safe, predictable growth for your money.", "安全で予測可能な資産運用。")
t("High-risk, high-reward investment, or try your luck and win the whole world with us?", "ハイリスク・ハイリターンの投資、それとも運試しで世界を勝ち取りますか？")
t("manage fixed deposit", "定期預金管理")
t("perform b2c banking", "B2Cバンキング実行")
t("high risk gambling", "ハイリスクギャンブル")
t("Analyzes user traffic behavior from a network tap to support botnet operations.\n\n[color=red]Requires access to a network tap with user traffic[/color].",
  "ネットワークタップからユーザーのトラフィック動向を分析し、ボットネット運用を支援します。\n\n[color=red]ユーザートラフィックのあるネットワークタップへのアクセスが必要[/color]。")
t("online instant messaging", "オンラインインスタントメッセージ")
t("talk to someone online", "オンラインで会話する")
t("accept neighbours' task", "近隣住民のタスクを受託")
t("Post small tasks and hire neighbors for help, or earn extra income by accepting tasks to support your tower community.",
  "小さなタスクを投稿して近隣住民にヘルプを依頼するか、タスクを受託してタワーコミュニティを支援しながら追加収入を得ましょう。")
t("request help from others", "他の人にヘルプを依頼")
t("stream media content", "メディアコンテンツをストリーミング")
t("print document", "ドキュメント印刷")
t("store file", "ファイル保存")
t("validate digital payment", "デジタル決済認証")
t("validate premium payment", "プレミアム決済認証")
t("view paid content", "有料コンテンツを閲覧")
t("view private content", "プライベートコンテンツを閲覧")
t("view public content", "パブリックコンテンツを閲覧")

# Databases
t("Primary aggregation data unit. Supports text and image storage.", "プライマリ集約データユニット。テキストと画像のストレージに対応。")
t("Primary aggregation data unit. Supports text, image and audio storage.\n\nImproved disk handling algorithm.",
  "プライマリ集約データユニット。テキスト、画像、オーディオのストレージに対応。\n\nディスク処理アルゴリズムの改善。")
t("Primary aggregation data unit. Supports text, image, audio and video storage.\n\nImproved disk handling algorithm.",
  "プライマリ集約データユニット。テキスト、画像、オーディオ、ビデオのストレージに対応。\n\nディスク処理アルゴリズムの改善。")
t("Based text-based database. Supports text storage usage.", "テキストベースのデータベース。テキストストレージに対応。")

# Decentro
t("Collects decentro currencies over the network and accumulate them on the installed device.", "ネットワーク上のデセントロ通貨を収集し、インストールされたデバイスに蓄積します。")
t("Authenticate Decentro transactions. Decentro peers can connect to this program to perform peer-to-peer transactions. You may only spend decentro currencies that are accessible by decentro nodes.",
  "デセントロ取引を認証します。デセントロピアはこのプログラムに接続してP2P取引を行えます。デセントロノードがアクセス可能なデセントロ通貨のみ使用できます。")
t("send decentro", "デセントロ送信")
t("Safeguards your decentro currencies from power loss or unscheduled shutdown events.", "停電や予期しないシャットダウンからデセントロ通貨を保護します。")
t("decentro currency network facilitator", "デセントロ通貨ネットワークファシリテーター")

# DNS
t("Replies network-addresses to DNS queries. \n[color=red]Requires access to a running text storage program[/color].",
  "DNSクエリにネットワークアドレスを返答します。\n[color=red]稼働中のテキストストレージプログラムへのアクセスが必要[/color]。")
t("Replies network-addresses to DNS queries.", "DNSクエリにネットワークアドレスを返答します。")
t("Enterprise grade DNS server.\n[color=red]Requires access to a running text storage program[/color].",
  "エンタープライズグレードのDNSサーバー。\n[color=red]稼働中のテキストストレージプログラムへのアクセスが必要[/color]。")

# DHCP
t("Automatically assigns network addresses and designated DNS server to network devices.", "ネットワークデバイスにネットワークアドレスと指定DNSサーバーを自動で割り当てます。")
t("Automatically assigns network addresses and designated DNS server to network devices.\n\n[color=red]Requires access to a running text storage program[/color].",
  "ネットワークデバイスにネットワークアドレスと指定DNSサーバーを自動で割り当てます。\n\n[color=red]稼働中のテキストストレージプログラムへのアクセスが必要[/color]。")

# Food delivery
t("accept food delivery", "フードデリバリーを受託")
t("food delivery platform", "フードデリバリープラットフォーム")
t("order any food", "任意の料理を注文")
t("order premium food", "プレミアム料理を注文")
t("post food menu", "フードメニューを投稿")
t("food review platform", "フードレビュープラットフォーム")
t("accept grocery delivery", "食料品配達を受託")
t("grocery and food delivery", "食料品・フードデリバリー")
t("order grocery delivery", "食料品配達を注文")
t("post grocery menu", "食料品メニューを投稿")
t("read or post grocery review", "食料品レビューを読む・投稿する")

# Media
t("host ideological advertisement", "思想広告をホスト")
t("post ideological advertisement", "思想広告を投稿")
t("host animation platform", "アニメーションプラットフォームをホスト")
t("post any animation", "アニメーションを投稿")
t("visit religious forum", "宗教フォーラムを閲覧")
t("share viral memes", "バイラルミームを共有")
t("aggregated forum social media", "集約型フォーラムSNS")
t("host image and text post", "画像・テキスト投稿をホスト")
t("host private forum", "プライベートフォーラムをホスト")
t("visit professional forum", "プロフェッショナルフォーラムを閲覧")
t("host private ethical hacking workshop", "プライベートエシカルハッキングワークショップをホスト")
t("join hacking workshop", "ハッキングワークショップに参加")
t("host movie platform", "動画プラットフォームをホスト")
t("We're seeing illegal downloads on our video contents over traffic {traffic_class}.", "トラフィック {traffic_class} で動画コンテンツの不正ダウンロードを検出しています。")
t("pirating movie content", "動画コンテンツの海賊行為")
t("post any movie", "動画を投稿")
t("stream any movie", "動画をストリーミング")
t("host lofi music channel", "Lofiミュージックチャンネルをホスト")
t("free music site", "無料音楽サイト")
t("post any music", "音楽を投稿")
t("stream any music", "音楽をストリーミング")
t("host podcast platform", "ポッドキャストプラットフォームをホスト")
t("stream any podcast", "ポッドキャストをストリーミング")
t("browse social media", "SNSを閲覧")
t("browse video post", "動画投稿を閲覧")
t("let's explore our additive streaming site to brighten your day.", "あなたの一日を彩るストリーミングサイトを探索しましょう。")
t("social media platform", "SNSプラットフォーム")
t("a media platform", "メディアプラットフォーム")

# Misc programs
t("DNS load test software.", "DNS負荷テストソフトウェア。")
t("Generic program.", "汎用プログラム。")
t("Remote debugger.", "リモートデバッガー。")
t("Power meter firmware.", "電力メーターファームウェア。")
t("Network switch firmware.", "ネットワークスイッチファームウェア。")
t("Firewall operating system; performs packet filtering.", "ファイアウォールOS。パケットフィルタリングを実行します。")
t("HA-enabled port grouping kernel.", "HA対応ポートグルーピングカーネル。")
t("Riser switch firmware.", "ライザースイッチファームウェア。")
t("Round-robin network load balancer.", "ラウンドロビンネットワークロードバランサー。")
t("Managed switch firmware.", "マネージドスイッチファームウェア。")
t("Packet routing program.", "パケットルーティングプログラム。")
t("Packet routing with VLAN subinterfaces.", "VLANサブインターフェース付きパケットルーティング。")
t("Packet monitoring system.", "パケット監視システム。")
t("Support printing services.\n\nAllows printer to be connected to produce print-text and print-image uses.",
  "印刷サービスに対応。\n\nプリンターを接続してprint-textおよびprint-imageユースを生成できます。")
t("printer firmware.", "プリンターファームウェア。")
t("VOIP phone firmware.", "VoIP電話ファームウェア。")
t("Supports Voice over Internet Protocol for streaming voice messages phones.\n\nAllows voip phones to be connected to produce stream-voice uses.",
  "音声メッセージのストリーミング用VoIPに対応。\n\nVoIP電話を接続してstream-voiceユースを生成できます。")

# Work/Hosting
t("host exclusive software services for business or personal use", "ビジネスまたは個人向けの独占ソフトウェアサービスをホスト")
t("buy intertower goods", "タワー間商品を購入")
t("visit external tower", "外部タワーを訪問")
t("host gambling platform", "ギャンブルプラットフォームをホスト")
t("host game posting and playing", "ゲーム投稿・プレイをホスト")
t("publish game storepage", "ゲームストアページを公開")
t("purchase any game", "ゲームを購入")
t("track, manage, and optimize the clients' product inventory at a small fee", "少額の手数料でクライアントの商品在庫を追跡・管理・最適化")
t("inventory management", "在庫管理")
t("join our comprehensive online university platform offering accredited degree programs and professional courses with flexible scheduling, expert faculty, and interactive learning experiences designed for working professionals and students.",
  "柔軟なスケジュール設定、専門教員、社会人・学生向けのインタラクティブな学習体験を備えた、認定学位プログラムとプロフェッショナルコースを提供するオンライン大学プラットフォームにご参加ください。")
t("purchase any online course", "オンラインコースを購入")
t("upload lecture video", "講義動画をアップロード")
t("medical consultation site", "オンライン医療相談サイト")
t("post medical consultation", "医療相談を投稿")
t("visit doctor online", "オンラインで医師に相談")
t("access a managed database without the need to set up physical hardware or manage database software.", "物理ハードウェアの設定やデータベースソフトウェアの管理なしでマネージドデータベースにアクセス。")
t("subscribe database service", "データベースサービスを契約")
t("host e-commerce site", "ECサイトをホスト")
t("host online merchant", "オンラインショップをホスト")
t("publish store page", "ストアページを公開")
t("purchase any supplies", "日用品を購入")
t("metro ticket selling platform", "メトロチケット販売プラットフォーム")
t("offer unbeatable travel packages to the public with the most affordable rates and exclusive deals - book now before these limited-time offers expire!",
  "最もお手頃な料金と限定特典で、お客様に最高のツアーパッケージを提供します。期間限定オファーが終了する前にご予約ください！")
t("purchase travel package", "ツアーパッケージを購入")
t("pay commercial utilities", "商業用公共料金を支払う")
t("pay residential utilities", "住宅用公共料金を支払う")
t("release antivirus software update", "アンチウイルスソフトウェアアップデートをリリース")
t("release privacy software update", "プライバシーソフトウェアアップデートをリリース")
t("open-source software repository. Supports software-updates requests.", "オープンソースソフトウェアリポジトリ。ソフトウェアアップデートリクエストに対応。")
t("antivirus software updates", "アンチウイルスソフトウェアアップデート")
t("software updates", "ソフトウェアアップデート")
t("host file storage", "ファイルストレージをホスト")
t("file transfer site", "ファイル転送サイト")
t("store file on cloud", "クラウドにファイルを保存")
t("transfer and store any file", "ファイルの転送と保存")

# Surveillance
t("cctv camera firmware", "CCTVカメラファームウェア")
t("Support surveillance monitoring services.\n\nAllows surveillance accessories to be connected to produce stream-live-video uses.",
  "監視モニタリングサービスに対応。\n\n監視アクセサリーを接続してstream-live-videoユースを生成できます。")
t("we need to monitor CCTV footage through a physical connection.", "物理接続を通じてCCTV映像を監視する必要があります。")
t("stream cctv footages", "CCTV映像をストリーミング")

# Text-based
t("join our community and start posting your blog today.", "コミュニティに参加して、今日からブログを投稿しましょう。")
t("post any blog post", "ブログ記事を投稿")
t(" join our community and start sharing your favourite books today.", "コミュニティに参加して、お気に入りの本を今日から共有しましょう。")
t("share any book", "本を共有")
t("a simple text-based forum", "シンプルなテキストベースフォーラム")
t("read and comment", "読む・コメントする")
t("Our text content is being scraped over {traffic_class}.", "テキストコンテンツが {traffic_class} を通じてスクレイピングされています。")
t("text scraping", "テキストスクレイピング")
t("experience enhanced project efficiency with our premium business kanban service - invite your team and organization to streamline project management with advanced features and professional collaboration tools.",
  "プレミアムビジネスカンバンサービスでプロジェクト効率を向上させましょう。高度な機能とプロフェッショナルなコラボレーションツールでプロジェクト管理を合理化するために、チームや組織を招待してください。")
t("do project planning", "プロジェクト計画を行う")
t("use business kanban", "ビジネスカンバンを使用")
t("Provides exchange email usages to users.", "ユーザーにExchangeメール機能を提供します。")
t("let's read incoming messages and compose responses when necessary.", "受信メッセージを読み、必要に応じて返信を作成しましょう。")
t("exchange email", "Eメール交換")
t("read any announcement", "お知らせを読む")
t("news posting site", "ニュース投稿サイト")
t("host news site", "ニュースサイトをホスト")
t("post any news", "ニュースを投稿")
t("read any news", "ニュースを読む")
t("read exclusive economical news", "限定経済ニュースを読む")
t("enabling real-time meetings", "リアルタイム会議を実現")
t("attend video meeting", "ビデオ会議に参加")

# Work
t("do work", "仕事をする")
t("do work with vpn", "VPNで仕事をする")
t("do confidential work", "機密業務を行う")
t("host confidential research work", "機密研究業務をホスト")
t("host freelance workspace", "フリーランスワークスペースをホスト")
t("hires professional gamers to broadcast live gameplay and provides viewers with access to watch these live gaming streams.",
  "プロゲーマーを雇用してライブゲームプレイを配信し、視聴者にこれらのライブゲーミングストリームへのアクセスを提供します。")
t("internal workspace which provides hired coders with advanced tools and collaborative environments to create custom software solutions for tower residents.",
  "雇用されたコーダーに高度なツールと協力的な環境を提供し、タワー住民向けのカスタムソフトウェアソリューションを作成する内部ワークスペース。")
t("host scientific research work", "科学研究業務をホスト")

# Worms
t("ANNOYING_MORRIS spreads itself across routers and servers using traffic types ranging from TCP/510 to TCP/519. It doesn't do any harm to its targets but wastes the bandwidth of the devices it traverses.",
  "ANNOYING_MORRISはTCP/510からTCP/519のトラフィックタイプを使用してルーターやサーバーに自己拡散します。ターゲットに害は与えませんが、通過するデバイスの帯域幅を浪費します。")

# ============================================================
# USERS
# ============================================================
t("Hardware refresh ({username})", "ハードウェア更新 ({username})")
t("Greetings network administrator,\n\nFYI, we've just refreshed our network connectivity hardware. \n\nThis means that our hardware address and network address has been reset.\n\nKindly ensure we still have connectivity to the Tower's network.\n\nBest regards\n{username}",
  "ネットワーク管理者様\n\nご連絡いたします。ネットワーク接続ハードウェアを更新しました。\n\nこれにより、ハードウェアアドレスとネットワークアドレスがリセットされました。\n\nタワーのネットワークへの接続性を確保してください。\n\n敬具\n{username}")
t("A tower dweller who just loves to browse media content.", "メディアコンテンツの閲覧が大好きなタワー住民。")
t("browse media content", "メディアコンテンツを閲覧")
t("A humble tower dweller who just wants to go online.", "ただインターネットに接続したい控えめなタワー住民。")
t("read political news", "政治ニュースを読む")
t("A tower dweller who just loves to voice message to their peers.", "仲間へのボイスメッセージが大好きなタワー住民。")
t("A media company that hosts their site on-premise.", "自社サイトをオンプレミスでホスティングするメディア企業。")
t("A news company that hosts their site on-premise.", "自社サイトをオンプレミスでホスティングするニュース企業。")
t("text-based political news site", "テキストベースの政治ニュースサイト")

# User descriptions - tier0
t("A skilled all-rounder who takes on almost every professional work in the tower and somehow nails them all. They stick to the same producer for online service unless there is a better option.",
  "タワーのほぼすべてのプロフェッショナルな仕事をこなし、なぜかすべてうまくやる万能な人材。より良い選択肢がない限り、同じプロデューサーのオンラインサービスを使い続けます。")
t("An individual who seamlessly integrates online activities into their daily routine, easily satisfied as long as they can stay connected.",
  "日常生活にオンライン活動をシームレスに取り入れる個人。接続が維持される限り簡単に満足します。")
t("An individual who briefly checks the latest online content with low network traffic, often browsing headlines from main sites.",
  "低ネットワークトラフィックで最新のオンラインコンテンツを手短にチェックし、主要サイトの見出しを閲覧する個人。")
t("read official news", "公式ニュースを読む")
t("An individual who dedicates time to intentionally seeking spiritual knowledge for deeper religious understanding and personal spiritual growth.",
  "より深い宗教的理解と個人的なスピリチュアルな成長のために、意図的にスピリチュアルな知識を求める個人。")
t("store files", "ファイルを保存")
t("An individual who dedicates time to methodically examining empirical evidence and scientific literature, employing critical thinking and analytical frameworks.",
  "批判的思考と分析的フレームワークを用いて、経験的証拠と科学文献を体系的に検討する個人。")
t("post scientific paper", "科学論文を投稿")
t("do scientific research", "科学研究を行う")
t("An individual who mostly online to socialize, and easily fulfil as long as they can online.", "主にオンラインで社交するために接続し、オンラインでいる限り簡単に満足する個人。")
t("view or post social media", "SNSを閲覧・投稿")
t("An individual who only goes online for basic networking needs, and easily fulfills them as long as they can get online.",
  "基本的なネットワーキングニーズのためだけにオンラインに接続し、接続できれば簡単に満たせる個人。")
t("An individual who intentionally limits online/social media time; perhaps only checks messages at set times.",
  "意図的にオンライン/SNSの時間を制限する個人。決まった時間にのみメッセージを確認することも。")
t("A dedicated homebody who finds joy in the kitchen, constantly experimenting with flavors and sharing favorite recipes with the world.",
  "キッチンに喜びを見出し、常に味を試行錯誤し、お気に入りのレシピを世界と共有する献身的な家庭派。")
t("post food recipe", "料理レシピを投稿")
t("A night owl who seamlessly integrates online activities into their daily routine, easily satisfied as long as they can stay connected.",
  "日常生活にオンライン活動をシームレスに取り入れる夜型の人。接続が維持される限り簡単に満足します。")
t("stream lofi music", "Lofiミュージックをストリーミング")

# Exclusive users
t("An intensely private individual who carefully guards personal information and maintains strict boundaries around their digital footprint.",
  "個人情報を慎重に守り、デジタルフットプリントの境界を厳格に維持する極めてプライバシーを重視する個人。")
t("store surveillance data", "監視データを保存")
t("A software engineer who writes code exclusively for game studio 24/7.", "24時間365日、ゲームスタジオのためだけにコードを書くソフトウェアエンジニア。")
t("do work through vpn", "VPNを通じて仕事をする")
t("An individual who is a passionate conservative activist who continuously shares advertisements with fellow tower residents.",
  "タワーの住民に広告を継続的に共有する熱心な保守派活動家。")
t("An individual who is a passionate liberal activist who continuously shares progressive advertisements, campaigns, and political content with fellow tower residents. They use high-bandwidth connections to distribute their ideology through frequent posting.",
  "タワーの住民に進歩的な広告、キャンペーン、政治的コンテンツを継続的に共有する熱心なリベラル活動家。高帯域接続を使用して頻繁に投稿することでイデオロギーを広めます。")
t("post advertisement", "広告を投稿")
t("An individual who is a passionate capitalistic activist who continuously shares advertisements with fellow tower residents.",
  "タワーの住民に広告を継続的に共有する熱心な資本主義活動家。")
t("A movie director who produces movie content on video subscription platform", "ビデオサブスクプラットフォームで映画コンテンツを制作する映画監督")
t("upload sci-fi movie", "SF映画をアップロード")
t("A audio lover who stream content on audio-streaming subscription platform.", "オーディオストリーミングのサブスクプラットフォームでコンテンツをストリーミングするオーディオ愛好家。")
t("An individual who requires background tasks like large cloud backups, or data processing for their scientific research. They are very passionate to work in research lab.",
  "科学研究のための大規模クラウドバックアップやデータ処理などのバックグラウンドタスクを必要とする個人。研究室での仕事に非常に情熱的です。")

# Low bandwidth users
t("A tech-savvy individual who dedicates their computing resources and time to decentro mining and is a low bandwidth user. ",
  "コンピューティングリソースと時間をデセントロマイニングに捧げる技術に精通した低帯域ユーザー。")
t("A tower dweller who just loves to view food related website and is a low bandwidth user.", "食関連のウェブサイトを閲覧するのが好きな低帯域のタワー住民。")
t("view online recipe", "オンラインレシピを閲覧")
t("A creative and low bandwidth user who regularly publishes detailed reviews about lifestyle products and shares their preferences.",
  "ライフスタイル製品の詳細なレビューを定期的に投稿し、好みを共有する創造的な低帯域ユーザー。")
t("share blog posts", "ブログ記事を共有")
t("A persistent digital salesperson who floods inboxes with unwanted emails.", "不要なメールで受信箱を溢れさせるしつこいデジタルセールスパーソン。")
t("post spam mail", "スパムメールを送信")
t("A low bandwidth tower dweller who just loves to hang out virtually with friends while gaming or just chatting.",
  "ゲームやチャットで仮想的に友人と過ごすのが好きな低帯域のタワー住民。")
t("chat with someone at night", "夜に誰かとチャットする")
t("A low bandwidth tower dweller who just loves to watch pet web content.", "ペットのウェブコンテンツを見るのが大好きな低帯域のタワー住民。")
t("enjoy pet content", "ペットコンテンツを楽しむ")
t("A low bandwidth cost-conscious shopper who purchases secondhand and cheap items to stretch their budget.",
  "予算を節約するために中古品や安い商品を購入するコスト意識の高い低帯域ユーザー。")
t("purchase recycled supplies", "リサイクル用品を購入")
t("A low bandwidth tower dweller who just loves to voice message to their peers.", "仲間へのボイスメッセージが大好きな低帯域のタワー住民。")

# Patient users
t("An individual who requires background tasks like large cloud backups, or data processing for their scientific research. They require high frequency/volume, but tolerant of interruptions as long as it completes eventually.",
  "科学研究のための大規模クラウドバックアップやデータ処理などのバックグラウンドタスクを必要とする個人。高い頻度/ボリュームが必要ですが、最終的に完了すれば中断に寛容です。")
t("process scientific papers", "科学論文を処理")
t("store backup files", "バックアップファイルを保存")

# Workers
t("A skilled all-rounder who takes on almost every professional work in the tower and somehow nails them all.",
  "タワーのほぼすべてのプロフェッショナルな仕事をこなし、なぜかすべてうまくやる万能な人材。")
t("A freelance skilled all-rounder who takes on almost every job in the tower and somehow nails them all.",
  "タワーのほぼすべての仕事をこなし、なぜかすべてうまくやるフリーランスの万能な人材。")
t("do freelance work", "フリーランスの仕事をする")
t("A tower dweller who helps their neighbors with different tasks when they have free time.", "空き時間に近隣住民のさまざまなタスクを手伝うタワー住民。")
t("An investor who spreads investments across multiple asset classes and markets while maintaining a successful professional career.",
  "成功したプロフェッショナルキャリアを維持しながら、複数の資産クラスと市場に分散投資する投資家。")
t("do risky investment", "リスキーな投資を行う")

# Critical uptime users
t("A dedicated viewer who maintains near-constant streaming activity throughout the day, prioritizing connection stability to ensure uninterrupted enjoyment of movies and digital content.",
  "一日中ほぼ絶え間なくストリーミング活動を維持し、映画やデジタルコンテンツの中断のない楽しみを確保するために接続の安定性を優先する熱心な視聴者。")
t("do remote support", "リモートサポートを行う")
t("An individual heavily reliant on constant, stable connection for work or critical services, but not necessarily using massive bandwidth constantly.",
  "仕事や重要なサービスのために常時安定した接続に大きく依存するが、必ずしも常に大量の帯域幅を使用するわけではない個人。")

# Greedy users
t("A greedy individual who seamlessly integrates online activities into their daily routine.", "日常生活にオンライン活動をシームレスに取り入れる貪欲な個人。")
t("A greedy individual who hunts for the next big win and places bets on everything from sports to random events.",
  "次の大勝利を狙い、スポーツからランダムイベントまであらゆるものに賭ける貪欲な個人。")
t("An individual who never deletes digital files. Takes tons of photos/videos, archives everything. ",
  "デジタルファイルを決して削除しない個人。大量の写真/動画を撮影し、すべてをアーカイブします。")
t("Someone who only goes for the best and always chooses luxury services", "常に最高のものを求め、常にラグジュアリーなサービスを選ぶ人")
t("stream scientific media", "科学メディアをストリーミング")
t("A greedy individual who rarely leaves the apartment, relies heavily on the internet for entertainment and essentials.",
  "アパートをほとんど出ず、娯楽と生活必需品をインターネットに大きく依存する貪欲な個人。")
t("store favourite movies", "お気に入りの映画を保存")
t("A greedy individual who always has the latest technology gadgets. Immediately tries new high-bandwidth services and applications.",
  "常に最新のテクノロジーガジェットを持つ貪欲な個人。新しい高帯域サービスやアプリケーションをすぐに試します。")
t("An individual who is obsessed with professional development and online certifications. Their require high bandwidth regularly as they stream lectures, download course materials, and participate in virtual workshops during day time.",
  "プロフェッショナル開発とオンライン資格に執着する個人。日中に講義をストリーミングし、教材をダウンロードし、バーチャルワークショップに参加するため、定期的に高帯域幅が必要です。")
t("stream lecture", "講義をストリーミング")
t("store lecture content", "講義コンテンツを保存")
t("An individual who attends online classes exclusively in evening hours after work, requiring high bandwidth to stream lectures, download course materials, and participate in virtual workshops during nighttime.",
  "仕事後の夜間にのみオンライン授業に参加し、講義のストリーミング、教材のダウンロード、バーチャルワークショップへの参加のため高帯域幅が必要な個人。")

# Illegal users
t("A 24/7 software engineer who requires high bandwidth for both continuous coding work and heavy personal internet usage.",
  "継続的なコーディング作業と大量の個人的なインターネット使用の両方に高帯域幅を必要とする24時間働くソフトウェアエンジニア。")
t("A cost-conscious consumer who actively seeks out free services, discounts, and budget options while being reluctant to spend on premium features.",
  "無料サービス、割引、格安オプションを積極的に探し、プレミアム機能への支出には消極的なコスト意識の高い消費者。")
t("order cheap food", "安い料理を注文")
t("purchase cheap supplies", "安い日用品を購入")
t("view free-tier content", "無料枠のコンテンツを閲覧")

# IXP
t("Internet exchange points are neighbouring buildings that exchange services with the current tower.", "インターネットエクスチェンジポイントは、現在のタワーとサービスを交換する近隣ビルです。")
t("talk to business partner", "ビジネスパートナーと会話する")
t("Step outside the tower. Your only portal to global travel, international goods, and the world beyond!", "タワーの外へ出ましょう。グローバルな旅行、国際商品、そしてその先の世界への唯一のポータルです！")

# ============================================================
# SLA WARNINGS
# ============================================================
t("SLA Warning: {user}", "SLA警告: {user}")
t("{username} is experiencing satisfaction below SLA.\n\nSLA breach will occur in {seconds_left} seconds if their satiety is not raised to {min_satiety_level}.\n\nA SLA breach will caused you to lose your position as the Tower's network admin.\n\nTogether we build towards new heights.\nBabel Secretariat",
  "{username} の満足度がSLAを下回っています。\n\n{seconds_left} 秒以内に満足度が {min_satiety_level} まで上がらない場合、SLA違反が発生します。\n\nSLA違反が発生すると、タワーのネットワーク管理者の地位を失います。\n\n共に新たな高みへ。\nバベル事務局")
t("Multiple SLA Warnings", "複数のSLA警告")
t("Multiple users with impending SLA breaches.\n\nLocate these users on the surveyor using the 'Only show SLA-breaching users' filter.\n\nIf connectivity is not restored to all of them, you will lose your position as the Tower's network admin.\n\nTogether we build towards new heights.\nBabel Secretariat",
  "SLA違反が差し迫っているユーザーが複数います。\n\nサーベイヤーの「SLA違反ユーザーのみ表示」フィルターでこれらのユーザーを特定してください。\n\n全員の接続が復旧しない場合、タワーのネットワーク管理者の地位を失います。\n\n共に新たな高みへ。\nバベル事務局")

# ============================================================
# LOCATIONS
# ============================================================
t("floor {floor_num} power theft", "フロア {floor_num} 電力窃盗")
t("floor {floor_num} power bill", "フロア {floor_num} 電気代", ctx="accounting_item")
t("easy mode waiver", "イージーモード免除", ctx="accounting_item")
t("floor {floor_num} network fee payment", "フロア {floor_num} ネットワーク利用料金")

# ============================================================
# UI - MENUS
# ============================================================
t("Quit", "終了")
t("Confirm", "確認")
t("Price", "価格")
t("Place", "配置")
t("Install", "インストール")
t("Remove", "削除")
t("Refresh", "更新")
t("Submit order", "注文を確定")
t("Checkout", "会計")
t("Checkout", "会計", ctx="ecommerce")
t("Merchants", "販売店")
t("Merchant", "販売店")
t("Total items", "合計アイテム数")
t("Total cost", "合計金額")
t("Continue browsing", "ブラウジングを続ける")
t("D-Market", "Dマーケット")
t("Sell", "売却")
t("Buy", "購入")
t("Trade", "取引")
t("Execute order", "注文を実行")
t("Color", "色")
t("Add to cart", "カートに追加", ctx="ecommerce")
t("Remove from cart", "カートから削除", ctx="ecommerce")
t("In stock", "在庫あり")
t("Cart", "カート")
t("Variant", "バリアント")
t("Tower Networking Inc.", "Tower Networking Inc.")
t("Nothing in cart", "カートは空です", ctx="ecommerce")
t("Modify cart", "カートを変更", ctx="ecommerce")
t("Order accepted.\n\nitems will be delivered to floor {floor_num}.\n", "注文が受理されました。\n\nアイテムはフロア {floor_num} に配送されます。\n", ctx="ecommerce")
t("Order not accepted.\n\nplease try again.", "注文が受理されませんでした。\n\n再度お試しください。", ctx="ecommerce")
t("Transactions", "取引履歴")
t("Due today", "本日支払い分")
t("Summary", "概要")
t("CreditStack", "CreditStack")
t("Current account balance.", "現在の口座残高。")
t("Account balance", "口座残高")
t("Account balance change at end of day.", "一日の終わりの口座残高変動。")
t("Today's payment due", "本日の支払い予定")
t("No transactions yet.", "取引はまだありません。")
t("Due Today", "本日支払い分")
t("Income", "収入")
t("Interest", "利息", ctx="finance")
t("OPEX", "営業費用", ctx="finance")
t("CAPEX", "設備投資", ctx="finance")
t("Donation", "寄付", ctx="finance")
t("Investment", "投資", ctx="finance")
t("Proposal processing", "提案処理", ctx="finance")
t("Trading", "取引", ctx="finance")
t("Petty", "雑費", ctx="finance")
t("Penalty", "罰金", ctx="finance")
t("Summary for day {n}", "{n} 日目の概要", ctx="finance")
t("Total", "合計")
t("Today", "今日")
t("Select an order type", "注文タイプを選択")
t("No decentro nodes to trade from", "取引可能なデセントロノードがありません")
t("Select a decentro node to trade from", "取引するデセントロノードを選択")
t("{n} decentro bought at {p} (arbitrage={f})", "{n} デセントロを {p} で購入 (アービトラージ={f})", ctx="accounting_item")
t("Sell decentro for total {total} cash", "デセントロを合計 {total} キャッシュで売却")
t("Buy decentro for total {total} cash", "デセントロを合計 {total} キャッシュで購入")
t("Decentrometer", "デセントロメーター")
t("Active nodes", "アクティブノード")
t("Decentro safes", "デセントロセーフ")
t("Decentro exchange", "デセントロ取引所")
t("Total accessible currencies on all nodes", "全ノードのアクセス可能な合計通貨数")
t("Decentro market bid (selling) value", "デセントロ市場の売値 (ビッド)")
t("Decentro market ask (buying) value", "デセントロ市場の買値 (アスク)")
t("Decentro arbitrage fee", "デセントロアービトラージ手数料")
t("Information shown is slightly delayed from actual market data.", "表示される情報は実際の市場データからやや遅延しています。")
t("The logical addresses of this node.", "このノードの論理アドレス。")
t("Address", "アドレス")
t("The total processed p2p-transactions on this node.", "このノードで処理されたP2P取引の合計。")
t("Total processed last tick", "前ティック処理合計")
t("The total stored p2p-currencies on this safe.", "このセーフに保存されたP2P通貨の合計。")
t("Total stored currencies", "保存通貨合計")
t("The number of p2p-currencies accessible by this node.", "このノードがアクセス可能なP2P通貨の数。")
t("Accessible currencies", "アクセス可能な通貨")

# ============================================================
# BARRACKS
# ============================================================
t("Rack/shelf selected.", "ラック/棚を選択しました。")
t("Cost: {cost}", "コスト: {cost}")
t("No rack/shelf selected.", "ラック/棚が選択されていません。")
t("Left click to select.", "左クリックで選択。")
t("Placement blocked.", "配置がブロックされました。")
t("Cannot remove that.", "削除できません。")
t("Please click on a rack to designate removal.", "削除するラックをクリックしてください。")
t("Rack not placed.", "ラックが配置されていません。")
t("floor {num} rack install", "フロア {num} ラック設置", ctx="accounting_item")
t("No rack selected.", "ラックが選択されていません。")
t("rack removal", "ラック撤去", ctx="accounting_item")
t("Install racks/shelvings.", "ラック/棚を設置する。")
t("Remove racks/shelvings.", "ラック/棚を撤去する。")
t("Barracks and sons", "Barracks and Sons")
t("Racks and shelvings, e.s.t. 2048", "ラックと棚、創業2048年")
t("Confirm placement", "配置を確認")
t("Rack selected.", "ラックを選択しました。")
t("Cost: xyz", "コスト: xyz")

# ============================================================
# BREAK TIME
# ============================================================
t("Order a cup of coffee.", "コーヒーを注文する。")
t("Order a cup of tea.", "お茶を注文する。")
t("Order a glass of water.", "水を注文する。")
t("Break Time not available co-op mode", "ブレイクタイムは協力モードでは利用できません")
t("Break Time not available for clients", "ブレイクタイムはクライアントには利用できません")
t("Break Time Deliveries", "ブレイクタイムデリバリー")
t("Enjoy life at your own pace.", "自分のペースで人生を楽しもう。")
t("Can't keep up? \n\nLet's get some strong caffeine in your system. The caffeine so strong you feel time slowing down!",
  "ついていけない？\n\n強力なカフェインを摂取しましょう。時間がスローダウンするほどの強さです！")
t("Order coffee.", "コーヒーを注文。")
t("Feeling bored?\n\nSome calming tea to slow you down... or speed the surrounding up.",
  "退屈ですか？\n\n落ち着くお茶でスローダウン...あるいは周囲をスピードアップ。")
t("Order tea.", "お茶を注文。")
t("Just feeling thirsty? Clear out the coffee and tea effects with water!\n\nKeep away from the servers!",
  "喉が渇いた？水でコーヒーとお茶の効果を打ち消しましょう！\n\nサーバーには近づけないでね！")
t("Order water.", "水を注文。")

# ============================================================
# CAMERA
# ============================================================
t("Successfully sent to us!", "正常に送信されました！")
t("Upload Images to Developer Cloud", "開発者クラウドに画像をアップロード")
t("Camera", "カメラ")
t("QUIT", "終了")
t("Pause time, keep the connection 📷", "時間を止めて、接続を維持 📷")
t("Take Shot", "撮影")
t("Previous Taken Shots:", "撮影済みショット:")
t("Hey there! Sharing these shots to the actual internet (not just in-game)! Everyone can see them! 😊 \n\n(Limit: 3 shots per upload)\n",
  "こんにちは！これらのショットは実際のインターネットに共有されます（ゲーム内だけではありません）！みんなが見られます！😊 \n\n（上限: 1回のアップロードにつき3枚）\n")
t("Upload is only enabled when in-game remote debugger access to consumeable \"store-image,software-as-a-service\" from producer. ",
  "アップロードはゲーム内のリモートデバッガーからプロデューサーの消費可能な「store-image,software-as-a-service」にアクセスできる場合にのみ有効です。")
t("Upload Images to Developers' Cloud", "開発者クラウドに画像をアップロード")

# ============================================================
# AUTOGRAPH
# ============================================================
t("Autograph", "Autograph", ctx="network_graphing_app")
t("Autograph", "Autograph")
t("Autograph configuration", "Autograph設定", ctx="network_graphing_app")
t("Straight", "直線", ctx="network_graphing_app")
t("Angular", "角度付き", ctx="network_graphing_app")
t("Sharp", "シャープ", ctx="network_graphing_app")
t("Top-down (for wide networks)", "トップダウン（広いネットワーク向け）", ctx="network_graphing_app")
t("Left-right (for deep networks)", "左右（深いネットワーク向け）", ctx="network_graphing_app")
t("Disabled", "無効")
t("Enabled", "有効")
t("no accessible remote debuggers, check power?", "アクセス可能なリモートデバッガーがありません。電源を確認してください。")
t("Generated on: {gen_dt}", "生成日時: {gen_dt}")
t("Scanning network", "ネットワークをスキャン中")
t("*", "*")
t("Network graph", "ネットワークグラフ")
t("Configure", "設定")
t("satiety: {satiety_ratio}%", "満足度: {satiety_ratio}%", ctx="user_satiety")
t("device is offline.", "デバイスはオフラインです。")
t("BW usage: {bandwidth_load}%", "帯域使用率: {bandwidth_load}%")
t("Auto-mode enabled", "自動モード有効", ctx="network_graphing_app")
t("Disable auto", "自動モードを無効化", ctx="network_graphing_app")
t("Scan and generate a network graph from the debugger now", "デバッガーからネットワークグラフをスキャンして生成する", ctx="network_graphing_app")
t("Enable auto", "自動モードを有効化", ctx="network_graphing_app")
t("Enable auto", "自動モードを有効化")
t("Autograph Configuration", "Autograph設定")
t("Graph orientation", "グラフの向き")
t("Line mode", "線モード")
t("Remote debugger", "リモートデバッガー")
t("No debugger selected", "デバッガーが選択されていません")
t("Scan and regenerate", "スキャンして再生成")

# ============================================================
# MERCHANTS
# ============================================================
t("At AB compute, we offer a variety of computing devices from different manufacturers at good prices. You need servers? AB compute got you covered.",
  "AB Computeでは、様々なメーカーのコンピューティングデバイスをお手頃価格で提供しています。サーバーが必要ですか？AB Computeにお任せください。")
t("Barracks and son's wheel division.\n\nWe're listing our mobility racks (a.k.a. trolleys) here on the DMarket. Get our app on the Rocketstore for your static shelving needs!",
  "Barracks and SonsのホイールDivision。\n\nモビリティラック（通称トロリー）をDマーケットに出品しています。固定棚のニーズにはロケットストアのアプリをご利用ください！")
t("Blade Networking © offers high quality network switches in the tower. Your one-stop merchant for all your connectivity needs.",
  "Blade Networking © は、タワー内で高品質なネットワークスイッチを提供します。接続に関するすべてのニーズにお応えするワンストップショップです。")
t("Cabler's Union is a nonprofit that runs the Cable NewsLetter. They also conduct research and development to improve the livelihood of cablers around the tall world.",
  "Cabler's Unionはケーブルニュースレターを運営する非営利団体です。タワー界のケーブラーの生活向上のための研究開発も行っています。")
t("Official Conduit Systems DMarket store. Quality routers from the disco series and ether series.",
  "Conduit Systems公式Dマーケットストア。ディスコシリーズとエーテルシリーズの高品質ルーター。")
t("Welcome to Data Liner Corporation DMarket's store. We offer top of the line (pun not intended) media converters and repeaters to transform and extend your physical lines in any way you want it.",
  "Data Liner Corporation Dマーケットストアへようこそ。最高級（ダジャレではありません）のメディアコンバーターとリピーターで、物理回線を自由に変換・延長できます。")
t("Debugging shop.", "デバッグショップ。")
t("{warranty}-day device warranty.", "{warranty}日間のデバイス保証。")
t("No device warranty provided.", "デバイス保証なし。")
t("Original", "オリジナル")
t("Orange", "オレンジ")
t("Grey", "グレー")
t("device purchase ({product_name})", "デバイス購入 ({product_name})", ctx="accounting_item")
t("New products", "新商品")
t("Discontinued products", "廃番商品")
t("DMarket updates - {merch_name}", "Dマーケット更新 - {merch_name}")
t("Consistently ranking in the leaders segment of the prestigious Partner's Magic Circle for network security infrastructure, Fortypoint security offers industry grade network taps and firewalls.\n\nFortypoint security is a subsidiary of Fortypoint global.",
  "名門Partner's Magic Circleのネットワークセキュリティ部門で常にリーダーセグメントにランクインするFortypoint Securityは、業界グレードのネットワークタップとファイアウォールを提供しています。\n\nFortypoint SecurityはFortypoint Globalの子会社です。")
t("Golonys Ltd manages and operates a wide portfolio of IT devices tower-wide.", "Golonys Ltdはタワー全体で幅広いITデバイスポートフォリオを管理・運営しています。")
t("Interchange Compute Corporation (ICC) manufactures the tall world's compute devices, ranging from homelab equipment to enterprise servers. ",
  "Interchange Compute Corporation (ICC) は、ホームラボ機器からエンタープライズサーバーまで、タワー界のコンピューティングデバイスを製造しています。")
t("Your trusted cabling merchant. Get all kinds of network and power cables here at Mr. Cable 👷‍♂️.",
  "信頼のケーブル販売店。ネットワークケーブルから電源ケーブルまで、Mr. Cable 👷‍♂️にお任せください。")
t("Cheap refurbished boxes for sale. No warranties!", "格安整備済みマシン販売中。保証なし！")
t("The Savannah Organization has decades of experience building and manufacturing server equipment. \n\nAs part of the Tower sustanability efforts, 10% of profits made by the organization is donated for wildlife preservation.",
  "Savannah Organizationはサーバー機器の構築・製造において数十年の経験を有しています。\n\nタワーのサステナビリティ活動の一環として、収益の10%を野生動物保護に寄付しています。")
t("Tenabolt authorized distributor. Visit the store to find out more about power extensions, UPS. Everything to keep the lights on.\n\nOur power appliances are certified quality with good warrany coverage.",
  "テナボルト正規販売店。電源延長、UPSなどの詳細はストアでご確認ください。照明を灯し続けるためのすべてがここに。\n\n当社の電源機器は品質認証済みで、充実した保証付きです。")
t("The Server Shoppe is your authorized distributor for Macrohard products.", "The Server ShoppeはMacrohard製品の正規販売店です。")
t("Get real-time insights on your tower's population with monitors built for data display and analysis.", "データ表示と分析のために作られたモニターで、タワーの人口のリアルタイム情報を取得しましょう。")
t("Zodiac Networks is a leading manufacturer of backbone high throughput routers.", "Zodiac Networksは基幹ネットワーク向け高スループットルーターの大手メーカーです。")

# ============================================================
# PLAYER INTERACTIONS
# ============================================================
t("Can't stick there", "そこには貼れません")
t("{player} has joined the game", "{player} がゲームに参加しました")
t("Left click to drag trolley", "左クリックでトロリーをドラッグ")
t("\n", "\n")
t("Network Port", "ネットワークポート")
t("VLAN Tags", "VLANタグ")
t("Hit 't' key to tear this note", "'t'キーでこのメモを破る")
t("Hit 't' key to tear up this box", "'t'キーでこの箱を破る")
t("Outlet", "アウトレット", ctx="socket")
t("Link is [color=green]up[/color]", "リンクは[color=green]アップ[/color]")
t("Link is [color=red]down[/color]", "リンクは[color=red]ダウン[/color]")
t("Malfunction", "故障")
t("Damaged by surge", "サージにより損傷")
t("Powered", "通電中")
t("Suspended", "サスペンド中")
t("Unpowered", "非通電")
t("Hardware Addr", "ハードウェアアドレス")
t("Network Addr", "ネットワークアドレス")
t("DNS Addr", "DNSアドレス")
t("Warranty", "保証")
t("day", "日")
t("No risk", "リスクなし")
t("Expired", "期限切れ")
t("Reliability", "信頼性")
t("unnamed", "名前なし")

# ============================================================
# PROPOSALS
# ============================================================
t("stamp duty", "印紙税", ctx="accounting_item")
t("{outage_perc}% of power outage occurring, {surge_perc}% of power surge occurring. Stamp duty costs {stamp_duty_costs}.",
  "停電発生率 {outage_perc}%、電力サージ発生率 {surge_perc}%。印紙税 {stamp_duty_costs}。")
t("secretariat RFP", "事務局RFP", ctx="accounting_item")
t("Remote backup technology acquisition", "リモートバックアップ技術取得", ctx="accounting_item")
t("Remote Backups", "リモートバックアップ", ctx="proposal_title")
t("3-2-1, let's back it up!", "3-2-1、バックアップしよう！", ctx="proposal_lore")
t("Adds a new \"sftp\" routine to netshell. Allows backup of configs/files on remote devices for price of {cost}.\n\t\nThe routine can also be used to remove malware when regular program uninstalls do not work.",
  "ネットシェルに新しい「sftp」ルーチンを追加します。{cost} でリモートデバイス上の設定/ファイルのバックアップが可能になります。\n\t\nこのルーチンは通常のプログラムアンインストールが機能しない場合のマルウェア除去にも使用できます。")
t("Botnets technology acquisition", "ボットネット技術取得", ctx="accounting_item")
t("Botnets research", "ボットネット研究", ctx="proposal_title")
t("Not enough users?", "ユーザーが足りない？", ctx="proposal_lore")
t("Adds a new \"botconf\" routine to netshell. Allow configuration of bots that can generate visitor traffic to enterprises. Funding costs {cost}.",
  "ネットシェルに新しい「botconf」ルーチンを追加します。企業への訪問トラフィックを生成するボットの設定が可能になります。資金コスト {cost}。")
t("elevator upgrade", "エレベーターアップグレード", ctx="accounting_item")
t("Elevator upgrade", "エレベーターアップグレード", ctx="proposal_title")
t("Faster travels for those emergencies", "緊急時のための高速移動", ctx="proposal_lore")
t("Decrease elevator wait time by {perc}%. Costs {cost}", "エレベーター待ち時間を {perc}% 短縮。コスト {cost}")
t("second monitor installation", "セカンドモニター設置", ctx="accounting_item")
t("Second monitor", "セカンドモニター", ctx="proposal_title")
t("Screen too small?", "画面が小さすぎる？", ctx="proposal_lore")
t("Allows use of a second monitor by pressing right-alt. Costs {cost}", "右Altキーでセカンドモニターを使用可能にします。コスト {cost}")
t("HA technology acquisition", "HA技術取得", ctx="accounting_item")
t("High availability research", "高可用性研究", ctx="proposal_title")
t("HA HA HA, no DR!", "HA HA HA、DRなし！", ctx="proposal_lore")
t("Adds a new \"haconf\" routine to netshell. Allow configuration of high-availability setup on ha-enabled routers. Funding costs {cost}.",
  "ネットシェルに新しい「haconf」ルーチンを追加します。HA対応ルーターでの高可用性設定が可能になります。資金コスト {cost}。")
t("Internet Exchange Point One", "インターネットエクスチェンジポイント1", ctx="proposal_title")
t("Now the whole world had one language and a common speech.", "かつて世界は一つの言語と共通の言葉を持っていた。", ctx="proposal_lore")
t("Request an internet exchange point with another tower. An internet exchange point is a floor with a connection point to another tower. Allowing cross-tower internet pays handsomely but is risky due to the strict SLA requirements.",
  "別のタワーとのインターネットエクスチェンジポイントを要求します。インターネットエクスチェンジポイントは別のタワーへの接続点を持つフロアです。タワー間インターネットは高収益ですが、厳格なSLA要件のためリスクがあります。")
t("Jailbreak installer acquisition", "ジェイルブレイクインストーラー取得", ctx="accounting_item")
t("Jailbreaker", "ジェイルブレイカー", ctx="proposal_title")
t("Hardware liberation day", "ハードウェア解放記念日", ctx="proposal_lore")
t("The \"sftp\" routine can now be used to install programs extracted from devices. Costs {cost}.",
  "「sftp」ルーチンでデバイスから抽出したプログラムをインストールできるようになります。コスト {cost}。")
t("Liability Insurance", "賠償責任保険", ctx="proposal_title")
t("Money solves problems", "お金が問題を解決する", ctx="proposal_lore")
t("SLA breaches no longer ends the game, but comes with a financial penalty of {breach_penalty} per breach. Adds a recurring premium cost of {cost} per day.",
  "SLA違反でゲームオーバーにならなくなりますが、違反ごとに {breach_penalty} の罰金が発生します。1日あたり {cost} の継続的な保険料が追加されます。")
t("software funding '{release_name}'", "ソフトウェア開発資金 '{release_name}'", ctx="accounting_item")
t("Fund the development of the software '{release_name}' at cost of {cost}.\n\n{software_details}",
  "ソフトウェア '{release_name}' の開発に {cost} を資金提供します。\n\n{software_details}")
t("NetOps technology acquisition", "NetOps技術取得", ctx="accounting_item")
t("NetOps Research", "NetOps研究", ctx="proposal_title")
t("Improvise, adapt, overcome", "即興、適応、克服", ctx="proposal_lore")
t("Adds automation utility for managing and monitoring your network for the price of {cost}.\n\nUnlocks the 'cron', 'try' and 'notify' routines on NetShell.",
  "ネットワークの管理・監視用の自動化ユーティリティを {cost} で追加します。\n\nNetShellの「cron」「try」「notify」ルーチンをアンロックします。")
t("New data center", "新データセンター", ctx="proposal_title")
t("It's free (?) real-estate baby!", "タダ（？）の不動産だぜ！", ctx="proposal_lore")
t("Request for a new data center, increases administrative fees by {perc}%.", "新しいデータセンターを要求します。管理費が {perc}% 増加します。")
t("Overvoltage directive", "過電圧指令", ctx="proposal_title")
t("POWER OVERWHELMING!", "パワー・オーバーウェルミング！", ctx="proposal_lore")
t("Power management technology acquisition", "電力管理技術取得", ctx="accounting_item")
t("Power Management Research", "電力管理研究", ctx="proposal_title")
t("Keep bills low and reliability high.", "コストを低く、信頼性を高く。", ctx="proposal_lore")
t("Adds power management utility for managing device power state for the price of {cost}.\n\nUnlocks the 'power' routines on NetShell.",
  "デバイスの電力状態を管理するための電力管理ユーティリティを {cost} で追加します。\n\nNetShellの「power」ルーチンをアンロックします。")
t("restructure administration", "管理体制の再構築", ctx="accounting_item")
t("Lean administration", "リーン管理", ctx="proposal_title")
t("Pain now for gain later", "今の痛みが後の利益に", ctx="proposal_lore")
t("Permanently reduce daily admin expenses by {perc}% at the cost of upfront {upfront} payment",
  "前払い {upfront} のコストで日次管理費を永久に {perc}% 削減します")
t("refurbhut support fund", "RefurbHut支援基金", ctx="accounting_item")
t("Refurbhut investment", "RefurbHut投資", ctx="proposal_title")
t("As long as it works...", "動けばいい...", ctx="proposal_lore")
t("Fund {cost} to support the opening of the RefurbHut merchant, which provides cheap refurbished (no warranty) devices.",
  "{cost} を資金提供してRefurbHut販売店の開店を支援します。格安の整備済み（保証なし）デバイスを提供します。")
t("Route discovery v1 technology acquisition", "ルート探索v1技術取得", ctx="accounting_item")
t("Route Discovery Protocol v1", "ルート探索プロトコル v1", ctx="proposal_title")
t("State of the art in 1988", "1988年の最先端", ctx="proposal_lore")
t("Adds a new \"rip\" routine to netshell. Allow configuration of automated route discoveries on routers for price of {cost}.",
  "ネットシェルに新しい「rip」ルーチンを追加します。ルーター上の自動ルート探索の設定が {cost} で可能になります。")
t("New scanning technology acquisition", "新スキャン技術取得", ctx="accounting_item")
t("Scanning exploit", "スキャンエクスプロイト", ctx="proposal_title")
t("Scanning exploit", "スキャンエクスプロイト")
t("Scans too shall pass.", "スキャンも乗り越えよう。", ctx="proposal_lore")
t("Allows netsh and autograph scans to bypass all router rules for a cost of {cost}.", "netshとAutographのスキャンがすべてのルータールールをバイパスできるようにします。コスト {cost}。")
t("The exploit can be optionally turned on/off.", "このエクスプロイトはオプションでオン/オフ切り替え可能です。")
t("cabler's union support fund", "ケーブラー組合支援基金", ctx="accounting_item")
t("Support the Cabler's Union", "ケーブラー組合を支援", ctx="proposal_title")
t("R&D - Rewire and Distribute equally", "R&D - 配線し直して平等に分配", ctx="proposal_lore")
t("Fund {cost} to support the Cabler's Union, an R&D institute for the benefit of cabling workers. This unlocks more proposals for the Cabler's Union.",
  "{cost} を資金提供してケーブラー組合（ケーブル作業者のためのR&D機関）を支援します。ケーブラー組合のさらなる提案がアンロックされます。")
t("Fund {cost} to support the Cabler's Union, an R&D institute for the benefit of cabling workers. In return, they promise to lobby for cheaper cable prices ({discount_perc}% discounts) from the merchants on the DMarket.",
  "{cost} を資金提供してケーブラー組合を支援します。見返りとして、Dマーケットの販売店からのケーブル価格値下げ（{discount_perc}% 割引）のロビー活動を約束します。")
t("Fund {cost} to support the Cabler's Union, an R&D institute for the benefit of cabling workers. This let's them sell their prototypes on the D-Market.",
  "{cost} を資金提供してケーブラー組合を支援します。これにより、Dマーケットでプロトタイプの販売が可能になります。")
t("fusion plant funding", "核融合プラント資金", ctx="accounting_item")
t("Fusion Plant Funding (Phase {n})", "核融合プラント資金 (フェーズ {n})", ctx="proposal_title")
t("Let's make a Sun.", "太陽を作ろう。", ctx="proposal_lore")
t("Support Tenabolt Corporation's effort in building a fusion power plant by funding {amt}", "テナボルト社の核融合発電所建設を {amt} の資金提供で支援します")
t("Reduce all Data Center power cost by {perc}%", "全データセンターの電力コストを {perc}% 削減")
t("Let's make it brighter.", "もっと明るくしよう。", ctx="proposal_lore")
t("Reduces probability of power outage/surge by {perc}%", "停電/サージの発生確率を {perc}% 低減")
t("Legal retaliation", "法的報復", ctx="proposal_title")
t("Another power outage? See you in court!", "また停電？法廷で会いましょう！", ctx="proposal_lore")
t("Lawyer up against Tenabolt Corporation.\n\nThis proposal eliminates future collaboration with Tenabolt Corporation.\nTenabolt Corporation now pays {value} per outage/surge events.\nAll items sold by Tenabolt reseller is {change_perc}% more expensive.",
  "テナボルト社に対して弁護士を立てます。\n\nこの提案によりテナボルト社との今後の協力が終了します。\nテナボルト社は停電/サージイベントごとに {value} を支払います。\nテナボルト正規販売店の全商品は {change_perc}% 値上がりします。")
t("Lobby against Tenabolt Corporation", "テナボルト社に対するロビー活動", ctx="proposal_title")
t("Power to the people.", "人民に力を。", ctx="proposal_lore")
t("Lobby for new law against Tenabolt Corporation.\n\nThis proposal eliminates future collaboration with Tenabolt Corporation.\nTenabolt Corporation can no longer issue fines against non Data Center power use.\nAll items sold by Tenabolt reseller is {change_perc}% more expensive.",
  "テナボルト社に対する新法のロビー活動を行います。\n\nこの提案によりテナボルト社との今後の協力が終了します。\nテナボルト社はデータセンター以外の電力使用に対して罰金を科せなくなります。\nテナボルト正規販売店の全商品は {change_perc}% 値上がりします。")
t("Undervoltage directive", "低電圧指令", ctx="proposal_title")
t("Better dark than magic smoke", "マジックスモークより暗い方がマシ", ctx="proposal_lore")
t("VM technology acquisition", "VM技術取得", ctx="accounting_item")
t("Virtual machines research", "仮想マシン研究", ctx="proposal_title")
t("carrier has arrived.", "キャリアが到着した。", ctx="proposal_lore")
t("Adds a new \"vmconf\" routine to netshell. Allow configuration of virtual machines on servers. Funding costs {cost}.",
  "ネットシェルに新しい「vmconf」ルーチンを追加します。サーバー上の仮想マシンの設定が可能になります。資金コスト {cost}。")
t("PADU development funding", "PADU開発資金")
t("Everyone's favorite database.", "みんなのお気に入りのデータベース。")
t("Poems DB", "Poems DB")
t("A DB just for the text chads.", "テキスト上級者のためのDB。")
t("Sun DNS", "Sun DNS")
t("We've got names for everyone.", "全員分の名前を用意しました。")
t("KEA DHCP Server", "KEA DHCPサーバー")
t("Mass host configurations, made easy.", "大量ホスト設定を簡単に。")

# ============================================================
# ROCKET STORE / APPS
# ============================================================
t("Rocket Store", "ロケットストア")

# ============================================================
# MISC UI
# ============================================================
t("Press the F1 key to access the in-game wiki", "F1キーでゲーム内Wikiにアクセス")
t("Press 'F8' to provide your feedback to us", "'F8'キーでフィードバックを送信")
t("Wall socket", "壁コンセント")
t("Data Center", "データセンター")
t("Consumers", "消費者")
t("Producer", "プロデューサー")
t("Router", "ルーター")
t("Switch", "スイッチ")
t("Networking 101", "ネットワーク入門")
t("Networking shell (netsh)", "ネットワーキングシェル (netsh)")

# ============================================================
# Many more translations needed - these will be handled by
# a fallback system for remaining entries
# ============================================================

# Now we need many more. Let me add all the remaining ones I've seen.

# Tutorial floor texts
t("Welcome to tower networking Inc. Tutorial\n\nExpectations:\n\n1. Basic mouse movement.\n2. Connect cables from wall socket to devices.\n3. Turn on/off devices in the current floor.",
  "Tower Networking Inc. チュートリアルへようこそ\n\n学習内容：\n\n1. マウスの基本操作\n2. 壁のコンセントからデバイスへケーブルを接続\n3. 現在のフロアでデバイスの電源オン/オフ")
t("Click either 'OK' button or the panel to complete the guide.", "'OK'ボタンまたはパネルをクリックしてガイドを完了します。")
t("Basic Movements", "基本操作")
t("click OK button to continue", "OKボタンをクリックして続行")
t("You can zoom in or zoom out by scrolling mouse wheel.", "マウスホイールでズームイン/ズームアウトできます。")
t("zoom in/out", "ズームイン/ズームアウト")
t("There are three ways to move:\n\nThe first method is to hold the right mouse button to pan and move.",
  "移動方法は3つあります：\n\n1つ目は右マウスボタンを押しながらパンして移動する方法です。")
t("hold right mouse to move", "右マウスボタン長押しで移動")
t("The second method is to hold the middle mouse button while the camera follows the position of the mouse cursor.",
  "2つ目は中マウスボタンを押しながら、カメラがマウスカーソルの位置に追従する方法です。")
t("hold middle mouse to move", "中マウスボタン長押しで移動")
t("The third method is to use WASD to move the camera, and hold Shift to move faster across the area.",
  "3つ目はWASDキーでカメラを移動し、Shiftキーを押しながら高速移動する方法です。")
t("type 'WASD' to move", "WASDキーで移動")
t("Hold the left mouse button to pick up and move objects.", "左マウスボタンを押してオブジェクトを持ち上げて移動します。")
t("pick and move device (debugger)", "デバイス（デバッガー）を掴んで移動")
t('Drag one end of power cable (from wall socket) into socket area of the "Boulder" to power up "Boulder".',
  '壁コンセントからの電源ケーブルの片端を「Boulder」のソケットエリアにドラッグして「Boulder」に電源を入れます。')
t("power up device (Boulder)", "デバイスに電源を入れる（Boulder）")
t("Toggle red switch to turn on Blade5.\n\nObserve the led indicator on the Blade5.",
  "赤いスイッチを切り替えてBlade5をオンにします。\n\nBlade5のLEDインジケーターを確認してください。")
t("toggle red switch on device", "デバイスの赤いスイッチを切り替え")
t('View the previous tutorial steps by clicking on "VIEW TUTORIAL" located on the right side.\n\nClick "CLOSE TUTORIAL" to minimize the tutorial steps panel.',
  '右側にある「チュートリアルを見る」をクリックして前のチュートリアルステップを確認できます。\n\n「チュートリアルを閉じる」をクリックしてチュートリアルパネルを最小化できます。')
t("view tutorial steps", "チュートリアルステップを見る")

# Many many more entries exist. For the remaining ones,
# I'll handle them in the PO file processing.

# Additional common UI elements and game text
t("Datacenter {floor_num} power bill", "データセンター {floor_num} 電気代")
t("Point A", "ポイントA")
t("Point B", "ポイントB")
t("Riser setup", "ライザー設定")
t("Floor 1", "フロア 1")
t("Riser outlet B", "ライザーアウトレットB")
t("Purchase device from app", "アプリからデバイスを購入")
t("Day Night Cycle", "昼夜サイクル")
t("Choose merchant", "販売店を選択")
t("Choose Variant", "バリアントを選択")
t("Add item to cart", "カートにアイテムを追加")
t("Manage finance", "財務管理")
t("Apply for a loan", "ローンを申請")
t("Basic Program Installation", "基本プログラムインストール")
t("Basic domain name system (DNS)", "基本ドメインネームシステム（DNS）")
t("User satiety", "ユーザー満足度")
t("DNS troubleshooting", "DNSトラブルシューティング")
t("Exit tutorial", "チュートリアルを終了")
t("Network routers", "ネットワークルーター")
t("Network routers (Method 1)", "ネットワークルーター（方法1）")
t("Advanced app tutorial", "高度なアプリチュートリアル")
t("Example APP from Rocket store", "ロケットストアのサンプルアプリ")
t("Vocal connector", "ボーカルコネクター")
t("Physical public VOIP phone", "パブリックVoIP電話")
t("Extra apps", "追加アプリ")
t("Network firewall", "ネットワークファイアウォール")
t("Malicious Consumer", "悪意ある消費者")
t("network tap", "ネットワークタップ")
t("network firewall", "ネットワークファイアウォール")
t("firewall 101", "ファイアウォール入門")
t("Final trial 101", "最終試験 101")
t("final trial 101", "最終試験 101")
t("TOWER NEWS LTD.", "TOWER NEWS LTD.")
t("tap your card", "カードをタップ")
t("{nport}-port ethernet load tester.", "{nport}ポート イーサネット負荷テスター。")

# Satisfaction panel / Surveyor items
t("Internet exchange points are neighbouring buildings that exchange services with the current tower.  ", "インターネットエクスチェンジポイントは、現在のタワーとサービスを交換する近隣ビルです。")
t("host memes forum", "ミームフォーラムをホスト")

# More producers
t("A large-scale film production facility that serves as the central hub for animated content.", "アニメーションコンテンツの中心的ハブとして機能する大規模映像制作施設。")
t("A creative production company that specializes in developing and producing animated content.", "アニメーションコンテンツの開発・制作を専門とするクリエイティブプロダクション。")
t("accept vendor contract", "ベンダー契約を受託")
t("host professional forum", "プロフェッショナルフォーラムをホスト")
t("send newsletter", "ニュースレターを送信")
t("customer service", "カスタマーサービス")
t("talk to customers", "顧客と会話する")
t("exchange business email", "ビジネスメールを交換")
t("use database service", "データベースサービスを利用")
t("free kanban platform", "無料カンバンプラットフォーム")
t("publish sci-fi game", "SF ゲームを公開")
t("upload movies to site", "サイトに動画をアップロード")
t("post podcast transcript", "ポッドキャストの原稿を投稿")
t("official news site", "公式ニュースサイト")
t("scientific news site", "科学ニュースサイト")
t("exclusive news site for public.", "一般向け限定ニュースサイト。")
t("promote on portal", "ポータルで宣伝")
t("post news on portal", "ポータルにニュースを投稿")
t("talk to believers", "信者と会話する")
t("purchase office supplies", "事務用品を購入")
t("do confidential research", "機密研究を行う")
t("do chips designing", "チップ設計を行う")
t("do gameplay streaming", "ゲームプレイストリーミングを行う")
t("stream jazz music", "ジャズ音楽をストリーミング")
t("do risky investment", "リスキーな投資を行う")

# ============================================================
# BATCH 2: UI / D-Market / Finance / Settings
# ============================================================

# Power messages
t("Dear tower residents,\n\nThe tower is experiencing power failures on floors {floors}. We are looking into the matter and expect to restore power within {deadline} seconds.\n\nPlease do not panic.\n\nTower Maintenance",
  "タワー住民の皆様へ\n\n現在、フロア {floors} にて停電が発生しております。原因を調査中であり、{deadline} 秒以内に復旧する見込みです。\n\n落ち着いて行動してください。\n\nタワーメンテナンス部門")
t("Dear tower residents,\n\nThis is a scheduled power maintenance on floors {floors} running for the next {deadline} seconds.\n\nPlease use this time to ensure your devices are protected by UPS or Surge Protectors.\n\nTower Maintenance",
  "タワー住民の皆様へ\n\nフロア {floors} にて {deadline} 秒間の計画停電を実施いたします。\n\nこの機会にデバイスがUPSまたはサージプロテクタで保護されていることをご確認ください。\n\nタワーメンテナンス部門")
t("Dear tower residents,\n\nReports indicate of an imminent power surge on floors {floors}. Devices that are unprotected will be damaged.\n\nPlease use this time to ensure your devices are protected by Surge Protectors.\n\nTower Maintenance",
  "タワー住民の皆様へ\n\nフロア {floors} にて電力サージの発生が予測されています。保護されていないデバイスは損傷を受けます。\n\nサージプロテクタでデバイスを保護してください。\n\nタワーメンテナンス部門")

# Cyberattack messages
t("Greetings Tower Admins,\n\t\t\nOur threat intel network shows unusual activity. A cyberattack event may affect your tower within the next {n} days.\n\nEnsure essential devices are protected behind firewalls.\n\t\t\nANON",
  "タワー管理者の皆様へ\n\t\t\n脅威インテリジェンスネットワークにて異常な活動を検知しました。{n} 日以内にサイバー攻撃がタワーに影響を及ぼす可能性があります。\n\n重要なデバイスをファイアウォールで保護してください。\n\t\t\nANON")
t("Greetings,\n\t\t\nNew threat intel suggests cyberattacks such as worms may affect your tower within the next {n} days.\n\nEnsure essential devices are protected behind firewalls.\n\t\t\nANON",
  "皆様へ\n\t\t\n新たな脅威インテリジェンスにより、{n} 日以内にワームなどのサイバー攻撃がタワーに影響する可能性があります。\n\n重要なデバイスをファイアウォールで保護してください。\n\t\t\nANON")

# Cable descriptions
t("Power cable, {pxlen} pixels in length.\n\nAC power plug for powering devices.",
  "電源ケーブル、長さ {pxlen} ピクセル。\n\nデバイスに電力を供給するAC電源プラグ。")
t("Compatible with SATA3.5\"", "SATA3.5\"対応")
t("HDD 3.5\" STO: 4", "HDD 3.5\" ストレージ: 4")
t("SATA 3.5\"", "SATA 3.5\"")

# Delivery / Orders
t("Unable to deliver {product} to floor {floor_num} because the elevator is offline!",
  "エレベーターがオフラインのため、{product} をフロア {floor_num} に配達できません！")
t("CARGO COUNT\n1", "貨物数\n1")
t("Order accepted.\n\nitems will be delivered to floor {floor_num}.",
  "注文を受け付けました。\n\n商品はフロア {floor_num} に配達されます。")
t("Order not accepted.\n\nplease try again.", "注文を受け付けられませんでした。\n\n再度お試しください。")
t("Select delivery location", "配達先を選択")
t("Bulk purchased items will be delivered one at a time to the selected floor.",
  "まとめ買いした商品は選択したフロアに1つずつ配達されます。")

# Game world
t("No description for this game world...\n\n", "このゲームワールドの説明はありません...\n\n")

# Debt warnings
t("FINAL WARNING!\n\nYou have over-drafted your accounts. Settle your debts in {days} days to avoid TERMINATION.",
  "最終警告！\n\n口座が超過引き落としされています。{days} 日以内に借金を清算しないと解雇されます。")
t("You have over-drafted your accounts. Settle your debts in {days} days to avoid escalation.",
  "口座が超過引き落としされています。{days} 日以内に借金を清算してください。")
t("Business liability insurance coverage has prevented your dismissal, but please still settle your debts.\n\nBusiness Liability Insurance will cease coverage after 3 consecutive days.",
  "事業賠償責任保険により解雇は回避されましたが、借金は清算してください。\n\n連続3日後に保険の適用は終了します。")

# D-Market categories
t("Browse", "閲覧")
t("Any", "すべて")
t("Network Cables", "ネットワークケーブル")
t("Power Cables", "電源ケーブル")
t("Network Switches", "ネットワークスイッチ")
t("Network Routers", "ネットワークルーター")
t("Network Firewalls/Taps", "ファイアウォール/タップ")
t("UPS/Surge Protectors", "UPS/サージプロテクタ")
t("Power Expanders", "電源拡張器")
t("Media Converters/Repeaters", "メディアコンバーター/リピーター")
t("Servers", "サーバー")
t("Decentro Rigs", "Decentroリグ")
t("Device Peripherals", "デバイス周辺機器")
t("No devices found...", "デバイスが見つかりません...")
t("Show More Filters", "フィルターを表示")
t("Show Less Filters", "フィルターを隠す")
t("Submit", "送信")
t("Modify", "変更")
t("Order submitted successfully", "注文が正常に送信されました")
t("Items will be delivered to floor {floor_num}.", "商品はフロア {floor_num} に配達されます。")
t("Failed to submit order", "注文の送信に失敗しました")
t("Please try again.", "再度お試しください。")
t("Clear", "クリア")
t("Filter for devices. Maximum 30 results.", "デバイスを検索。最大30件表示。")
t("Search keyword...", "検索キーワード...")
t("Device Type", "デバイスタイプ")
t("Warranty (days)", "保証期間（日）")
t("Traversals / tick", "トラバーサル/tick")
t("CPU", "CPU")
t("Memory", "メモリ")
t("Storage", "ストレージ")
t("Show more filters", "フィルターを表示")
t("Reset Filters", "フィルターをリセット")
t("Max 30 results.", "最大30件。")
t("Search", "検索")
t("Total Items", "合計アイテム数")
t("Total Costs", "合計金額")
t("Dismiss", "閉じる")
t("Show related listings", "関連商品を表示")
t("Back to listings", "商品一覧に戻る")
t("Listed by {merchant}", "{merchant} の出品")
t("YE$", "はい")
t("No", "いいえ")

# Fi$hy Loans
t("No loan sharks available", "ローン業者がいません")
t("No loan offers available", "ローン商品がありません")
t("Confirm loan application?", "ローン申請を確認しますか？")
t("You don't have any loans", "ローンはありません")
t("Confirm repayment?", "返済を確認しますか？")
t("Fi$hy Financing", "Fi$hyファイナンス")
t("What you owe", "借入残高")
t("Interest due today", "本日の利息")
t("Active loans", "アクティブなローン")
t("Back", "戻る")
t("Apply new loan", "新規ローン申請")
t("Yes", "はい")
t("Daily interest cost", "日次利息コスト")
t("Repayment cost", "返済金額")
t("Repay", "返済")
t("Loan principal", "ローン元金")
t("Apply loan", "ローン申請")

# Illusion Browser / Memento
t("EXIT", "終了")
t("Illusion Browser", "イリュージョンブラウザ")
t("Illusion Browser is powered by godot_wry", "イリュージョンブラウザはgodot_wryで動作しています")
t("DNS Entries", "DNSエントリ")
t("NetAddr Assignments", "ネットワークアドレス割当")
t("Device Units", "デバイスユニット")
t("No dns entries configured", "DNSエントリが設定されていません")
t("{domain_name} maps to {addr} (DNS={srvaddr})", "{domain_name} → {addr} (DNS={srvaddr})")
t("{domain_name} maps to {addr}", "{domain_name} → {addr}")
t("No network address assigned", "ネットワークアドレスが割り当てられていません")
t("{networkaddr} assigned to {hardwareaddr}", "{networkaddr} → {hardwareaddr} に割当済")
t("overlaps with", "重複:")
t("No matching device", "一致するデバイスなし")
t("Memento Entries", "メメントエントリ")
t("Momento Entries", "メメントエントリ")
t("Exit", "終了")

# Device management / Memento filters
t("Filter for devices. Max 30 results.", "デバイスを検索。最大30件。")
t("keyword...", "キーワード...")
t("Location", "場所")
t("Asset registration day", "資産登録日")
t("Warranty left (days)", "保証残日数")
t("Reset filters", "フィルターをリセット")
t("Apply filters", "フィルターを適用")
t("Only host may edit device notes.", "ホストのみデバイスノートを編集できます。")
t("Automatic replacement incurs a daily fee of {daily_fee} per device and replaces malfunctioning devices within one day.",
  "自動交換は1デバイスあたり日額 {daily_fee} の手数料がかかり、故障デバイスを1日以内に交換します。")
t("{n} days", "{n} 日")
t("The warranty period remaining on the device.", "デバイスの残り保証期間。")
t("Asset registered on", "資産登録日")
t("The physical location of the device.", "デバイスの物理的な場所。")
t("Asset is currently on", "現在の資産場所")
t("Warranty days left", "保証残日数")
t("The reliability of the device.", "デバイスの信頼性。")
t("Automatically this device if it has malfunction.", "故障時にこのデバイスを自動交換する。")
t("Replace hardware if malfunction", "故障時にハードウェアを交換")
t("Automatic replacement incurs a daily fee of 30 per device and replaces malfunctioning devices within one day.",
  "自動交換は1デバイスあたり日額30の手数料がかかり、故障デバイスを1日以内に交換します。")

# MessageBox
t("MessageBox", "メッセージボックス")
t("Mark all as read", "すべて既読にする")
t("Back to message list", "メッセージ一覧に戻る")

# Netsh terminal
t("welcome to netsh remote terminal debugger.", "netshリモートターミナルデバッガーへようこそ。")
t("input '{man}' for usage manual/help.", "'{man}' と入力してマニュアル/ヘルプを表示。")
t("'{dbg_addr}' set as default debugger.", "'{dbg_addr}' をデフォルトデバッガーに設定。")
t("input + enter to submit command.", "入力 + Enterでコマンドを送信。")
t("cmd interrupt.", "コマンド中断。")
t("recursion depth exceeded.", "再帰の深さを超えました。")
t("unknown routine: '{routine}'.", "不明なルーチン: '{routine}'。")
t("type '{man_cmd}' for usage-manual/help.", "'{man_cmd}' と入力してマニュアル/ヘルプを表示。")
t("pressing UP arrow will cycle previous commands.", "上矢印キーで過去のコマンドを呼び出せます。")
t("pressing ctrl-c will abort action.", "Ctrl+Cでアクションを中止します。")
t("pressing ctrl-d will exit from the terminal.", "Ctrl+Dでターミナルを終了します。")
t("invalid routine: '{routine}'", "無効なルーチン: '{routine}'")
t("user interrupt.", "ユーザー中断。")
t("user quit", "ユーザー終了")
t("netshell", "ネットシェル")
t("remote terminal debugger", "リモートターミナルデバッガー")
t("type 'man' for manual, 'man <routine>' for more", "'man' でマニュアル、'man <ルーチン名>' で詳細を表示")

# The Registry app
t("No usage associated for this domain", "このドメインに関連する利用がありません")
t("This domain provides uses for", "このドメインが提供する利用:")
t("and", "と")
t("On successful consumption, users pay [color=yellow]{ppu}[/color] per use.",
  "消費成功時、ユーザーは1回あたり [color=yellow]{ppu}[/color] を支払います。")
t("It cost [color=yellow]{regcost}[/color] when it was registered.",
  "登録時のコストは [color=yellow]{regcost}[/color] でした。")
t("There were [color=yellow]{n_visit_today}[/color] visits today.",
  "本日の訪問数は [color=yellow]{n_visit_today}[/color] です。")
t("Projected profit today is [color=green]{profit_today}[/color].",
  "本日の見込み利益は [color=green]{profit_today}[/color] です。")
t("Marketing fees for this change: {cost}", "この変更のマーケティング手数料: {cost}")
t("Deregister", "登録解除")
t("Modify PPU", "PPUを変更")
t("Abort", "中止")
t("Take down this domain service.", "このドメインサービスを停止する。")
t("De-register", "登録解除")
t("Modify the pay-per-use of this domain.", "このドメインの従量課金を変更する。")
t("The revenue generated everytime an end user consumes the service.",
  "エンドユーザーがサービスを利用するたびに発生する収益。")
t("Price per consumption", "1回あたりの利用料金")
t("Cost of registration", "登録コスト")
t("( ✅ ) Confirm", "( ✅ ) 確認")
t("( ❗ ) Deregister", "( ❗ ) 登録解除")
t("( ❌ ) Back", "( ❌ ) 戻る")
t("Finalize registration", "登録を確定")
t("Domain de-registration", "ドメイン登録解除")
t("No USE associated, this domain is useless.", "USEが関連付けられていません。このドメインは無用です。")
t("Register the domain.", "ドメインを登録する。")
t("Registered domains", "登録済みドメイン")
t("Back to main menu", "メインメニューに戻る")
t("You don't have any registered domain services", "登録済みのドメインサービスはありません")
t("REGISTERED DOMAINS", "登録済みドメイン")
t("(🔙) Return to Main Menu", "(🔙) メインメニューに戻る")
t("Domain name", "ドメイン名")
t("Register new domain name", "新規ドメイン名を登録")
t("Associate usage", "利用を関連付け")
t("Finalize", "確定")
t("Registration cost", "登録コスト")
t("No valid use spec to configure", "設定可能なUSE仕様がありません")
t("Not available", "利用不可")
t("Invalid domain, valid example: abc.com, ftp.net", "無効なドメイン名。有効例: abc.com, ftp.net")
t("Available", "利用可能")
t("( + ) Associate USE", "( + ) USEを関連付け")
t("( ✓ ) Finalize ", "( ✓ ) 確定")
t("The Registry", "The Registry")
t("View registered domains", "登録済みドメインを表示")
t("Leave The Registry", "The Registryを終了")
t("THE REGISTRY", "THE REGISTRY")
t(" 🌟REGISTER NEW DOMAIN NAME", " 🌟新規ドメイン名を登録")
t("📑 VIEW REGISTERED DOMAINS", "📑 登録済みドメインを表示")
t("🢠 LEAVE THE REGISTRY", "🢠 THE REGISTRYを終了")
t("USE specification.", "USE仕様。")
t("Usage spec.", "利用仕様。")
t("License cost", "ライセンスコスト")

# Rocket Store
t("Acquire launcher", "ランチャーを取得")
t("Already installed.", "インストール済み。")
t("Acquire app license.", "アプリライセンスを取得。")
t("ACQUIRE LAUNCHER", "ランチャーを取得")
t("Rocket Store: Your one-stop app launcher retailer", "Rocket Store: アプリランチャーの総合ストア")
t("The camera app lets you capture stunning photos with ease. \n\nIncluding ability to share to the real-world internet.",
  "カメラアプリで美しい写真を簡単に撮影。\n\n実際のインターネットに共有する機能付き。")
t("Asset and assignments tracking.", "資産と割当の追跡。")
t("Offer's a single pane of glass to see all DNS entries mapping, network address assignment and more.",
  "DNSエントリマッピング、ネットワークアドレス割当などを一画面で確認できます。")
t("Domain name registration.", "ドメイン名登録。")
t("The registry lets you register new domain names and services to earn revenue.",
  "The Registryで新しいドメイン名とサービスを登録して収益を得られます。")
t("Sticky notes.", "付箋メモ。")
t("SticKy PriNtZ", "SticKy PriNtZ")
t("NEEDZ a physical LabeL? Nothing is as TRUSTworthy as our SticKy PriNtZ.",
  "物理ラベルが必要？SticKy PriNtZほど信頼できるものはありません。")
t("Rack installations.", "ラック設置。")
t("Barracks and sons racking and shelving company app.\n\nFor all your rack and mount needs.",
  "Barracks and Sonsラック＆棚アプリ。\n\nラックとマウントのことなら何でも。")
t("Music player.", "音楽プレーヤー。")
t("SynthAmp", "SynthAmp")
t("A tribute to the all time Llama whipping music player.", "伝説のLlama音楽プレーヤーへのオマージュ。")
t("Network graph viewer.", "ネットワークグラフビューアー。")
t("Creates network graphs from debugger scans.", "デバッガースキャンからネットワークグラフを作成。")
t("Decentro manager.", "Decentroマネージャー。")
t("Manage your decentro currencies.", "Decentro通貨を管理。")
t("Socket installation.", "ソケット設置。")
t("Socketeer", "Socketeer")
t("Socket outlet maker application.\n\nSimple sockets for every occasion.",
  "ソケットアウトレットメーカーアプリ。\n\nあらゆる場面に対応するシンプルなソケット。")

# Elevator / Skyline Caller
t("Call for Cabin", "キャビンを呼ぶ")
t("Calling", "呼出中")
t(".", ".")
t("Exit Skyline Caller", "Skyline Callerを終了")
t("...", "...")
t("Select Cabin Destination:", "行き先を選択:")
t("cost", "コスト")

# Socketeer app
t("Please click on a socket to designate removal.", "ソケットをクリックして撤去を指定してください。")
t("Socket not placed.", "ソケットが設置されていません。")
t("socketeer ({socketid})", "socketeer ({socketid})")
t("Place {socket_type} socket", "{socket_type} ソケットを設置")
t("socket removal ({socketid})", "ソケット撤去 ({socketid})")
t("Now everyone can make sockets!", "誰でもソケットを作れます！")
t("Make a socket.", "ソケットを作る。")
t("1. Choose a socket type", "1. ソケットタイプを選択")
t("2. Click to start placing. \"CTRL\" button to undo.", "2. クリックして設置開始。\"CTRL\"で取消。")
t("Place socket", "ソケットを設置")
t("3. Confirmed placement? Click to confirm.", "3. 設置を確認しますか？クリックで確定。")
t("Remove a socket.", "ソケットを撤去する。")
t("1. Click to start removal selection.", "1. クリックして撤去選択を開始。")
t("Remove socket", "ソケットを撤去")
t("2. Confirmed for removal?\nClick to confirm.", "2. 撤去しますか？\nクリックで確定。")

# SticKy PriNtZ app
t("We chargez {cost_per_print} moniez for each pasted printz.", "1枚あたり {cost_per_print} のお金がかかります。")
t("stick-IT PRINTZ", "stick-IT PRINTZ")
t("STICKY PRINTZ", "STICKY PRINTZ")
t("QUITZ", "終了")
t("[u]How to use?[/u]\n\n1. Input text to add as a sticky note.\n2. Press print button.\n3. Paste on device.",
  "[u]使い方[/u]\n\n1. 付箋として追加するテキストを入力。\n2. 印刷ボタンを押す。\n3. デバイスに貼り付け。")
t("NOTE CONTENTZ", "メモ内容")
t("write\nsumtin", "何か\n書いてね")
t("PRINTZ IT !!!", "印刷する！！！")

# Floor management
t("This floor has {n} users.", "このフロアには {n} 人のユーザーがいます。")
t("A network outage notice has been issued for this floor.", "このフロアにネットワーク停止通知が発行されています。")
t("Select a floor management action.", "フロア管理アクションを選択してください。")
t("Issue network outage notice", "ネットワーク停止通知を発行")
t("Floor management currently only available to network owner.", "フロア管理は現在ネットワークオーナーのみ利用可能です。")
t("Issue a network outage notice to floor {n}.\n\t\t\t\nAll users will go offline (not consuming anything).\n\nUseful for restructuring connections.\n\nDuration: End of the day.",
  "フロア {n} にネットワーク停止通知を発行。\n\t\t\t\nすべてのユーザーがオフラインになります（消費なし）。\n\n接続の再構成に便利です。\n\n期間: 当日終了まで。")
t("A network outage is already scheduled on this floor.", "このフロアにはすでにネットワーク停止が予定されています。")
t("Unable to issue outage notices at this time.", "現在、停止通知を発行できません。")
t("Please choose a valid option.", "有効なオプションを選択してください。")
t("Click to manage the floor.", "クリックしてフロアを管理。")

# Surveyor app
t("Curr. satiety", "現在の満足度")
t("Lowest today", "本日最低")
t("Surveyor", "サーベイヤー")
t("SLAs fulfilled", "SLA達成")
t("Search by floor/username.", "フロア/ユーザー名で検索。")
t("Only show SLA-breaching users", "SLA違反ユーザーのみ表示")
t("Back to list", "一覧に戻る")
t("This behavior only targets sites with these topics.", "この動作はこれらのトピックを持つサイトのみを対象とします。")
t("This behavior creates these uses on the visited sites.", "この動作は訪問先サイトにこれらのUSEを生成します。")
t("This behavior consumes these uses on the visited sites.", "この動作は訪問先サイトのこれらのUSEを消費します。")
t("The traffic weight of this behavior", "この動作のトラフィック重み")
t("Importance", "重要度")
t("The higher this is, the more influence it has over the user's overall satisfaction.",
  "高いほどユーザーの総合満足度への影響が大きくなります。")
t("Consumed {n} uses from {dst}", "{dst} から {n} USE消費")
t("yes", "はい")
t("no", "いいえ")
t("Produces", "生産")
t("Consumes", "消費")
t("Subjects", "サブジェクト")
t("The size of the network traffic when the request is made.", "リクエスト時のネットワークトラフィックサイズ。")
t("Bandwidth cost per traversal", "トラバーサルあたりの帯域幅コスト")
t("Currently satisfied?", "現在満足？")
t("Unassigned", "未割当")
t("Periodic", "周期的")
t("On-Boot", "起動時")
t("Time left until SLA breach: {seconds_left} seconds", "SLA違反まで: {seconds_left} 秒")
t("You will lose the game when this timer runs out!", "このタイマーが切れるとゲームオーバーです！")
t("User is offline due to network outage notice.", "ネットワーク停止通知によりユーザーはオフラインです。")
t("User is inactive.", "ユーザーは非アクティブです。")
t("No issues with this user.", "このユーザーに問題はありません。")
t("Payment by lowest satiety today", "本日の最低満足度による支払い")
t("Payment by usage fulfilment today", "本日の利用達成度による支払い")
t("Information copied to clipboard", "情報をクリップボードにコピーしました")
t("username (user type)", "ユーザー名 (ユーザータイプ)")
t("Issues and complaints", "問題と苦情")
t("Activity period", "活動時間帯")
t("User is active within this period of time.", "ユーザーはこの時間帯にアクティブです。")
t("Grace days left", "猶予日数")
t("Number of days left before SLA breach incidents will start to trigger.",
  "SLA違反イベントが発生するまでの残り日数。")
t("SLA", "SLA")
t("Floor", "フロア")
t("Satiety", "満足度")
t("Lowest satiety today", "本日の最低満足度")
t("Usage fulfilment today", "本日の利用達成度")
t("Payment today", "本日の支払い")
t("Hardware addr", "ハードウェアアドレス")
t("Network addr", "ネットワークアドレス")
t("DNS addrs", "DNSアドレス")
t("DHCP mode", "DHCPモード")
t("Bandwidth consumption", "帯域幅消費")
t("Copy user network details", "ユーザーのネットワーク詳細をコピー")
t("Behavior insights", "行動分析")
t("This host can support these uses.", "このホストがサポートできるUSE。")
t("Associated topics for the uses.", "USEに関連するトピック。")
t("The desired visitor vs. actual visitor count.", "希望訪問者数 vs. 実際の訪問者数。")
t("Uses", "USE")
t("Visits/Required", "訪問数/必要数")
t("View user profile.", "ユーザープロファイルを表示。")
t("User is offline.", "ユーザーはオフラインです。")
t("Offline", "オフライン")
t("Visitors for", "訪問者:")
t("Unique visitors", "ユニーク訪問者")
t("Satiety change today", "本日の満足度変化")
t("Synthamp", "Synthamp")
t("Never", "なし")
t("Floor will be automatically accepted on this day.", "このフロアはこの日に自動的に承認されます。")
t("Auto accept date", "自動承認日")
t("Cash to receive when accepting this floor now.", "このフロアを今承認した場合に受け取る金額。")
t("Upfront payment", "前払い金")
t("User Type", "ユーザータイプ")
t("Min. Satiety", "最低満足度")
t("Grace Days", "猶予日数")
t("This floor has no users.", "このフロアにはユーザーがいません。")
t("Accept this build now", "このビルドを今承認")

# The Secretariat
t("Submitted", "送信済み")
t("Submit and activate this proposal.", "この提案を送信して有効化する。")
t("Will not be deferred (locked).", "繰り延べされません（ロック済み）。")
t("Unlock this proposal", "この提案のロックを解除")
t("This proposal is already locked, it will not be deferred.", "この提案はすでにロックされており、繰り延べされません。")
t("To be deferred on day {n}.", "{n} 日目に繰り延べされます。")
t("Lock this proposal", "この提案をロック")
t("Locking this proposal so it will not be deferred.", "この提案をロックして繰り延べを防止します。")
t("Submit and activate", "送信して有効化")
t("Active proposals", "アクティブな提案")
t("No applied proposals", "適用済みの提案なし")
t("Applied proposals", "適用済みの提案")
t("No proposals", "提案なし")
t("No floor onboardings", "フロアオンボーディングなし")
t("Floor users onboarding list", "フロアユーザーオンボーディングリスト")
t("Secretariat not available", "事務局は利用できません")
t("New proposals from The Secretariat", "事務局からの新しい提案")
t("Floor build", "フロア建設")
t("Proposals", "提案")
t("History", "履歴")
t("Re-roll proposals.", "提案を再抽選。")
t("RFP can only be made by host.", "RFPはホストのみ作成できます。")
t("The Secretariat", "事務局")
t("Floor Build", "フロア建設")
t("The Secretariat offers Request for proposals (RFPs) services for new floor builds.",
  "事務局はフロア新設のためのRFP（提案要求）サービスを提供しています。")
t("Current fee :", "現在の手数料:")
t("Issue new RFP", "新規RFPを発行")
t("Unknown", "不明")

# Floor Alert
t("Floor Alert", "フロアアラート")
t("issues and complains ", "問題と苦情")
t("Top issue in floor", "フロアの最重要問題")
t("Next", "次へ")
t("total count\n", "合計件数\n")
t("reported by\n", "報告者\n")
t("No issue.", "問題なし。")
t("Top issue in floor {sfn}", "フロア {sfn} の最重要問題")

# Tower Link
t("Tower Link not available.", "Tower Linkは利用できません。")
t("Link view", "リンク表示")
t("Tower view", "タワー表示")
t("Highest average traversal", "最高平均トラバーサル")
t("Highest peak traversal", "最高ピークトラバーサル")
t("Highest daily cost", "最高日次コスト")
t("Lowest average traversal", "最低平均トラバーサル")
t("Lowest peak traversal", "最低ピークトラバーサル")
t("Lowest daily cost", "最低日次コスト")
t("Link created.", "リンク作成完了。")
t("No socket selected", "ソケット未選択")
t("Outlet type: {type}", "アウトレットタイプ: {type}")
t("Outlet type mismatched", "アウトレットタイプ不一致")
t("Already picked for linking", "リンク済みとして選択済み")
t("Part of an existing link", "既存リンクの一部")
t("No sizings", "サイズなし")
t("N/A", "N/A")
t("trav. per tick", "trav./tick")
t("Tower Link Ltd. Open Socket Linker", "Tower Link Ltd. オープンソケットリンカー")
t("Create link", "リンク作成")
t("View links", "リンク表示")
t("Sort by", "ソート順")
t("Point A floor select", "ポイントAフロア選択")
t("Point A unlinked outlet select", "ポイントA未リンクアウトレット選択")
t("Point B floor select", "ポイントBフロア選択")
t("Point B unlinked outlet select", "ポイントB未リンクアウトレット選択")
t("Link type", "リンクタイプ")
t("Link size", "リンクサイズ")
t("Link bandwidth", "リンク帯域幅")
t("Quotation", "見積もり")
t("Same floor links are heavily taxed due to tower walling regulations.",
  "同一フロアリンクはタワー壁面規制により高い税金がかかります。")
t("Setup cost", "設置コスト")
t("Daily cost", "日次コスト")
t("Reset", "リセット")
t("Request link", "リンク要求")
t("Link still active.", "リンクはまだアクティブです。")
t("Deactivate", "無効化")
t("Link up", "リンクアップ")
t("Link is maxed out", "リンクが上限に達しています")
t("Upgrade this link", "このリンクをアップグレード")
t("Remove this link", "このリンクを削除")
t("Reactivate", "再有効化")
t("Link down", "リンクダウン")
t("Decomission", "廃止")
t("MAXED", "上限")
t("COPPER", "銅線")
t("The link type and grade.", "リンクのタイプとグレード。")
t("Setup cost of this link.", "このリンクの設置コスト。")
t("Cost to operate this link, paid end of day.", "このリンクの運用コスト。日末に支払い。")
t("Cost per day", "日次コスト")
t("Average traversal per tick.", "tickあたりの平均トラバーサル。")
t("Average traversal", "平均トラバーサル")
t("Highest traversal per tick for the day.", "本日のtickあたり最高トラバーサル。")
t("Peak today", "本日のピーク")
t("Deactivate this link.", "このリンクを無効化する。")
t("Manage", "管理")
t("New Link size", "新しいリンクサイズ")
t("New link bandwidth", "新しいリンク帯域幅")
t("Upgrade cost", "アップグレードコスト")
t("New daily cost", "新しい日次コスト")
t("Upgrade", "アップグレード")
t("Decomission this link.", "このリンクを廃止する。")

# Tower stats / population
t("population stats", "人口統計")
t("tower population", "タワー人口")
t("User Count", "ユーザー数")
t("Average Satiety (%)", "平均満足度 (%)")
t("Floor {floor_num}", "フロア {floor_num}")
t("satiety stats", "満足度統計")
t("floor satiety", "フロア満足度")
t("User heat map", "ユーザーヒートマップ")
t("Top 5 Lowest Satiety per Floor", "フロア別最低満足度トップ5")
t("Lowest \nSatiety", "最低\n満足度")
t("No domains with visitor data", "訪問者データのあるドメインなし")
t("Visitors to {domain_name}", "{domain_name} への訪問者")
t("visitor stats", "訪問者統計")
t("domain", "ドメイン")
t("unnamed app", "無名アプリ")
t("tower stats", "タワー統計")
t("babel-link", "babel-link")

# MobileOS
t("MobileOS", "MobileOS")
t("Account balance: {acc_balance}", "口座残高: {acc_balance}")
t("Left-click to cycle information. Right-click to lock/unlock.", "左クリックで情報切替。右クリックでロック/解除。")
t("Manage your finances.", "財務を管理する。")
t("View messages.", "メッセージを表示。")
t("msgbox", "メッセージボックス")
t("Technical admin tool.", "技術管理ツール。")
t("netsh", "netsh")
t("Check on your users.", "ユーザーの状況を確認。")
t("The good ole DMarketV1.", "おなじみのDMarketV1。")
t("Purchase devices/cables.", "デバイス/ケーブルを購入。")
t("D-Market2", "D-Market2")
t("Create network links between floors.", "フロア間のネットワークリンクを作成。")
t("Tower Link", "Tower Link")
t("Borrow money.", "お金を借りる。")
t("Fi$hy Loans", "Fi$hy Loans")
t("High-level admin functions.", "ハイレベル管理機能。")
t("Unlock new applications for MobileOS.", "MobileOSの新しいアプリをアンロック。")
t("Browse the Internet.", "インターネットを閲覧。")
t("Time manipulation.", "時間操作。")
t("Break Time", "Break Time")
t("use the terminal your way.", "ターミナルを自由に使う。")
t("list command aliases.", "コマンドエイリアスを一覧表示。")
t("set command alias.", "コマンドエイリアスを設定。")
t("unset command alias.", "コマンドエイリアスを解除。")
t("No user command aliases", "ユーザーコマンドエイリアスなし")
t("User command aliases:", "ユーザーコマンドエイリアス:")
t("User command alias '{alias}' cleared", "ユーザーコマンドエイリアス '{alias}' を解除しました")
t("'{keyword}' is reserved and cannot be use as alias.", "'{keyword}' は予約語のためエイリアスに使用できません。")
t("'{lit}{alias}{end}' is now short for '{lit}{cmd}{end}'", "'{lit}{alias}{end}' は '{lit}{cmd}{end}' の短縮形になりました")

# ============================================================
# BATCH 3: Netsh routines / shell helpers
# ============================================================
t("shell quality-of-life enhancements.", "シェルの便利機能。")
t("sets a 'default' debugger to always use.", "常に使用する'デフォルト'デバッガーを設定。")
t("cycle a 'default' debugger to always use.", "'デフォルト'デバッガーを切替。")
t("clear always helper settings.", "alwaysヘルパー設定をクリア。")
t("sets a 'default' device to always be on.", "常に使用する'デフォルト'デバイスを設定。")
t("cleared 'always using' helper.", "'always using'ヘルパーをクリアしました。")
t("you must now include 'using <debugger_addr>' when inputting commands.",
  "コマンド入力時に 'using <debugger_addr>' を含める必要があります。")
t("i.e., 'scan devices' will no longer work and should be 'scan devices using {addr}'.",
  "例: 'scan devices' は使えなくなり、'scan devices using {addr}' と入力してください。")
t("invalid address", "無効なアドレス")
t("address should be a valid domain name, network address or hardware address.",
  "アドレスは有効なドメイン名、ネットワークアドレス、またはハードウェアアドレスである必要があります。")
t("always using {dbgaddr} as debugger address.", "{dbgaddr} をデバッガーアドレスとして常時使用。")
t("try doing debugger related commands without inputting debugger address.",
  "デバッガーアドレスを入力せずにデバッガー関連コマンドを試してみてください。")
t("i.e., 'scan devices' should now work instead of 'scan devices using {addr}'.",
  "例: 'scan devices using {addr}' の代わりに 'scan devices' で動作するようになります。")
t("cleared 'always on' helper.", "'always on'ヘルパーをクリアしました。")
t("you must now include 'on <device_addr>' when inputting commands.",
  "コマンド入力時に 'on <device_addr>' を含める必要があります。")
t("i.e., 'dstat' will no longer work and should be 'dstat on {addr}'.",
  "例: 'dstat' は使えなくなり、'dstat on {addr}' と入力してください。")
t("always using {devaddr} as device address.", "{devaddr} をデバイスアドレスとして常時使用。")
t("try doing device related commands without inputting device address.",
  "デバイスアドレスを入力せずにデバイス関連コマンドを試してみてください。")
t("i.e., 'dstat' should now work instead of 'dstat on {addr}'.",
  "例: 'dstat on {addr}' の代わりに 'dstat' で動作するようになります。")
t("invalid '{always_cmd}' command, see manual with '{man_always}'.",
  "無効な '{always_cmd}' コマンド。'{man_always}' でマニュアルを参照してください。")

# Bot management
t("manage bots on devices.", "デバイス上のボットを管理。")
t("show bots and their configuration on device.", "デバイス上のボットと設定を表示。")
t("create a bot to generate visit traffic to an address.", "アドレスへの訪問トラフィックを生成するボットを作成。")
t("Missing 'using' keyword.", "'using' キーワードがありません。")
t("Missing 'on' keyword.", "'on' キーワードがありません。")
t("no bots configured on {dev_addr}.", "{dev_addr} にボットが設定されていません。")
t("Missing 'to' keyword.", "'to' キーワードがありません。")
t("Invalid bot type: {bot}", "無効なボットタイプ: {bot}")
t("bot {botname} created.", "ボット {botname} を作成しました。")
t("to start/stop/delete the bot:", "ボットの開始/停止/削除:")
t("clear screen.", "画面をクリア。")

# Cron
t("scheduled commands.", "スケジュールコマンド。")
t("show scheduled commands.", "スケジュールコマンドを表示。")
t("add a new cron schedule.", "新しいcronスケジュールを追加。")
t("remove cron schedules.", "cronスケジュールを削除。")
t("clear cron logs.", "cronログをクリア。")
t("clear all cron schedules and logs.", "すべてのcronスケジュールとログをクリア。")
t("No cron schedules, input 'man cron' for help.", "cronスケジュールなし。'man cron' でヘルプを表示。")
t("Id", "ID")
t("Sched.", "スケジュール")
t("Command", "コマンド")
t("Invalid cron expression: {expr}", "無効なcron式: {expr}")
t("Valid cron expression examples:", "有効なcron式の例:")
t("Cron schedule installed successfully.", "cronスケジュールが正常にインストールされました。")
t("Cron schedule removed successfully.", "cronスケジュールが正常に削除されました。")
t("All cron schedules and logs cleared.", "すべてのcronスケジュールとログをクリアしました。")
t("All cron logs cleared.", "すべてのcronログをクリアしました。")

# DHCP management
t("management", "管理")
t("show DHCP options on dhcp server.", "DHCPサーバーのDHCPオプションを表示。")
t("make the DHCP server auto designate dns servers.", "DHCPサーバーがDNSサーバーを自動指定するようにする。")
t("make the DHCP server auto assign network addresses with specified prefix.",
  "DHCPサーバーが指定プレフィックスでネットワークアドレスを自動割当するようにする。")
t("make the DHCP server assign a specific network address based on the requester's hardware address.",
  "DHCPサーバーが要求者のハードウェアアドレスに基づいて特定のネットワークアドレスを割り当てるようにする。")
t("DHCP options on {dhcpaddr}", "{dhcpaddr} のDHCPオプション")
t("no dns designation", "DNS指定なし")
t("no network assignment prefix", "ネットワーク割当プレフィックスなし")
t("no network address binds/reservation", "ネットワークアドレスバインド/予約なし")
t("prefix too long.", "プレフィックスが長すぎます。")
t("DHCP assignment prefix should not exceed {maxchars} characters.",
  "DHCP割当プレフィックスは {maxchars} 文字を超えてはいけません。")
t("DHCP server {dhcpaddr} now auto assigns network address with prefix '{prefix}'.",
  "DHCPサーバー {dhcpaddr} がプレフィックス '{prefix}' でネットワークアドレスを自動割当します。")
t("invalid DNS server address.", "無効なDNSサーバーアドレス。")
t("DHCP server {dhcpaddr} now auto designates these DNS servers: {dnsaddrs}.",
  "DHCPサーバー {dhcpaddr} がこれらのDNSサーバーを自動指定します: {dnsaddrs}。")
t("{hwaddr} is not a valid hardware address.", "{hwaddr} は有効なハードウェアアドレスではありません。")
t("Missing 'as' keyword.", "'as' キーワードがありません。")
t("invalid network address", "無効なネットワークアドレス")
t("network address must begin with a '@' and may only consist of alpha-numeric and '.' characters.",
  "ネットワークアドレスは '@' で始まり、英数字と '.' のみ使用できます。")
t("DHCP server {dhcpaddr} now assigns {nwaddr} on dhcp requests from {hwaddr}.",
  "DHCPサーバー {dhcpaddr} が {hwaddr} からのDHCP要求に {nwaddr} を割り当てます。")
t("DHCP server {dhcpaddr} network address binding for {hwaddr} removed.",
  "DHCPサーバー {dhcpaddr} の {hwaddr} のネットワークアドレスバインドを削除しました。")
t("unknown dhcp option: {opt}.", "不明なDHCPオプション: {opt}。")

# DNS commands
t("test resolving a domain.", "ドメインの名前解決をテスト。")
t("map a domain to an address.", "ドメインをアドレスにマッピング。")
t("clear dns record for domain.", "ドメインのDNSレコードをクリア。")
t("show dns server mapping.", "DNSサーバーマッピングを表示。")
t("clear all dns records on a server.", "サーバー上のすべてのDNSレコードをクリア。")
t("Missing lookup address.", "ルックアップアドレスがありません。")
t("no DNS servers available to process the request.", "リクエストを処理できるDNSサーバーがありません。")
t("response from {dns_addr}", "{dns_addr} からの応答")
t("took {n} bandwidth.", "帯域幅 {n} を使用。")
t("Missing 'map' domain.", "'map' ドメインがありません。")
t("invalid domain", "無効なドメイン")
t("added DNS entry on {dns_addr}", "{dns_addr} にDNSエントリを追加")
t("Missing 'unmap' domain.", "'unmap' ドメインがありません。")
t("cleared DNS entry on {dns_addr}", "{dns_addr} のDNSエントリをクリア")
t("DNS records on {dns_addr}", "{dns_addr} のDNSレコード")
t("Global DNS records", "グローバルDNSレコード")
t("domain.", "ドメイン。")
t("pointer.", "ポインタ。")
t("cleared {n} records from {dns_addr}", "{dns_addr} から {n} レコードをクリア")

# Device status (dstat)
t("view device status through a remote debugger.", "リモートデバッガーでデバイスの状態を表示。")
t("get status of the specified device.", "指定デバイスの状態を取得。")
t("clear port tx/rx statistics on the specified device.", "指定デバイスのポートtx/rx統計をクリア。")
t("Port usage statistics on {dev_addr} reset.", "{dev_addr} のポート使用統計をリセットしました。")
t("Product name", "製品名")
t("Outlet name", "アウトレット名")
t("hops from debugger", "デバッガーからのホップ数")
t("uptime", "稼働時間")
t("seconds", "秒")
t("CPU used", "CPU使用量")
t("tick(s) per second", "tick/秒")
t("Addresses", "アドレス")
t("Network load", "ネットワーク負荷")
t("Peripherals", "周辺機器")
t("Removable storage", "リムーバブルストレージ")
t("Data wiper USB stick", "データワイプUSBスティック")
t("Unknown peripheral", "不明な周辺機器")
t("Installed programs", "インストール済みプログラム")
t("Storage used", "ストレージ使用量")
t("Running processes", "実行中プロセス")
t("Memory used", "メモリ使用量")
t("Usage stack", "使用スタック")
t("Port stats", "ポート統計")

# Echo / print / msg
t("send multiplayer message (visible on everyone's terminal).", "マルチプレイヤーメッセージを送信（全員のターミナルに表示）。")
t("print to terminal.", "ターミナルに出力。")

# Firewall
t("manage rules on firewalls.", "ファイアウォールのルールを管理。")
t("show firewall policies and their number.", "ファイアウォールポリシーと番号を表示。")
t("set the default policy of the firewall to allow or deny.", "ファイアウォールのデフォルトポリシーを許可または拒否に設定。")
t("add a firewall policy.", "ファイアウォールポリシーを追加。")
t("remove firewall policies by number.", "番号でファイアウォールポリシーを削除。")
t("clear all policies.", "すべてのポリシーをクリア。")
t("default policy", "デフォルトポリシー")
t("default should either be", "デフォルトは次のいずれかにしてください")
t("added default policy", "デフォルトポリシーを追加")
t("firewall policy from (source) address must be a hardware or network address.",
  "ファイアウォールポリシーの送信元アドレスはハードウェアまたはネットワークアドレスである必要があります。")
t("firewall policy to (dst) address must be a hardware or network address.",
  "ファイアウォールポリシーの宛先アドレスはハードウェアまたはネットワークアドレスである必要があります。")
t("policy {policy} already exists on {fw}.", "ポリシー {policy} は既に {fw} に存在します。")
t("added policy on {fw}.", "{fw} にポリシーを追加しました。")
t("removed firewall policy", "ファイアウォールポリシーを削除しました")
t("firewall policies for {fw} cleared.", "{fw} のファイアウォールポリシーをクリアしました。")

# HA configuration
t("manage high-availability setup on devices.", "デバイスの高可用性設定を管理。")
t("show all ports on the device.", "デバイスの全ポートを表示。")
t("create a physical port grouping.", "物理ポートグループを作成。")
t("remove port grouping by number.", "番号でポートグループを削除。")
t("device {dev_addr} has reached port group limits.", "デバイス {dev_addr} はポートグループの上限に達しました。")
t("haconf 'group' requires more than 1 port to be grouped", "haconf 'group' はグループ化に2つ以上のポートが必要です")
t("port {port} is not a valid port on {dev_addr}", "ポート {port} は {dev_addr} の有効なポートではありません")
t("duplicate {port} specified.", "ポート {port} が重複しています。")
t("port {port} is already grouped by {port_group}.", "ポート {port} は既にポートグループ {port_group} に属しています。")
t("port group created with ports {ports}.", "ポート {ports} でポートグループを作成しました。")
t("not a valid port group '{invalid_group}'.", "'{invalid_group}' は有効なポートグループではありません。")
t("removed port group '{port_group}'.", "ポートグループ '{port_group}' を削除しました。")

# List debuggers
t("list debuggers for remote access.", "リモートアクセス用のデバッガーを一覧表示。")
t("list accessible remote debuggers.", "アクセス可能なリモートデバッガーを一覧表示。")
t("the routine lists only debuggers that are RUNNING, make sure the debugger is turned on.",
  "このルーチンは実行中のデバッガーのみ表示します。デバッガーの電源が入っていることを確認してください。")
t("accessible remote debuggers", "アクセス可能なリモートデバッガー")
t("(Floor {n})", "(フロア {n})")
t("currently, debugger '{dbgaddr}' is set as the default debugger.",
  "現在、デバッガー '{dbgaddr}' がデフォルトデバッガーに設定されています。")
t("input '{always}' to learn more about the 'always' command",
  "'{always}' と入力して 'always' コマンドの詳細を確認してください")

# Man / help
t("usage manual/help routine.", "マニュアル/ヘルプルーチン。")
t("'{man}' or '{man_routine}' to get help.", "'{man}' または '{man_routine}' でヘルプを表示。")
t("hit ESCAPE key or click anywhere outside to unfocus window.", "ESCキーまたはウィンドウ外をクリックでフォーカス解除。")
t("shell shortcuts/usage help.", "シェルショートカット/使い方ヘルプ。")
t("cycle previous executed command", "過去に実行したコマンドを呼び出し")
t("try auto complete word", "単語の自動補完を試行")
t("erase previous word from cursor", "カーソルの前の単語を消去")
t("go to start of command", "コマンドの先頭へ移動")
t("go to end of command", "コマンドの末尾へ移動")
t("halt/exit/clear", "停止/終了/クリア")
t("exit terminal", "ターミナルを終了")
t("paste from clipboard", "クリップボードから貼り付け")
t("toggle terminal", "ターミナルを切替")
t("input '{man_routine}' for more help.", "'{man_routine}' と入力して詳細ヘルプを表示。")
t("for command input help, see '{man_shell}' for some usage hints.",
  "コマンド入力ヘルプについては '{man_shell}' を参照。")
t("for connectivity troubleshooting, see '{man_connect}'.",
  "接続のトラブルシューティングについては '{man_connect}' を参照。")
t("unknown routine", "不明なルーチン")
t("input '{man}' for list of routines.", "'{man}' と入力してルーチン一覧を表示。")

# Net configuration
t("invalid network address: max {maxchars} characters including '@'.",
  "無効なネットワークアドレス: '@'を含めて最大 {maxchars} 文字。")
t("manage network address configuration on devices/users.", "デバイス/ユーザーのネットワークアドレス設定を管理。")
t("set a network address on device/user.", "デバイス/ユーザーにネットワークアドレスを設定。")
t("clear the network address on device/user.", "デバイス/ユーザーのネットワークアドレスをクリア。")
t("manage network DNS configuration on devices/users.", "デバイス/ユーザーのネットワークDNS設定を管理。")
t("designate the DNS server address for the device/user.", "デバイス/ユーザーのDNSサーバーアドレスを指定。")
t("clear the designated dns server on device/user.", "デバイス/ユーザーの指定DNSサーバーをクリア。")
t("manage network DHCP configuration on devices/users.", "デバイス/ユーザーのネットワークDHCP設定を管理。")
t("configure dhcp request mode for the device/user.", "デバイス/ユーザーのDHCPリクエストモードを設定。")
t("perform a dhcp request from the device/user now.", "デバイス/ユーザーからDHCPリクエストを今すぐ実行。")
t("manage network port configuration on devices/users.", "デバイス/ユーザーのネットワークポート設定を管理。")
t("show port configuration for device/user.", "デバイス/ユーザーのポート設定を表示。")
t("reset/clear port configuration on ports.", "ポートのポート設定をリセット/クリア。")
t("configure ports as backend/upstream for proxies/load-balancers.",
  "ポートをプロキシ/ロードバランサーのバックエンド/アップストリームとして設定。")
t("set a different port metric.", "異なるポートメトリックを設定。")
t("manage network configuration on devices/users.", "デバイス/ユーザーのネットワーク設定を管理。")
t("show network configuration on device/user.", "デバイス/ユーザーのネットワーク設定を表示。")
t("show network address configuration help.", "ネットワークアドレス設定ヘルプを表示。")
t("show network dns configuration help.", "ネットワークDNS設定ヘルプを表示。")
t("show network dhcp configuration help.", "ネットワークDHCP設定ヘルプを表示。")
t("show network ports configuration help.", "ネットワークポート設定ヘルプを表示。")
t("device {dev} networking information", "デバイス {dev} のネットワーク情報")
t("hardware address", "ハードウェアアドレス")
t("network address", "ネットワークアドレス")
t("dns server", "DNSサーバー")
t("periodic", "周期的")
t("on boot only", "起動時のみ")
t("disabled", "無効")
t("dhcp mode", "DHCPモード")
t("bandwidth capacity (travs./tick)", "帯域幅容量 (trav./tick)")
t("network load balancer without back-ports configured.", "バックポートが未設定のネットワークロードバランサー。")
t("network load balancer back-ports:", "ネットワークロードバランサーのバックポート:")
t("Missing 'set' keyword.", "'set' キーワードがありません。")
t("an invalid address cannot be designated as the DNS address.",
  "無効なアドレスはDNSアドレスに指定できません。")
t("DHCP set to {newmode} on '{devaddr}'.", "'{devaddr}' のDHCPを {newmode} に設定しました。")
t("forcing '{dev}' to perform DHCP request now.", "'{dev}' にDHCPリクエストを強制実行中。")
t("Port configuration", "ポート設定")
t("port", "ポート")
t("met.", "メトリック")
t("attributes", "属性")
t("{portid} configuration -> {new_cfg}", "{portid} 設定 -> {new_cfg}")
t("metric value must be a number", "メトリック値は数値である必要があります")
t("{portid} metric -> {value}", "{portid} メトリック -> {value}")
t("network address changed on {dev}.", "{dev} のネットワークアドレスが変更されました。")
t("designated DNS changed on {dev}.", "{dev} の指定DNSが変更されました。")

# Pcap / notification
t("sends an on-screen notification.", "画面上に通知を送信。")
t("starts traffic capture on a network tap.", "ネットワークタップでトラフィックキャプチャを開始。")
t("starts traffic capture on a network tap, with optional traffic type filter.",
  "ネットワークタップでトラフィックキャプチャを開始（オプションのトラフィックタイプフィルター付き）。")
t("is offline.", "オフラインです。")
t("live packet capture on {dev}", "{dev} のライブパケットキャプチャ")
t("bandwidth/tick", "帯域幅/tick")
t("top {n} requests", "上位 {n} リクエスト")

# Ping
t("ping a device from the debugger.", "デバッガーからデバイスにpingを送信。")
t("send a ping with a specific traffic class.", "特定のトラフィッククラスでpingを送信。")
t("sending {tft} to {dst}", "{tft} を {dst} に送信中")
t("address '{addr}' unreachable.", "アドレス '{addr}' に到達できません。")
t("reply from", "応答元")

# Power management
t("remote device power management.", "リモートデバイス電源管理。")
t("remotely power on/off device(s).", "リモートでデバイスの電源をオン/オフ。")
t("Broadcasting {cmd_name} command from {deb_addr}.", "{deb_addr} から {cmd_name} コマンドをブロードキャスト中。")
t("Sending {cmd_name} command to {dev_addr} from {deb_addr}.", "{deb_addr} から {dev_addr} に {cmd_name} コマンドを送信中。")
t("Sent: {traffic_class}", "送信済み: {traffic_class}")

# Program management
t("program", "プログラム")
t("list available programs to install.", "インストール可能なプログラムを一覧表示。")
t("get program description.", "プログラムの説明を取得。")
t("view installed/running programs on device.", "デバイス上のインストール済み/実行中プログラムを表示。")
t("install program on device.", "デバイスにプログラムをインストール。")
t("start program on device.", "デバイスでプログラムを開始。")
t("stop program on device.", "デバイスでプログラムを停止。")
t("uninstall program on device.", "デバイスからプログラムをアンインストール。")
t("no programs available!", "利用可能なプログラムがありません！")
t("program '{prg}' not found.", "プログラム '{prg}' が見つかりません。")
t("do '{listprog}' to list programs available for installation.",
  "'{listprog}' でインストール可能なプログラムを一覧表示してください。")
t("no {state} programs on {dev}.", "{dev} に{state}のプログラムはありません。")
t("program name", "プログラム名")
t("program type", "プログラムタイプ")
t("producer", "プロデューサー")
t("produce output", "出力を生産")
t("per tick", "tick毎")
t("converter", "コンバーター")
t("all", "すべて")
t("required inputs", "必要な入力")
t("produce target", "生産ターゲット")
t("source", "ソース")
t("destination", "宛先")
t("null", "null")
t("data storage", "データストレージ")
t("stores", "保存")
t("compatible uses per free storage", "空きストレージあたりの互換USE数")
t("firmware", "ファームウェア")
t("cpu load", "CPU負荷")
t("install size (code+data)", "インストールサイズ（コード+データ）")
t("memory size", "メモリサイズ")
t("description", "説明")

# Proxy
t("manage proxy configuration on devices.", "デバイスのプロキシ設定を管理。")
t("show proxy configuration on device.", "デバイスのプロキシ設定を表示。")

# Quit
t("exit netsh.", "netshを終了。")

# RIP routing
t("configure auto route discovery on routers.", "ルーターの自動ルート検出を設定。")
t("show routes and their number.", "ルートとその番号を表示。")
t("start/stop advertise routing information.", "ルーティング情報のアドバタイズを開始/停止。")
t("listen/ignore advertised routing information from other routers.",
  "他のルーターからのルーティング情報アドバタイズを受信/無視。")
t("{green}listening{end} for route advertisements.", "ルートアドバタイズを{green}受信中{end}。")
t("{red}ignoring/passing{end} route advertisements.", "ルートアドバタイズを{red}無視/パススルー中{end}。")
t("{green}advertising{end} route table over all ports.", "全ポートでルートテーブルを{green}アドバタイズ中{end}。")
t("{green}advertising{end} route table over {port}.", "{port} でルートテーブルを{green}アドバタイズ中{end}。")
t("{red}not advertising{end} route table.", "ルートテーブルを{red}アドバタイズしていません{end}。")
t("router is not advertising on {port}.", "ルーターは {port} でアドバタイズしていません。")
t("{red}stopped advertising{end} route table over all ports.", "全ポートでルートテーブルのアドバタイズを{red}停止{end}。")
t("{red}stopped advertising{end} route table over {port}.", "{port} でルートテーブルのアドバタイズを{red}停止{end}。")
t("router {rtaddr} configured to {green}listen{end} for route advertisements.",
  "ルーター {rtaddr} をルートアドバタイズ{green}受信{end}に設定しました。")
t("router {rtaddr} configured to {red}ignore/passthrough{end} route advertisements.",
  "ルーター {rtaddr} をルートアドバタイズ{red}無視/パススルー{end}に設定しました。")

# Route management
t("manage routes on routers.", "ルーターのルートを管理。")
t("set a default route.", "デフォルトルートを設定。")
t("append route.", "ルートを追加。")
t("remove route by number.", "番号でルートを削除。")
t("clear all routes.", "すべてのルートをクリア。")
t("forward/drop all broadcast requests.", "全ブロードキャストリクエストを転送/破棄。")
t("unmatched traffic (default) is forwarded via {defaultroute}.",
  "未一致トラフィック（デフォルト）は {defaultroute} 経由で転送されます。")
t("unmatched traffic (default) is {red}dropped{end}.",
  "未一致トラフィック（デフォルト）は{red}破棄{end}されます。")
t("broadcast traffic is {green}enabled{end} on all ports.",
  "ブロードキャストトラフィックは全ポートで{green}有効{end}です。")
t("broadcast traffic is {red}dropped{end} on all ports.",
  "ブロードキャストトラフィックは全ポートで{red}破棄{end}されます。")
t("added default route via {viaport} on {dev}.",
  "{dev} に {viaport} 経由のデフォルトルートを追加しました。")
t("unmatched traffic (default) is dropped on {dev}.",
  "{dev} で未一致トラフィック（デフォルト）は破棄されます。")
t("routing rule destination must be either a prefix of a network address, or a hardware address.",
  "ルーティングルールの宛先はネットワークアドレスのプレフィックスまたはハードウェアアドレスである必要があります。")
t("routing rule source is a portN:logical_addr combination.",
  "ルーティングルールのソースは portN:論理アドレス の組み合わせです。")
t("routing rule source address must be either a prefix of a network address, or a hardware address.",
  "ルーティングルールのソースアドレスはネットワークアドレスのプレフィックスまたはハードウェアアドレスである必要があります。")
t("update route {route} via {old_port} -> {new_port} on {dev}.",
  "{dev} のルート {route} を {old_port} -> {new_port} に更新しました。")
t("added route {route} via {port} on {dev}.",
  "{dev} にルート {route} を {port} 経由で追加しました。")
t("removed route", "ルートを削除しました")
t("route table for {dev} cleared.", "{dev} のルートテーブルをクリアしました。")
t("broadcast traffic will now be {status}.", "ブロードキャストトラフィックは {status} に変更されました。")
t("forwarded", "転送")
t("dropped", "破棄")

# Scan
t("scan and list devices that are accessible through a remote debugger.",
  "リモートデバッガーからアクセス可能なデバイスをスキャンして一覧表示。")
t("scan for devices matching the type reachable from a source.",
  "ソースから到達可能な指定タイプのデバイスをスキャン。")
t("all device types", "すべてのデバイスタイプ")
t("users", "ユーザー")
t("network switches", "ネットワークスイッチ")
t("network routers", "ネットワークルーター")
t("network taps", "ネットワークタップ")
t("network firewalls", "ネットワークファイアウォール")
t("dns servers", "DNSサーバー")
t("dhcp servers", "DHCPサーバー")
t("tower links", "タワーリンク")
t("virtual machines", "仮想マシン")
t("all network nodes", "すべてのネットワークノード")
t("scanning from {srcaddr} for {tft}", "{srcaddr} から {tft} をスキャン中")
t("no {device_type} accessible", "{device_type} にアクセスできません")
t("scans from {srcaddr} for {tft}", "{srcaddr} から {tft} をスキャン")

# SFTP
t("remote tool for file backup/migration.", "ファイルバックアップ/移行用リモートツール。")
t("show data and configuration files.", "データと設定ファイルを表示。")
t("copy file from source to dst.", "ソースから宛先にファイルをコピー。")
t("remove file from source.", "ソースからファイルを削除。")
t("no files/data found on {dev}.", "{dev} にファイル/データが見つかりません。")
t("Missing filename.", "ファイル名がありません。")
t("insufficient storage on {dev} for sftp copy of '{filename}'.",
  "{dev} のストレージ不足のため '{filename}' のsftpコピーができません。")
t("copied '{filename}' (size={size}) from {dev} to {dst} as '{result}'.",
  "'{filename}'（サイズ={size}）を {dev} から {dst} に '{result}' としてコピーしました。")
t("bad filename '{badname}'.", "無効なファイル名 '{badname}'。")
t("file '{badname}' not found on {dev}.", "ファイル '{badname}' が {dev} に見つかりません。")
t("removed all user files {dev}.", "{dev} のすべてのユーザーファイルを削除しました。")
t("deleted '{filename}' (size={size}) on {dev}.", "{dev} の '{filename}'（サイズ={size}）を削除しました。")

# STP
t("configure spanning tree protocol on managed switches.", "マネージドスイッチのスパニングツリープロトコルを設定。")
t("show stp status.", "STPステータスを表示。")
t("enable/disable stp.", "STPを有効化/無効化。")
t("configure stp priority value.", "STPの優先度値を設定。")
t("status", "ステータス")
t("stp is {status} on {addr}", "STPは {addr} で {status} です")
t("enabled", "有効")
t("priority", "優先度")
t("role-in-tree", "ツリー内の役割")
t("root bridge", "ルートブリッジ")
t("designated bridge", "指定ブリッジ")
t("root port", "ルートポート")
t("path cost", "パスコスト")
t("stp {state_s} on managed switch {addr}.", "マネージドスイッチ {addr} のSTPを {state_s} にしました。")
t("priority value must be a number", "優先度値は数値である必要があります")
t("stp priority managed switch {addr} changed from {old_val} -> {new_val}.",
  "マネージドスイッチ {addr} のSTP優先度を {old_val} -> {new_val} に変更しました。")

# Trace
t("trace network traversal from a device to another device.", "デバイス間のネットワークトラバーサルをトレース。")
t("perform a network graph trace from address2 to address1 using the debugger.",
  "デバッガーを使用してaddress2からaddress1へのネットワークグラフトレースを実行。")
t("trace with specific traffic type.", "特定のトラフィックタイプでトレース。")
t("device {to_addr} ({ctxaddr}) unreachable from {src}",
  "デバイス {to_addr}（{ctxaddr}）は {src} から到達不能")
t("trace completed.", "トレース完了。")

# Try/catch
t("try a command, run another if failed.", "コマンドを試行し、失敗した場合は別のコマンドを実行。")
t("try running cmd1, then cmd2 if successful, otherwise cmd3.",
  "cmd1を実行し、成功すればcmd2、失敗すればcmd3を実行。")

# VLAN
t("manage virtual local area networks.", "仮想LANを管理。")
t("show virtual lan setup on the managed switch.", "マネージドスイッチの仮想LAN設定を表示。")
t("tag a vlan ID to port(s) on the managed switch.", "マネージドスイッチのポートにVLAN IDをタグ付け。")
t("untag a vlan ID from port(s) on the managed switch.", "マネージドスイッチのポートからVLAN IDのタグを解除。")
t("clear vlan configuration on the managed switch.", "マネージドスイッチのVLAN設定をクリア。")
t("No VLAN ports configured.", "VLANポートが設定されていません。")
t("VLAN port tags", "VLANポートタグ")
t("Exceeded max VLAN tag length {maxlen}.", "VLAN タグの最大長 {maxlen} を超えました。")
t("Invalid VLAN tag, must begin with '#' and contains alpha-numeric characters.",
  "無効なVLANタグ。'#'で始まり英数字を含む必要があります。")
t("Invalid port '{portid}'.", "無効なポート '{portid}'。")
t("Invalid subinterface name '{subif}', must be alpha-numeric or '.'.",
  "無効なサブインターフェース名 '{subif}'。英数字または '.' である必要があります。")
t("Added subinterface {subif} with VLAN tag {tag} to port '{portid}'",
  "ポート '{portid}' にVLANタグ {tag} のサブインターフェース {subif} を追加しました")
t("Added VLAN tag {tag} to port '{portid}'", "ポート '{portid}' にVLANタグ {tag} を追加しました")
t("Removed VLAN tag(s) from subinterface '{portid}'", "サブインターフェース '{portid}' からVLANタグを削除しました")
t("Removed VLAN tag(s) from port '{portid}'", "ポート '{portid}' からVLANタグを削除しました")
t("Cleared all VLAN tags on '{devaddr}'", "'{devaddr}' のすべてのVLANタグをクリアしました")

# VM management
t("manage virtual machines.", "仮想マシンを管理。")
t("show virtual machines on the server.", "サーバー上の仮想マシンを表示。")
t("create a virtual machine on the server.", "サーバーに仮想マシンを作成。")
t("device {dev_addr} is a virtual machine.", "デバイス {dev_addr} は仮想マシンです。")
t("no virtual machines configured on {dev_addr}.", "{dev_addr} に仮想マシンが設定されていません。")
t("virtual machine {vmname} created with netaddr {netaddr}.",
  "仮想マシン {vmname} をネットアドレス {netaddr} で作成しました。")
t("virtual machine {vmname} created.", "仮想マシン {vmname} を作成しました。")
t("to start/stop/delete the virtual machine:", "仮想マシンの開始/停止/削除:")

# Watch
t("watch the device information/programs through a remote debugger.",
  "リモートデバッガーでデバイス情報/プログラムを監視。")
t("watch the specified device.", "指定デバイスを監視。")
t("watch any moused-over device.", "マウスオーバーしたデバイスを監視。")
t("no device being watched", "監視中のデバイスなし")
t("hover mouse over a device to get information.", "デバイスにマウスオーバーして情報を取得。")
t("watching", "監視中")
t("ctrl+c to return", "Ctrl+Cで戻る")
t("hit 'tab' key to cycle different views", "'Tab'キーで表示を切替")
t("Request traffic class", "リクエストトラフィッククラス")

# Error messages
t("invalid command, type '{man}' for help.", "無効なコマンド。'{man}' と入力してヘルプを表示。")
t("{viaport} not a valid port on {dev}.", "{viaport} は {dev} の有効なポートではありません。")
t("debugger {dbgaddr} not accessible.", "デバッガー {dbgaddr} にアクセスできません。")
t("use '{lstdbg}' to display accessible remote debuggers.",
  "'{lstdbg}' でアクセス可能なリモートデバッガーを表示してください。")
t("{device_type} {dev_addr} not accessible via debugger {deb_addr}.",
  "{device_type} {dev_addr} はデバッガー {deb_addr} 経由でアクセスできません。")
t("use '{scan}' to see which {device_type} are accessible.",
  "'{scan}' でアクセス可能な {device_type} を確認してください。")
t("device {dev_addr} is not a {req_type}", "デバイス {dev_addr} は {req_type} ではありません")
t("configure DNS with the '{dns}' command.", "'{dns}' コマンドでDNSを設定してください。")
t("no error.", "エラーなし。")
t("cannot reach DNS to resolve '{fqdn}'.", "'{fqdn}' を解決するDNSに到達できません。")
t("cannot connect.", "接続できません。")
t("address '{addr}' is not a valid network/hardware address.",
  "アドレス '{addr}' は有効なネットワーク/ハードウェアアドレスではありません。")
t("hardware addresses consists only of numbers.", "ハードウェアアドレスは数字のみで構成されます。")
t("network addresses must begin with a '@' character.", "ネットワークアドレスは '@' で始まる必要があります。")
t("load", "負荷")
t("Check if installed and running with sufficient capacity?",
  "十分な容量でインストール・実行されていますか？")
t("'{dstaddr}' is not accessible from '{dbgaddr}':",
  "'{dstaddr}' は '{dbgaddr}' からアクセスできません:")
t("If {dst} is connected to {src} through any router, ensure routes are configured.",
  "{dst} がルーター経由で {src} に接続されている場合、ルートが設定されていることを確認してください。")
t("Ensure {tft} traffic from {src} to {dst} is allowed by all firewalls along the path.",
  "{src} から {dst} への {tft} トラフィックが経路上のすべてのファイアウォールで許可されていることを確認してください。")
t("Use trace/ping utilities. you may also try to connect your debugger closer to the server.",
  "trace/pingユーティリティを使用してください。デバッガーをサーバーに近づけて接続することもできます。")
t("Check if target still has network bandwidth to handle requests.",
  "ターゲットがリクエストを処理するネットワーク帯域幅をまだ持っているか確認してください。")

# ============================================================
# BATCH 4: Game settings / Main menu / Save-Load / Game Over
# ============================================================
t("Day 0", "0日目")
t("Only host can save game", "ホストのみゲームを保存できます")
t("Cannot save in tutorial", "チュートリアル中は保存できません")
t("Game is paused", "ゲーム一時停止中")
t("Game is running", "ゲーム実行中")
t("Public joinable", "パブリック参加可能")
t("Disallow public join", "パブリック参加を禁止")
t("Join ID (friends only)", "参加ID（フレンドのみ）")
t("Allow public join", "パブリック参加を許可")
t("Steam lobby settings", "Steamロビー設定")
t("Back to game", "ゲームに戻る")
t("Change game settings", "ゲーム設定を変更")
t("Toggle wiki/help", "Wiki/ヘルプの切替")
t("Give feedback / bug report", "フィードバック/バグ報告")
t("Save current game", "現在のゲームを保存")
t("Quit to main menu", "メインメニューに戻る")
t("Quit to desktop", "デスクトップに戻る")

# Game mechanics
t("Backend service.", "バックエンドサービス。")
t("Manifest probability is {prob}%", "出現確率は {prob}%")
t("Malicious.", "悪意あり。")
t("Chooses random providers.", "ランダムなプロバイダーを選択。")
t("Chooses same provider.", "同じプロバイダーを選択。")
t("Chooses providers by market share.", "市場シェアでプロバイダーを選択。")
t("Out-of-band random peer selection", "帯域外ランダムピア選択")
t("Requires peer tracking provider.", "ピアトラッキングプロバイダーが必要。")

# Tower Catalog
t("Tower Catalog", "タワーカタログ")
t("Show unseen/locked only", "未閲覧/ロック済みのみ表示")
t("Floors", "フロア")
t("New floors can be unlocked by surviving until day 40 on an endless mode game.",
  "エンドレスモードで40日目まで生存すると新しいフロアがアンロックされます。")
t("Loading...", "読み込み中...")
t("Users", "ユーザー")
t("Unlocked", "アンロック済み")
t("Locked", "ロック中")
t("MY Location", "現在地")
t("Possible users", "出現可能ユーザー")
t("Behaviors", "行動パターン")

# Clipboard
t("Network address copied to clipboard", "ネットワークアドレスをクリップボードにコピー")
t("Hardware address copied to clipboard", "ハードウェアアドレスをクリップボードにコピー")
t("View clipboard", "クリップボードを表示")
t("Close clipboard", "クリップボードを閉じる")
t("The device unit's product name", "デバイスユニットの製品名")
t("The username", "ユーザー名")
t("The hardware address", "ハードウェアアドレス")
t("The network address", "ネットワークアドレス")
t("Copy network address", "ネットワークアドレスをコピー")
t("This address is currently copied (right click textboxes to paste).",
  "このアドレスはコピー済みです（テキストボックスを右クリックで貼り付け）。")
t("Copy hardware address", "ハードウェアアドレスをコピー")
t("Copy domain name", "ドメイン名をコピー")
t("The user is hosting a service with this domain", "ユーザーがこのドメインでサービスをホスト中")
t("This domain name is currently copied", "このドメイン名はコピー済みです")
t("unassigned", "未割当")
t("copy", "コピー")

# Feedback form
t("You are sending faster than we can handle. Try again in a moment.",
  "送信速度が速すぎます。少し待ってからもう一度お試しください。")
t("We have reached the maximum input for processing! If you are experiencing an issue, please reach out to the developers via discord.",
  "処理可能な入力の上限に達しました！問題が発生している場合は、Discord経由で開発者にお問い合わせください。")
t("Minimize", "最小化")
t("Thank you for your input!", "ご入力ありがとうございます！")
t("More details would be super helpful! The more details you can provide, the better we can help.",
  "詳細な情報をいただけると大変助かります！詳しく書いていただけるほど、より良いサポートが可能です。")
t("Feedback / Bug Report", "フィードバック / バグ報告")
t("We would love to hear feedback/bug report from you\nPlease let us know how we can improve.",
  "フィードバック/バグ報告をお待ちしています\n改善のためのご意見をお聞かせください。")
t("I want to provide", "報告内容")
t("Feedback", "フィードバック")
t("Bug Report", "バグ報告")
t("Short description of your feedback/bug report", "フィードバック/バグ報告の簡単な説明")
t("Your name", "お名前")
t("<Optional> For credit of the discovery/feedback", "<任意> 発見/フィードバックのクレジット用")
t("Your email", "メールアドレス")
t("<Optional> For futher contact if necessary", "<任意> 必要時の追加連絡用")
t("Happiness", "満足度")
t("Long description of your feedback/bug report with details", "フィードバック/バグ報告の詳細な説明")
t("Send Feedback/Bug Report", "フィードバック/バグ報告を送信")
t("Submitting feedback / bug report", "フィードバック/バグ報告を送信中")
t("Thank you for your response", "ご回答ありがとうございます")

# Difficulty selection
t("Initial Difficulty Selection", "難易度選択")
t("This game is a complex sandbox which may be a frustrating experience for new players. An easier option is available to minimize the frustrating aspects of the game.",
  "このゲームは複雑なサンドボックスゲームで、初めてのプレイヤーにはストレスがかかるかもしれません。ストレスを軽減するイージーオプションが利用可能です。")
t("Easy Mode", "イージーモード")
t("I just want to take it easy.", "のんびりやりたい。")
t("In easy mode, days are longer and income is increased, with less malfunction and cyber events.",
  "イージーモードでは、日が長くなり収入が増加し、故障やサイバーイベントが減少します。")
t("Standard Mode", "スタンダードモード")
t("I can handle standard mode.", "スタンダードモードで大丈夫。")
t("In standard mode, devices will randomly fail after their warranty runs out.",
  "スタンダードモードでは、保証期間終了後にデバイスがランダムに故障します。")
t("Hard Mode", "ハードモード")
t("Bring it on.", "かかってこい。")
t("In hard mode, power outage and surge events occur more frequently.",
  "ハードモードでは、停電やサージイベントがより頻繁に発生します。")
t("Zen Mode", "禅モード")
t("Stress free for me.", "ストレスフリーで。")
t("Zen mode is identical to standard mode except floors will not be automatically built.",
  "禅モードはスタンダードモードと同じですが、フロアが自動的に建設されません。")

# Loading screen tips
t("Loading", "読み込み中")
t("Did you know?", "知っていましたか？")
t("To debug/configure a target device, the [color=yellow]debugger[/color] needs to be able to reach the device through the network.",
  "ターゲットデバイスをデバッグ/設定するには、[color=yellow]デバッガー[/color]がネットワーク経由でデバイスに到達できる必要があります。")
t("The [color=yellow]alias[/color] command allows you to create your own personal shorthand commands (e.g., 'ds' for 'dstat').",
  "[color=yellow]alias[/color] コマンドで独自の短縮コマンドを作成できます（例: 'dstat' の代わりに 'ds'）。")
t("The cron routine allows scheduled command execution. It is useful for automating tasks like periodic DNS resolution or device checks.",
  "cronルーチンでコマンドのスケジュール実行が可能です。定期的なDNS解決やデバイスチェックなどの自動化に便利です。")
t("A server can only function as a DNS server is it has \"[color=yellow]dns-lite[/color]\" or \"[color=yellow]dns-server[/color]\" program installed and running.",
  "サーバーがDNSサーバーとして機能するには「[color=yellow]dns-lite[/color]」または「[color=yellow]dns-server[/color]」プログラムがインストールされ実行中である必要があります。")
t("You may set multiple designated DNS servers for a device/client.",
  "デバイス/クライアントに複数のDNSサーバーを指定できます。")
t("Network switches are easy to use as it does not need any configuration.",
  "ネットワークスイッチは設定不要で簡単に使えます。")
t("Routers performs longest [color=yellow]prefix[/color] matching for route selection. Use network addresses grouping to consolidate routes effectively.",
  "ルーターはルート選択に最長[color=yellow]プレフィックス[/color]マッチングを使用します。ネットワークアドレスのグループ化でルートを効果的に統合できます。")
t("All users will periodically do a DHCP request broadcast. Use the [color=yellow]dhcp[/color] command to configure a dhcp server to automate network address assignments.",
  "すべてのユーザーは定期的にDHCPリクエストをブロードキャストします。[color=yellow]dhcp[/color] コマンドでDHCPサーバーを設定し、ネットワークアドレスの割り当てを自動化できます。")
t("You can run more processes on a server than its installed CPU to overcommit. Processes may take longer to produce when overcommitted.",
  "インストール済みCPU以上のプロセスをサーバーで実行してオーバーコミットできます。オーバーコミット時は生産に時間がかかる場合があります。")
t("Firewall rules on network addresses are based on prefixes. [color=yellow]@abc[/color] will match all addresses starting with [color=yellow]@abc[/color].",
  "ネットワークアドレスのファイアウォールルールはプレフィックスベースです。[color=yellow]@abc[/color] は [color=yellow]@abc[/color] で始まるすべてのアドレスに一致します。")
t("Becareful when setting firewall rules, as you may get [color=red]locked out[/color] of managing your own device through the debugger.",
  "ファイアウォールルール設定時は注意してください。デバッガー経由で自分のデバイスを管理できなくなる[color=red]ロックアウト[/color]が発生する可能性があります。")
t("You can host your own services for additional income using [color=yellow]The Registry[/color] application.",
  "[color=yellow]The Registry[/color] アプリケーションで独自のサービスをホストして追加収入を得られます。")
t("Users will pay at the end of the day based on their lowest satisfaction level.",
  "ユーザーは一日の最低満足度に基づいて日末に支払いを行います。")
t("Certain users may have [color=red]malicious behaviors[/color]. Use the network tap and pcap to analyze the traffic!",
  "特定のユーザーは[color=red]悪意ある行動[/color]を取ることがあります。ネットワークタップとpcapでトラフィックを分析しましょう！")
t("Press and hold the \"T\" key while dragging the mouse around to select and move multiple devices.",
  "\"T\"キーを押しながらマウスをドラッグして、複数のデバイスを選択・移動できます。")
t("Press and hold the \"G\" key to snap the mouse to the grid.",
  "\"G\"キーを押し続けるとマウスがグリッドにスナップします。")
t("Pressing the \"R\" key while holding a plug/device will rotate it.",
  "プラグ/デバイスを持った状態で\"R\"キーを押すと回転します。")
t("Double clicking and holding the left-mouse button allows you to drag cables freely. This is useful for organizing your cables.",
  "左マウスボタンをダブルクリック＆ホールドでケーブルを自由にドラッグできます。ケーブルの整理に便利です。")
t("There are 3 methods of motion. You can [color=yellow]pan with right click[/color], [color=yellow]zoom with scroll wheel[/color] and [color=yellow]elevate between floors with the elevator or WASD[/color].",
  "移動方法は3つあります。[color=yellow]右クリックでパン[/color]、[color=yellow]スクロールホイールでズーム[/color]、[color=yellow]エレベーターまたはWASDでフロア間移動[/color]。")
t("Proposals can be submitted to the Secretariat to unlock new features for your tower.",
  "事務局に提案を提出して、タワーの新機能をアンロックできます。")
t("The sftp routine allows remote backup of device configurations to another device. Use it to protect important configurations.",
  "sftpルーチンでデバイス設定を別のデバイスにリモートバックアップできます。重要な設定の保護に使用してください。")
t("The rip routine allows automated route discoveries between routers. Use it to automatically update routing tables.",
  "ripルーチンでルーター間の自動ルート検出が可能です。ルーティングテーブルの自動更新に使用してください。")
t("Buying [color=yellow]cables in bulk[/color] will cause them to share an identical length.",
  "[color=yellow]ケーブルをまとめ買い[/color]すると、同一の長さになります。")
t("As your network grows large, hardware replacements due to malfunction may be overwhelming. Consider using the [color=yellow]auto-replace[/color] option in DMarket.",
  "ネットワークが大きくなると、故障によるハードウェア交換が大変になるかもしれません。DMarketの[color=yellow]自動交換[/color]オプションの使用を検討してください。")
t("Network worms may spread (with early warnings) throughout your network! Use firewalls and the sftp/program routines to contain and remove them.",
  "ネットワークワームが（事前警告付きで）ネットワーク全体に拡散する可能性があります！ファイアウォールとsftp/programルーチンで封じ込めと除去を行いましょう。")
t("User traffic tapping/analysis is key to keep a botnet up and running in Decentro mode.",
  "Decentroモードでボットネットを維持するには、ユーザートラフィックのタップ/分析が鍵です。")

# Main menu / credits
t("CHANGELOGS", "変更履歴")
t("ANNOUNCEMENTS @ Pocosia Studios", "お知らせ @ Pocosia Studios")
t("TOWER NETWORKING INC.", "TOWER NETWORKING INC.")
t("Greetings from Pocosia Studios!\n\nThanks for supporting our game.\n\nHere are some latest updates:",
  "Pocosia Studiosからのご挨拶！\n\nゲームを応援いただきありがとうございます。\n\n最新の更新情報:")
t("Don't show again", "今後表示しない")
t("OK", "OK")
t("BACK TO MAIN MENU", "メインメニューに戻る")
t("A NETWORK GRAPH SIMULATION GAME BY POCOSIA STUDIOS", "POCOSIA STUDIOSによるネットワークグラフシミュレーションゲーム")
t("CREDITS", "クレジット")
t("COMMUNITY", "コミュニティ")
t("PLAYTESTERS", "プレイテスター")
t("LOCALIZATION", "ローカライズ")
t("AUDIO-VISUAL SOURCES", "オーディオビジュアルソース")
t("Close", "閉じる")

# Advanced game options
t("Advanced game options", "ゲーム詳細設定")
t("Starting cash for the run.", "ゲーム開始時の所持金。")
t("Starting cash", "初期資金")
t("Length of day in seconds for the run.", "1日の長さ（秒）。")
t("Day period (seconds)", "日数期間（秒）")
t("Maximum number of days allowed to be in debt before losing the game.",
  "ゲームオーバーになるまでの借金可能日数。")
t("Maximum days in debt", "最大借金日数")
t("Admin fee cost per user.", "ユーザーあたりの管理費。")
t("Cost to install a network socket in the tower (using Socketeer).",
  "タワーにネットワークソケットを設置するコスト（Socketeer使用）。")
t("Socket installation cost", "ソケット設置コスト")
t("Limit the total floors that will be built. Set to 0 for no limit.",
  "建設するフロアの上限を制限。0で無制限。")
t("Tower floor limit", "タワーフロア上限")
t("In free play, you won't lose the game", "フリープレイではゲームオーバーになりません")
t("Free-play", "フリープレイ")
t("DISABLED", "無効")
t("Start with all routines, programs and devices unlocked.", "すべてのルーチン、プログラム、デバイスをアンロック状態で開始。")
t("Start with all tech enabled", "全技術を有効にして開始")
t("If enabled, power is free on data centers.", "有効にすると、データセンターの電力が無料になります。")
t("Waive power fee", "電力料金免除")
t("If enterprise users will automatically create DNS mapping. Only available in easy mode.",
  "エンタープライズユーザーが自動的にDNSマッピングを作成するか。イージーモードでのみ利用可能。")
t("Auto create DNS mappings", "DNSマッピング自動作成")
t("If NetShell will print connectivity help in game.", "NetShellがゲーム内で接続ヘルプを表示するか。")
t("Print connectivity hints", "接続ヒントを表示")
t("If network errors are visible with naked eye (i.e., Overloaded).",
  "ネットワークエラーが目視で確認できるか（例: 過負荷）。")
t("See errors/hints in world", "ワールド内でエラー/ヒントを表示")
t("If enabled, device never gets overloaded due to network bandwidth.",
  "有効にすると、ネットワーク帯域幅によるデバイスの過負荷がなくなります。")
t("Device has infinite bandwidth", "デバイスの帯域幅無制限")
t("If debugger actions (i.e., watch) costs bandwidth.", "デバッガーアクション（watch等）が帯域幅を消費するか。")
t("Debugger access bandwidth", "デバッガーアクセス帯域幅")
t("Adds a layer of difficulty when moving devices around.", "デバイス移動時の難易度が上がります。")
t("Device movement collisions", "デバイス移動の衝突判定")
t("DNS mappings is localized.", "DNSマッピングがローカライズされます。")
t("DNS local mappings", "DNSローカルマッピング")
t("Player installed programs autostart.", "プレイヤーがインストールしたプログラムが自動起動。")
t("Autostart installed programs", "インストール済みプログラムの自動起動")
t("All requests requires network address assigned on source.",
  "すべてのリクエストでソースにネットワークアドレスの割り当てが必要。")
t("Requests needs netaddr", "リクエストにネットアドレスが必要")
t("The likelihood of devices to malfunction if exceeded their warranty.",
  "保証期間超過時のデバイス故障確率。")
t("Device malfunction prob.", "デバイス故障確率")
t("The likelihood of power outage events occuring.", "停電イベントの発生確率。")
t("Power outage events prob.", "停電イベント確率")
t("The likelihood of power surge events occurring.", "サージイベントの発生確率。")
t("Power surge events prob.", "サージイベント確率")
t("The likelihood of a cyberattack (i.e., worms, DDOS) occuring.",
  "サイバー攻撃（ワーム、DDoS等）の発生確率。")
t("Cyberattack events prob.", "サイバー攻撃イベント確率")
t("The likelihood of users resetting their hardware if they go below their SLA level.",
  "SLAレベル以下になった際にユーザーがハードウェアをリセットする確率。")
t("User hardware reset prob.", "ユーザーハードウェアリセット確率")
t("Longer periods means new floors are build less frequently.",
  "期間が長いほどフロアの建設頻度が低くなります。")
t("Floor build period multiplier", "フロア建設期間の倍率")
t("Longer periods means more time before a floor is automatically accepted.",
  "期間が長いほどフロアが自動承認されるまでの時間が長くなります。")
t("Max days in floor queue", "フロアキュー最大日数")
t("Affects how the total network fee paid by users.",
  "ユーザーが支払う総ネットワーク料金に影響します。")
t("User fee payment multiplier", "ユーザー料金支払い倍率")
t("User in grace periods will not trigger SLA breach events.",
  "猶予期間中のユーザーはSLA違反イベントをトリガーしません。")
t("User grace days multiplier", "ユーザー猶予日数の倍率")
t("Affects how much time can pass between a SLA warning and the actual SLA breach.",
  "SLA警告から実際のSLA違反までの時間に影響します。")
t("SLA breach timer multiplier", "SLA違反タイマーの倍率")
t("The longer the warranty period, the longer the device stays functional.",
  "保証期間が長いほど、デバイスが機能し続ける期間も長くなります。")
t("Warranty period multiplier", "保証期間の倍率")
t("How fast admin fee should scale with number of days passed.",
  "経過日数に応じた管理費のスケーリング速度。")
t("Admin fee scaling factor", "管理費スケーリング係数")
t("The daily fee per device for automatic replacement on malfunction.",
  "故障時の自動交換のデバイスあたり日額。")
t("Auto replace daily rate", "自動交換の日額")
t("Maximum length of network addresses (excluding '@').",
  "ネットワークアドレスの最大長（'@'を除く）。")
t("Max netaddr length", "最大ネットアドレス長")

# Lobby / multiplayer
t("Welcome back", "おかえりなさい")
t("Join", "参加")
t("Join a game", "ゲームに参加")
t("Join ID", "参加ID")
t("Public lobbies", "パブリックロビー")
t("Refresh lobbies", "ロビーを更新")
t("Multiplayer is currently disabled", "マルチプレイヤーは現在無効です")
t("Resume game", "ゲームを再開")
t("That's awesome! Hope to see you during release.", "すばらしい！リリース時にお会いしましょう。")
t("What's New?", "新着情報")
t("Rack Mounting", "ラックマウント")
t("Early access release: Game is in active development, hit f8 for bug report.",
  "早期アクセス: ゲームは開発中です。F8でバグ報告できます。")
t("Latest community news", "最新コミュニティニュース")
t("Start a new game", "新しいゲームを開始")
t("Load from saves", "セーブデータを読み込む")
t("Wishlist the game on Steam", "Steamでウィッシュリストに追加")
t("Tower catalogue", "タワーカタログ")
t("Read changelogs", "変更履歴を読む")
t("Show credits", "クレジットを表示")
t("Music by Karl Casey @ White Bat Audio", "音楽: Karl Casey @ White Bat Audio")
t("Tutorials", "チュートリアル")
t("Scenarios", "シナリオ")
t("Intern (Easy mode)", "インターン（イージーモード）")
t("Admin (Standard)", "管理者（スタンダード）")
t("Architect (Hard mode)", "アーキテクト（ハードモード）")
t("Co-op (Multiplayer mode)", "Co-op（マルチプレイヤーモード）")
t("Zen (No auto-build mode)", "禅（自動建設なしモード）")
t("Nirvana (Hard without auto-build)", "涅槃（ハード＋自動建設なし）")
t("Show advanced options", "詳細設定を表示")
t("Hide advanced options", "詳細設定を隠す")
t("Achievements/unlocks enabled", "実績/アンロック有効")
t("Achievements/unlocks disabled", "実績/アンロック無効")
t("Player Name", "プレイヤー名")
t("Host a game", "ゲームをホスト")
t("Testing", "テスト")
t("World seed", "ワールドシード")
t("Randomize seed.", "シードをランダム化。")
t("Difficulty preset", "難易度プリセット")
t("Play Solo", "ソロプレイ")
t("Play with Friends", "フレンドとプレイ")
t("No lobbies found", "ロビーが見つかりません")
t("Host", "ホスト")
t("Game Mode", "ゲームモード")
t("# Players", "プレイヤー数")
t("Your operating system is incompatible with the host.", "お使いのOSはホストと互換性がありません。")
t("Resume save: {savename}", "セーブを再開: {savename}")
t("Host the saved game", "セーブしたゲームをホスト")
t("Saving game... (PLEASE WAIT)", "ゲームを保存中...（お待ちください）")
t("Overwrite save", "セーブを上書き")
t("overwrites the save '{savename}'", "セーブ '{savename}' を上書きします")
t("Create save", "セーブを作成")
t("create a new save", "新しいセーブを作成")
t("Saved successfully", "保存に成功しました")
t("Saved success", "保存成功")
t("Failed to save: {errmsg}", "保存に失敗: {errmsg}")
t("Saved Games", "セーブデータ")
t("delete the save", "セーブを削除")
t("Delete save", "セーブを削除")
t("Filter by save name...", "セーブ名でフィルター...")

# Settings
t("Game", "ゲーム")
t("Graphics", "グラフィック")
t("Audio", "オーディオ")
t("Windowed", "ウィンドウ")
t("Fullscreen", "フルスクリーン")
t("Hide", "非表示")
t("Show", "表示")
t("Off", "オフ")
t("On", "オン")
t("Minimal", "最小")
t("Normal", "標準")
t("High", "高")
t("Reset defaults", "デフォルトにリセット")
t("Save settings", "設定を保存")
t("Audio settings", "オーディオ設定")
t("Master volume", "マスター音量")
t("SFX volume", "効果音音量")
t("Music volume", "BGM音量")
t("Language settings", "言語設定")
t("Language", "言語")
t("ENGLISH", "英語")
t("TEST", "テスト")
t("Misc settings", "その他の設定")
t("Max FPS", "最大FPS")
t("Physics Simulation", "物理シミュレーション")
t("Show announcements on start", "起動時にお知らせを表示")
t("Use DMarket v2", "DMarket v2を使用")
t("If time speed-up/slow-down controls in game will affect physics simulation.",
  "ゲーム内の時間加速/減速操作が物理シミュレーションに影響するか。")
t("Time Control Affects Physics/Animations", "時間操作が物理/アニメーションに影響")
t("Show username", "ユーザー名を表示")
t("Show help guides", "ヘルプガイドを表示")
t("Camera movement settings", "カメラ移動設定")
t("Mouse panning speed", "マウスパン速度")
t("Keyboard (wasd) panning speed", "キーボード（WASD）パン速度")
t("Drag (right click) panning speed", "ドラッグ（右クリック）パン速度")
t("Holding shift will pan camera", "Shiftキーを押しながらカメラをパン")
t("Window settings", "ウィンドウ設定")
t("Vertical sync", "垂直同期")
t("Window mode", "ウィンドウモード")
t("Shader settings", "シェーダー設定")
t("RGB shift", "RGBシフト")
t("CRT monitor effect", "CRTモニターエフェクト")
t("Flickering lights effect", "ちらつき照明エフェクト")

# Game Over / Statistics
t("LOADING", "読み込み中")
t("Game Statistics", "ゲーム統計")
t("Game Over", "ゲームオーバー")
t("Termination reason", "終了理由")
t("Achievements/unlock enabled", "実績/アンロック有効")
t("Difficulty", "難易度")
t("Days in operation", "運営日数")
t("Total data centers", "データセンター合計")
t("Total service floors", "サービスフロア合計")
t("Total users", "ユーザー合計")
t("User majority", "ユーザーの多数派")
t("Daily satiety average", "日次平均満足度")
t("Daily income average", "日次平均収入")
t("Total proposals submitted", "提出済み提案合計")
t("Total network outages notice issued", "発行済みネットワーク停止通知合計")
t("Total loans taken", "借入合計")
t("Total days in debt", "借金日数合計")
t("Total scheduled power outages occurred", "計画停電発生回数")
t("Total unscheduled power outages occurred", "予期せぬ停電発生回数")
t("Total power surge occurred", "サージ発生回数")
t("Total devices malfunction due to end of life", "寿命による故障デバイス合計")
t("Total devices damaged by surge", "サージ破損デバイス合計")
t("Total cyberattacks occurred", "サイバー攻撃発生回数")
t("Total coffee drank", "コーヒー消費回数")
t("Total tea drank", "お茶消費回数")
t("Accept", "承認")

# Tutorial UI
t("tutorial step name", "チュートリアルステップ名")
t("Close tutorial", "チュートリアルを閉じる")
t("View tutorial", "チュートリアルを表示")
t("Activated tutorial", "有効化されたチュートリアル")
t("activated tutorial", "有効化されたチュートリアル")
t("Tutorial scenario ended.", "チュートリアルシナリオが終了しました。")
t("Click OK to exit to main menu.", "OKをクリックしてメインメニューに戻ります。")

# Onboarding / hints
t("welcome onboard", "ようこそ")
t("Press F1 to refer to the tutorial recap (your learning materials). ",
  "F1キーでチュートリアルの振り返り（学習資料）を参照できます。")
t("purchase cables from D-Market2 app", "D-Market2アプリからケーブルを購入")
t("device/user access to the debugger for network troubleshooting",
  "ネットワークトラブルシューティング用にデバイス/ユーザーがデバッガーにアクセス")
t("connect devices and users with a switch", "スイッチでデバイスとユーザーを接続")
t("launch Surveyor app to observe tower residents' needs", "Surveyorアプリでタワー住民のニーズを観察")
t("install DNS program on server (Boulder series) using netsh\ncommand: [program install dns-lite on <server_addr>]\ncommand: [program start dns-lite on <server_addr>]",
  "netshを使用してサーバー（Boulderシリーズ）にDNSプログラムをインストール\nコマンド: [program install dns-lite on <server_addr>]\nコマンド: [program start dns-lite on <server_addr>]")
t("set up riser link between floors through Tower Link app", "Tower Linkアプリでフロア間のライザーリンクを設定")
t("consumer access to DNS server", "コンシューマーのDNSサーバーへのアクセス")
t("correct DNS mapping through netsh \ncommand: [dns map <producer_domain> as <producer_addr>]",
  "netshで正しいDNSマッピングを設定\nコマンド: [dns map <producer_domain> as <producer_addr>]")
t("at least one tower resident's satiety > 50%", "少なくとも1人のタワー住民の満足度が50%以上")
t("accept at least one new floor through 'The Secretariat' app", "'The Secretariat'アプリで少なくとも1つの新しいフロアを承認")
t("launch new app from Rocket Store app", "Rocket Storeアプリから新しいアプリを起動")
t("self-register domain name as stream-voice service provider from 'The Registry' app",
  "'The Registry'アプリからストリームボイスサービスプロバイダーとしてドメイン名を自己登録")
t("configure route entries on the router", "ルーターにルートエントリを設定")
t("protect and support essential devices with UPS", "UPSで重要なデバイスを保護・支援")
t("recycle unwanted items at the recycling center", "リサイクルセンターで不要アイテムをリサイクル")
t("unlock proposals from The Secretariat app", "The Secretariatアプリから提案をアンロック")
t("protect devices/users from malicious activities using a firewall",
  "ファイアウォールを使用してデバイス/ユーザーを悪意ある活動から保護")
t("onboarding material", "オンボーディング資料")
t("dismiss", "閉じる")

# Hint system
t("[i][color=#18fa80]Debugger Alice (Debugger)[/color][/i]: Allow me to check for issues!",
  "[i][color=#18fa80]デバッガーAlice（デバッガー）[/color][/i]: 問題を確認させてください！")
t("Devices / Users Hint", "デバイス/ユーザーヒント")
t("View hint", "ヒントを表示")
t("Dimiss hint?", "ヒントを閉じますか？")
t("I am ready to manage my network without hint. ", "ヒントなしでネットワークを管理する準備ができました。")
t("Dismiss all notifications", "すべての通知を閉じる")

# SLA warnings
t("{username} is experiencing satisfaction below SLA.\n\nSLA breach will occur if not resolved.",
  "{username} の満足度がSLA以下です。\n\n解決しないとSLA違反が発生します。")
t("Multiple users with impending SLA breaches.\n\nLocate these users and resolve their issues.",
  "複数のユーザーにSLA違反の危機が迫っています。\n\nこれらのユーザーを特定し、問題を解決してください。")

# ============================================================
# BATCH 5: Service/business descriptions, user type descriptions
# ============================================================

t("Congratulations on getting appointed as our new tower network administrator.\n\nYour role as the administrator is to ensure all tower tenants (including future ones) has their SLA met. You can check this with the \u2018Surveyor\u2019 on your MobileOS.\n\nWhen a new floor is built, they will be put under your network\u2019s jurisdiction. Please ensure the new floor residents/offices has their SLA\u2019s met within their allotted grace period.\n\nYou may accept floor builds earlier then their scheduled build times using \u2018The Secretariat\u2019 on MobileOS.\n\nThe finance department will allow up to {max_days_in_debt} day(s) in debt.\n\nShould you fail to meet any financial obligations or breach any tenant SLA, you will be replaced.\n\nTogether we build towards new heights.\nBabel Secretariat",
  "新しいタワーネットワーク管理者に任命されたことをお祝い申し上げます。\n\n管理者としての役割は、すべてのタワーテナント（将来のテナントを含む）のSLAを満たすことです。MobileOSの「Surveyor」で確認できます。\n\n新しいフロアが建設されると、あなたのネットワークの管轄下に置かれます。新しいフロアの住民/オフィスのSLAが猶予期間内に満たされるようにしてください。\n\nMobileOSの「The Secretariat」を使用して、予定より早くフロアの建設を承認できます。\n\n財務部門は最大 {max_days_in_debt} 日の借金を許容します。\n\n財務義務の不履行またはテナントのSLA違反が発生した場合、あなたは解任されます。\n\n共に新たな高みを目指しましょう。\nBabel事務局")

t("let\u2019s explore our additive streaming site to brighten your day.",
  "私たちのストリーミングサイトを探索して、素敵な1日を過ごしましょう。")

t("A kanban platform that empowers users to create customizable boards for planning, tracking, and managing projects of any type. ",
  "カスタマイズ可能なボードを作成して、あらゆるプロジェクトの計画、追跡、管理を可能にするカンバンプラットフォーム。")

t("experience enhanced project efficiency with our premium business kanban service - invite your team and organization to streamline project management.",
  "プレミアムビジネスカンバンサービスでプロジェクト効率を向上 - チームと組織を招待してプロジェクト管理を効率化。")

t("A flexible travel provider that offers standalone or combined bookings for flights and accommodations.",
  "フライトと宿泊の単独または組み合わせ予約を提供する柔軟な旅行プロバイダー。")

t("Digital classroom requiring consistent full day bandwidth for synchronized learning experiences across multiple time zones.",
  "複数のタイムゾーンでの同期学習体験のために、終日安定した帯域幅が必要なデジタル教室。")

t("join our comprehensive online university platform offering accredited degree programs designed for working professionals and students.",
  "社会人と学生向けの認定学位プログラムを提供する総合オンライン大学プラットフォームにご参加ください。")

t("Digital classroom requiring consistent night time bandwidth for synchronized learning experiences across multiple time zones.",
  "複数のタイムゾーンでの同期学習体験のために、夜間の安定した帯域幅が必要なデジタル教室。")

t("join our comprehensive online university platform offering accredited degree program designed for working professionals and students.",
  "社会人と学生向けの認定学位プログラムを提供する総合オンライン大学プラットフォームにご参加ください。")

t("A budget-friendly e-commerce seller specializing in refurbished electronics and upcycled goods, providing basic transaction services through their online storefront.",
  "リファービッシュ電子機器やアップサイクル商品を専門とする低価格eコマース販売者。オンラインストアで基本的な取引サービスを提供。")

t("offers unbeatable prices on used devices for tower residents with exclusive bulk discounts.",
  "タワー住民向けの中古デバイスを限定大量割引付きで圧倒的な低価格で提供。")

t("An indie gaming studios that hosts their development workspace on-premise.",
  "開発ワークスペースをオンプレミスでホストするインディーゲームスタジオ。")

t("An internal development workspace for hired coders, plus a secure login site where gamers can view game releases.",
  "雇用されたプログラマー向けの内部開発ワークスペースと、ゲーマーがゲームリリースを閲覧できるセキュアなログインサイト。")

t("An online shopping platform which provides high-quality servers, switches, and networking equipment for home tech setups.",
  "家庭用テクノロジー環境向けの高品質サーバー、スイッチ、ネットワーク機器を提供するオンラインショッピングプラットフォーム。")

t("let's buy high-quality servers, switches, and networking equipment for home tech setups.",
  "家庭用テクノロジー環境向けの高品質サーバー、スイッチ、ネットワーク機器を購入しよう。")

t("Tech and office supply store offering computers, networking equipment, printers, and administrative essentials - your one-stop shop for all business and home office technology needs.",
  "コンピューター、ネットワーク機器、プリンター、管理用品を取り揃えたテクノロジー＆オフィス用品店 - ビジネスとホームオフィスのテクノロジーニーズにワンストップで対応。")

t("we are your one-stop shop for all business and home office technology needs.",
  "ビジネスとホームオフィスのテクノロジーニーズにワンストップで対応します。")

t("An indie gaming studios which specialises in horror games and hosts their development workspace on-premise.",
  "ホラーゲームを専門とし、開発ワークスペースをオンプレミスでホストするインディーゲームスタジオ。")

t("An internal development workspace for hired coders, plus a secure login site where gamers can view latest game releases.",
  "雇用されたプログラマー向けの内部開発ワークスペースと、ゲーマーが最新ゲームリリースを閲覧できるセキュアなログインサイト。")

t("A travel agency that create one-stop vacation packages by leveraging relationships with airlines, hotels, and local tour operators.",
  "航空会社、ホテル、現地ツアーオペレーターとの関係を活用してワンストップバケーションパッケージを作成する旅行代理店。")

t("book your dream vacation with our curated high-end travel deals.",
  "厳選されたハイエンドな旅行プランで夢のバケーションを予約しよう。")

t("A cheap restaurant that operates through delivery apps, optimizing its menu and operations for efficient online food delivery.",
  "デリバリーアプリを通じて運営される低価格レストラン。効率的なオンラインフードデリバリーに最適化されたメニューとオペレーション。")

t("food review community where people can share and read restaurant reviews.",
  "レストランのレビューを共有・閲覧できるフードレビューコミュニティ。")

t("A community job board where residents can post small tasks and hire neighbors for help - earn extra income while supporting your tower community.",
  "住民が小さなタスクを投稿して隣人を雇える地域求人掲示板 - タワーコミュニティを支えながら副収入を得よう。")

t("A pioneering technology company offering an all-in-one super-app that seamlessly integrates ride-hailing, food delivery, and digital payment services online.",
  "配車、フードデリバリー、デジタル決済サービスをシームレスに統合するオールインワンスーパーアプリを提供する先進的テクノロジー企業。")

t("An e-commerce platform where multiple merchants sell various products, offering customers a wide selection of items from different sellers in one convenient location.",
  "複数の販売者がさまざまな商品を販売するeコマースプラットフォーム。異なる販売者からの幅広い商品を1つの便利な場所で提供。")

t("we are online marketplace platform hosting multiple e-commerce sellers.",
  "複数のeコマース販売者をホストするオンラインマーケットプレイスプラットフォームです。")

t("A subscription database-as-a-service platform which provide managed database service to small data company.",
  "小規模データ企業にマネージドデータベースサービスを提供するサブスクリプション型DBaaSプラットフォーム。")

t("A digital distribution service platform which releases games.",
  "ゲームをリリースするデジタル配信サービスプラットフォーム。")

t("free to post your own games and play others' creations.",
  "自分のゲームを投稿し、他の人の作品をプレイできます。")

t("A subscription video streaming service platform which release movie and entertainment show.",
  "映画やエンターテイメント番組をリリースするサブスクリプション型動画ストリーミングサービスプラットフォーム。")

t("we are movie platform where users can upload and watch films - share your videos or discover new content from our community of creators.",
  "ユーザーが映画をアップロード・視聴できるプラットフォーム - あなたの動画を共有したり、クリエイターコミュニティの新しいコンテンツを発見しよう。")

t("A premium restaurant that operates through delivery apps, optimizing its menu and operations for efficient online food delivery.",
  "デリバリーアプリを通じて運営されるプレミアムレストラン。効率的なオンラインフードデリバリーに最適化されたメニューとオペレーション。")

t("A convenient healthcare platform connecting patients with licensed physicians for virtual consultations, medical advice, and prescriptions from any location.",
  "患者と認定医師をつなぎ、どこからでもバーチャル診察、医療アドバイス、処方箋を受けられる便利なヘルスケアプラットフォーム。")

t("online medical consultation platform connecting patients with licensed healthcare professionals for virtual appointments.",
  "患者と認定医療専門家をつなぐオンライン医療相談プラットフォーム。バーチャル予約に対応。")

t("A platform where individuals showcase their diverse perspectives through personalized blogs and interactive community engagement. They expect more visitors than usual.",
  "個人がパーソナライズされたブログとインタラクティブなコミュニティ参加を通じて多様な視点を発信するプラットフォーム。通常より多くの訪問者が見込まれます。")

t("An interactive community platform by tower residents that brings book enthusiasts together for meaningful connections around shared literary passions.",
  "タワー住民による読書愛好家を集めて文学的な情熱を共有するインタラクティブなコミュニティプラットフォーム。")

t("A software-as-a-service (SaaS) provider company that hosts their cloud storage service. They expect more visitors than usual.",
  "クラウドストレージサービスをホストするSaaSプロバイダー企業。通常より多くの訪問者が見込まれます。")

t("we provide cloud storage service offering reliable online backup and file sharing.",
  "信頼性の高いオンラインバックアップとファイル共有を提供するクラウドストレージサービスです。")

t("An international data company that hosts their workspace on-premise and hire more freelancer.",
  "ワークスペースをオンプレミスでホストし、フリーランサーを多く雇用する国際データ企業。")

t("internal workspace which provides freelance coders with advanced tools and collaborative environments to create the best working experience within tower.",
  "フリーランスプログラマーに高度なツールと共同作業環境を提供し、タワー内で最高の労働体験を実現する内部ワークスペース。")

t("An international data company that hosts their workspace on-premise, and hire permanent staff.",
  "ワークスペースをオンプレミスでホストし、正社員を雇用する国際データ企業。")

t("An internal workspace for hired coders to develop custom software solutions, plus a login-protected site where authorized users can view company data products and case studies.",
  "雇用されたプログラマーがカスタムソフトウェアソリューションを開発する内部ワークスペースと、認可されたユーザーが企業データ製品や事例を閲覧できるログイン保護サイト。")

t("An economics news company that hosts their site on-premise (focus mainly on economics news)",
  "サイトをオンプレミスでホストする経済ニュース企業（主に経済ニュースに注力）")

t("An indie gaming studios that hosts their development workspace on-premise, and hire mostly freelancers.",
  "開発ワークスペースをオンプレミスでホストし、主にフリーランサーを雇用するインディーゲームスタジオ。")

t("A comedy movie director who produces movie content on video subscription platform",
  "動画サブスクリプションプラットフォームで映画コンテンツを制作するコメディ映画監督")

t("An music streaming company that provide music streaming from musician.",
  "ミュージシャンの音楽ストリーミングを提供する音楽ストリーミング企業。")

t("An podcast streaming company that provide podcast streaming from podcasters.",
  "ポッドキャスターのポッドキャストストリーミングを提供するポッドキャストストリーミング企業。")

t("An official political news company that hosts their site on-premise.",
  "サイトをオンプレミスでホストする公式政治ニュース企業。")

t("A platform where individuals deepen their spiritual journey through sacred text studies, religious discourse, and faith-based resources.",
  "聖典学習、宗教的議論、信仰ベースのリソースを通じて精神的な旅を深めるプラットフォーム。")

t("let's share your spiritual journey with us.",
  "あなたの精神的な旅を共有しましょう。")

t("A scientific news company that hosts their site on-premise.",
  "サイトをオンプレミスでホストする科学ニュース企業。")

t("All-in-one community portal connecting residents, staff, and service providers through a unified platform.",
  "住民、スタッフ、サービスプロバイダーを統合プラットフォームで接続するオールインワンコミュニティポータル。")

t("feel free to read or post announcement.",
  "お知らせの閲覧・投稿はご自由にどうぞ。")

t("A social media company that hosts media content from influencer and other content creator.",
  "インフルエンサーやその他のコンテンツクリエイターのメディアコンテンツをホストするソーシャルメディア企業。")

t("A bank which enable transaction within tower. Require always on and consistent network services.",
  "タワー内での取引を可能にする銀行。常時稼働で安定したネットワークサービスが必要。")

t("enjoy our best professional banking services for both businesses and individual customers.",
  "法人・個人のお客様に最高のプロフェッショナルバンキングサービスをお届けします。")

t("A instant-messaging company that allows user to chat with each other at real time.",
  "ユーザー同士がリアルタイムでチャットできるインスタントメッセージング企業。")

t("let's chat with your loved ones instantly.",
  "大切な人と今すぐチャットしよう。")

t("A basic email service provider who has consistent low bandwidth usage, and enable residents to read and send email. ",
  "安定して低帯域幅で利用でき、住民がメールの読み書きを行えるベーシックなメールサービスプロバイダー。")

t("A software company that provides software updates for their client.",
  "クライアント向けにソフトウェアアップデートを提供するソフトウェア企業。")

t("release software update for companies.",
  "企業向けにソフトウェアアップデートをリリース。")

t("An integrated utility management ecosystem streamlining resource monitoring, usage optimization, and payment processing for all building services and infrastructure. This company often expects more visitors.",
  "すべてのビル設備とインフラのリソース監視、使用最適化、決済処理を効率化する統合ユーティリティ管理エコシステム。この企業は多くの訪問者が見込まれることが多い。")

t("kindly pay your monthly utilities bills by the due date to avoid service interruptions.",
  "サービスの中断を避けるため、月額公共料金を期日までにお支払いください。")

t("This advertisement company specializes in promoting ideological campaigns for political associations, offering cost-effective broadcasting services.",
  "政治団体向けの思想キャンペーン促進を専門とし、コスト効率の良い放送サービスを提供する広告企業。")

t("A place which provides comprehensive resources, collaboration tools, and expert support for academics, scientists, and researchers to conduct studies and share findings.",
  "学者、科学者、研究者が研究を行い成果を共有するための包括的なリソース、コラボレーションツール、専門的サポートを提供する場所。")

t("An one-stop cctv service provider who enables their subscribers to view cctv footages at real-time.",
  "加入者がCCTV映像をリアルタイムで閲覧できるワンストップCCTVサービスプロバイダー。")

t("allow users to store surveillance data with the utmost privacy settings.",
  "最高のプライバシー設定で監視データを保存できるようにします。")

t("A researcher who designs, develops, and studies artificial intelligence systems to advance the field through research, experimentation",
  "研究と実験を通じてAI分野を発展させるために人工知能システムを設計、開発、研究する研究者")

t("A highly specialized engineer who designs the architectural blueprints and detailed circuit layouts for microprocessors, memory chips, and other semiconductor devices",
  "マイクロプロセッサ、メモリチップ、その他の半導体デバイスのアーキテクチャ設計図と詳細な回路レイアウトを設計する高度な専門エンジニア")

t("A professional e-sports streamer broadcasting live gameplay on gaming platforms, entertaining viewers with competitive gaming content.",
  "ゲームプラットフォームでライブゲームプレイを配信し、競技ゲームコンテンツで視聴者を楽しませるプロeスポーツストリーマー。")

t("An individual who watches multiple movies lasting several hours without breaks in a single sitting.",
  "一度に数時間の映画を休憩なしで何本も視聴する個人。")

t("A tower dweller who loves jazz music and enjoys listening to various jazz artists.",
  "ジャズ音楽を愛し、さまざまなジャズアーティストの曲を楽しむタワー住民。")

t("A home-based person who handles work, shopping, and household tasks online. They stick to familiar websites unless better options appear.",
  "仕事、買い物、家事をオンラインで処理する在宅の人。より良い選択肢が現れない限り、慣れたウェブサイトを利用する傾向。")

t("An individual who requires background tasks like large cloud backups, or data processing, but tolerant of interruptions as long as it completes eventually. \n\nThey stick to familiar websites unless better options appear.",
  "大規模なクラウドバックアップやデータ処理などのバックグラウンドタスクを必要とするが、最終的に完了する限り中断には寛容な個人。\n\nより良い選択肢が現れない限り、慣れたウェブサイトを利用する傾向。")

t("A centralized mart that enables multiple household stores to create their own digital storefronts while providing integrated delivery and logistics services to connect local grocers.",
  "複数の家庭用品店が独自のデジタルストアフロントを作成できるようにし、地元の食料品店をつなぐ統合配送・物流サービスを提供する集約型マート。")

t("A E-sport streaming platform that employs professional gamers to broadcast live gameplay and provides viewers with access to watch these live gaming streams.",
  "プロゲーマーを雇用してライブゲームプレイを配信し、視聴者にライブゲームストリームへのアクセスを提供するeスポーツストリーミングプラットフォーム。")

t("A retail establishment that sells food products, beverages, and household essentials for daily consumption.",
  "食品、飲料、日用品を販売する小売店。")

t("An inventory management software company which automatically tracks, manages, and optimizes their clients' product inventory across multiple sales channels.",
  "複数の販売チャネルにわたるクライアントの商品在庫を自動的に追跡、管理、最適化する在庫管理ソフトウェア企業。")

t("A specialized audio production facility that produces high-quality audio content for various media and entertainment projects.",
  "さまざまなメディアやエンターテイメントプロジェクト向けに高品質なオーディオコンテンツを制作する専門オーディオ制作施設。")

t("An online discussion forum that requires users to verify their professional credentials before gaining access to view content or participate in discussions",
  "コンテンツの閲覧やディスカッションへの参加前に専門資格の確認が必要なオンラインディスカッションフォーラム")

t("Cloud-based platforms that enable high-quality video meetings, webinars, and real-time collaboration through secure, scalable communication technology for businesses, education, and personal use.",
  "ビジネス、教育、個人利用向けに、安全でスケーラブルな通信技術を通じて高品質なビデオ会議、ウェビナー、リアルタイムコラボレーションを可能にするクラウドベースプラットフォーム。")

t("A software company that provides antivirus software updates for their client.",
  "クライアント向けにアンチウイルスソフトウェアアップデートを提供するソフトウェア企業。")

t("A software company that releases software updates which protect personal information and anonymity for their clients",
  "クライアントの個人情報と匿名性を保護するソフトウェアアップデートをリリースするソフトウェア企業")

t("{username} is experiencing satisfaction below SLA.\n\nSLA breach will occur in {seconds_left} seconds if their satiety is not raised to {min_satiety_level}.\n\nA SLA breach will caused you to lose your position as the Tower\u2019s network admin.\n\nTogether we build towards new heights.\nBabel Secretariat",
  "{username} の満足度がSLA以下です。\n\n{seconds_left} 秒以内に満足度を {min_satiety_level} まで上げないとSLA違反が発生します。\n\nSLA違反が発生すると、タワーのネットワーク管理者としての地位を失います。\n\n共に新たな高みを目指しましょう。\nBabel事務局")

# ============================================================
# BATCH 6: Tutorial steps (Tutorial 1 - Basic Debugger)
# ============================================================
# ============================================================
# BATCH 6: Tutorial steps (Tutorial 1 - Basic Debugger)
# ============================================================
t("3 consumers are connected to the network switch.",
  "3人のコンシューマーがネットワークスイッチに接続されています。")
t("identify 3 consumers", "3人のコンシューマーを特定")
t("1 producer is connected to the network switch.",
  "1人のプロデューサーがネットワークスイッチに接続されています。")
t("identify 1 producer", "1人のプロデューサーを特定")
t("The debugger is connected to the network switch and the boulder server below it.",
  "デバッガーはネットワークスイッチとその下のBoulderサーバーに接続されています。")
t("locate debugger and boulder server", "デバッガーとBoulderサーバーの場所を確認")
t("Bring up your mobileOS by clicking on bottom left \"View MobileOS\" OR hitting left ALT key.\n\nMiddle-click on the MobileOS screen to shift the screen to the opposite side.",
  "左下の「View MobileOS」をクリックするか左ALTキーを押してmobileOSを表示します。\n\nMobileOS画面をミドルクリックすると画面を反対側に移動できます。")
t("view mobile os", "MobileOSを表示")
t("Launch the networking shell or \"netsh\" application by clicking on the icon on your phone.",
  "スマホのアイコンをクリックしてネットワークシェル「netsh」アプリを起動します。")
t("launch netsh app", "netshアプリを起動")
t("Input \"lstdbg\" into the console.\n\nThis shows you the list of debuggers.",
  "コンソールに「lstdbg」と入力します。\n\nこれでデバッガーの一覧が表示されます。")
t("[command]: lstdbg: list debuggers", "[コマンド]: lstdbg: デバッガー一覧")
t("You will see a debugger with hardware address = 36149",
  "ハードウェアアドレス = 36149 のデバッガーが表示されます")
t("Let's scan some devices with the debugger, input:\n\nscan devices using 36149",
  "デバッガーでデバイスをスキャンしましょう。以下を入力：\n\nscan devices using 36149")
t("[command]: scan devices using 36149", "[コマンド]: scan devices using 36149")
t("Observe that the debugger \"sees\" 3 devices:\n1. itself (Debugger Alice)\n2. blade10 switch\n3. boulder server",
  "デバッガーが3つのデバイスを「認識」していることを確認：\n1. 自分自身（Debugger Alice）\n2. blade10スイッチ\n3. Boulderサーバー")
t("debugger \"sees\" 3 devices", "デバッガーが3つのデバイスを「認識」")
t("Let's scan for users using the same debugger, input:\n\nscan users using 36149",
  "同じデバッガーでユーザーをスキャンしましょう。以下を入力：\n\nscan users using 36149")
t("[command]: scan users using 36149", "[コマンド]: scan users using 36149")
t("The debugger is able to see 4 users.", "デバッガーは4人のユーザーを認識できます。")
t("debugger \"sees\" 4 users", "デバッガーが4人のユーザーを「認識」")
t("Its tedious to keep typing the \"using 36149\" part\n\nLet's fix this",
  "毎回「using 36149」と入力するのは面倒です\n\nこれを解決しましょう")
t("We can make netsh always use a debugger for all commands, input:\n\nalways using 36149",
  "netshが全コマンドで常にデバッガーを使用するよう設定できます。以下を入力：\n\nalways using 36149")
t("[command]: always using 36149", "[コマンド]: always using 36149")
t("This will make all commands by default use the debugger 36149.",
  "これで全コマンドがデフォルトでデバッガー36149を使用します。")
t("Let's try scanning again, input:\n\nscan users",
  "もう一度スキャンしてみましょう。以下を入力：\n\nscan users")
t("[command]: scan users", "[コマンド]: scan users")
t("Observe that the command runs correctly without specifying the debugger address with \"using 36149\"",
  "「using 36149」でデバッガーアドレスを指定せずにコマンドが正しく実行されることを確認")
t("There are other shortcuts to some commands.\n\nTry input \"scan d\"",
  "他のコマンドにもショートカットがあります。\n\n「scan d」と入力してみてください")
t("[command]: scan d", "[コマンド]: scan d")
t("Notice \"scan d\" is the same command as \"scan devices\".\n\nTry input \"scan u\"",
  "「scan d」は「scan devices」と同じコマンドです。\n\n「scan u」と入力してみてください")
t("[command]: scan u", "[コマンド]: scan u")
t("\"scan u\" is same as \"scan users\".\n\nHow to find out more about \"scan\"?",
  "「scan u」は「scan users」と同じです。\n\n「scan」についてもっと知るには？")
t("Use the \"man\" command, input:\n\nman scan",
  "「man」コマンドを使います。以下を入力：\n\nman scan")
t("[command]: man scan", "[コマンド]: man scan")
t("The man command shows you the syntax and examples to use any command.",
  "manコマンドはコマンドの構文と使用例を表示します。")
t("To find out how to use the netsh more efficiently, input:\n\nman shell",
  "netshをもっと効率的に使う方法を知るには、以下を入力：\n\nman shell")
t("[command]: man shell", "[コマンド]: man shell")
t("Let's now figure out why our user's are not satisfied.",
  "では、ユーザーが満足していない理由を調べましょう。")
t("Input \"quit\" to quit netsh.\n\nLaunch the \"Surveyor\" application",
  "「quit」と入力してnetshを終了します。\n\n「Surveyor」アプリを起動してください")
t("launch Surveyor app", "Surveyorアプリを起動")
t("Click on the user details (the magnifying glass) for the user \"pleasing-crane\"",
  "ユーザー「pleasing-crane」の詳細（虫眼鏡）をクリックします")
t("read user details for \"pleasing-crane\"", "「pleasing-crane」のユーザー詳細を表示")
t("Observe the issues faced by the user.\n\nIt cannot reach any DNS servers at the moment.",
  "ユーザーが直面している問題を確認します。\n\n現在、DNSサーバーに到達できません。")
t("The boulder server (below the debugger) has the DNS server installed.",
  "Boulderサーバー（デバッガーの下）にはDNSサーバーがインストールされています。")
t("Lets troubleshoot the problem. \n\nQuit surveyor and head back to netsh.",
  "問題のトラブルシューティングを行いましょう。\n\nSurveyorを終了してnetshに戻ります。")
t("launch netsh again", "netshを再度起動")
t("If you can see the device or user physically, you can hover your mouse over to get its addresses.",
  "デバイスやユーザーが物理的に見える場合、マウスオーバーでアドレスを取得できます。")
t("Hover your mouse over the server below the debugger and note its address.",
  "デバッガーの下にあるサーバーにマウスオーバーしてアドレスを確認してください。")
t("hover your mouse over server", "サーバーにマウスオーバー")
t("You should see\n\nHardware Addr: 41216", "以下が表示されます\n\nHardware Addr: 41216")
t("hardware address of server: 41216", "サーバーのハードウェアアドレス: 41216")
t("If you do not have physical access to the device/user, scanning is a way to get addresses.",
  "デバイス/ユーザーに物理的にアクセスできない場合、スキャンでアドレスを取得できます。")
t("Get the hardware address of \"pleasing-crane\", input:\n\nscan u",
  "「pleasing-crane」のハードウェアアドレスを取得します。以下を入力：\n\nscan u")
t("Note the hardware address of pleasing-crane, which is 51574.",
  "pleasing-craneのハードウェアアドレスは51574です。")
t("hardware address of pleasing-crane: 51574", "pleasing-craneのハードウェアアドレス: 51574")
t("Now, let's trace the server from the user, input:\n\ntrace 41216 from 51574",
  "では、ユーザーからサーバーへのトレースを行いましょう。以下を入力：\n\ntrace 41216 from 51574")
t("[command]: trace 41216 from 51574", "[コマンド]: trace 41216 from 51574")
t("Observe that on \"hop 1\", it reaches a device with address \"14673\", the rest are 2 hops away.",
  "「ホップ1」でアドレス「14673」のデバイスに到達し、残りは2ホップ先にあることを確認します。")
t("None of what the user sees is the destination \"41216\".\n\nThe user cannot reach the server.",
  "ユーザーが認識しているデバイスの中に目的地「41216」はありません。\n\nユーザーはサーバーに到達できません。")
t("Upon closer inspection, the server is connected to the debugger and NOT the switch.",
  "よく確認すると、サーバーはスイッチではなくデバッガーに接続されています。")
t("Unplug the GREEN cable from the debugger and plug it into the switch.",
  "デバッガーからGREENケーブルを抜いてスイッチに接続してください。")
t("plug green cable from debugger into switch", "デバッガーからスイッチにGREENケーブルを接続")
t("Now let's trace again:\n\ntrace 41216 from 51574",
  "もう一度トレースしましょう：\n\ntrace 41216 from 51574")
t("[command] again: trace 41216 from 51574", "[コマンド] 再度: trace 41216 from 51574")
t("Observe that now, the user can successfully reach the server.",
  "ユーザーがサーバーに正常に到達できるようになったことを確認します。")
t("user can reach server", "ユーザーがサーバーに到達可能")

# Tutorial: Connectivity Troubleshooting
t("Consumers are now consuming from the producer using the hardware address supplied from the DNS server.",
  "コンシューマーはDNSサーバーから提供されたハードウェアアドレスを使用してプロデューサーから消費しています。")
t("First, let's try to ping the producer\n\nLet's find out its address",
  "まず、プロデューサーにpingしてみましょう\n\nそのアドレスを調べます")
t("You can quickly copy addresses by hovering over the user's interface and right clicking.",
  "ユーザーのインターフェースにマウスオーバーして右クリックすると素早くアドレスをコピーできます。")
t("Right click the user to ensure the address is copied.",
  "ユーザーを右クリックしてアドレスがコピーされたことを確認します。")
t("right click to copy producer's address", "右クリックでプロデューサーのアドレスをコピー")
t("Now from netsh, type \"ping\" and right click again.\n\nThe address is pasted.",
  "netshから「ping」と入力して再度右クリックします。\n\nアドレスが貼り付けられます。")
t("[command]: ping 36005", "[コマンド]: ping 36005")
t("Running the \"ping\" command shows the debugger is able to \"see\" the producer.",
  "「ping」コマンドを実行すると、デバッガーがプロデューサーを「認識」できることがわかります。")
t("ping command allows debugger to \"see\" the producer",
  "pingコマンドでデバッガーがプロデューサーを「認識」可能")
t("Now let's unplug the producer.\n\nDisconnect the WHITE cable from the interface.",
  "では、プロデューサーを切断しましょう。\n\nインターフェースからWHITEケーブルを外します。")
t("unnplug white cable from \"frail-squid\" (producer)",
  "「frail-squid」（プロデューサー）からWHITEケーブルを外す")
t("Let's try to ping again:\n\nping 36005",
  "もう一度pingしてみましょう：\n\nping 36005")
t("The debugger can no longer see the producer.\n\nNotice satiety is dropping among users.",
  "デバッガーがプロデューサーを認識できなくなりました。\n\nユーザーの満足度が低下していることに注目してください。")
t("Reconnect the WHITE cable.\n\nping the producer again to ensure it is now up.",
  "WHITEケーブルを再接続します。\n\nプロデューサーに再度pingして復旧を確認します。")
t("reconnect white cable to producer", "プロデューサーにWHITEケーブルを再接続")

# Tutorial: Riser Links
t("Wonder how floors in the tower are connected? A riser enables the network connection between them.",
  "タワーのフロア間はどう接続されているのでしょうか？ライザーがフロア間のネットワーク接続を可能にします。")
t("identify riser", "ライザーを確認")
t("Press \"ALT\" key or bottom left \"VIEW MobileOS\" to view MobileOS.\n\nOpen Tower Link app to set up riser connections between different floors.",
  "「ALT」キーまたは左下の「VIEW MobileOS」でMobileOSを表示します。\n\nTower Linkアプリを開いてフロア間のライザー接続を設定します。")
t("launch Tower Link", "Tower Linkを起動")
t("A complete riser link consists of two points: Point A and Point B.\n\nSet the floor of Point A to '0'. The unlinked riser outlets on floor '0' available for Point A are displayed.\n\nAt the moment, there is only one available outlet on floor 0. Select 'TEJM' as the outlet for Point A.",
  "完全なライザーリンクは2つのポイントで構成されます：ポイントAとポイントB。\n\nポイントAのフロアを「0」に設定します。フロア「0」の未接続ライザーアウトレットが表示されます。\n\n現在、フロア0には1つのアウトレットのみ利用可能です。ポイントAに「TEJM」を選択してください。")
t("select 'TEJM' as Point A in Tower Link app", "Tower Linkアプリでポイントとして「TEJM」を選択")
t("Next, set the floor of Point B to '1' and select 'ABVN' as the outlet for Point B.",
  "次に、ポイントBのフロアを「1」に設定し、ポイントBに「ABVN」を選択します。")
t("select 'ABVN' outlet in floor 1 as riser Point B", "フロア1の「ABVN」アウトレットをライザーポイントBに選択")
t("\"CAT1 Copper\" is the default riser link size.\n\nFor more bandwidth, select other options from the dropdown. \n\nMonitor the link bandwidth and the changes in setup and daily costs based on your choice.",
  "「CAT1 Copper」がデフォルトのライザーリンクサイズです。\n\nより多くの帯域幅が必要な場合は、ドロップダウンから他のオプションを選択してください。\n\nリンクの帯域幅と、選択に応じた設置コストと日次コストの変化を確認してください。")
t("select \"basic copper\" as riser link size", "ライザーリンクサイズに「basic copper」を選択")
t("Click \"REQUEST LINK\" to create the riser link after confirming your selection.",
  "選択を確認した後、「REQUEST LINK」をクリックしてライザーリンクを作成します。")
t("complete riser setup between floors", "フロア間のライザー設定を完了")
t("Once the riser link is successfully created, \"LINKED\" will appear on the outlet.\n\nAdditionally, by clicking the \"VIEW LINKS\" tab in the app, you can see the details of your created riser link.",
  "ライザーリンクが正常に作成されると、アウトレットに「LINKED」と表示されます。\n\nまた、アプリの「VIEW LINKS」タブをクリックすると、作成したライザーリンクの詳細を確認できます。")
t("\"VIEW LINKS\" in Tower Link app", "Tower Linkアプリの「VIEW LINKS」")
t("To connect the \"BOULDER\" on floor 0 to the resident living on floor 1 via the riser link you just created, connect the Ethernet cable from Blade5 to Outlet A (TEJM).\n\nNotes: The Boulder is already connected to Blade5 on the current floor.",
  "作成したライザーリンクを使ってフロア0の「BOULDER」をフロア1の住民に接続するには、Blade5からアウトレットA（TEJM）にEthernetケーブルを接続します。\n\n注意：BoulderはすでにBlade5に接続されています。")
t("connect Blade5 to Outlet A (TEJM)", "Blade5をアウトレットA（TEJM）に接続")
t("To use elevator to travel to floor 1, select '1' on this elevator panel.",
  "エレベーターでフロア1に移動するには、エレベーターパネルで「1」を選択します。")
t("Elevator use", "エレベーターの使用")
t("select '1' on elevator panel", "エレベーターパネルで「1」を選択")
t("Observe the countdown timer until it reaches zero.\n\nWhen the elevator door opens, click the panel to enter, and it will take you to Floor 1.",
  "カウントダウンタイマーがゼロになるまで待ちます。\n\nエレベーターのドアが開いたら、パネルをクリックして乗り込むと、フロア1に移動します。")
t("enter elevator", "エレベーターに乗る")
t("Connect cable from Outlet B (ABVN) to the Blade5. \n\nResidents connected to Blade5 can access Outlet A through Outlet B.",
  "アウトレットB（ABVN）からBlade5にケーブルを接続します。\n\nBlade5に接続された住民は、アウトレットBを通じてアウトレットAにアクセスできます。")
t("connect cable from ABVN outlet to Blade5 switch", "ABVNアウトレットからBlade5スイッチにケーブルを接続")
t("To deactivate the created link, click 'DEACTIVATE LINK' under 'VIEW LINKS' in the Tower Link app. You can then choose to reactivate or decommission the link.\n\nNotes: If the available outlets don\u2019t meet your needs, you can request a custom outlet position in future tutorial scenarios through a different app.",
  "作成したリンクを無効化するには、Tower Linkアプリの「VIEW LINKS」で「DEACTIVATE LINK」をクリックします。その後、リンクの再有効化または廃止を選択できます。\n\n注意：利用可能なアウトレットがニーズに合わない場合、別のアプリを使って今後のチュートリアルシナリオでカスタムアウトレット位置をリクエストできます。")
t("deactivate riser link", "ライザーリンクを無効化")

# Tutorial: D-Market / Shopping
t("Experience your first day night cycle! The current day night cycle is simulated to be shorter than usual game.",
  "初めての昼夜サイクルを体験しましょう！現在の昼夜サイクルは通常のゲームより短く設定されています。")
t("Follow the next few steps to purchase new items on the D-Market app.",
  "次の手順に従ってD-Marketアプリで新しいアイテムを購入します。")
t("Launch D-Market app. ", "D-Marketアプリを起動します。")
t("launch D-Market app", "D-Marketアプリを起動")
t("Click the \u2018+ Add to Cart\u2019 button below the item\u2019s image to add it to your cart.\n\nPurchase at least one of each of the following items:\n\n1. Blade5 (Blade Networking Inc.)\n2. Power UK-B 500 (Mr Cable)\n3. Ethernet 1000 (Mr Cable) \n4. MacroHard Boulder SRV (AB Compute Ltd.)\n5. Debugger Alice (AB Compute Ltd.)\n\nYou can apply a filter or use the search bar to find the item in the D-Market app.",
  "アイテム画像の下にある「+ Add to Cart」ボタンをクリックしてカートに追加します。\n\n以下のアイテムをそれぞれ1つ以上購入してください：\n\n1. Blade5（Blade Networking Inc.）\n2. Power UK-B 500（Mr Cable）\n3. Ethernet 1000（Mr Cable）\n4. MacroHard Boulder SRV（AB Compute Ltd.）\n5. Debugger Alice（AB Compute Ltd.）\n\nD-Marketアプリでフィルターや検索バーを使ってアイテムを見つけることができます。")
t("purchase items (Blade5, Power UK-B 500, Ethernet 1000, MacroHard Boulder SRV, Debugger Alice)",
  "アイテムを購入（Blade5、Power UK-B 500、Ethernet 1000、MacroHard Boulder SRV、Debugger Alice）")
t("For ethernet cables, you can choose color before adding to cart.",
  "Ethernetケーブルはカートに追加する前に色を選べます。")
t("Click 'Checkout' button, select the floor, and pick up your item in front of elevator later.",
  "「Checkout」ボタンをクリックし、フロアを選択して、後でエレベーター前でアイテムを受け取ります。")
t("Click 'Submit' button to confirm order.", "「Submit」ボタンをクリックして注文を確定します。")
t("Launch 'Credit Stack' app after purchasing several items from online store.\n\nCheckout your spending on 'Transaction' tab.",
  "オンラインストアでアイテムを購入した後、「Credit Stack」アプリを起動します。\n\n「Transaction」タブで支出を確認してください。")
t("launch Credit Stack app", "Credit Stackアプリを起動")
t("To increase your initial capital for purchasing more devices, apply for a loan through the Fi$hy Loans app.",
  "デバイス購入のための初期資金を増やすには、Fi$hy Loansアプリでローンを申請します。")
t("launch Fi$hy Loans", "Fi$hy Loansを起動")
t("Checkout 'Credit Stack' again to observe daily expenses and interest that you need to pay for your loan.",
  "「Credit Stack」を再度確認して、ローンの日次費用と利息を確認してください。")

# Tutorial: DNS Setup
t("In the previous tutorial, you learned that end-users have their complaints and issues listed in 'Surveyor' app.",
  "前のチュートリアルでは、エンドユーザーの苦情と問題が「Surveyor」アプリに表示されることを学びました。")
t("launch 'Surveyor' app", "「Surveyor」アプリを起動")
t("Click Net Nester (consumers) profile on Surveyor app to identify their issues.",
  "Surveyorアプリで Net Nester（コンシューマー）のプロファイルをクリックして問題を特定します。")
t("click consumer's profile", "コンシューマーのプロファイルをクリック")
t("Can you see that consumers need DNS servers to access services from the producer?",
  "コンシューマーがプロデューサーのサービスにアクセスするためにDNSサーバーが必要であることがわかりますか？")
t("identify dns requirements of consumers", "コンシューマーのDNS要件を特定")
t("Net Nesters need dns servers to read and comment on 'texttextvelv.biz'",
  "Net Nestersは「texttextvelv.biz」の閲覧とコメントにDNSサーバーが必要です")
t("Exit current Net Nester profile on Surveyor app. Click on WireSync News (producer) profile on Surveyor app.",
  "SurveyorアプリでNet Nesterのプロファイルを閉じます。WireSync News（プロデューサー）のプロファイルをクリックします。")
t("click producer's profile", "プロデューサーのプロファイルをクリック")
t("See that the producer (WireSync News) actually need more proper visitors for their hosted services?",
  "プロデューサー（WireSync News）のホストサービスに適切な訪問者がもっと必要であることがわかりますか？")
t("Notice the behavior insights of the producer. They produce read text, post text with 'texttextvelv.biz'",
  "プロデューサーの行動分析に注目してください。「texttextvelv.biz」でread text、post textを生産しています")
t("Recall the Net Nesters' issues? Without access to DNS server, they can't access services from WireSync News.",
  "Net Nestersの問題を覚えていますか？DNSサーバーにアクセスできないと、WireSync Newsのサービスにアクセスできません。")
t("To resolve Net Nesters' issues with viewing services from WireSync News, use the netsh app to install 'dns-lite'.",
  "Net NestersがWireSync Newsのサービスを閲覧する問題を解決するため、netshアプリで「dns-lite」をインストールします。")
t("Open netsh app on your phone.\n\nType 'man program' in netsh app.",
  "スマホでnetshアプリを開きます。\n\nnetshアプリで「man program」と入力します。")
t("[command]: man program", "[コマンド]: man program")
t("Type 'program list' to list available program to install.",
  "「program list」と入力してインストール可能なプログラムを一覧表示します。")
t("[command]: program list", "[コマンド]: program list")
t("Type 'program describe dns-lite' in netsh.\n\ndns-lite is the dns-server required by Net Nester.",
  "netshで「program describe dns-lite」と入力します。\n\ndns-liteはNet Nesterが必要とするDNSサーバーです。")
t("[command]: program describe dns-lite", "[コマンド]: program describe dns-lite")
t("To install dns-lite on server, type 'program install dns-lite on 21802' on netsh.\n\n21802 is hardware address of server",
  "サーバーにdns-liteをインストールするには、netshで「program install dns-lite on 21802」と入力します。\n\n21802はサーバーのハードウェアアドレスです")
t("[command]: program install dns-lite on 21802", "[コマンド]: program install dns-lite on 21802")
t("To start dns-lite on server, type 'program start dns-lite on 21802' on netsh.\n\nNote: Autostart installed program is currently enabled in endless mode by default.",
  "サーバーでdns-liteを開始するには、netshで「program start dns-lite on 21802」と入力します。\n\n注意：インストール済みプログラムの自動起動はエンドレスモードではデフォルトで有効です。")
t("[command]: program start dns-lite on 21802", "[コマンド]: program start dns-lite on 21802")
t("There are two ways to observe available use stack on the server.\n\n1. Type 'watch' on netsh; then mouse over the server.\n",
  "サーバーの利用可能なUSEスタックを確認する方法は2つあります。\n\n1. netshで「watch」と入力し、サーバーにマウスオーバーする。\n")
t("Basic Program Operation", "基本的なプログラム操作")
t("[command]: watch", "[コマンド]: watch")
t("The second method is: \n\n1. Type 'watch 21802' on netsh\n\nBoth watch commands show 'reply-dns-queries'",
  "2番目の方法は：\n\n1. netshで「watch 21802」と入力する\n\nどちらのwatchコマンドも「reply-dns-queries」を表示します")
t("[command]: watch 21802", "[コマンド]: watch 21802")
t("Notice issues faced by Net Nesters now from Surveyor. They have no DNS entries for 'texttextvelv.biz'.",
  "SurveyorでNet Nestersが直面している問題を確認します。「texttextvelv.biz」のDNSエントリがありません。")
t("No DNS entries on the consumers' (Net Nesters) profile in the Surveyor app.\n\nThis means they can access the DNS server, but there is no valid mapping for the domain name.\n\nProducers like WireSync News provide services under domain names (e.g., texttextvelv.biz).\n\nTo use these services, consumers must do a DNS lookup to get the destination address.\n\nIn this case, texttextvelv.biz should resolve to address of WireSync News.\n\nWithout proper DNS mapping, consumers cannot reach the service to read or comment.",
  "Surveyorアプリのコンシューマー（Net Nesters）のプロファイルにDNSエントリがありません。\n\nこれはDNSサーバーにアクセスできるが、ドメイン名の有効なマッピングがないことを意味します。\n\nWireSync Newsのようなプロデューサーはドメイン名（例：texttextvelv.biz）でサービスを提供しています。\n\nこれらのサービスを利用するには、コンシューマーはDNSルックアップで宛先アドレスを取得する必要があります。\n\nこの場合、texttextvelv.bizはWireSync Newsのアドレスに解決される必要があります。\n\n適切なDNSマッピングがないと、コンシューマーはサービスにアクセスして閲覧やコメントができません。")
t("Type 'dns map texttextvelv.biz as 78121' on netsh. \nwhere 78121 is address of WireSync News company.\n\nNote: You can copy the producer's details from the Surveyor app. Click \"View Clipboard\" to see the copied content, then copy the domain name and address from the clipboard and paste them into Netsh.",
  "netshで「dns map texttextvelv.biz as 78121」と入力します。\n78121はWireSync News社のアドレスです。\n\n注意：Surveyorアプリからプロデューサーの詳細をコピーできます。「View Clipboard」をクリックしてコピーした内容を確認し、ドメイン名とアドレスをクリップボードからNetshに貼り付けてください。")
t("[command]: dns map texttextvelv.biz as 78121", "[コマンド]: dns map texttextvelv.biz as 78121")
t("Notice that Net Nester no longer has issues visiting  'texttextvelv.biz' after successful dns mapping and program installation.",
  "DNSマッピングとプログラムインストールが成功した後、Net Nesterが「texttextvelv.biz」へのアクセスに問題がなくなったことを確認します。")
t("1. Type 'program describe padu_v1' on netsh.\n2. Then, type, 'program describe dns-server' on netsh.\n\nNotice that dns-server is upgraded version of dns-lite since it produces 20 reply-dns-queries per tick; while padu_v1 is the storage program required by dns-server.",
  "1. netshで「program describe padu_v1」と入力します。\n2. 次に、netshで「program describe dns-server」と入力します。\n\ndns-serverはdns-liteの上位版で、tickあたり20のreply-dns-queriesを生産します。padu_v1はdns-serverが必要とするストレージプログラムです。")
t("[command]: program describe dns-server", "[コマンド]: program describe dns-server")
t("dns-server can support more residents at a time, but it requires access to a running text storage program (padu_v1).\n\nThis step is to show you the difference between dns-lite and dns-server. You do not need to install dns-server in this tutorial.",
  "dns-serverはより多くの住民を同時にサポートできますが、実行中のテキストストレージプログラム（padu_v1）へのアクセスが必要です。\n\nこのステップはdns-liteとdns-serverの違いを示すためのものです。このチュートリアルではdns-serverをインストールする必要はありません。")
t("dns-server requires access to padu_v1", "dns-serverはpadu_v1へのアクセスが必要")
t("Observe the satisfaction level of the residents to ensure they successfully visit 'texttextvelv.biz' online.\n",
  "住民の満足度を確認して、「texttextvelv.biz」へのオンラインアクセスが成功していることを確認してください。\n")
t("Don't worry if you wish to skip dns mapping after installing dns program. You may enable auto create dns-mappings mode before entering the actual game later.",
  "DNSプログラムインストール後にDNSマッピングをスキップしたい場合はご心配なく。実際のゲームに入る前に自動DNSマッピング作成モードを有効にできます。")
t("Click OK to exit tutorial once you have ensured the networking needs of the tower residents are fulfilled.",
  "タワー住民のネットワーク要件が満たされたことを確認したら、OKをクリックしてチュートリアルを終了してください。")

# Tutorial: Router Setup
t("The following steps show how to improve a switch-only setup by adding a router for more efficient network traffic. \n\nUnlike switches in the game, a router performs route traversal to a specific link, which reduces unnecessary visits during a network traversal. \n\nIn this tutorial, you\u2019ll learn how to set up and manage routing rules with commands.",
  "以下の手順では、ルーターを追加してスイッチのみの構成をより効率的なネットワークトラフィックに改善する方法を説明します。\n\nゲーム内のスイッチとは異なり、ルーターは特定のリンクへのルートトラバーサルを実行し、ネットワークトラバーサル中の不要な訪問を減らします。\n\nこのチュートリアルでは、コマンドを使用してルーティングルールを設定・管理する方法を学びます。")
t("Connect router (Disco Micro) port 0 to the networking switch (Blade10) to enable debugger access.\n\nEnsure the debugger is always connected to the network for troubleshooting and configuration task.\n",
  "ルーター（Disco Micro）のポート0をネットワークスイッチ（Blade10）に接続してデバッガーアクセスを有効にします。\n\nトラブルシューティングと設定作業のため、デバッガーが常にネットワークに接続されていることを確認してください。\n")
t("connect router port0 to switch", "ルーターのポート0をスイッチに接続")
t("Notice that the router is connected to the debugger through the switch. Open the netsh app.\n\nInput 'scan router'.",
  "ルーターがスイッチを通じてデバッガーに接続されていることを確認します。netshアプリを開きます。\n\n「scan router」と入力します。")
t("[command]: scan router", "[コマンド]: scan router")
t("Notice that the hardware address of the router is 48460.",
  "ルーターのハードウェアアドレスが48460であることを確認します。")
t("Input 'man route' on netsh.\n\nThe subsequent steps show how to append route on router ports.",
  "netshで「man route」と入力します。\n\n以降の手順ではルーターポートにルートを追加する方法を示します。")
t("[command]: man route", "[コマンド]: man route")
t("Unplug the white cable which connects WireSync News to the switch.\n\nThen, connect the purple cable from router port 2 to WireSync News, as we want to append the route to WireSync News on port 2 of the router.\n\nNote: A physical cable connection to the route target is required, in addition to setting the route through the 'route' routine in the netsh app.",
  "WireSync Newsをスイッチに接続しているWHITEケーブルを外します。\n\n次に、ルーターのポート2からWireSync Newsにpurpleケーブルを接続します。ルーターのポート2にWireSync Newsへのルートを追加するためです。\n\n注意：netshアプリの「route」ルーチンでルートを設定するだけでなく、ルートターゲットへの物理ケーブル接続も必要です。")
t("connect router port2 to WireSync News", "ルーターのポート2をWireSync Newsに接続")
t("Append route to WireSync News on router port 2.\n\nInput 'route add 36005 via port2 on 48460'\n\nNotes: 36005 is WireSync News address; 48460 is router's address",
  "ルーターのポート2にWireSync Newsへのルートを追加します。\n\n「route add 36005 via port2 on 48460」と入力します。\n\n注意：36005はWireSync Newsのアドレス、48460はルーターのアドレスです")
t("[command]: route add 36005 via port2 on 48460", "[コマンド]: route add 36005 via port2 on 48460")
t("Disconnect the DNS server from the networking switch:\n\nUnplug the green Ethernet cable from the DNS server.\n\nNote: The dns-lite program is running on 'Boulder' with '41216' address. Hence, we call it as DNS server in this tutorial.",
  "ネットワークスイッチからDNSサーバーを切断します：\n\nDNSサーバーからgreenのEthernetケーブルを外します。\n\n注意：dns-liteプログラムはアドレス「41216」の「Boulder」で実行されています。このチュートリアルではこれをDNSサーバーと呼びます。")
t("unplug green cable from DNS server", "DNSサーバーからGREENケーブルを外す")
t("The DNS server is now disconnected from the switch.\n\nConnect router port 1 to the DNS server.",
  "DNSサーバーがスイッチから切断されました。\n\nルーターのポート1をDNSサーバーに接続します。")
t("connect router port1 to DNS server", "ルーターのポート1をDNSサーバーに接続")
t("Append route to DNS server on router.\n\nInput 'route add 41216 via port1 on 48460'\n\nThen, input 'route show on 48460' to ensure route on port 1 and port 2 are correctly configured.",
  "ルーターにDNSサーバーへのルートを追加します。\n\n「route add 41216 via port1 on 48460」と入力します。\n\n次に「route show on 48460」と入力して、ポート1とポート2のルートが正しく設定されていることを確認します。")
t("[command]: route add 41216 via port1 on 48460", "[コマンド]: route add 41216 via port1 on 48460")
t("There are a few methods for a device/user to access DNS server behind the router.\n\nIn this tutorial, we will focus on only one method:\n1.  set default route to point to network that always has DNS server\n\nFor more info, press 'F1' to checkout the detailed explanations on DNS server behind router.",
  "ルーターの背後にあるDNSサーバーにデバイス/ユーザーがアクセスする方法はいくつかあります。\n\nこのチュートリアルでは1つの方法のみに焦点を当てます：\n1. DNSサーバーが常にあるネットワークを指すデフォルトルートを設定する\n\n詳細についてはF1キーを押してルーター背後のDNSサーバーの詳細説明を確認してください。")
t("press 'F1' to checkout the details", "F1キーで詳細を確認")
t("The easiest way for devices to access the DNS server behind the router is to set a default route. \n\nSet router port 1 as the default route since the DNS server is connected there. The default route acts as a fallback. Any traffic without a specific destination match automatically goes through it.\n\nInput 'route default via port1 on 48460'",
  "デバイスがルーター背後のDNSサーバーにアクセスする最も簡単な方法はデフォルトルートを設定することです。\n\nDNSサーバーが接続されているルーターのポート1をデフォルトルートに設定します。デフォルトルートはフォールバックとして機能します。特定の宛先に一致しないトラフィックは自動的にこのルートを通過します。\n\n「route default via port1 on 48460」と入力します")
t("[command]: route default via port1 on 48460", "[コマンド]: route default via port1 on 48460")
t("You should now observe that the consumers are able to reach the DNS server behind the router. \n\nPress F1 to read more on Method 2 (set designated DNS server address on consumers) and Method 3 (place DNS server on every side of router) if you want to learn more methods.",
  "コンシューマーがルーター背後のDNSサーバーに到達できるようになったことを確認してください。\n\nさらに多くの方法を学びたい場合は、F1キーを押して方法2（コンシューマーに指定DNSサーバーアドレスを設定）と方法3（ルーターの各側にDNSサーバーを配置）について詳しく読んでください。")

# Tutorial: Registry & Service Provider
t("Open Rocket Store app.\n\nPurchase The Registry app released by Rocket Store.",
  "Rocket Storeアプリを開きます。\n\nRocket Storeがリリースした The Registry アプリを購入します。")
t("launch Rocket Store app", "Rocket Storeアプリを起動")
t("Before following the step-by-step instructions to become a service provider, here's a heads-up on the required steps:\n\nTo become a 'stream-voice' provider, you need to:\n\n1. Own a domain: Register your domain on the Registry app.\n2. Run the voip-server: Launch the voip-server program.\n3. Connect a public VoIP phone: Connect a VoIP phone to the voip-server (this creates the 'stream-voice' user stack on the voip-server).\n4. DNS mapping: Map your domain (e.g., streamvoice.com) to the voip-server for consumer access.\n\nFollow the next steps to self-register a domain name and become a service provider.",
  "サービスプロバイダーになるための手順を確認しておきましょう：\n\n「stream-voice」プロバイダーになるには：\n\n1. ドメインを所有：Registryアプリでドメインを登録\n2. voip-serverを実行：voip-serverプログラムを起動\n3. パブリックVoIP電話を接続：VoIP電話をvoip-serverに接続（voip-serverに「stream-voice」USEスタックが作成される）\n4. DNSマッピング：ドメイン（例：streamvoice.com）をvoip-serverにマッピングしてコンシューマーアクセスを有効化\n\n次の手順に従ってドメイン名を自己登録し、サービスプロバイダーになりましょう。")
t("Observe which-rabbit profile in Surveyor app.\n\nNotice that 'no suitable providers for talk to someone online'.",
  "Surveyorアプリでwhich-rabbitのプロファイルを確認します。\n\n「talk to someone online」の適切なプロバイダーがいないことに注意してください。")
t("launch 'Surveyor app' and notice complaints from writing-rabbit",
  "「Surveyor」アプリを起動してwriting-rabbitの苦情を確認")
t("You can become provider to this service through The Registry app.",
  "The Registryアプリを通じてこのサービスのプロバイダーになれます。")
t("1. Open The Registry app.\n2. Click Register New Domain Name button to self-register a domain name.",
  "1. The Registryアプリを開きます。\n2. 「Register New Domain Name」ボタンをクリックしてドメイン名を自己登録します。")
t("launch The Registry app to register new domain name", "The Registryアプリを起動して新規ドメイン名を登録")
t("1. Type 'streamvoice.com' as the domain name.\n2. Set the price per consumption to 0.5 using the slider.\n3. Click (+) Associate usage button.\n4. Select 'stream-voice' from the dropdown of USE spec.\n5. Click Finalize button and followed by Confirm button.\n\nYou have now successfully register your domain name.\n",
  "1. ドメイン名に「streamvoice.com」と入力します。\n2. スライダーで1回あたりの利用料金を0.5に設定します。\n3. 「(+) Associate usage」ボタンをクリックします。\n4. USE仕様のドロップダウンから「stream-voice」を選択します。\n5. 「Finalize」ボタンをクリックし、続けて「Confirm」ボタンをクリックします。\n\nドメイン名の登録が完了しました。\n")
t("register streamvoice.com as domain name with required setting",
  "必要な設定でstreamvoice.comをドメイン名として登録")
t("Input 'program describe voip-server' on netsh.\n\nNotice that voip-server produces accept-voip-phone-connection and allows voip-phone to be connected and produce 'stream-voice' uses. ",
  "netshで「program describe voip-server」と入力します。\n\nvoip-serverがaccept-voip-phone-connectionを生産し、voip-phoneの接続と「stream-voice」USEの生産を可能にすることに注目してください。")
t("[command]: program describe voip-server", "[コマンド]: program describe voip-server")
t("The voip-server program is already installed on the server (hardware address: 15313), which is connected to the public phone via a switch.\n\nTo check running programs on the server, use the command:\nprogram view running on 15313\n\nBoth dns-lite and voip-server are currently running.",
  "voip-serverプログラムはすでにサーバー（ハードウェアアドレス：15313）にインストールされており、スイッチを介してパブリック電話に接続されています。\n\nサーバー上の実行中プログラムを確認するには、以下のコマンドを使用します：\nprogram view running on 15313\n\ndn-liteとvoip-serverの両方が現在実行中です。")
t("[command]: program view running on 15313", "[コマンド]: program view running on 15313")
t("Input 'dns map streamvoice.com as 15313' to map your registered domain name with voip server address.",
  "「dns map streamvoice.com as 15313」と入力して、登録したドメイン名をvoipサーバーアドレスにマッピングします。")
t("[command]: dns map streamvoice.com as 15313", "[コマンド]: dns map streamvoice.com as 15313")
t("Input 'watch 15313' on netsh.\n\n'stream-voice' use stack is successfully consumed by the residents through proper connection\n\n",
  "netshで「watch 15313」と入力します。\n\n「stream-voice」USEスタックが適切な接続を通じて住民に正常に消費されています\n\n")
t("[command]: watch 15313", "[コマンド]: watch 15313")
t("More apps are accessible on the Rocket Store for your convenience.\n\nFor instance, the 'Socketeer' app allows you to create riser outlets at custom positions.\n\nOnce the outlet you created is confirmed through the 'Socketeer' app, it will appear in the Tower Link app for your link configuration.\n\nYou can directly plug cables into the created outlet port, even if the outlet is not linked to another outlet in the Tower Link app.",
  "Rocket Storeにはさらに便利なアプリがあります。\n\n例えば、「Socketeer」アプリではカスタム位置にライザーアウトレットを作成できます。\n\n「Socketeer」アプリで作成したアウトレットが確認されると、Tower Linkアプリにリンク設定用として表示されます。\n\nTower Linkアプリで他のアウトレットにリンクされていなくても、作成したアウトレットポートにケーブルを直接接続できます。")
t("explore more apps in Rocket Store", "Rocket Storeでさらにアプリを探索")
t("Right click on device to copy addresses to clipboard.\n \nCtrl + V to paste on netsh terminal.",
  "デバイスを右クリックしてアドレスをクリップボードにコピーします。\n\nCtrl + Vでnetshターミナルに貼り付けます。")

# Tutorial: Endless Mode Final
t("Welcome, tower network admin!\n\nThis is a final tutorial which shows you the actual gameplay in endless mode. \n\nFeel free to end this tutorial and play endless mode when you think you are ready.",
  "タワーネットワーク管理者、ようこそ！\n\nこれはエンドレスモードの実際のゲームプレイを示す最終チュートリアルです。\n\n準備ができたと思ったら、いつでもこのチュートリアルを終了してエンドレスモードをプレイしてください。")
t("There are 3 devices in the data center (floor 0). \n1. Debugger Alice\n2. Server (MacroHard Boulder SRV)\n3. Switch (Blade10)",
  "データセンター（フロア0）には3つのデバイスがあります。\n1. Debugger Alice\n2. サーバー（MacroHard Boulder SRV）\n3. スイッチ（Blade10）")
t("Scan the device using the debugger. \n\nInput \"scan d\" into the MobileOS netsh app.\n\nNote: Click 'View MobileOS' on the left bottom of the screen or hit the \"ALT\" key to bring up your MobileOS.",
  "デバッガーを使ってデバイスをスキャンします。\n\nMobileOSのnetshアプリに「scan d」と入力します。\n\n注意：画面左下の「View MobileOS」をクリックするか「ALT」キーを押してMobileOSを表示します。")
t("Debugger can only \"see\" itself, because \n\n1. Server is not powered although it is connected to debugger\n2. No physical cable connection between debugger and switch",
  "デバッガーは自分自身のみ「認識」できます。理由は：\n\n1. サーバーはデバッガーに接続されていますが電源が入っていない\n2. デバッガーとスイッチ間に物理ケーブル接続がない")
t("Purchase Power UK-B 500 from D-Market and power up the server with the wall socket",
  "D-MarketからPower UK-B 500を購入し、壁のソケットでサーバーに電源を供給します")
t("power up the server", "サーバーの電源を入れる")
t("Scan the device using the debugger again, and the debugger will see itself and the boulder server.\n\n1. Debugger (Debugger Alice) : 92443\n2. Server (MacroHard Boulder SRV): 53800\n\nTo see the switch (blade10) from the debugger,\n\ntoggle the switch on blade10, then connect it to the debugger.",
  "デバッガーを使って再度デバイスをスキャンすると、自分自身とBoulderサーバーが認識されます。\n\n1. デバッガー（Debugger Alice）：92443\n2. サーバー（MacroHard Boulder SRV）：53800\n\nデバッガーからスイッチ（blade10）を認識するには、\n\nblade10のスイッチをオンにして、デバッガーに接続します。")
t("turn on the switch (blade10) and connect it to the debugger",
  "スイッチ（blade10）をオンにしてデバッガーに接続")
t("Every device/users connected through a switch is connected without configuration. To ensure more users can access the server, connect the server directly to the switch. \n\nPress F1 to read more about the switch.",
  "スイッチを通じて接続されたデバイス/ユーザーは設定なしで接続されます。より多くのユーザーがサーバーにアクセスできるよう、サーバーをスイッチに直接接続してください。\n\nF1キーでスイッチについてもっと読む。")
t("connect the server directly to the switch", "サーバーをスイッチに直接接続")
t("Remember your task in the tower? Make sure both producers and consumers are online happily.\n\nLaunch Surveyor app to identify their needs. \n\nCan you recognize the producers and consumers in the tower? \n\n1. Floor 1: Net Nester (consumers)\n2. Floor 2: Sync News (producer)",
  "タワーでのタスクを覚えていますか？プロデューサーとコンシューマーの両方がオンラインで満足していることを確認してください。\n\nSurveyorアプリを起動してニーズを特定します。\n\nタワー内のプロデューサーとコンシューマーを見分けられますか？\n\n1. フロア1：Net Nester（コンシューマー）\n2. フロア2：Sync News（プロデューサー）")
t("launch the Surveyor app to identify the needs of consumers and producers",
  "Surveyorアプリを起動してコンシューマーとプロデューサーのニーズを特定")
t("Differentiate their main roles (producer and consumer) through their issues and complaints, and behavior insights.\n\n1. Sync News (Producer): An individual who needs proper visitors to consume their use stack (e.g, read-text, post-text)) on their domain (news.markhor-text.site)\n\n2. Net Nester (Consumer): An individual who wants to visit websites to browse and use network services (e.g, read political news, read and comment)",
  "問題と苦情、行動分析から主な役割（プロデューサーとコンシューマー）を区別します。\n\n1. Sync News（プロデューサー）：ドメイン（news.markhor-text.site）上のUSEスタック（例：read-text、post-text）を消費する適切な訪問者が必要な個人\n\n2. Net Nester（コンシューマー）：ウェブサイトを訪問してネットワークサービス（例：政治ニュースを読む、読み書きする）を閲覧・利用したい個人")
t("Notice there are two main issues faced by Net Nesters. \n\n1. No DNS servers for 'news.markhor-text.site' to 'read and comment'\n\n2. No DNS servers for 'news.markhor-video.site' to 'read political news'\n\nNo dhcp servers for auto setup is non essential error, and you can ignore this warning now.",
  "Net Nestersが直面している2つの主な問題に注意してください。\n\n1. 「read and comment」のための「news.markhor-text.site」のDNSサーバーがない\n\n2. 「read political news」のための「news.markhor-video.site」のDNSサーバーがない\n\n自動セットアップのDHCPサーバーがないという警告は重要ではないので、今は無視できます。")
t("no dns servers for consumers", "コンシューマーにDNSサーバーがない")
t("Let's install dns-lite on the Boulder server. \n\nCan't recall the steps to have dns-lite running on the Boulder server?\n\nPress F1 to read the Tutorial: Basic Domain Name System (DNS) to install the dns program.",
  "Boulderサーバーにdns-liteをインストールしましょう。\n\nBoulderサーバーでdns-liteを実行する手順を思い出せませんか？\n\nF1キーを押して「チュートリアル：基本DNS」を読み、DNSプログラムをインストールしてください。")
t("run the dns-lite program on the server", "サーバーでdns-liteプログラムを実行")
t("After installing dns-lite on Boulder, the consumers are still not able to access the DNS server in the data center, because they are not connected to the DNS server in data center. \n\nSetup a riser link between floor 0 and floor 1 though the Tower Link app. \n\n1. Point A: Floor 0, SVJP\n2. Point B: Floor 1, XJLJ",
  "Boulderにdns-liteをインストールした後も、コンシューマーはデータセンターのDNSサーバーにアクセスできません。データセンターのDNSサーバーに接続されていないためです。\n\nTower Linkアプリでフロア0とフロア1の間にライザーリンクを設定してください。\n\n1. ポイントA：フロア0、SVJP\n2. ポイントB：フロア1、XJLJ")
t("setup a riser link between floor 0 and floor 1", "フロア0とフロア1の間にライザーリンクを設定")
t("Before traveling to floor 1, let's complete the essential connection from riser point A (SVJP) to the DNS server, so that consumers can access the DNS server. \n\n1. Connect Riser point A to the switch (blade 10)",
  "フロア1に移動する前に、ライザーポイントA（SVJP）からDNSサーバーへの必須接続を完了し、コンシューマーがDNSサーバーにアクセスできるようにしましょう。\n\n1. ライザーポイントAをスイッチ（blade 10）に接続")
t("connect riser point A (SVJP) to the switch", "ライザーポイントA（SVJP）をスイッチに接続")
t("Let's travel to floor 1 to complete our setup on floor 1, so they can access the DNS server on floor 0.",
  "フロア1に移動してフロア1の設定を完了し、フロア0のDNSサーバーにアクセスできるようにしましょう。")
t("enter the elevator to travel to floor 1", "エレベーターに乗ってフロア1に移動")
t("Continue this tutorial after you ensure: \n\n1. Proper connection on floor 1 between consumers. \n\nTo confirm this,  let's use the debugger to 'scan u'; the debugger should see 3 consumers from floor 1. ",
  "以下を確認した後、このチュートリアルを続けてください：\n\n1. フロア1でコンシューマー間の適切な接続\n\nこれを確認するため、デバッガーで「scan u」を実行します。デバッガーはフロア1の3人のコンシューマーを認識するはずです。")
t("With proper connection to the DNS server, notice that the main issues and complaints faced by the Net Nesters (consumers) are:\n\n1. No DNS entries for 'news.markhor-text.site' to 'read and comment'\n\n2. No DNS entries for 'news.markhor-video.site' to 'read political news'\n\nThey can now access the DNS server in the data center, but they do not have proper DNS lookup of the domain names they wish to visit. \n\nThis mean they do not know where to consume their use. They do not have destination address that they can visit to consume use from producer. \n",
  "DNSサーバーへの適切な接続ができた状態で、Net Nesters（コンシューマー）が直面している主な問題を確認します：\n\n1. 「read and comment」のための「news.markhor-text.site」のDNSエントリがない\n\n2. 「read political news」のための「news.markhor-video.site」のDNSエントリがない\n\nデータセンターのDNSサーバーにアクセスできるようになりましたが、訪問したいドメイン名の適切なDNSルックアップができません。\n\nつまり、USEを消費する場所がわかりません。プロデューサーからUSEを消費するために訪問できる宛先アドレスがないのです。\n")
t("no dns entries for the domain", "ドメインのDNSエントリがない")
t("Let's set up a riser link between the producer and consumers.\n\nSet up the riser with the following setup: \n\n1. Point A: Floor 0, TUJX\n2. Point B: Floor 2, YSRR\n",
  "プロデューサーとコンシューマーの間にライザーリンクを設定しましょう。\n\n以下の設定でライザーを設定します：\n\n1. ポイントA：フロア0、TUJX\n2. ポイントB：フロア2、YSRR\n")
t("set up a riser link between floor 0 and floor 2", "フロア0とフロア2の間にライザーリンクを設定")
t("After the riser link is set up, ensure riser point A (TUJX) is connected to the switch.\n\nLet's travel to floor 2 to complete the physical connection on floor 2, so that Net Nesters (consumers) on floor 1 can reach Sync News (producer) on floor 2 through our setup. ",
  "ライザーリンクの設定後、ライザーポイントA（TUJX）がスイッチに接続されていることを確認します。\n\nフロア2に移動してフロア2の物理接続を完了し、フロア1のNet Nesters（コンシューマー）がフロア2のSync News（プロデューサー）に到達できるようにしましょう。")
t("enter the elevator to travel to floor 2", "エレベーターに乗ってフロア2に移動")
t("Ensure the producer can reach the debugger from data center.\n\n1. ping 75648\n\nwhere 75648 is the hardware address of cluttered-markhor (Sync News)",
  "データセンターからプロデューサーがデバッガーに到達できることを確認します。\n\n1. ping 75648\n\n75648はcluttered-markhor（Sync News）のハードウェアアドレスです")
t("[command]: ping 75648", "[コマンド]: ping 75648")
t("Now, let's do DNS mapping so that the consumers perform DNS lookup when they want to access the services hosted by the producer. \n\nYou can copy the producer's hardware address and domain name from the clipboard directly after you click 'Copy user network details' in the Surveyor app.",
  "次に、コンシューマーがプロデューサーのサービスにアクセスする際にDNSルックアップを実行できるようDNSマッピングを行いましょう。\n\nSurveyorアプリの「Copy user network details」をクリックした後、クリップボードからプロデューサーのハードウェアアドレスとドメイン名を直接コピーできます。")
t("refer to the copied producer's details from the clipboard",
  "クリップボードからコピーしたプロデューサーの詳細を参照")
t("Do DNS mapping based on the copied information in the clipboard. \n\n1. dns map news.markhor-video.site as 75648\n2. dns map news.markhor-text.site as 75648\n\nPress F1 to refer to the Tutorial: Basic Domain Name System, if you forgot the steps for DNS configuration in the actual game.",
  "クリップボードにコピーした情報に基づいてDNSマッピングを行います。\n\n1. dns map news.markhor-video.site as 75648\n2. dns map news.markhor-text.site as 75648\n\n実際のゲームでのDNS設定手順を忘れた場合は、F1キーで「チュートリアル：基本DNS」を参照してください。")
t("correct the dns mapping for at least one domain", "少なくとも1つのドメインのDNSマッピングを修正")
t("let's watch our DNS use stack on our DNS server. It is tedius to keep referring to the DNS hardware address which is hard to remember. \n\n1. net address set dns on 53800",
  "DNSサーバーのDNS USEスタックを確認しましょう。覚えにくいDNSハードウェアアドレスを毎回参照するのは面倒です。\n\n1. net address set dns on 53800")
t("[command]: net address set dns on 53800", "[コマンド]: net address set dns on 53800")
t("Now, watch the DNS server to observe the use-stack of the DNS server. \n\nwatch @dns\n\nNotice that the dns use stack is continuously used by the consumers to perform DNS lookup",
  "DNSサーバーを監視してDNSサーバーのUSEスタックを確認します。\n\nwatch @dns\n\nDNS USEスタックがコンシューマーのDNSルックアップに継続的に使用されていることに注目してください")
t("[command]: watch @dns", "[コマンド]: watch @dns")
t("Now, you should see that all the users are actually satisfied after the correct network setup. \n\nCongratulations! This means you are now able to proceed to the next step to accept more users to live in the tower. \n\nYou can launch the Break Time app when you want to speed up or slow down time.",
  "正しいネットワーク設定後、すべてのユーザーが実際に満足していることを確認できます。\n\nおめでとうございます！これで、タワーに住む新しいユーザーを受け入れる次のステップに進むことができます。\n\n時間を加速または減速したい場合は、Break Timeアプリを起動できます。")
t("launch the Break Time app", "Break Timeアプリを起動")
t("Launch 'The Secretariat' app to accept a new floor to be onboarded in this tower. \n\nThe awaiting floor is shown in the 'Floor build' tab. Click 'Accept this build now' to spawn the floor with 'Vocal Connector' users.",
  "「The Secretariat」アプリを起動して、タワーに新しいフロアをオンボーディングします。\n\n待機中のフロアは「Floor build」タブに表示されます。「Accept this build now」をクリックして「Vocal Connector」ユーザーのフロアを生成します。")
t("launch The Secretariat app to accept a new floor",
  "The Secretariatアプリを起動して新しいフロアを承認")
t("You should now be familiar with the process. \n\n1. Set up a riser link between floor 0 and floor 3.\n2. Connect riser Point A to the switch",
  "これでプロセスに慣れたはずです。\n\n1. フロア0とフロア3の間にライザーリンクを設定\n2. ライザーポイントAをスイッチに接続")
t("setup the riser connection between floor 0 and floor3; connect riser point A to the switch",
  "フロア0とフロア3のライザー接続を設定；ライザーポイントAをスイッチに接続")

# ============================================================
# Now let's parse and process the PO file

# ============================================================
# BATCH 7: Remaining tutorials (firewall, worm, final steps)
# ============================================================
t("Travel to floor 3, and complete your connection there.",
  "フロア3に移動して、そこの接続を完了してください。")
t("enter the elevator to travel to floor 3", "エレベーターに乗ってフロア3に移動")
t("Purchase another Boulder server to set up and keep the voip-server running. \n\n1. purchase a Boulder+ server from D-market \n2. run the voip-server program on the purchased server\n3. ensure consumers from floor 3 can access the voip-server in data center through riser\n\nPress F1 to check out the Tutorial: Rocket Store and Domain Name Registration for voip-server setup.",
  "voip-serverを実行するために別のBoulderサーバーを購入します。\n\n1. D-marketからBoulder+サーバーを購入\n2. 購入したサーバーでvoip-serverプログラムを実行\n3. フロア3のコンシューマーがライザー経由でデータセンターのvoip-serverにアクセスできることを確認\n\nF1キーで「チュートリアル：Rocket Storeとドメイン名登録」のvoip-serverセットアップを確認してください。")
t("ensure Vocal Connector (consumers) access the voip-server in the data center",
  "Vocal Connector（コンシューマー）がデータセンターのvoip-serverにアクセスできることを確認")
t("The 'accept-voip-phone-connection' use stack is converted to the 'stream-voice' use stack on the voip-server through proper setup between the voip-server and voip-phone. \n\n1. watch the voip server to observe the 'stream-voice' use stack",
  "voip-serverとvoip-phoneの適切な設定により、「accept-voip-phone-connection」USEスタックがvoip-serverで「stream-voice」USEスタックに変換されます。\n\n1. voipサーバーをwatchして「stream-voice」USEスタックを確認")
t("As a provider for the stream-voice service, you need to register a new domain name.\n\n1. Launch the 'The Registry' app after installing it from the 'Rocket Store' app.",
  "stream-voiceサービスのプロバイダーとして、新しいドメイン名を登録する必要があります。\n\n1. 「Rocket Store」アプリからインストールした「The Registry」アプリを起動します。")
t("launch the 'The Registry' app", "「The Registry」アプリを起動")
t("Register your stream-voice service at an affordable price.\n\n1. Choose your domain name\n2. Use the slider to set the price per consumption for your service\n3. Click the '(+) Associate usage' button to add 'stream-voice' use on your domain.",
  "手頃な価格でstream-voiceサービスを登録します。\n\n1. ドメイン名を選択\n2. スライダーでサービスの1回あたりの利用料金を設定\n3. 「(+) Associate usage」ボタンをクリックしてドメインに「stream-voice」USEを追加")
t("register your domain for the 'stream-voice' service",
  "「stream-voice」サービス用のドメインを登録")
t("After registering your domain name for the stream-voice service, do dns mapping for your registered domain to your voip-server.",
  "stream-voiceサービスのドメイン名を登録した後、登録したドメインをvoip-serverにDNSマッピングします。")
t("When days go by, the number of visitors increases. To support a bigger network, you need to\n\n1. upgrade to padu_v1 + dns-server\n2. replace the switch with a router\n\nTo upgrade dns-lite to dns-server, you can check out the requirements to run a dns-server. \n\nType 'program describe dns-server' command\n\nThe dns-server requires 1 'store-text' as input to produce 20 'reply-dns-queries' per tick. ",
  "日数が経つにつれて訪問者が増えます。大きなネットワークをサポートするには：\n\n1. padu_v1 + dns-serverにアップグレード\n2. スイッチをルーターに交換\n\ndns-liteからdns-serverへのアップグレードには、dns-serverの実行要件を確認してください。\n\n「program describe dns-server」コマンドを入力します\n\ndns-serverはtickあたり20の「reply-dns-queries」を生産するために1つの「store-text」入力が必要です。")
t("Type the 'program describe padu_v1' command. \n\nNotice that padu_v1 produces 'store-text'; which is the required input for dns-server to produce 'reply-dns-queries'. \n\nYou do not need to replace dns-lite with dns-server + padu_v1 in this tutorial, but keep this information in mind for endless mode.",
  "「program describe padu_v1」コマンドを入力します。\n\npadu_v1が「store-text」を生産することに注目してください。これはdns-serverが「reply-dns-queries」を生産するために必要な入力です。\n\nこのチュートリアルではdns-liteをdns-server + padu_v1に交換する必要はありませんが、エンドレスモードのためにこの情報を覚えておいてください。")
t("[command]: program describe padu_v1", "[コマンド]: program describe padu_v1")
t("If you only choose to play as an intern (easy mode) in endless mode, bandwidth is not a concern in the game. You can omit the remaining router tutorial if you prefer a full switch setup in the game. \n\nHowever, if you prefer to play in standard mode, you should utilize a router for better network bandwidth optimization.\n\nLet's replace the switch with a router. \n\n1. toggle the power switch of the Disco Nano router\n\nPress F1 to refer to the Tutorial: Router Configuration to recall the steps required to configure a route on the router. ",
  "インターン（イージーモード）でプレイする場合、帯域幅はゲーム内で問題になりません。スイッチのみの構成を好む場合は、残りのルーターチュートリアルを省略できます。\n\nただし、スタンダードモードでプレイする場合は、ルーターを使用してネットワーク帯域幅を最適化することをお勧めします。\n\nスイッチをルーターに交換しましょう。\n\n1. Disco Nanoルーターの電源スイッチをオンにする\n\nF1キーで「チュートリアル：ルーター設定」を参照して、ルーターのルート設定手順を思い出してください。")
t("toggle the power switch of the Disco Nano router", "Disco Nanoルーターの電源スイッチをオンにする")
t("Before typing the route command, ensure the debugger is connected to the router.\n\n2. set a route on port2 of the router as the producer's hardware address (75648)\n\ninput 'route add 75648 via port2 on 69681'",
  "routeコマンドを入力する前に、デバッガーがルーターに接続されていることを確認します。\n\n2. ルーターのport2にプロデューサーのハードウェアアドレス（75648）へのルートを設定\n\n「route add 75648 via port2 on 69681」と入力します")
t("[command]: route add 75648 via port2 on 69681", "[コマンド]: route add 75648 via port2 on 69681")
t("For the consumers who are connected to the router to access the DNS server without extra route configuration, \n\ninput 'route default via port3 on 69681'\n\nIn the next step, you will connect the DNS server to port3 of the router.\n",
  "ルーターに接続されたコンシューマーが追加のルート設定なしでDNSサーバーにアクセスできるように、\n\n「route default via port3 on 69681」と入力します\n\n次の手順で、DNSサーバーをルーターのport3に接続します。\n")
t("[command]: route default via port3 on 69681", "[コマンド]: route default via port3 on 69681")
t("Ensure the connections for consumers, producers and dns-server are complete through the router.\n\n1. connect DNS server to the default port of the router (port3).\n2. connect the producer link (TUJX) to port2 of the router\n3. connect the consumer link (SVJP) to port4 of the router\n\nLaunch Surveyor app to notice the satiety of the users after replacing the switch with a router. They should be satisfied when they are able to reach each other.",
  "コンシューマー、プロデューサー、DNSサーバーのルーター経由の接続が完了していることを確認します。\n\n1. DNSサーバーをルーターのデフォルトポート（port3）に接続\n2. プロデューサーリンク（TUJX）をルーターのport2に接続\n3. コンシューマーリンク（SVJP）をルーターのport4に接続\n\nSurveyorアプリを起動して、スイッチをルーターに交換した後のユーザーの満足度を確認します。互いに到達できれば満足しているはずです。")
t("complete the connection of the network to the router",
  "ネットワークのルーターへの接続を完了")
t("You have successfully acquired all the necessary knowledge before entering endless mode. \n\nAlways press F1 to look at the steps recap for each tutorial if you have issues while playing.",
  "エンドレスモードに入る前に必要なすべての知識を習得しました。\n\nプレイ中に問題がある場合は、いつでもF1キーで各チュートリアルのステップ概要を確認してください。")
t("completed all essential tutorials", "すべての必須チュートリアルを完了")
t("Complete connection between Net Nester (consumers) and DNS server. \n\n1. Ensure Net Nesters are connected through switch with ethernet cables. \n2. Ensure switch is powered on through toggle switch. Observe the led indicator to confirm that. \n3. Ensure the switch is connected to riser Point B to access DNS server in floor 0.",
  "Net Nester（コンシューマー）とDNSサーバー間の接続を完了します。\n\n1. Net Nesters がEthernetケーブルでスイッチ経由で接続されていることを確認\n2. スイッチの電源がトグルスイッチでオンになっていることを確認。LEDインジケーターで確認\n3. スイッチがライザーポイントBに接続されてフロア0のDNSサーバーにアクセスできることを確認")
t("complete connection in floor 1; and ensure switch is powered so at least one user in floor 1 can reach dns server on floor 0",
  "フロア1の接続を完了；スイッチの電源を入れてフロア1のユーザーがフロア0のDNSサーバーに到達できるようにする")
t("Travel to floor 0 to continue tutorial after the connection in floor 1 completed. ",
  "フロア1の接続完了後、フロア0に移動してチュートリアルを続行します。")
t("Connect riser point B to Sync News (producer) so the consumers can access their service after proper setup.\n\nTravel back to floor0 after completing the connection.",
  "コンシューマーが適切な設定後にサービスにアクセスできるように、ライザーポイントBをSync News（プロデューサー）に接続します。\n\n接続完了後、フロア0に戻ります。")
t("connect producer to riser point B", "プロデューサーをライザーポイントBに接続")
t("Complete the connection in floor 3. \n\nYou can use your creativity to connect the users in this floor. ",
  "フロア3の接続を完了します。\n\nこのフロアのユーザー接続は自由に行ってください。")
t("Checkout Vocal Connector profile on Surveyor app. \n\nNotice that there is no suitable provider for them to \"talk to someone online\".",
  "SurveyorアプリでVocal Connectorのプロファイルを確認します。\n\n「talk to someone online」の適切なプロバイダーがいないことに注意してください。")
t("Now, you can become the provider to the service which is desired by the consumer. \n\ninput 'program list' to identify potential program.",
  "コンシューマーが望むサービスのプロバイダーになれます。\n\n「program list」と入力して候補プログラムを確認します。")
t("Notice 'voip-server' program? \n\nFind out voip-server program through 'program describe voip-server' command",
  "「voip-server」プログラムに気づきましたか？\n\n「program describe voip-server」コマンドでvoip-serverプログラムの詳細を確認します")
t("voip-server is a producer program, which produce 'accept-voip-phone-connection' use stack. It also allows voip-phone to be connected and produce 'stream-voice' uses. \n\nLet's produce 'stream-voice' uses yourself through voip-server program.",
  "voip-serverはプロデューサープログラムで、「accept-voip-phone-connection」USEスタックを生産します。また、voip-phoneの接続と「stream-voice」USEの生産を可能にします。\n\nvoip-serverプログラムを通じて自分で「stream-voice」USEを生産しましょう。")
t("Ensure you have complete connection between consumers, voip phone outlet and riser through switch.",
  "コンシューマー、voip電話アウトレット、ライザー間のスイッチ経由の接続が完了していることを確認します。")
t("ensure proper complete between users", "ユーザー間の適切な接続を確認")
t("Head back to data center after completing connection between floor 3 users to data center.",
  "フロア3のユーザーとデータセンター間の接続完了後、データセンターに戻ります。")
t("enter elevator to travel to floor 0", "エレベーターに乗ってフロア0に移動")

# Tutorial: Firewall & Worm removal
t("Expectations:\n\n1. Use network tap to inspect traffic passing through a device. (pcap routine)\n2. Use network firewall to filter unwanted traffic (e.g., text-scraping) from malicious users. (firewall routine)",
  "目標：\n\n1. ネットワークタップを使用してデバイスを通過するトラフィックを検査（pcapルーチン）\n2. ネットワークファイアウォールを使用して悪意あるユーザーからの不要なトラフィック（テキストスクレイピング等）をフィルタリング（firewallルーチン）")
t("Certain users may have malicious behavior that is not shown on the Surveyor application. There are two malicious activities ongoing now:\n\n1. Morris Worm\n2. Text Scraping\n\nThese malicious behaviors can affect the health of the network and have negative safety impact on other users.",
  "特定のユーザーにはSurveyorアプリに表示されない悪意ある行動がある場合があります。現在2つの悪意ある活動が進行中です：\n\n1. Morrisワーム\n2. テキストスクレイピング\n\nこれらの悪意ある行動はネットワークの健全性に影響を与え、他のユーザーに悪影響を及ぼします。")
t("Notice that the producer's satiety has been fluctuating.\n\nLet's observe the traffic which traverses to the producer.\n",
  "プロデューサーの満足度が変動していることに注目してください。\n\nプロデューサーに到達するトラフィックを観察しましょう。\n")
t("Launch Surveyor app to monitor issues and complaints of producer (WireSync News)\n\nWireSync News has a complaint that says 'Our text content is being scraped over tcp/8034'.\n\nFrom WireSync News's complaint, we know that tcp/8034 is the traffic for a malicious user to scrape text content from WireSync News.",
  "Surveyorアプリを起動してプロデューサー（WireSync News）の問題と苦情を監視します\n\nWireSync Newsの苦情に「Our text content is being scraped over tcp/8034」とあります。\n\nWireSync Newsの苦情から、tcp/8034が悪意あるユーザーのテキストスクレイピングに使用されていることがわかります。")
t("To observe the traffic between consumers and the producer, we can use a network tap.\n\nConnect network tap port0 to the switch with the purple cable.\n\nNow, the network tap is connected to the network that connects the producer and consumers.\n",
  "コンシューマーとプロデューサー間のトラフィックを観察するために、ネットワークタップを使用できます。\n\nネットワークタップのport0をpurpleケーブルでスイッチに接続します。\n\nこれで、ネットワークタップがプロデューサーとコンシューマーを接続するネットワークに接続されました。\n")
t("connect network tap port0 to the switch with the purple cable",
  "ネットワークタップのport0をpurpleケーブルでスイッチに接続")
t("Type 'man pcap' in the netsh app.\n\nThe pcap command starts traffic capture on a network tap.\n\nThen, type 'pcap on 97889'.",
  "netshアプリで「man pcap」と入力します。\n\npcapコマンドはネットワークタップでトラフィックキャプチャを開始します。\n\n次に「pcap on 97889」と入力します。")
t("[command]: pcap on 97889", "[コマンド]: pcap on 97889")
t("Observe the traffic from the network tap port0.\n\nMalicious traffic detected:\n\n- tcp/8034: text scraping\n- tcp/510-tcp/519: morris replication",
  "ネットワークタップport0からのトラフィックを観察します。\n\n悪意あるトラフィックを検出：\n\n- tcp/8034: テキストスクレイピング\n- tcp/510-tcp/519: morrisワーム複製")
t("Move purple cable from switch to firewall port3 and check traffic.\n\nFirewall shows same malicious traffic:\n-tcp/8034 and tcp/510-519 pass through (firewall interconnected to entire network)\n\nObserve the actual traffic required:\n-tcp/80: web access\n-tcp/23: debugger access\n-udp/53: DNS query",
  "purpleケーブルをスイッチからファイアウォールport3に移動してトラフィックを確認します。\n\nファイアウォールでも同じ悪意あるトラフィックが表示されます：\n-tcp/8034とtcp/510-519が通過（ファイアウォールはネットワーク全体に接続）\n\n必要な実際のトラフィックを確認：\n-tcp/80: Webアクセス\n-tcp/23: デバッガーアクセス\n-udp/53: DNSクエリ")
t("move purple cable from switch to firewall port3",
  "purpleケーブルをスイッチからファイアウォールport3に移動")
t("Firewalls can be used to protect devices/users by filtering unwanted traffic and blocking malicious activities. When network traffic arrives, firewall policies grant or deny passage. We need to deny malicious traffic but allow legitimate traffic.\n\nFirst, check current firewall policies:\n-Type 'man firewall' in netsh app\n-Type 'firewall show on 14673' to check applied policies before adding new ones",
  "ファイアウォールは不要なトラフィックをフィルタリングし悪意ある活動をブロックしてデバイス/ユーザーを保護できます。ネットワークトラフィックが到着すると、ファイアウォールポリシーが通過を許可または拒否します。悪意あるトラフィックを拒否し、正当なトラフィックを許可する必要があります。\n\nまず、現在のファイアウォールポリシーを確認します：\n-netshアプリで「man firewall」と入力\n-「firewall show on 14673」で新しいポリシーを追加する前に適用済みポリシーを確認")
t("[command]: firewall show on 14673", "[コマンド]: firewall show on 14673")
t("The default firewall policy is allow, which means it allows all traffic to traverse.\n\nIn this tutorial, we will use a method that blacklists all traffic and only whitelists wanted traffic.\n\nTo allow debugger access, input 'firewall allow tcp/23 on 14673'. \n\nThis prevents you from being locked out of the firewall.",
  "デフォルトのファイアウォールポリシーはallowで、すべてのトラフィックの通過を許可します。\n\nこのチュートリアルでは、すべてのトラフィックをブラックリストに登録し、必要なトラフィックのみをホワイトリストに登録する方法を使います。\n\nデバッガーアクセスを許可するために「firewall allow tcp/23 on 14673」と入力します。\n\nこれでファイアウォールからロックアウトされることを防ぎます。")
t("[command]: firewall allow tcp/23 on 14673", "[コマンド]: firewall allow tcp/23 on 14673")
t("2. To allow online activities for consumers, \n\ninput 'firewall allow tcp/80 on 14673'",
  "2. コンシューマーのオンライン活動を許可するために、\n\n「firewall allow tcp/80 on 14673」と入力します")
t("[command]: firewall allow tcp/80 on 14673", "[コマンド]: firewall allow tcp/80 on 14673")
t("3. Then, to allow consumers to perform DNS query, \n\ninput 'firewall allow udp/53 on 14673'",
  "3. 次に、コンシューマーがDNSクエリを実行できるように、\n\n「firewall allow udp/53 on 14673」と入力します")
t("[command]: firewall allow udp/53 on 14673", "[コマンド]: firewall allow udp/53 on 14673")
t("Lastly, ensure all other traffic is denied as the default firewall policy. \n\nInput 'firewall default deny on 14673'; this is to block all malicious traffic since this is the default policy.",
  "最後に、他のすべてのトラフィックがデフォルトのファイアウォールポリシーとして拒否されるようにします。\n\n「firewall default deny on 14673」と入力します。これはデフォルトポリシーとしてすべての悪意あるトラフィックをブロックします。")
t("[command]: firewall default deny on 14673", "[コマンド]: firewall default deny on 14673")
t("Input 'pcap on 97889' again.\n\nNotice that tcp/8034 and tcp/510-tcp/519 can no longer be seen from the network tap, which means this traffic is denied from passing through the firewall.\n\nUnplug the network tap from firewall port3.\n\nUse the yellow cable to connect WireSync News to firewall port3.",
  "「pcap on 97889」をもう一度入力します。\n\ntcp/8034とtcp/510-tcp/519がネットワークタップから見えなくなったことを確認します。これらのトラフィックがファイアウォールを通過できなくなりました。\n\nネットワークタップをファイアウォールport3から外します。\n\nyellowケーブルでWireSync Newsをファイアウォールport3に接続します。")
t("use the yellow cable to connect WireSync News to firewall port3.",
  "yellowケーブルでWireSync Newsをファイアウォールport3に接続します。")
t("However, the whole network is still infected by worm activity. The worm program remains on the server and router unless you actively remove it.\n\nTo remove the worm from the routers/servers, one needs to separate the routers/servers from one another to prevent them from infecting each other again while removing the worm.\n\n1. Unplug the green cable from firewall port2 to disconnect the router from the network.",
  "しかし、ネットワーク全体はまだワーム活動に感染しています。ワームプログラムは積極的に削除しない限り、サーバーとルーターに残ります。\n\nルーター/サーバーからワームを除去するには、除去中に互いに再感染しないよう分離する必要があります。\n\n1. ファイアウォールport2からgreenケーブルを外してルーターをネットワークから切断します。")
t("unplug the green cable from firewall port2 to disconnect the router",
  "ファイアウォールport2からgreenケーブルを外してルーターを切断")
t("2. Unplug the green cable from firewall port1 to disconnect the server from the network.",
  "2. ファイアウォールport1からgreenケーブルを外してサーバーをネットワークから切断します。")
t("unplug the green cable from firewall port1 to disconnect the server",
  "ファイアウォールport1からgreenケーブルを外してサーバーを切断")
t("Connect the debugger to Boulder server port0 using the white cable to uninstall the program.\n\n1. Unplug the white cable from the switch (blade 10)\n2. Plug the white cable into Boulder server port0",
  "whiteケーブルでデバッガーをBoulderサーバーport0に接続してプログラムをアンインストールします。\n\n1. スイッチ（blade 10）からwhiteケーブルを外す\n2. whiteケーブルをBoulderサーバーport0に接続")
t("plug the white cable into the server (Boulder) port0",
  "whiteケーブルをサーバー（Boulder）のport0に接続")
t("1. Input 'program view running on 41216'\nNotice that morris19 is running on the server.\n\n2. Input 'program uninstall morris19 on 41216'\nNotice that morris19 is removed from the server now.",
  "1. 「program view running on 41216」と入力\nmorris19がサーバーで実行中であることを確認します。\n\n2. 「program uninstall morris19 on 41216」と入力\nmorris19がサーバーから削除されたことを確認します。")
t("[command]: program uninstall morris19 on 41216", "[コマンド]: program uninstall morris19 on 41216")
t("Now, let's proceed to remove the worm program from the router.\n\nWe need to use a different approach to remove the worm from the router since we cannot uninstall the program from the router through the program routine.\n\n1. Unplug the white cable from server.\n2. Plug the white cable into the router port1 to connect the debugger to the router.",
  "では、ルーターからワームプログラムを除去しましょう。\n\nルーターからはprogramルーチンでプログラムをアンインストールできないため、別のアプローチが必要です。\n\n1. サーバーからwhiteケーブルを外す\n2. whiteケーブルをルーターのport1に接続してデバッガーをルーターに接続")
t("plug the white cable into the router port1 to connect the debugger to the router",
  "whiteケーブルをルーターのport1に接続してデバッガーをルーターに接続")
t("Type 'man sftp'\n\nsftp is a routine for remote file backup/migration.",
  "「man sftp」と入力します\n\nsftpはファイルのリモートバックアップ/移行用ルーチンです。")
t("[command]: man sftp", "[コマンド]: man sftp")
t("To list all the files on the router,\n\nType 'sftp ls on 51727'",
  "ルーター上のすべてのファイルを一覧表示するには、\n\n「sftp ls on 51727」と入力します")
t("[command]: sftp ls on 51727", "[コマンド]: sftp ls on 51727")
t("Notice that /bin/morris19 is where the worm resides in the router.\n\nRemove this worm file from the router.\n\nType 'sftp rm /bin/morris19 on 51727'",
  "/bin/morris19がルーター内のワームの場所であることに注目します。\n\nルーターからこのワームファイルを削除します。\n\n「sftp rm /bin/morris19 on 51727」と入力します")
t("[command]: sftp rm /bin/morris19 on 51727", "[コマンド]: sftp rm /bin/morris19 on 51727")
t("Type 'sftp ls on 51727' again to ensure the worm program is removed from the router.",
  "「sftp ls on 51727」をもう一度入力してワームプログラムがルーターから削除されたことを確認します。")
t("Now, put devices/users who will be affected by malicious activities behind the firewall.\n\n1. Use green cable to connect the router to the firewall port2",
  "悪意ある活動の影響を受けるデバイス/ユーザーをファイアウォールの背後に配置します。\n\n1. greenケーブルでルーターをファイアウォールport2に接続")
t("use green cable to connect the router to the firewall port2",
  "greenケーブルでルーターをファイアウォールport2に接続")
t("2. Use green cable to connect the server back to the firewall port1",
  "2. greenケーブルでサーバーをファイアウォールport1に再接続")
t("use green cable to connect the server back to the firewall port1",
  "greenケーブルでサーバーをファイアウォールport1に再接続")
t("Launch the Surveyor app to ensure the producer is no longer being scraped by malicious users.\n\nYou should notice that the producer no longer has issues with text-scraping, and worm activity is not infecting the router, server, and the producer.",
  "Surveyorアプリを起動して、プロデューサーが悪意あるユーザーにスクレイピングされなくなったことを確認します。\n\nプロデューサーにテキストスクレイピングの問題がなくなり、ワーム活動がルーター、サーバー、プロデューサーに感染していないことを確認できます。")
t("The current tutorial whitelists wanted traffic only.\n\nAlternative Method: \n\nTo blacklist malicious traffic instead:\n1. Create deny policy for each worm traffic (tcp/510 - tcp/519 for morris19)\n2. Add deny policy for text scraping: 'firewall deny tcp/8034 on 14673'\n\nPress F1 to read more about firewall policies.",
  "このチュートリアルでは必要なトラフィックのみをホワイトリストに登録しました。\n\n代替方法：\n\n悪意あるトラフィックをブラックリストに登録する場合：\n1. 各ワームトラフィックの拒否ポリシーを作成（morris19の場合 tcp/510 - tcp/519）\n2. テキストスクレイピングの拒否ポリシーを追加：「firewall deny tcp/8034 on 14673」\n\nF1キーでファイアウォールポリシーの詳細を読めます。")

# ============================================================
# BATCH 8: Misc UI variants, file descriptions, hints
# ============================================================
t("Get real-time insights on your tower\u2019s population with monitors built for data display and analysis.",
  "データ表示と分析に特化したモニターでタワーの人口に関するリアルタイムの分析情報を取得。")
t("user file.", "ユーザーファイル。")
t("virtual machine.", "仮想マシン。")
t("program binary.", "プログラムバイナリ。")
t("router config.", "ルーター設定。")
t("dhcp server config.", "DHCPサーバー設定。")
t("firewall config.", "ファイアウォール設定。")
t("dns zone mapping", "DNSゾーンマッピング")
t("vlan tag config", "VLANタグ設定")
t("data storage.", "データストレージ。")
t("Checkout", "チェックアウト", "ecommerce")
t("Add to cart", "カートに追加", "ecommerce")
t("Remove from cart", "カートから削除", "ecommerce")
t("Nothing in cart", "カートに何もありません", "ecommerce")
t("Modify cart", "カートを変更", "ecommerce")
t("satiety: {satiety_ratio}%", "満足度: {satiety_ratio}%", "user_satiety")
t("Bulk purchased items will be delivered one at a time to the selected floor",
  "まとめ買いした商品は選択したフロアに1つずつ配達されます")
t("Automatic replacement incurs a daily fee of {daily_fee} per device and costs {replace_price} the device breaks.",
  "自動交換は1デバイスあたり日額 {daily_fee} の手数料がかかり、デバイス故障時に {replace_price} のコストがかかります。")
t("Automatic replacement incurs a daily fee of 30 per device and costs more when the device breaks.",
  "自動交換は1デバイスあたり日額30の手数料がかかり、デバイス故障時にはさらにコストがかかります。")
t("On successful consumption, users pay [color=yellow]{ppu}[/color] per use (billed end of day).",
  "消費成功時、ユーザーは1回あたり [color=yellow]{ppu}[/color] を支払います（日末請求）。")
t("It cost [color=yellow]{regcost}[/color] when it was registered",
  "登録時のコストは [color=yellow]{regcost}[/color] でした")
t("There were [color=yellow]{n_visit_today}[/color] visits today, and [color=yellow]{n_visit_total}[/color] all-time.",
  "本日の訪問数は [color=yellow]{n_visit_today}[/color]、累計 [color=yellow]{n_visit_total}[/color] です。")
t("The revenue generated everytime an end user consumes the service (billed daily). Setting this too high will cause users to not want to use this service.",
  "エンドユーザーがサービスを利用するたびに発生する収益（日次請求）。高すぎると、ユーザーがサービスを利用しなくなります。")
t("The camera app lets you capture stunning photos with ease. \n\nWant to take your photography skills to the next level? Download it now and start snapping!",
  "カメラアプリで美しい写真を簡単に撮影。\n\n写真スキルをレベルアップしたいですか？今すぐダウンロードして撮影を始めましょう！")
t("Offer's a single pane of glass to see all DNS entries mapping, network address assignments and device locations, and automated device replacement packages at affordable rates.\n\nThe best asset/network management app on the market!",
  "DNSエントリマッピング、ネットワークアドレス割当、デバイスの場所、そして手頃な価格の自動デバイス交換パッケージを一画面で確認。\n\n市場最高の資産/ネットワーク管理アプリ！")
t("The registry lets you register new domain names and services.\n\nGot a service you want to host? Register them here!",
  "The Registryで新しいドメイン名とサービスを登録できます。\n\nホストしたいサービスがありますか？ここで登録しましょう！")
t("NEEDZ a physical LabeL? Nothing is as TRUSTworthy as our Stick-IT notez!\n\nPriNtZ and stick your own sticky notez to your plantz, friend's head, walls, and most importantly, your computery devices.",
  "物理ラベルが必要？Stick-ITメモほど信頼できるものはありません！\n\n自分のメモを印刷して植木、友達の頭、壁、そして最も重要なコンピューターデバイスに貼りましょう。")
t("Barracks and sons racking and shelving company app.\n\nFor all your shelves/racks installation needs.",
  "Barracks and Sonsラック＆棚アプリ。\n\n棚/ラックの設置ニーズに対応。")
t("Socket outlet maker application.\n\nSimple sockets for everyone.",
  "ソケットアウトレットメーカーアプリ。\n\nシンプルなソケットを全員に。")
t("[u]How to use?[/u]\n\n1. Input text to add as a sticky note.\n2. choose a color.\n3. click \"PRINTZ\".\n4. move mouse to where you want to place the notez.\n5. left click to paste the note.\n6. to remove a note, hover your mouse over and press 'T'.",
  "[u]使い方[/u]\n\n1. 付箋として追加するテキストを入力。\n2. 色を選ぶ。\n3. \"PRINTZ\"をクリック。\n4. メモを配置したい場所にマウスを移動。\n5. 左クリックでメモを貼り付け。\n6. メモを削除するには、マウスオーバーして「T」キーを押す。")
t("Issue a network outage notice to floor {n}.\n\t\t\t\nAll users on the floor will become inactive at the start of day {start_day}.\nThey will resume activities at the start of day {end_day}.\n\nFollowing the Secretariat's instructions, you can only issue outage notices every {k} days. \nYou can currently issue {t} network outage notices.",
  "フロア {n} にネットワーク停止通知を発行。\n\t\t\t\nフロアのすべてのユーザーは {start_day} 日目の開始時に非アクティブになります。\n{end_day} 日目の開始時に活動を再開します。\n\n事務局の指示に従い、{k} 日ごとにのみ停止通知を発行できます。\n現在 {t} 回のネットワーク停止通知を発行できます。")
t("The higher this is, the more influence it has over the user's satiety.",
  "高いほどユーザーの満足度への影響が大きくなります。")
t("Number of days left before SLA breach incidents will start to appear for this user.",
  "このユーザーのSLA違反イベントが発生するまでの残り日数。")
t("The Secretariat offers Request for proposals (RFPs) services for a fee. This service puts the current proposals on hold and new ones are requested.",
  "事務局は有料でRFP（提案要求）サービスを提供しています。このサービスは現在の提案を保留にし、新しい提案を要求します。")
t("Same floor links are heavily taxed due to tower walling regulations",
  "同一フロアリンクはタワー壁面規制により高い税金がかかります")
t("make the DHCP server auto assign network addresses with specific prefix.",
  "DHCPサーバーが特定のプレフィックスでネットワークアドレスを自動割当するようにする。")
t("make the DHCP server assign a specific network address based on hardware address.",
  "DHCPサーバーがハードウェアアドレスに基づいて特定のネットワークアドレスを割り当てるようにする。")
t("DHCP server {dhcpaddr} now auto assigns network address with prefix '{prefix}' for clients",
  "DHCPサーバー {dhcpaddr} がクライアントにプレフィックス '{prefix}' でネットワークアドレスを自動割当します")
t("DHCP server {dhcpaddr} now auto designates these DNS servers for clients.",
  "DHCPサーバー {dhcpaddr} がクライアントにこれらのDNSサーバーを自動指定します。")
t("network address must begin with a '@' and may only consist of digits 0-9, alphabets a-z, '_' underscore, '-' dash and '/' slash characters.",
  "ネットワークアドレスは '@' で始まり、数字0-9、アルファベットa-z、'_' アンダースコア、'-' ダッシュ、'/' スラッシュのみ使用できます。")
t("DHCP server {dhcpaddr} network address binding for {hwaddr} cleared.",
  "DHCPサーバー {dhcpaddr} の {hwaddr} のネットワークアドレスバインドをクリアしました。")
t("the routine lists only debuggers that are RUNNING, make sure to power them up",
  "このルーチンは実行中のデバッガーのみ表示します。電源が入っていることを確認してください")
t("currently, debugger '{dbgaddr}' is set as the default debugger with the '{always}' command.",
  "現在、'{always}' コマンドでデバッガー '{dbgaddr}' がデフォルトデバッガーに設定されています。")
t("starts traffic capture on a network tap, with optional traffic filters.",
  "ネットワークタップでトラフィックキャプチャを開始（オプションのトラフィックフィルター付き）。")
t("routing rule destination must be either a prefix of a network address or a hardware address.",
  "ルーティングルールの宛先はネットワークアドレスのプレフィックスまたはハードウェアアドレスである必要があります。")
t("routing rule source address must be either a prefix of a network address or a hardware address.",
  "ルーティングルールのソースアドレスはネットワークアドレスのプレフィックスまたはハードウェアアドレスである必要があります。")
t("copied '{filename}' (size={size}) from {dev} to {dst} as '{rename}'.",
  "'{filename}'（サイズ={size}）を {dev} から {dst} に '{rename}' としてコピーしました。")
t("perform a network graph trace from address2 to address1 using a debugger.",
  "デバッガーを使用してaddress2からaddress1へのネットワークグラフトレースを実行。")
t("Invalid VLAN tag, must begin with '#' and contains alpha-numeric, -, _ or /.",
  "無効なVLANタグ。'#'で始まり英数字、-、_、/を含む必要があります。")
t("Invalid subinterface name '{subif}', must be alpha-numeric of length 3 or below",
  "無効なサブインターフェース名 '{subif}'。3文字以下の英数字である必要があります")
t("Ensure {tft} traffic from {src} to {dst} is allowed by all firewalls that it will pass through.",
  "{src} から {dst} への {tft} トラフィックが通過するすべてのファイアウォールで許可されていることを確認してください。")
t("Use trace/ping utilities. you may also try to connect your debugger at different points in the network.",
  "trace/pingユーティリティを使用してください。ネットワークの異なるポイントにデバッガーを接続することもできます。")
t("New floors can be unlocked by surviving until day 40 on an endless run.",
  "エンドレスランで40日目まで生存すると新しいフロアがアンロックされます。")
t("This address is currently copied (right click textboxes to paste)",
  "このアドレスはコピー済みです（テキストボックスを右クリックで貼り付け）")
t("We have reached the maximum input for processing! If you are still unable to send after multiple attempts, please contact us at support@pocosia.com",
  "処理可能な入力の上限に達しました！複数回試しても送信できない場合は、support@pocosia.comまでお問い合わせください。")
t("More details would be super helpful! The more details you can share about the issue, the better we can fix it. Mind adding some extra info and trying again?",
  "詳細な情報をいただけると大変助かります！問題について詳しく共有いただけるほど、より良く修正できます。追加情報を記入してもう一度お試しいただけますか？")
t("We would love to hear feedback/bug report from you\nPlease let us know the details of your feedback/bugs report",
  "フィードバック/バグ報告をお待ちしています\nフィードバック/バグ報告の詳細をお聞かせください")
t("Press F1 to refer to the tutorial recap (your learning material).",
  "F1キーでチュートリアルの振り返り（学習資料）を参照できます。")
t("device/user access to the debugger for network troubleshooting/configuration tasks",
  "ネットワークトラブルシューティング/設定作業用にデバイス/ユーザーがデバッガーにアクセス")
t("install DNS program on server (Boulder series) using netsh\ncommand: [program install dns-lite on <server address>]",
  "netshを使用してサーバー（Boulderシリーズ）にDNSプログラムをインストール\nコマンド: [program install dns-lite on <server address>]")
t("correct DNS mapping through netsh \ncommand: [dns map <producer's domain> as <producer's address>]",
  "netshで正しいDNSマッピングを設定\nコマンド: [dns map <producer's domain> as <producer's address>]")
t("[i][color=#18fa80]Debugger Alice (Debugger)[/color][/i]: Allows troubleshooting and configuration of your operating network using the netsh application  \n[i][color=#18fa80]Boulder (Server)[/color][/i]: General computing server to run programs (e.g., DNS server)  \n[i][color=#18fa80]Blade10 (Switch)[/color][/i]: Simplest, low-cost, and inefficient way for device/user interconnection to facilitate network traversal (real-life example: hub)  \n[i][color=#18fa80]DiscoMicro (Router)[/color][/i]: Optimized bandwidth usage for device/user interconnection to facilitate network traversal; requires route configuration using netsh  \n[i][color=#18fa80]Producer[/color][/i]: User who use your network to reach consumers; their content is consumed by end-users\n[i][color=#18fa80]Consumer[/color][/i]: User who use your network to browse and access network services",
  "[i][color=#18fa80]Debugger Alice（デバッガー）[/color][/i]: netshアプリを使用してネットワークのトラブルシューティングと設定を行います\n[i][color=#18fa80]Boulder（サーバー）[/color][/i]: プログラム（DNSサーバー等）を実行する汎用コンピューティングサーバー\n[i][color=#18fa80]Blade10（スイッチ）[/color][/i]: デバイス/ユーザー相互接続のための最もシンプルで低コストだが非効率な方法（現実の例：ハブ）\n[i][color=#18fa80]DiscoMicro（ルーター）[/color][/i]: デバイス/ユーザー相互接続のための最適化された帯域幅使用；netshによるルート設定が必要\n[i][color=#18fa80]プロデューサー[/color][/i]: コンシューマーに到達するためにネットワークを使用するユーザー；コンテンツはエンドユーザーに消費される\n[i][color=#18fa80]コンシューマー[/color][/i]: ネットワークサービスを閲覧・利用するためにネットワークを使用するユーザー")
t("[i][color=#18fa80]Debugger Alice (Debugger)[/color][/i]: Allow me to check for issues!",
  "[i][color=#18fa80]デバッガーAlice（デバッガー）[/color][/i]: 問題をチェックさせてください！")

# Difficulty descriptions (variants)
t("This game is a complex sandbox which may be a frustrating experience if your goal is just to take it easy.\n\nDepending on your preference on how to play this game, the following are difficulty presets that may suitable to different players with varying technical backgrounds. This setting can be changed later on.",
  "このゲームは複雑なサンドボックスゲームで、のんびりプレイしたい場合はストレスがかかるかもしれません。\n\nプレイスタイルの好みに応じて、技術的なバックグラウンドが異なるプレイヤーに適した難易度プリセットがあります。この設定は後から変更できます。")
t("In easy mode, days are longer and income is increased, with lower daily expenses. Users also have a longer grace period before SLA breach events can occur. Devices do not fail and there are no power outages. Devices have unlimited bandwidth and users will do their own DNS mapping. \n\nSuitable for easy-goers that just want to enjoy physically connecting the residents in the Tower. Minimum server configuration required (e.g., installing DNS servers).",
  "イージーモードでは、日が長くなり収入が増加し、日次費用が低下します。SLA違反イベントが発生する前のユーザーの猶予期間も長くなります。デバイスは故障せず、停電もありません。デバイスの帯域幅は無制限で、ユーザーが自分でDNSマッピングを行います。\n\nタワーの住民を物理的に接続することを楽しみたいカジュアルプレイヤーに最適。最小限のサーバー設定（DNSサーバーのインストール等）が必要です。")
t("In standard mode, devices will randomly fail after their warranty period has expired. Power outage and surge events may occur. Devices also have finite bandwidth and can be \"overloaded\". DNS mapping is global, but are entirely handled by the player. Programs will automatically start when installed and when the device is powered up.\n\nSuitable for players that have basic system administration knowledge, or for those who enjoys problem solving.",
  "スタンダードモードでは、保証期間終了後にデバイスがランダムに故障します。停電やサージイベントが発生する可能性があります。デバイスの帯域幅は有限で「過負荷」になることがあります。DNSマッピングはグローバルですが、すべてプレイヤーが管理します。プログラムはインストール時とデバイス起動時に自動的に開始されます。\n\n基本的なシステム管理知識を持つプレイヤーや、問題解決を楽しむプレイヤーに最適。")
t("In hard mode, power outage and surge events occur more frequently. Accessing devices (even for configuration/monitoring) will cost bandwidth. Programs do not automatically start when installed or when the device is powered up. DNS mapping is local, which means different DNS servers responds differently based on its own configuration. All devices (including the debugger) requires a Network Address assigned to initiate requests.\n\nSuitable for players that has survived to day 40 in Standard mode, or for those who REALLY enjoys hardcore problem solving.",
  "ハードモードでは、停電やサージイベントがより頻繁に発生します。デバイスへのアクセス（設定/監視でも）に帯域幅を消費します。プログラムはインストール時やデバイス起動時に自動起動しません。DNSマッピングはローカルで、異なるDNSサーバーはそれぞれの設定に基づいて異なる応答をします。すべてのデバイス（デバッガーを含む）はリクエスト開始にネットワークアドレスの割り当てが必要です。\n\nスタンダードモードで40日目まで生存したプレイヤー、または本格的な問題解決を楽しむプレイヤーに最適。")
t("Zen mode is identical to standard mode except floors will not be automatically built. Explore the game at your own pace.\n\nSuitable for players that want to enjoy the game without the constant stress of time.",
  "禅モードはスタンダードモードと同じですが、フロアが自動的に建設されません。自分のペースでゲームを探索できます。\n\n時間の常なるストレスなくゲームを楽しみたいプレイヤーに最適。")

# Loading tips (variants)
t("To debug/configure a target device, the [color=yellow]debugger[/color] you're using [color=yellow]netsh[/color] from must be able to reach the target with traffic type [color=palegreen]tcp/23[/color].",
  "ターゲットデバイスをデバッグ/設定するには、[color=yellow]netsh[/color]を使用している[color=yellow]デバッガー[/color]がトラフィックタイプ [color=palegreen]tcp/23[/color] でターゲットに到達できる必要があります。")
t("The [color=yellow]alias[/color] command allows you to create terminal \"shortcuts\". For example, [color=yellow]alias dnsup program install dns-lite[/color] allows just typing [color=yellow]dnsup on 123[/color] to install [color=lightsalmon]dns-lite[/color] on the server with address [color=00FA9A]123[/color]. \nPositional parameters are also supported (e.g., [color=yellow]alias mixup echo $3 $1 $2[/color], which allows [color=yellow]mixup a b c[/color] to become [color=yellow]echo c a b[/color].",
  "[color=yellow]alias[/color] コマンドでターミナルの「ショートカット」を作成できます。例えば、[color=yellow]alias dnsup program install dns-lite[/color] と設定すると、[color=yellow]dnsup on 123[/color] と入力するだけでアドレス [color=00FA9A]123[/color] のサーバーに [color=lightsalmon]dns-lite[/color] をインストールできます。\n位置パラメータもサポートされています（例：[color=yellow]alias mixup echo $3 $1 $2[/color] と設定すると、[color=yellow]mixup a b c[/color] が [color=yellow]echo c a b[/color] になります）。")
t("The cron routine allows scheduled command execution. It is unlocked through the \"[color=deepskyblue]NetOps Research[/color]\" proposal.",
  "cronルーチンでコマンドのスケジュール実行が可能です。「[color=deepskyblue]NetOps Research[/color]」提案でアンロックされます。")
t("A server can only function as a DNS server is it has \"[color=lightsalmon]reply-dns-queries[/color]\" uses on it. If a device/user \"[color=red]cannot reach a DNS server[/color]\", it could mean that there is no network connection (physical or otherwise) to the server [color=yellow]OR[/color] it does not have sufficient uses on the stack. Use the [color=yellow]dstat[/color] or [color=yellow]watch[/color] routine to help with troubleshooting.",
  "サーバーがDNSサーバーとして機能するには「[color=lightsalmon]reply-dns-queries[/color]」USEが必要です。デバイス/ユーザーが「[color=red]DNSサーバーに到達できない[/color]」場合、サーバーへのネットワーク接続（物理的またはその他）がない[color=yellow]か[/color]、スタックに十分なUSEがないことを意味します。[color=yellow]dstat[/color] または [color=yellow]watch[/color] ルーチンでトラブルシューティングしてください。")
t("You may set multiple designated DNS servers for a device/client by doing [color=yellow]net dns set @dns1 @dns2 on @target[/color].",
  "[color=yellow]net dns set @dns1 @dns2 on @target[/color] でデバイス/クライアントに複数のDNSサーバーを指定できます。")
t("Network switches are easy to use as it does not need any configuration. However, they have limited bandwidth.",
  "ネットワークスイッチは設定不要で簡単に使えますが、帯域幅に制限があります。")
t("Routers performs longest [color=yellow]prefix[/color] matching for network address. [color=yellow]@net1/ via port1[/color] will route both [color=FF0565]@net1/srv[/color] and [color=FF0565]@net1/dns[/color] to [color=7FFFD4]port 1[/color].",
  "ルーターはネットワークアドレスの最長[color=yellow]プレフィックス[/color]マッチングを実行します。[color=yellow]@net1/ via port1[/color] は [color=FF0565]@net1/srv[/color] と [color=FF0565]@net1/dns[/color] の両方を [color=7FFFD4]port 1[/color] にルーティングします。")
t("All users will periodically do a DHCP request broadcast. Use a [color=yellow]DHCP server[/color] to auto-configure a large number of users/devices.",
  "すべてのユーザーは定期的にDHCPリクエストをブロードキャストします。[color=yellow]DHCPサーバー[/color]を使用して大量のユーザー/デバイスを自動設定できます。")
t("You can run more processes on a server than its installed CPU at a reduced performance. \nYou cannot do the same if memory is exceeded.",
  "サーバーのインストール済みCPU以上のプロセスを性能低下で実行できます。\nメモリが超過した場合は同じことはできません。")
t("Firewall rules on network addresses are based on prefixes. [color=yellow]deny tcp/22 from @net1[/color] blocks [color=palegreen]tcp/22[/color] from [color=FF0565]@net1-srv[/color] and [color=FF0565]@net1-dns[/color].",
  "ネットワークアドレスのファイアウォールルールはプレフィックスベースです。[color=yellow]deny tcp/22 from @net1[/color] は [color=FF0565]@net1-srv[/color] と [color=FF0565]@net1-dns[/color] からの [color=palegreen]tcp/22[/color] をブロックします。")
t("Becareful when setting firewall rules, as you may get [color=yellow]locked out[/color] with no way to configure it unless you factory reset it.",
  "ファイアウォールルール設定時は注意してください。工場出荷時リセット以外に設定する方法がない[color=yellow]ロックアウト[/color]が発生する可能性があります。")
t("You can host your own services for additional income using [color=yellow]The Registry[/color] application. Becareful to not over-compete with your enterprise clients as that may reduce their satiety.",
  "[color=yellow]The Registry[/color] アプリケーションで独自のサービスをホストして追加収入を得られます。エンタープライズクライアントと過度に競合しないよう注意してください。満足度が低下する可能性があります。")
t("Users will pay at the end of the day based on their lowest satiety level or usage fulfilment.",
  "ユーザーは一日の最低満足度または利用達成度に基づいて日末に支払いを行います。")
t("Certain users may have [color=red]malicious behaviors[/color] that are not shown on the Surveyor application. These malicious behaviors can affect the health of the network and have [color=red]negative satiety impact towards other users[/color].",
  "特定のユーザーにはSurveyorアプリに表示されない[color=red]悪意ある行動[/color]がある場合があります。これらの悪意ある行動はネットワークの健全性に影響を与え、[color=red]他のユーザーの満足度に悪影響[/color]を及ぼします。")
t("Press and hold the \"T\" key while dragging the mouse around allows you to use the tape measurement.",
  "\"T\"キーを押しながらマウスをドラッグするとテープ計測を使用できます。")
t("Double clicking and holding the left-mouse button allows you to hold multiple cables at once.",
  "左マウスボタンをダブルクリック＆ホールドで複数のケーブルを同時に保持できます。")
t("There are 3 methods of motion. You can [color=yellow]pan with WASD[/color], dragging the mouse while [color=yellow]holding right-click[/color] or moving the mouse while [color=yellow]holding left-shift OR the middle mouse button[/color]. You can also scroll in/out with the mouse wheel.",
  "移動方法は3つあります。[color=yellow]WASDでパン[/color]、[color=yellow]右クリックを押しながら[/color]マウスドラッグ、または[color=yellow]左Shiftまたはミドルマウスボタンを押しながら[/color]マウス移動。スクロールホイールでズームイン/アウトもできます。")
t("Proposals can be submitted to the Secretariat to unlock new advantages. The pool of available proposals is [color=yellow]re-drafted periodically[/color], with the [color=yellow]option of locking one[/color] of the proposals to prevent it from being re-shuffled.",
  "事務局に提案を提出して新しい利点をアンロックできます。利用可能な提案プールは[color=yellow]定期的に再作成[/color]され、提案の1つを[color=yellow]ロック[/color]して再シャッフルを防止できます。")
t("The sftp routine allows remote backup of device configuration and programs. It is unlocked through the \"[color=deepskyblue]Remote Backups[/color]\" proposal.",
  "sftpルーチンでデバイス設定とプログラムのリモートバックアップが可能です。「[color=deepskyblue]Remote Backups[/color]」提案でアンロックされます。")
t("The rip routine allows automated route discoveries between routers. It is unlocked through the \"[color=deepskyblue]Route Discovery Protocol v1[/color]\" proposal.",
  "ripルーチンでルーター間の自動ルート検出が可能です。「[color=deepskyblue]Route Discovery Protocol v1[/color]」提案でアンロックされます。")
t("Buying [color=yellow]cables in bulk[/color] will cause them to come in a box.",
  "[color=yellow]ケーブルをまとめ買い[/color]すると箱で届きます。")
t("As your network grows large, hardware replacements due to malfunction becomes difficult. Use the [color=yellow]memento[/color] app to mark devices for automatic replacement. The service costs a [color=yellow]daily fee per device[/color] and [color=yellow]charges twice as much for the replacement[/color]. All configuration and data on the replaced device will also be gone, so be sure to keep a backup!",
  "ネットワークが大きくなると、故障によるハードウェア交換が困難になります。[color=yellow]memento[/color]アプリでデバイスを自動交換対象にマークできます。サービスには[color=yellow]デバイスごとの日額[/color]がかかり、[color=yellow]交換時には2倍のコスト[/color]がかかります。交換されたデバイスのすべての設定とデータも失われるため、バックアップを取っておいてください！")
t("Network worms may spread (with early warnings) throughout your network and infect devices. Use firewalls to filter out their traffic and contain the spread.",
  "ネットワークワームが（事前警告付きで）ネットワーク全体に拡散しデバイスに感染する可能性があります。ファイアウォールでトラフィックをフィルタリングし拡散を封じ込めましょう。")
t("User traffic tapping/analysis is key to keep a botnet up and running at all times.",
  "ボットネットを常時稼働させるには、ユーザートラフィックのタップ/分析が鍵です。")

# Announcements / early access
t("Greetings from Pocosia Studios!\n\nThanks for supporting our game. We are a small team of 2 working on this project.\n\n[color=yellow]This is the early-access build of the game[/color]. There will be bugs and incomplete features as we are still actively developing the game. We will be treating the early-access as test-beds and avenues for feedback. Check out our discord and steam community for the feature road map.\n\n[color=yellow]Feel free to share your thoughts and feedback throughout your gameplay by hitting F8[/color]. Your feedback helps us make the game fun, and we truly hope you have a great time with our game!\n\nThis version has an [color=yellow]endless survival mode[/color] which serves as the main scenario for the game.\n\n[color=palegreen]PS: Special thanks to all players whom have provided feedback; we are working to incorporate your suggestions into the game.[/color]\n\n[color=FFA07A]Rules for public streaming/video - please add credits to Karl Casey @ White Bat Audio for the awesome music.[/color]",
  "Pocosia Studiosからのご挨拶！\n\nゲームを応援いただきありがとうございます。2人の小さなチームでこのプロジェクトに取り組んでいます。\n\n[color=yellow]これはゲームの早期アクセスビルドです[/color]。まだ開発中のため、バグや未完成の機能があります。早期アクセスをテスト環境とフィードバックの場として活用します。DiscordとSteamコミュニティで機能ロードマップをご確認ください。\n\n[color=yellow]F8キーでいつでもフィードバックや感想を共有してください[/color]。皆様のフィードバックがゲームをより楽しくし、ゲームを楽しんでいただけることを願っています！\n\nこのバージョンにはゲームのメインシナリオとなる[color=yellow]エンドレスサバイバルモード[/color]があります。\n\n[color=palegreen]PS: フィードバックを提供してくださったすべてのプレイヤーに感謝します。皆様のご提案をゲームに反映する作業を進めています。[/color]\n\n[color=FFA07A]配信/動画のルール - 素晴らしい音楽のクレジットとしてKarl Casey @ White Bat Audioを記載してください。[/color]")

# Game settings variants
t("Maximum number of days allowed to be in debt before losing the run.",
  "ゲームオーバーになるまでの借金可能日数。")
t("If enterprise users will automatically create DNS mapping. Only applicable for non DNS local mapping.",
  "エンタープライズユーザーが自動的にDNSマッピングを作成するか。非DNSローカルマッピングでのみ適用。")
t("If network errors are visible with naked eye (i.e., Overload texts).",
  "ネットワークエラーが目視で確認できるか（例：過負荷テキスト）。")
t("If enabled, device never gets overloaded due to network bandwidth issues.",
  "有効にすると、ネットワーク帯域幅の問題によるデバイスの過負荷がなくなります。")
t("The likelihood of devices to malfunction if exceeded their warranty period and have reliability <= 1%.",
  "保証期間超過で信頼性が1%以下の場合のデバイス故障確率。")
t("The likelihood of users resetting their hardware if they go offline.",
  "ユーザーがオフラインになった場合にハードウェアをリセットする確率。")
t("Longer periods means more time before a floor is automatically built. Zero for infinite time.",
  "期間が長いほどフロアが自動建設されるまでの時間が長くなります。0で無限。")
t("Affects how much time can pass between a SLA warning and the breach.",
  "SLA警告から違反までの時間に影響します。")
t("The longer the warranty period, the longer the device stays operational.",
  "保証期間が長いほど、デバイスが稼働し続ける期間も長くなります。")
t("Early access release: Game is in active development, hit f8 to share feedback and report bugs.",
  "早期アクセス: ゲームは開発中です。F8でフィードバック共有とバグ報告ができます。")
t("If time speed-up/slow-down controls in game will affect physics. Setting this to \"yes\" disable time control in co-op.",
  "ゲーム内の時間加速/減速操作が物理に影響するか。「はい」に設定するとCo-opで時間操作が無効になります。")

# ============================================================
# Now let's parse and process the PO file

# ============================================================
# BATCH 9: Wiki / Help articles
# ============================================================

# Wiki: Surveyor / Satiety
t("The [color=skyblue][url]debugger[/url][/color] (specified with \"[color=yellow]using[/color]\" keyword) must be able to [color=skyblue][url]reach[/url][/color] the [color=magenta]target[/color] in order to use this command. Alternatively, the [color=skyblue][url]always routine[/url][/color] can be used to automatically [i]always[/i] specify a default debugger, which allows the ommision of the [color=yellow]using[/color] [color=magenta]<debugger_addr>[/color] part seen in most commands. Additionally, the \"[color=yellow]using[/color]\" keyword accepts both [color=skyblue][url]hardware address[/url][/color] and [color=skyblue][url]network address[/url][/color].",
  "[color=skyblue][url]デバッガー[/url][/color]（「[color=yellow]using[/color]」キーワードで指定）がこのコマンドを使用するには、[color=magenta]ターゲット[/color]に[color=skyblue][url]到達[/url][/color]できる必要があります。また、[color=skyblue][url]alwaysルーチン[/url][/color]を使用してデフォルトのデバッガーを自動的に[i]常に[/i]指定でき、ほとんどのコマンドに見られる [color=yellow]using[/color] [color=magenta]<debugger_addr>[/color] 部分を省略できます。さらに、「[color=yellow]using[/color]」キーワードは[color=skyblue][url]ハードウェアアドレス[/url][/color]と[color=skyblue][url]ネットワークアドレス[/url][/color]の両方を受け付けます。")

t("Every user has a [color=yellow]satiety level[/color] (displayed as a percentage) that indicates their satisfaction with the network services.\n\nThe figure on the left shows a surveyor view of end-users on floor number 0 their respective satiety levels.\n\nA [color=red]red satiety level[/color] (i.e., the satiety level of the [color=yellow]end-user[/color] \"[color=orange]firsthand-coyote[/color]\") indicates that the user's [color=yellow]Satisfaction level agreement[/color] or [color=yellow]SLA[/color] is not met.",
  "すべてのユーザーにはネットワークサービスへの満足度を示す[color=yellow]満足度レベル[/color]（パーセンテージで表示）があります。\n\n左の図はフロア0のエンドユーザーとそれぞれの満足度レベルのSurveyorビューを示しています。\n\n[color=red]赤い満足度レベル[/color]（つまり[color=yellow]エンドユーザー[/color]「[color=orange]firsthand-coyote[/color]」の満足度レベル）はユーザーの[color=yellow]満足度レベル契約[/color]（[color=yellow]SLA[/color]）が満たされていないことを示します。")

t("SLA is the minimum satiety that the user can tolerate. If a user's satiety goes below their SLA, a count-down timer starts before they file a complaint to the tower's board, which will trigger a [color=skyblue][url]game-over[/url][/color].\n\nDifferent [color=skyblue][url]user types[/url][/color] may have different SLAs. A more important user (e.g., a company) may have higher SLA requirement than a less important one. For example, the user \"[color=orange]firsthand-coyote[/color]\" is of type \"[color=orange]WireSync News[/color]\", which is a producer and thus have a higher SLA requirement.",
  "SLAはユーザーが許容できる最低満足度です。ユーザーの満足度がSLA以下になると、タワーの理事会に苦情を提出するまでのカウントダウンタイマーが開始され、[color=skyblue][url]ゲームオーバー[/url][/color]がトリガーされます。\n\n異なる[color=skyblue][url]ユーザータイプ[/url][/color]は異なるSLAを持つことがあります。より重要なユーザー（企業など）はそうでないユーザーよりも高いSLA要件を持つ場合があります。例えば、ユーザー「[color=orange]firsthand-coyote[/color]」はタイプ「[color=orange]WireSync News[/color]」で、プロデューサーのためSLA要件が高くなっています。")

t("Details for every user can be viewed by clicking on the icon to the right of the satiety percentages.\n\nThe following are the concepts and meaning of the fields shown in the detailed view\n\n[color=yellow][i]Issues and Complaints[/i][/color]: The problems that are currently faced by the user. These messages serve as guides when trying to increase user satiety levels.\n\n[color=yellow][i]grace days left[/i][/color]: The number of days before their SLA becomes effective. A user with satiety below their SLA and an expired grace period (i.e., grace days left = 0) will trigger game-over events.\n\n[color=yellow][i]SLA[/i][/color]: This is the minimum satiety levels required by the user.\n\n[color=yellow][i]Floor[/i][/color]: The floor number in which this user is physically located.\n\n[color=yellow][i]Satiety[/i][/color]: The satiety level of the user at this moment.\n\n[color=yellow][i]Lowest satiety today[/i][/color]: The lowest satiety level of the user for the current day.\n\n[color=yellow][i]Payment due today[/i][/color]: The income to receive from this user at the end of day. The amount is [color=orange]proportional to the lowest satiety they experience for the day[/color]. Therefore, you ought to keep your users satisfied [color=orange]throughout the day[/color] to ensure a profit can be made.\n\n[color=yellow][i]Networking details[/i][/color]: In addition, the network information of the user such as their [color=skyblue][url]hardware address[/url][/color], [color=skyblue][url]network address[/url][/color] and [color=skyblue][url]bandwidth[/url][/color] consumption is listed.\n\n[color=yellow][i]Behaviour insights[/i][/color]: The [color=skyblue][url]behavior[/url][/color] list of the user. Each of these behavior contributes towards satiety gain/loss, proportional to the importance of the behavior.\n",
  "各ユーザーの詳細は満足度パーセンテージの右にあるアイコンをクリックして確認できます。\n\n以下は詳細ビューに表示されるフィールドの概念と意味です\n\n[color=yellow][i]問題と苦情[/i][/color]: ユーザーが現在直面している問題。これらのメッセージはユーザーの満足度を上げるためのガイドとして機能します。\n\n[color=yellow][i]猶予日数[/i][/color]: SLAが有効になるまでの日数。満足度がSLA以下で猶予期間が切れた（猶予日数 = 0）ユーザーはゲームオーバーイベントをトリガーします。\n\n[color=yellow][i]SLA[/i][/color]: ユーザーが要求する最低満足度レベル。\n\n[color=yellow][i]フロア[/i][/color]: ユーザーが物理的に位置するフロア番号。\n\n[color=yellow][i]満足度[/i][/color]: 現時点でのユーザーの満足度レベル。\n\n[color=yellow][i]本日の最低満足度[/i][/color]: 今日のユーザーの最低満足度レベル。\n\n[color=yellow][i]本日の支払い[/i][/color]: 日末にこのユーザーから受け取る収入。金額は[color=orange]その日に経験した最低満足度に比例[/color]します。そのため、利益を確保するには[color=orange]一日を通して[/color]ユーザーを満足させ続ける必要があります。\n\n[color=yellow][i]ネットワーク詳細[/i][/color]: さらに、[color=skyblue][url]ハードウェアアドレス[/url][/color]、[color=skyblue][url]ネットワークアドレス[/url][/color]、[color=skyblue][url]帯域幅[/url][/color]消費などのユーザーのネットワーク情報が表示されます。\n\n[color=yellow][i]行動分析[/i][/color]: ユーザーの[color=skyblue][url]行動[/url][/color]リスト。各行動は行動の重要度に比例して満足度の上昇/低下に寄与します。\n")

t("When a user's grace period is over and their satiety falls below the SLA, a [color=red]red notice timer[/color] will appear in their detailed panel along with an email notification.\n\n",
  "ユーザーの猶予期間が終了し満足度がSLA以下になると、詳細パネルに[color=red]赤い通知タイマー[/color]がメール通知とともに表示されます。\n\n")

t("A SLA breach will happen if their satiety is not brought to the required SLA. [color=yellow]ANY SLA breach[/color] will result in a game-over.\n\nFor example, if \"[color=orange]firsthand-coyote[/color]\" satiety is not brought back up to [color=orange]20.0%[/color] in 105 seconds, then the [color=skyblue][url]game will be over[/url][/color].",
  "満足度を必要なSLAまで回復しないとSLA違反が発生します。[color=yellow]いかなるSLA違反も[/color]ゲームオーバーとなります。\n\n例えば、「[color=orange]firsthand-coyote[/color]」の満足度を105秒以内に [color=orange]20.0%[/color] まで回復しないと、[color=skyblue][url]ゲームオーバー[/url][/color]になります。")

# Wiki: DHCP
t("DHCP", "DHCP")
t("configure hosts en-masse", "ホストを一括設定")
t("Dynamic Host Configuration Protocol (DHCP)", "動的ホスト構成プロトコル（DHCP）")
t("In Tower Networking Inc., [color=yellow] DHCP[/color] or dynamic host configuration protocol can be used to assign [color=skyblue][url]network addresses[/url][/color] and [color=skyblue][url]designated DNS server address[/url][/color] automatically.\n\nUse of DHCP allows the player to configure devices en-masse.\n\n",
  "Tower Networking Inc.では、[color=yellow]DHCP[/color]（動的ホスト構成プロトコル）を使用して[color=skyblue][url]ネットワークアドレス[/url][/color]と[color=skyblue][url]指定DNSサーバーアドレス[/url][/color]を自動的に割り当てることができます。\n\nDHCPを使用することで、プレイヤーはデバイスを一括設定できます。\n\n")
t("Running a DHCP Server", "DHCPサーバーの実行")
t("A [color=skyblue][url]device[/url][/color] is able to function as a DHCP server if it has the \"[color=lightsalmon][reply-dhcp-request][/color]\" [color=skyblue][url]use[/url][/color] in its [color=yellow]USE STACK[/color]. This can be achieved by running [color=skyblue][url]programs[/url][/color] such as \"[color=orange]kea[/color]\".\n\nThe device should also have enough bandwidth capacity to handle the DHCP requests.\n\n",
  "[color=skyblue][url]デバイス[/url][/color]は[color=yellow]USEスタック[/color]に「[color=lightsalmon][reply-dhcp-request][/color]」[color=skyblue][url]USE[/url][/color]があればDHCPサーバーとして機能できます。これは「[color=orange]kea[/color]」などの[color=skyblue][url]プログラム[/url][/color]を実行することで達成できます。\n\nデバイスにはDHCPリクエストを処理するのに十分な帯域幅容量も必要です。\n\n")
t("A DHCP server will attempt to apply [color=yellow]DHCP options[/color] to clients that are performing DHCP requests. Unlike DNS entries, DHCP options are [color=yellow]not global[/color], which allows for per-network setups.",
  "DHCPサーバーはDHCPリクエストを実行しているクライアントに[color=yellow]DHCPオプション[/color]を適用しようとします。DNSエントリとは異なり、DHCPオプションは[color=yellow]グローバルではない[/color]ため、ネットワーク単位の設定が可能です。")
t("DHCP Requests", "DHCPリクエスト")
t("Every network-capable device/user has the ability to perform [color=yellow]dhcp requests[/color]. A DHCP request will attempt to reach a DHCP server in order to obtain and apply network configuration. \n\n",
  "すべてのネットワーク対応デバイス/ユーザーは[color=yellow]DHCPリクエスト[/color]を実行する能力があります。DHCPリクエストはネットワーク設定を取得・適用するためにDHCPサーバーへの到達を試みます。\n\n")
t("In the examples shown above, notice the following:\n\n1. The [color=skyblue][url]designated DNS server[/url][/color] of the clients who successfully [color=skyblue][url]reached[/url][/color] the DHCP server and consumed a use from are set to the same as the [color=yellow]DNS option[/color] on the DHCP server. Similarly, their [color=skyblue][url]network address[/url][/color] are assigned with the same prefix as the [color=yellow]Prefix option[/color].\n2. [s]The client on the other side of the router (i.e., [color=orange]CHARLIE[/color]) is unable to reach the DHCP server. [color=yellow]DHCP requests do not travel across routers[/color][/s]. (This quirky limitation has been removed to allow for more player freedom in version 0.7.11). DHCP [color=skyblue][url]broadcast requests[/url][/color] can now traverses through router if the router is configured to forward broadcasts traffic.\n\n[color=skyblue][url]Users[/url][/color] will use DHCP by default, while [color=skyblue][url]devices[/url][/color] that you own do not use DHCP unless configured to do so.  DHCP can be set to [color=yellow]boot-only[/color], [color=yellow]periodic[/color] and [color=yellow]disabled[/color] using the [color=skyblue][url]net[/url][/color] routine. [s]Whether a device has DHCP enabled or not can be viewed using the command \"[color=yellow]net show on [color=magenta]<addr_of_the_device_or_user>[/color][/color]\", which is displayed on the [color=yellow]dhcp enabled[/color] line.[/s] (DHCP now has 3 modes in the version 0.8.24).\n\n[color=yellow]on-boot only[/color]: Device only performs a single DHCP requests on boot.\n[color=green]periodic[/color]: Device regularly performs DHCP requests.\n[color=red]disabled[/color]: Device never performs DHCP requests.\n\n",
  "上記の例で以下に注目してください：\n\n1. DHCPサーバーに正常に[color=skyblue][url]到達[/url][/color]しUSEを消費したクライアントの[color=skyblue][url]指定DNSサーバー[/url][/color]はDHCPサーバーの[color=yellow]DNSオプション[/color]と同じに設定されます。同様に、[color=skyblue][url]ネットワークアドレス[/url][/color]は[color=yellow]プレフィックスオプション[/color]と同じプレフィックスで割り当てられます。\n2. [s]ルーターの反対側のクライアント（つまり[color=orange]CHARLIE[/color]）はDHCPサーバーに到達できません。[color=yellow]DHCPリクエストはルーターを越えません[/color][/s]。（この制限はバージョン0.7.11でプレイヤーの自由度向上のために削除されました）。ルーターがブロードキャストトラフィックの転送に設定されている場合、DHCP[color=skyblue][url]ブロードキャストリクエスト[/url][/color]はルーターを通過できるようになりました。\n\n[color=skyblue][url]ユーザー[/url][/color]はデフォルトでDHCPを使用しますが、所有する[color=skyblue][url]デバイス[/url][/color]は設定しない限りDHCPを使用しません。DHCPは[color=skyblue][url]net[/url][/color]ルーチンで[color=yellow]boot-only[/color]、[color=yellow]periodic[/color]、[color=yellow]disabled[/color]に設定できます。[s]デバイスのDHCPが有効かどうかは「[color=yellow]net show on [color=magenta]<デバイスまたはユーザーのアドレス>[/color][/color]」コマンドの[color=yellow]dhcp enabled[/color]行で確認できます。[/s]（バージョン0.8.24でDHCPに3つのモードが追加されました）。\n\n[color=yellow]on-boot only[/color]: デバイスは起動時にのみDHCPリクエストを実行。\n[color=green]periodic[/color]: デバイスは定期的にDHCPリクエストを実行。\n[color=red]disabled[/color]: デバイスはDHCPリクエストを実行しない。\n\n")

t("\nWhen DHCP is enabled, the device/user [color=yellow]automatically sends DHCP [i]approximately[/i] every 10 seconds[/color]. This means if you want to update the [color=skyblue][url]network address[/url][/color] prefixes or the DNS server address, you just have to update the DHCP options using the [color=skyblue][url]dhcp routine[/url][/color].\n\nAdditionally, you can also force a device/user to perform a DHCP request immediately with the [color=skyblue][url]net routine[/url][/color]. This allows you to immediately test the DHCP setup without waiting.",
  "\nDHCPが有効な場合、デバイス/ユーザーは[color=yellow]約10秒ごとにDHCPを自動送信[/color]します。つまり、[color=skyblue][url]ネットワークアドレス[/url][/color]のプレフィックスやDNSサーバーアドレスを更新したい場合は、[color=skyblue][url]dhcpルーチン[/url][/color]でDHCPオプションを更新するだけです。\n\nさらに、[color=skyblue][url]netルーチン[/url][/color]でデバイス/ユーザーにDHCPリクエストを即座に実行させることもできます。これにより、待たずにDHCPセットアップをすぐにテストできます。")
t("DHCP Address Assignment", "DHCPアドレス割当")
t("When a DHCP request is fulfilled, the DHCP server will check if the prefix of the network address of the requestor matches its [color=yellow]prefix option[/color]. If it is not a match, [color=yellow]a new network address is assigned to the requestor[/color].\n\nThe new network address is composed from the prefix and [color=yellow]4 randomly chosen alphabets[/color]. The [color=yellow]DHCP server ensures no address collision with other assigned network addresses[/color] before assigning the new address.\n\nTherefore, the maximum length of the prefix option is [color=yellow]5 characters long[/color].",
  "DHCPリクエストが処理されると、DHCPサーバーは要求者のネットワークアドレスのプレフィックスが[color=yellow]プレフィックスオプション[/color]と一致するか確認します。一致しない場合、[color=yellow]新しいネットワークアドレスが要求者に割り当てられます[/color]。\n\n新しいネットワークアドレスはプレフィックスと[color=yellow]ランダムに選ばれた4文字のアルファベット[/color]で構成されます。[color=yellow]DHCPサーバーは新しいアドレスを割り当てる前に他の割り当て済みネットワークアドレスとの衝突がないことを確認[/color]します。\n\nそのため、プレフィックスオプションの最大長は[color=yellow]5文字[/color]です。")

# Wiki: DNS
t("Domain Name System", "ドメインネームシステム")
t("Mapping domain names to addresses.", "ドメイン名をアドレスにマッピング。")
t("Domain Name System (DNS)", "ドメインネームシステム（DNS）")
t("The [color=yellow]domain name system[/color] or simply [color=yellow]DNS[/color] is an important element to any network. It provides a mapping between a [color=skyblue][url]domain name[/url][/color] to a [color=skyblue][url]network address[/url][/color] or a [color=skyblue][url]hardware address[/url][/color]. The act of turning a domain name into an address is called [color=yellow]DNS resolution[/color] or [color=yellow]DNS lookup[/color], while the mapping between a domain name and an address is called a [color=yellow]DNS entry[/color] or a [color=yellow]DNS mapping[/color].\n\nFor example, consider a domain name \"[color=orange]abc.com[/color]\" and a DNS entry \"[color=orange]abc.com \u2192 12345[/color]\". A DNS lookup of abc.com would result in [color=orange]12345[/color].\n\nDNS resolution traversals has the traffic class \"[color=orange]udp/53[/color]\".",
  "[color=yellow]ドメインネームシステム[/color]または単に[color=yellow]DNS[/color]はあらゆるネットワークの重要な要素です。[color=skyblue][url]ドメイン名[/url][/color]から[color=skyblue][url]ネットワークアドレス[/url][/color]または[color=skyblue][url]ハードウェアアドレス[/url][/color]へのマッピングを提供します。ドメイン名をアドレスに変換する行為を[color=yellow]DNS解決[/color]または[color=yellow]DNSルックアップ[/color]と呼び、ドメイン名とアドレス間のマッピングを[color=yellow]DNSエントリ[/color]または[color=yellow]DNSマッピング[/color]と呼びます。\n\n例えば、ドメイン名「[color=orange]abc.com[/color]」とDNSエントリ「[color=orange]abc.com → 12345[/color]」を考えます。abc.comのDNSルックアップ結果は [color=orange]12345[/color] になります。\n\nDNS解決トラバーサルのトラフィッククラスは「[color=orange]udp/53[/color]」です。")
t("Running a DNS server", "DNSサーバーの実行")
t("A [color=skyblue][url]device[/url][/color] is able to function as a DNS server if it has the \"[color=lightsalmon][reply-dns-queries][/color]\" [color=skyblue][url]use[/url][/color] in its [color=yellow]USE STACK[/color]. This can be achieved by running [color=skyblue][url]programs[/url][/color] such as \"[color=orange]dns-lite[/color]\" or \"[color=orange]dns-server[/color]\".\n\nThe device should also have enough bandwidth capacity to handle DNS resolution traffic.\n\n",
  "[color=skyblue][url]デバイス[/url][/color]は[color=yellow]USEスタック[/color]に「[color=lightsalmon][reply-dns-queries][/color]」[color=skyblue][url]USE[/url][/color]があればDNSサーバーとして機能できます。これは「[color=orange]dns-lite[/color]」や「[color=orange]dns-server[/color]」などの[color=skyblue][url]プログラム[/url][/color]を実行することで達成できます。\n\nデバイスにはDNS解決トラフィックを処理するのに十分な帯域幅容量も必要です。\n\n")
t("Using the netsh \"[color=skyblue][url]dns routine[/url][/color]\", a DNS mapping  can be created (input \"[color=orange]man dns[/color]\" for more help).\n\nIn standard mode, [color=yellow]DNS entries[/color] are global. This means if the entry exists, any DNS server will be able to resolve it. Likewise, it also means as long as the debugger running the command can reach a DNS server, the mapping creation will be successful.\n\nThe picture below shows an example of creating a DNS mapping for \"[color=orange]foobar.com[/color]\" which maps to the [color=skyblue][url]hardware address[/url][/color] \"[color=orange]12345[/color]\".",
  "netshの「[color=skyblue][url]dnsルーチン[/url][/color]」でDNSマッピングを作成できます（「[color=orange]man dns[/color]」でヘルプを表示）。\n\nスタンダードモードでは、[color=yellow]DNSエントリ[/color]はグローバルです。つまりエントリが存在すれば、どのDNSサーバーでも解決できます。同様に、コマンドを実行するデバッガーがDNSサーバーに到達できればマッピングの作成は成功します。\n\n下の図は「[color=orange]foobar.com[/color]」を[color=skyblue][url]ハードウェアアドレス[/url][/color]「[color=orange]12345[/color]」にマッピングするDNSマッピング作成の例です。")
t("DNS Resolution/Lookup", "DNS解決/ルックアップ")
t("To resolve a domain name:\n\n1. The device/user must be able to reach any DNS servers that has the \"[color=orange]reply-dns-queries[/color]\" use left in its stack.\n2. A DNS entry for the desired [color=skyblue][url]domain name[/url][/color] must exists.\n\n",
  "ドメイン名を解決するには：\n\n1. デバイス/ユーザーがスタックに「[color=orange]reply-dns-queries[/color]」USEが残っているDNSサーバーに到達できること。\n2. 目的の[color=skyblue][url]ドメイン名[/url][/color]のDNSエントリが存在すること。\n\n")
t("The pictures on the right shows issues with DNS resolution. \n\nIn the first picture, the debugger is unable to reach the DNS server.\n\nIn the second picture, the DNS entry for '[color=orange]nosuchthing.com[/color]' does not exists.\n\n",
  "右の図はDNS解決の問題を示しています。\n\n最初の図では、デバッガーがDNSサーバーに到達できません。\n\n2番目の図では、「[color=orange]nosuchthing.com[/color]」のDNSエントリが存在しません。\n\n")
t("Consumer DNS Usage", "コンシューマーのDNS利用")
t("[color=skyblue][url]Consumers[/url][/color] relies on domain names to access services that are compatible with their use specification. The following is a typical consumption flow:\n\n1. Consumer chooses a compatible service/provider identified by a domain name.\n2. Consumer  attempts to reach [color=yellow]ANY[/color] DNS server to resolve the domain name to a [color=skyblue][url]logical address[/url][/color].\n3. Consumer attempts to connect to the logical address obtained in step 2.\n4. Consumer attempts to consume a compatible use from the destination.\n\n",
  "[color=skyblue][url]コンシューマー[/url][/color]はUSE仕様と互換性のあるサービスにアクセスするためにドメイン名を利用します。以下は一般的な消費フローです：\n\n1. コンシューマーがドメイン名で識別される互換サービス/プロバイダーを選択。\n2. コンシューマーが[color=yellow]任意の[/color]DNSサーバーに到達を試みてドメイン名を[color=skyblue][url]論理アドレス[/url][/color]に解決。\n3. コンシューマーがステップ2で取得した論理アドレスへの接続を試行。\n4. コンシューマーが宛先から互換USEの消費を試行。\n\n")
t("\nThis means that [color=yellow]without a correct DNS setup, consumers are unable to consume at all![/color] There may be other issues affecting whether a consumer is able to use DNS successfully, such as:\n\n  - There is no route between the consumer and the DNS server (if connected using a router).\n  - There is a firewall policy blocking traffic class [color=orange]udp/53[/color] (if connected through a firewall).\n  - Any component between the consumer and the DNS server (or the DNS server itself) has [color=skyblue][url]exhausted its bandwidth[/url][/color] (e.g., overloaded switch).",
  "\nつまり、[color=yellow]正しいDNSセットアップがないと、コンシューマーは一切消費できません！[/color] コンシューマーがDNSを正常に利用できるかに影響する他の問題もあります：\n\n  - コンシューマーとDNSサーバー間にルートがない（ルーター経由の場合）。\n  - トラフィッククラス[color=orange]udp/53[/color]をブロックするファイアウォールポリシーがある（ファイアウォール経由の場合）。\n  - コンシューマーとDNSサーバー間のコンポーネント（またはDNSサーバー自体）が[color=skyblue][url]帯域幅を使い果たしている[/url][/color]（例：過負荷のスイッチ）。")
t("Advance DNS Configuration", "高度なDNS設定")
t("By default, all DNS resolution traffic is a broadcast. This means that if the traversal goes through a router, it will always take the default route. This is shown when you hover your mouse over a device/user (or use the [color=skyblue][url]net[/url][/color] routine) by indicating the DNS server address as \"[color=gray]unassigned[/color]\".\n\nThere is an option to designate a DNS server address for devices using the [color=skyblue][url]net[/url][/color] routine. A designated DNS server means that when DNS resolution is performed on the device/end-user, it will attempt to reach the specified address to perform DNS resolution. [color=yellow]This allows setting a specific route for DNS traffic on a router[/color].\n\nDesignating a DNS server address is one of the ways to handle issues with [color=skyblue][url]DNS servers behind routers[/url][/color].\n",
  "デフォルトでは、すべてのDNS解決トラフィックはブロードキャストです。つまり、トラバーサルがルーターを通過する場合、常にデフォルトルートを使用します。これはデバイス/ユーザーにマウスオーバー（または[color=skyblue][url]net[/url][/color]ルーチンを使用）するとDNSサーバーアドレスが「[color=gray]unassigned[/color]」と表示されることで確認できます。\n\n[color=skyblue][url]net[/url][/color]ルーチンでデバイスにDNSサーバーアドレスを指定するオプションがあります。指定DNSサーバーとは、デバイス/エンドユーザーでDNS解決が実行される際に、指定されたアドレスにDNS解決のために到達を試みることを意味します。[color=yellow]これにより、ルーター上でDNSトラフィック用の特定ルートを設定できます[/color]。\n\nDNSサーバーアドレスの指定は、[color=skyblue][url]ルーター背後のDNSサーバー[/url][/color]の問題に対処する方法の1つです。\n")
t("Local DNS (Hard mode)", "ローカルDNS（ハードモード）")
t("On hard mode, DNS mappings are localized. This means different DNS servers respond to DNS queries differently based on their local DNS entries.\n\nDNS servers can form hierarchies through the [color=yellow]net dns set[/color] command. For example, in a setup with 2 DNS servers, server A and server B. Suppose server A is the root server (where all the entries first defined). If a user attempts to perform a lookup on server B, they would encounter a no DNS entries error because there are no mappings configured on server B.\n\nThere are 2 known method to solve this problem:\n\n1. Perform DNS mapping on server B. However, this is pretty tedious if there are more than 2 DNS servers.\n2. Assign a DNS server on server B using [color=yellow]net dns set <srv_A> on <srv_B>[/color]. This makes server B use server A as a source.\n\nIf a user/device attempts to lookup a domain on server B, server B will then attempt to lookup the domain on server A and cache the results. This makes it so that in the future, server B can respond to DNS queries even if no mapping were performed on it.",
  "ハードモードでは、DNSマッピングがローカライズされます。つまり、異なるDNSサーバーはローカルDNSエントリに基づいてDNSクエリに異なる応答をします。\n\nDNSサーバーは[color=yellow]net dns set[/color]コマンドで階層を形成できます。例えば、2つのDNSサーバー、サーバーAとサーバーBの構成を考えます。サーバーAがルートサーバー（すべてのエントリが最初に定義される場所）だとします。ユーザーがサーバーBでルックアップを試みると、サーバーBにマッピングが設定されていないためDNSエントリなしエラーが発生します。\n\nこの問題を解決する方法は2つあります：\n\n1. サーバーBでDNSマッピングを実行する。ただし、DNSサーバーが2つ以上ある場合はかなり面倒です。\n2. [color=yellow]net dns set <srv_A> on <srv_B>[/color]でサーバーBにDNSサーバーを割り当てる。これによりサーバーBがサーバーAをソースとして使用します。\n\nユーザー/デバイスがサーバーBでドメインルックアップを試みると、サーバーBはサーバーAでドメインルックアップを試み結果をキャッシュします。これにより、将来サーバーBはマッピングが実行されていなくてもDNSクエリに応答できるようになります。")

# Wiki: Domain Names
t("Domain Names", "ドメイン名")
t("Public network services", "パブリックネットワークサービス")
t("Domain Names and Services", "ドメイン名とサービス")
t("In Tower Networking Inc., A [color=yellow]service[/color] is represented by a [color=yellow]domain name[/color].\n\nA service can be seen as a [color=skyblue][url]use[/url][/color] provider. A service provides uses under a domain name. Usually, [color=skyblue][url]enterprise users[/url][/color] will provide services.\n\nThe following is a behavior insight from an enterprise user, which lists the services it provides along with their corresponding domain names.",
  "Tower Networking Inc.では、[color=yellow]サービス[/color]は[color=yellow]ドメイン名[/color]で表されます。\n\nサービスは[color=skyblue][url]USE[/url][/color]プロバイダーと見なすことができます。サービスはドメイン名の下でUSEを提供します。通常、[color=skyblue][url]エンタープライズユーザー[/url][/color]がサービスを提供します。\n\n以下はエンタープライズユーザーの行動分析で、提供するサービスと対応するドメイン名が一覧表示されています。")
t("\nTo use a service, a [color=skyblue][url]consumer[/url][/color] performs [color=skyblue][url]DNS lookup[/url][/color] of the domain names they wish to visit to get a destination [color=skyblue][url]logical address[/url][/color]. They then attempt to consume from the destination to satisfy their needs.",
  "\nサービスを利用するには、[color=skyblue][url]コンシューマー[/url][/color]が訪問したいドメイン名の[color=skyblue][url]DNSルックアップ[/url][/color]を実行して宛先の[color=skyblue][url]論理アドレス[/url][/color]を取得します。その後、ニーズを満たすために宛先からの消費を試みます。")
t("Hosting your own services", "独自サービスのホスティング")
t("It is possible that there are unfulfilled needs on the [color=skyblue][url]consumers[/url][/color]. This happens when there are no equivalent enterprise users which provides the service that can satisfy a particular need.\n\nWhen this happens, it will show up in the \"[i]Issues and Complaints[/i]\" section of the user's detailed view in the [color=skyblue][url]Surveyor[/url][/color] application. The example below shows that the user [color=orange]blond-shrimp[/color] cannot find any suitable services for their needs of \"[color=orange]talk to someone online[/color]\".\n",
  "[color=skyblue][url]コンシューマー[/url][/color]に満たされていないニーズがある場合があります。これは特定のニーズを満たすサービスを提供する同等のエンタープライズユーザーがいない場合に発生します。\n\nこの場合、[color=skyblue][url]Surveyor[/url][/color]アプリのユーザー詳細ビューの「[i]問題と苦情[/i]」セクションに表示されます。下の例ではユーザー[color=orange]blond-shrimp[/color]が「[color=orange]talk to someone online[/color]」のニーズに適したサービスが見つからないことを示しています。\n")
t("\nIn this case, it may be necessary to host your own service to fill the void. This can be done using [color=skyblue][url]the Registry[/url][/color] application.\n\nWhen you host your own services, a \"[color=yellow]pay per use[/color]\" fee may be charged to consumers. This means that whenever your service is chosen for consumption, and it is successfully visited and consumed, the consumer pays you a fee.",
  "\nこの場合、空白を埋めるために独自のサービスをホストする必要があるかもしれません。これは[color=skyblue][url]The Registry[/url][/color]アプリで行えます。\n\n独自サービスをホストする場合、コンシューマーに「[color=yellow]従量課金[/color]」料金を請求できます。つまり、サービスが消費のために選ばれ、正常に訪問・消費されるたびに、コンシューマーから料金が支払われます。")
t("\nWhile this may be a good way to boost your income, if you are hosting services that your enterprise users are also hosting, it means you are competing with them for users, which may lower their satiety.\n",
  "\nこれは収入を増やす良い方法かもしれませんが、エンタープライズユーザーもホストしているサービスをホストする場合、ユーザーを巡って競合することになり、満足度が低下する可能性があります。\n")

# Wiki: Elevator
t("Elevator", "エレベーター")
t("moving objects from one floor to another.", "フロア間でオブジェクトを移動する。")
t("Elevator System", "エレベーターシステム")
t("The [color=yellow]elevator[/color] is the only way to move between floors. The way it works is slightly different than how elevators work as you know it.\n\nElevators can be summoned to your current floor using the number pad panel beside the elevator. \n\nWhen an elevator arrives, [color=yellow]it will only travel to the floor you have originally summoned it for[/color]. \n\nNot only can the elevator be used to transport you (the player) to other floors, it can also be used to transport objects such as [color=skyblue][url]devices[/url][/color] and cables placed in the cargo area.",
  "[color=yellow]エレベーター[/color]はフロア間を移動する唯一の手段です。動作方法は一般的なエレベーターとは少し異なります。\n\nエレベーターはエレベーター横のテンキーパネルを使って現在のフロアに呼び出せます。\n\nエレベーターが到着すると、[color=yellow]最初に呼び出したフロアにのみ移動します[/color]。\n\nエレベーターはプレイヤーを他のフロアに移動するだけでなく、貨物エリアに置かれた[color=skyblue][url]デバイス[/url][/color]やケーブルなどのオブジェクトの輸送にも使えます。")
t("The [color=yellow]number pad[/color] on the elevator shaft door allows you to summon the elevator to your desired floor by clicking on the number button (See the picture on the right) of the panel. \n\nThe further your destination floor from your current floor, the longer it takes for the elevator to arrive.\n",
  "エレベーターシャフトドアの[color=yellow]テンキー[/color]でパネルの番号ボタン（右の図参照）をクリックして目的のフロアにエレベーターを呼び出せます。\n\n目的フロアが現在のフロアから遠いほど、エレベーターの到着に時間がかかります。\n")
t("The [color=yellow]panel[/color] on the elevator shaft door allows you to interact with the elevator when it has arrived.\n\nOnce the elevator arrives, by clicking on the \"ENTER ELEVATOR\" button (See the picture on the left), you and every object that is located in the cargo area will be transported to the destination floor.\n\nAlternatively, by clicking on the \"CARGO ONLY\" button, only the objects in the cargo area will be transported to the destination floor, and you will remain in the current floor.\n\nThe \"CARGO ONLY\" button is mostly useful in multiplayer sessions when you need to co-ordinate inventory management between floors.",
  "エレベーターシャフトドアの[color=yellow]パネル[/color]でエレベーター到着時に操作できます。\n\nエレベーター到着後、「ENTER ELEVATOR」ボタン（左の図参照）をクリックすると、あなたと貨物エリアにあるすべてのオブジェクトが目的フロアに輸送されます。\n\nまた、「CARGO ONLY」ボタンをクリックすると、貨物エリアのオブジェクトのみが目的フロアに輸送され、あなたは現在のフロアに留まります。\n\n「CARGO ONLY」ボタンはマルチプレイヤーセッションでフロア間の在庫管理を調整する際に特に役立ちます。")
t("The display panel found at the top of the elevator helps indicate how many objects are currently placed in the cargo area.\n\nEnsure that connected devices are not placed in the cargo area as to not cause a service disruption when you accidentally send them away!",
  "エレベーター上部のディスプレイパネルは、現在貨物エリアに配置されているオブジェクトの数を示します。\n\n接続されたデバイスが貨物エリアに配置されていないことを確認してください。誤って送ってしまうとサービス中断の原因になります！")

# Wiki: Enterprise Users
t("Enterprise Users", "エンタープライズユーザー")
t("the big fishes in the pond", "大口のお客様")
t("Enterprise End Users (Company Subscribers)", "エンタープライズエンドユーザー（企業加入者）")
t("[color=yellow]Enterprise users[/color] represents a company-level [color=skyblue][url]user[/url][/color] that is subscribed to your internet services for the sake of reaching [color=skyblue][url]resident users[/url][/color].\n\nLike end-users, they may be [color=yellow]interfaced with an ethernet or fiber optic connection[/color] to your network.\n\nTypically, enterprise users are [color=skyblue][url]providers[/url][/color] and has a stricter SLA. They also pay more for internet connectivity.\n\nTo satisfy enterprise users, ensure their target audience is able to reach them (Keep an eye on them using the [color=skyblue][url]Suveyor[/url][/color] application). \n\nYou may also need to keep malicious users away from them through the use of [color=skyblue][url]network taps[/url][/color] and [color=skyblue][url]firewalls[/url][/color].",
  "[color=yellow]エンタープライズユーザー[/color]は[color=skyblue][url]レジデントユーザー[/url][/color]にリーチするためにインターネットサービスに加入している企業レベルの[color=skyblue][url]ユーザー[/url][/color]です。\n\nエンドユーザーと同様に、[color=yellow]Ethernetまたは光ファイバー接続[/color]でネットワークに接続される場合があります。\n\n通常、エンタープライズユーザーは[color=skyblue][url]プロバイダー[/url][/color]で、より厳格なSLAを持っています。インターネット接続料金も高額です。\n\nエンタープライズユーザーを満足させるには、ターゲットオーディエンスが到達できることを確認してください（[color=skyblue][url]Surveyor[/url][/color]アプリで監視）。\n\n[color=skyblue][url]ネットワークタップ[/url][/color]と[color=skyblue][url]ファイアウォール[/url][/color]を使用して悪意あるユーザーを遠ざける必要があるかもしれません。")

# Wiki: Game Over
t("how to NOT lose", "負けない方法")
t("In Tower Networking Inc., the game will be over when ANY of the following conditions occur:\n\n        1. Player is in-debt (negative cash balance) for a specified number of days.\n        2. A SLA breach has occurred.\n\nPlanning ahead is key to survival in this cutthroat environment!",
  "Tower Networking Inc.では、以下のいずれかの条件が発生するとゲームオーバーになります：\n\n        1. プレイヤーが指定日数の間借金（マイナスの現金残高）状態。\n        2. SLA違反が発生。\n\nこの厳しい環境で生き残るには計画が鍵です！")

# Wiki: HandheldOS
t("HandheldOS", "HandheldOS")
t("powerful all-in-one mobile device.", "パワフルなオールインワンモバイルデバイス。")
t("Handheld Operating System (HandheldOS)", "ハンドヘルドオペレーティングシステム（HandheldOS）")
t("\nThe [color=yellow]handheld-OS[/color] is your most important tool to run your entire operations. It contains [color=yellow]applications[/color] that can help you observe details about your finances, customer satisfaction and the state of your network.\n\nIt can be used by toggling the [color=yellow]left Alt[/color] key, which will bring up the handheld device for your to interact with.\n\nWith the mouse pointer, click any application on the [color=yellow]home screen[/color] to use them.",
  "\n[color=yellow]handheld-OS[/color]はすべての運営を管理する最も重要なツールです。財務、顧客満足度、ネットワークの状態に関する詳細を確認できる[color=yellow]アプリケーション[/color]を搭載しています。\n\n[color=yellow]左Alt[/color]キーで切り替えることでハンドヘルドデバイスを表示して操作できます。\n\nマウスポインターで[color=yellow]ホーム画面[/color]のアプリケーションをクリックして使用します。")
t("These are must-have applications to run your ISP successfully:\n\n[color=yellow][url][i]CreditStack[/i][/url][/color]: Lets you see your financial position.\n\n[color=yellow][url][i]msgbox[/i][/url][/color]: Logs the messages and notifications you received.\n\n[color=yellow][url][i]netsh[/i][/url][/color]: Used to configure your networking devices and servers.\n\n[color=yellow][url][i]Surveyor[/i][/url][/color]: Lets you see who your [color=skyblue][url]end-users[/url][/color] are and how to satisfy them.\n\n[color=yellow][url][i]D-Market[/i][/url][/color]: A place to buy networking and power [color=skyblue][url]devices[/url][/color] to run your network.\n\n[color=yellow][url][i]Tower-Link[/i][/url][/color]: Allows you to place network risers across different floors.\n\n[color=yellow][url][i]Fi$shy Loans[/i][/url][/color]: Lets you borrow and repay loans.\n\n[color=yellow][url][i]The Secretariat[/i][/url][/color]: Lets you vote on any decisions.\n\n[color=yellow][url][i]Rocket Store[/i][/url][/color]: Lets you install more applications on to your mobile.",
  "ISPを成功させるために必須のアプリケーション：\n\n[color=yellow][url][i]CreditStack[/i][/url][/color]: 財務状況を確認。\n\n[color=yellow][url][i]msgbox[/i][/url][/color]: 受信したメッセージと通知を記録。\n\n[color=yellow][url][i]netsh[/i][/url][/color]: ネットワークデバイスとサーバーの設定に使用。\n\n[color=yellow][url][i]Surveyor[/i][/url][/color]: [color=skyblue][url]エンドユーザー[/url][/color]の確認と満足させる方法を把握。\n\n[color=yellow][url][i]D-Market[/i][/url][/color]: ネットワークと電源[color=skyblue][url]デバイス[/url][/color]を購入する場所。\n\n[color=yellow][url][i]Tower-Link[/i][/url][/color]: 異なるフロア間にネットワークライザーを設置。\n\n[color=yellow][url][i]Fi$shy Loans[/i][/url][/color]: ローンの借入と返済。\n\n[color=yellow][url][i]The Secretariat[/i][/url][/color]: 意思決定への投票。\n\n[color=yellow][url][i]Rocket Store[/i][/url][/color]: モバイルにアプリケーションを追加インストール。")

# Wiki: Power
t("Power", "電力")
t("a basic necessity for all devices.", "すべてのデバイスの基本的な必需品。")
t("All [color=skyblue][url]devices[/url][/color] require [color=yellow]power[/color] to operate. On certain [color=skyblue][url]floors[/url][/color] (i.e., the [color=skyblue][url]data-center[/url][/color]), there is an operational cost to using power.",
  "すべての[color=skyblue][url]デバイス[/url][/color]は動作に[color=yellow]電力[/color]が必要です。特定の[color=skyblue][url]フロア[/url][/color]（[color=skyblue][url]データセンター[/url][/color]など）では電力使用に運用コストがかかります。")
t("Device energy usage for the day are measured in kilowatt hours (kwh).\n\nEach device has its own power usage specification, which may [color=yellow]contribute to a higher/lower energy cost[/color] at the end of day.\n\n",
  "デバイスの1日のエネルギー使用量はキロワット時（kWh）で測定されます。\n\n各デバイスには独自の電力使用仕様があり、日末の[color=yellow]エネルギーコストの増減に寄与[/color]する場合があります。\n\n")
t("At some floors, [color=yellow]power failures[/color] may also occur which may lead to service disruption. Use preventive-measures such as an uninterrupted power supply (UPS) to buffer the critical systems from such interruptions.",
  "一部のフロアでは[color=yellow]停電[/color]が発生しサービス中断につながる場合があります。無停電電源装置（UPS）などの予防策を使用して、重要なシステムをこのような中断から保護してください。")

# Wiki: Resident Users
t("Resident Users", "レジデントユーザー")
t("the driving force the network", "ネットワークの原動力")
t("Resident End Users (Individual/Families)", "レジデントエンドユーザー（個人/家族）")
t("[color=yellow]Resident users[/color] are entities that are domiciled in the tower. \n\nTypically, residents are [color=skyblue][url]consumers[/url][/color] and require an assortment of network connectivity [color=skyblue][url]services[/url][/color] to be satisfied.\n\n",
  "[color=yellow]レジデントユーザー[/color]はタワーに居住するエンティティです。\n\n通常、レジデントは[color=skyblue][url]コンシューマー[/url][/color]で、満足するためにさまざまなネットワーク接続[color=skyblue][url]サービス[/url][/color]が必要です。\n\n")
t("Residents may be [color=yellow]interfaced with an ethernet or fiber optic outlet[/color] to your network.\n\nAside from the status panel next to their network interface, you can also [color=yellow]inspect the conditions[/color] of all the users under your jurisdiction by using the [color=skyblue][url]Surveyor[/url][/color] application.",
  "レジデントは[color=yellow]Ethernetまたは光ファイバーアウトレット[/color]でネットワークに接続される場合があります。\n\nネットワークインターフェース横のステータスパネルに加えて、[color=skyblue][url]Surveyor[/url][/color]アプリを使用して管轄下のすべてのユーザーの[color=yellow]状態を確認[/color]することもできます。")

# Wiki: Software/Programs
t("Software", "ソフトウェア")
t("moving requests from one device to another.", "デバイス間でリクエストを移動。")
t("Software [color=yellow]programs[/color] determines the behavior of [color=skyblue][url]devices[/url][/color]. A program that is running is a [color=yellow]process[/color]. A program has 3 properties:\n\n",
  "ソフトウェア[color=yellow]プログラム[/color]は[color=skyblue][url]デバイス[/url][/color]の動作を決定します。実行中のプログラムは[color=yellow]プロセス[/color]です。プログラムには3つのプロパティがあります：\n\n")
t("[color=yellow][i]CPU Load[/i][/color]: The CPU cost when the program is run.\n\n[color=yellow][i]Code Size[/i][/color]: The storage requirement to install the program.\n\n[color=yellow][i]Memory Size[/i][/color]: The memory requirements to run the program.",
  "[color=yellow][i]CPU負荷[/i][/color]: プログラム実行時のCPUコスト。\n\n[color=yellow][i]コードサイズ[/i][/color]: プログラムインストールに必要なストレージ。\n\n[color=yellow][i]メモリサイズ[/i][/color]: プログラム実行に必要なメモリ。")
t("\nPrograms on any device are managed using the [color=skyblue][url]program[/url][/color] routine. Programs can be installed, started, stopped and uninstalled on server devices using the [color=skyblue][url]debugger[/url][/color].\n\nWhen a device's CPU capacity is exceeded, the running processes get will be throttled and have reduced output. [color=yellow]Trying to run a program with a CPU load higher than the device's total CPU capacity will cause the process to always be skipped[/color], thereby wasting memory of the device.\n\nBefore a program can be installed onto a device, [color=yellow]the storage capacity of the device must meet the code size of the program[/color]. This means that you cannot install a program with a larger code size than the available storage of the device.\n\nBefore a program can be started on a device, [color=yellow]the memory capacity of the device must meet the memory size of the program[/color]. This means that you cannot start a program with a larger memory size than the available memory of the device.\n\n\n",
  "\nデバイス上のプログラムは[color=skyblue][url]program[/url][/color]ルーチンで管理されます。プログラムは[color=skyblue][url]デバッガー[/url][/color]を使用してサーバーデバイスにインストール、開始、停止、アンインストールできます。\n\nデバイスのCPU容量を超えると、実行中のプロセスはスロットルされ出力が低下します。[color=yellow]デバイスの総CPU容量より高いCPU負荷のプログラムを実行しようとすると、プロセスは常にスキップされ[/color]、デバイスのメモリが無駄になります。\n\nプログラムをデバイスにインストールするには、[color=yellow]デバイスのストレージ容量がプログラムのコードサイズを満たす必要があります[/color]。つまり、デバイスの利用可能なストレージよりコードサイズが大きいプログラムはインストールできません。\n\nプログラムをデバイスで開始するには、[color=yellow]デバイスのメモリ容量がプログラムのメモリサイズを満たす必要があります[/color]。つまり、デバイスの利用可能なメモリよりメモリサイズが大きいプログラムは開始できません。\n\n\n")
t("Program Types", "プログラムタイプ")
t("Programs are divided into 3 categories:\n\n  1. Producers\n  2. Converters\n  3. Firmwares\n\n",
  "プログラムは3つのカテゴリに分けられます：\n\n  1. プロデューサー\n  2. コンバーター\n  3. ファームウェア\n\n")
t("[color=yellow]Producers[/color] process creates [color=skyblue][url]uses[/url][/color] that can then be consumed by [color=skyblue][url]end-users[/url][/color] or another process.\n\nThe picture on the left shows 2 running processes, \"[color=orange]dns-lite[/color]\" and \"[color=orange]kea[/color]\" that is producing \"[color=lightsalmon][reply-dns-queries][/color]\" and \"[color=lightsalmon][reply-dhcp-request][/color]\" uses. Currently there are 5 \"[color=lightsalmon][reply-dns-queries][/color]\" and 1 \"[color=lightsalmon][reply-dhcp-request][/color]\" uses in the device's stack.",
  "[color=yellow]プロデューサー[/color]プロセスは[color=skyblue][url]エンドユーザー[/url][/color]や他のプロセスが消費できる[color=skyblue][url]USE[/url][/color]を生成します。\n\n左の図は実行中の2つのプロセス「[color=orange]dns-lite[/color]」と「[color=orange]kea[/color]」が「[color=lightsalmon][reply-dns-queries][/color]」と「[color=lightsalmon][reply-dhcp-request][/color]」USEを生産している様子を示しています。現在デバイスのスタックには5つの「[color=lightsalmon][reply-dns-queries][/color]」と1つの「[color=lightsalmon][reply-dhcp-request][/color]」USEがあります。")
t("Running processes will always produce up until a fixed limit of uses per cycle. This means that [color=yellow]running more than 1 process of the same program will not increase the maximum number of uses[/color].\n\nA different program will have to be installed to increase the capacity on a particular device. Alternatively, a program can be run across more devices to scale horizontally.\n\n\n",
  "実行中のプロセスはサイクルあたりのUSEの固定上限まで常に生産します。つまり、[color=yellow]同じプログラムのプロセスを1つ以上実行してもUSEの最大数は増加しません[/color]。\n\n特定のデバイスの容量を増やすには、別のプログラムをインストールする必要があります。または、より多くのデバイスでプログラムを実行して水平スケーリングできます。\n\n\n")
t("[color=yellow]Converters[/color] process consumes [color=skyblue][url]uses[/url][/color] from a process to produce another different use.\n\nFor example, the \"[color=orange]dns-server[/color]\" program consumes \"[color=lightsalmon][store-text][/color]\" uses to produce \"[color=lightsalmon][dns-reply][/color]\". In order for \"[color=orange]dns-server[/color]\" program to function, it must be able to consume uses from a device ([color=yellow]itself included[/color]) that is running any process that can create \"[color=lightsalmon][store-text][/color]\" uses. In this case, the program \"[color=orange]padu_v1[/color]\" fits the requirement.\n\nPrograms can be further examined using the \"[color=yellow]program describe [color=magenta]<program-name>[/color][/color]\" command. See the [color=skyblue][url]program[/url][/color] command for more information.",
  "[color=yellow]コンバーター[/color]プロセスはプロセスから[color=skyblue][url]USE[/url][/color]を消費して別のUSEを生産します。\n\n例えば、「[color=orange]dns-server[/color]」プログラムは「[color=lightsalmon][store-text][/color]」USEを消費して「[color=lightsalmon][dns-reply][/color]」を生産します。「[color=orange]dns-server[/color]」プログラムが機能するには、「[color=lightsalmon][store-text][/color]」USEを作成できるプロセスを実行しているデバイス（[color=yellow]自分自身を含む[/color]）からUSEを消費できる必要があります。この場合、プログラム「[color=orange]padu_v1[/color]」が要件を満たします。\n\nプログラムは「[color=yellow]program describe [color=magenta]<プログラム名>[/color][/color]」コマンドでさらに詳しく確認できます。詳細は[color=skyblue][url]program[/url][/color]コマンドを参照してください。")
t("[color=yellow]Firmware[/color] processes do not usually produce or consume [color=skyblue][url]uses[/url][/color] but they grant capabilities to the [color=skyblue][url]device[/url][/color] they are running on.\n\nFor instance, the program \"[color=orange]bladeos[/color]\" is a network switch firmware, which allows the device to perform network [color=skyblue][url]switching[/url][/color].\n\nAnother firmware program is \"[color=orange]iptable[/color]\", which allows the device to perform network [color=skyblue][url]routing[/url][/color].",
  "[color=yellow]ファームウェア[/color]プロセスは通常[color=skyblue][url]USE[/url][/color]を生産・消費しませんが、実行中の[color=skyblue][url]デバイス[/url][/color]に機能を付与します。\n\n例えば、プログラム「[color=orange]bladeos[/color]」はネットワークスイッチファームウェアで、デバイスにネットワーク[color=skyblue][url]スイッチング[/url][/color]を実行させます。\n\nもう1つのファームウェアプログラム「[color=orange]iptable[/color]」はデバイスにネットワーク[color=skyblue][url]ルーティング[/url][/color]を実行させます。")
t("\nThe firmware \"[color=orange]firewatcher[/color]\" allows a device to function as a firewall. This allows the device to do network [color=skyblue][url]filtering[/url][/color].\n\nA special firmware \"[color=orange]wirerat[/color]\" allows a device to perform [color=skyblue][url]traffic inspection[/url][/color], which makes the device function as a network tap. In addition, this firmware also generates the use \"[color=lightsalmon][inspect-network-packets][/color]\" which are consumed by [color=skyblue][url]intrusion prevention[/url][/color] or [color=skyblue][url]censorship[/url][/color] programs.",
  "\nファームウェア「[color=orange]firewatcher[/color]」はデバイスをファイアウォールとして機能させます。デバイスにネットワーク[color=skyblue][url]フィルタリング[/url][/color]を実行させます。\n\n特殊なファームウェア「[color=orange]wirerat[/color]」はデバイスに[color=skyblue][url]トラフィック検査[/url][/color]を実行させ、ネットワークタップとして機能させます。さらに、このファームウェアは[color=skyblue][url]侵入防止[/url][/color]や[color=skyblue][url]検閲[/url][/color]プログラムが消費するUSE「[color=lightsalmon][inspect-network-packets][/color]」も生成します。")
t("\nFirmware programs are not available by default. However, they can be stolen from equipment manufacturers or acquired from the black-market. In addition, firmware programs/processes cannot be modified without first jail-breaking the device.",
  "\nファームウェアプログラムはデフォルトでは利用できません。ただし、機器メーカーから盗んだり闇市場から入手できます。さらに、ファームウェアプログラム/プロセスはデバイスをジェイルブレイクしないと変更できません。")

# Misc wiki
t("Nothing...", "なし...")
t("No relevant entries found...", "関連するエントリが見つかりません...")
t("Stub article", "スタブ記事")
t("1 day ago", "1日前")
t("day 1", "1日目")

# ============================================================
# Now let's parse and process the PO file

# BATCH 10: Wiki articles - titles, short descriptions, device specs

# USE (Use Serving Element) - titles
t("Use Serving Element", "USEサービング要素")
t("Resources on your network.", "ネットワーク上のリソース。")
t("Use Serving Element (USE)", "USEサービング要素（USE）")
t("USE Production", "USEの生成")
t("USE Consumption", "USEの消費")

# USE specification details (long entry with BBCode)
t("[color=ffb82f]read and comment[/color]: This behavior is defined by the USE specification \"consumes [color=009ee3]read-text,post-text[/color]\", which means it must consume a USE with both the word \"[color=yellow]read-text[/color]\" and \"[color=yellow]post-text[/color]\". This means that this behavior can/cannot be satisfied by any of the following USE\n\n  - [color=lightsalmon][post-text,read-text][/color] [color=green]OK[/color]\n  - [color=lightsalmon][read-text,post-text][/color] [color=green]OK[/color]\n  - [color=lightsalmon][post-text,read-text,post-image][/color] [color=green]OK[/color]\n  - [color=lightsalmon][post-text][/color] [color=red]NOT OK[/color]\n  - [color=lightsalmon][read-text,political][/color] [color=red]NOT OK[/color]\n  - [color=lightsalmon][post-image][/color] [color=red]DEFINITELY NOT OK[/color]\n\nNotice that the ordering of the words do not matter within the USE, and that additional words also works.\n\nConcisely, a [color=yellow]USE specification[/color] is an [color=yellow]AND condition[/color] on each of the comma separated words.\n\n[color=ffb82f]read political news[/color]: Defined by the USE specification \"consumes [color=009ee3]read-news,political[/color]\", which translates to \"read news\" AND \"political\".\n\n  - [color=lightsalmon][read-news,political][/color] [color=green]OK[/color]\n  - [color=lightsalmon][read-news,political,view-image][/color] [color=green]OK[/color]\n  - [color=lightsalmon][read-news,sports][/color] [color=red]NOT OK[/color]\n  - [color=lightsalmon][read-news][/color] [color=red]NOT OK[/color]",
   "[color=ffb82f]閲覧とコメント[/color]：この行動はUSE仕様「consumes [color=009ee3]read-text,post-text[/color]」で定義されており、「[color=yellow]read-text[/color]」と「[color=yellow]post-text[/color]」の両方を含むUSEを消費する必要があります。この行動は以下のUSEで満たされる/満たされないことを意味します\n\n  - [color=lightsalmon][post-text,read-text][/color] [color=green]OK[/color]\n  - [color=lightsalmon][read-text,post-text][/color] [color=green]OK[/color]\n  - [color=lightsalmon][post-text,read-text,post-image][/color] [color=green]OK[/color]\n  - [color=lightsalmon][post-text][/color] [color=red]NG[/color]\n  - [color=lightsalmon][read-text,political][/color] [color=red]NG[/color]\n  - [color=lightsalmon][post-image][/color] [color=red]完全にNG[/color]\n\nUSE内の語順は関係なく、追加の単語があっても問題ありません。\n\n簡潔に言えば、[color=yellow]USE仕様[/color]はカンマ区切りの各単語に対する[color=yellow]AND条件[/color]です。\n\n[color=ffb82f]政治ニュースを読む[/color]：USE仕様「consumes [color=009ee3]read-news,political[/color]」で定義され、「read news」AND「political」を意味します。\n\n  - [color=lightsalmon][read-news,political][/color] [color=green]OK[/color]\n  - [color=lightsalmon][read-news,political,view-image][/color] [color=green]OK[/color]\n  - [color=lightsalmon][read-news,sports][/color] [color=red]NG[/color]\n  - [color=lightsalmon][read-news][/color] [color=red]NG[/color]")

# User Types and Behaviors
t("Users Types and Behaviors", "ユーザータイプと行動")
t("types of users in your network (and how they behave).", "ネットワーク内のユーザータイプ（とその行動）。")
t("User Types and Behavior", "ユーザータイプと行動")
t("Consumer Behavior", "コンシューマー行動")
t("Producer Behavior", "プロデューサー行動")

# VLAN
t("VLAN", "VLAN")
t("segregation of networks without routers.", "ルーターなしでのネットワーク分離。")
t("Virtual Local Area Networks (VLAN)", "仮想ローカルエリアネットワーク（VLAN）")

# Device Debugger
t("Device Debugger", "デバイスデバッガー")
t("a quintessential tool for operating your network", "ネットワーク運用に不可欠なツール")
t("The Debugger Device", "デバッガーデバイス")

# Devices
t("Devices", "デバイス")
t("operable devices to run your internet services.", "インターネットサービスを運用するための操作可能なデバイス。")

# Bandwidth
t("Bandwidth", "帯域幅")
t("how to not overload networks", "ネットワークを過負荷にしない方法")
t("Network Bandwidth", "ネットワーク帯域幅")

# DNS behind Routers
t("DNS Servers behind Routers", "ルーター越しのDNSサーバー")
t("how to do DNS with routers", "ルーターでのDNS設定方法")
t("DNS Servers Behind Routers", "ルーター越しのDNSサーバー")
t("DNS servers on default route", "デフォルトルート上のDNSサーバー")
t("Designated DNS server address", "指定DNSサーバーアドレス")
t("DNS servers everywhere", "あらゆる場所にDNSサーバー")

# Network Firewall
t("Network Firewall", "ネットワークファイアウォール")
t("keeping unwanted traffic away", "不要なトラフィックを遮断する")
t("Address distinction", "アドレスの区別")

# Hardware Addresses
t("Hardware Addresses", "ハードウェアアドレス")
t("random unique address", "ランダムな一意のアドレス")
t("Hardware Address (Random Unique Addresses)", "ハードウェアアドレス（ランダムな一意のアドレス）")

# Logical Addresses
t("Logical Addresses", "論理アドレス")
t("reference addresses", "参照用アドレス")

# Network Addresses
t("Network Addresses", "ネットワークアドレス")
t("player assigned addresses", "プレイヤーが割り当てるアドレス")
t("Network Addresses (Player Assigned Addresses)", "ネットワークアドレス（プレイヤー割り当てアドレス）")
t("Assigning network addresses", "ネットワークアドレスの割り当て")
t("Meaningful grouping", "意味のあるグループ分け")
t("Multi-casting", "マルチキャスト")

# Network Router
t("segmenting networks with routers", "ルーターによるネットワークの分割")
t("Traversal without destination address", "宛先アドレスなしのトラバーサル")
t("Traversal with hardware destination address", "ハードウェア宛先アドレスありのトラバーサル")
t("Traversal with network destination address", "ネットワーク宛先アドレスありのトラバーサル")
t("Why do you need routers in large networks?", "大規模ネットワークでルーターが必要な理由")
t("the simplest interconnect", "最もシンプルな相互接続")

# Network Taps
t("Network Taps", "ネットワークタップ")
t("packet inspection", "パケット検査")
t("Network Inspection (Tapping)", "ネットワーク検査（タッピング）")

# Network Traffic Types
t("Network Traffic Types", "ネットワークトラフィックタイプ")
t("classification of traversal intents", "トラバーサルの意図の分類")

# Network Traversal
t("Network Traversal", "ネットワークトラバーサル")
t("core network mechanics", "コアネットワークメカニズム")
t("Network Traversals", "ネットワークトラバーサル")
t("Traversals without specific destination address.", "特定の宛先アドレスなしのトラバーサル。")
t("Traversals with specific destination address.", "特定の宛先アドレスありのトラバーサル。")

# Netsh Routine Wiki entries
t("always (Netsh Routine)", "always（Netshルーティン）")
t("default debugger specification", "デフォルトデバッガーの指定")
t("always routine", "alwaysルーティン")
t("always using", "always using")
t("dhcp (Netsh Routine)", "dhcp（Netshルーティン）")
t("dhcp management", "DHCP管理")
t("dhcp routine", "dhcpルーティン")
t("dhcp show", "dhcp show")
t("dhcp option", "dhcp option")
t("dns (Netsh Routine)", "dns（Netshルーティン）")
t("dns management routine", "DNS管理ルーティン")
t("dns routine", "dnsルーティン")
t("dns map", "dns map")
t("dns lookup", "dns lookup")
t("dns clear", "dns clear")
t("firewall (Netsh Routine)", "firewall（Netshルーティン）")
t("firewall policy configuration", "ファイアウォールポリシー設定")
t("firewall routine", "firewallルーティン")
t("firewall show", "firewall show")
t("firewall allow/deny", "firewall allow/deny")
t("firewall default", "firewall default")
t("firewall remove", "firewall remove")
t("lstdbg (Netsh Routine)", "lstdbg（Netshルーティン）")
t("find your debuggers", "デバッガーを見つける")
t("lstdbg routine", "lstdbgルーティン")
t("net (Netsh Routine)", "net（Netshルーティン）")
t("network configuration routine", "ネットワーク設定ルーティン")
t("net routine", "netルーティン")
t("net show", "net show")
t("net address", "net address")
t("net dns", "net dns")
t("net dhcp", "net dhcp")
t("pcap (Netsh Routine)", "pcap（Netshルーティン）")
t("perform packet capture/inspection", "パケットキャプチャ/検査の実行")
t("pcap routine", "pcapルーティン")
t("pcap", "pcap")
t("program (Netsh Routine)", "program（Netshルーティン）")
t("install and run programs on servers", "サーバーにプログラムをインストール・実行する")
t("program routine", "programルーティン")
t("program list", "program list")
t("program describe", "program describe")
t("program view", "program view")
t("program install/uninstall", "program install/uninstall")
t("program start", "program start")
t("program stop", "program stop")
t("route (Netsh Routine)", "route（Netshルーティン）")
t("route management", "ルート管理")
t("route routine", "routeルーティン")
t("route show", "route show")
t("route add", "route add")
t("route default", "route default")
t("route remove", "route remove")
t("scan (Netsh Routine)", "scan（Netshルーティン）")
t("enumerate device and users on your network", "ネットワーク上のデバイスとユーザーを列挙する")
t("scan routine", "scanルーティン")
t("scan", "scan")
t("trace/ping (Netsh Routine)", "trace/ping（Netshルーティン）")
t("network tracing", "ネットワークトレース")
t("trace & ping routine", "trace & pingルーティン")
t("trace", "trace")
t("ping", "ping")
t("watch (Netsh Routine)", "watch（Netshルーティン）")
t("monitor device state", "デバイス状態の監視")
t("watch routine", "watchルーティン")
t("watch", "watch")

# Application Wiki entries
t("DMarket Application", "D-Marketアプリケーション")
t("an e-commerce store for device purchases", "デバイス購入用のeコマースストア")
t("DMarket application", "D-Marketアプリケーション")
t("netsh Application", "netshアプリケーション")
t("a command-line application that goes hand-in-hand with the debugger", "デバッガーと連携するコマンドラインアプリケーション")
t("NetShell Application", "NetShellアプリケーション")
t("Surveyor Application", "Surveyorアプリケーション")

# Tutorial recaps
t("Tutorial: Basic Game Controls", "チュートリアル：基本操作")
t("tutorial recap for basic game controls", "基本操作チュートリアルのまとめ")
t("Tutorial: Basic Game Control", "チュートリアル：基本操作")
t("Tutorial: Basic Networking", "チュートリアル：基本ネットワーク")
t("tutorial recap for basic networking", "基本ネットワークチュートリアルのまとめ")
t("Tutorial: Riser Setup Across Floor", "チュートリアル：フロア間ライザー設定")
t("tutorial recap for riser setup across floor", "フロア間ライザー設定チュートリアルのまとめ")
t("Tutorial: Online Store Item Purchase", "チュートリアル：オンラインストアでの購入")
t("tutorial recap for online store item purchase", "オンラインストア購入チュートリアルのまとめ")
t("Tutorial: Basic Domain Name System", "チュートリアル：基本ドメインネームシステム")
t("tutorial recap for basic DNS", "基本DNSチュートリアルのまとめ")
t("Tutorial: Basic Domain Name System (DNS)", "チュートリアル：基本ドメインネームシステム（DNS）")
t("Tutorial: Router Configuration", "チュートリアル：ルーター設定")
t("tutorial recap for router configuration", "ルーター設定チュートリアルのまとめ")
t("Tutorial: Rocket Store and Domain Name Registration", "チュートリアル：Rocket Storeとドメイン名登録")
t("tutorial recap for rocket store and domain name registration", "Rocket Storeとドメイン名登録チュートリアルのまとめ")
t("Tutorial: Rocket Store and Register Domain Name", "チュートリアル：Rocket Storeとドメイン名登録")

# Wiki misc
t("Nothing...", "何もありません...")
t("No relevant entries found...", "関連するエントリが見つかりません...")
t("Stub article", "スタブ記事")
t("search keyword...", "キーワードで検索...")
t("Previous", "前へ")
t("Back to top", "トップに戻る")
t("WIKI ENTRY NAME", "WIKIエントリ名")
t("MORE DETAILS", "詳細情報")
t("how to NOT lose", "負けない方法")
t("Not a cable", "ケーブルではありません")
t("Incompatible cable", "互換性のないケーブル")
t("At capacity", "容量上限")

# Device descriptions
t("{nport}-port core router.", "{nport}ポートコアルーター。")
t("High bandwidth router for core networking.", "コアネットワーキング用高帯域幅ルーター。")
t("2-2 hardware-based round-robin network load balancer.", "2-2ハードウェアベースのラウンドロビンネットワークロードバランサー。")
t("{nport}-port ethernet remote debugger.", "{nport}ポート イーサネットリモートデバッガー。")
t("{nport}-port ethernet load tester. Blasts UDP/53 DNS query traffic towards targeted devices.", "{nport}ポート イーサネットロードテスター。対象デバイスにUDP/53 DNSクエリトラフィックを送信します。")
t("Decentro mining rig.", "Decentroマイニングリグ。")
t("Not rack mountable.", "ラックマウント不可。")
t("Handles up to {bw_cap_per_tick} traversals per tick.", "1ティックあたり最大{bw_cap_per_tick}トラバーサルを処理。")
t("CPU cycles 1 tick every {tick_period} seconds.", "CPU: {tick_period}秒ごとに1ティック処理。")
t("Power consumption: {power}W.", "消費電力: {power}W。")
t("Specs: {ncpu} CPU, {nmem} memory and {nsto} storage.", "スペック: CPU {ncpu}、メモリ {nmem}、ストレージ {nsto}。")
t("Supports up to {power}W loads.", "最大{power}Wの負荷をサポート。")
t("Stores up to {max_cable_len} length.", "最大{max_cable_len}の長さを収納可能。")
t("{nport}-port network storage device.", "{nport}ポート ネットワークストレージデバイス。")
t('Comes with 5 SATA 3.5" expansion slots.', '5つのSATA 3.5"拡張スロット付き。')
t("{nport}-port modular computing unit.", "{nport}ポート モジュラーコンピューティングユニット。")
t("Homelab equipment.", "ホームラボ機器。")
t("Top of the line enterprise grade network firewall.", "最高級エンタープライズグレードネットワークファイアウォール。")
t("Power switch.", "電源スイッチ。")
t("Ethernet in-line network tap with port-mirroring capabilities.", "ポートミラーリング機能付きイーサネットインラインネットワークタップ。")
t("Duplex (bidirectional) media converter.", "デュプレックス（双方向）メディアコンバーター。")
t("RJ45 bidirectional media repeater.", "RJ45双方向メディアリピーター。")
t("Fiber optic SC bidirectional media repeater.", "光ファイバーSC双方向メディアリピーター。")
t("RJ45 unidirectional media repeater.", "RJ45単方向メディアリピーター。")
t("Fiber optic SC unidirectional media repeater.", "光ファイバーSC単方向メディアリピーター。")
t("Make length: {len} px", "長さ設定: {len} px")
t("Provides Decentro transaction verification to the p2p currency network.", "Decentroピアツーピア通貨ネットワークへのトランザクション検証を提供します。")
t("Traffic from either front ports are alternated between the back ports.", "フロントポートからのトラフィックはバックポート間で交互に振り分けられます。")
t("back0", "back0")
t("back1", "back1")
t("front2", "front2")
t("front3", "front3")
t("Z0", "Z0")
t("Z1", "Z1")
t("Z2", "Z2")
t("Z3", "Z3")
t("DC", "DC")
t("I/O", "I/O")
t("IN", "IN")
t("OUT", "OUT")
t("Ethernet in-line network traffic monitoring and filtering system.", "イーサネットインラインネットワークトラフィック監視・フィルタリングシステム。")
t("Mixed medium in-line network traffic monitoring and filtering system.", "ミックスドメディアインラインネットワークトラフィック監視・フィルタリングシステム。")
t("RJ45 to Fiber optic SC simplex (unidirection) media converter.", "RJ45から光ファイバーSCシンプレックス（単方向）メディアコンバーター。")
t("Fiber optic SC to RJ45 simplex (unidirection) media converter.", "光ファイバーSCからRJ45シンプレックス（単方向）メディアコンバーター。")

# Hit ESC / wiki hints
t("Hit 'ESC' to pause/unpause the game to read the wiki without time pressure.", "ESCキーを押してゲームを一時停止/再開し、時間に追われずにWikiを読みましょう。")
t("Have some thoughts/feedback about the concepts/wiki? Feel free to share it with us by pressing F8. We appreciate any feedback!", "コンセプト/Wikiについてご意見・フィードバックがありますか？F8キーを押してお気軽にお寄せください。フィードバックを歓迎します！")

# Emoji entries
t("\u23f8\ufe0f", "\u23f8\ufe0f")
t("\U0001f504", "\U0001f504")

# Variable-only entries
t("{bd_text}", "{bd_text}")



# BATCH 11: Wiki article body translations (auto-generated)
# Wiki article translations - auto-generated
# Generated by gen_wiki_translations.py

t("A [color=skyblue][url]device[/url][/color] is able to function as a DNS server if it has the \"[color=lightsalmon][reply-dns-queries][/color]\" [color=skyblue][url]use[/url][/color] in its [color=yellow]USE STACK[/color]. This can be achieved by running [color=skyblue][url]programs[/url][/color] such as \"[color=orange]dns-lite[/color]\" or \"[color=orange]dns-server[/color]\".\n\nThe device should also have enough bandwidth capacity to handle DNS resolution traffic.", "[color=skyblue][url]デバイス[/url][/color]は、[color=yellow]USEスタック[/color]に「[color=lightsalmon][reply-dns-queries][/color]」という[color=skyblue][url]USE[/url][/color]を持っている場合、DNSサーバーとして機能できます。これは「[color=orange]dns-lite[/color]」や「[color=orange]dns-server[/color]」などの[color=skyblue][url]プログラム[/url][/color]を実行することで実現できます。\n\nデバイスにはDNS解決トラフィックを処理するのに十分な帯域幅容量も必要です。")
t("The pictures on the right shows issues with DNS resolution. \n\nIn the first picture, the debugger is unable to reach the DNS server.\n\nIn the second picture, the DNS entry for '[color=orange]nosuchthing.com[/color]' does not exists.", "右の画像はDNS解決に関する問題を示しています。\n\n最初の画像では、デバッガーがDNSサーバーに到達できません。\n\n2番目の画像では、「[color=orange]nosuchthing.com[/color]」のDNSエントリが存在しません。")
t("Oops... looks like the link you clicked is still work-in-progress...\n\nHaving trouble with the wiki? Share your thoughts with us using the [color=yellow]F8 key[/color].", "おっと...クリックしたリンクはまだ作成中のようです...\n\nWikiでお困りですか？[color=yellow]F8キー[/color]でご意見をお聞かせください。")
t("Use Serving Element", "USEサービング要素")
t("Resources on your network.", "ネットワーク上のリソースです。")
t("Use Serving Element (USE)", "USEサービング要素 (USE)")
t("A \"[color=yellow]USE[/color]\" is an acronym for \"[color=yellow]Use Serving Element[/color]\", which is a resource on a device or user that serves a particular use. A single USE is enclosed by square brackets '[ ... ]' when observed using the [color=skyblue][url]watch[/url][/color] routine.", "「[color=yellow]USE[/color]」は「[color=yellow]Use Serving Element[/color]」の略称で、デバイスやユーザー上で特定の用途を提供するリソースです。単一のUSEは[color=skyblue][url]watch[/url][/color]ルーチンで観察すると、角括弧「[ ... ]」で囲まれて表示されます。")
t("A USE can be produced by a [color=skyblue][url]producer[/url][/color] user. For example, the user behavior shown in the picture above using the [color=skyblue][url]Surveyor[/url][/color] produces 2 types of USE: \"[color=lightsalmon][political,read-text,read-news][/color]\" and \"[color=lightsalmon][read-text,post-text][/color]\".", "USEは[color=skyblue][url]プロデューサー[/url][/color]ユーザーによって生産されます。例えば、上の画像に示されたユーザー行動は[color=skyblue][url]Surveyor[/url][/color]を使用して、2種類のUSE「[color=lightsalmon][political,read-text,read-news][/color]」と「[color=lightsalmon][read-text,post-text][/color]」を生産しています。")
t("A USE can also be produced by a running [color=skyblue][url]program[/url][/color]. For example, the program \"[color=orange]dns-lite[/color]\" shown in the picture above using the [color=skyblue][url]program[/url][/color] routine will produce the USE: \"[color=lightsalmon][reply-dns-queries][/color]\"", "USEは実行中の[color=skyblue][url]プログラム[/url][/color]によっても生産されます。例えば、上の画像に示された「[color=orange]dns-lite[/color]」プログラムは[color=skyblue][url]program[/url][/color]ルーチンを使用すると、USE「[color=lightsalmon][reply-dns-queries][/color]」を生産します。")
t("At any given time, [color=yellow]a producer can generate USE up to a certain limit until they are consumed[/color].", "任意の時点で、[color=yellow]プロデューサーは消費されるまで一定の上限までUSEを生成できます[/color]。")
t("USE Consumption", "USEの消費")
t("A USE can be consumed by an [color=skyblue][url]end-user[/url][/color] with a [color=skyblue][url]consumer[/url][/color] behavior to [color=yellow]increase their satiety levels[/color]. USE consumption is defined by a USE specification. Consider the behaviors shown in the picture below:", "USEは[color=skyblue][url]エンドユーザー[/url][/color]の[color=skyblue][url]コンシューマー[/url][/color]行動によって消費され、[color=yellow]満足度レベルを上昇[/color]させます。USE消費はUSE仕様によって定義されます。以下の画像に示された行動を考えてみましょう:")
t("Users have different [color=yellow]types[/color] that will affect how they are satisfied.\n\nTypically, [color=skyblue][url]resident families or single users[/url][/color] (e.g., [color=orange]Net Nester[/color]) uses your network to browse and access network services. This means their satiety increases when they are able to access (and consume) [color=skyblue][url]content[/url][/color] over the network. These user behaviors are classified as [color=yellow][i]Consumer Behavior[/i][/color].\n\nConversely, [color=skyblue][url]company-level user types[/url][/color] (e.g., [color=orange]WireSync News[/color]) uses your network to reach consumers. Their satiety increases when their [color=skyblue][url]content[/url][/color] is consumed by other end users. These behavior are classified as [color=yellow][i]Producer Behavior[/i][/color].", "ユーザーにはそれぞれ異なる[color=yellow]タイプ[/color]があり、満足度の達成方法に影響します。\n\n一般的に、[color=skyblue][url]居住者の家族や単身ユーザー[/url][/color]（例：[color=orange]Net Nester[/color]）はネットワークを使ってブラウジングやネットワークサービスへのアクセスを行います。つまり、ネットワーク経由で[color=skyblue][url]コンテンツ[/url][/color]にアクセス（消費）できると満足度が上がります。これらのユーザー行動は[color=yellow][i]コンシューマー行動[/i][/color]に分類されます。\n\n一方、[color=skyblue][url]企業レベルのユーザータイプ[/url][/color]（例：[color=orange]WireSync News[/color]）はネットワークを使ってコンシューマーにリーチします。彼らの[color=skyblue][url]コンテンツ[/url][/color]が他のエンドユーザーに消費されると満足度が上がります。これらの行動は[color=yellow][i]プロデューサー行動[/i][/color]に分類されます。")
t("Lastly, there is a special type of users known as [color=yellow][i]Transformers[/i][/color]. These users are consumers by nature, but they also produce something in return. Conceptually, these are independent content creators.", "最後に、[color=yellow][i]トランスフォーマー[/i][/color]と呼ばれる特別なタイプのユーザーがいます。これらのユーザーは本質的にコンシューマーですが、見返りに何かを生産します。概念的には、独立したコンテンツクリエイターです。")
t("Consumer behavior is defined by a [color=skyblue][url]use[/url][/color] specification and an importance factor.\n\nThe higher the importance, the greater the impact on satiety if the behavior is satisfied (or not).", "コンシューマー行動は[color=skyblue][url]USE[/url][/color]仕様と重要度係数によって定義されます。\n\n重要度が高いほど、行動が満たされた（または満たされなかった）場合の満足度への影響が大きくなります。")
t("To satisfy a behavior, the user must first be able to access a [color=skyblue][url]DNS[/url][/color] server to resolve the address to visit. This means a DNS mapping for the user selected provider to visit.\n\nWhen an address is obtained, the user then attempts to consume a compatible use from the destination. There could be different factors at play that result in a user not being able to consume successfully. A non-exhaustive list of reasons are listed as follows:\n\n1. User is not connected to network.\n2. Destination (e.g., company endpoint) is not connected to network.\n3. No routing rules from user to destination (if connected through a router).\n4. Blocked by firewall policy (if connected through a firewall).\n5. Bandwidth exhaustion in any of the in-line devices (e.g., switch overloaded).\n6. Destination has insufficient uses (e.g., company overloaded/DDOS attacks).\n\nIn addition, giving the [color=orange]wrong destination address[/color] on the DNS mapping will also cause the consume action to fail because the user is consuming from the wrong place.", "行動を満たすには、ユーザーはまず[color=skyblue][url]DNS[/url][/color]サーバーにアクセスして訪問先のアドレスを解決する必要があります。これは、ユーザーが選択した訪問先プロバイダーのDNSマッピングが必要です。\n\nアドレスを取得すると、ユーザーは宛先から互換性のあるUSEの消費を試みます。ユーザーが正常に消費できない原因にはさまざまな要因が考えられます。以下は理由の非網羅的なリストです:\n\n1. ユーザーがネットワークに接続されていない。\n2. 宛先（例：企業エンドポイント）がネットワークに接続されていない。\n3. ユーザーから宛先へのルーティングルールがない（ルーター経由で接続されている場合）。\n4. ファイアウォールポリシーによりブロックされている（ファイアウォール経由で接続されている場合）。\n5. インラインデバイスの帯域幅が枯渇している（例：スイッチの過負荷）。\n6. 宛先のUSEが不足している（例：企業の過負荷/DDoS攻撃）。\n\nさらに、DNSマッピングで[color=orange]間違った宛先アドレス[/color]を設定すると、ユーザーが間違った場所から消費しようとするため、消費アクションが失敗します。")
t("The [color=skyblue][url]Surveyor[/url][/color] application is a must-have tool when attempting to fix consumer's networking issues. Any problems faced by the user is logged on the \"Issues and Complaints\" section in the detailed view of a particular user.", "[color=skyblue][url]Surveyor[/url][/color]アプリケーションは、コンシューマーのネットワーク問題を解決する際に必須のツールです。ユーザーが直面する問題は、特定のユーザーの詳細ビューの「問題と苦情」セクションに記録されます。")
t("Producer behavior is defined by a [color=skyblue][url]use[/url][/color] specification, a [color=skyblue][url]domain name[/url][/color] and a visitor quota (shown in the \"[color=yellow]visits/required[/color]\" label on the behavior insights section.", "プロデューサー行動は[color=skyblue][url]USE[/url][/color]仕様、[color=skyblue][url]ドメイン名[/url][/color]、および訪問者クォータ（行動インサイトセクションの「[color=yellow]visits/required[/color]」ラベルに表示）によって定義されます。")
t("The satiety of a producer is determined by the average quota performance of each services they are hosting. The quota for each service also indicate the capacity of the producer for that particular produced [color=skyblue][url]use[/url][/color] specification.\n\nFor example, the view above shows that the service \"[color=orange]textfirsthand.biz[/color]\" has 3 visitors at the moment, but is able to serve up to 15.\n\nThe domain name of the producing behavior is what consumers \"[i]see[/i]\". Therefore, a [color=skyblue][url]DNS mapping[/url][/color] must for the domain name that correctly directs consumers to the right producers.", "プロデューサーの満足度は、ホスティングしている各サービスの平均クォータ実績によって決まります。各サービスのクォータは、その特定の生産[color=skyblue][url]USE[/url][/color]仕様のプロデューサーの容量も示しています。\n\n例えば、上のビューでは、サービス「[color=orange]textfirsthand.biz[/color]」に現在3人の訪問者がいますが、最大15人まで対応可能です。\n\n生産行動のドメイン名は、コンシューマーが「[i]見る[/i]」ものです。したがって、コンシューマーを正しいプロデューサーに誘導するドメイン名の[color=skyblue][url]DNSマッピング[/url][/color]が必要です。")
t("In Tower Networking Inc., [color=yellow] VLAN[/color] or virtual local area networks can be used to assign a particular network port on a [color=skyblue][url]network switch[/url][/color] to a specific broadcast domain. A broadcast domain means all devices on the same domain is able to broadcast to one another, effectively being on the same \"network\".\n\nOn an unmanaged network switch without VLAN, all ports are on the same broadcast domain. This means if a user/device performs a traversal on that switch it may possibly visit all other devices on that same switch, which lowers the effective bandwidth of the switch.\n\nBy \"tagging\" ports, one can limit the traversals to only relevant devices on the switch. The following animation exhibit 2 VLAN switches.", "Tower Networking Inc.では、[color=yellow]VLAN[/color]（仮想ローカルエリアネットワーク）を使用して、[color=skyblue][url]ネットワークスイッチ[/url][/color]の特定のネットワークポートを特定のブロードキャストドメインに割り当てることができます。ブロードキャストドメインとは、同じドメイン上のすべてのデバイスが互いにブロードキャストでき、事実上同じ「ネットワーク」上にあることを意味します。\n\nVLANなしの非マネージドネットワークスイッチでは、すべてのポートが同じブロードキャストドメインにあります。つまり、ユーザー/デバイスがそのスイッチでトラバーサルを実行すると、同じスイッチ上の他のすべてのデバイスを訪問する可能性があり、スイッチの実効帯域幅が低下します。\n\nポートに「タグ」を付けることで、トラバーサルをスイッチ上の関連デバイスのみに制限できます。次のアニメーションは2つのVLANスイッチを示しています。")
t("The following observations can be made:\n\n1. Traversals on the switch is now only limited to ports of the same tag in which the requests comes from. On switch 1, only ports with tag [color=magenta]#BBB[/color] is traversed.\n2. Traversals can \"use\" different tags after egressing (exiting) a switch. On switch 2, the connected port (Port 2) is tagged [color=magenta]#AAA[/color], which allows Alice to successfully reach Bob.\n\nVLAN prevents irrelevant traffic from hitting other nodes. In the animation example, Charlie and Dave do not have their bandwidth wasted by Alice's traversal.", "以下の観察が可能です:\n\n1. スイッチでのトラバーサルは、リクエスト元と同じタグのポートのみに制限されます。スイッチ1では、タグ[color=magenta]#BBB[/color]のポートのみがトラバーサルされます。\n2. トラバーサルは、スイッチを出た（イグレスした）後に異なるタグを「使用」できます。スイッチ2では、接続ポート（ポート2）にタグ[color=magenta]#AAA[/color]が付けられており、AliceがBobに正常に到達できます。\n\nVLANは無関係なトラフィックが他のノードに到達するのを防ぎます。アニメーションの例では、CharlieとDaveの帯域幅はAliceのトラバーサルによって浪費されません。")
t("The [color=yellow]debugger[/color] [color=skyblue][url]device[/url][/color] is a 2-port device used to allow troubleshooting and configuration tasks using the [color=skyblue][url]netsh[/url][/color] [color=skyblue][url]application[/url][/color].\n\nTo [color=yellow]configure or troubleshoot a device[/color], a debugger must be [color=skyblue][url]powered[/url][/color] and a [color=skyblue][url]network route[/url][/color] must exist [color=yellow]between the debugger and the device[/color].\n\nIt is a good idea to place the debugger in your datacenter and connect it directly to your core switches to allow a single debugger to troubleshoot/configure your entire datacenter.", "[color=yellow]デバッガー[/color][color=skyblue][url]デバイス[/url][/color]は、[color=skyblue][url]netsh[/url][/color][color=skyblue][url]アプリケーション[/url][/color]を使用してトラブルシューティングや設定作業を行うための2ポートデバイスです。\n\n[color=yellow]デバイスの設定やトラブルシューティング[/color]を行うには、デバッガーに[color=skyblue][url]電源[/url][/color]が入っており、[color=yellow]デバッガーとデバイスの間[/color]に[color=skyblue][url]ネットワーク経路[/url][/color]が存在する必要があります。\n\nデバッガーをデータセンターに配置し、コアスイッチに直接接続することで、1台のデバッガーでデータセンター全体のトラブルシューティング/設定が可能になります。")
t("The figure on the right shows a direct connection setup from the debugger to a device.\n\nThis allows the debugger to execute commands on this device.", "右の図は、デバッガーからデバイスへの直接接続のセットアップを示しています。\n\nこれにより、デバッガーはこのデバイスでコマンドを実行できます。")
t("A slightly better setup is to wire the debugger through a switch. This allows the debugger to execute commands on every device connected through the switch.\n\nIn the example to the right, the debugger will be able to debug and configure both device A and device B without needing to change the cabling setup.", "より良いセットアップは、デバッガーをスイッチ経由で接続することです。これにより、デバッガーはスイッチを通じて接続されたすべてのデバイスでコマンドを実行できます。\n\n右の例では、ケーブル配線を変更することなく、デバッガーはデバイスAとデバイスBの両方をデバッグおよび設定できます。")
t("To see the list of debuggers currently accessible, use the \"[color=yellow]lstdbg[/color]\" command. This will show a list of debuggers and their [color=skyblue][url]logical address[/url][/color].\n\nYou can then see the list of devices that are accessible by the debugger using the \"[color=yellow]scan[/color]\" command; if the debugger address is [color=orange]63168[/color], then input \"[color=yellow]scan devices using 63168[/color]\".\n\nThe scan command shows a list of device that are accessible by the debugger and their corresponding network address.\n\nUsing the \"[color=yellow]watch[/color]\" command on the listed device addresses, detailed information about the device can then be seen on the debugger. For example, if the scanned device address is [color=orange]41216[/color], then input \"[color=yellow]watch 41216 using 63168[/color]\".", "現在アクセス可能なデバッガーの一覧を表示するには、「[color=yellow]lstdbg[/color]」コマンドを使用します。デバッガーのリストとその[color=skyblue][url]論理アドレス[/url][/color]が表示されます。\n\n次に、「[color=yellow]scan[/color]」コマンドを使用して、デバッガーからアクセス可能なデバイスの一覧を表示できます。デバッガーのアドレスが[color=orange]63168[/color]の場合、「[color=yellow]scan devices using 63168[/color]」と入力します。\n\nscanコマンドは、デバッガーからアクセス可能なデバイスとその対応するネットワークアドレスのリストを表示します。\n\n表示されたデバイスアドレスに対して「[color=yellow]watch[/color]」コマンドを使用すると、デバッガー上にデバイスの詳細情報が表示されます。例えば、スキャンされたデバイスアドレスが[color=orange]41216[/color]の場合、「[color=yellow]watch 41216 using 63168[/color]」と入力します。")
t("It may be unwieldly to keep typing address of the debugger if you always debug from the same debugger.\n\nUse the [color=skyblue][url]always routine[/url][/color] command to set the default debugger to  use.\n\nFor example, given that the debugger address is [color=orange]51727[/color] and we always want to use that, input \"[color=yellow]always using 51727[/color]\".\n\nThis allows you to then type any debugger related commands without the \"using ...\" part.\n\nThis means that instead of typing \"[color=yellow]scan devices using 51727[/color]\", you would only need to type \"[color=yellow]scan devices[/color]\".", "常に同じデバッガーからデバッグする場合、毎回デバッガーのアドレスを入力するのは面倒かもしれません。\n\n[color=skyblue][url]alwaysルーチン[/url][/color]コマンドを使用して、使用するデフォルトデバッガーを設定しましょう。\n\n例えば、デバッガーのアドレスが[color=orange]51727[/color]で常にそれを使いたい場合、「[color=yellow]always using 51727[/color]」と入力します。\n\nこれにより、デバッガー関連のコマンドを「using ...」の部分なしで入力できるようになります。\n\nつまり、「[color=yellow]scan devices using 51727[/color]」と入力する代わりに、「[color=yellow]scan devices[/color]」とだけ入力すればよくなります。")
t("You can always refer to the [color=skyblue][url]netsh[/url][/color] guide for help. Always remember that the command \"[color=yellow]man[/color]\" (short for manual) is a useful way to find out more about a command. To use the command, simply type \"[color=yellow]man[/color]\" or \"[color=yellow]man[/color] [color=magenta]<name of program you want to find out>[/color]\"", "いつでも[color=skyblue][url]netsh[/url][/color]ガイドを参照できます。「[color=yellow]man[/color]」コマンド（manualの略）はコマンドの詳細を調べるのに便利です。使用するには、「[color=yellow]man[/color]」または「[color=yellow]man[/color] [color=magenta]<調べたいプログラム名>[/color]」と入力してください。")
t("A [color=yellow]device[/color] is an operational unit that can be [color=skyblue][url]powered[/url][/color] or [color=skyblue][url]networked[/url][/color].\n\nWhen powered, devices will run [color=skyblue][url]programs[/url][/color] that enable them to produce [color=skyblue][url]uses[/url][/color] and function as network equipment. Typically, a networked device can be accessed by [color=skyblue][url]routines[/url][/color] using a [color=skyblue][url]debugger[/url][/color].", "[color=yellow]デバイス[/color]は、[color=skyblue][url]電源供給[/url][/color]や[color=skyblue][url]ネットワーク接続[/url][/color]が可能な動作ユニットです。\n\n電源が入ると、デバイスは[color=skyblue][url]プログラム[/url][/color]を実行し、[color=skyblue][url]USE[/url][/color]を生産してネットワーク機器として機能します。通常、ネットワーク接続されたデバイスは[color=skyblue][url]デバッガー[/url][/color]を使用した[color=skyblue][url]ルーチン[/url][/color]でアクセスできます。")
t("When [color=yellow]hovering the mouse[/color] over a device, important information such as the device's product name, device power state, the [color=skyblue][url]hardware address[/url][/color] and configured [color=skyblue][url]network address[/url][/color] and [color=skyblue][url]designated DNS server address[/url][/color] will be shown.\n\nBy default, a device purchased off-the-shelf will not have any network address or designated DNS server assigned, therefore ommiting these information from the hover panel.", "[color=yellow]マウスをデバイスの上に置く[/color]と、デバイスの製品名、電源状態、[color=skyblue][url]ハードウェアアドレス[/url][/color]、設定された[color=skyblue][url]ネットワークアドレス[/url][/color]、[color=skyblue][url]指定DNSサーバーアドレス[/url][/color]などの重要な情報が表示されます。\n\nデフォルトでは、購入したばかりのデバイスにはネットワークアドレスや指定DNSサーバーが割り当てられていないため、ホバーパネルにこれらの情報は表示されません。")
t("[color=yellow]Devices[/color] can be purchased from various merchants found in [color=skyblue][url]DMARKET[/url][/color].", "[color=yellow]デバイス[/color]は[color=skyblue][url]DMARKET[/url][/color]にあるさまざまな販売業者から購入できます。")
t("In Tower Networking Inc., all [color=skyblue][url]devices[/url][/color] has a finite [color=yellow]bandwidth capacity[/color] (unless you're playing in easy mode).\n\nWhen a device's bandwidth is exhausted, it cannot facilitate [color=skyblue][url]network traversals[/url][/color] anymore and the effect is visible on the device either by physically looking at it or by using [color=skyblue][url]netsh[/url][/color] routines such as [color=skyblue][url]watch[/url][/color].", "Tower Networking Inc.では、すべての[color=skyblue][url]デバイス[/url][/color]には有限の[color=yellow]帯域幅容量[/color]があります（イージーモードでプレイしている場合を除く）。\n\nデバイスの帯域幅が枯渇すると、[color=skyblue][url]ネットワークトラバーサル[/url][/color]を処理できなくなり、その影響はデバイスを物理的に見るか、[color=skyblue][url]watch[/url][/color]などの[color=skyblue][url]netsh[/url][/color]ルーチンを使用することで確認できます。")
t("The bandwidth capacity of a device can be inspected using [color=skyblue][url]net[/url][/color] routine or the [color=skyblue][url]watch[/url][/color] routine using the [color=skyblue][url]netsh[/url][/color] application. If the [color=yellow]network load[/color] is consistently at 100%, then the device is likely to be [color=yellow]overloaded[/color].", "デバイスの帯域幅容量は、[color=skyblue][url]netsh[/url][/color]アプリケーションの[color=skyblue][url]net[/url][/color]ルーチンまたは[color=skyblue][url]watch[/url][/color]ルーチンで確認できます。[color=yellow]ネットワーク負荷[/color]が常に100%の場合、デバイスは[color=yellow]過負荷[/color]になっている可能性があります。")
t("[color=skyblue][url]Risers[/url][/color] also have bandwidth capacity, which are shown using the [color=skyblue][url]tower link[/url][/color] application. It is shown as as the limit of \"[color=yellow]utilization (traversals/tick)[/color]\". If the utilization consistently hits 100%, then the link is [color=yellow]overloaded[/color].", "[color=skyblue][url]ライザー[/url][/color]にも帯域幅容量があり、[color=skyblue][url]Tower Link[/url][/color]アプリケーションで表示されます。「[color=yellow]utilization (traversals/tick)[/color]」の上限として表示されます。使用率が常に100%に達している場合、リンクは[color=yellow]過負荷[/color]です。")
t("In Tower Networking Inc., all user traversals requires [color=skyblue][url]DNS[/url][/color] resolution to obtain the destination address. By default, DNS resolution is a [color=skyblue][url]network traversal[/url][/color] without specific destination address (i.e., a broadcast).\n\nThis means that the traversal will attempt to visit every node attempting to resolve the [color=skyblue][url]domain name[/url][/color]. While this works for a [color=skyblue][url]switch-only[/url][/color] network, the traversal cannot reach a DNS server if it is on a non-default [color=skyblue][url]route[/url][/color] from a router.", "Tower Networking Inc.では、すべてのユーザートラバーサルは宛先アドレスを取得するために[color=skyblue][url]DNS[/url][/color]解決を必要とします。デフォルトでは、DNS解決は特定の宛先アドレスを持たない[color=skyblue][url]ネットワークトラバーサル[/url][/color]（つまりブロードキャスト）です。\n\nこれは、トラバーサルが[color=skyblue][url]ドメイン名[/url][/color]を解決しようとしてすべてのノードを訪問することを意味します。[color=skyblue][url]スイッチのみ[/url][/color]のネットワークでは機能しますが、ルーターのデフォルトでない[color=skyblue][url]経路[/url][/color]にDNSサーバーがある場合、トラバーサルは到達できません。")
t("There are 3 ways to solve this issue:\n\n1. The [color=yellow]default route[/color] can be set to point to a network that always has a DNS server (i.e., [color=7FFFD4]port 1[/color]).\n2. A [color=yellow]designated DNS server address[/color] can be set on [color=orange]ALICE[/color] so that the DNS resolution traversal has a specific destination address.\n3. Place a DNS server on every side of the router.\n\nYou are free to choose how do you want to setup your network. The ideal solution differs depending on the scale and situation. It may also be possible to mix the solutions to create your own unique approach to handle this kinds or problem.", "この問題を解決する方法は3つあります:\n\n1. [color=yellow]デフォルトルート[/color]を常にDNSサーバーがあるネットワーク（つまり[color=7FFFD4]ポート1[/color]）を指すように設定できます。\n2. [color=orange]ALICE[/color]に[color=yellow]指定DNSサーバーアドレス[/color]を設定して、DNS解決トラバーサルに特定の宛先アドレスを持たせることができます。\n3. ルーターの各側にDNSサーバーを配置します。\n\nネットワークのセットアップ方法は自由に選択できます。理想的な解決策は規模や状況によって異なります。独自のアプローチを作成するために解決策を組み合わせることも可能です。")
t("This is the easiest solution. To do this, you only need to configure the default route on the [color=skyblue][url]router[/url][/color] using the [color=skyblue][url]route[/url][/color] routine on [color=skyblue][url]netsh[/url][/color].\n\ncommand: [color=yellow]route default via [color=orange]port1[/color] on [color=magenta]<address of router 1>[/color][/color]", "これは最も簡単な解決策です。[color=skyblue][url]netsh[/url][/color]の[color=skyblue][url]route[/url][/color]ルーチンを使用して、[color=skyblue][url]ルーター[/url][/color]のデフォルトルートを設定するだけです。\n\nコマンド: [color=yellow]route default via [color=orange]port1[/color] on [color=magenta]<ルーター1のアドレス>[/color][/color]")
t("This solution works for small networks but when the number of routers increases, it may become difficult to track the default routing path to a network with a DNS server.", "この解決策は小規模なネットワークでは機能しますが、ルーターの数が増えると、DNSサーバーのあるネットワークへのデフォルトルーティングパスを追跡するのが難しくなる場合があります。")
t("This solution requires configuration on the users and the router. The use of [color=skyblue][url]DHCP[/url][/color] may be necessary to quickly designated DNS server addresses on many users without doing them one by one.\n\nTo use this solution on the example problem, designate a DNS server address with the [color=skyblue][url]net[/url][/color] routine using [color=skyblue][url]netsh[/url][/color].\n\ncommand: [color=yellow]net dns set [color=orange]@dns-1[/color] on [color=magenta]<address of ALICE>[/color][/color]\n\nThen a route for DNS needs to be added to the router using the [color=skyblue][url]route[/url][/color] routine using [color=skyblue][url]netsh[/url][/color].\n\ncommand: [color=yellow]route add [color=orange]@dns-1[/color] via [color=orange]port1[/color] on [color=magenta]<address of router 1>[/color][/color]", "この解決策はユーザーとルーターの設定が必要です。多くのユーザーに一括で指定DNSサーバーアドレスを設定するには、[color=skyblue][url]DHCP[/url][/color]の使用が必要になる場合があります。\n\nこの解決策を例題に適用するには、[color=skyblue][url]netsh[/url][/color]の[color=skyblue][url]net[/url][/color]ルーチンで指定DNSサーバーアドレスを設定します。\n\nコマンド: [color=yellow]net dns set [color=orange]@dns-1[/color] on [color=magenta]<ALICEのアドレス>[/color][/color]\n\n次に、[color=skyblue][url]netsh[/url][/color]の[color=skyblue][url]route[/url][/color]ルーチンを使用して、ルーターにDNS用のルートを追加する必要があります。\n\nコマンド: [color=yellow]route add [color=orange]@dns-1[/color] via [color=orange]port1[/color] on [color=magenta]<ルーター1のアドレス>[/color][/color]")
t("For example, the user \"[color=orange]lumbering-civet[/color]\" is configured to use the address \"[color=orange]@mydns[/color]\" as its DNS server.\n\nThis means that when this user attempts to perform DNS resolution, it will only try to connect to the device/user with the address \"[color=orange]@mydns[/color]\"", "例えば、ユーザー「[color=orange]lumbering-civet[/color]」はDNSサーバーとしてアドレス「[color=orange]@mydns[/color]」を使用するように設定されています。\n\nこれは、このユーザーがDNS解決を実行しようとする際、アドレス「[color=orange]@mydns[/color]」を持つデバイス/ユーザーにのみ接続を試みることを意味します。")
t("This solution can be easily scaled when new routers are added, they just have to point the DNS route back to ROUTER 1 without needing to trace the default route chain.\n\nHowever, it may be infeasible to configure the designated DNS server addresses of many users, therefore, this solution usually requires the help of a [color=skyblue][url]DHCP[/url][/color] server.", "この解決策は新しいルーターが追加された際に容易にスケールできます。新しいルーターはデフォルトルートチェーンをたどる必要なく、DNSルートをルーター1に向けるだけで済みます。\n\nただし、多くのユーザーに指定DNSサーバーアドレスを設定するのは現実的でない場合があるため、この解決策は通常[color=skyblue][url]DHCP[/url][/color]サーバーの助けが必要です。")
t("This solution will work without any network and routing configuration. However, it is expensive to implement and it may be physically difficult to place DNS servers everywhere due to limited power points.\n\nHowever, this solution has another benefit in that DNS traversal traffic is localized. This will halve the amount of traffic across wide network because every user always performs DNS traversals.", "この解決策はネットワークやルーティングの設定なしで動作します。ただし、実装コストが高く、電源コンセントの制限によりDNSサーバーをあらゆる場所に配置するのが物理的に困難な場合があります。\n\nしかし、この解決策にはDNSトラバーサルトラフィックがローカライズされるという別の利点があります。すべてのユーザーが常にDNSトラバーサルを実行するため、広域ネットワーク全体のトラフィック量を半減させることができます。")
t("Notice that in this example, DNS traffic does not pass through ROUTER 1 because each sub-network has its own DNS server.", "この例では、各サブネットワークに独自のDNSサーバーがあるため、DNSトラフィックはルーター1を通過しないことに注目してください。")
t("In Tower Networking Inc., a [color=yellow]network firewall[/color] can be used to filter unwanted traffic (e.g., web scraping, denial-of-service attack) from [color=skyblue][url]malicious users[/url][/color].\n\nPacket filtering is done before the traffic enters the firewall. This means that dropped traffic does not affect the [color=skyblue][url]bandwidth[/url][/color] of the firewall.", "Tower Networking Inc.では、[color=yellow]ネットワークファイアウォール[/color]を使用して、[color=skyblue][url]悪意のあるユーザー[/url][/color]からの不要なトラフィック（例：Webスクレイピング、サービス拒否攻撃）をフィルタリングできます。\n\nパケットフィルタリングはトラフィックがファイアウォールに入る前に行われます。つまり、ドロップされたトラフィックはファイアウォールの[color=skyblue][url]帯域幅[/url][/color]に影響しません。")
t("Firewalls can be configured using the [color=skyblue][url]firewall routine[/url][/color] on the [color=skyblue][url]netsh[/url][/color] application.\n\nA [color=yellow]firewall rule[/color] can be added to allow/deny traversals based on:\n\n1. Source [color=skyblue][url]logical address[/url][/color]\n2. Destination [color=skyblue][url]logical address[/url][/color] (or the lack thereof)\n3. [color=skyblue][url]Traffic types[/url][/color]\n\nWhen a traversal reaches a firewall, the firewall checks all policies in ascending order. If there is an explicit allow/deny policy that matches the traversal attributes, the policy is applied and the traversal is either granted or deny passage through the firewall.\n\nOne must becareful when configuring firewall rules as there is risk of getting locked out (e.g., removing the default allow policy before allowing [color=palegreen]tcp/23[/color] traffic for further configuration using the [color=skyblue][url]firewall routine[/url][/color]).", "ファイアウォールは[color=skyblue][url]netsh[/url][/color]アプリケーションの[color=skyblue][url]firewallルーチン[/url][/color]で設定できます。\n\n[color=yellow]ファイアウォールルール[/color]を追加して、以下に基づいてトラバーサルを許可/拒否できます:\n\n1. 送信元[color=skyblue][url]論理アドレス[/url][/color]\n2. 宛先[color=skyblue][url]論理アドレス[/url][/color]（またはその欠如）\n3. [color=skyblue][url]トラフィックタイプ[/url][/color]\n\nトラバーサルがファイアウォールに到達すると、ファイアウォールはすべてのポリシーを昇順でチェックします。トラバーサルの属性に一致する明示的な許可/拒否ポリシーがある場合、そのポリシーが適用され、トラバーサルの通過が許可または拒否されます。\n\nファイアウォールルールの設定には注意が必要です。ロックアウトされるリスクがあります（例：[color=skyblue][url]firewallルーチン[/url][/color]でさらなる設定のために[color=palegreen]tcp/23[/color]トラフィックを許可する前にデフォルト許可ポリシーを削除する）。")
t("On firewalls, there is a key difference between [color=skyblue][url]hardware address[/url][/color] and [color=skyblue][url]network address[/url][/color]. \n\nFor addresses on policies specified with [color=00FA9A]hardware addresses[/color], [color=yellow]exact matching[/color] is performed. This means the following policy:\n\n[color=orange]allow from 12345 to 56789[/color]\n\nwill grant passageway for traversals that are coming from a device/user that has the hardware address \"[color=00FA9A]12345[/color]\" and has destination hardware address \"[color=00FA9A]56789[/color]\"\n\nFor addresses on policies specified with [color=FF0565]network addresses[/color], [color=yellow]prefix matching[/color] is performed. This means the following policy:\n\n[color=orange]allow from @net1/ to @net2/[/color]\n\nwill grant passageway for traversals that are coming from a device/user that has a network address with prefix \"[color=FF0565]@net1/[/color]\" (e.g., \"[color=FF0565]@net1/alice[/color]\") and has a destination network address with prefix matching \"[color=FF0565]@net2/[/color]\" (e.g., \"[color=FF0565]@net2/server[/color]\").", "ファイアウォールでは、[color=skyblue][url]ハードウェアアドレス[/url][/color]と[color=skyblue][url]ネットワークアドレス[/url][/color]には重要な違いがあります。\n\n[color=00FA9A]ハードウェアアドレス[/color]で指定されたポリシーのアドレスには、[color=yellow]完全一致[/color]が行われます。つまり、以下のポリシー:\n\n[color=orange]allow from 12345 to 56789[/color]\n\nは、ハードウェアアドレス「[color=00FA9A]12345[/color]」を持つデバイス/ユーザーからの、宛先ハードウェアアドレスが「[color=00FA9A]56789[/color]」のトラバーサルの通過を許可します。\n\n[color=FF0565]ネットワークアドレス[/color]で指定されたポリシーのアドレスには、[color=yellow]プレフィックス一致[/color]が行われます。つまり、以下のポリシー:\n\n[color=orange]allow from @net1/ to @net2/[/color]\n\nは、プレフィックス「[color=FF0565]@net1/[/color]」を持つネットワークアドレス（例：「[color=FF0565]@net1/alice[/color]」）のデバイス/ユーザーからの、宛先ネットワークアドレスのプレフィックスが「[color=FF0565]@net2/[/color]」（例：「[color=FF0565]@net2/server[/color]」）に一致するトラバーサルの通過を許可します。")
t("In Tower Networking Inc., [color=00FA9A]hardware addresses[/color] are random [color=yellow]unique addresses[/color] automatically assigned to each network-capable [color=skyblue][url]device[/url][/color] and [color=skyblue][url]users[/url][/color].\n\nHardware addresses are [color=yellow]1 to 5 digits in length[/color]. They are used to reference device and users when running [color=skyblue][url]netsh[/url][/color] routines.\n\n[color=00FA9A]Hardware addresses[/color] are a type of [color=skyblue][url]logical address[/url][/color], along with [color=FF0565][url]network addresses[/url][/color]", "Tower Networking Inc.では、[color=00FA9A]ハードウェアアドレス[/color]はネットワーク対応の[color=skyblue][url]デバイス[/url][/color]と[color=skyblue][url]ユーザー[/url][/color]に自動的に割り当てられるランダムな[color=yellow]一意のアドレス[/color]です。\n\nハードウェアアドレスは[color=yellow]1～5桁[/color]です。[color=skyblue][url]netsh[/url][/color]ルーチンを実行する際にデバイスやユーザーを参照するために使用されます。\n\n[color=00FA9A]ハードウェアアドレス[/color]は[color=FF0565][url]ネットワークアドレス[/url][/color]と並ぶ[color=skyblue][url]論理アドレス[/url][/color]の一種です。")
t("In Tower Networking Inc., a [color=yellow]logical address[/color] (or simply called \"[color=yellow]address[/color]\" or \"[color=yellow]addr[/color]\") is represented as either a [color=00FA9A][url]hardware addresses[/url][/color] or a [color=FF0565][url]network addresses[/url][/color]. These addresses logically refers to a single device or user. In the case of network addresses, a logical address may refer to a group of device or users.\n\nMost [color=skyblue][url]netsh[/url][/color] commands accepts logical addresses as input.", "Tower Networking Inc.では、[color=yellow]論理アドレス[/color]（単に「[color=yellow]アドレス[/color]」や「[color=yellow]addr[/color]」とも呼ばれる）は[color=00FA9A][url]ハードウェアアドレス[/url][/color]または[color=FF0565][url]ネットワークアドレス[/url][/color]として表されます。これらのアドレスは論理的に1つのデバイスまたはユーザーを指します。ネットワークアドレスの場合、論理アドレスはデバイスやユーザーのグループを指すこともあります。\n\nほとんどの[color=skyblue][url]netsh[/url][/color]コマンドは論理アドレスを入力として受け付けます。")
t("In Tower Networking Inc., [color=FF0565]network addresses[/color] are player assigned addresses (a.k.a. a device alias). \n\nNetwork addresses [color=yellow]always begins with the alias symbol @[/color] and is [color=yellow]capped to 9 alpha-numerical characters long[/color]. The special characters dash \"-\", underscore \"_\" and forward slash \"/\" is also allowed in network addresses.\n\nBecause they are player assigned, it is [i]technically[/i] possible for [color=yellow]more than 1 devices to have the same network address[/color].\n\nIt is important to also know that while network addresses are interchangeable with hardware addresses when used in [color=skyblue][url]netsh[/url][/color], they are NOT the interchangeable when it comes to [color=skyblue][url]routing[/url][/color]!\n\nFor example, if a device has hardware address \"[color=00FA9A]12345[/color]\" and is assigned the network address \"[color=FF0565]@sv1[/color]\". If a visitor is trying to visit \"[color=FF0565]@sv1[/color]\" (i.e., obtained from the [color=skyblue][url]DNS[/url][/color] server), a [color=skyblue][url]network route[/url][/color] \"[color=00FA9A]12345[/color] via [color=7FFFD4]port1[/color]\" will NOT work. This is because when the visitor's traffic reaches the router, the router does not know that \"[color=00FA9A]12345[/color]\" and  \"[color=FF0565]@sv1[/color]\" are the same. There are 2 ways to resolve this problem, that is to either:\n\n1. Use network address in the route configuration (e.g., \"[color=FF0565]@sv1[/color] via [color=7FFFD4]port1[/color]\").\n2. Set the DNS entry mapping to the hardware address \"[color=00FA9A]12345[/color]\".\n\nConcisely, there are no correlation between a device's hardware and network address.", "Tower Networking Inc.では、[color=FF0565]ネットワークアドレス[/color]はプレイヤーが割り当てるアドレス（デバイスエイリアス）です。\n\nネットワークアドレスは[color=yellow]常にエイリアス記号@で始まり[/color]、[color=yellow]9文字以下の英数字[/color]に制限されます。ダッシュ「-」、アンダースコア「_」、スラッシュ「/」も使用できます。\n\nプレイヤーが割り当てるため、[i]技術的には[/i][color=yellow]複数のデバイスが同じネットワークアドレスを持つ[/color]ことが可能です。\n\n[color=skyblue][url]netsh[/url][/color]で使用する際、ネットワークアドレスはハードウェアアドレスと互換性がありますが、[color=skyblue][url]ルーティング[/url][/color]に関しては互換性がないことを理解しておくことが重要です！\n\n例えば、デバイスのハードウェアアドレスが「[color=00FA9A]12345[/color]」で、ネットワークアドレス「[color=FF0565]@sv1[/color]」が割り当てられている場合、訪問者が「[color=FF0565]@sv1[/color]」（つまり[color=skyblue][url]DNS[/url][/color]サーバーから取得）を訪問しようとしているとき、[color=skyblue][url]ネットワークルート[/url][/color]「[color=00FA9A]12345[/color] via [color=7FFFD4]port1[/color]」は機能しません。これは、訪問者のトラフィックがルーターに到達した際、ルーターは「[color=00FA9A]12345[/color]」と「[color=FF0565]@sv1[/color]」が同じものであることを知らないためです。この問題を解決するには2つの方法があります:\n\n1. ルート設定にネットワークアドレスを使用する（例：「[color=FF0565]@sv1[/color] via [color=7FFFD4]port1[/color]」）。\n2. DNSエントリのマッピングをハードウェアアドレス「[color=00FA9A]12345[/color]」に設定する。\n\n簡潔に言えば、デバイスのハードウェアアドレスとネットワークアドレスの間に相関関係はありません。")
t("[color=yellow]The game can be played without using any network addresses[/color]. Every routine used in [color=skyblue][url]netsh[/url][/color] allows use of either a [color=00FA9A][url]hardware address[/url][/color] or a network addresses interchangeably.\n\nHowever, network addresses are an important part of the game for several reasons.", "[color=yellow]ネットワークアドレスを使用せずにゲームをプレイすることもできます[/color]。[color=skyblue][url]netsh[/url][/color]で使用されるすべてのルーチンは、[color=00FA9A][url]ハードウェアアドレス[/url][/color]とネットワークアドレスのどちらでも互換的に使用できます。\n\nただし、ネットワークアドレスはいくつかの理由でゲームの重要な要素です。")
t("Network addresses can be assigned using the [color=skyblue][url]net routine[/url][/color].", "ネットワークアドレスは[color=skyblue][url]netルーチン[/url][/color]を使用して割り当てることができます。")
t("When [color=skyblue][url]routers[/url][/color] are used, network addresses can be used to group devices and users as to simplify the routing table configuration. You can also use assign meaning or other labels to devices and users to help better track what's the purpose (or where) is the device.\n\nFor instance, it may be easier to tell that \"[color=FF0565]@dns-1[/color]\" is a DNS server than its randomly generated hardware address \"[color=00FA9A]12381[/color]\".\n\nAdditionally, it is quite easy to know that \"[color=FF0565]@f1/server[/color]\" is a server on floor 1 instead of looking for it physically.\n\nThe following diagram shows an example network with nodes assigned with network addresses. Notice that the route table can be easily made to handle traffic betweenthe nodes.", "[color=skyblue][url]ルーター[/url][/color]を使用する場合、ネットワークアドレスを使ってデバイスやユーザーをグループ化し、ルーティングテーブルの設定を簡素化できます。また、デバイスやユーザーに意味やラベルを割り当てて、その目的や場所を追跡しやすくすることもできます。\n\n例えば、ランダムに生成されたハードウェアアドレス「[color=00FA9A]12381[/color]」よりも、「[color=FF0565]@dns-1[/color]」がDNSサーバーであることの方が分かりやすいでしょう。\n\nさらに、「[color=FF0565]@f1/server[/color]」が1階のサーバーであることは、物理的に探すよりも簡単に分かります。\n\n以下の図は、ネットワークアドレスが割り当てられたノードを持つネットワーク例を示しています。ルートテーブルがノード間のトラフィックを処理するために容易に作成できることに注目してください。")
t("For example, to run a large-scale DNS service, an option could be to assign a common network address (e.g., \"[color=FF0565]@bigdns[/color]\") to multiple servers running the DNS server programs. These servers can then be placed in different locations to localize the DNS traffic. User's can then be assigned \"[color=FF0565]@bigdns[/color]\" as their [color=skyblue][url]designated DNS server[/url][/color], which can then distribute DNS traffic load across the network.", "例えば、大規模なDNSサービスを運用するために、複数のDNSサーバープログラムを実行しているサーバーに共通のネットワークアドレス（例：「[color=FF0565]@bigdns[/color]」）を割り当てる方法があります。これらのサーバーを異なる場所に配置してDNSトラフィックをローカライズできます。ユーザーには[color=skyblue][url]指定DNSサーバー[/url][/color]として「[color=FF0565]@bigdns[/color]」を割り当てることで、DNSトラフィック負荷をネットワーク全体に分散できます。")
t("In Tower Networking Inc., a [color=yellow]network router[/color] can perform route traversals into a specific link, which [color=yellow]reduces unnecessary visits[/color] from a [color=skyblue][url]network traversal[/url][/color]. A router is defined by a routing table, which is basically a list of destination and the ports in which the traversal should take to reach them.\n\nOne can think of routers in this game as directional sign-boards for network traffic.\n\n[color=skyblue][url]devices[/url][/color]/[color=skyblue][url]users[/url][/color] connected with a router can perform [color=skyblue][url]network traversals[/url][/color] through the router by the following rules:\n\n1. If the traversal does not have a specific destination address, it goes through the [color=yellow] default[/color] route.\n2. If the traversal has a specific destination [color=skyblue][url]hardware address[/url][/color] or [color=skyblue][url]network address[/url][/color], but the address is not matched in the routing table, it goes through the [color=yellow] default [/color]route.\n3. If the traversal has a specific destination [color=skyblue][url]hardware address[/url][/color] and [color=yellow]an exact destination address[/color] is matched in the routing table, it goes through the specified route.\n4. If the traversal has a specific destination [color=skyblue][url]network address[/url][/color] and [color=yellow]a prefix of the destination address[/color] is matched in the routing table, it goes through the specified route.\n5. If the traversal has a specific destination [color=skyblue][url]network address[/url][/color] and [color=yellow]multiple prefixes of the address is matched[/color] in the routing table, it goes through the route specified by the [color=yellow]longest prefix[/color].\n\nLet's understand the rules by examples.", "Tower Networking Inc.では、[color=yellow]ネットワークルーター[/color]はトラバーサルを特定のリンクにルーティングでき、[color=skyblue][url]ネットワークトラバーサル[/url][/color]からの[color=yellow]不要な訪問を削減[/color]します。ルーターはルーティングテーブルによって定義され、基本的に宛先とトラバーサルが到達するために通過すべきポートのリストです。\n\nこのゲームでは、ルーターをネットワークトラフィックの方向案内板と考えることができます。\n\nルーターで接続された[color=skyblue][url]デバイス[/url][/color]/[color=skyblue][url]ユーザー[/url][/color]は、以下のルールに従ってルーターを通じた[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行できます:\n\n1. トラバーサルに特定の宛先アドレスがない場合、[color=yellow]デフォルト[/color]ルートを通ります。\n2. トラバーサルに特定の宛先[color=skyblue][url]ハードウェアアドレス[/url][/color]または[color=skyblue][url]ネットワークアドレス[/url][/color]があるが、ルーティングテーブルにアドレスが一致しない場合、[color=yellow]デフォルト[/color]ルートを通ります。\n3. トラバーサルに特定の宛先[color=skyblue][url]ハードウェアアドレス[/url][/color]があり、ルーティングテーブルで[color=yellow]完全一致する宛先アドレス[/color]がある場合、指定されたルートを通ります。\n4. トラバーサルに特定の宛先[color=skyblue][url]ネットワークアドレス[/url][/color]があり、ルーティングテーブルで[color=yellow]宛先アドレスのプレフィックス[/color]が一致する場合、指定されたルートを通ります。\n5. トラバーサルに特定の宛先[color=skyblue][url]ネットワークアドレス[/url][/color]があり、ルーティングテーブルで[color=yellow]複数のプレフィックスが一致[/color]する場合、[color=yellow]最長プレフィックス[/color]で指定されたルートを通ります。\n\n例を使ってルールを理解しましょう。")
t("Notice the following:\n\n1. The first traversal is a traversal [color=yellow]without specific destination address[/color]; the are no designated DNS address for [color=orange]ALICE[/color]. Therefore, the [color=yellow]default[/color] entry is used, sending the traversal towards [color=7FFFD4]port 1[/color].\n2., The second traversal uses the address obtained from the DNS resolution phase, which sets it at [color=00FA9A]12345[/color]. This is a traversal [color=yellow]with a specific destination address[/color]. In the example's case, a route entry for [color=00FA9A]12345[/color] exists and sends the traversal towards [color=7FFFD4]port 2[/color].\n3. If ROUTER 1 is a [color=skyblue][url]network switch[/url][/color], during the second traversal, 1 unnecessary visit is made because the traversal would have first tried [color=7FFFD4]port 1[/color] being the lower port.\n4. Therefore, the use of router has optimized the traversal, reducing unnecessary bandwidth usage.\n\nNow let's look at the examples for all the cases.", "以下に注目してください:\n\n1. 最初のトラバーサルは[color=yellow]特定の宛先アドレスのない[/color]トラバーサルです。[color=orange]ALICE[/color]に指定DNSアドレスがありません。そのため[color=yellow]default[/color]エントリが使用され、トラバーサルは[color=7FFFD4]ポート1[/color]に送られます。\n2. 2番目のトラバーサルはDNS解決フェーズで取得したアドレスを使用し、[color=00FA9A]12345[/color]に設定されます。これは[color=yellow]特定の宛先アドレスを持つ[/color]トラバーサルです。この例では、[color=00FA9A]12345[/color]のルートエントリが存在し、トラバーサルは[color=7FFFD4]ポート2[/color]に送られます。\n3. もしルーター1が[color=skyblue][url]ネットワークスイッチ[/url][/color]だった場合、2番目のトラバーサルでは、より低いポートである[color=7FFFD4]ポート1[/color]を先に試すため、1回の不要な訪問が発生します。\n4. したがって、ルーターの使用によりトラバーサルが最適化され、不要な帯域幅の使用が削減されます。\n\n次に、すべてのケースの例を見てみましょう。")
t("Traversal without destination address always uses the [color=yellow]default[/color] route on the router.", "宛先アドレスのないトラバーサルは、常にルーターの[color=yellow]default[/color]ルートを使用します。")
t("In the case of [color=skyblue][url]hardware address[/url][/color], [color=yellow]an exact match[/color] is required to use the route.\n\nIn this example where the hardware address is [color=orange]12345[/color], the second route in the table is used, sending the traversal down [color=7FFFD4]port 2[/color].", "[color=skyblue][url]ハードウェアアドレス[/url][/color]の場合、ルートを使用するには[color=yellow]完全一致[/color]が必要です。\n\nこの例では、ハードウェアアドレスが[color=orange]12345[/color]なので、テーブルの2番目のルートが使用され、トラバーサルは[color=7FFFD4]ポート2[/color]に送られます。")
t("In this example where the hardware address is [color=orange]123[/color], the [color=yellow]default[/color] route in the table is used because none of the routes are matched. This will send the traversal down [color=7FFFD4]port 3[/color].", "この例では、ハードウェアアドレスが[color=orange]123[/color]なので、どのルートも一致しないため、テーブルの[color=yellow]default[/color]ルートが使用されます。これにより、トラバーサルは[color=7FFFD4]ポート3[/color]に送られます。")
t("In the case of [color=skyblue][url]network address[/url][/color], the route with the  [color=yellow]longest prefix match[/color] chosen.\n\nIn this example where the network address is [color=orange]@dns[/color], the third route in the table is longest matching prefix, sending the traversal down [color=7FFFD4]port 1[/color]. The route [color=orange]@dns/s-1[/color] may be a longest prefix, but it is not a prefix of [color=orange]@dns[/color].", "[color=skyblue][url]ネットワークアドレス[/url][/color]の場合、[color=yellow]最長プレフィックス一致[/color]のルートが選択されます。\n\nこの例では、ネットワークアドレスが[color=orange]@dns[/color]なので、テーブルの3番目のルートが最長一致プレフィックスとなり、トラバーサルは[color=7FFFD4]ポート1[/color]に送られます。ルート[color=orange]@dns/s-1[/color]はより長いプレフィックスかもしれませんが、[color=orange]@dns[/color]のプレフィックスではありません。")
t("In this example where the network address is [color=orange]@dns-123[/color], the third route in the table is still longest matching prefix, sending the traversal down [color=7FFFD4]port 1[/color]. This means that ANY destination network address that starts with [color=orange]@dns[/color] AND not starting with [color=orange]@dns/s-1[/color] gets routed through [color=7FFFD4]port 1[/color].", "この例では、ネットワークアドレスが[color=orange]@dns-123[/color]なので、テーブルの3番目のルートが依然として最長一致プレフィックスとなり、トラバーサルは[color=7FFFD4]ポート1[/color]に送られます。つまり、[color=orange]@dns[/color]で始まり、かつ[color=orange]@dns/s-1[/color]で始まらない宛先ネットワークアドレスはすべて[color=7FFFD4]ポート1[/color]を通じてルーティングされます。")
t("In this example where the network address is [color=orange]@dns/s-123[/color], the fourth route in the table is the longest matching prefix, sending the traversal down [color=7FFFD4]port 2[/color]. Even if [color=orange]@dns/s-123[/color] also has a prefix of [color=orange]@dns[/color], only the [color=yellow]longest match[/color] is chosen.", "この例では、ネットワークアドレスが[color=orange]@dns/s-123[/color]なので、テーブルの4番目のルートが最長一致プレフィックスとなり、トラバーサルは[color=7FFFD4]ポート2[/color]に送られます。[color=orange]@dns/s-123[/color]は[color=orange]@dns[/color]もプレフィックスとして持ちますが、[color=yellow]最長一致[/color]のみが選択されます。")
t("In this example where the network address is [color=orange]@d[/color], no matching prefix is found in the route table, sending the traversal down the default route via [color=7FFFD4]port 3[/color].", "この例では、ネットワークアドレスが[color=orange]@d[/color]なので、ルートテーブルに一致するプレフィックスが見つからず、トラバーサルはデフォルトルート経由で[color=7FFFD4]ポート3[/color]に送られます。")
t("As the number of users in your network increases and more services are added, the size of your network will expand until at a point where [color=skyblue][url]bandwidth usage[/url][/color] becomes an issue (unless if you're playing on easy mode).\n\nConsider a network where only [color=skyblue][url]network switches[/url][/color] are used.", "ネットワーク上のユーザー数が増え、サービスが追加されるにつれて、ネットワークの規模は拡大し、ある時点で[color=skyblue][url]帯域幅の使用[/url][/color]が問題になります（イージーモードでプレイしている場合を除く）。\n\n[color=skyblue][url]ネットワークスイッチ[/url][/color]のみを使用したネットワークを考えてみましょう。")
t("For [color=orange]ALICE[/color] to visit [color=orange]BOB[/color], all nodes colored [color=yellow]yellow[/color] are unnecessarily visited (see [color=skyblue][url]network switching[/url][/color] for details), wasting bandwidth on the switches and the endpoints.\n\nWhen a device's [color=skyblue][url]bandwidth is exhausted[/url][/color], they stop allowing traversals, causing impact to other users and functionality of the network.\n\nNow consider if we strategically place 2 routers in the highly interconnected nodes (i.e., core backbone of the network). The number of unnecessarily visited nodes can be cut down to a minimum.", "[color=orange]ALICE[/color]が[color=orange]BOB[/color]を訪問するために、[color=yellow]黄色[/color]で表示されたすべてのノードが不必要に訪問されます（詳細は[color=skyblue][url]ネットワークスイッチング[/url][/color]を参照）。帯域幅が浪費されます。\n\nデバイスの[color=skyblue][url]帯域幅が枯渇[/url][/color]すると、トラバーサルを許可しなくなり、他のユーザーやネットワークの機能に影響を与えます。\n\nここで、高度に相互接続されたノード（つまりネットワークのコアバックボーン）に2台のルーターを戦略的に配置した場合を考えてみましょう。不要に訪問されるノード数を最小限に抑えることができます。")
t("In Tower Networking Inc., a [color=yellow]network switch[/color] is a low-cost and inefficient way to interconnect to facilitate [color=skyblue][url]network traversals[/url][/color]. [color=yellow]They require NO configuration and will work off-the-shelf[/color].\n\n[color=skyblue][url]devices[/url][/color]/[color=skyblue][url]users[/url][/color] connected with a switch can perform [color=skyblue][url]network traversals[/url][/color] through the switch.\n\n[b]Note to seasoned experts[/b]: The networking mechanism differs from real-world, where network switches uses CAM tables and spanning-tree protocols to build the network connectivity graph. In this game, switches just functions as a hub because the link layer is not simulated. No ARP happens on the devices!\n\nTo help understand how switches work. We consider an example user [color=orange]ALICE[/color] who always wants to reach [color=orange]BOB[/color]. You may want to read up on [color=skyblue][url]network traversals[/url][/color] so you can easily follow the examples.", "Tower Networking Inc.では、[color=yellow]ネットワークスイッチ[/color]は[color=skyblue][url]ネットワークトラバーサル[/url][/color]を容易にするための低コストで非効率的な相互接続方法です。[color=yellow]設定不要でそのまま使用できます[/color]。\n\nスイッチで接続された[color=skyblue][url]デバイス[/url][/color]/[color=skyblue][url]ユーザー[/url][/color]は、スイッチを通じた[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行できます。\n\n[b]経験豊富な方への注意[/b]: このゲームのネットワークメカニズムは実世界とは異なります。実世界ではネットワークスイッチはCAMテーブルとスパニングツリープロトコルを使用してネットワーク接続グラフを構築しますが、このゲームではスイッチはリンク層がシミュレートされていないためハブとして機能します。デバイス上でARPは発生しません！\n\nスイッチの動作を理解するために、常に[color=orange]BOB[/color]に到達したいユーザー[color=orange]ALICE[/color]の例を考えます。例を簡単に追えるよう、[color=skyblue][url]ネットワークトラバーサル[/url][/color]について先に読んでおくことをお勧めします。")
t("From the sample network example, note the following:\n\n1. The traversal always starts from the lowest port when it reaches a switch.\n2. [color=orange]DAVE[/color] did not get visited because it is on a higher port; the traversal has ended when it successfully reached [color=orange]BOB[/color] on port.\n\nSwitches can be daisy-chained together.", "サンプルネットワークの例から、以下に注目してください:\n\n1. トラバーサルはスイッチに到達すると常に最も低いポートから開始します。\n2. [color=orange]DAVE[/color]はより高いポートにいるため訪問されませんでした。トラバーサルはポート上で[color=orange]BOB[/color]に正常に到達した時点で終了しました。\n\nスイッチはデイジーチェーン接続が可能です。")
t("Observe the following from the daisy chain example:\n\n1. When the destination is [color=orange]BOB[/color], despite being on SWITCH 3, which is nearer to [color=orange]ALICE[/color] compared to [color=orange]ECHO[/color], [color=orange]ECHO[/color] gets visited first because it is on the path via a lower port.\n2. When the destination is [color=orange]DAVE[/color], despite being 2 hops away from [color=orange]ALICE[/color], it gets visited last. The traversal spans the entire network.\n3. This means that [color=yellow]every node connected through the lower ports on a switch is visited first before the traversal can reach a higher port destination[/color].\n\nObservation 3 tells us that switches, although simple to use, must be carefully used in a large network to prevent unnecessary traversals. If the ports are simply connected, then a switch network becomes very inefficient when the network is large.\n\nConsider the following network:", "デイジーチェーンの例から以下を観察してください:\n\n1. 宛先が[color=orange]BOB[/color]の場合、スイッチ3にあり[color=orange]ECHO[/color]より[color=orange]ALICE[/color]に近いにもかかわらず、[color=orange]ECHO[/color]がより低いポート経由のパス上にあるため先に訪問されます。\n2. 宛先が[color=orange]DAVE[/color]の場合、[color=orange]ALICE[/color]から2ホップ離れているにもかかわらず、最後に訪問されます。トラバーサルはネットワーク全体に及びます。\n3. つまり、[color=yellow]スイッチの低いポートを通じて接続されたすべてのノードは、トラバーサルが高いポートの宛先に到達できるようになる前にまず訪問されます[/color]。\n\n観察3から、スイッチは使用が簡単ですが、不要なトラバーサルを防ぐために大規模ネットワークでは慎重に使用する必要があることが分かります。ポートが単純に接続されると、大規模ネットワークではスイッチネットワークは非常に非効率的になります。\n\n以下のネットワークを考えてみましょう:")
t("Our prior observation tells us that in order for [color=orange]ALICE[/color] to reach the destination, all the nodes colored in [color=yellow]yellow[/color] are visited (recall that lower ports are always visited first).\n\nWith a switch-only setup, the [color=skyblue][url]bandwidth[/url][/color] of the entire network will be exhausted fast because of the unnecessary visits.", "先ほどの観察から、[color=orange]ALICE[/color]が宛先に到達するために、[color=yellow]黄色[/color]で示されたすべてのノードが訪問されることが分かります（低いポートが常に先に訪問されることを思い出してください）。\n\nスイッチのみのセットアップでは、不要な訪問によりネットワーク全体の[color=skyblue][url]帯域幅[/url][/color]がすぐに枯渇します。")
t("In Tower Networking Inc., a [color=yellow]network tap[/color] can be used to inspect traffic passing through a device. Tapping is useful because it can help uncover misconfiguration and unexpected behaviors coming from users and devices.\n\nUnlike the [color=skyblue][url]watch routine[/url][/color], which has limited view on the port traffic statistics, network tapping can see [color=skyblue][url]traffic types[/url][/color] of [color=skyblue][url]network traversals[/url][/color] as they flow through the tap.\n\nNetwork tapping can be done with the [color=skyblue][url]pcap routine[/url][/color].", "Tower Networking Inc.では、[color=yellow]ネットワークタップ[/color]を使用してデバイスを通過するトラフィックを検査できます。タッピングは設定ミスやユーザー・デバイスからの予期しない動作を発見するのに役立ちます。\n\nポートトラフィック統計の限定的なビューしか持たない[color=skyblue][url]watchルーチン[/url][/color]とは異なり、ネットワークタッピングではタップを流れる[color=skyblue][url]ネットワークトラバーサル[/url][/color]の[color=skyblue][url]トラフィックタイプ[/url][/color]を確認できます。\n\nネットワークタッピングは[color=skyblue][url]pcapルーチン[/url][/color]で実行できます。")
t("In Tower Networking Inc., each [color=skyblue][url]network traversal[/url][/color] has a [color=yellow]traffic type[/color]. Traffic types can only be seen using a [color=skyblue][url]network tap[/url][/color] and can be blocked or allowed using a [color=skyblue][url]network firewall[/url][/color].\n\nHere are a few example traffic types that are generally used by traversals:\n\n[color=palegreen]tcp/23[/color] - This is used by various [color=skyblue][url]debuggers[/url][/color] such as [color=skyblue][url]net routine[/url][/color], [color=skyblue][url]program routine[/url][/color] to configure devices.\n[color=palegreen]udp/53[/color] - [color=skyblue][url]DNS[/url][/color] traffic.\n[color=palegreen]tcp/80[/color] - Domestic [color=skyblue][url]services[/url][/color]\n[color=palegreen]udp/67[/color] - [color=skyblue][url]DHCP[/url][/color] traffic\n \nThere are many other traffic types that may be used by [color=skyblue][url]users[/url][/color]. Some of the traffic types may be [color=skyblue][url]malicious[/url][/color].", "Tower Networking Inc.では、各[color=skyblue][url]ネットワークトラバーサル[/url][/color]には[color=yellow]トラフィックタイプ[/color]があります。トラフィックタイプは[color=skyblue][url]ネットワークタップ[/url][/color]でのみ確認でき、[color=skyblue][url]ネットワークファイアウォール[/url][/color]でブロックまたは許可できます。\n\n以下はトラバーサルで一般的に使用されるトラフィックタイプの例です:\n\n[color=palegreen]tcp/23[/color] - [color=skyblue][url]netルーチン[/url][/color]や[color=skyblue][url]programルーチン[/url][/color]などの各種[color=skyblue][url]デバッガー[/url][/color]がデバイスの設定に使用します。\n[color=palegreen]udp/53[/color] - [color=skyblue][url]DNS[/url][/color]トラフィック。\n[color=palegreen]tcp/80[/color] - 一般[color=skyblue][url]サービス[/url][/color]\n[color=palegreen]udp/67[/color] - [color=skyblue][url]DHCP[/url][/color]トラフィック\n \n[color=skyblue][url]ユーザー[/url][/color]が使用する他の多くのトラフィックタイプがあります。一部のトラフィックタイプは[color=skyblue][url]悪意のある[/url][/color]ものかもしれません。")
t("In Tower Networking Inc., device and users performs [color=yellow]network traversal[/color] to consume/convert [color=lightsalmon][url]uses[/url][/color]. Simply put, a network traversal is a \"network request\" from a consumer.\n\nWhen a device/user attempts to connect, a [s]Breadth-first search (BFS)[/s] [color=red](This behavior is changed in 0.8.24)[/color] [color=yellow]Depth-first search (DFS)[/color] graph traversal is performed with the source as the root of the graph. Let's see how this works with an example. Consider the following sample network.", "Tower Networking Inc.では、デバイスとユーザーは[color=lightsalmon][url]USE[/url][/color]を消費/変換するために[color=yellow]ネットワークトラバーサル[/color]を実行します。簡単に言えば、ネットワークトラバーサルはコンシューマーからの「ネットワークリクエスト」です。\n\nデバイス/ユーザーが接続を試みると、ソースをグラフのルートとして[s]幅優先探索 (BFS)[/s] [color=red]（この動作は0.8.24で変更されました）[/color] [color=yellow]深さ優先探索 (DFS)[/color]グラフトラバーサルが実行されます。例を使ってこの仕組みを見てみましょう。以下のサンプルネットワークを考えます。")
t("In this network, [color=orange]ALICE[/color] is a [color=skyblue][url]consumer[/url][/color] and wants to access [color=skyblue][url]services[/url][/color]  offered by [color=orange]NEWS COMPANY[/color].\n\n[color=orange]ALICE[/color] first needs to access any [color=skyblue][url]DNS[/url][/color] server to resolve the domain name of the service into a [color=skyblue][url]logical address[/url][/color]. To do this, [color=orange]ALICE[/color] performs a traversal to consume the [color=skyblue][url]use[/url][/color] [color=lightsalmon][reply-dns-queries][/color] WITHOUT any specific destination in mind.", "このネットワークでは、[color=orange]ALICE[/color]は[color=skyblue][url]コンシューマー[/url][/color]で、[color=orange]NEWS COMPANY[/color]が提供する[color=skyblue][url]サービス[/url][/color]にアクセスしたいと考えています。\n\n[color=orange]ALICE[/color]はまず、サービスのドメイン名を[color=skyblue][url]論理アドレス[/url][/color]に解決するために[color=skyblue][url]DNS[/url][/color]サーバーにアクセスする必要があります。そのため、[color=orange]ALICE[/color]は特定の宛先を指定せずに[color=skyblue][url]USE[/url][/color] [color=lightsalmon][reply-dns-queries][/color]を消費するトラバーサルを実行します。")
t("Using the address gotten from the DNS server, [color=orange]ALICE[/color] then performs another traversal to consume uses for the service [color=lightpink]usefulnet.org[/color] on a specific [color=skyblue][url]hardware-address[/url][/color] [color=00FA9A]12345[/color].", "DNSサーバーから取得したアドレスを使用して、[color=orange]ALICE[/color]はサービス[color=lightpink]usefulnet.org[/color]のUSEを消費するため、特定の[color=skyblue][url]ハードウェアアドレス[/url][/color] [color=00FA9A]12345[/color]に対して別のトラバーサルを実行します。")
t("[color=orange]ALICE[/color] was able to successfully access the service hosted on [color=orange]NEWS COMPANY[/color].\n\nNote the following:\n1. The DFS traversal [color=yellow]always[/color] starts from the lowest port from any device.\n2. This example only demonstrates that how [color=orange]ALICE[/color] was able to [color=yellow]reach[/color] [color=orange]NEWS COMPANY[/color]. It may be the case that [color=orange]NEWS COMPANY[/color] does not have sufficient [color=skyblue][url]uses[/url][/color] available left for [color=orange]ALICE[/color] to consume (e.g., overloaded by other [color=skyblue][url]consumers[/url][/color], under DDoS attacks).\n3. If the [color=skyblue][url]DNS[/url][/color] mapping is [color=red]wrong[/color], the [color=yellow]destination address[/color] obtained by [color=orange]ALICE[/color] may cause it to miss [color=orange]NEWS COMPANY[/color] even if it has the compatible [color=skyblue][url]use[/url][/color].\n\nFrom this example, we see 2 main types of network traversals, which are traversal for consumption [color=yellow]with[/color] or [color=yellow]without[/color] any specific destination address.", "[color=orange]ALICE[/color]は[color=orange]NEWS COMPANY[/color]でホストされているサービスに正常にアクセスできました。\n\n以下に注目してください:\n1. DFSトラバーサルは[color=yellow]常に[/color]任意のデバイスの最も低いポートから開始します。\n2. この例は、[color=orange]ALICE[/color]が[color=orange]NEWS COMPANY[/color]に[color=yellow]到達[/color]できた方法のみを示しています。[color=orange]NEWS COMPANY[/color]に[color=orange]ALICE[/color]が消費するための[color=skyblue][url]USE[/url][/color]が十分に残っていない場合もあります（例：他の[color=skyblue][url]コンシューマー[/url][/color]による過負荷、DDoS攻撃）。\n3. [color=skyblue][url]DNS[/url][/color]マッピングが[color=red]間違っている[/color]場合、[color=orange]ALICE[/color]が取得した[color=yellow]宛先アドレス[/color]により、互換性のある[color=skyblue][url]USE[/url][/color]があっても[color=orange]NEWS COMPANY[/color]を見逃す可能性があります。\n\nこの例から、ネットワークトラバーサルには主に2つのタイプがあることが分かります。特定の宛先アドレス[color=yellow]あり[/color]または[color=yellow]なし[/color]の消費トラバーサルです。")
t("In a sense, this traversal type functions like a \"[color=yellow]broadcast[/color]\". The traversal stops when the intent of the request (i.e., to consume a use) is achieved. Examples of this kinds of traversals include:\n\n1. [color=skyblue][url]Undesignated DNS[/url][/color] resolution.\n2. [color=skyblue][url]DHCP[/url][/color] request.\n3. Network [color=skyblue][url]scan[/url][/color] routines using the Debugger.\n\nThese traversals will always choose the \"default\" route when approaching a [color=skyblue][url]router[/url][/color]. They are also matched by [color=yellow]Destination: Any[/color] rules when approaching a [color=skyblue][url]firewall[/url][/color].\n\nThe following is a traversal without any specific address example: [color=orange]ALICE[/color] performs a DHCP request (to automatically set a designated DNS server address and a network address).", "ある意味、このトラバーサルタイプは「[color=yellow]ブロードキャスト[/color]」のように機能します。トラバーサルはリクエストの目的（つまりUSEの消費）が達成されると停止します。この種のトラバーサルの例には以下があります:\n\n1. [color=skyblue][url]未指定DNS[/url][/color]解決。\n2. [color=skyblue][url]DHCP[/url][/color]リクエスト。\n3. デバッガーを使用したネットワーク[color=skyblue][url]scan[/url][/color]ルーチン。\n\nこれらのトラバーサルは[color=skyblue][url]ルーター[/url][/color]に近づくと常に「default」ルートを選択します。また、[color=skyblue][url]ファイアウォール[/url][/color]に近づくと[color=yellow]Destination: Any[/color]ルールに一致します。\n\n以下は、特定のアドレスのないトラバーサルの例です: [color=orange]ALICE[/color]がDHCPリクエスト（指定DNSサーバーアドレスとネットワークアドレスを自動的に設定するため）を実行します。")
t("Notice the following:\n\n1. The traversal stops after consuming successfully from DHCP server 1.\n2. The are no traffic for DNS server and DHCP server 2, their network bandwidth is not affected.\n3. News Company gets visited because it was in a lower port, even if does not have compatible uses.\n\nLet's consider what happens when DHCP server 1 is down (e.g., under heavy load, affected by malware, power malfunction).", "以下に注目してください:\n\n1. トラバーサルはDHCPサーバー1からの消費に成功した後に停止します。\n2. DNSサーバーとDHCPサーバー2にはトラフィックがなく、ネットワーク帯域幅は影響を受けません。\n3. News Companyは互換性のあるUSEを持っていなくても、より低いポートにあったため訪問されます。\n\nDHCPサーバー1がダウンした場合（例：高負荷、マルウェアの影響、電源障害）に何が起こるか考えてみましょう。")
t("As you would expect, [color=orange]ALICE[/color] would consume from DHCP server 2 instead. In this case, the traversal traffic also \"hits\" DNS server, which will reduces the available bandwidth.", "予想通り、[color=orange]ALICE[/color]は代わりにDHCPサーバー2から消費します。この場合、トラバーサルトラフィックはDNSサーバーにも「到達」し、利用可能な帯域幅が減少します。")
t("This traversal requires the [color=yellow]destination address[/color] to first be [color=yellow]MATCHED[/color] before the intent of the traversal can be achieved. This address functions like a \"[color=yellow]unicast[/color]\" for [color=skyblue][url]hardware addresses[/url][/color] and may function like a \"[color=yellow]multicast[/color]\" for [color=skyblue][url]network addresses[/url][/color].\n\nExamples of specific address traversals are:\n\n1. [color=skyblue][url]ping[/url][/color] or [color=skyblue][url]trace[/url][/color] routines using the Debugger.\n2. User accessing a service AFTER DNS resolution.\n3. [color=skyblue][url]Designated DNS[/url][/color] resolution.\n\nConsider the example to help better understand: [color=orange]ALICE[/color] obtained hardware address [color=00FA9A]12345[/color] to consume use [color=lightsalmon][read-text,post-text][/color] for the service [color=lightpink]pearlforum.net[/color].", "このトラバーサルでは、トラバーサルの目的を達成する前に[color=yellow]宛先アドレス[/color]がまず[color=yellow]一致[/color]する必要があります。このアドレスは[color=skyblue][url]ハードウェアアドレス[/url][/color]に対しては「[color=yellow]ユニキャスト[/color]」として機能し、[color=skyblue][url]ネットワークアドレス[/url][/color]に対しては「[color=yellow]マルチキャスト[/color]」として機能する場合があります。\n\n特定アドレストラバーサルの例には以下があります:\n\n1. デバッガーを使用した[color=skyblue][url]ping[/url][/color]または[color=skyblue][url]trace[/url][/color]ルーチン。\n2. DNS解決後のユーザーによるサービスアクセス。\n3. [color=skyblue][url]指定DNS[/url][/color]解決。\n\n理解を深めるために例を考えましょう: [color=orange]ALICE[/color]はハードウェアアドレス[color=00FA9A]12345[/color]を取得し、サービス[color=lightpink]pearlforum.net[/color]のUSE [color=lightsalmon][read-text,post-text][/color]を消費しようとしています。")
t("Notice the following:\n\n1. Even if Elle's forum has compatible uses, [color=orange]ALICE[/color] does not consume from it because the destination address does not match.\n2. The nature of DFS means that [color=orange]ALICE[/color] will traverse deeper into the graph first before trying SWITCH 1's immediate neighbor on port 2.\n\nNow let's consider an example with [color=skyblue][url]network addresses[/url][/color].", "以下に注目してください:\n\n1. Elleのフォーラムに互換性のあるUSEがあっても、宛先アドレスが一致しないため[color=orange]ALICE[/color]はそこから消費しません。\n2. DFSの性質上、[color=orange]ALICE[/color]はスイッチ1のポート2の直接の隣接ノードを試す前に、グラフの奥深くまでトラバーサルします。\n\n次に[color=skyblue][url]ネットワークアドレス[/url][/color]の例を見てみましょう。")
t("Note the following:\n\n1. There are NO correlation between network addresses and hardware addresses. If the network address of MEDIA server 1 is unconfigured, a traversal with a specific destination network address will NOT reach it.\n\nSuppose that MEDIA server 1 becomes unavailable:", "以下に注目してください:\n\n1. ネットワークアドレスとハードウェアアドレスの間に相関関係はありません。MEDIAサーバー1のネットワークアドレスが未設定の場合、特定の宛先ネットワークアドレスを持つトラバーサルはそこに到達しません。\n\nMEDIAサーバー1が利用不能になったとします:")
t("Observe that this behavior is quite similar to traversals without specific destination address. Network addresses allows a group of devices to respond to the same addresses.", "この動作は、特定の宛先アドレスのないトラバーサルとかなり似ていることに注目してください。ネットワークアドレスにより、デバイスのグループが同じアドレスに応答できます。")
t("The [color=yellow] always routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man always[/color]\". It is used to specify defaults on the shell to reduce the length of commands that you need to type.", "[color=yellow]alwaysルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man always[/color]」と入力するとマニュアルにアクセスできます。入力するコマンドの長さを短縮するために、シェルのデフォルト値を指定するために使用されます。")
t("[color=yellow]always using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command sets a [color=yellow]default debugger address[/color] for the \"[color=yellow]using[/color]\" keyword for all netsh routines. \n\nConsider the following effects with the intent of using the debugger [color=orange]4567[/color] for the commands:\n\nWithout default debugger address, commands that interact with device/users always need to be followed with the \"[color=yellow]using[/color]\" keyword to specify which debugger are we running it from:\n\"[color=orange]net show on 123 using 4567[/color]\"\n\"[color=orange]scan firewalls using 4567[/color]\"\n\nWith default debugger address (after doing \"[color=orange]always using 4567[/color]\"), commands may now be shorter and easier to input:\n\"[color=orange]net show on 123[/color]\"\n\"[color=orange]scan firewalls[/color]\"\n\nNote that even with a default debugger set with the [color=yellow]always using[/color] command, you can still specify a different debugger (i.e., override the default) with the \"[color=yellow]using[/color]\" keyword.\n\nFor example, after doing \"[color=orange]always using 4567[/color]\" and running a [color=orange]net show[/color] command, you want to use the another debugger [color=orange]89123[/color] for just one command to scan devices:\n\"[color=orange]net show on 123[/color]\"\n\"[color=orange]scan devices using 89123[/color]\"\n\nThe first command is performed on debugger [color=orange]4567[/color] while the second is performed on debugger [color=orange]89123[/color]. This may sometimes be necessary if you have debuggers on different part of the networks that cannot [color=skyblue][url]reach[/url][/color] the target devices.\n\nAdditionally, the \"[color=yellow]using[/color]\" keyword accepts both [color=skyblue][url]hardware address[/url][/color] and [color=skyblue][url]network address[/url][/color]. This means that you can also do [color=orange]always using @mydebug[/color] to set a default debugger with network addresses instead (if the debugger has been assigned the network address [color=orange]@mydebug[/color]).", "[color=yellow]always using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドはすべてのnetshルーチンの「[color=yellow]using[/color]」キーワードに対する[color=yellow]デフォルトデバッガーアドレス[/color]を設定します。\n\nデバッガー[color=orange]4567[/color]を使用する場合の効果を考えてみましょう:\n\nデフォルトデバッガーアドレスなしでは、デバイス/ユーザーとやり取りするコマンドは常に「[color=yellow]using[/color]」キーワードでどのデバッガーから実行するか指定する必要があります:\n「[color=orange]net show on 123 using 4567[/color]」\n「[color=orange]scan firewalls using 4567[/color]」\n\nデフォルトデバッガーアドレス設定後（「[color=orange]always using 4567[/color]」実行後）、コマンドが短く簡単になります:\n「[color=orange]net show on 123[/color]」\n「[color=orange]scan firewalls[/color]」\n\n[color=yellow]always using[/color]コマンドでデフォルトデバッガーを設定しても、「[color=yellow]using[/color]」キーワードで別のデバッガーを指定（デフォルトをオーバーライド）できます。\n\n例えば、「[color=orange]always using 4567[/color]」実行後に[color=orange]net show[/color]コマンドを実行し、1つのコマンドだけ別のデバッガー[color=orange]89123[/color]を使用してデバイスをスキャンしたい場合:\n「[color=orange]net show on 123[/color]」\n「[color=orange]scan devices using 89123[/color]」\n\n最初のコマンドはデバッガー[color=orange]4567[/color]で実行され、2番目はデバッガー[color=orange]89123[/color]で実行されます。ネットワークの異なる部分にあるデバッガーがターゲットデバイスに[color=skyblue][url]到達[/url][/color]できない場合に必要になることがあります。\n\nさらに、「[color=yellow]using[/color]」キーワードは[color=skyblue][url]ハードウェアアドレス[/url][/color]と[color=skyblue][url]ネットワークアドレス[/url][/color]の両方を受け付けます。つまり、デバッガーにネットワークアドレス[color=orange]@mydebug[/color]が割り当てられている場合、[color=orange]always using @mydebug[/color]でネットワークアドレスを使ったデフォルトデバッガーの設定も可能です。")
t("The [color=yellow]dhcp routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man dhcp[/color]\". It is used configure options on [color=skyblue][url]DHCP[/url][/color] servers.", "[color=yellow]dhcpルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man dhcp[/color]」と入力するとマニュアルにアクセスできます。[color=skyblue][url]DHCP[/url][/color]サーバーのオプションを設定するために使用されます。")
t("The routine uses traffic type [color=palegreen]tcp/23[/color] to access DHCP servers", "このルーチンはDHCPサーバーにアクセスするためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。")
t("[color=yellow]dhcp show on [color=magenta]<address-of-target-dhcp>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command shows the DHCP option information on the [color=magenta]target server[/color].\n\nExamples:\n\"[color=orange]dhcp show on 123 using 456[/color]\"\n\"[color=orange]dhcp show on @mydhcp[/color]\"", "[color=yellow]dhcp show on [color=magenta]<対象DHCPのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象サーバー[/color]のDHCPオプション情報を表示します。\n\n例:\n「[color=orange]dhcp show on 123 using 456[/color]」\n「[color=orange]dhcp show on @mydhcp[/color]」")
t("[color=yellow]dhcp option prefix on [color=magenta]<address-of-target-dhcp>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\nThis sets the [color=yellow]Prefix DHCP option[/color] on the [color=magenta]target server[/color].\n\n[color=yellow]dhcp option dns on [color=magenta]<address-of-target-dhcp>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\nThis sets the [color=yellow]DNS DHCP option[/color] on the [color=magenta]target server[/color].\n\nExamples:\n\"[color=orange]dhcp option prefix @net1- on 123 using 456[/color]\"\n\"[color=orange]dhcp option dns @dns on @mydhcp[/color]\"", "[color=yellow]dhcp option prefix on [color=magenta]<対象DHCPのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n[color=magenta]対象サーバー[/color]の[color=yellow]PrefixのDHCPオプション[/color]を設定します。\n\n[color=yellow]dhcp option dns on [color=magenta]<対象DHCPのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n[color=magenta]対象サーバー[/color]の[color=yellow]DNSのDHCPオプション[/color]を設定します。\n\n例:\n「[color=orange]dhcp option prefix @net1- on 123 using 456[/color]」\n「[color=orange]dhcp option dns @dns on @mydhcp[/color]」")
t("The [color=yellow]dns routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man dns[/color]\". It is used to create/clear [color=skyblue][url]DNS entries[/url][/color].", "[color=yellow]dnsルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man dns[/color]」と入力するとマニュアルにアクセスできます。[color=skyblue][url]DNSエントリ[/url][/color]の作成/クリアに使用されます。")
t("This routine uses traffic type [color=palegreen]udp/53[/color] to reach the DNS servers from the debugger.", "このルーチンはデバッガーからDNSサーバーに到達するためにトラフィックタイプ[color=palegreen]udp/53[/color]を使用します。")
t("[color=yellow]dns map [color=magenta]<domain-name>[/color] as [color=magenta]<resolved-address>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command maps the [color=magenta][url]domain name[/url][/color] to a [color=magenta][url]logical address[/url][/color]. The debugger must be able to reach any DNS server for this command to succeed. DNS entries are global, which means it does not matter which DNS servers are reached.\n\nExamples:\n\"[color=orange]dns map towernews.org as 12345 using 456[/color]\"\n\"[color=orange]dns map towernews.org as @net1/townews[/color]\"", "[color=yellow]dns map [color=magenta]<ドメイン名>[/color] as [color=magenta]<解決先アドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta][url]ドメイン名[/url][/color]を[color=magenta][url]論理アドレス[/url][/color]にマッピングします。デバッガーがいずれかのDNSサーバーに到達できる必要があります。DNSエントリはグローバルなので、どのDNSサーバーに到達するかは関係ありません。\n\n例:\n「[color=orange]dns map towernews.org as 12345 using 456[/color]」\n「[color=orange]dns map towernews.org as @net1/townews[/color]」")
t("[color=yellow]dns lookup [color=magenta]<domain-name>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis performs a test DNS resolution for the [color=magenta][url]domain name[/url][/color] using the debugger.\n\nExamples:\n\"[color=orange]dns lookup towernews.org using 456[/color]\"\n\"[color=orange]dns lookup foostore.com[/color]\"", "[color=yellow]dns lookup [color=magenta]<ドメイン名>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nデバッガーを使用して[color=magenta][url]ドメイン名[/url][/color]のテストDNS解決を実行します。\n\n例:\n「[color=orange]dns lookup towernews.org using 456[/color]」\n「[color=orange]dns lookup foostore.com[/color]」")
t("[color=yellow]dns clear [color=magenta]<domain-name>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command removes the DNS entry for the [color=magenta][url]domain name[/url][/color]. The debugger must be able to reach any DNS server for this command to succeed. DNS entries are global, which means it does not matter which DNS servers are reached.\n\nExamples:\n\"[color=orange]dns clear towernews.org as 12345 using 456[/color]\"\n\"[color=orange]dns clear foostore.com\"", "[color=yellow]dns clear [color=magenta]<ドメイン名>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta][url]ドメイン名[/url][/color]のDNSエントリを削除します。デバッガーがいずれかのDNSサーバーに到達できる必要があります。DNSエントリはグローバルなので、どのDNSサーバーに到達するかは関係ありません。\n\n例:\n「[color=orange]dns clear towernews.org as 12345 using 456[/color]」\n「[color=orange]dns clear foostore.com[/color]」")
t("The [color=yellow]firewall routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man firewall[/color]\". It is used to manage [color=skyblue][url]network firewalls[/url][/color].", "[color=yellow]firewallルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man firewall[/color]」と入力するとマニュアルにアクセスできます。[color=skyblue][url]ネットワークファイアウォール[/url][/color]を管理するために使用されます。")
t("The routine uses traffic type [color=palegreen]tcp/23[/color] to access and configure the firewalls.", "このルーチンはファイアウォールにアクセスして設定するためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。")
t("[color=yellow]firewall show on [color=magenta]<address-of-target-firewall>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command shows the firewall policies on the [color=magenta]target firewall[/color].\n\nExamples:\n\"[color=orange]firewall show on 123 using 456[/color]\"\n\"[color=orange]firewall show on @fw1[/color]\"", "[color=yellow]firewall show on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象ファイアウォール[/color]のファイアウォールポリシーを表示します。\n\n例:\n「[color=orange]firewall show on 123 using 456[/color]」\n「[color=orange]firewall show on @fw1[/color]」")
t("[color=yellow]firewall allow [color=magenta]<traffic-type>[/color] from [color=magenta]<src-addr>[/color] to [color=magenta]<dst-addr>[/color] on [color=magenta]<address-of-target-firewall>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command adds a new \"[color=yellow]allow[/color]\" policy to the [color=magenta]target firewall[/color]. It is optional to specify the [color=magenta][url]traffic-type[/url][/color], [color=magenta]source address[/color] and [color=magenta]destination address[/color]. If unspecified, it is treated as [color=yellow]any[/color].\n\nExamples:\n\"[color=orange]firewall allow 123 to 456 on 789 using 101[/color]\" - Explicitly allow source [color=orange]123[/color] to destination [color=orange]456[/color] on the firewall [color=orange]789[/color].\n\n\"[color=orange]firewall allow udp/53 to @dns on 789[/color]\" - Explicitly allow traffic [color=orange]udp/53[/color] with destination prefix [color=orange]@dns[/color] on the firewall [color=orange]789[/color].\n\n\"[color=orange]firewall allow tcp/80 on @fw1[/color]\" - Explicitly allow traffic [color=orange]tcp/80[/color] from anywhere to anywhere on firewall [color=orange]@fw1[/color].\n\n[color=yellow]firewall deny [color=magenta]<traffic-type>[/color] from [color=magenta]<src-addr>[/color] to [color=magenta]<dst-addr>[/color] on [color=magenta]<address-of-target-firewall>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis similar command adds a new \"[color=yellow]deny[/color]\" policy to the [color=magenta]target firewall[/color]. It is optional to specify the [color=magenta][url]traffic-type[/url][/color], [color=magenta]source address[/color] and [color=magenta]destination address[/color].  If unspecified, it is treated as [color=yellow]any[/color].\n\nExamples:\n\"[color=orange]firewall deny from @user2 on 789[/color]\" - Explicitly deny source address with prefix [color=orange]@user2[/color] to any destination on the firewall [color=orange]789[/color].\n\n\"[color=orange]firewall deny tcp/22 on 789[/color]\" - Explicitly deny traffic [color=orange]tcp/22[/color] from any source to any destination on firewall [color=orange]789[/color].", "[color=yellow]firewall allow [color=magenta]<トラフィックタイプ>[/color] from [color=magenta]<送信元アドレス>[/color] to [color=magenta]<宛先アドレス>[/color] on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象ファイアウォール[/color]に新しい「[color=yellow]allow[/color]」ポリシーを追加します。[color=magenta][url]トラフィックタイプ[/url][/color]、[color=magenta]送信元アドレス[/color]、[color=magenta]宛先アドレス[/color]の指定は任意です。未指定の場合は[color=yellow]any[/color]として扱われます。\n\n例:\n「[color=orange]firewall allow 123 to 456 on 789 using 101[/color]」 - 送信元[color=orange]123[/color]から宛先[color=orange]456[/color]をファイアウォール[color=orange]789[/color]で明示的に許可します。\n\n「[color=orange]firewall allow udp/53 to @dns on 789[/color]」 - トラフィック[color=orange]udp/53[/color]で宛先プレフィックス[color=orange]@dns[/color]をファイアウォール[color=orange]789[/color]で明示的に許可します。\n\n「[color=orange]firewall allow tcp/80 on @fw1[/color]」 - トラフィック[color=orange]tcp/80[/color]をファイアウォール[color=orange]@fw1[/color]ですべての送信元からすべての宛先に対して明示的に許可します。\n\n[color=yellow]firewall deny [color=magenta]<トラフィックタイプ>[/color] from [color=magenta]<送信元アドレス>[/color] to [color=magenta]<宛先アドレス>[/color] on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n同様のコマンドで[color=magenta]対象ファイアウォール[/color]に新しい「[color=yellow]deny[/color]」ポリシーを追加します。[color=magenta][url]トラフィックタイプ[/url][/color]、[color=magenta]送信元アドレス[/color]、[color=magenta]宛先アドレス[/color]の指定は任意です。未指定の場合は[color=yellow]any[/color]として扱われます。\n\n例:\n「[color=orange]firewall deny from @user2 on 789[/color]」 - 送信元アドレスプレフィックス[color=orange]@user2[/color]から任意の宛先への通信をファイアウォール[color=orange]789[/color]で明示的に拒否します。\n\n「[color=orange]firewall deny tcp/22 on 789[/color]」 - トラフィック[color=orange]tcp/22[/color]をファイアウォール[color=orange]789[/color]ですべての送信元からすべての宛先に対して明示的に拒否します。")
t("[color=yellow]firewall default allow on [color=magenta]<address-of-target-firewall>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command sets the default policy (when no policies are matched) to [color=green]allow[/color] on the [color=magenta]target firewall[/color].\n\n[color=yellow]firewall default deny on [color=magenta]<address-of-target-firewall>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command sets the default policy (when no policies are matched) to [color=red]deny[/color] on the [color=magenta]target firewall[/color].\n\nExamples:\n\"[color=orange]firewall default deny port0 on 123 using 456[/color]\"\n\"[color=orange]firewall default allow on @fw1[/color]\"", "[color=yellow]firewall default allow on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象ファイアウォール[/color]のデフォルトポリシー（ポリシーが一致しない場合）を[color=green]allow[/color]に設定します。\n\n[color=yellow]firewall default deny on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象ファイアウォール[/color]のデフォルトポリシー（ポリシーが一致しない場合）を[color=red]deny[/color]に設定します。\n\n例:\n「[color=orange]firewall default deny port0 on 123 using 456[/color]」\n「[color=orange]firewall default allow on @fw1[/color]」")
t("[color=yellow]firewall remove [color=magenta]<policy-id>[/color] on [color=magenta]<address-of-target-firewall>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command removes the firewall policy specified by [color=magenta]policy-id[/color] on the [color=magenta]target firewall[/color]. The list of policy-id is obtained using the \"firewall show\" command. Multiple policies can be removed in the same command.\n\nExamples:\n\"[color=orange]firewall remove #0 on 123 using 456[/color]\"\n\"[color=orange]firewall remove #1 #2 on @fw1[/color]\"", "[color=yellow]firewall remove [color=magenta]<ポリシーID>[/color] on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象ファイアウォール[/color]の[color=magenta]ポリシーID[/color]で指定されたファイアウォールポリシーを削除します。ポリシーIDの一覧は「firewall show」コマンドで取得できます。同じコマンドで複数のポリシーを削除できます。\n\n例:\n「[color=orange]firewall remove #0 on 123 using 456[/color]」\n「[color=orange]firewall remove #1 #2 on @fw1[/color]」")
t("The [color=yellow]lstdbg routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man lstdbg[/color]\". It is used to list active ([color=skyblue][url]powered[/url][/color]) [color=skyblue][url]debuggers[/url][/color].\n\nThe routine is very simple to use, just input the command \"[color=yellow]lstdbg[/color]\" and the list of active debuggers are shown. The debugger currently specified by the [color=skyblue][url]always routine[/url][/color] is shown in green.", "[color=yellow]lstdbgルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man lstdbg[/color]」と入力するとマニュアルにアクセスできます。有効な（[color=skyblue][url]電源が入った[/url][/color]）[color=skyblue][url]デバッガー[/url][/color]を一覧表示するために使用されます。\n\n使い方はとても簡単で、「[color=yellow]lstdbg[/color]」と入力するだけでアクティブなデバッガーの一覧が表示されます。[color=skyblue][url]alwaysルーチン[/url][/color]で現在指定されているデバッガーは緑色で表示されます。")
t("The [color=yellow]net routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man net[/color]\". It is used to configure network parameters on [color=skyblue][url]devices[/url][/color] and [color=skyblue][url]users[/url][/color] in the tower.", "[color=yellow]netルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man net[/color]」と入力するとマニュアルにアクセスできます。タワー内の[color=skyblue][url]デバイス[/url][/color]や[color=skyblue][url]ユーザー[/url][/color]のネットワークパラメータを設定するために使用されます。")
t("This routine uses traffic type [color=palegreen]tcp/23[/color] to reach the targets from the debugger.", "このルーチンはデバッガーからターゲットに到達するためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。")
t("[color=yellow]net show on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command shows the network information (e.g., [color=skyblue][url]network address[/url][/color], [color=skyblue][url]bandwidth capacity[/url][/color], [color=skyblue][url]DHCP[/url][/color] enabled/disabled and [color=skyblue][url]DNS[/url][/color] information) on the [color=magenta]target[/color].\n\nExamples:\n\"[color=orange]net show on 123 using 456[/color]\"\n\"[color=orange]net show on @mydev[/color]\"", "[color=yellow]net show on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象[/color]のネットワーク情報（例：[color=skyblue][url]ネットワークアドレス[/url][/color]、[color=skyblue][url]帯域幅容量[/url][/color]、[color=skyblue][url]DHCP[/url][/color]の有効/無効、[color=skyblue][url]DNS[/url][/color]情報）を表示します。\n\n例:\n「[color=orange]net show on 123 using 456[/color]」\n「[color=orange]net show on @mydev[/color]」")
t("[color=yellow]net address set [color=magenta]<address>[/color] on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n[color=yellow]net address clear on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThe first command sets the [color=skyblue][url]network address[/url][/color] of the [color=magenta]target[/color] to [color=magenta]address[/color]. \nThe second command clears the network address of the [color=magenta]target[/color].\n\nExamples:\n\"[color=orange]net address set @myaddr on 123 using 456[/color]\"\n\"[color=orange]net address clear on 123\"", "[color=yellow]net address set [color=magenta]<アドレス>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n[color=yellow]net address clear on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n最初のコマンドは[color=magenta]対象[/color]の[color=skyblue][url]ネットワークアドレス[/url][/color]を[color=magenta]アドレス[/color]に設定します。\n2番目のコマンドは[color=magenta]対象[/color]のネットワークアドレスをクリアします。\n\n例:\n「[color=orange]net address set @myaddr on 123 using 456[/color]」\n「[color=orange]net address clear on 123[/color]」")
t("[color=yellow]net dns set [color=magenta]<dns_srv_addr>[/color] on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n[color=yellow]net dns clear on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThe first command sets the [color=skyblue][url]designated DNS server address[/url][/color] of the [color=magenta]target[/color] to [color=magenta]address[/color]. \nThe second command clears the designated DNS server address of the [color=magenta]target[/color].\n\nExamples:\n\"[color=orange]net dns set @dns1 on 123 using 456[/color]\"\n\"[color=orange]net dns clear on 123\"", "[color=yellow]net dns set [color=magenta]<DNSサーバーアドレス>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n[color=yellow]net dns clear on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n最初のコマンドは[color=magenta]対象[/color]の[color=skyblue][url]指定DNSサーバーアドレス[/url][/color]を[color=magenta]アドレス[/color]に設定します。\n2番目のコマンドは[color=magenta]対象[/color]の指定DNSサーバーアドレスをクリアします。\n\n例:\n「[color=orange]net dns set @dns1 on 123 using 456[/color]」\n「[color=orange]net dns clear on 123[/color]」")
t("[color=yellow]net dhcp enable on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\nEnables [color=skyblue][url]DHCP[/url][/color] on the [color=magenta]target[/color]. DHCP request is performed approximately every 10 seconds automatically if enabled.\n\n[color=yellow]net dhcp disable on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\nDisables [color=skyblue][url]DHCP[/url][/color] on the [color=magenta]target[/color].\n\n[color=yellow]net dhcp request on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\nImmediately perform a DHCP request from the [color=magenta]target[/color].\n\nExamples:\n\"[color=orange]net dhcp enable on 123 using 456[/color]\"\n\"[color=orange]net dhcp disable on 123\"\n\"[color=orange]net dhcp request on 123\"", "[color=yellow]net dhcp enable on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n[color=magenta]対象[/color]で[color=skyblue][url]DHCP[/url][/color]を有効にします。有効にすると、約10秒ごとに自動的にDHCPリクエストが実行されます。\n\n[color=yellow]net dhcp disable on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n[color=magenta]対象[/color]で[color=skyblue][url]DHCP[/url][/color]を無効にします。\n\n[color=yellow]net dhcp request on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n[color=magenta]対象[/color]からDHCPリクエストを直ちに実行します。\n\n例:\n「[color=orange]net dhcp enable on 123 using 456[/color]」\n「[color=orange]net dhcp disable on 123[/color]」\n「[color=orange]net dhcp request on 123[/color]」")
t("The [color=yellow]pcap routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man pcap[/color]\". It is used to start packet capture/inspection on [color=skyblue][url]network taps[/url][/color].", "[color=yellow]pcapルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man pcap[/color]」と入力するとマニュアルにアクセスできます。[color=skyblue][url]ネットワークタップ[/url][/color]でパケットキャプチャ/検査を開始するために使用されます。")
t("The routine uses traffic type [color=palegreen]tcp/23[/color] to start the packet capture process.", "このルーチンはパケットキャプチャプロセスを開始するためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。")
t("[color=yellow]pcap [color=magenta]<address-of-target-tap>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\nThis command instructs the [color=magenta]target network tap[/color] to start packet capture/inspection.\n\nExamples:\n\"[color=orange]pcap on @mytap using 456[/color]\"\n\"[color=orange]pcap on 123[/color]\"", "[color=yellow]pcap [color=magenta]<対象タップのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\nこのコマンドは[color=magenta]対象ネットワークタップ[/color]にパケットキャプチャ/検査を開始するよう指示します。\n\n例:\n「[color=orange]pcap on @mytap using 456[/color]」\n「[color=orange]pcap on 123[/color]」")
t("The [color=yellow]program routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man program[/color]\". It is used to install and run programs on [color=skyblue][url]devices[/url][/color].", "[color=yellow]programルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man program[/color]」と入力するとマニュアルにアクセスできます。[color=skyblue][url]デバイス[/url][/color]にプログラムをインストールして実行するために使用されます。")
t("The routine uses traffic type [color=palegreen]tcp/23[/color] to access and install/run programs on the target.", "このルーチンはターゲットにプログラムをアクセス・インストール/実行するためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。")
t("[color=yellow]program list[/color]\n\nThis command list the programs available to be installed on the servers. The list include the [color=yellow]release names[/color] of the programs, which are keywords used to identify the [color=skyblue][url]programs[/url][/color].\n\nExamples:\n\"[color=orange]program list[/color]\"", "[color=yellow]program list[/color]\n\nこのコマンドはサーバーにインストール可能なプログラムの一覧を表示します。リストには[color=skyblue][url]プログラム[/url][/color]を識別するためのキーワードであるプログラムの[color=yellow]リリース名[/color]が含まれます。\n\n例:\n「[color=orange]program list[/color]」")
t("[color=yellow]program describe [color=magenta]<release-name>[/color][/color]\n\nThis command prints out information about the program specified by the [color=magenta]release name[/color].\n\nExamples:\n\"[color=orange]program describe dns-server[/color]\"", "[color=yellow]program describe [color=magenta]<リリース名>[/color][/color]\n\nこのコマンドは[color=magenta]リリース名[/color]で指定されたプログラムの情報を表示します。\n\n例:\n「[color=orange]program describe dns-server[/color]」")
t("[color=yellow]program view installed on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command lists installed programs on the [color=magenta]target device[/color].\n\nExamples:\n\"[color=orange]program view installed on 123 using 456[/color]\"\n\"[color=orange]program view installed on @dns[/color]\"\n\n[color=yellow]program view running on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command lists running programs on the [color=magenta]target device[/color] along  with their process-id (pid).\n\nExamples:\n\"[color=orange]program view running on 123 using 456[/color]\"\n\"[color=orange]program view running on @dns[/color]\"", "[color=yellow]program view installed on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象デバイス[/color]にインストールされているプログラムを一覧表示します。\n\n例:\n「[color=orange]program view installed on 123 using 456[/color]」\n「[color=orange]program view installed on @dns[/color]」\n\n[color=yellow]program view running on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象デバイス[/color]で実行中のプログラムとそのプロセスID（pid）を一覧表示します。\n\n例:\n「[color=orange]program view running on 123 using 456[/color]」\n「[color=orange]program view running on @dns[/color]」")
t("[color=yellow]program install [color=magenta]<release-name>[/color] on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command installs a [color=magenta]program specified by the release name[/color] on the [color=magenta]target device[/color].\n\nExamples:\n\"[color=orange]program install kea on 123 using 456[/color]\"\n\"[color=orange]program install dns-lite on @dns[/color]\"\n\n[color=yellow]program uninstall [color=magenta]<release-name>[/color] on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command uninstalls a [color=magenta]program specified by the release name[/color] on the [color=magenta]target device[/color].\n\nExamples:\n\"[color=orange]program uninstall kea on 123 using 456[/color]\"\n\"[color=orange]program uninstall dns-lite on @dns[/color]\"", "[color=yellow]program install [color=magenta]<リリース名>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]リリース名で指定されたプログラム[/color]を[color=magenta]対象デバイス[/color]にインストールします。\n\n例:\n「[color=orange]program install kea on 123 using 456[/color]」\n「[color=orange]program install dns-lite on @dns[/color]」\n\n[color=yellow]program uninstall [color=magenta]<リリース名>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]リリース名で指定されたプログラム[/color]を[color=magenta]対象デバイス[/color]からアンインストールします。\n\n例:\n「[color=orange]program uninstall kea on 123 using 456[/color]」\n「[color=orange]program uninstall dns-lite on @dns[/color]」")
t("[color=yellow]program start [color=magenta]<release-name>[/color] on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command starts an installed [color=magenta]program specified by the release name[/color] on the [color=magenta]target device[/color].\n\nExamples:\n\"[color=orange]program start kea on 123 using 456[/color]\"\n\"[color=orange]program start dns-lite on @dns[/color]\"", "[color=yellow]program start [color=magenta]<リリース名>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象デバイス[/color]にインストール済みの[color=magenta]リリース名で指定されたプログラム[/color]を起動します。\n\n例:\n「[color=orange]program start kea on 123 using 456[/color]」\n「[color=orange]program start dns-lite on @dns[/color]」")
t("[color=yellow]program stop [color=magenta]<release-name>[/color] on [color=magenta]<address-of-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command stops a running [color=magenta]process specified by the release name[/color] on the [color=magenta]target device[/color].\n\nExamples:\n\"[color=orange]program stop opentxt on 123 using 456[/color]\"\n\"[color=orange]program stop dns-lite on @dns[/color]\"", "[color=yellow]program stop [color=magenta]<リリース名>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象デバイス[/color]で実行中の[color=magenta]リリース名で指定されたプロセス[/color]を停止します。\n\n例:\n「[color=orange]program stop opentxt on 123 using 456[/color]」\n「[color=orange]program stop dns-lite on @dns[/color]」")
t("The [color=yellow]route routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man route[/color]\". It is used to manage [color=skyblue][url]network routers[/url][/color].", "[color=yellow]routeルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man route[/color]」と入力するとマニュアルにアクセスできます。[color=skyblue][url]ネットワークルーター[/url][/color]を管理するために使用されます。")
t("The routine uses traffic type [color=palegreen]tcp/23[/color] to access and configure the routers.", "このルーチンはルーターにアクセスして設定するためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。")
t("[color=yellow]route show on [color=magenta]<address-of-target-router>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command shows the routing information on the [color=magenta]target router[/color].\n\nExamples:\n\"[color=orange]route show on 123 using 456[/color]\"\n\"[color=orange]route show on @rt1[/color]\"", "[color=yellow]route show on [color=magenta]<対象ルーターのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象ルーター[/color]のルーティング情報を表示します。\n\n例:\n「[color=orange]route show on 123 using 456[/color]」\n「[color=orange]route show on @rt1[/color]」")
t("[color=yellow]route add [color=magenta]<destination-addr-prefix>[/color] via [color=magenta]<port-id>[/color] on [color=magenta]<address-of-target-router>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command adds a new route on the [color=magenta]target router[/color]. The added route will send traversals to [color=magenta]port-id[/color] if the [color=magenta]destination address prefix[/color] is the longest matched. Port-id accepts the port number (e.g., 0, 1) or the name of the port (e.g., port0, port1).\n\nExamples:\n\"[color=orange]route add @net1- via port0 on 123 using 456[/color]\"\n\"[color=orange]route add 8183 via 1 on @rt1[/color]\"", "[color=yellow]route add [color=magenta]<宛先アドレスプレフィックス>[/color] via [color=magenta]<ポートID>[/color] on [color=magenta]<対象ルーターのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象ルーター[/color]に新しいルートを追加します。追加されたルートは、[color=magenta]宛先アドレスプレフィックス[/color]が最長一致した場合にトラバーサルを[color=magenta]ポートID[/color]に送ります。ポートIDはポート番号（例：0、1）またはポート名（例：port0、port1）を受け付けます。\n\n例:\n「[color=orange]route add @net1- via port0 on 123 using 456[/color]」\n「[color=orange]route add 8183 via 1 on @rt1[/color]」")
t("[color=yellow]route default via [color=magenta]<port-id>[/color] on [color=magenta]<address-of-target-router>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command sets the default port on the [color=magenta]target router[/color], such that when no address prefixes are matched, it sends the traversal to [color=magenta]port-id[/color]. Port-id accepts the port number (e.g., 0, 1) or the name of the port (e.g., port0, port1).\n\nExamples:\n\"[color=orange]route default via port0 on 123 using 456[/color]\"\n\"[color=orange]route default via 1 on @rt1[/color]\"", "[color=yellow]route default via [color=magenta]<ポートID>[/color] on [color=magenta]<対象ルーターのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象ルーター[/color]のデフォルトポートを設定します。アドレスプレフィックスが一致しない場合、トラバーサルを[color=magenta]ポートID[/color]に送ります。ポートIDはポート番号（例：0、1）またはポート名（例：port0、port1）を受け付けます。\n\n例:\n「[color=orange]route default via port0 on 123 using 456[/color]」\n「[color=orange]route default via 1 on @rt1[/color]」")
t("[color=yellow]route remove [color=magenta]<route-id>[/color] on [color=magenta]<address-of-target-router>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command removes the route specified by [color=magenta]route-id[/color] on the [color=magenta]target router[/color]. The list of route-id is obtained using the \"route show\" command. Multiple routes can be removed in the same command.\n\nExamples:\n\"[color=orange]route remove #0 on 123 using 456[/color]\"\n\"[color=orange]route remove #1 #2 on @rt1[/color]\"", "[color=yellow]route remove [color=magenta]<ルートID>[/color] on [color=magenta]<対象ルーターのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは[color=magenta]対象ルーター[/color]の[color=magenta]ルートID[/color]で指定されたルートを削除します。ルートIDの一覧は「route show」コマンドで取得できます。同じコマンドで複数のルートを削除できます。\n\n例:\n「[color=orange]route remove #0 on 123 using 456[/color]」\n「[color=orange]route remove #1 #2 on @rt1[/color]」")
t("The [color=yellow]scan routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man scan[/color]\". It is used to detect [color=skyblue][url]devices[/url][/color] and [color=skyblue][url]users[/url][/color] reachable by the debugger.", "[color=yellow]scanルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man scan[/color]」と入力するとマニュアルにアクセスできます。デバッガーから到達可能な[color=skyblue][url]デバイス[/url][/color]や[color=skyblue][url]ユーザー[/url][/color]を検出するために使用されます。")
t("The scan uses traffic type [color=palegreen]tcp/23[/color] to find devices, which means if [color=palegreen]tcp/23[/color] is blocked, devices will not show up on the scan.", "スキャンはデバイスを検出するためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。つまり、[color=palegreen]tcp/23[/color]がブロックされている場合、デバイスはスキャンに表示されません。")
t("[color=yellow]scan [color=magenta]<type>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command performs a scan for the [color=magenta]specified type[/color] of network devices or users that is [color=skyblue][url]reachable[/url][/color] from the debugger. \n\nThe following is a list of types available for scanning. The singular and plural form of the word is accepted (e.g., you can type \"switch\" instead of \"switches\"). You can also type the letters in the bracket (e.g., you can type \"d\" instead of \"devices\").\n\n1. devices (d)\n2. switches (s)\n3. routers (r)\n4. users (u)\n5. taps (t)\n6. firewalls (f)\n7. dns-servers (dns)\n8. dhcp-servers (dhcp)\n\nExamples:\n\"[color=orange]scan devices using 456[/color]\"\n\"[color=orange]scan switches[/color]\"\n\"[color=orange]scan router[/color]\"\n\"[color=orange]scan r[/color]\"\n\"[color=orange]scan users[/color]\"\n\"[color=orange]scan dns[/color]\"", "[color=yellow]scan [color=magenta]<タイプ>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドはデバッガーから[color=skyblue][url]到達可能[/url][/color]な[color=magenta]指定タイプ[/color]のネットワークデバイスまたはユーザーをスキャンします。\n\n以下はスキャン可能なタイプの一覧です。単数形と複数形の両方が受け付けられます（例：「switches」の代わりに「switch」と入力可能）。括弧内の文字でも入力できます（例：「devices」の代わりに「d」と入力可能）。\n\n1. devices (d)\n2. switches (s)\n3. routers (r)\n4. users (u)\n5. taps (t)\n6. firewalls (f)\n7. dns-servers (dns)\n8. dhcp-servers (dhcp)\n\n例:\n「[color=orange]scan devices using 456[/color]」\n「[color=orange]scan switches[/color]」\n「[color=orange]scan router[/color]」\n「[color=orange]scan r[/color]」\n「[color=orange]scan users[/color]」\n「[color=orange]scan dns[/color]」")
t("The [color=yellow]trace routine[/color] and [color=yellow]ping routine[/color] are routines on [color=skyblue][url]netsh[/url][/color]. They are used to trace traffic from one [color=skyblue][url]device[/url][/color] or [color=skyblue][url]user[/url][/color] to another.", "[color=yellow]traceルーチン[/color]と[color=yellow]pingルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。ある[color=skyblue][url]デバイス[/url][/color]または[color=skyblue][url]ユーザー[/url][/color]から別のデバイス/ユーザーへのトラフィックをトレースするために使用されます。")
t("The routines allows different traffic types to be specified to test connectivity across [color=skyblue][url]firewalls[/url][/color]. The default traffic type is [color=palegreen]icmp[/color].", "これらのルーチンでは、[color=skyblue][url]ファイアウォール[/url][/color]を介した接続性をテストするために異なるトラフィックタイプを指定できます。デフォルトのトラフィックタイプは[color=palegreen]icmp[/color]です。")
t("[color=yellow]trace [color=magenta]<address-of-destination>[/color] from [color=magenta]<address-of-source>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\nInstructs [color=magenta]source[/color] to perform a [color=skyblue][url]network traversal[/url][/color] with to [color=magenta]destination[/color] with [color=palegreen]icmp[/color] traffic.\n\n[color=yellow]trace [color=magenta]<dest>[/color] from [color=magenta]<source>[/color] with [color=magenta]<traffic-type>[/color] using [color=magenta]<debugger>[/color][/color]\nInstructs [color=magenta]source[/color] to perform a [color=skyblue][url]network traversal[/url][/color] with to [color=magenta]destination[/color] with the specified [color=magenta][url]traffic type[/url][/color].\n\nExamples:\n\"[color=orange]trace 123 from @src1 using 456[/color]\"\n\"[color=orange]trace @dst2 from 987[/color]\"\n\"[color=orange]trace @net1-dns from 987 with udp/53[/color]\"", "[color=yellow]trace [color=magenta]<宛先のアドレス>[/color] from [color=magenta]<送信元のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n[color=magenta]送信元[/color]に、[color=palegreen]icmp[/color]トラフィックで[color=magenta]宛先[/color]への[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行するよう指示します。\n\n[color=yellow]trace [color=magenta]<宛先>[/color] from [color=magenta]<送信元>[/color] with [color=magenta]<トラフィックタイプ>[/color] using [color=magenta]<デバッガー>[/color][/color]\n[color=magenta]送信元[/color]に、指定された[color=magenta][url]トラフィックタイプ[/url][/color]で[color=magenta]宛先[/color]への[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行するよう指示します。\n\n例:\n「[color=orange]trace 123 from @src1 using 456[/color]」\n「[color=orange]trace @dst2 from 987[/color]」\n「[color=orange]trace @net1-dns from 987 with udp/53[/color]」")
t("[color=yellow]ping [color=magenta]<address-of-destination>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\nPerform a [color=skyblue][url]network traversal[/url][/color] from the debugger to [color=magenta]destination[/color] with [color=palegreen]icmp[/color] traffic.\n\n[color=yellow]ping [color=magenta]<dest>[/color] with [color=magenta]<traffic-type>[/color] using [color=magenta]<debugger>[/color][/color]\nPerform a [color=skyblue][url]network traversal[/url][/color] from the debugger to [color=magenta]destination[/color] with the specified [color=magenta][url]traffic type[/url][/color].\n\nExamples:\n\"[color=orange]ping 123 using 456[/color]\"\n\"[color=orange]ping @dst2[/color]\"\n\"[color=orange]ping @net1-dns with udp/53[/color]\"", "[color=yellow]ping [color=magenta]<宛先のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\nデバッガーから[color=magenta]宛先[/color]へ[color=palegreen]icmp[/color]トラフィックで[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行します。\n\n[color=yellow]ping [color=magenta]<宛先>[/color] with [color=magenta]<トラフィックタイプ>[/color] using [color=magenta]<デバッガー>[/color][/color]\nデバッガーから[color=magenta]宛先[/color]へ指定された[color=magenta][url]トラフィックタイプ[/url][/color]で[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行します。\n\n例:\n「[color=orange]ping 123 using 456[/color]」\n「[color=orange]ping @dst2[/color]」\n「[color=orange]ping @net1-dns with udp/53[/color]」")
t("The [color=yellow]watch routine[/color] is a routine on [color=skyblue][url]netsh[/url][/color]. Its manual can be accessed by inputting \"[color=yellow]man watch[/color]\". It is used to monitor [color=skyblue][url]devices[/url][/color].", "[color=yellow]watchルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。「[color=yellow]man watch[/color]」と入力するとマニュアルにアクセスできます。[color=skyblue][url]デバイス[/url][/color]を監視するために使用されます。")
t("The routine uses traffic type [color=palegreen]tcp/23[/color] to access the monitoring targets.", "このルーチンは監視対象にアクセスするためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。")
t("[color=yellow]watch using [color=magenta]<address-of-debugger>[/color][/color]\nThis command starts the monitor without any specific target. By hovering the mouse on devices that you want to watch, the device on the mouse will be monitored.\n\n[color=yellow]watch [color=magenta]<address-of-monitoring-target>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\nThis command specifically watches a [color=magenta]target[/color]. Hovering the mouse over other devices will not affect what is updated on the terminal display.\n\nExamples:\n\"[color=orange]watch using 456[/color]\"\n\"[color=orange]watch[/color]\"\n\"[color=orange]watch on @mydev using 456[/color]\"\n\"[color=orange]watch on 123[/color]\"", "[color=yellow]watch using [color=magenta]<デバッガーのアドレス>[/color][/color]\nこのコマンドは特定のターゲットなしでモニターを開始します。監視したいデバイスにマウスを合わせると、マウス上のデバイスが監視されます。\n\n[color=yellow]watch [color=magenta]<監視対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\nこのコマンドは[color=magenta]対象[/color]を指定して監視します。他のデバイスにマウスを合わせても、ターミナルディスプレイの表示内容は変わりません。\n\n例:\n「[color=orange]watch using 456[/color]」\n「[color=orange]watch[/color]」\n「[color=orange]watch on @mydev using 456[/color]」\n「[color=orange]watch on 123[/color]」")
t("The [color=yellow]DMarket application[/color] is an [color=skyblue][url]application[/url][/color] that can be used to purchase [color=skyblue][url]devices[/url][/color] to operate your network.\n\nDifferent merchants and original equipment manufacturers operates on the platform.\n\nDevices purchased on DMarket are sent to the specified floor [color=yellow]one at a time[/color].", "[color=yellow]DMarketアプリケーション[/color]は、ネットワークを運用するための[color=skyblue][url]デバイス[/url][/color]を購入できる[color=skyblue][url]アプリケーション[/url][/color]です。\n\nさまざまな販売業者やOEMメーカーがプラットフォーム上で運営しています。\n\nDMarketで購入したデバイスは指定したフロアに[color=yellow]1つずつ[/color]配送されます。")
t("a command-line application that goes hand-in-hand with the debugger device.", "デバッガーデバイスと組み合わせて使用するコマンドラインアプリケーションです。")
t("The [color=yellow]netshell application[/color] is an [color=skyblue][url]application[/url][/color] that can be used to setup, operate and troubleshoot your network and services.\n\nIt is a command-line tool that you interact with by typing commands into the lower input box and observe the results of the command in the upper window.\n\nYou can input commands by typing in the input box, then hit the \"[color=yellow]enter⏎[/color]\" key to submit the command.\n\nnetshell consists of various \"[color=purple]routines[/color]\" that each does different kinds of debugging/setup work.\n\nTo see the routines available for your use, input the command \"[color=yellow]man[/color]\" . This will result in a list of available routines.\n\nTo exit the application, input \"[color=yellow]exit[/color]\" or press \"[color=yellow]ctrl+c[/color]\".", "[color=yellow]netshellアプリケーション[/color]はネットワークとサービスのセットアップ、運用、トラブルシューティングに使用できる[color=skyblue][url]アプリケーション[/url][/color]です。\n\n下部の入力ボックスにコマンドを入力し、上部のウィンドウでコマンドの結果を確認するコマンドラインツールです。\n\n入力ボックスにコマンドを入力し、「[color=yellow]enter⏎[/color]」キーを押してコマンドを送信します。\n\nnetshellはさまざまな「[color=purple]ルーチン[/color]」で構成されており、それぞれ異なる種類のデバッグ/セットアップ作業を行います。\n\n使用可能なルーチンを確認するには、「[color=yellow]man[/color]」コマンドを入力します。利用可能なルーチンのリストが表示されます。\n\nアプリケーションを終了するには、「[color=yellow]exit[/color]」と入力するか「[color=yellow]ctrl+c[/color]」を押します。")
t("The \"[color=yellow]man[/color]\" can also do more if followed by the name of the routine.\n\nAs an example, typing in the command \"[color=yellow]man program[/color]\" will print the usage manual for the \"[color=skyblue][url]program[/url][/color]\" routine.\n\nThe usage help is color coded to help you better understand how each commands can be used. \"[color=yellow]Literals[/color]\" (i.e., typing directly as shown) are highlighted in yellow while \"[color=magenta]Variables[/color]\" (i.e., changing based on usage) are highlighted in magenta.\n\nLet's consider the usage help for \"getting program description\":\n\"[color=yellow]program describe[/color] [color=magenta]program_name[/color]\"\n\nTo use this command, one would type in the [color=yellow]literals[/color] exactly followed by the [color=magenta]name of the program[/color] they want to describe. For example, to describe the \"[color=orange]dns-server[/color]\" application, input \"[color=yellow]program describe dns-server[/color]\".\n\nNotice we substitute [color=magenta]program_name[/color] with [color=orange]dns-server[/color] instead of typing \"program_name\" literally.\n\nTo get the list of program names available, the command \"[color=yellow]program list[/color]\" will display a list. Notice this command does not need any variables, and can be typed literally.", "「[color=yellow]man[/color]」コマンドはルーチン名を後に続けるとさらに多くの情報を表示できます。\n\n例として、「[color=yellow]man program[/color]」と入力すると、「[color=skyblue][url]program[/url][/color]」ルーチンの使用マニュアルが表示されます。\n\n使用ヘルプは各コマンドの使い方を理解しやすくするために色分けされています。「[color=yellow]リテラル[/color]」（そのまま入力する）は黄色でハイライトされ、「[color=magenta]変数[/color]」（使用状況に応じて変わる）はマゼンタでハイライトされます。\n\n「プログラムの説明を取得」の使用ヘルプを考えてみましょう:\n「[color=yellow]program describe[/color] [color=magenta]program_name[/color]」\n\nこのコマンドを使用するには、[color=yellow]リテラル[/color]をそのまま入力し、続けて説明したい[color=magenta]プログラム名[/color]を入力します。例えば、「[color=orange]dns-server[/color]」アプリケーションを説明するには、「[color=yellow]program describe dns-server[/color]」と入力します。\n\n[color=magenta]program_name[/color]を「program_name」とそのまま入力するのではなく、[color=orange]dns-server[/color]に置き換えていることに注目してください。\n\n利用可能なプログラム名の一覧を取得するには、「[color=yellow]program list[/color]」コマンドでリストが表示されます。このコマンドは変数を必要とせず、そのまま入力できます。")
t("The netshell is used together with a  [color=skyblue][url]debugger[/url][/color].\n\nAn important routine to use on netsh is the \"[color=orange]lstdbg[/color]\" routine, which lists all [color=skyblue][url]debuggers[/url][/color] that netsh can connect to. A vast majority of the routines, such as [color=yellow]scan[/color], [color=yellow]trace[/color] and [color=yellow]watch[/color] works through the [color=skyblue][url]debugger[/url][/color].\n\nEssentially, the debugger is responsible for running the routines. An example is the \"[color=yellow]scan devices using[/color] [color=magenta]debugger_address[/color]\", which scans any devices that is [color=skyblue][url]reachable[/url][/color] from the debugger ([color=skyblue][url]address[/url][/color] specified by the \"[color=yellow]using[/color]\" keyword).", "netshellは[color=skyblue][url]デバッガー[/url][/color]と一緒に使用します。\n\nnetshで使う重要なルーチンは「[color=orange]lstdbg[/color]」ルーチンで、netshが接続可能な全[color=skyblue][url]デバッガー[/url][/color]を一覧表示します。[color=yellow]scan[/color]、[color=yellow]trace[/color]、[color=yellow]watch[/color]など大部分のルーチンは[color=skyblue][url]デバッガー[/url][/color]を通じて動作します。\n\n基本的に、デバッガーがルーチンの実行を担当します。例えば「[color=yellow]scan devices using[/color] [color=magenta]debugger_address[/color]」は、デバッガー（「[color=yellow]using[/color]」キーワードで指定された[color=skyblue][url]アドレス[/url][/color]）から[color=skyblue][url]到達可能[/url][/color]なデバイスをスキャンします。")
t("The [color=yellow]Surveyor application[/color] is an [color=skyblue][url]application[/url][/color] that can be used to observe and monitor the [color=skyblue][url]users[/url][/color] under your internet service's purview.", "[color=yellow]Surveyorアプリケーション[/color]はインターネットサービスの管轄下にある[color=skyblue][url]ユーザー[/url][/color]を観察・監視するために使用できる[color=skyblue][url]アプリケーション[/url][/color]です。")
t("[i]Basic Camera Movement[/i]\n\n1. Right Mouse Button (Hold + Drag): Rotate or pan the camera view.\n2. Middle Mouse Button (Hold + Drag): Move the camera across the scene.\n3. Mouse Wheel: Zoom in and out.\n4. WASD + Shift: Move the camera using keyboard navigation; hold Shift to move faster.", "[i]基本的なカメラ操作[/i]\n\n1. 右マウスボタン（ホールド＋ドラッグ）: カメラビューを回転またはパンします。\n2. 中マウスボタン（ホールド＋ドラッグ）: シーン上でカメラを移動します。\n3. マウスホイール: ズームイン・ズームアウトします。\n4. WASD + Shift: キーボードでカメラを移動します。Shiftを押し続けると高速移動します。")
t("[i]Device Interaction[/i]\n\n1. Left Mouse Button: Interact with devices (e.g., pick device).", "[i]デバイス操作[/i]\n\n1. 左マウスボタン: デバイスを操作します（例：デバイスを掴む）。")
t("[i]Powering Devices[/i]\n\n1. Connect cables to wall sockets to provide power.\n2. Toggle the red power switch on devices to turn them on.", "[i]デバイスの電源投入[/i]\n\n1. ケーブルを壁のコンセントに接続して電源を供給します。\n2. デバイスの赤い電源スイッチを切り替えて電源を入れます。")
t("[i]Mobile OS interaction[/i]\n\nTo bring up Mobile OS:\n1. Click the [i][color=red]View MobileOS[/color][/i] button\n2. Hit the left ALT key\n\nTo move Mobile OS to the opposite side of the screen:\n1. Middle click on the Mobile OS screen", "[i]モバイルOSの操作[/i]\n\nモバイルOSを表示するには:\n1. [i][color=red]View MobileOS[/color][/i]ボタンをクリック\n2. 左ALTキーを押す\n\nモバイルOSを画面の反対側に移動するには:\n1. モバイルOS画面を中クリック")
t("[i]List of Basic Networking Commands for Connectivity in [i][color=red]netsh[/color][/i] app [/i]\nBefore using the following commands, ensure that you have connected devices/users to a debugger through cables.\n\nThe [i][color=green]devices/users[/color][/i] can only be \"seen\" by the [i][color=green]debugger[/color][/i] after they are connected together through a [i][color=green]switch[/color][/i] or a [i][color=green]router[/color][/i].\n\n1. [i][color=yellow]lstdbg[/color][/i] : show list of debuggers\n2. [i][color=yellow]scan devices using <debugger_address>[/color][/i] : scan connected devices with debugger\n3. [i][color=yellow]scan users using <debugger_address>[/color][/i] : scan connected users with debugger\n4. [i][color=yellow]always using <debugger_address>[/color][/i] : enable netsh to always use a debugger for commands\n\nAfter setting the default debugger address through [i][color=yellow]always using <debugger_address>[/color][/i], you do not need to type the debugger address while achieving the same result.\n\n1. [i][color=yellow]scan users [/color][/i]: same result as scan users using <debugger_address>\n2. [i][color=yellow]scan devices [/color][/i]: same result as scan devices using <debugger_address>\n3. [i][color=yellow]trace <address1> from <address2>[/color][/i]: perform a network trace from address2 to address1 using the debugger\n4. [i][color=yellow]ping <address1>[/color][/i]: ping a device/user from the debugger\n\nShortcut commands\n\n1. [i][color=yellow]scan u [/color][/i] : shortcut for scan users\n2. [i][color=yellow]scan d [/color][/i] : shortcut for scan devices\n\nTo better understand how to use each routine in netsh:\n\n1.[i][color=yellow] man <routine>[/color][/i] : man scan, man always, man shell, etc.", "[i][i][color=red]netsh[/color][/i]アプリでの基本的なネットワーキングコマンド一覧[/i]\n以下のコマンドを使用する前に、デバイス/ユーザーがケーブルでデバッガーに接続されていることを確認してください。\n\n[i][color=green]デバイス/ユーザー[/color][/i]は[i][color=green]スイッチ[/color][/i]または[i][color=green]ルーター[/color][/i]を通じて接続された後にのみ、[i][color=green]デバッガー[/color][/i]から「認識」されます。\n\n1. [i][color=yellow]lstdbg[/color][/i]: デバッガーの一覧を表示\n2. [i][color=yellow]scan devices using <debugger_address>[/color][/i]: デバッガーで接続されたデバイスをスキャン\n3. [i][color=yellow]scan users using <debugger_address>[/color][/i]: デバッガーで接続されたユーザーをスキャン\n4. [i][color=yellow]always using <debugger_address>[/color][/i]: コマンドで常にデバッガーを使用するよう設定\n\n[i][color=yellow]always using <debugger_address>[/color][/i]でデフォルトのデバッガーアドレスを設定した後は、同じ結果を得るためにデバッガーアドレスを入力する必要がありません。\n\n1. [i][color=yellow]scan users [/color][/i]: scan users using <debugger_address>と同じ結果\n2. [i][color=yellow]scan devices [/color][/i]: scan devices using <debugger_address>と同じ結果\n3. [i][color=yellow]trace <address1> from <address2>[/color][/i]: デバッガーを使用してaddress2からaddress1へのネットワークトレースを実行\n4. [i][color=yellow]ping <address1>[/color][/i]: デバッガーからデバイス/ユーザーにpingを実行\n\nショートカットコマンド\n\n1. [i][color=yellow]scan u [/color][/i]: scan usersのショートカット\n2. [i][color=yellow]scan d [/color][/i]: scan devicesのショートカット\n\nnetshの各ルーチンの使い方をより理解するには:\n\n1.[i][color=yellow] man <routine>[/color][/i]: man scan、man always、man shellなど。")
t("[i]Monitor Users' Profile in [i][color=red]Surveyor[/color][/i] app [/i]\n\n1. Click on the user details (the magnifying glass) on Surveyor app\n2. Identify the user cannot reach DNS server based on 'No DNS Servers for <user's name> to <action>'\n3. Ensure the physical connection between debugger, switch, devices/users are completed with switch/router", "[i][i][color=red]Surveyor[/color][/i]アプリでユーザープロフィールを監視[/i]\n\n1. Surveyorアプリでユーザーの詳細（虫眼鏡）をクリック\n2. 「No DNS Servers for <ユーザー名> to <アクション>」に基づいてユーザーがDNSサーバーに到達できないことを確認\n3. デバッガー、スイッチ、デバイス/ユーザー間の物理接続がスイッチ/ルーターで完了していることを確認")
t("[i]Small Tip in Game[/i]\n\n1. Hover the mouse over a device to see the device's address\n2. Right click on a device to copy the address, and right click on netsh to paste the address.\n3. If you do not have physical access to devices (e.g., they are located on another floor), you can use scanning commands to obtain their addresses.", "[i]ゲーム内の小さなヒント[/i]\n\n1. デバイスにマウスを合わせるとデバイスのアドレスが表示されます\n2. デバイスを右クリックしてアドレスをコピーし、netshで右クリックしてアドレスを貼り付けられます。\n3. デバイスに物理的にアクセスできない場合（例：別のフロアにある場合）、スキャンコマンドを使用してアドレスを取得できます。")
t("[i]Set up riser link between floors[/i]\n1. Launch Tower Link app\n2. Select Point A floor and outlet\n3. Select Point B floor and outlet\n4. Select link size from dropdown\n5. Click 'REQUEST LINKS' to confirm riser setup\n6. Click 'VIEW LINKS' tab to monitor/deactivate/decommission riser link\n\nNotes: \n1. More bandwidth is more expensive\n2. If both Point A and B are on the same floor, the riser setup is expensive.", "[i]フロア間のライザーリンク設定[/i]\n1. Tower Linkアプリを起動\n2. ポイントAのフロアとアウトレットを選択\n3. ポイントBのフロアとアウトレットを選択\n4. ドロップダウンからリンクサイズを選択\n5. 「REQUEST LINKS」をクリックしてライザー設定を確定\n6. 「VIEW LINKS」タブでライザーリンクの監視/無効化/廃止を行う\n\n注意:\n1. 帯域幅が大きいほど高価になります\n2. ポイントAとBが同じフロアにある場合、ライザー設定は高額になります。")
t("[i]Device Interaction[/i]\n1. Left Mouse Button: Interact with devices (e.g., pick device).", "[i]デバイス操作[/i]\n1. 左マウスボタン: デバイスを操作します（例：デバイスを掴む）。")
t("[i]Powering Devices[/i]\n1. Connect cables to wall sockets to provide power.\n2. Toggle the red power switch on devices to turn them on.", "[i]デバイスの電源投入[/i]\n1. ケーブルを壁のコンセントに接続して電源を供給します。\n2. デバイスの赤い電源スイッチを切り替えて電源を入れます。")
t("Launch D-Market app\n1. Use search function or filter function to add items to cart\n2. You can choose variants for some items (e.g., ethernet cables)\n3. Click checkout followed by the submit button to confirm order\n4. Purchased items will be delivered through the elevator", "D-Marketアプリを起動\n1. 検索機能またはフィルター機能を使用してカートにアイテムを追加\n2. 一部のアイテムではバリエーションを選択できます（例：イーサネットケーブル）\n3. チェックアウトをクリックし、送信ボタンで注文を確定\n4. 購入したアイテムはエレベーターで配送されます")
t("[i]Manage finance[/i]\n\n1. Always launch Credit Stack app to monitor your finances\n2. Plan your finances accordingly. Being in debt can lead to game over", "[i]財務管理[/i]\n\n1. 常にCredit Stackアプリを起動して財務状況を確認しましょう\n2. 財務を計画的に管理しましょう。負債はゲームオーバーにつながります")
t("[i]Apply loan[/i]\n\n1. Apply for a loan through Fi$hy Loans app to increase your initial capital to expand your network", "[i]ローンの申請[/i]\n\n1. Fi$hy Loansアプリでローンを申請し、ネットワーク拡大のための初期資金を増やしましょう")
t("[i]Identify needs of producer and consumers[/i]\n1. Launch Surveyor app\n2. Click producer's and consumers' profile; either click on their name/click on magnifying glass icon\n3. From behavior insights; you can differentiate between producer (e.g, WireSync News) and consumers (Net Nester)\n4. producer behaviour: use specification (read-text, post-text), a domain name (eg. texttextvelv.biz) and \"visits/required\" label\n5. consumer behaviour: use specification (eg., read-text and post text) to read and comment.", "[i]プロデューサーとコンシューマーのニーズを把握[/i]\n1. Surveyorアプリを起動\n2. プロデューサーとコンシューマーのプロフィールをクリック（名前または虫眼鏡アイコンをクリック）\n3. 行動インサイトからプロデューサー（例：WireSync News）とコンシューマー（Net Nester）を区別できます\n4. プロデューサー行動: USE仕様（read-text, post-text）、ドメイン名（例：texttextvelv.biz）、「visits/required」ラベル\n5. コンシューマー行動: USE仕様（例：read-textとpost text）で閲覧やコメントを行います。")
t("[i]Step to install DNS program in [i][color=red]netsh[/color][/i] app [/i]\nBefore using the following commands, ensure that you have connected devices/users to a debugger through cables, the debugger address is defaulted to 36005 through always using command in this tutorial.\n\n1. man program \n2. program list\n3. program describe dns-lite\n4. program install dns-lite on 21802; 21802 is the server hardware address\n5. program start dns-lite on 21802\n6. <optional> watch 21802\n7. dns map texttextvelv.biz as 78121; 78121 is the producer (WireSync News)'s hardware address", "[i][i][color=red]netsh[/color][/i]アプリでDNSプログラムをインストールする手順[/i]\n以下のコマンドを使用する前に、デバイス/ユーザーがケーブルでデバッガーに接続されていることを確認してください。このチュートリアルではalways usingコマンドでデバッガーアドレスが36005にデフォルト設定されています。\n\n1. man program \n2. program list\n3. program describe dns-lite\n4. program install dns-lite on 21802; 21802はサーバーのハードウェアアドレスです\n5. program start dns-lite on 21802\n6. <任意> watch 21802\n7. dns map texttextvelv.biz as 78121; 78121はプロデューサー（WireSync News）のハードウェアアドレスです")
t("Useful route commands in the netsh app\n\n1. man route - Check syntax for route commands\n2. route show - Display current routes\n3. route default - Set default route\n4. route add - Add new route", "netshアプリで便利なrouteコマンド\n\n1. man route - routeコマンドの構文を確認\n2. route show - 現在のルートを表示\n3. route default - デフォルトルートを設定\n4. route add - 新しいルートを追加")
t("[i]Physical connection to the router (hardware address: 48460)[/i]\n\n1. Connect the debugger to the router before setting up routes through netsh\n2. Make sure each user/device connects to the correct router port.\n\nFor example: If you use the command \"route add 36005 via port2 on 48460\", then the user/device with address 36005 (the destination for port2) must be plugged into port2 of router 48460, where 36005 is the producer's address (WireSync News).", "[i]ルーターへの物理接続（ハードウェアアドレス: 48460）[/i]\n\n1. netshでルートを設定する前に、デバッガーをルーターに接続します\n2. 各ユーザー/デバイスが正しいルーターポートに接続されていることを確認してください。\n\n例えば: 「route add 36005 via port2 on 48460」コマンドを使用する場合、アドレス36005のユーザー/デバイス（port2の宛先）はルーター48460のport2に接続されている必要があります。36005はプロデューサー（WireSync News）のアドレスです。")
t("[i][i]Method 1: Point default route to a network with DNS server[/i][/i]\n\nSet the router's default route to the port where your DNS server connects.\n\n1. Connect DNS server to router port 1\n2. Set port 1 as default route: route default via port1 on 48460\n3. Add route to the producer's address: route add 36005 via port2 on 48460\n4. Connect your consumers to any port of the router (48460) so they can reach the DNS server via port1 and reach the producer (36005) via port2\n\nWhy it works: Any traffic without a specific route automatically goes through the default route, so users can reach the DNS server without extra setup.", "[i][i]方法1: デフォルトルートをDNSサーバーのあるネットワークに設定[/i][/i]\n\nルーターのデフォルトルートをDNSサーバーが接続されているポートに設定します。\n\n1. DNSサーバーをルーターのポート1に接続\n2. ポート1をデフォルトルートに設定: route default via port1 on 48460\n3. プロデューサーのアドレスへのルートを追加: route add 36005 via port2 on 48460\n4. コンシューマーをルーター（48460）の任意のポートに接続し、port1経由でDNSサーバーに、port2経由でプロデューサー（36005）に到達できるようにします\n\nなぜ機能するか: 特定のルートがないトラフィックは自動的にデフォルトルートを通るため、追加設定なしでユーザーがDNSサーバーに到達できます。")
t("[i]Rocket Store[/i]: Your one-stop app launcher retailer\n\nPurchase more advanced apps (e.g., The Registry, Socketeer, Autograph)", "[i]Rocket Store[/i]: ワンストップアプリランチャー販売店\n\nより高度なアプリを購入できます（例：The Registry、Socketeer、Autograph）")
t("[i]Become stream-voice service provider:[/i]\n\n1. Own a domain: Register your domain on the Registry app.\n2. Run the voip-server: Launch the voip-server program.\n3. Connect a public VoIP phone: Connect a VoIP phone to the voip-server (this creates the 'stream-voice' user stack on the voip-server).\n4. DNS mapping: Map your domain (e.g., streamvoice.com) to the voip-server for consumer access.", "[i]stream-voiceサービスプロバイダーになる:[/i]\n\n1. ドメインを所有する: The Registryアプリでドメインを登録します。\n2. voip-serverを実行する: voip-serverプログラムを起動します。\n3. 公衆VoIP電話を接続する: VoIP電話をvoip-serverに接続します（voip-server上に「stream-voice」ユーザースタックが作成されます）。\n4. DNSマッピング: コンシューマーがアクセスできるようにドメイン（例：streamvoice.com）をvoip-serverにマッピングします。")
t("[i]Register Domain Name[/i]\n\n1. Launch The Registry app\n2. Type 'streamvoice.com' as the domain name.\n3. Set the price per consumption to 0.5 using the slider.\n4. Click (+) Associate usage button.\n5. Select 'stream-voice' from the dropdown of USE spec.\n6. Click Finalize button and followed by Confirm button.", "[i]ドメイン名の登録[/i]\n\n1. The Registryアプリを起動\n2. ドメイン名として「streamvoice.com」と入力します。\n3. スライダーで消費あたりの価格を0.5に設定します。\n4. (+) Associate usageボタンをクリックします。\n5. USE仕様のドロップダウンから「stream-voice」を選択します。\n6. Finalizeボタンをクリックし、続いてConfirmボタンをクリックします。")
t("Hit 'ESC' to pause/unpause the game to read the wiki without the stress of time running out.", "「ESC」を押してゲームを一時停止/再開し、時間を気にせずWikiを読むことができます。")
t("Have some thoughts/feedback about the concepts/wiki? Feel free to share them with us using the F8 key.", "コンセプトやWikiについてご意見やフィードバックがありますか？F8キーでお気軽にお知らせください。")
t("{nport}-port ethernet load tester. Blasts UDP/53 DNS query traffic.", "{nport}ポートイーサネット負荷テスター。UDP/53 DNSクエリトラフィックを発生させます。")
t("Ethernet in-line network tap with port-mirroring capabilities. Produces packet traffic captures.", "イーサネットインラインネットワークタップ。ポートミラーリング機能を搭載。パケットトラフィックキャプチャを生成します。")
t("A box for cable/peripheral organization.", "ケーブル/周辺機器整理用ボックス。")
t("Cabling toolkit for RJ-45 terminations.", "RJ-45端末処理用ケーブリングツールキット。")
t("Cabling toolkit for Fiber optic (SC) terminations.", "光ファイバー（SC）端末処理用ケーブリングツールキット。")
t("Used as shelf piece of mounting racks", "マウンティングラックの棚板として使用します。")
t("Mountable power distribution strip. Used as power extension when wall sockets are limited.", "マウント型電源分配タップ。壁のコンセントが限られている場合に電源延長として使用します。")
t("Power distribution strip. Used as power extension when wall sockets are limited.", "電源分配タップ。壁のコンセントが限られている場合に電源延長として使用します。")
t("Extra monitor which displays all the DNS-entries mapping, network address assignments and device location.", "すべてのDNSエントリマッピング、ネットワークアドレス割り当て、デバイスの場所を表示する追加モニター。")
t("Extra monitor displaying the total population count in the tower, available for sale.", "タワー内の総人口数を表示する追加モニター。販売可能。")
t("Extra monitor displaying resident satiety levels, available for sale.", "住民の満足度レベルを表示する追加モニター。販売可能。")
t("Extra monitor which can be used to monitor the users under your internet service's purview", "インターネットサービスの管轄下にあるユーザーを監視するための追加モニター。")
t("Extra monitor displaying top floor issues, available for sale.", "上位フロアの問題を表示する追加モニター。販売可能。")
t("Extra monitor displaying visitor count by domain name, available for sale.", "ドメイン名別の訪問者数を表示する追加モニター。販売可能。")
t("Automatic Voltage Regulator.", "自動電圧調整器。")
t("Protects devices from being damaged by power surges.", "電力サージによるデバイスの損傷を防ぎます。")
t("Uninterrupted power supply unit.", "無停電電源装置。")
t("Keeps devices functioning in the event of power outages/surges.", "停電やサージの際にデバイスの動作を維持します。")
t("Uninterrupted power supply unit (expanded load).", "無停電電源装置（拡張負荷対応）。")
t("Mountable uninterrupted power supply unit (expanded load).", "マウント型無停電電源装置（拡張負荷対応）。")
t("Uninterrupted power supply unit (extra-expanded load).", "無停電電源装置（超拡張負荷対応）。")
t("Max: {load} W", "最大: {load} W")
t("{nport}-port mixed media network capable router.", "{nport}ポートミクストメディアネットワーク対応ルーター。")
t("Allows VLAN subinterfaces.", "VLANサブインターフェースに対応。")
t("{nport}-port mixed media network router.", "{nport}ポートミクストメディアネットワークルーター。")
t("Suitable for small businesses.", "中小企業向け。")
t("Improved performance and maximum throughput.", "性能向上と最大スループットを実現。")
t("3rd generation edition. Supports high-availability setups.", "第3世代エディション。高可用性セットアップに対応。")
t("{nport}-port ethernet network router.", "{nport}ポートイーサネットネットワークルーター。")
t("Economical model for medium sized enterprises.", "中規模企業向けエコノミーモデル。")
t("Economical model for medium sized enterprises. High-availability support.", "中規模企業向けエコノミーモデル。高可用性対応。")
t("{nport}-port mixed-media network router. Small form factor suitable for routing on the edge.", "{nport}ポートミクストメディアネットワークルーター。エッジルーティングに適した小型フォームファクター。")
t("{nport}-port mixed-media network router. 2nd generation edge routing device with even smaller form factor. Less is more.", "{nport}ポートミクストメディアネットワークルーター。第2世代エッジルーティングデバイス。さらに小型なフォームファクター。Less is more。")
t("{nport}-port mixed-media network router. 3rd generation edge routing device with high availability support.", "{nport}ポートミクストメディアネットワークルーター。第3世代エッジルーティングデバイス。高可用性対応。")
t("{nport}-port general computing server.", "{nport}ポート汎用コンピューティングサーバー。")
t("2 extensible SATA 3.5\" slot.", "2基の拡張SATA 3.5\"スロット搭載。")
t("The gazelle is a durable device that is designed to last long in high load conditions.", "Gazelleは高負荷条件下で長持ちするよう設計された耐久性の高いデバイスです。")
t("Scalable compute.", "スケーラブルコンピューティング。")
t("High performance model with extra bandwidth.", "追加帯域幅を搭載した高性能モデル。")
t("High performance model.", "高性能モデル。")
t("{nport}-port high bandwidth computing server.", "{nport}ポート高帯域幅コンピューティングサーバー。")
t("Fiber enabled compute server.", "光ファイバー対応コンピューティングサーバー。")
t("{nport}-port high performance computing server.", "{nport}ポート高性能コンピューティングサーバー。")
t("Comes with 6 SATA 3.5\" expansion slot.", "6基のSATA 3.5\"拡張スロット搭載。")
t("Comes with 2 SATA 3.5\" expansion slot", "2基のSATA 3.5\"拡張スロット搭載。")
t("{nport}-port mixed media network managed switch. Supports VLAN port tagging.", "{nport}ポートミクストメディアネットワークマネージドスイッチ。VLANポートタグに対応。")
t("This device is well sought after in the second hand market.", "この機器は中古市場で人気があります。")
t("{nport}-port ethernet managed network switch. Supports VLAN port tagging.", "{nport}ポートイーサネットマネージドネットワークスイッチ。VLANポートタグに対応。")
t("More ports at a cheaper price.", "より多くのポートをより安価に。")
t("{nport}-port mixed media network switch. \nSupports VLAN port tagging.", "{nport}ポートミクストメディアネットワークスイッチ。\nVLANポートタグに対応。")
t("Enterprise grade equipment.", "エンタープライズグレードの機器。")
t("{nport}-port ethernet network switch.", "{nport}ポートイーサネットネットワークスイッチ。")
t("Suitable for entry-level networks.", "エントリーレベルのネットワークに最適。")
t("{nport}-port fiber-optic network switch.", "{nport}ポート光ファイバーネットワークスイッチ。")
t("{nport}-port mixed media network switch.", "{nport}ポートミクストメディアネットワークスイッチ。")
t("Enterprise grade equipment. Consumes high power to support throughput.", "エンタープライズグレードの機器。スループットを支えるため高消費電力です。")
t("{nport}-port fiber-optic managed network switch. Supports VLAN port tagging.", "{nport}ポート光ファイバーマネージドネットワークスイッチ。VLANポートタグに対応。")

# BATCH 12: Final remaining entries
t("Cable Reclaim", "ケーブル回収")
t("Remaining", "残り")
t("Make a cable.", "ケーブルを作成。")
t("Make", "作成")
t("stats pie", "統計円グラフ")
t("TENABOLT", "TENABOLT")
t("SURGE Guard", "SURGEガード")
t("Uses DC power.", "DC電源を使用。")

# ============================================================
# BATCH 13: Game update new entries (2026-03-28 update)
# ============================================================

# New tutorial/wiki entries
t("1. Type 'streamvoice.com' as the domain name.\n2. Set the price per consumption to 0.5 using the slider.\n3. Click (+) Associate USE button.\n4. Select 'stream-voice' from the dropdown of USE spec.\n5. Click Finalize button and followed by Confirm button.\n\nYou have now successfully register your domain name.\n",
  "1. ドメイン名として「streamvoice.com」と入力します。\n2. スライダーを使って消費単価を0.5に設定します。\n3. (+) USE関連付けボタンをクリックします。\n4. USE仕様のドロップダウンから「stream-voice」を選択します。\n5. 確定ボタンをクリックし、続けて確認ボタンをクリックします。\n\nこれでドメイン名の登録が完了しました。\n")

t("[i]Register Domain Name[/i]\n\n1. Launch The Registry app\n2. Type 'streamvoice.com' as the domain name.\n3. Set the price per consumption to 0.5 using the slider.\n4. Click (+) Associate USE button.\n5. Select 'stream-voice' from the dropdown of USE spec.\n6. Click Finalize button and followed by Confirm button.",
  "[i]ドメイン名の登録[/i]\n\n1. The Registryアプリを起動します\n2. ドメイン名として「streamvoice.com」と入力します。\n3. スライダーを使って消費単価を0.5に設定します。\n4. (+) USE関連付けボタンをクリックします。\n5. USE仕様のドロップダウンから「stream-voice」を選択します。\n6. 確定ボタンをクリックし、続けて確認ボタンをクリックします。")

# Proposals
t("Adds a new \"sftp\" routine to netshell. Allows backup of configs/files on remote devices for price of {cost}.\n\t\nThe routine can also be used to remove malware when regular program uninstalls do not work.",
  "netshellに新しい「sftp」ルーチンを追加します。{cost}の費用でリモートデバイスの設定/ファイルのバックアップが可能になります。\n\t\n通常のプログラムアンインストールが機能しない場合、このルーチンでマルウェアを除去することもできます。")

t("Request for a new data center at the cost of doubling the current daily admin expense.",
  "現在の日次管理費用を2倍にする代わりに、新しいデータセンターを設置する申請。")

t("Proposals can be submitted to the Secretariat to unlock new advantages. The pool of available proposals is [color=yellow]re-drafted periodically[/color], with the [color=yellow]option of locking one[/color] of the proposals to prevent expiry.",
  "事務局に提案を提出して新しいアドバンテージをアンロックできます。利用可能な提案プールは[color=yellow]定期的に再作成され[/color]、提案のうち[color=yellow]1つをロックして[/color]期限切れを防ぐことができます。")

# SLA / Insurance
t("Business liability insurance coverage has prevented your dismissal by The Secretariat.\n\t\t\t\nThe adjusted penalty of {penalty} is debited from your accounts.\n\nPlease see that the user {sla_violated_username} has their SLA fulfilled immediately.",
  "事業賠償責任保険により、事務局からの解任が防止されました。\n\t\t\t\n調整後のペナルティ {penalty} がアカウントから引き落とされます。\n\nユーザー {sla_violated_username} のSLAを直ちに履行してください。")

# Threat intel / Security events
t("Greetings Tower Admins,\n\t\t\nOur threat intel network shows signs of a network worm on these floors:\n{floors}\n\nInitial forensics report indicates the worm is of signature [u]{worm_signature}[/u], and could begin spreading from the victim's network by {start}.\n\t\n[i]{worm_descript}[/i]\n\nInformation brought to you courtesy of Fortypoint Global",
  "タワー管理者の皆様へ\n\t\t\n脅威インテリジェンスネットワークにより、以下のフロアでネットワークワームの兆候が検出されました：\n{floors}\n\n初期フォレンジックレポートによると、ワームのシグネチャは[u]{worm_signature}[/u]であり、{start}までに被害者のネットワークから拡散を開始する可能性があります。\n\t\n[i]{worm_descript}[/i]\n\nこの情報はFortypoint Globalの提供でお届けしています")

t("Greetings,\n\t\t\nNew threat intel suggests cyberattacks such as network worms and co-ordinated denial-of-service may start occurring soon.\n\nWe pledge to share information of such activities ahead of time so that you can be prepared.\n\nConsistently ranking in the leaders segment of the prestigious Partner's Magic Circle for network security infrastructure, Fortypoint security offers industry grade firewalls which can help block such attacks.\n\nIf any of your device has been infected by the malware, you can remove the malware program using the \"program\" routine or the \"sftp\" routine.\n\nInformation brought to you courtesy of Fortypoint Global",
  "ご挨拶申し上げます。\n\t\t\n最新の脅威インテリジェンスによると、ネットワークワームや協調型サービス拒否攻撃などのサイバー攻撃がまもなく発生する可能性があります。\n\nこのような活動の情報を事前に共有し、皆様が備えられるようにいたします。\n\nネットワークセキュリティインフラの権威あるPartner's Magic Circleのリーダーセグメントに常にランクインしているFortypoint securityは、このような攻撃をブロックできる業界グレードのファイアウォールを提供しています。\n\nデバイスがマルウェアに感染した場合、「program」ルーチンまたは「sftp」ルーチンを使用してマルウェアプログラムを除去できます。\n\nこの情報はFortypoint Globalの提供でお届けしています")

# Network outage
t("Issue a network outage notice to floor {n}.\n\t\t\t\nAll users on the floor will become inactive at the start of day {start_day}.\nThey will resume activities at the start of day {end_day}.\n\nFollowing the Secretariat's instructions, you can only issue outage notices every {k} days. \nYou can currently issue {t} network outage notices.",
  "フロア {n} にネットワーク障害通知を発行します。\n\t\t\t\nフロア上のすべてのユーザーは{start_day}日目の開始時に非アクティブになります。\n{end_day}日目の開始時に活動を再開します。\n\n事務局の指示に従い、障害通知は{k}日ごとにのみ発行できます。\n現在{t}件のネットワーク障害通知を発行できます。")

# Device descriptions
t("Handles up to {bw_per_second} traversals per second.", "毎秒最大{bw_per_second}回のトラバーサルを処理します。")
t("{nport}-port ethernet DNS load tester.", "{nport}ポートイーサネットDNS負荷テスター。")

# UI / Settings
t("If enabled, power is free on metered floors.", "有効にすると、従量制フロアの電力が無料になります。")
t("Traversals / second", "トラバーサル/秒")
t("VIEW MobileOS", "MobileOSを表示")

# Debugger / scan / trace commands
t("debugger {dbgaddr} has no network address assigned, it is unable to make requests.", "デバッガー {dbgaddr} にネットワークアドレスが割り当てられていないため、リクエストを送信できません。")
t("scan for devices matching the type reachable from the debugger.", "デバッガーから到達可能な一致するタイプのデバイスをスキャンします。")
t("scans from {dbgaddr} for {tft}", "{dbgaddr}から{tft}をスキャン中")
t("sending {tft} from {src} to {dst}", "{src}から{dst}へ{tft}を送信中")

# Converter description
t("Produce target's use stack limit is {factor} compatible uses per free memory.", "生産ターゲットのUSEスタック上限は空きメモリあたり{factor}個の互換USEです。", ctx="converter_description")

# Measurement unit
t("cycle(s)/sec", "サイクル/秒", ctx="measurement_unit")

# Wiki entries - switching
t("\nObserve the following from the daisy chain example:\n\n1. If the destination is NOT on a switch, ALL other devices/users connected to that switch gets visited.\n2. When [color=orange]BOB[/color] is on SWITCH 3, every node except [color=orange]GIRAFFE[/color] is visited. \n    [color=orange]BOB[/color]'s distance from [color=orange]ALICE[/color] is [color=yellow]4 hops[/color] away.\n2. When [color=orange]BOB[/color] is on SWITCH 2, then no device/user on SWITCH 3 is visited. \n    [color=orange]BOB[/color]'s distance from [color=orange]ALICE[/color] is [color=yellow]3 hops[/color] away.\n3. This means that [color=yellow]if the destination is N hops away, then all nodes connected by a network of daisy chained switches that are lesser than N hops will get visited[/color]. This is the nature of a breadth-first search.\n\nObservation 3 tells us that switches, although simple to use, cannot efficiently function in a large network.\n\nConsider the following network:",
  "\nデイジーチェーンの例から以下のことが観察できます：\n\n1. 宛先がスイッチ上にない場合、そのスイッチに接続されている他のすべてのデバイス/ユーザーが訪問されます。\n2. [color=orange]BOB[/color]がスイッチ3にいる場合、[color=orange]GIRAFFE[/color]以外のすべてのノードが訪問されます。\n    [color=orange]BOB[/color]と[color=orange]ALICE[/color]の距離は[color=yellow]4ホップ[/color]です。\n2. [color=orange]BOB[/color]がスイッチ2にいる場合、スイッチ3上のデバイス/ユーザーは訪問されません。\n    [color=orange]BOB[/color]と[color=orange]ALICE[/color]の距離は[color=yellow]3ホップ[/color]です。\n3. つまり、[color=yellow]宛先がNホップ先にある場合、Nホップ未満のデイジーチェーンスイッチネットワークに接続されたすべてのノードが訪問されます[/color]。これが幅優先探索の性質です。\n\n観察3から、スイッチは使いやすいものの、大規模ネットワークでは効率的に機能できないことがわかります。\n\n以下のネットワークを考えてみましょう：")

t("\nOur prior observation tells us that in order for [color=orange]ALICE[/color] to reach [color=orange]BOB[/color], all the nodes colored in [color=yellow]yellow[/color] are visited, while the nodes in [color=7B68EE]purple[/color] are visited (or not) depending on the ports they are connected to (recall that lower ports are always visited first).\n\nWith a switch-only setup, the [color=skyblue][url]bandwidth[/url][/color] of the entire network will be exhausted fast because of the unnecessary visits.",
  "\n先ほどの観察から、[color=orange]ALICE[/color]が[color=orange]BOB[/color]に到達するために、[color=yellow]黄色[/color]で示されたすべてのノードが訪問され、[color=7B68EE]紫色[/color]のノードは接続されているポートによって訪問される場合とされない場合があります（低いポート番号が常に先に訪問されることを思い出してください）。\n\nスイッチのみの構成では、不必要な訪問によりネットワーク全体の[color=skyblue][url]帯域幅[/url][/color]がすぐに枯渇してしまいます。")

# Wiki entries - traversal
t("Notice the following:\n\n1. Even if Elle's forum has compatible uses, [color=orange]ALICE[/color] does not consume from it because the destination address does not match.\n2. The nature of BFS means that [color=orange]ALICE[/color] will try SWITCH 1's immediate neighbour first before moving deeper into the graph.\n\nNow let's consider an example with [color=skyblue][url]network addresses[/url][/color].",
  "以下の点に注意してください：\n\n1. Elleのフォーラムに互換性のあるUSEがあっても、宛先アドレスが一致しないため[color=orange]ALICE[/color]はそこから消費しません。\n2. BFSの性質上、[color=orange]ALICE[/color]はグラフの深部に進む前にスイッチ1の直接の隣接ノードを先に試します。\n\n次に、[color=skyblue][url]ネットワークアドレス[/url][/color]を使った例を考えてみましょう。")

t("[color=orange]ALICE[/color] was able to successfully access the service hosted on [color=orange]NEWS COMPANY[/color].\n\nNote the following:\n1. The BFS traversal [color=yellow]always[/color] starts from the lowest port from any device.\n2. This example only demonstrates that how [color=orange]ALICE[/color] was able to [color=yellow]reach[/color] [color=orange]NEWS COMPANY[/color]. It may be the case that [color=orange]NEWS COMPANY[/color] does not have sufficient [color=skyblue][url]uses[/url][/color] available left for [color=orange]ALICE[/color] to consume (e.g., overloaded by other [color=skyblue][url]consumers[/url][/color], under DDoS attacks).\n3. If the [color=skyblue][url]DNS[/url][/color] mapping is [color=red]wrong[/color], the [color=yellow]destination address[/color] obtained by [color=orange]ALICE[/color] may cause it to miss [color=orange]NEWS COMPANY[/color] even if it has the compatible [color=skyblue][url]use[/url][/color].\n\nFrom this example, we see 2 main types of network traversals, which are traversal for consumption [color=yellow]with[/color] or [color=yellow]without[/color] any specific destination address.\n\n",
  "[color=orange]ALICE[/color]は[color=orange]NEWS COMPANY[/color]がホストするサービスに正常にアクセスできました。\n\n以下の点に注意してください：\n1. BFSトラバーサルは[color=yellow]常に[/color]各デバイスの最も低いポートから開始されます。\n2. この例は[color=orange]ALICE[/color]が[color=orange]NEWS COMPANY[/color]に[color=yellow]到達[/color]できた方法を示しているだけです。[color=orange]NEWS COMPANY[/color]には[color=orange]ALICE[/color]が消費するための十分な[color=skyblue][url]USE[/url][/color]が残っていない場合があります（例：他の[color=skyblue][url]コンシューマー[/url][/color]による過負荷、DDoS攻撃下など）。\n3. [color=skyblue][url]DNS[/url][/color]マッピングが[color=red]間違っている[/color]場合、[color=orange]ALICE[/color]が取得した[color=yellow]宛先アドレス[/color]により、互換性のある[color=skyblue][url]USE[/url][/color]があっても[color=orange]NEWS COMPANY[/color]を見逃す可能性があります。\n\nこの例から、ネットワークトラバーサルには主に2種類あることがわかります：特定の宛先アドレス[color=yellow]あり[/color]の消費トラバーサルと[color=yellow]なし[/color]の消費トラバーサルです。\n\n")

# Wiki - firewall route remove
t("[color=yellow]route remove [color=magenta]<policy-id>[/color] on [color=magenta]<address-of-target-firewall>[/color] using [color=magenta]<address-of-debugger>[/color][/color]\n\nThis command removes the firewall policy specified by [color=magenta]policy-id[/color] on the [color=magenta]target firewall[/color]. The list of policy-id is obtained using the \"firewall show\" command. Multiple policies can be removed in the same command.\n\nExamples:\n\"[color=orange]firewall remove #0 on 123 using 456[/color]\"\n\"[color=orange]firewall remove #1 #2 on @fw1[/color]\"",
  "[color=yellow]route remove [color=magenta]<ポリシーID>[/color] on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\nこのコマンドは、[color=magenta]対象ファイアウォール[/color]上の[color=magenta]ポリシーID[/color]で指定されたファイアウォールポリシーを削除します。ポリシーIDのリストは「firewall show」コマンドで取得できます。同一コマンドで複数のポリシーを削除できます。\n\n例：\n「[color=orange]firewall remove #0 on 123 using 456[/color]」\n「[color=orange]firewall remove #1 #2 on @fw1[/color]」")


# ============================================================
# PARSER AND TRANSLATION FUNCTIONS
# ============================================================

def parse_po_file(filepath):
    """Parse a PO file and return list of entries"""
    entries = []
    current = {
        'comments': [],
        'msgctxt': None,
        'msgid_lines': [],
        'msgstr_lines': [],
        'state': 'idle'
    }

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')

            if line.startswith('#'):
                if current['state'] == 'msgstr' and current['msgid_lines']:
                    entries.append(current.copy())
                    current = {
                        'comments': [],
                        'msgctxt': None,
                        'msgid_lines': [],
                        'msgstr_lines': [],
                        'state': 'idle'
                    }
                current['comments'].append(line)
                continue

            if line.startswith('msgctxt "'):
                current['msgctxt'] = line[9:-1]
                current['state'] = 'msgctxt'
                continue

            if line.startswith('msgid "'):
                current['state'] = 'msgid'
                current['msgid_lines'].append(line[7:-1])
                continue

            if line.startswith('msgstr "'):
                current['state'] = 'msgstr'
                current['msgstr_lines'].append(line[8:-1])
                continue

            if line.startswith('"') and line.endswith('"'):
                text = line[1:-1]
                if current['state'] == 'msgctxt':
                    if current['msgctxt'] is None:
                        current['msgctxt'] = text
                    else:
                        current['msgctxt'] += text
                elif current['state'] == 'msgid':
                    current['msgid_lines'].append(text)
                elif current['state'] == 'msgstr':
                    current['msgstr_lines'].append(text)
                continue

            if line == '':
                continue

    # Don't forget the last entry
    if current['state'] == 'msgstr' and current['msgid_lines']:
        entries.append(current.copy())

    # Build full msgid/msgstr strings, unescaping PO escape sequences
    def unescape_po(s):
        s = s.replace('\\n', '\n')
        s = s.replace('\\t', '\t')
        s = s.replace('\\"', '"')
        s = s.replace('\\\\', '\\')
        return s

    for entry in entries:
        entry['msgid'] = unescape_po(''.join(entry['msgid_lines']))
        entry['msgstr'] = unescape_po(''.join(entry['msgstr_lines']))

    return entries

def escape_po_string(s):
    """Escape a string for PO file format"""
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    return s

def format_po_string(s, prefix='msgstr'):
    """Format a string for PO file, splitting multiline strings"""
    if not s:
        return f'{prefix} ""'

    # Check if we need multiline
    if '\n' in s or '\t' in s:
        parts = s.split('\n')
        lines = [f'{prefix} ""']
        for i, part in enumerate(parts):
            escaped = escape_po_string(part)
            if i < len(parts) - 1:
                lines.append(f'"{escaped}\\n"')
            else:
                lines.append(f'"{escaped}"')
        return '\n'.join(lines)
    else:
        escaped = escape_po_string(s)
        return f'{prefix} "{escaped}"'

def write_po_file(entries, filepath):
    """Write entries to a PO file"""
    import io as _io
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        for i, entry in enumerate(entries):
            # Write comments
            for comment in entry['comments']:
                f.write(comment + '\n')

            # Write msgctxt if present
            if entry['msgctxt']:
                escaped_ctx = escape_po_string(entry['msgctxt'])
                f.write(f'msgctxt "{escaped_ctx}"\n')

            # Write msgid (preserve original format)
            msgid = entry['msgid']
            if '\n' in msgid:
                parts = msgid.split('\n')
                f.write('msgid ""\n')
                for j, part in enumerate(parts):
                    escaped = part.replace('\\', '\\\\').replace('"', '\\"')
                    if j < len(parts) - 1:
                        f.write(f'"{escaped}\\n"\n')
                    else:
                        f.write(f'"{escaped}"\n')
            else:
                escaped = msgid.replace('\\', '\\\\').replace('"', '\\"')
                f.write(f'msgid "{escaped}"\n')

            # Write translated msgstr
            msgstr = entry.get('translated', entry['msgstr'])
            if '\n' in msgstr:
                parts = msgstr.split('\n')
                f.write('msgstr ""\n')
                for j, part in enumerate(parts):
                    escaped = part.replace('\\', '\\\\').replace('"', '\\"')
                    if j < len(parts) - 1:
                        f.write(f'"{escaped}\\n"\n')
                    else:
                        f.write(f'"{escaped}"\n')
            else:
                escaped = msgstr.replace('\\', '\\\\').replace('"', '\\"')
                f.write(f'msgstr "{escaped}"\n')

            f.write('\n')

def translate_entry(entry):
    """Try to translate an entry"""
    msgid = entry['msgid']
    ctx = entry['msgctxt']

    # Look up in translation dictionary
    key = (ctx, msgid)
    if key in TRANSLATIONS:
        return TRANSLATIONS[key]

    # Try without context
    key_no_ctx = (None, msgid)
    if key_no_ctx in TRANSLATIONS:
        return TRANSLATIONS[key_no_ctx]

    # Try with stripped whitespace (handles trailing \n differences)
    msgid_stripped = msgid.strip()
    for k, v in TRANSLATIONS.items():
        if k[1] and k[1].strip() == msgid_stripped:
            if ctx is None or k[0] is None or k[0] == ctx:
                return v

    # Return empty string for untranslated entries
    return ""

def main():
    print("Parsing PO file...")
    entries = parse_po_file(INPUT_FILE)
    print(f"Found {len(entries)} entries in ja.po")

    # Check en.po for new entries not in ja.po
    import os
    if os.path.exists(EN_FILE):
        print("Checking en.po for new entries...")
        en_entries = parse_po_file(EN_FILE)
        ja_keys = set()
        for e in entries:
            if e['msgid']:
                ja_keys.add((e.get('msgctxt'), e['msgid']))
        new_count = 0
        for e in en_entries:
            if e['msgid']:
                key = (e.get('msgctxt'), e['msgid'])
                if key not in ja_keys:
                    # Add new entry from en.po with empty msgstr
                    new_entry = {
                        'comments': e.get('comments', []),
                        'msgctxt': e.get('msgctxt'),
                        'msgid': e['msgid'],
                        'msgid_lines': e.get('msgid_lines', []),
                        'msgstr': '',
                        'msgstr_lines': [],
                        'translated': '',
                        'state': 'msgstr',
                    }
                    entries.append(new_entry)
                    new_count += 1
        if new_count:
            print(f"Added {new_count} new entries from en.po")
        else:
            print("No new entries found in en.po")

    translated_count = 0
    untranslated = []

    for entry in entries:
        if not entry['msgid']:  # Skip header
            entry['translated'] = entry['msgstr']
            continue

        translation = translate_entry(entry)
        if translation:
            entry['translated'] = translation
            translated_count += 1
        else:
            entry['translated'] = ''
            untranslated.append(entry['msgid'][:60])

    total = sum(1 for e in entries if e['msgid'])
    print(f"Translated: {translated_count}/{total}")
    print(f"Untranslated: {total-translated_count}")

    # Update header
    for entry in entries:
        if not entry['msgid']:
            entry['translated'] = entry['msgstr'].replace(
                'PO-Revision-Date: 2026-01-26 20:28+0800',
                'PO-Revision-Date: 2026-03-28 00:00+0900'
            ).replace(
                'X-Generator: Poedit 3.5',
                'X-Generator: Claude Code Translation Tool'
            )
            break

    print(f"Writing translated file to {OUTPUT_FILE}...")
    write_po_file(entries, OUTPUT_FILE)
    print("Done!")

    # Write untranslated list for reference
    with open(OUTPUT_FILE.replace('.po', '_untranslated.txt'), 'w', encoding='utf-8') as f:
        for msg in untranslated:
            f.write(msg + '\n')
    print(f"Untranslated list written to ja_untranslated.txt")

if __name__ == '__main__':
    main()
