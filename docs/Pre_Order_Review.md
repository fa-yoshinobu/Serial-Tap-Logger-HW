# Serial Tap Logger 発注前レビュー

2026年11月25日、Rev.1の初回発注前に確認した内容。確認対象はHW `cb1bdee`。

## 発注前レビューの結果

- **RXD校正用TP8は移設済み。** 基板左上からX=37.033、Y=63.521 mm。WeAct A1と電源モジュールPS1の間にあり、液晶の外側から測れる。[パッド座標](Pin_Mapping.csv)
- **現行104点版は照合済み。** JLCDFMでU4・U7を含むIC 10点すべての1番ピンが左上のランドと一致した。[向きの照合記録](Manufacturing.md#裏面の実装向き)

microSDのCMDとDAT0～3には既に各10 kΩのプルアップ（R47～R51）がある。今回のレビューでは、カード容量を理由とするSerial側の回路変更は不要と判断した。容量別の認識・記録・読み戻しは実カードでの確認項目。[SDの配線と電源](Design_Notes.md#sdhcの高速記録)

## 確認済みの範囲

- ベタ再充填後のDRC違反・未配線・回路図との接続不一致は各0件。ERCはエラー・警告とも0件。
- 工場実装BOMとCPLの部品番号は104点が一致。[製造資料](Manufacturing.md)
- TP8のプローブの当てやすさと実カードの動作は試作機で確認する。

## 2026年11月26日 JLCDFMでの確認

- TP8移設版のGerberでPCB DFMを実行した。Danger表示はシルクと穴の間隔100件、挿入ランドとSMDランドの間隔7件（最小1.29 mm）。パッド内ビアはWarning 2件で、ドリルと基板上の座標を突き合わせるとTP7・TP10。実装ペーストを使わない校正パッドである。Danger箇所の全件の個別照合は未実施。[JLCDFMの基板解析PDF](verification/JLCDFM-TP8-2026-11-26.pdf)
- JLCDFMの裏面配置一覧とCPLで参照番号104点を全件照合し、欠落・余分な部品は各0点。SMT DFM画面では部品干渉・部品間隔・ランドのない端子の指摘は各0件。[裏面の向きの照合図](verification/PCBA_Orientation_Bottom.png)

### 現行Gerberへの反映

- TP7（TXD）とTP10（CTS）のビアをパッド外へ移し、校正用の表面ランドを穴のない状態にした。TP6（VLO）は0.95 mm移動し、Y1の挿入ランドとの間隔を約1.26 mmから約2.18 mmに広げた。
- 現行Gerberのシルクと露出した丸穴との最短間隔は表面0.614 mm、裏面0.564 mm。0.15 mm未満の丸穴はレジストで覆われたビアのみで、シルクは維持した。J3の5番ランドとR68の1番ランドは約1.45 mmで、J3の手はんだ時に確認する。
- KiCadのDRC違反・未配線・回路図との不一致は各0件。現行Gerberで表面の校正パッド8点と裏面ペースト269開口を照合した。工場実装104点のBOM・CPLは上記の確認時と同一。[現行Gerber](../pcb/manufacturing/Serial_Tap_Logger_RS232C_Rev1_Gerber.zip)
- 修正版をJLCDFMで再解析した。パッド内ビアの指摘は2件から0件、挿入ランドとSMDランドのDangerは7件から5件（すべて裏面）。シルクと穴のDanger表示は100件。残ったランド間隔の指摘は、手はんだ時のこて先と隣接ランドの間隔を確認するために記録した。[修正版の解析PDF](verification/JLCDFM-Calibration-2026-11-26.pdf)

[RS422-485 Wave Loggerの発注前レビュー](https://github.com/fa-yoshinobu/RS422-485-Wave-Logger-HW/blob/main/docs/Pre_Order_Review.md)
