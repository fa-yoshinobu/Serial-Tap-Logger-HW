# Serial Tap Logger Rev.1 作業状況

2026-11-25時点。

## 回路図・部品表

C31をU12のOSCIとGNDの間に追加し、R59・R60を3.3 kΩ、R71を1.5 kΩに変更した。回路図のERCはエラー・警告とも0件。実装BOMは22品種104点。基板、ガーバー・ドリル、CPL、両面の配線図まで反映した。

## 基板・製造データ

- 発注前DFMで、C28・C29・U1・R68のGNDビアをパッド外へ移した。穴の縁と各パッドの隙間は順に0.420、0.350、0.325、0.300 mm。電源ビア7個はランド径0.60 mmのまま穴径を0.30 mmとし、環幅0.15 mmを確保した。シルクはD1・D2の極性表示、SOICの1番マークとR51・D2の参照番号の位置を調整し、細い外形線を0.15 mmに揃えた。[製造用Gerber ZIP](../pcb/manufacturing/Serial_Tap_Logger_RS232C_Rev1_Gerber.zip)
- 11月25日の最終版で、基板DFMのランド環幅とシルク対パッドの危険判定は0件。裏面104点のSMT実装DFMは危険・警告とも0件。[基板DFM・SMT実装DFMのレポート](verification/JLCDFM-Rev1.pdf)
- JLCDFMの危険表示はシルク対穴77件、挿入部品ランド対SMDランド7件。602個のドリル穴を両面のGerberで照合した。露出穴からシルクまでの最短距離は表0.614 mm、裏0.564 mm。シルクから0.15 mm以内に入る穴は、表22個、裏36個で、いずれも該当面のレジストに開口がない。TSVの座標は製造Gerber座標。負の距離はドリル穴とシルクの重なりを表す。[全穴の照合結果](verification/Silk-hole-clearance.tsv)
- 挿入部品ランドとSMDランドを全組合せで調べ、外周間が2.50 mm以内の22組を記録した。最短はY1とテストパッドTP6の1.256 mm。工場実装部品との最短はJ3.5とR68.1の1.446 mm。配置を維持してGerberを再出力し、基板DFMとSMTを再実行した。実物のこてでの作業性は未検証。[ランド間隔の照合結果](verification/PTH-SMD-clearance.tsv)

