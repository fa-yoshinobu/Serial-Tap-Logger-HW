# Serial Tap Logger | RS-232C Rev.1 製造・部品手配

[README](../README.md) ／ [設計資料](Design_Notes.md) ／ [作業状況](Work_Status.md)

## 実装と部品手配

Serial Tapの表面の挿入部品と裏面のはんだ付け箇所は、手はんだ実装図の4・5ページに掲載した。[手はんだ実装図](../enclosure/drawings/Hand-Solder-Assembly-Rev1.pdf)・[JLCDFMの検査レポート](verification/JLCDFM-Rev1.pdf)

**2026-11-25版の製造データ**　C31（22 pF）をU12の近くに裏面実装し、R59・R60（3.3 kΩ）、R71（1.5 kΩ）を反映した。実装BOMと配置CSVは全104点で一致し、ガーバーの裏面ペースト269開口を実装パッド中心と照合した。C31の配置座標はX=31.2500、Y=−48.7000 mm、Bottom、0°。

RTCはPCF8563T（U12）を裏面に実装し、水晶振動子Y1は秋月104005（VT-200-F）を表面で直立させて手はんだする。時計保持用の秋月104250（1.5 F／5.5 V）は液晶の下に平置きする。5 V電源は秋月BP5293-50（PS1）を表面に直立させて手はんだする。記録操作にはEC11の押し込み（GP18）を使用する設計。[液晶下の寸法・取付条件](../enclosure/drawings/RTC_Assembly.md) ／ [基板の両面配線図](Serial_Tap_Logger_RS232C_Rev1_2d_view.png)

| 用途 | 現行ファイル | 内容 |
|---|---|---|
| JLCPCB実装部品 | [PCBA_BOM.csv](../pcb/manufacturing/PCBA_BOM.csv) | LCSC番号・型番・定数・数量/枚。22品種104点 |
| JLCPCB配置 | [PCBA_CPL.csv](../pcb/manufacturing/PCBA_CPL.csv) | 104点の座標と回転。全点Bottom、mm |
| 手配・手はんだ | [Hand_Assembly_BOM.csv](../pcb/manufacturing/Hand_Assembly_BOM.csv) | 秋月の部品・ソケット、AliExpressのWeActと表示器、電源モジュール、スーパーキャパシタ、C22、Grove端子J7・J8。標準品と条件付きのピンヘッダを区分 |
| 端子照合 | [主要部品ピン照合.csv](Pin_Mapping.csv) | 回路ネット・パッド番号・基板上の座標 |
| 基板製造 | [ガーバー・ドリル一式](../pcb/manufacturing/Serial_Tap_Logger_RS232C_Rev1_Gerber.zip) | 100 × 100 mm、2層、外形・ドリル入り |

R67（RTCバックアップ充電、1 kΩ）、C1〜C8（100 pF）、R69・R70（Grove GPIO直列、各100 Ω）は工場実装。Grove端子J7・J8（Seeed 110990037、秋月112634）は表面でWeActより先に手はんだする。R66（シールド選択、0 Ω）は初回未実装。裏面では、Groveの実装位置に `J7 I2C 3V3` と `J8 GPIO 3V3` を表示する。測定点はTP1から順に `5V_A`、`3V3`、`GND`、`BIAS`、`VHI`、`VLO`。信号名は対応する番号と測定パッドの間に印刷する。[裏面実装図](../enclosure/drawings/PCBA_Back.png)

記録バッファの増量が必要なら、WeAct RP2350B Core Board裏面のU7（Secondary Flash / PSRAM）に **AP Memory `APS6404L-3SQR-SN`**（8 MiB／64 Mbit、3.3 V系、SOP-8）を実装する。使用時はファームウェア側で初期化とバッファ割り当てが必要。[WeAct公式基板資料](https://github.com/WeActStudio/WeActStudio.RP2350BCoreBoard/tree/main/HDK) ／ [AP Memoryデータシート](https://www.apmemory.com/wp-content/uploads/APS6404L-3SQR.pdf)

## JLCPCB入稿時の確認

表面処理は有鉛HASL、配送を日本向けOCSとする場合の発注条件です。表の現行ガーバー・BOM・CPLを組み合わせて入稿する。現行Gerberには表面校正パッドTP7～TP14、TP7・TP10のパッド外へのビア移動、裏面TP6の移設を反映済み。表面は校正パッド8点の位置、裏面はGroveの用途・電圧とTP1〜TP6の信号名を確認する。[発注前レビュー](Pre_Order_Review.md)

### 裏面の実装向き

**現行104点版は確認済み。** 2026年11月26日にJLCDFMの裏面配置一覧とCPLの104点を全件照合した。U4・U7を含むU1〜U9・U12の1番ピンは、配置図で全点が左上のランドに一致した。その後のGerber修正でも、実装BOM・CPLと裏面ペースト開口は同一。[発注前レビュー](Pre_Order_Review.md) ／ [設計の向き照合図](verification/PCBA_Orientation_Bottom.png)

旧103点版のJLCPCBカートでは、初回読込時にU4・U7が180°逆に表示された。カート上で補正して保存し、IC 10点の1番ピン、D1のカソード（下）、D2のカソード（左）を照合した。[旧版の初回読込](verification/JLCPCB_103_Bottom_As_Loaded.jpg) ／ [補正後](verification/JLCPCB_103_Bottom_Corrected.jpg) ／ [D1](verification/JLCPCB_103_D1.jpg) ／ [D2](verification/JLCPCB_103_D2.jpg)
