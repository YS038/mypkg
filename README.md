# robosys2025 
ロボットシステム学課題2

# mypkg

## ノードの説明  
このパッケージでは、talker ノードが数値を publish し、  
listener ノードがその数値を subscribe して受信します。  
saver ノードは、受信した数値をファイルに保存します。  
 

talker.py 　：一定の周期で数値を送信する  
listener.py ：talkerのデータを受信する  
saver.py 　 ：受信したデータをファイルに保存する  
## ノードを起動する方法  
talker　　　：ros2 run mypkg talker  
listener    :ros2 run mypkg listener  
saver       :ros2 run mypkg saver  


## 使用しているトピック



## 動作環境   
    OS:Ubuntu 24.04.3 LTS  
    version：Python 3.12.3  
    ROS 2: Jazzy 

- このパッケージのコードは，下記のスライドを，本人の許可を得て自身の著作としたものです．
 (https://ryuichiueda.github.io/slides_marp/robosys2025/lesson2.html)
 (https://ryuichiueda.github.io/slides_marp/robosys2025/lesson3.html)
 (https://ryuichiueda.github.io/slides_marp/robosys2025/lesson4.html)
 (https://ryuichiueda.github.io/slides_marp/robosys2025/lesson5.html)
 (https://ryuichiueda.github.io/slides_marp/robosys2025/lesson6.html)
 (https://ryuichiueda.github.io/slides_marp/robosys2025/lesson7.html)
-Ⓒ　2025 yuu

## ライセンス

このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．


SPDX-License-Identifier: BSD-3-Clause    
SPDX-FileCopyrightText: 2025 yuu
