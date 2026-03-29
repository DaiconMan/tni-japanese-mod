#!/usr/bin/env python3
"""
Generate wiki_translations.py from real_untranslated_v2.txt
Produces t() calls with Japanese translations for all wiki/help entries.
"""

import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "real_untranslated_v2.txt")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "wiki_translations.py")


def parse_entries(filepath):
    """Parse the real_untranslated_v2.txt file into a list of (entry_num, ctx, msgid) tuples."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    entries = []
    pattern = r"=== ENTRY (\d+) ctx=(.*?) ===\n(.*?)\n=== END ==="
    for m in re.finditer(pattern, content, re.DOTALL):
        entry_num = int(m.group(1))
        ctx = m.group(2).strip()
        msgid = m.group(3).strip()
        entries.append((entry_num, ctx, msgid))
    return entries


def escape_for_python(s):
    """Escape a string for use inside a Python double-quoted string."""
    s = s.replace("\\", "\\\\")
    s = s.replace('"', '\\"')
    s = s.replace("\n", "\\n")
    return s


# Build translations dict: entry_num -> japanese translation
# We translate every entry by hand for quality.
TRANSLATIONS = {}

# Entry 0: "title long title" - skip (placeholder)
TRANSLATIONS[0] = None

# Entry 1: DNS server wiki article
TRANSLATIONS[1] = (
    "[color=skyblue][url]デバイス[/url][/color]は、[color=yellow]USEスタック[/color]に"
    "「[color=lightsalmon][reply-dns-queries][/color]」という[color=skyblue][url]USE[/url][/color]"
    "を持っている場合、DNSサーバーとして機能できます。これは「[color=orange]dns-lite[/color]」や"
    "「[color=orange]dns-server[/color]」などの[color=skyblue][url]プログラム[/url][/color]を実行することで実現できます。\n\n"
    "デバイスにはDNS解決トラフィックを処理するのに十分な帯域幅容量も必要です。"
)

# Entry 2: DNS resolution issues
TRANSLATIONS[2] = (
    "右の画像はDNS解決に関する問題を示しています。\n\n"
    "最初の画像では、デバッガーがDNSサーバーに到達できません。\n\n"
    "2番目の画像では、「[color=orange]nosuchthing.com[/color]」のDNSエントリが存在しません。"
)

# Entry 3: WIP link
TRANSLATIONS[3] = (
    "おっと...クリックしたリンクはまだ作成中のようです...\n\n"
    "Wikiでお困りですか？[color=yellow]F8キー[/color]でご意見をお聞かせください。"
)

# Entry 4: Title
TRANSLATIONS[4] = "USEサービング要素"

# Entry 5: Short description
TRANSLATIONS[5] = "ネットワーク上のリソースです。"

# Entry 6: Title with acronym
TRANSLATIONS[6] = "USEサービング要素 (USE)"

# Entry 7: USE explanation
TRANSLATIONS[7] = (
    "「[color=yellow]USE[/color]」は「[color=yellow]Use Serving Element[/color]」の略称で、"
    "デバイスやユーザー上で特定の用途を提供するリソースです。単一のUSEは[color=skyblue][url]watch[/url][/color]"
    "ルーチンで観察すると、角括弧「[ ... ]」で囲まれて表示されます。"
)

# Entry 8: USE produced by producer
TRANSLATIONS[8] = (
    "USEは[color=skyblue][url]プロデューサー[/url][/color]ユーザーによって生産されます。"
    "例えば、上の画像に示されたユーザー行動は[color=skyblue][url]Surveyor[/url][/color]を使用して、"
    "2種類のUSE「[color=lightsalmon][political,read-text,read-news][/color]」と"
    "「[color=lightsalmon][read-text,post-text][/color]」を生産しています。"
)

# Entry 9: USE produced by program
TRANSLATIONS[9] = (
    "USEは実行中の[color=skyblue][url]プログラム[/url][/color]によっても生産されます。"
    "例えば、上の画像に示された「[color=orange]dns-lite[/color]」プログラムは"
    "[color=skyblue][url]program[/url][/color]ルーチンを使用すると、"
    "USE「[color=lightsalmon][reply-dns-queries][/color]」を生産します。"
)

# Entry 10: Producer limit
TRANSLATIONS[10] = (
    "任意の時点で、[color=yellow]プロデューサーは消費されるまで一定の上限までUSEを生成できます[/color]。"
)

# Entry 11: Title
TRANSLATIONS[11] = "USEの消費"

# Entry 12: USE consumption
TRANSLATIONS[12] = (
    "USEは[color=skyblue][url]エンドユーザー[/url][/color]の[color=skyblue][url]コンシューマー[/url][/color]行動によって"
    "消費され、[color=yellow]満足度レベルを上昇[/color]させます。USE消費はUSE仕様によって定義されます。"
    "以下の画像に示された行動を考えてみましょう:"
)

# Entry 13: User types
TRANSLATIONS[13] = (
    "ユーザーにはそれぞれ異なる[color=yellow]タイプ[/color]があり、満足度の達成方法に影響します。\n\n"
    "一般的に、[color=skyblue][url]居住者の家族や単身ユーザー[/url][/color]（例：[color=orange]Net Nester[/color]）は"
    "ネットワークを使ってブラウジングやネットワークサービスへのアクセスを行います。"
    "つまり、ネットワーク経由で[color=skyblue][url]コンテンツ[/url][/color]にアクセス（消費）できると満足度が上がります。"
    "これらのユーザー行動は[color=yellow][i]コンシューマー行動[/i][/color]に分類されます。\n\n"
    "一方、[color=skyblue][url]企業レベルのユーザータイプ[/url][/color]（例：[color=orange]WireSync News[/color]）は"
    "ネットワークを使ってコンシューマーにリーチします。彼らの[color=skyblue][url]コンテンツ[/url][/color]が"
    "他のエンドユーザーに消費されると満足度が上がります。"
    "これらの行動は[color=yellow][i]プロデューサー行動[/i][/color]に分類されます。"
)

# Entry 14: Transformers
TRANSLATIONS[14] = (
    "最後に、[color=yellow][i]トランスフォーマー[/i][/color]と呼ばれる特別なタイプのユーザーがいます。"
    "これらのユーザーは本質的にコンシューマーですが、見返りに何かを生産します。"
    "概念的には、独立したコンテンツクリエイターです。"
)

# Entry 15: Consumer behavior importance
TRANSLATIONS[15] = (
    "コンシューマー行動は[color=skyblue][url]USE[/url][/color]仕様と重要度係数によって定義されます。\n\n"
    "重要度が高いほど、行動が満たされた（または満たされなかった）場合の満足度への影響が大きくなります。"
)

# Entry 16: Satisfying behavior
TRANSLATIONS[16] = (
    "行動を満たすには、ユーザーはまず[color=skyblue][url]DNS[/url][/color]サーバーにアクセスして"
    "訪問先のアドレスを解決する必要があります。これは、ユーザーが選択した訪問先プロバイダーのDNSマッピングが必要です。\n\n"
    "アドレスを取得すると、ユーザーは宛先から互換性のあるUSEの消費を試みます。"
    "ユーザーが正常に消費できない原因にはさまざまな要因が考えられます。"
    "以下は理由の非網羅的なリストです:\n\n"
    "1. ユーザーがネットワークに接続されていない。\n"
    "2. 宛先（例：企業エンドポイント）がネットワークに接続されていない。\n"
    "3. ユーザーから宛先へのルーティングルールがない（ルーター経由で接続されている場合）。\n"
    "4. ファイアウォールポリシーによりブロックされている（ファイアウォール経由で接続されている場合）。\n"
    "5. インラインデバイスの帯域幅が枯渇している（例：スイッチの過負荷）。\n"
    "6. 宛先のUSEが不足している（例：企業の過負荷/DDoS攻撃）。\n\n"
    "さらに、DNSマッピングで[color=orange]間違った宛先アドレス[/color]を設定すると、"
    "ユーザーが間違った場所から消費しようとするため、消費アクションが失敗します。"
)

# Entry 17: Surveyor for consumer issues
TRANSLATIONS[17] = (
    "[color=skyblue][url]Surveyor[/url][/color]アプリケーションは、コンシューマーのネットワーク問題を"
    "解決する際に必須のツールです。ユーザーが直面する問題は、特定のユーザーの詳細ビューの"
    "「問題と苦情」セクションに記録されます。"
)

# Entry 18: Producer behavior
TRANSLATIONS[18] = (
    "プロデューサー行動は[color=skyblue][url]USE[/url][/color]仕様、"
    "[color=skyblue][url]ドメイン名[/url][/color]、および訪問者クォータ"
    "（行動インサイトセクションの「[color=yellow]visits/required[/color]」ラベルに表示）によって定義されます。"
)

# Entry 19: Producer satiety
TRANSLATIONS[19] = (
    "プロデューサーの満足度は、ホスティングしている各サービスの平均クォータ実績によって決まります。"
    "各サービスのクォータは、その特定の生産[color=skyblue][url]USE[/url][/color]仕様のプロデューサーの容量も示しています。\n\n"
    "例えば、上のビューでは、サービス「[color=orange]textfirsthand.biz[/color]」に現在3人の訪問者がいますが、"
    "最大15人まで対応可能です。\n\n"
    "生産行動のドメイン名は、コンシューマーが「[i]見る[/i]」ものです。"
    "したがって、コンシューマーを正しいプロデューサーに誘導するドメイン名の"
    "[color=skyblue][url]DNSマッピング[/url][/color]が必要です。"
)

# Entry 20: VLAN
TRANSLATIONS[20] = (
    "Tower Networking Inc.では、[color=yellow]VLAN[/color]（仮想ローカルエリアネットワーク）を使用して、"
    "[color=skyblue][url]ネットワークスイッチ[/url][/color]の特定のネットワークポートを"
    "特定のブロードキャストドメインに割り当てることができます。"
    "ブロードキャストドメインとは、同じドメイン上のすべてのデバイスが互いにブロードキャストでき、"
    "事実上同じ「ネットワーク」上にあることを意味します。\n\n"
    "VLANなしの非マネージドネットワークスイッチでは、すべてのポートが同じブロードキャストドメインにあります。"
    "つまり、ユーザー/デバイスがそのスイッチでトラバーサルを実行すると、"
    "同じスイッチ上の他のすべてのデバイスを訪問する可能性があり、スイッチの実効帯域幅が低下します。\n\n"
    "ポートに「タグ」を付けることで、トラバーサルをスイッチ上の関連デバイスのみに制限できます。"
    "次のアニメーションは2つのVLANスイッチを示しています。"
)

# Entry 21: VLAN observations
TRANSLATIONS[21] = (
    "以下の観察が可能です:\n\n"
    "1. スイッチでのトラバーサルは、リクエスト元と同じタグのポートのみに制限されます。"
    "スイッチ1では、タグ[color=magenta]#BBB[/color]のポートのみがトラバーサルされます。\n"
    "2. トラバーサルは、スイッチを出た（イグレスした）後に異なるタグを「使用」できます。"
    "スイッチ2では、接続ポート（ポート2）にタグ[color=magenta]#AAA[/color]が付けられており、"
    "AliceがBobに正常に到達できます。\n\n"
    "VLANは無関係なトラフィックが他のノードに到達するのを防ぎます。"
    "アニメーションの例では、CharlieとDaveの帯域幅はAliceのトラバーサルによって浪費されません。"
)

# Entry 22: Debugger device
TRANSLATIONS[22] = (
    "[color=yellow]デバッガー[/color][color=skyblue][url]デバイス[/url][/color]は、"
    "[color=skyblue][url]netsh[/url][/color][color=skyblue][url]アプリケーション[/url][/color]を使用して"
    "トラブルシューティングや設定作業を行うための2ポートデバイスです。\n\n"
    "[color=yellow]デバイスの設定やトラブルシューティング[/color]を行うには、"
    "デバッガーに[color=skyblue][url]電源[/url][/color]が入っており、"
    "[color=yellow]デバッガーとデバイスの間[/color]に[color=skyblue][url]ネットワーク経路[/url][/color]が"
    "存在する必要があります。\n\n"
    "デバッガーをデータセンターに配置し、コアスイッチに直接接続することで、"
    "1台のデバッガーでデータセンター全体のトラブルシューティング/設定が可能になります。"
)

# Entry 23: Direct connection setup
TRANSLATIONS[23] = (
    "右の図は、デバッガーからデバイスへの直接接続のセットアップを示しています。\n\n"
    "これにより、デバッガーはこのデバイスでコマンドを実行できます。"
)

# Entry 24: Switch setup
TRANSLATIONS[24] = (
    "より良いセットアップは、デバッガーをスイッチ経由で接続することです。"
    "これにより、デバッガーはスイッチを通じて接続されたすべてのデバイスでコマンドを実行できます。\n\n"
    "右の例では、ケーブル配線を変更することなく、デバッガーはデバイスAとデバイスBの両方を"
    "デバッグおよび設定できます。"
)

# Entry 25: lstdbg and scan commands
TRANSLATIONS[25] = (
    "現在アクセス可能なデバッガーの一覧を表示するには、「[color=yellow]lstdbg[/color]」コマンドを使用します。"
    "デバッガーのリストとその[color=skyblue][url]論理アドレス[/url][/color]が表示されます。\n\n"
    "次に、「[color=yellow]scan[/color]」コマンドを使用して、デバッガーからアクセス可能なデバイスの一覧を表示できます。"
    "デバッガーのアドレスが[color=orange]63168[/color]の場合、"
    "「[color=yellow]scan devices using 63168[/color]」と入力します。\n\n"
    "scanコマンドは、デバッガーからアクセス可能なデバイスとその対応するネットワークアドレスのリストを表示します。\n\n"
    "表示されたデバイスアドレスに対して「[color=yellow]watch[/color]」コマンドを使用すると、"
    "デバッガー上にデバイスの詳細情報が表示されます。例えば、スキャンされたデバイスアドレスが"
    "[color=orange]41216[/color]の場合、「[color=yellow]watch 41216 using 63168[/color]」と入力します。"
)

# Entry 26: always routine shortcut
TRANSLATIONS[26] = (
    "常に同じデバッガーからデバッグする場合、毎回デバッガーのアドレスを入力するのは面倒かもしれません。\n\n"
    "[color=skyblue][url]alwaysルーチン[/url][/color]コマンドを使用して、"
    "使用するデフォルトデバッガーを設定しましょう。\n\n"
    "例えば、デバッガーのアドレスが[color=orange]51727[/color]で常にそれを使いたい場合、"
    "「[color=yellow]always using 51727[/color]」と入力します。\n\n"
    "これにより、デバッガー関連のコマンドを「using ...」の部分なしで入力できるようになります。\n\n"
    "つまり、「[color=yellow]scan devices using 51727[/color]」と入力する代わりに、"
    "「[color=yellow]scan devices[/color]」とだけ入力すればよくなります。"
)

# Entry 27: man command
TRANSLATIONS[27] = (
    "いつでも[color=skyblue][url]netsh[/url][/color]ガイドを参照できます。"
    "「[color=yellow]man[/color]」コマンド（manualの略）はコマンドの詳細を調べるのに便利です。"
    "使用するには、「[color=yellow]man[/color]」または"
    "「[color=yellow]man[/color] [color=magenta]<調べたいプログラム名>[/color]」と入力してください。"
)

# Entry 28: Device definition
TRANSLATIONS[28] = (
    "[color=yellow]デバイス[/color]は、[color=skyblue][url]電源供給[/url][/color]や"
    "[color=skyblue][url]ネットワーク接続[/url][/color]が可能な動作ユニットです。\n\n"
    "電源が入ると、デバイスは[color=skyblue][url]プログラム[/url][/color]を実行し、"
    "[color=skyblue][url]USE[/url][/color]を生産してネットワーク機器として機能します。"
    "通常、ネットワーク接続されたデバイスは[color=skyblue][url]デバッガー[/url][/color]を使用した"
    "[color=skyblue][url]ルーチン[/url][/color]でアクセスできます。"
)

# Entry 29: Hovering over device
TRANSLATIONS[29] = (
    "[color=yellow]マウスをデバイスの上に置く[/color]と、デバイスの製品名、電源状態、"
    "[color=skyblue][url]ハードウェアアドレス[/url][/color]、設定された"
    "[color=skyblue][url]ネットワークアドレス[/url][/color]、"
    "[color=skyblue][url]指定DNSサーバーアドレス[/url][/color]などの重要な情報が表示されます。\n\n"
    "デフォルトでは、購入したばかりのデバイスにはネットワークアドレスや指定DNSサーバーが"
    "割り当てられていないため、ホバーパネルにこれらの情報は表示されません。"
)

# Entry 30: Purchasing devices
TRANSLATIONS[30] = (
    "[color=yellow]デバイス[/color]は[color=skyblue][url]DMARKET[/url][/color]にある"
    "さまざまな販売業者から購入できます。"
)

# Entry 31: Bandwidth capacity
TRANSLATIONS[31] = (
    "Tower Networking Inc.では、すべての[color=skyblue][url]デバイス[/url][/color]には有限の"
    "[color=yellow]帯域幅容量[/color]があります（イージーモードでプレイしている場合を除く）。\n\n"
    "デバイスの帯域幅が枯渇すると、[color=skyblue][url]ネットワークトラバーサル[/url][/color]を"
    "処理できなくなり、その影響はデバイスを物理的に見るか、[color=skyblue][url]watch[/url][/color]などの"
    "[color=skyblue][url]netsh[/url][/color]ルーチンを使用することで確認できます。"
)

# Entry 32: Inspecting bandwidth
TRANSLATIONS[32] = (
    "デバイスの帯域幅容量は、[color=skyblue][url]netsh[/url][/color]アプリケーションの"
    "[color=skyblue][url]net[/url][/color]ルーチンまたは[color=skyblue][url]watch[/url][/color]ルーチンで"
    "確認できます。[color=yellow]ネットワーク負荷[/color]が常に100%の場合、"
    "デバイスは[color=yellow]過負荷[/color]になっている可能性があります。"
)

# Entry 33: Risers bandwidth
TRANSLATIONS[33] = (
    "[color=skyblue][url]ライザー[/url][/color]にも帯域幅容量があり、"
    "[color=skyblue][url]Tower Link[/url][/color]アプリケーションで表示されます。"
    "「[color=yellow]utilization (traversals/tick)[/color]」の上限として表示されます。"
    "使用率が常に100%に達している場合、リンクは[color=yellow]過負荷[/color]です。"
)

# Entry 34: DNS behind routers
TRANSLATIONS[34] = (
    "Tower Networking Inc.では、すべてのユーザートラバーサルは宛先アドレスを取得するために"
    "[color=skyblue][url]DNS[/url][/color]解決を必要とします。デフォルトでは、DNS解決は"
    "特定の宛先アドレスを持たない[color=skyblue][url]ネットワークトラバーサル[/url][/color]"
    "（つまりブロードキャスト）です。\n\n"
    "これは、トラバーサルが[color=skyblue][url]ドメイン名[/url][/color]を解決しようとして"
    "すべてのノードを訪問することを意味します。[color=skyblue][url]スイッチのみ[/url][/color]の"
    "ネットワークでは機能しますが、ルーターのデフォルトでない"
    "[color=skyblue][url]経路[/url][/color]にDNSサーバーがある場合、トラバーサルは到達できません。"
)

# Entry 35: 3 solutions
TRANSLATIONS[35] = (
    "この問題を解決する方法は3つあります:\n\n"
    "1. [color=yellow]デフォルトルート[/color]を常にDNSサーバーがあるネットワーク"
    "（つまり[color=7FFFD4]ポート1[/color]）を指すように設定できます。\n"
    "2. [color=orange]ALICE[/color]に[color=yellow]指定DNSサーバーアドレス[/color]を設定して、"
    "DNS解決トラバーサルに特定の宛先アドレスを持たせることができます。\n"
    "3. ルーターの各側にDNSサーバーを配置します。\n\n"
    "ネットワークのセットアップ方法は自由に選択できます。"
    "理想的な解決策は規模や状況によって異なります。"
    "独自のアプローチを作成するために解決策を組み合わせることも可能です。"
)

# Entry 36: Solution 1 - default route
TRANSLATIONS[36] = (
    "これは最も簡単な解決策です。[color=skyblue][url]netsh[/url][/color]の"
    "[color=skyblue][url]route[/url][/color]ルーチンを使用して、"
    "[color=skyblue][url]ルーター[/url][/color]のデフォルトルートを設定するだけです。\n\n"
    "コマンド: [color=yellow]route default via [color=orange]port1[/color] on [color=magenta]<ルーター1のアドレス>[/color][/color]"
)

# Entry 37: Solution 1 limitation
TRANSLATIONS[37] = (
    "この解決策は小規模なネットワークでは機能しますが、ルーターの数が増えると、"
    "DNSサーバーのあるネットワークへのデフォルトルーティングパスを追跡するのが難しくなる場合があります。"
)

# Entry 38: Solution 2 - designated DNS
TRANSLATIONS[38] = (
    "この解決策はユーザーとルーターの設定が必要です。"
    "多くのユーザーに一括で指定DNSサーバーアドレスを設定するには、"
    "[color=skyblue][url]DHCP[/url][/color]の使用が必要になる場合があります。\n\n"
    "この解決策を例題に適用するには、[color=skyblue][url]netsh[/url][/color]の"
    "[color=skyblue][url]net[/url][/color]ルーチンで指定DNSサーバーアドレスを設定します。\n\n"
    "コマンド: [color=yellow]net dns set [color=orange]@dns-1[/color] on [color=magenta]<ALICEのアドレス>[/color][/color]\n\n"
    "次に、[color=skyblue][url]netsh[/url][/color]の[color=skyblue][url]route[/url][/color]ルーチンを使用して、"
    "ルーターにDNS用のルートを追加する必要があります。\n\n"
    "コマンド: [color=yellow]route add [color=orange]@dns-1[/color] via [color=orange]port1[/color] on [color=magenta]<ルーター1のアドレス>[/color][/color]"
)

# Entry 39: Designated DNS example
TRANSLATIONS[39] = (
    "例えば、ユーザー「[color=orange]lumbering-civet[/color]」はDNSサーバーとして"
    "アドレス「[color=orange]@mydns[/color]」を使用するように設定されています。\n\n"
    "これは、このユーザーがDNS解決を実行しようとする際、"
    "アドレス「[color=orange]@mydns[/color]」を持つデバイス/ユーザーにのみ接続を試みることを意味します。"
)

# Entry 40: Solution 2 scalability
TRANSLATIONS[40] = (
    "この解決策は新しいルーターが追加された際に容易にスケールできます。"
    "新しいルーターはデフォルトルートチェーンをたどる必要なく、"
    "DNSルートをルーター1に向けるだけで済みます。\n\n"
    "ただし、多くのユーザーに指定DNSサーバーアドレスを設定するのは現実的でない場合があるため、"
    "この解決策は通常[color=skyblue][url]DHCP[/url][/color]サーバーの助けが必要です。"
)

# Entry 41: Solution 3 - DNS everywhere
TRANSLATIONS[41] = (
    "この解決策はネットワークやルーティングの設定なしで動作します。"
    "ただし、実装コストが高く、電源コンセントの制限によりDNSサーバーをあらゆる場所に"
    "配置するのが物理的に困難な場合があります。\n\n"
    "しかし、この解決策にはDNSトラバーサルトラフィックがローカライズされるという別の利点があります。"
    "すべてのユーザーが常にDNSトラバーサルを実行するため、"
    "広域ネットワーク全体のトラフィック量を半減させることができます。"
)

# Entry 42: DNS traffic localized
TRANSLATIONS[42] = (
    "この例では、各サブネットワークに独自のDNSサーバーがあるため、"
    "DNSトラフィックはルーター1を通過しないことに注目してください。"
)

# Entry 43: Network firewall
TRANSLATIONS[43] = (
    "Tower Networking Inc.では、[color=yellow]ネットワークファイアウォール[/color]を使用して、"
    "[color=skyblue][url]悪意のあるユーザー[/url][/color]からの不要なトラフィック"
    "（例：Webスクレイピング、サービス拒否攻撃）をフィルタリングできます。\n\n"
    "パケットフィルタリングはトラフィックがファイアウォールに入る前に行われます。"
    "つまり、ドロップされたトラフィックはファイアウォールの[color=skyblue][url]帯域幅[/url][/color]に影響しません。"
)

# Entry 44: Firewall configuration
TRANSLATIONS[44] = (
    "ファイアウォールは[color=skyblue][url]netsh[/url][/color]アプリケーションの"
    "[color=skyblue][url]firewallルーチン[/url][/color]で設定できます。\n\n"
    "[color=yellow]ファイアウォールルール[/color]を追加して、以下に基づいてトラバーサルを許可/拒否できます:\n\n"
    "1. 送信元[color=skyblue][url]論理アドレス[/url][/color]\n"
    "2. 宛先[color=skyblue][url]論理アドレス[/url][/color]（またはその欠如）\n"
    "3. [color=skyblue][url]トラフィックタイプ[/url][/color]\n\n"
    "トラバーサルがファイアウォールに到達すると、ファイアウォールはすべてのポリシーを昇順でチェックします。"
    "トラバーサルの属性に一致する明示的な許可/拒否ポリシーがある場合、"
    "そのポリシーが適用され、トラバーサルの通過が許可または拒否されます。\n\n"
    "ファイアウォールルールの設定には注意が必要です。ロックアウトされるリスクがあります"
    "（例：[color=skyblue][url]firewallルーチン[/url][/color]でさらなる設定のために"
    "[color=palegreen]tcp/23[/color]トラフィックを許可する前にデフォルト許可ポリシーを削除する）。"
)

# Entry 45: Hardware vs network address on firewalls
TRANSLATIONS[45] = (
    "ファイアウォールでは、[color=skyblue][url]ハードウェアアドレス[/url][/color]と"
    "[color=skyblue][url]ネットワークアドレス[/url][/color]には重要な違いがあります。\n\n"
    "[color=00FA9A]ハードウェアアドレス[/color]で指定されたポリシーのアドレスには、"
    "[color=yellow]完全一致[/color]が行われます。つまり、以下のポリシー:\n\n"
    "[color=orange]allow from 12345 to 56789[/color]\n\n"
    "は、ハードウェアアドレス「[color=00FA9A]12345[/color]」を持つデバイス/ユーザーからの、"
    "宛先ハードウェアアドレスが「[color=00FA9A]56789[/color]」のトラバーサルの通過を許可します。\n\n"
    "[color=FF0565]ネットワークアドレス[/color]で指定されたポリシーのアドレスには、"
    "[color=yellow]プレフィックス一致[/color]が行われます。つまり、以下のポリシー:\n\n"
    "[color=orange]allow from @net1/ to @net2/[/color]\n\n"
    "は、プレフィックス「[color=FF0565]@net1/[/color]」を持つネットワークアドレス"
    "（例：「[color=FF0565]@net1/alice[/color]」）のデバイス/ユーザーからの、"
    "宛先ネットワークアドレスのプレフィックスが「[color=FF0565]@net2/[/color]」"
    "（例：「[color=FF0565]@net2/server[/color]」）に一致するトラバーサルの通過を許可します。"
)

# Entry 46: Hardware addresses
TRANSLATIONS[46] = (
    "Tower Networking Inc.では、[color=00FA9A]ハードウェアアドレス[/color]はネットワーク対応の"
    "[color=skyblue][url]デバイス[/url][/color]と[color=skyblue][url]ユーザー[/url][/color]に"
    "自動的に割り当てられるランダムな[color=yellow]一意のアドレス[/color]です。\n\n"
    "ハードウェアアドレスは[color=yellow]1～5桁[/color]です。"
    "[color=skyblue][url]netsh[/url][/color]ルーチンを実行する際にデバイスやユーザーを参照するために使用されます。\n\n"
    "[color=00FA9A]ハードウェアアドレス[/color]は[color=FF0565][url]ネットワークアドレス[/url][/color]と並ぶ"
    "[color=skyblue][url]論理アドレス[/url][/color]の一種です。"
)

# Entry 47: Logical addresses
TRANSLATIONS[47] = (
    "Tower Networking Inc.では、[color=yellow]論理アドレス[/color]"
    "（単に「[color=yellow]アドレス[/color]」や「[color=yellow]addr[/color]」とも呼ばれる）は"
    "[color=00FA9A][url]ハードウェアアドレス[/url][/color]または"
    "[color=FF0565][url]ネットワークアドレス[/url][/color]として表されます。"
    "これらのアドレスは論理的に1つのデバイスまたはユーザーを指します。"
    "ネットワークアドレスの場合、論理アドレスはデバイスやユーザーのグループを指すこともあります。\n\n"
    "ほとんどの[color=skyblue][url]netsh[/url][/color]コマンドは論理アドレスを入力として受け付けます。"
)

# Entry 48: Network addresses
TRANSLATIONS[48] = (
    "Tower Networking Inc.では、[color=FF0565]ネットワークアドレス[/color]はプレイヤーが"
    "割り当てるアドレス（デバイスエイリアス）です。\n\n"
    "ネットワークアドレスは[color=yellow]常にエイリアス記号@で始まり[/color]、"
    "[color=yellow]9文字以下の英数字[/color]に制限されます。"
    "ダッシュ「-」、アンダースコア「_」、スラッシュ「/」も使用できます。\n\n"
    "プレイヤーが割り当てるため、[i]技術的には[/i]"
    "[color=yellow]複数のデバイスが同じネットワークアドレスを持つ[/color]ことが可能です。\n\n"
    "[color=skyblue][url]netsh[/url][/color]で使用する際、ネットワークアドレスはハードウェアアドレスと"
    "互換性がありますが、[color=skyblue][url]ルーティング[/url][/color]に関しては互換性がないことを"
    "理解しておくことが重要です！\n\n"
    "例えば、デバイスのハードウェアアドレスが「[color=00FA9A]12345[/color]」で、"
    "ネットワークアドレス「[color=FF0565]@sv1[/color]」が割り当てられている場合、"
    "訪問者が「[color=FF0565]@sv1[/color]」（つまり[color=skyblue][url]DNS[/url][/color]サーバーから取得）を"
    "訪問しようとしているとき、[color=skyblue][url]ネットワークルート[/url][/color]"
    "「[color=00FA9A]12345[/color] via [color=7FFFD4]port1[/color]」は機能しません。"
    "これは、訪問者のトラフィックがルーターに到達した際、ルーターは"
    "「[color=00FA9A]12345[/color]」と「[color=FF0565]@sv1[/color]」が同じものであることを"
    "知らないためです。この問題を解決するには2つの方法があります:\n\n"
    "1. ルート設定にネットワークアドレスを使用する（例：「[color=FF0565]@sv1[/color] via [color=7FFFD4]port1[/color]」）。\n"
    "2. DNSエントリのマッピングをハードウェアアドレス「[color=00FA9A]12345[/color]」に設定する。\n\n"
    "簡潔に言えば、デバイスのハードウェアアドレスとネットワークアドレスの間に相関関係はありません。"
)

# Entry 49: Playing without network addresses
TRANSLATIONS[49] = (
    "[color=yellow]ネットワークアドレスを使用せずにゲームをプレイすることもできます[/color]。"
    "[color=skyblue][url]netsh[/url][/color]で使用されるすべてのルーチンは、"
    "[color=00FA9A][url]ハードウェアアドレス[/url][/color]とネットワークアドレスのどちらでも"
    "互換的に使用できます。\n\n"
    "ただし、ネットワークアドレスはいくつかの理由でゲームの重要な要素です。"
)

# Entry 50: Assigning network addresses
TRANSLATIONS[50] = (
    "ネットワークアドレスは[color=skyblue][url]netルーチン[/url][/color]を使用して割り当てることができます。"
)

# Entry 51: Why network addresses matter
TRANSLATIONS[51] = (
    "[color=skyblue][url]ルーター[/url][/color]を使用する場合、ネットワークアドレスを使って"
    "デバイスやユーザーをグループ化し、ルーティングテーブルの設定を簡素化できます。"
    "また、デバイスやユーザーに意味やラベルを割り当てて、その目的や場所を追跡しやすくすることもできます。\n\n"
    "例えば、ランダムに生成されたハードウェアアドレス「[color=00FA9A]12381[/color]」よりも、"
    "「[color=FF0565]@dns-1[/color]」がDNSサーバーであることの方が分かりやすいでしょう。\n\n"
    "さらに、「[color=FF0565]@f1/server[/color]」が1階のサーバーであることは、"
    "物理的に探すよりも簡単に分かります。\n\n"
    "以下の図は、ネットワークアドレスが割り当てられたノードを持つネットワーク例を示しています。"
    "ルートテーブルがノード間のトラフィックを処理するために容易に作成できることに注目してください。"
)

# Entry 52: Common network address for DNS
TRANSLATIONS[52] = (
    "例えば、大規模なDNSサービスを運用するために、複数のDNSサーバープログラムを実行している"
    "サーバーに共通のネットワークアドレス（例：「[color=FF0565]@bigdns[/color]」）を割り当てる方法があります。"
    "これらのサーバーを異なる場所に配置してDNSトラフィックをローカライズできます。"
    "ユーザーには[color=skyblue][url]指定DNSサーバー[/url][/color]として"
    "「[color=FF0565]@bigdns[/color]」を割り当てることで、"
    "DNSトラフィック負荷をネットワーク全体に分散できます。"
)

# Entry 53: Network router
TRANSLATIONS[53] = (
    "Tower Networking Inc.では、[color=yellow]ネットワークルーター[/color]は"
    "トラバーサルを特定のリンクにルーティングでき、"
    "[color=skyblue][url]ネットワークトラバーサル[/url][/color]からの"
    "[color=yellow]不要な訪問を削減[/color]します。"
    "ルーターはルーティングテーブルによって定義され、"
    "基本的に宛先とトラバーサルが到達するために通過すべきポートのリストです。\n\n"
    "このゲームでは、ルーターをネットワークトラフィックの方向案内板と考えることができます。\n\n"
    "ルーターで接続された[color=skyblue][url]デバイス[/url][/color]/"
    "[color=skyblue][url]ユーザー[/url][/color]は、以下のルールに従って"
    "ルーターを通じた[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行できます:\n\n"
    "1. トラバーサルに特定の宛先アドレスがない場合、[color=yellow]デフォルト[/color]ルートを通ります。\n"
    "2. トラバーサルに特定の宛先[color=skyblue][url]ハードウェアアドレス[/url][/color]または"
    "[color=skyblue][url]ネットワークアドレス[/url][/color]があるが、"
    "ルーティングテーブルにアドレスが一致しない場合、[color=yellow]デフォルト[/color]ルートを通ります。\n"
    "3. トラバーサルに特定の宛先[color=skyblue][url]ハードウェアアドレス[/url][/color]があり、"
    "ルーティングテーブルで[color=yellow]完全一致する宛先アドレス[/color]がある場合、"
    "指定されたルートを通ります。\n"
    "4. トラバーサルに特定の宛先[color=skyblue][url]ネットワークアドレス[/url][/color]があり、"
    "ルーティングテーブルで[color=yellow]宛先アドレスのプレフィックス[/color]が一致する場合、"
    "指定されたルートを通ります。\n"
    "5. トラバーサルに特定の宛先[color=skyblue][url]ネットワークアドレス[/url][/color]があり、"
    "ルーティングテーブルで[color=yellow]複数のプレフィックスが一致[/color]する場合、"
    "[color=yellow]最長プレフィックス[/color]で指定されたルートを通ります。\n\n"
    "例を使ってルールを理解しましょう。"
)

# Entry 54: Router example observations
TRANSLATIONS[54] = (
    "以下に注目してください:\n\n"
    "1. 最初のトラバーサルは[color=yellow]特定の宛先アドレスのない[/color]トラバーサルです。"
    "[color=orange]ALICE[/color]に指定DNSアドレスがありません。"
    "そのため[color=yellow]default[/color]エントリが使用され、"
    "トラバーサルは[color=7FFFD4]ポート1[/color]に送られます。\n"
    "2. 2番目のトラバーサルはDNS解決フェーズで取得したアドレスを使用し、"
    "[color=00FA9A]12345[/color]に設定されます。これは[color=yellow]特定の宛先アドレスを持つ[/color]"
    "トラバーサルです。この例では、[color=00FA9A]12345[/color]のルートエントリが存在し、"
    "トラバーサルは[color=7FFFD4]ポート2[/color]に送られます。\n"
    "3. もしルーター1が[color=skyblue][url]ネットワークスイッチ[/url][/color]だった場合、"
    "2番目のトラバーサルでは、より低いポートである[color=7FFFD4]ポート1[/color]を先に試すため、"
    "1回の不要な訪問が発生します。\n"
    "4. したがって、ルーターの使用によりトラバーサルが最適化され、不要な帯域幅の使用が削減されます。\n\n"
    "次に、すべてのケースの例を見てみましょう。"
)

# Entry 55: No destination address
TRANSLATIONS[55] = (
    "宛先アドレスのないトラバーサルは、常にルーターの[color=yellow]default[/color]ルートを使用します。"
)

# Entry 56: Hardware address exact match
TRANSLATIONS[56] = (
    "[color=skyblue][url]ハードウェアアドレス[/url][/color]の場合、"
    "ルートを使用するには[color=yellow]完全一致[/color]が必要です。\n\n"
    "この例では、ハードウェアアドレスが[color=orange]12345[/color]なので、"
    "テーブルの2番目のルートが使用され、"
    "トラバーサルは[color=7FFFD4]ポート2[/color]に送られます。"
)

# Entry 57: Hardware address no match -> default
TRANSLATIONS[57] = (
    "この例では、ハードウェアアドレスが[color=orange]123[/color]なので、"
    "どのルートも一致しないため、テーブルの[color=yellow]default[/color]ルートが使用されます。"
    "これにより、トラバーサルは[color=7FFFD4]ポート3[/color]に送られます。"
)

# Entry 58: Network address longest prefix match
TRANSLATIONS[58] = (
    "[color=skyblue][url]ネットワークアドレス[/url][/color]の場合、"
    "[color=yellow]最長プレフィックス一致[/color]のルートが選択されます。\n\n"
    "この例では、ネットワークアドレスが[color=orange]@dns[/color]なので、"
    "テーブルの3番目のルートが最長一致プレフィックスとなり、"
    "トラバーサルは[color=7FFFD4]ポート1[/color]に送られます。"
    "ルート[color=orange]@dns/s-1[/color]はより長いプレフィックスかもしれませんが、"
    "[color=orange]@dns[/color]のプレフィックスではありません。"
)

# Entry 59: Prefix match example 2
TRANSLATIONS[59] = (
    "この例では、ネットワークアドレスが[color=orange]@dns-123[/color]なので、"
    "テーブルの3番目のルートが依然として最長一致プレフィックスとなり、"
    "トラバーサルは[color=7FFFD4]ポート1[/color]に送られます。"
    "つまり、[color=orange]@dns[/color]で始まり、かつ[color=orange]@dns/s-1[/color]で"
    "始まらない宛先ネットワークアドレスはすべて[color=7FFFD4]ポート1[/color]を通じてルーティングされます。"
)

# Entry 60: Longest prefix match example
TRANSLATIONS[60] = (
    "この例では、ネットワークアドレスが[color=orange]@dns/s-123[/color]なので、"
    "テーブルの4番目のルートが最長一致プレフィックスとなり、"
    "トラバーサルは[color=7FFFD4]ポート2[/color]に送られます。"
    "[color=orange]@dns/s-123[/color]は[color=orange]@dns[/color]もプレフィックスとして持ちますが、"
    "[color=yellow]最長一致[/color]のみが選択されます。"
)

# Entry 61: No prefix match
TRANSLATIONS[61] = (
    "この例では、ネットワークアドレスが[color=orange]@d[/color]なので、"
    "ルートテーブルに一致するプレフィックスが見つからず、"
    "トラバーサルはデフォルトルート経由で[color=7FFFD4]ポート3[/color]に送られます。"
)

# Entry 62: Router usage motivation
TRANSLATIONS[62] = (
    "ネットワーク上のユーザー数が増え、サービスが追加されるにつれて、ネットワークの規模は拡大し、"
    "ある時点で[color=skyblue][url]帯域幅の使用[/url][/color]が問題になります"
    "（イージーモードでプレイしている場合を除く）。\n\n"
    "[color=skyblue][url]ネットワークスイッチ[/url][/color]のみを使用したネットワークを考えてみましょう。"
)

# Entry 63: Switch-only inefficiency
TRANSLATIONS[63] = (
    "[color=orange]ALICE[/color]が[color=orange]BOB[/color]を訪問するために、"
    "[color=yellow]黄色[/color]で表示されたすべてのノードが不必要に訪問されます"
    "（詳細は[color=skyblue][url]ネットワークスイッチング[/url][/color]を参照）。"
    "帯域幅が浪費されます。\n\n"
    "デバイスの[color=skyblue][url]帯域幅が枯渇[/url][/color]すると、"
    "トラバーサルを許可しなくなり、他のユーザーやネットワークの機能に影響を与えます。\n\n"
    "ここで、高度に相互接続されたノード（つまりネットワークのコアバックボーン）に"
    "2台のルーターを戦略的に配置した場合を考えてみましょう。"
    "不要に訪問されるノード数を最小限に抑えることができます。"
)

# Entry 64: Network switch
TRANSLATIONS[64] = (
    "Tower Networking Inc.では、[color=yellow]ネットワークスイッチ[/color]は"
    "[color=skyblue][url]ネットワークトラバーサル[/url][/color]を容易にするための"
    "低コストで非効率的な相互接続方法です。"
    "[color=yellow]設定不要でそのまま使用できます[/color]。\n\n"
    "スイッチで接続された[color=skyblue][url]デバイス[/url][/color]/"
    "[color=skyblue][url]ユーザー[/url][/color]は、"
    "スイッチを通じた[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行できます。\n\n"
    "[b]経験豊富な方への注意[/b]: このゲームのネットワークメカニズムは実世界とは異なります。"
    "実世界ではネットワークスイッチはCAMテーブルとスパニングツリープロトコルを使用して"
    "ネットワーク接続グラフを構築しますが、このゲームではスイッチはリンク層が"
    "シミュレートされていないためハブとして機能します。デバイス上でARPは発生しません！\n\n"
    "スイッチの動作を理解するために、常に[color=orange]BOB[/color]に到達したい"
    "ユーザー[color=orange]ALICE[/color]の例を考えます。"
    "例を簡単に追えるよう、[color=skyblue][url]ネットワークトラバーサル[/url][/color]について"
    "先に読んでおくことをお勧めします。"
)

# Entry 65: Switch observations
TRANSLATIONS[65] = (
    "サンプルネットワークの例から、以下に注目してください:\n\n"
    "1. トラバーサルはスイッチに到達すると常に最も低いポートから開始します。\n"
    "2. [color=orange]DAVE[/color]はより高いポートにいるため訪問されませんでした。"
    "トラバーサルはポート上で[color=orange]BOB[/color]に正常に到達した時点で終了しました。\n\n"
    "スイッチはデイジーチェーン接続が可能です。"
)

# Entry 66: Daisy chain observations
TRANSLATIONS[66] = (
    "デイジーチェーンの例から以下を観察してください:\n\n"
    "1. 宛先が[color=orange]BOB[/color]の場合、スイッチ3にあり"
    "[color=orange]ECHO[/color]より[color=orange]ALICE[/color]に近いにもかかわらず、"
    "[color=orange]ECHO[/color]がより低いポート経由のパス上にあるため先に訪問されます。\n"
    "2. 宛先が[color=orange]DAVE[/color]の場合、[color=orange]ALICE[/color]から2ホップ離れているにもかかわらず、"
    "最後に訪問されます。トラバーサルはネットワーク全体に及びます。\n"
    "3. つまり、[color=yellow]スイッチの低いポートを通じて接続されたすべてのノードは、"
    "トラバーサルが高いポートの宛先に到達できるようになる前にまず訪問されます[/color]。\n\n"
    "観察3から、スイッチは使用が簡単ですが、不要なトラバーサルを防ぐために"
    "大規模ネットワークでは慎重に使用する必要があることが分かります。"
    "ポートが単純に接続されると、大規模ネットワークではスイッチネットワークは非常に非効率的になります。\n\n"
    "以下のネットワークを考えてみましょう:"
)

# Entry 67: Yellow nodes bandwidth
TRANSLATIONS[67] = (
    "先ほどの観察から、[color=orange]ALICE[/color]が宛先に到達するために、"
    "[color=yellow]黄色[/color]で示されたすべてのノードが訪問されることが分かります"
    "（低いポートが常に先に訪問されることを思い出してください）。\n\n"
    "スイッチのみのセットアップでは、不要な訪問によりネットワーク全体の"
    "[color=skyblue][url]帯域幅[/url][/color]がすぐに枯渇します。"
)

# Entry 68: Network taps
TRANSLATIONS[68] = (
    "Tower Networking Inc.では、[color=yellow]ネットワークタップ[/color]を使用して"
    "デバイスを通過するトラフィックを検査できます。タッピングは設定ミスや"
    "ユーザー・デバイスからの予期しない動作を発見するのに役立ちます。\n\n"
    "ポートトラフィック統計の限定的なビューしか持たない[color=skyblue][url]watchルーチン[/url][/color]とは異なり、"
    "ネットワークタッピングではタップを流れる[color=skyblue][url]ネットワークトラバーサル[/url][/color]の"
    "[color=skyblue][url]トラフィックタイプ[/url][/color]を確認できます。\n\n"
    "ネットワークタッピングは[color=skyblue][url]pcapルーチン[/url][/color]で実行できます。"
)

# Entry 69: Traffic types
TRANSLATIONS[69] = (
    "Tower Networking Inc.では、各[color=skyblue][url]ネットワークトラバーサル[/url][/color]には"
    "[color=yellow]トラフィックタイプ[/color]があります。トラフィックタイプは"
    "[color=skyblue][url]ネットワークタップ[/url][/color]でのみ確認でき、"
    "[color=skyblue][url]ネットワークファイアウォール[/url][/color]でブロックまたは許可できます。\n\n"
    "以下はトラバーサルで一般的に使用されるトラフィックタイプの例です:\n\n"
    "[color=palegreen]tcp/23[/color] - [color=skyblue][url]netルーチン[/url][/color]や"
    "[color=skyblue][url]programルーチン[/url][/color]などの各種"
    "[color=skyblue][url]デバッガー[/url][/color]がデバイスの設定に使用します。\n"
    "[color=palegreen]udp/53[/color] - [color=skyblue][url]DNS[/url][/color]トラフィック。\n"
    "[color=palegreen]tcp/80[/color] - 一般[color=skyblue][url]サービス[/url][/color]\n"
    "[color=palegreen]udp/67[/color] - [color=skyblue][url]DHCP[/url][/color]トラフィック\n \n"
    "[color=skyblue][url]ユーザー[/url][/color]が使用する他の多くのトラフィックタイプがあります。"
    "一部のトラフィックタイプは[color=skyblue][url]悪意のある[/url][/color]ものかもしれません。"
)

# Entry 70: Network traversal
TRANSLATIONS[70] = (
    "Tower Networking Inc.では、デバイスとユーザーは[color=lightsalmon][url]USE[/url][/color]を"
    "消費/変換するために[color=yellow]ネットワークトラバーサル[/color]を実行します。"
    "簡単に言えば、ネットワークトラバーサルはコンシューマーからの「ネットワークリクエスト」です。\n\n"
    "デバイス/ユーザーが接続を試みると、ソースをグラフのルートとして"
    "[s]幅優先探索 (BFS)[/s] [color=red]（この動作は0.8.24で変更されました）[/color]"
    " [color=yellow]深さ優先探索 (DFS)[/color]グラフトラバーサルが実行されます。"
    "例を使ってこの仕組みを見てみましょう。以下のサンプルネットワークを考えます。"
)

# Entry 71: ALICE consumer example
TRANSLATIONS[71] = (
    "このネットワークでは、[color=orange]ALICE[/color]は[color=skyblue][url]コンシューマー[/url][/color]で、"
    "[color=orange]NEWS COMPANY[/color]が提供する[color=skyblue][url]サービス[/url][/color]に"
    "アクセスしたいと考えています。\n\n"
    "[color=orange]ALICE[/color]はまず、サービスのドメイン名を"
    "[color=skyblue][url]論理アドレス[/url][/color]に解決するために"
    "[color=skyblue][url]DNS[/url][/color]サーバーにアクセスする必要があります。"
    "そのため、[color=orange]ALICE[/color]は特定の宛先を指定せずに"
    "[color=skyblue][url]USE[/url][/color] [color=lightsalmon][reply-dns-queries][/color]を"
    "消費するトラバーサルを実行します。"
)

# Entry 72: Using DNS address
TRANSLATIONS[72] = (
    "DNSサーバーから取得したアドレスを使用して、[color=orange]ALICE[/color]は"
    "サービス[color=lightpink]usefulnet.org[/color]のUSEを消費するため、"
    "特定の[color=skyblue][url]ハードウェアアドレス[/url][/color] "
    "[color=00FA9A]12345[/color]に対して別のトラバーサルを実行します。"
)

# Entry 73: Successful access notes
TRANSLATIONS[73] = (
    "[color=orange]ALICE[/color]は[color=orange]NEWS COMPANY[/color]でホストされている"
    "サービスに正常にアクセスできました。\n\n"
    "以下に注目してください:\n"
    "1. DFSトラバーサルは[color=yellow]常に[/color]任意のデバイスの最も低いポートから開始します。\n"
    "2. この例は、[color=orange]ALICE[/color]が[color=orange]NEWS COMPANY[/color]に"
    "[color=yellow]到達[/color]できた方法のみを示しています。"
    "[color=orange]NEWS COMPANY[/color]に[color=orange]ALICE[/color]が消費するための"
    "[color=skyblue][url]USE[/url][/color]が十分に残っていない場合もあります"
    "（例：他の[color=skyblue][url]コンシューマー[/url][/color]による過負荷、DDoS攻撃）。\n"
    "3. [color=skyblue][url]DNS[/url][/color]マッピングが[color=red]間違っている[/color]場合、"
    "[color=orange]ALICE[/color]が取得した[color=yellow]宛先アドレス[/color]により、"
    "互換性のある[color=skyblue][url]USE[/url][/color]があっても"
    "[color=orange]NEWS COMPANY[/color]を見逃す可能性があります。\n\n"
    "この例から、ネットワークトラバーサルには主に2つのタイプがあることが分かります。"
    "特定の宛先アドレス[color=yellow]あり[/color]または[color=yellow]なし[/color]の消費トラバーサルです。"
)

# Entry 74: Broadcast traversal
TRANSLATIONS[74] = (
    "ある意味、このトラバーサルタイプは「[color=yellow]ブロードキャスト[/color]」のように機能します。"
    "トラバーサルはリクエストの目的（つまりUSEの消費）が達成されると停止します。"
    "この種のトラバーサルの例には以下があります:\n\n"
    "1. [color=skyblue][url]未指定DNS[/url][/color]解決。\n"
    "2. [color=skyblue][url]DHCP[/url][/color]リクエスト。\n"
    "3. デバッガーを使用したネットワーク[color=skyblue][url]scan[/url][/color]ルーチン。\n\n"
    "これらのトラバーサルは[color=skyblue][url]ルーター[/url][/color]に近づくと常に「default」ルートを選択します。"
    "また、[color=skyblue][url]ファイアウォール[/url][/color]に近づくと"
    "[color=yellow]Destination: Any[/color]ルールに一致します。\n\n"
    "以下は、特定のアドレスのないトラバーサルの例です: "
    "[color=orange]ALICE[/color]がDHCPリクエスト"
    "（指定DNSサーバーアドレスとネットワークアドレスを自動的に設定するため）を実行します。"
)

# Entry 75: DHCP traversal observations
TRANSLATIONS[75] = (
    "以下に注目してください:\n\n"
    "1. トラバーサルはDHCPサーバー1からの消費に成功した後に停止します。\n"
    "2. DNSサーバーとDHCPサーバー2にはトラフィックがなく、ネットワーク帯域幅は影響を受けません。\n"
    "3. News Companyは互換性のあるUSEを持っていなくても、より低いポートにあったため訪問されます。\n\n"
    "DHCPサーバー1がダウンした場合（例：高負荷、マルウェアの影響、電源障害）に何が起こるか考えてみましょう。"
)

# Entry 76: DHCP server 1 down
TRANSLATIONS[76] = (
    "予想通り、[color=orange]ALICE[/color]は代わりにDHCPサーバー2から消費します。"
    "この場合、トラバーサルトラフィックはDNSサーバーにも「到達」し、利用可能な帯域幅が減少します。"
)

# Entry 77: Unicast traversal
TRANSLATIONS[77] = (
    "このトラバーサルでは、トラバーサルの目的を達成する前に[color=yellow]宛先アドレス[/color]が"
    "まず[color=yellow]一致[/color]する必要があります。"
    "このアドレスは[color=skyblue][url]ハードウェアアドレス[/url][/color]に対しては"
    "「[color=yellow]ユニキャスト[/color]」として機能し、"
    "[color=skyblue][url]ネットワークアドレス[/url][/color]に対しては"
    "「[color=yellow]マルチキャスト[/color]」として機能する場合があります。\n\n"
    "特定アドレストラバーサルの例には以下があります:\n\n"
    "1. デバッガーを使用した[color=skyblue][url]ping[/url][/color]または"
    "[color=skyblue][url]trace[/url][/color]ルーチン。\n"
    "2. DNS解決後のユーザーによるサービスアクセス。\n"
    "3. [color=skyblue][url]指定DNS[/url][/color]解決。\n\n"
    "理解を深めるために例を考えましょう: [color=orange]ALICE[/color]はハードウェアアドレス"
    "[color=00FA9A]12345[/color]を取得し、サービス[color=lightpink]pearlforum.net[/color]の"
    "USE [color=lightsalmon][read-text,post-text][/color]を消費しようとしています。"
)

# Entry 78: Unicast traversal observations
TRANSLATIONS[78] = (
    "以下に注目してください:\n\n"
    "1. Elleのフォーラムに互換性のあるUSEがあっても、宛先アドレスが一致しないため"
    "[color=orange]ALICE[/color]はそこから消費しません。\n"
    "2. DFSの性質上、[color=orange]ALICE[/color]はスイッチ1のポート2の直接の隣接ノードを"
    "試す前に、グラフの奥深くまでトラバーサルします。\n\n"
    "次に[color=skyblue][url]ネットワークアドレス[/url][/color]の例を見てみましょう。"
)

# Entry 79: Network address traversal
TRANSLATIONS[79] = (
    "以下に注目してください:\n\n"
    "1. ネットワークアドレスとハードウェアアドレスの間に相関関係はありません。"
    "MEDIAサーバー1のネットワークアドレスが未設定の場合、"
    "特定の宛先ネットワークアドレスを持つトラバーサルはそこに到達しません。\n\n"
    "MEDIAサーバー1が利用不能になったとします:"
)

# Entry 80: Network address group behavior
TRANSLATIONS[80] = (
    "この動作は、特定の宛先アドレスのないトラバーサルとかなり似ていることに注目してください。"
    "ネットワークアドレスにより、デバイスのグループが同じアドレスに応答できます。"
)

# Entry 81: always routine
TRANSLATIONS[81] = (
    "[color=yellow]alwaysルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man always[/color]」と入力するとマニュアルにアクセスできます。"
    "入力するコマンドの長さを短縮するために、シェルのデフォルト値を指定するために使用されます。"
)

# Entry 82: always using command detail
TRANSLATIONS[82] = (
    "[color=yellow]always using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドはすべてのnetshルーチンの「[color=yellow]using[/color]」キーワードに対する"
    "[color=yellow]デフォルトデバッガーアドレス[/color]を設定します。\n\n"
    "デバッガー[color=orange]4567[/color]を使用する場合の効果を考えてみましょう:\n\n"
    "デフォルトデバッガーアドレスなしでは、デバイス/ユーザーとやり取りするコマンドは常に"
    "「[color=yellow]using[/color]」キーワードでどのデバッガーから実行するか指定する必要があります:\n"
    "「[color=orange]net show on 123 using 4567[/color]」\n"
    "「[color=orange]scan firewalls using 4567[/color]」\n\n"
    "デフォルトデバッガーアドレス設定後（「[color=orange]always using 4567[/color]」実行後）、"
    "コマンドが短く簡単になります:\n"
    "「[color=orange]net show on 123[/color]」\n"
    "「[color=orange]scan firewalls[/color]」\n\n"
    "[color=yellow]always using[/color]コマンドでデフォルトデバッガーを設定しても、"
    "「[color=yellow]using[/color]」キーワードで別のデバッガーを指定（デフォルトをオーバーライド）できます。\n\n"
    "例えば、「[color=orange]always using 4567[/color]」実行後に[color=orange]net show[/color]コマンドを実行し、"
    "1つのコマンドだけ別のデバッガー[color=orange]89123[/color]を使用してデバイスをスキャンしたい場合:\n"
    "「[color=orange]net show on 123[/color]」\n"
    "「[color=orange]scan devices using 89123[/color]」\n\n"
    "最初のコマンドはデバッガー[color=orange]4567[/color]で実行され、"
    "2番目はデバッガー[color=orange]89123[/color]で実行されます。"
    "ネットワークの異なる部分にあるデバッガーがターゲットデバイスに"
    "[color=skyblue][url]到達[/url][/color]できない場合に必要になることがあります。\n\n"
    "さらに、「[color=yellow]using[/color]」キーワードは[color=skyblue][url]ハードウェアアドレス[/url][/color]と"
    "[color=skyblue][url]ネットワークアドレス[/url][/color]の両方を受け付けます。"
    "つまり、デバッガーにネットワークアドレス[color=orange]@mydebug[/color]が割り当てられている場合、"
    "[color=orange]always using @mydebug[/color]でネットワークアドレスを使った"
    "デフォルトデバッガーの設定も可能です。"
)

# Entry 83: dhcp routine
TRANSLATIONS[83] = (
    "[color=yellow]dhcpルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man dhcp[/color]」と入力するとマニュアルにアクセスできます。"
    "[color=skyblue][url]DHCP[/url][/color]サーバーのオプションを設定するために使用されます。"
)

# Entry 84: dhcp traffic type
TRANSLATIONS[84] = (
    "このルーチンはDHCPサーバーにアクセスするためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。"
)

# Entry 85: dhcp show
TRANSLATIONS[85] = (
    "[color=yellow]dhcp show on [color=magenta]<対象DHCPのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象サーバー[/color]のDHCPオプション情報を表示します。\n\n"
    "例:\n"
    "「[color=orange]dhcp show on 123 using 456[/color]」\n"
    "「[color=orange]dhcp show on @mydhcp[/color]」"
)

# Entry 86: dhcp option
TRANSLATIONS[86] = (
    "[color=yellow]dhcp option prefix on [color=magenta]<対象DHCPのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "[color=magenta]対象サーバー[/color]の[color=yellow]PrefixのDHCPオプション[/color]を設定します。\n\n"
    "[color=yellow]dhcp option dns on [color=magenta]<対象DHCPのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "[color=magenta]対象サーバー[/color]の[color=yellow]DNSのDHCPオプション[/color]を設定します。\n\n"
    "例:\n"
    "「[color=orange]dhcp option prefix @net1- on 123 using 456[/color]」\n"
    "「[color=orange]dhcp option dns @dns on @mydhcp[/color]」"
)

# Entry 87: dns routine
TRANSLATIONS[87] = (
    "[color=yellow]dnsルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man dns[/color]」と入力するとマニュアルにアクセスできます。"
    "[color=skyblue][url]DNSエントリ[/url][/color]の作成/クリアに使用されます。"
)

# Entry 88: dns traffic type
TRANSLATIONS[88] = (
    "このルーチンはデバッガーからDNSサーバーに到達するためにトラフィックタイプ"
    "[color=palegreen]udp/53[/color]を使用します。"
)

# Entry 89: dns map
TRANSLATIONS[89] = (
    "[color=yellow]dns map [color=magenta]<ドメイン名>[/color] as [color=magenta]<解決先アドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta][url]ドメイン名[/url][/color]を"
    "[color=magenta][url]論理アドレス[/url][/color]にマッピングします。"
    "デバッガーがいずれかのDNSサーバーに到達できる必要があります。"
    "DNSエントリはグローバルなので、どのDNSサーバーに到達するかは関係ありません。\n\n"
    "例:\n"
    "「[color=orange]dns map towernews.org as 12345 using 456[/color]」\n"
    "「[color=orange]dns map towernews.org as @net1/townews[/color]」"
)

# Entry 90: dns lookup
TRANSLATIONS[90] = (
    "[color=yellow]dns lookup [color=magenta]<ドメイン名>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "デバッガーを使用して[color=magenta][url]ドメイン名[/url][/color]のテストDNS解決を実行します。\n\n"
    "例:\n"
    "「[color=orange]dns lookup towernews.org using 456[/color]」\n"
    "「[color=orange]dns lookup foostore.com[/color]」"
)

# Entry 91: dns clear
TRANSLATIONS[91] = (
    "[color=yellow]dns clear [color=magenta]<ドメイン名>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta][url]ドメイン名[/url][/color]のDNSエントリを削除します。"
    "デバッガーがいずれかのDNSサーバーに到達できる必要があります。"
    "DNSエントリはグローバルなので、どのDNSサーバーに到達するかは関係ありません。\n\n"
    "例:\n"
    "「[color=orange]dns clear towernews.org as 12345 using 456[/color]」\n"
    "「[color=orange]dns clear foostore.com[/color]」"  # note: original has unclosed quote
)

# Entry 92: firewall routine
TRANSLATIONS[92] = (
    "[color=yellow]firewallルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man firewall[/color]」と入力するとマニュアルにアクセスできます。"
    "[color=skyblue][url]ネットワークファイアウォール[/url][/color]を管理するために使用されます。"
)

# Entry 93: firewall traffic type
TRANSLATIONS[93] = (
    "このルーチンはファイアウォールにアクセスして設定するために"
    "トラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。"
)

# Entry 94: firewall show
TRANSLATIONS[94] = (
    "[color=yellow]firewall show on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象ファイアウォール[/color]のファイアウォールポリシーを表示します。\n\n"
    "例:\n"
    "「[color=orange]firewall show on 123 using 456[/color]」\n"
    "「[color=orange]firewall show on @fw1[/color]」"
)

# Entry 95: firewall allow/deny
TRANSLATIONS[95] = (
    "[color=yellow]firewall allow [color=magenta]<トラフィックタイプ>[/color] from [color=magenta]<送信元アドレス>[/color] to [color=magenta]<宛先アドレス>[/color] on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象ファイアウォール[/color]に新しい「[color=yellow]allow[/color]」ポリシーを追加します。"
    "[color=magenta][url]トラフィックタイプ[/url][/color]、[color=magenta]送信元アドレス[/color]、"
    "[color=magenta]宛先アドレス[/color]の指定は任意です。未指定の場合は[color=yellow]any[/color]として扱われます。\n\n"
    "例:\n"
    "「[color=orange]firewall allow 123 to 456 on 789 using 101[/color]」 - "
    "送信元[color=orange]123[/color]から宛先[color=orange]456[/color]をファイアウォール[color=orange]789[/color]で明示的に許可します。\n\n"
    "「[color=orange]firewall allow udp/53 to @dns on 789[/color]」 - "
    "トラフィック[color=orange]udp/53[/color]で宛先プレフィックス[color=orange]@dns[/color]を"
    "ファイアウォール[color=orange]789[/color]で明示的に許可します。\n\n"
    "「[color=orange]firewall allow tcp/80 on @fw1[/color]」 - "
    "トラフィック[color=orange]tcp/80[/color]をファイアウォール[color=orange]@fw1[/color]で"
    "すべての送信元からすべての宛先に対して明示的に許可します。\n\n"
    "[color=yellow]firewall deny [color=magenta]<トラフィックタイプ>[/color] from [color=magenta]<送信元アドレス>[/color] to [color=magenta]<宛先アドレス>[/color] on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "同様のコマンドで[color=magenta]対象ファイアウォール[/color]に新しい「[color=yellow]deny[/color]」ポリシーを追加します。"
    "[color=magenta][url]トラフィックタイプ[/url][/color]、[color=magenta]送信元アドレス[/color]、"
    "[color=magenta]宛先アドレス[/color]の指定は任意です。未指定の場合は[color=yellow]any[/color]として扱われます。\n\n"
    "例:\n"
    "「[color=orange]firewall deny from @user2 on 789[/color]」 - "
    "送信元アドレスプレフィックス[color=orange]@user2[/color]から任意の宛先への通信を"
    "ファイアウォール[color=orange]789[/color]で明示的に拒否します。\n\n"
    "「[color=orange]firewall deny tcp/22 on 789[/color]」 - "
    "トラフィック[color=orange]tcp/22[/color]をファイアウォール[color=orange]789[/color]で"
    "すべての送信元からすべての宛先に対して明示的に拒否します。"
)

# Entry 96: firewall default allow/deny
TRANSLATIONS[96] = (
    "[color=yellow]firewall default allow on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象ファイアウォール[/color]のデフォルトポリシー"
    "（ポリシーが一致しない場合）を[color=green]allow[/color]に設定します。\n\n"
    "[color=yellow]firewall default deny on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象ファイアウォール[/color]のデフォルトポリシー"
    "（ポリシーが一致しない場合）を[color=red]deny[/color]に設定します。\n\n"
    "例:\n"
    "「[color=orange]firewall default deny port0 on 123 using 456[/color]」\n"
    "「[color=orange]firewall default allow on @fw1[/color]」"
)

# Entry 97: firewall remove
TRANSLATIONS[97] = (
    "[color=yellow]firewall remove [color=magenta]<ポリシーID>[/color] on [color=magenta]<対象ファイアウォールのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象ファイアウォール[/color]の"
    "[color=magenta]ポリシーID[/color]で指定されたファイアウォールポリシーを削除します。"
    "ポリシーIDの一覧は「firewall show」コマンドで取得できます。"
    "同じコマンドで複数のポリシーを削除できます。\n\n"
    "例:\n"
    "「[color=orange]firewall remove #0 on 123 using 456[/color]」\n"
    "「[color=orange]firewall remove #1 #2 on @fw1[/color]」"
)

# Entry 98: lstdbg routine
TRANSLATIONS[98] = (
    "[color=yellow]lstdbgルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man lstdbg[/color]」と入力するとマニュアルにアクセスできます。"
    "有効な（[color=skyblue][url]電源が入った[/url][/color]）"
    "[color=skyblue][url]デバッガー[/url][/color]を一覧表示するために使用されます。\n\n"
    "使い方はとても簡単で、「[color=yellow]lstdbg[/color]」と入力するだけでアクティブなデバッガーの一覧が表示されます。"
    "[color=skyblue][url]alwaysルーチン[/url][/color]で現在指定されているデバッガーは緑色で表示されます。"
)

# Entry 99: net routine
TRANSLATIONS[99] = (
    "[color=yellow]netルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man net[/color]」と入力するとマニュアルにアクセスできます。"
    "タワー内の[color=skyblue][url]デバイス[/url][/color]や"
    "[color=skyblue][url]ユーザー[/url][/color]のネットワークパラメータを設定するために使用されます。"
)

# Entry 100: net traffic type
TRANSLATIONS[100] = (
    "このルーチンはデバッガーからターゲットに到達するためにトラフィックタイプ"
    "[color=palegreen]tcp/23[/color]を使用します。"
)

# Entry 101: net show
TRANSLATIONS[101] = (
    "[color=yellow]net show on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象[/color]のネットワーク情報（例："
    "[color=skyblue][url]ネットワークアドレス[/url][/color]、"
    "[color=skyblue][url]帯域幅容量[/url][/color]、"
    "[color=skyblue][url]DHCP[/url][/color]の有効/無効、"
    "[color=skyblue][url]DNS[/url][/color]情報）を表示します。\n\n"
    "例:\n"
    "「[color=orange]net show on 123 using 456[/color]」\n"
    "「[color=orange]net show on @mydev[/color]」"
)

# Entry 102: net address set/clear
TRANSLATIONS[102] = (
    "[color=yellow]net address set [color=magenta]<アドレス>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "[color=yellow]net address clear on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "最初のコマンドは[color=magenta]対象[/color]の[color=skyblue][url]ネットワークアドレス[/url][/color]を"
    "[color=magenta]アドレス[/color]に設定します。\n"
    "2番目のコマンドは[color=magenta]対象[/color]のネットワークアドレスをクリアします。\n\n"
    "例:\n"
    "「[color=orange]net address set @myaddr on 123 using 456[/color]」\n"
    "「[color=orange]net address clear on 123[/color]」"  # original has unclosed quote
)

# Entry 103: net dns set/clear
TRANSLATIONS[103] = (
    "[color=yellow]net dns set [color=magenta]<DNSサーバーアドレス>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "[color=yellow]net dns clear on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "最初のコマンドは[color=magenta]対象[/color]の"
    "[color=skyblue][url]指定DNSサーバーアドレス[/url][/color]を[color=magenta]アドレス[/color]に設定します。\n"
    "2番目のコマンドは[color=magenta]対象[/color]の指定DNSサーバーアドレスをクリアします。\n\n"
    "例:\n"
    "「[color=orange]net dns set @dns1 on 123 using 456[/color]」\n"
    "「[color=orange]net dns clear on 123[/color]」"  # original has unclosed quote
)

# Entry 104: net dhcp enable/disable/request
TRANSLATIONS[104] = (
    "[color=yellow]net dhcp enable on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "[color=magenta]対象[/color]で[color=skyblue][url]DHCP[/url][/color]を有効にします。"
    "有効にすると、約10秒ごとに自動的にDHCPリクエストが実行されます。\n\n"
    "[color=yellow]net dhcp disable on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "[color=magenta]対象[/color]で[color=skyblue][url]DHCP[/url][/color]を無効にします。\n\n"
    "[color=yellow]net dhcp request on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "[color=magenta]対象[/color]からDHCPリクエストを直ちに実行します。\n\n"
    "例:\n"
    "「[color=orange]net dhcp enable on 123 using 456[/color]」\n"
    "「[color=orange]net dhcp disable on 123[/color]」\n"  # original has unclosed quote
    "「[color=orange]net dhcp request on 123[/color]」"  # original has unclosed quote
)

# Entry 105: pcap routine
TRANSLATIONS[105] = (
    "[color=yellow]pcapルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man pcap[/color]」と入力するとマニュアルにアクセスできます。"
    "[color=skyblue][url]ネットワークタップ[/url][/color]でパケットキャプチャ/検査を開始するために使用されます。"
)

# Entry 106: pcap traffic type
TRANSLATIONS[106] = (
    "このルーチンはパケットキャプチャプロセスを開始するためにトラフィックタイプ"
    "[color=palegreen]tcp/23[/color]を使用します。"
)

# Entry 107: pcap command
TRANSLATIONS[107] = (
    "[color=yellow]pcap [color=magenta]<対象タップのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "このコマンドは[color=magenta]対象ネットワークタップ[/color]にパケットキャプチャ/検査を開始するよう指示します。\n\n"
    "例:\n"
    "「[color=orange]pcap on @mytap using 456[/color]」\n"
    "「[color=orange]pcap on 123[/color]」"
)

# Entry 108: program routine
TRANSLATIONS[108] = (
    "[color=yellow]programルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man program[/color]」と入力するとマニュアルにアクセスできます。"
    "[color=skyblue][url]デバイス[/url][/color]にプログラムをインストールして実行するために使用されます。"
)

# Entry 109: program traffic type
TRANSLATIONS[109] = (
    "このルーチンはターゲットにプログラムをアクセス・インストール/実行するために"
    "トラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。"
)

# Entry 110: program list
TRANSLATIONS[110] = (
    "[color=yellow]program list[/color]\n\n"
    "このコマンドはサーバーにインストール可能なプログラムの一覧を表示します。"
    "リストには[color=skyblue][url]プログラム[/url][/color]を識別するためのキーワードである"
    "プログラムの[color=yellow]リリース名[/color]が含まれます。\n\n"
    "例:\n"
    "「[color=orange]program list[/color]」"
)

# Entry 111: program describe
TRANSLATIONS[111] = (
    "[color=yellow]program describe [color=magenta]<リリース名>[/color][/color]\n\n"
    "このコマンドは[color=magenta]リリース名[/color]で指定されたプログラムの情報を表示します。\n\n"
    "例:\n"
    "「[color=orange]program describe dns-server[/color]」"
)

# Entry 112: program view installed/running
TRANSLATIONS[112] = (
    "[color=yellow]program view installed on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象デバイス[/color]にインストールされているプログラムを一覧表示します。\n\n"
    "例:\n"
    "「[color=orange]program view installed on 123 using 456[/color]」\n"
    "「[color=orange]program view installed on @dns[/color]」\n\n"
    "[color=yellow]program view running on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象デバイス[/color]で実行中のプログラムとそのプロセスID（pid）を一覧表示します。\n\n"
    "例:\n"
    "「[color=orange]program view running on 123 using 456[/color]」\n"
    "「[color=orange]program view running on @dns[/color]」"
)

# Entry 113: program install/uninstall
TRANSLATIONS[113] = (
    "[color=yellow]program install [color=magenta]<リリース名>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]リリース名で指定されたプログラム[/color]を"
    "[color=magenta]対象デバイス[/color]にインストールします。\n\n"
    "例:\n"
    "「[color=orange]program install kea on 123 using 456[/color]」\n"
    "「[color=orange]program install dns-lite on @dns[/color]」\n\n"
    "[color=yellow]program uninstall [color=magenta]<リリース名>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]リリース名で指定されたプログラム[/color]を"
    "[color=magenta]対象デバイス[/color]からアンインストールします。\n\n"
    "例:\n"
    "「[color=orange]program uninstall kea on 123 using 456[/color]」\n"
    "「[color=orange]program uninstall dns-lite on @dns[/color]」"
)

# Entry 114: program start
TRANSLATIONS[114] = (
    "[color=yellow]program start [color=magenta]<リリース名>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象デバイス[/color]にインストール済みの"
    "[color=magenta]リリース名で指定されたプログラム[/color]を起動します。\n\n"
    "例:\n"
    "「[color=orange]program start kea on 123 using 456[/color]」\n"
    "「[color=orange]program start dns-lite on @dns[/color]」"
)

# Entry 115: program stop
TRANSLATIONS[115] = (
    "[color=yellow]program stop [color=magenta]<リリース名>[/color] on [color=magenta]<対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象デバイス[/color]で実行中の"
    "[color=magenta]リリース名で指定されたプロセス[/color]を停止します。\n\n"
    "例:\n"
    "「[color=orange]program stop opentxt on 123 using 456[/color]」\n"
    "「[color=orange]program stop dns-lite on @dns[/color]」"
)

# Entry 116: route routine
TRANSLATIONS[116] = (
    "[color=yellow]routeルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man route[/color]」と入力するとマニュアルにアクセスできます。"
    "[color=skyblue][url]ネットワークルーター[/url][/color]を管理するために使用されます。"
)

# Entry 117: route traffic type
TRANSLATIONS[117] = (
    "このルーチンはルーターにアクセスして設定するためにトラフィックタイプ"
    "[color=palegreen]tcp/23[/color]を使用します。"
)

# Entry 118: route show
TRANSLATIONS[118] = (
    "[color=yellow]route show on [color=magenta]<対象ルーターのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象ルーター[/color]のルーティング情報を表示します。\n\n"
    "例:\n"
    "「[color=orange]route show on 123 using 456[/color]」\n"
    "「[color=orange]route show on @rt1[/color]」"
)

# Entry 119: route add
TRANSLATIONS[119] = (
    "[color=yellow]route add [color=magenta]<宛先アドレスプレフィックス>[/color] via [color=magenta]<ポートID>[/color] on [color=magenta]<対象ルーターのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象ルーター[/color]に新しいルートを追加します。"
    "追加されたルートは、[color=magenta]宛先アドレスプレフィックス[/color]が最長一致した場合に"
    "トラバーサルを[color=magenta]ポートID[/color]に送ります。"
    "ポートIDはポート番号（例：0、1）またはポート名（例：port0、port1）を受け付けます。\n\n"
    "例:\n"
    "「[color=orange]route add @net1- via port0 on 123 using 456[/color]」\n"
    "「[color=orange]route add 8183 via 1 on @rt1[/color]」"
)

# Entry 120: route default
TRANSLATIONS[120] = (
    "[color=yellow]route default via [color=magenta]<ポートID>[/color] on [color=magenta]<対象ルーターのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象ルーター[/color]のデフォルトポートを設定します。"
    "アドレスプレフィックスが一致しない場合、トラバーサルを[color=magenta]ポートID[/color]に送ります。"
    "ポートIDはポート番号（例：0、1）またはポート名（例：port0、port1）を受け付けます。\n\n"
    "例:\n"
    "「[color=orange]route default via port0 on 123 using 456[/color]」\n"
    "「[color=orange]route default via 1 on @rt1[/color]」"
)

# Entry 121: route remove
TRANSLATIONS[121] = (
    "[color=yellow]route remove [color=magenta]<ルートID>[/color] on [color=magenta]<対象ルーターのアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドは[color=magenta]対象ルーター[/color]の"
    "[color=magenta]ルートID[/color]で指定されたルートを削除します。"
    "ルートIDの一覧は「route show」コマンドで取得できます。"
    "同じコマンドで複数のルートを削除できます。\n\n"
    "例:\n"
    "「[color=orange]route remove #0 on 123 using 456[/color]」\n"
    "「[color=orange]route remove #1 #2 on @rt1[/color]」"
)

# Entry 122: scan routine
TRANSLATIONS[122] = (
    "[color=yellow]scanルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man scan[/color]」と入力するとマニュアルにアクセスできます。"
    "デバッガーから到達可能な[color=skyblue][url]デバイス[/url][/color]や"
    "[color=skyblue][url]ユーザー[/url][/color]を検出するために使用されます。"
)

# Entry 123: scan traffic type
TRANSLATIONS[123] = (
    "スキャンはデバイスを検出するためにトラフィックタイプ[color=palegreen]tcp/23[/color]を使用します。"
    "つまり、[color=palegreen]tcp/23[/color]がブロックされている場合、デバイスはスキャンに表示されません。"
)

# Entry 124: scan command
TRANSLATIONS[124] = (
    "[color=yellow]scan [color=magenta]<タイプ>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n\n"
    "このコマンドはデバッガーから[color=skyblue][url]到達可能[/url][/color]な"
    "[color=magenta]指定タイプ[/color]のネットワークデバイスまたはユーザーをスキャンします。\n\n"
    "以下はスキャン可能なタイプの一覧です。単数形と複数形の両方が受け付けられます"
    "（例：「switches」の代わりに「switch」と入力可能）。"
    "括弧内の文字でも入力できます（例：「devices」の代わりに「d」と入力可能）。\n\n"
    "1. devices (d)\n"
    "2. switches (s)\n"
    "3. routers (r)\n"
    "4. users (u)\n"
    "5. taps (t)\n"
    "6. firewalls (f)\n"
    "7. dns-servers (dns)\n"
    "8. dhcp-servers (dhcp)\n\n"
    "例:\n"
    "「[color=orange]scan devices using 456[/color]」\n"
    "「[color=orange]scan switches[/color]」\n"
    "「[color=orange]scan router[/color]」\n"
    "「[color=orange]scan r[/color]」\n"
    "「[color=orange]scan users[/color]」\n"
    "「[color=orange]scan dns[/color]」"
)

# Entry 125: trace and ping routines
TRANSLATIONS[125] = (
    "[color=yellow]traceルーチン[/color]と[color=yellow]pingルーチン[/color]は"
    "[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "ある[color=skyblue][url]デバイス[/url][/color]または"
    "[color=skyblue][url]ユーザー[/url][/color]から別のデバイス/ユーザーへの"
    "トラフィックをトレースするために使用されます。"
)

# Entry 126: trace/ping traffic types
TRANSLATIONS[126] = (
    "これらのルーチンでは、[color=skyblue][url]ファイアウォール[/url][/color]を介した接続性をテストするために"
    "異なるトラフィックタイプを指定できます。デフォルトのトラフィックタイプは[color=palegreen]icmp[/color]です。"
)

# Entry 127: trace command
TRANSLATIONS[127] = (
    "[color=yellow]trace [color=magenta]<宛先のアドレス>[/color] from [color=magenta]<送信元のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "[color=magenta]送信元[/color]に、[color=palegreen]icmp[/color]トラフィックで"
    "[color=magenta]宛先[/color]への[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行するよう指示します。\n\n"
    "[color=yellow]trace [color=magenta]<宛先>[/color] from [color=magenta]<送信元>[/color] with [color=magenta]<トラフィックタイプ>[/color] using [color=magenta]<デバッガー>[/color][/color]\n"
    "[color=magenta]送信元[/color]に、指定された[color=magenta][url]トラフィックタイプ[/url][/color]で"
    "[color=magenta]宛先[/color]への[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行するよう指示します。\n\n"
    "例:\n"
    "「[color=orange]trace 123 from @src1 using 456[/color]」\n"
    "「[color=orange]trace @dst2 from 987[/color]」\n"
    "「[color=orange]trace @net1-dns from 987 with udp/53[/color]」"
)

# Entry 128: ping command
TRANSLATIONS[128] = (
    "[color=yellow]ping [color=magenta]<宛先のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "デバッガーから[color=magenta]宛先[/color]へ[color=palegreen]icmp[/color]トラフィックで"
    "[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行します。\n\n"
    "[color=yellow]ping [color=magenta]<宛先>[/color] with [color=magenta]<トラフィックタイプ>[/color] using [color=magenta]<デバッガー>[/color][/color]\n"
    "デバッガーから[color=magenta]宛先[/color]へ指定された"
    "[color=magenta][url]トラフィックタイプ[/url][/color]で"
    "[color=skyblue][url]ネットワークトラバーサル[/url][/color]を実行します。\n\n"
    "例:\n"
    "「[color=orange]ping 123 using 456[/color]」\n"
    "「[color=orange]ping @dst2[/color]」\n"
    "「[color=orange]ping @net1-dns with udp/53[/color]」"
)

# Entry 129: watch routine
TRANSLATIONS[129] = (
    "[color=yellow]watchルーチン[/color]は[color=skyblue][url]netsh[/url][/color]のルーチンです。"
    "「[color=yellow]man watch[/color]」と入力するとマニュアルにアクセスできます。"
    "[color=skyblue][url]デバイス[/url][/color]を監視するために使用されます。"
)

# Entry 130: watch traffic type
TRANSLATIONS[130] = (
    "このルーチンは監視対象にアクセスするためにトラフィックタイプ"
    "[color=palegreen]tcp/23[/color]を使用します。"
)

# Entry 131: watch command
TRANSLATIONS[131] = (
    "[color=yellow]watch using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "このコマンドは特定のターゲットなしでモニターを開始します。"
    "監視したいデバイスにマウスを合わせると、マウス上のデバイスが監視されます。\n\n"
    "[color=yellow]watch [color=magenta]<監視対象のアドレス>[/color] using [color=magenta]<デバッガーのアドレス>[/color][/color]\n"
    "このコマンドは[color=magenta]対象[/color]を指定して監視します。"
    "他のデバイスにマウスを合わせても、ターミナルディスプレイの表示内容は変わりません。\n\n"
    "例:\n"
    "「[color=orange]watch using 456[/color]」\n"
    "「[color=orange]watch[/color]」\n"
    "「[color=orange]watch on @mydev using 456[/color]」\n"
    "「[color=orange]watch on 123[/color]」"
)

# Entry 132: DMarket application
TRANSLATIONS[132] = (
    "[color=yellow]DMarketアプリケーション[/color]は、ネットワークを運用するための"
    "[color=skyblue][url]デバイス[/url][/color]を購入できる"
    "[color=skyblue][url]アプリケーション[/url][/color]です。\n\n"
    "さまざまな販売業者やOEMメーカーがプラットフォーム上で運営しています。\n\n"
    "DMarketで購入したデバイスは指定したフロアに[color=yellow]1つずつ[/color]配送されます。"
)

# Entry 133: netsh description
TRANSLATIONS[133] = (
    "デバッガーデバイスと組み合わせて使用するコマンドラインアプリケーションです。"
)

# Entry 134: netshell application
TRANSLATIONS[134] = (
    "[color=yellow]netshellアプリケーション[/color]はネットワークとサービスのセットアップ、"
    "運用、トラブルシューティングに使用できる[color=skyblue][url]アプリケーション[/url][/color]です。\n\n"
    "下部の入力ボックスにコマンドを入力し、上部のウィンドウでコマンドの結果を確認する"
    "コマンドラインツールです。\n\n"
    "入力ボックスにコマンドを入力し、「[color=yellow]enter⏎[/color]」キーを押してコマンドを送信します。\n\n"
    "netshellはさまざまな「[color=purple]ルーチン[/color]」で構成されており、"
    "それぞれ異なる種類のデバッグ/セットアップ作業を行います。\n\n"
    "使用可能なルーチンを確認するには、「[color=yellow]man[/color]」コマンドを入力します。"
    "利用可能なルーチンのリストが表示されます。\n\n"
    "アプリケーションを終了するには、「[color=yellow]exit[/color]」と入力するか"
    "「[color=yellow]ctrl+c[/color]」を押します。"
)

# Entry 135: man command detailed
TRANSLATIONS[135] = (
    "「[color=yellow]man[/color]」コマンドはルーチン名を後に続けるとさらに多くの情報を表示できます。\n\n"
    "例として、「[color=yellow]man program[/color]」と入力すると、"
    "「[color=skyblue][url]program[/url][/color]」ルーチンの使用マニュアルが表示されます。\n\n"
    "使用ヘルプは各コマンドの使い方を理解しやすくするために色分けされています。"
    "「[color=yellow]リテラル[/color]」（そのまま入力する）は黄色でハイライトされ、"
    "「[color=magenta]変数[/color]」（使用状況に応じて変わる）はマゼンタでハイライトされます。\n\n"
    "「プログラムの説明を取得」の使用ヘルプを考えてみましょう:\n"
    "「[color=yellow]program describe[/color] [color=magenta]program_name[/color]」\n\n"
    "このコマンドを使用するには、[color=yellow]リテラル[/color]をそのまま入力し、"
    "続けて説明したい[color=magenta]プログラム名[/color]を入力します。"
    "例えば、「[color=orange]dns-server[/color]」アプリケーションを説明するには、"
    "「[color=yellow]program describe dns-server[/color]」と入力します。\n\n"
    "[color=magenta]program_name[/color]を「program_name」とそのまま入力するのではなく、"
    "[color=orange]dns-server[/color]に置き換えていることに注目してください。\n\n"
    "利用可能なプログラム名の一覧を取得するには、「[color=yellow]program list[/color]」コマンドで"
    "リストが表示されます。このコマンドは変数を必要とせず、そのまま入力できます。"
)

# Entry 136: netshell with debugger
TRANSLATIONS[136] = (
    "netshellは[color=skyblue][url]デバッガー[/url][/color]と一緒に使用します。\n\n"
    "netshで使う重要なルーチンは「[color=orange]lstdbg[/color]」ルーチンで、"
    "netshが接続可能な全[color=skyblue][url]デバッガー[/url][/color]を一覧表示します。"
    "[color=yellow]scan[/color]、[color=yellow]trace[/color]、[color=yellow]watch[/color]など"
    "大部分のルーチンは[color=skyblue][url]デバッガー[/url][/color]を通じて動作します。\n\n"
    "基本的に、デバッガーがルーチンの実行を担当します。"
    "例えば「[color=yellow]scan devices using[/color] [color=magenta]debugger_address[/color]」は、"
    "デバッガー（「[color=yellow]using[/color]」キーワードで指定された"
    "[color=skyblue][url]アドレス[/url][/color]）から"
    "[color=skyblue][url]到達可能[/url][/color]なデバイスをスキャンします。"
)

# Entry 137: Surveyor application
TRANSLATIONS[137] = (
    "[color=yellow]Surveyorアプリケーション[/color]はインターネットサービスの管轄下にある"
    "[color=skyblue][url]ユーザー[/url][/color]を観察・監視するために使用できる"
    "[color=skyblue][url]アプリケーション[/url][/color]です。"
)

# Entry 138: Basic camera movement tutorial
TRANSLATIONS[138] = (
    "[i]基本的なカメラ操作[/i]\n\n"
    "1. 右マウスボタン（ホールド＋ドラッグ）: カメラビューを回転またはパンします。\n"
    "2. 中マウスボタン（ホールド＋ドラッグ）: シーン上でカメラを移動します。\n"
    "3. マウスホイール: ズームイン・ズームアウトします。\n"
    "4. WASD + Shift: キーボードでカメラを移動します。Shiftを押し続けると高速移動します。"
)

# Entry 139: Device interaction tutorial
TRANSLATIONS[139] = (
    "[i]デバイス操作[/i]\n\n"
    "1. 左マウスボタン: デバイスを操作します（例：デバイスを掴む）。"
)

# Entry 140: Powering devices tutorial
TRANSLATIONS[140] = (
    "[i]デバイスの電源投入[/i]\n\n"
    "1. ケーブルを壁のコンセントに接続して電源を供給します。\n"
    "2. デバイスの赤い電源スイッチを切り替えて電源を入れます。"
)

# Entry 141: Mobile OS interaction
TRANSLATIONS[141] = (
    "[i]モバイルOSの操作[/i]\n\n"
    "モバイルOSを表示するには:\n"
    "1. [i][color=red]View MobileOS[/color][/i]ボタンをクリック\n"
    "2. 左ALTキーを押す\n\n"
    "モバイルOSを画面の反対側に移動するには:\n"
    "1. モバイルOS画面を中クリック"
)

# Entry 142: Basic networking commands
TRANSLATIONS[142] = (
    "[i][i][color=red]netsh[/color][/i]アプリでの基本的なネットワーキングコマンド一覧[/i]\n"
    "以下のコマンドを使用する前に、デバイス/ユーザーがケーブルでデバッガーに接続されていることを確認してください。\n\n"
    "[i][color=green]デバイス/ユーザー[/color][/i]は[i][color=green]スイッチ[/color][/i]または"
    "[i][color=green]ルーター[/color][/i]を通じて接続された後にのみ、"
    "[i][color=green]デバッガー[/color][/i]から「認識」されます。\n\n"
    "1. [i][color=yellow]lstdbg[/color][/i]: デバッガーの一覧を表示\n"
    "2. [i][color=yellow]scan devices using <debugger_address>[/color][/i]: デバッガーで接続されたデバイスをスキャン\n"
    "3. [i][color=yellow]scan users using <debugger_address>[/color][/i]: デバッガーで接続されたユーザーをスキャン\n"
    "4. [i][color=yellow]always using <debugger_address>[/color][/i]: コマンドで常にデバッガーを使用するよう設定\n\n"
    "[i][color=yellow]always using <debugger_address>[/color][/i]でデフォルトのデバッガーアドレスを設定した後は、"
    "同じ結果を得るためにデバッガーアドレスを入力する必要がありません。\n\n"
    "1. [i][color=yellow]scan users [/color][/i]: scan users using <debugger_address>と同じ結果\n"
    "2. [i][color=yellow]scan devices [/color][/i]: scan devices using <debugger_address>と同じ結果\n"
    "3. [i][color=yellow]trace <address1> from <address2>[/color][/i]: デバッガーを使用してaddress2からaddress1へのネットワークトレースを実行\n"
    "4. [i][color=yellow]ping <address1>[/color][/i]: デバッガーからデバイス/ユーザーにpingを実行\n\n"
    "ショートカットコマンド\n\n"
    "1. [i][color=yellow]scan u [/color][/i]: scan usersのショートカット\n"
    "2. [i][color=yellow]scan d [/color][/i]: scan devicesのショートカット\n\n"
    "netshの各ルーチンの使い方をより理解するには:\n\n"
    "1.[i][color=yellow] man <routine>[/color][/i]: man scan、man always、man shellなど。"
)

# Entry 143: Monitor users in Surveyor
TRANSLATIONS[143] = (
    "[i][i][color=red]Surveyor[/color][/i]アプリでユーザープロフィールを監視[/i]\n\n"
    "1. Surveyorアプリでユーザーの詳細（虫眼鏡）をクリック\n"
    "2. 「No DNS Servers for <ユーザー名> to <アクション>」に基づいてユーザーがDNSサーバーに到達できないことを確認\n"
    "3. デバッガー、スイッチ、デバイス/ユーザー間の物理接続がスイッチ/ルーターで完了していることを確認"
)

# Entry 144: Small tips
TRANSLATIONS[144] = (
    "[i]ゲーム内の小さなヒント[/i]\n\n"
    "1. デバイスにマウスを合わせるとデバイスのアドレスが表示されます\n"
    "2. デバイスを右クリックしてアドレスをコピーし、netshで右クリックしてアドレスを貼り付けられます。\n"
    "3. デバイスに物理的にアクセスできない場合（例：別のフロアにある場合）、スキャンコマンドを使用してアドレスを取得できます。"
)

# Entry 145: Riser link setup
TRANSLATIONS[145] = (
    "[i]フロア間のライザーリンク設定[/i]\n"
    "1. Tower Linkアプリを起動\n"
    "2. ポイントAのフロアとアウトレットを選択\n"
    "3. ポイントBのフロアとアウトレットを選択\n"
    "4. ドロップダウンからリンクサイズを選択\n"
    "5. 「REQUEST LINKS」をクリックしてライザー設定を確定\n"
    "6. 「VIEW LINKS」タブでライザーリンクの監視/無効化/廃止を行う\n\n"
    "注意:\n"
    "1. 帯域幅が大きいほど高価になります\n"
    "2. ポイントAとBが同じフロアにある場合、ライザー設定は高額になります。"
)

# Entry 146: Device interaction (duplicate)
TRANSLATIONS[146] = (
    "[i]デバイス操作[/i]\n"
    "1. 左マウスボタン: デバイスを操作します（例：デバイスを掴む）。"
)

# Entry 147: Powering devices (duplicate)
TRANSLATIONS[147] = (
    "[i]デバイスの電源投入[/i]\n"
    "1. ケーブルを壁のコンセントに接続して電源を供給します。\n"
    "2. デバイスの赤い電源スイッチを切り替えて電源を入れます。"
)

# Entry 148: D-Market purchasing
TRANSLATIONS[148] = (
    "D-Marketアプリを起動\n"
    "1. 検索機能またはフィルター機能を使用してカートにアイテムを追加\n"
    "2. 一部のアイテムではバリエーションを選択できます（例：イーサネットケーブル）\n"
    "3. チェックアウトをクリックし、送信ボタンで注文を確定\n"
    "4. 購入したアイテムはエレベーターで配送されます"
)

# Entry 149: Manage finance
TRANSLATIONS[149] = (
    "[i]財務管理[/i]\n\n"
    "1. 常にCredit Stackアプリを起動して財務状況を確認しましょう\n"
    "2. 財務を計画的に管理しましょう。負債はゲームオーバーにつながります"
)

# Entry 150: Apply loan
TRANSLATIONS[150] = (
    "[i]ローンの申請[/i]\n\n"
    "1. Fi$hy Loansアプリでローンを申請し、ネットワーク拡大のための初期資金を増やしましょう"
)

# Entry 151: Identify needs
TRANSLATIONS[151] = (
    "[i]プロデューサーとコンシューマーのニーズを把握[/i]\n"
    "1. Surveyorアプリを起動\n"
    "2. プロデューサーとコンシューマーのプロフィールをクリック（名前または虫眼鏡アイコンをクリック）\n"
    "3. 行動インサイトからプロデューサー（例：WireSync News）とコンシューマー（Net Nester）を区別できます\n"
    "4. プロデューサー行動: USE仕様（read-text, post-text）、ドメイン名（例：texttextvelv.biz）、「visits/required」ラベル\n"
    "5. コンシューマー行動: USE仕様（例：read-textとpost text）で閲覧やコメントを行います。"
)

# Entry 152: DNS program install tutorial
TRANSLATIONS[152] = (
    "[i][i][color=red]netsh[/color][/i]アプリでDNSプログラムをインストールする手順[/i]\n"
    "以下のコマンドを使用する前に、デバイス/ユーザーがケーブルでデバッガーに接続されていることを確認してください。"
    "このチュートリアルではalways usingコマンドでデバッガーアドレスが36005にデフォルト設定されています。\n\n"
    "1. man program \n"
    "2. program list\n"
    "3. program describe dns-lite\n"
    "4. program install dns-lite on 21802; 21802はサーバーのハードウェアアドレスです\n"
    "5. program start dns-lite on 21802\n"
    "6. <任意> watch 21802\n"
    "7. dns map texttextvelv.biz as 78121; 78121はプロデューサー（WireSync News）のハードウェアアドレスです"
)

# Entry 153: Useful route commands
TRANSLATIONS[153] = (
    "netshアプリで便利なrouteコマンド\n\n"
    "1. man route - routeコマンドの構文を確認\n"
    "2. route show - 現在のルートを表示\n"
    "3. route default - デフォルトルートを設定\n"
    "4. route add - 新しいルートを追加"
)

# Entry 154: Physical connection to router
TRANSLATIONS[154] = (
    "[i]ルーターへの物理接続（ハードウェアアドレス: 48460）[/i]\n\n"
    "1. netshでルートを設定する前に、デバッガーをルーターに接続します\n"
    "2. 各ユーザー/デバイスが正しいルーターポートに接続されていることを確認してください。\n\n"
    "例えば: 「route add 36005 via port2 on 48460」コマンドを使用する場合、"
    "アドレス36005のユーザー/デバイス（port2の宛先）はルーター48460のport2に"
    "接続されている必要があります。36005はプロデューサー（WireSync News）のアドレスです。"
)

# Entry 155: Method 1 - default route to DNS
TRANSLATIONS[155] = (
    "[i][i]方法1: デフォルトルートをDNSサーバーのあるネットワークに設定[/i][/i]\n\n"
    "ルーターのデフォルトルートをDNSサーバーが接続されているポートに設定します。\n\n"
    "1. DNSサーバーをルーターのポート1に接続\n"
    "2. ポート1をデフォルトルートに設定: route default via port1 on 48460\n"
    "3. プロデューサーのアドレスへのルートを追加: route add 36005 via port2 on 48460\n"
    "4. コンシューマーをルーター（48460）の任意のポートに接続し、port1経由でDNSサーバーに、port2経由でプロデューサー（36005）に到達できるようにします\n\n"
    "なぜ機能するか: 特定のルートがないトラフィックは自動的にデフォルトルートを通るため、"
    "追加設定なしでユーザーがDNSサーバーに到達できます。"
)

# Entry 156: Rocket Store
TRANSLATIONS[156] = (
    "[i]Rocket Store[/i]: ワンストップアプリランチャー販売店\n\n"
    "より高度なアプリを購入できます（例：The Registry、Socketeer、Autograph）"
)

# Entry 157: Stream-voice service provider
TRANSLATIONS[157] = (
    "[i]stream-voiceサービスプロバイダーになる:[/i]\n\n"
    "1. ドメインを所有する: The Registryアプリでドメインを登録します。\n"
    "2. voip-serverを実行する: voip-serverプログラムを起動します。\n"
    "3. 公衆VoIP電話を接続する: VoIP電話をvoip-serverに接続します（voip-server上に「stream-voice」ユーザースタックが作成されます）。\n"
    "4. DNSマッピング: コンシューマーがアクセスできるようにドメイン（例：streamvoice.com）をvoip-serverにマッピングします。"
)

# Entry 158: Register domain name
TRANSLATIONS[158] = (
    "[i]ドメイン名の登録[/i]\n\n"
    "1. The Registryアプリを起動\n"
    "2. ドメイン名として「streamvoice.com」と入力します。\n"
    "3. スライダーで消費あたりの価格を0.5に設定します。\n"
    "4. (+) Associate usageボタンをクリックします。\n"
    "5. USE仕様のドロップダウンから「stream-voice」を選択します。\n"
    "6. Finalizeボタンをクリックし、続いてConfirmボタンをクリックします。"
)

# Entry 159: Pause hint
TRANSLATIONS[159] = (
    "「ESC」を押してゲームを一時停止/再開し、時間を気にせずWikiを読むことができます。"
)

# Entry 160: Feedback
TRANSLATIONS[160] = (
    "コンセプトやWikiについてご意見やフィードバックがありますか？F8キーでお気軽にお知らせください。"
)

# Entry 161: Load tester description
TRANSLATIONS[161] = (
    "{nport}ポートイーサネット負荷テスター。UDP/53 DNSクエリトラフィックを発生させます。"
)

# Entry 162: Network tap description
TRANSLATIONS[162] = (
    "イーサネットインラインネットワークタップ。ポートミラーリング機能を搭載。パケットトラフィックキャプチャを生成します。"
)

# Entry 163: Cable box
TRANSLATIONS[163] = "ケーブル/周辺機器整理用ボックス。"

# Entry 164: RJ-45 toolkit
TRANSLATIONS[164] = "RJ-45端末処理用ケーブリングツールキット。"

# Entry 165: Fiber optic toolkit
TRANSLATIONS[165] = "光ファイバー（SC）端末処理用ケーブリングツールキット。"

# Entry 166: Shelf piece
TRANSLATIONS[166] = "マウンティングラックの棚板として使用します。"

# Entry 167: Mountable power strip
TRANSLATIONS[167] = "マウント型電源分配タップ。壁のコンセントが限られている場合に電源延長として使用します。"

# Entry 168: Power strip
TRANSLATIONS[168] = "電源分配タップ。壁のコンセントが限られている場合に電源延長として使用します。"

# Entry 169: DNS monitor
TRANSLATIONS[169] = "すべてのDNSエントリマッピング、ネットワークアドレス割り当て、デバイスの場所を表示する追加モニター。"

# Entry 170: Population monitor
TRANSLATIONS[170] = "タワー内の総人口数を表示する追加モニター。販売可能。"

# Entry 171: Satiety monitor
TRANSLATIONS[171] = "住民の満足度レベルを表示する追加モニター。販売可能。"

# Entry 172: User monitor
TRANSLATIONS[172] = "インターネットサービスの管轄下にあるユーザーを監視するための追加モニター。"

# Entry 173: Floor issues monitor
TRANSLATIONS[173] = "上位フロアの問題を表示する追加モニター。販売可能。"

# Entry 174: Visitor count monitor
TRANSLATIONS[174] = "ドメイン名別の訪問者数を表示する追加モニター。販売可能。"

# Entry 175: AVR
TRANSLATIONS[175] = "自動電圧調整器。"

# Entry 176: Power surge protection
TRANSLATIONS[176] = "電力サージによるデバイスの損傷を防ぎます。"

# Entry 177: UPS
TRANSLATIONS[177] = "無停電電源装置。"

# Entry 178: UPS function
TRANSLATIONS[178] = "停電やサージの際にデバイスの動作を維持します。"

# Entry 179: UPS expanded
TRANSLATIONS[179] = "無停電電源装置（拡張負荷対応）。"

# Entry 180: Mountable UPS
TRANSLATIONS[180] = "マウント型無停電電源装置（拡張負荷対応）。"

# Entry 181: UPS extra expanded
TRANSLATIONS[181] = "無停電電源装置（超拡張負荷対応）。"

# Entry 182: Max load - passthrough variable
TRANSLATIONS[182] = "最大: {load} W"

# Entry 183: Router description
TRANSLATIONS[183] = "{nport}ポートミクストメディアネットワーク対応ルーター。"

# Entry 184: VLAN subinterfaces
TRANSLATIONS[184] = "VLANサブインターフェースに対応。"

# Entry 185: Mixed media router
TRANSLATIONS[185] = "{nport}ポートミクストメディアネットワークルーター。"

# Entry 186: Small business
TRANSLATIONS[186] = "中小企業向け。"

# Entry 187: Improved performance
TRANSLATIONS[187] = "性能向上と最大スループットを実現。"

# Entry 188: 3rd gen
TRANSLATIONS[188] = "第3世代エディション。高可用性セットアップに対応。"

# Entry 189: Ethernet router
TRANSLATIONS[189] = "{nport}ポートイーサネットネットワークルーター。"

# Entry 190: Economical medium
TRANSLATIONS[190] = "中規模企業向けエコノミーモデル。"

# Entry 191: Economical medium HA
TRANSLATIONS[191] = "中規模企業向けエコノミーモデル。高可用性対応。"

# Entry 192: Small form factor router
TRANSLATIONS[192] = "{nport}ポートミクストメディアネットワークルーター。エッジルーティングに適した小型フォームファクター。"

# Entry 193: 2nd gen edge router
TRANSLATIONS[193] = "{nport}ポートミクストメディアネットワークルーター。第2世代エッジルーティングデバイス。さらに小型なフォームファクター。Less is more。"

# Entry 194: 3rd gen edge router
TRANSLATIONS[194] = "{nport}ポートミクストメディアネットワークルーター。第3世代エッジルーティングデバイス。高可用性対応。"

# Entry 195: General computing server
TRANSLATIONS[195] = "{nport}ポート汎用コンピューティングサーバー。"

# Entry 196: SATA slots
TRANSLATIONS[196] = "2基の拡張SATA 3.5\"スロット搭載。"

# Entry 197: Gazelle description
TRANSLATIONS[197] = "Gazelleは高負荷条件下で長持ちするよう設計された耐久性の高いデバイスです。"

# Entry 198: Scalable compute
TRANSLATIONS[198] = "スケーラブルコンピューティング。"

# Entry 199: High performance extra bandwidth
TRANSLATIONS[199] = "追加帯域幅を搭載した高性能モデル。"

# Entry 200: High performance
TRANSLATIONS[200] = "高性能モデル。"

# Entry 201: High bandwidth server
TRANSLATIONS[201] = "{nport}ポート高帯域幅コンピューティングサーバー。"

# Entry 202: Fiber enabled
TRANSLATIONS[202] = "光ファイバー対応コンピューティングサーバー。"

# Entry 203: High performance server
TRANSLATIONS[203] = "{nport}ポート高性能コンピューティングサーバー。"

# Entry 204: 6 SATA slots
TRANSLATIONS[204] = "6基のSATA 3.5\"拡張スロット搭載。"

# Entry 205: 2 SATA slots
TRANSLATIONS[205] = "2基のSATA 3.5\"拡張スロット搭載。"

# Entry 206: Managed switch mixed media
TRANSLATIONS[206] = "{nport}ポートミクストメディアネットワークマネージドスイッチ。VLANポートタグに対応。"

# Entry 207: Second hand market
TRANSLATIONS[207] = "この機器は中古市場で人気があります。"

# Entry 208: Managed switch ethernet
TRANSLATIONS[208] = "{nport}ポートイーサネットマネージドネットワークスイッチ。VLANポートタグに対応。"

# Entry 209: More ports cheaper
TRANSLATIONS[209] = "より多くのポートをより安価に。"

# Entry 210: Mixed media switch VLAN
TRANSLATIONS[210] = "{nport}ポートミクストメディアネットワークスイッチ。\nVLANポートタグに対応。"

# Entry 211: Enterprise grade
TRANSLATIONS[211] = "エンタープライズグレードの機器。"

# Entry 212: Ethernet switch
TRANSLATIONS[212] = "{nport}ポートイーサネットネットワークスイッチ。"

# Entry 213: Entry level
TRANSLATIONS[213] = "エントリーレベルのネットワークに最適。"

# Entry 214: Fiber optic switch
TRANSLATIONS[214] = "{nport}ポート光ファイバーネットワークスイッチ。"

# Entry 215: Mixed media switch
TRANSLATIONS[215] = "{nport}ポートミクストメディアネットワークスイッチ。"

# Entry 216: Enterprise high power
TRANSLATIONS[216] = "エンタープライズグレードの機器。スループットを支えるため高消費電力です。"

# Entry 217: Fiber optic managed switch
TRANSLATIONS[217] = "{nport}ポート光ファイバーマネージドネットワークスイッチ。VLANポートタグに対応。"


def main():
    entries = parse_entries(INPUT_FILE)
    print(f"Parsed {len(entries)} entries from {INPUT_FILE}")

    lines = []
    lines.append("# Wiki article translations - auto-generated")
    lines.append("# Generated by gen_wiki_translations.py")
    lines.append("")

    translated_count = 0
    skipped_count = 0

    for entry_num, ctx, msgid in entries:
        if entry_num not in TRANSLATIONS:
            print(f"WARNING: Entry {entry_num} has no translation defined!")
            continue

        translation = TRANSLATIONS[entry_num]
        if translation is None:
            skipped_count += 1
            continue

        # Escape the msgid and translation for Python string
        escaped_msgid = escape_for_python(msgid)
        escaped_translation = escape_for_python(translation)

        lines.append(f't("{escaped_msgid}", "{escaped_translation}")')
        translated_count += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        f.write("\n")

    print(f"Generated {OUTPUT_FILE}")
    print(f"  Translated: {translated_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Total entries: {len(entries)}")


if __name__ == "__main__":
    main()