- 8線の入力しきい値を決めるR44を750 Ω、R45を820 Ωに変更した。5.00 V給電時の線路換算値は公称+2.42 Vと−2.17 V。±3 Vでの入力判定は試作で確認する。[入力回路と判定点](Design_Notes.md#入力回路)
- 基板外形は100 × 100 mm。PCBAは裏面22品種104点。C29・C30（VHI・VLO 100 nF）、R71（BIAS 1.5 kΩ）、C31（RTC_OSCI 22 pF）を実装する。秋月104005（Y1）はφ0.55 mmの穴2か所、ピッチ1.27 mmで表面に直立させて手はんだする。秋月BP5293-50（PS1）も表面に直立させ、穴は3か所ともφ1.2 mm。ランド径1.6 mm、リード寸法とピッチの公差から見積もった必要穴径は約1.08 mm。[PS1の寸法図 Fig.31](https://akizukidenshi.com/goodsaffix/BP5293_DataSheet_J_VerC_161013.pdf#page=18)
- Grove端子J7・J8は表面で手はんだする。J7はSCL・SDA、J8は裏面に追加したR69・R70（各100 Ω）経由のGP22・GP24。各端子の3番は3.3 V、4番はGND。裏面に `J7 I2C 3V3` と `J8 GPIO 3V3` を表示する。TP1〜TP6には順に `5V_A`・`3V3`・`GND`・`BIAS`・`VHI`・`VLO` を併記した。KiCadのネットリストで接続を照合した。今回のBOMとCPLの部品番号は裏面104点で一致し、重複・欠落は0件。[裏面実装図](../enclosure/drawings/PCBA_Back.png)・[ピン照合表](Pin_Mapping.csv)
- J7のSCLを内側に通す案はDSR_POSとのクリアランスに制約があり、従来の外回り（50.4 mm、ビア5個）を維持した。Groveピン付近で同層の最小間隔は、3.3 V–J8.4（GND）0.2358 mm、DC_IN–J7.4（GND）0.2400 mm、3.3 V–DC_IN 1.7067 mm。[Grove配線図](verification/Grove_Routing.png)
- R66は未実装で、専用フットプリントにペースト層を設定していない。PS1・C22・C27・J7・J8は工場実装の位置ファイルの出力対象外。C28のGND接続はパッド外のビアを使用する。J7・J8のめっきピン穴は計8か所。現行ガーバーの裏面ペースト開口269か所は、工場実装104点のパッド中心とすべて一致した。今回増えた2開口はC31の両端子。ドリルはめっき594か所（ビア・長穴を含む）と非めっき8か所の位置・径、長穴の長さを基板と照合した。
- 補助原点は (98.5, 55) mm。製造用CPLはKiCadの座標出力に対し、U1〜U9・U12を90°、D1・D2を180°補正済み。Q3は補正なし。103点版のJLCPCBプレビューではU4・U7の1番ピンが右下に表示されたため、この2個を画面上で各180°回転した。カートの「製品の詳細」→「部品配置」を開き直し、全10個のICの1番ピンが左上のシルク三角と一致することを確認した。D1のカソードは下、D2は左。裏面をH1が左上、Groveが下になる向きで比較した。[初期表示](verification/JLCPCB_103_Bottom_As_Loaded.jpg) ／ [カート保存後](verification/JLCPCB_103_Bottom_Corrected.jpg) ／ [基板の照合図](verification/PCBA_Orientation_Bottom.png)
- 基板の表裏のシルク文字は高さ1.00 mm以上、線幅0.15 mm以上。DC入力の極性表示 `DC 12V CENTER +` は高さ1.20 mm、線幅0.18 mm。JLCPCBの公表値を適用したローカル検査で、文字寸法とパッドへの重なりの警告は0件。[JLCPCBの製造仕様](https://jlcpcb.com/capabilities/pcb-capabilities/)
- ERC、DRC、未配線、回路図との不一致は各0件。[検証レポート](verification/)

## 3Dモデルとケース

- DCジャック（MJ-179PH）は端子を含む共通モデルに更新した。旧トレーで2番端子に当たった支柱Bを右前へ移し、組立CADで2番端子とのすきま3.41 mmを確認した。奥行111.5 mm版はトレーのみ再印刷すればよい。[トレーSTL](../enclosure/print/Case_Print_Rev1_Tray.stl)

- [基板STEP](../enclosure/3d-models/Serial_Tap_Logger_RS232C_Rev1_PCBA.step)と[ケース組立STEP](../enclosure/3d-models/Case_Print_Rev1_Assembly.step)には、C31を含む表面12点・裏面104点と基板本体を収録した。11月24日版では部品115点と基板本体をトレー・上ぶたのそれぞれと照合し、計232組の体積干渉は0件。ケースまでの最小すきまはPS1が1.70 mm、Y1が5.20 mm、追加したC29・C30が各5.12 mm、R71が5.47 mm。
- 固定部の張り出しを含むケース最大外寸は幅121.10 × 奥行114.05 × 高さ32.80 mm。Groveは前パネル、DCジャックはその周囲のくぼみと面一にした。DE-9押さえリブ下端は13.10 mm。簡略モデルとのすきまはJ1・J2とも0.55 mm。基板用タッピング下穴はφ2.5 mm・深さ5.5 mmで、ねじはM3×6、ゴム足用の座ぐりはφ10 mm・深さ1.0 mm。[最新外観・寸法・STEP・STL](../enclosure/drawings/Case_Print_Rev1.md)

## フットプリントとピン割り当ての照合（2026-11-25）

### 資料・設計データで確認済み

- 現行基板のパッドに割り当てられた90ネットのうち、9ネットは未接続指定。ピン照合表241行のパッド番号・座標・ネットが基板と一致した。ERC・DRCと回路図との不一致は各0件。裏面実装のBOMとCPLは104点で一致した。[ピン照合表](Pin_Mapping.csv)
- J1・J2（DMR-09PGG／SGG）は同番号の全9ピンを直結。端子ピッチ2.77 mm、列間2.84 mm、取付穴間隔24.99 mm。嵌合面の幅広い5ピン側が上になる配置。[J1メーカー図面](https://akizukidenshi.com/goodsaffix/DMR-09PGG_20220218.PDF)・[J2図面](https://akizukidenshi.com/goodsaffix/DMR-09SGG.pdf)
- J6（MJ-179PH）は奥の1番がセンター＋、口側の2番がスリーブ、横の3番がスイッチ端子。配置と端子割り当てが一致した。[メーカー図面](https://akizukidenshi.com/goodsaffix/mj179ph_mj180ph.pdf)
- J3（AE-MICRO-SD-DIP）は部品面を上から見てカード口を手前にすると右端が1番DAT2。1〜10番の信号順と角パッドの位置が一致した。カード口側の支持用に電気的に未接続のφ1.02 mm穴を4か所追加し、製造データと組立CADに反映した。付属細ピンとソケットの嵌合は現物で確認する。[秋月の説明書](https://akizukidenshi.com/goodsaffix/K-5488_AE-MICRO-SD-DIP.pdf)・[支持穴の配置図](https://akizukidenshi.com/goodsaffix/AE-MICRO-SD-DIP_plot.pdf#page=10)
- J4（TFT＋EC11）は参照写真の12ピン順と一致。画面を左、つまみを右にすると下端が1番GND。
- A1の60ピンとGPIO割り当てを照合した。microSDはSPI0のGP34〜36とDAT0〜3のGP36〜39、TFTはSPI1のGP26・GP27、I²C0はGP20・GP21、ADCはGP40〜47、比較器出力はGP1〜16。U1〜U9、U12、Q3、PS1の端子、D1・D2・C27の極性、VHI・VLOの判定点も照合済み。[WeAct公式ピン配置](https://github.com/WeActStudio/WeActStudio.RP2350BCoreBoard/blob/main/HDK/RP2350B_PINOUT.png)
- WeActのGP0（二次Flash/PSRAMのCS）、GP23（基板キー）、GP25（基板LED）はキャリアから駆動しない。
- WeActのVBUSと5Vの間は理想ダイオードIC（U2）。USB接続時のQ3のVGSは約+0.05 Vでオフ。

### 現物で確認する項目

1. **J1・J2**の信号ピンと固定金具が基板の穴に入ることを確認する。J1のメーカー図面の外形寸法Eは12.55 ±0.38 mm（最大12.93 mm）。リブ下端は13.10 mmに上げたので、寸法上限でも0.17 mmのすきまが残る。念のため、ねじを締める前に上ぶたを仮合わせする。[J1メーカー図面](https://akizukidenshi.com/goodsaffix/DMR-09PGG_20220218.PDF)
2. **J4**の購入品で12ピンの並びと1番GND、取付穴の位置を確認する。
3. **A1**のU2をまたぐVBUS－5V間のジャンパーパッドが開放であることを確認する。短絡しているとDC給電時にUSBホストへ逆流する。
4. **PS1**のリードがφ1.2 mmの穴3か所に入ることを確認する。

## 試作機での確認

- PS1のピン挿入、ケース嵌合、DE-9押さえとタッピングねじの効き、負荷時の電源電圧・ピーク電流・温度を確認する。PS1の上限は1 A。
- RTC発振と115,200 bps連続記録を確認する。[実機立ち上げ手順](https://github.com/fa-yoshinobu/Serial-Tap-Logger-FW/blob/main/docs/validation/Bringup.md)
