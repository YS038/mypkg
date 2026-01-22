# robosys2025 
ロボットシステム学課題2

# mypkg

## ノードの説明
このパッケージには、数値データを送受信・記録するノードが含まれています。
`countup` トピック（`std_msgs/msg/Int16`）を使用します。

- talker ノード：数値データを publish する
- listener ノード：数値データを受信して表示する
- saver ノード：数値データを受信し，受信回数と合計値を計算して保存する


## 使用しているトピック
- `countup`（std_msgs/msg/Int16）  
  - 数値データを送受信するためのトピック

## 動作環境   
- OS:Ubuntu 22.04.3 LTS  
- version：Python 3.12.3  
- ROS 2: Jazzy


 
## 参考資料
本パッケージの talker ノードおよび listener ノードは，
以下の講義資料を参考にして作成しました。

- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson2.html
- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson3.html
- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson4.html
- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson5.html
- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson6.html
- https://ryuichiueda.github.io/slides_marp/robosys2025/lesson7.html

## ライセンス

このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
