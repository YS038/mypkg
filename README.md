# robosys2025 
ロボットシステム学課題2

# mypkg

## ノードの説明  
このパッケージには、数値データを送受信するノードが含まれています。
`countup` トピック（`std_msgs/msg/Int16`）を使用します。
  
## ノードを起動する方法  
talker   : ros2 run mypkg talker
listener : ros2 run mypkg listener
saver    : ros2 run mypkg saver  


## 使用しているトピック
- `countup`（std_msgs/msg/Int16）  
  - 数値データを送受信するためのトピック

## 動作環境   
- OS:Ubuntu 24.04.3 LTS  
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
