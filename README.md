# robosys2025 
ロボットシステム学課題１

# mypkg
ノードの説明
これは数値を送信して認識して、それをファイルに保存します。

talker.py 　：一定の周期で数値を送信する
listener.py ：talkerのデータを受信する
saver.py 　 ：受信したデータをファイルに保存する

保存される先は　~/mylogs/mylog.csv　です。

実行方法
ビルドのやり方
cd ~/ros2_ws
colcon build
source install/setup.bash

ノードを起動する方法
talker　　　：ros2 run mypkg talker
listener    :ros2 run mypkg listener
saver       :ros2 run mypkg saver





動作環境 
    OS:linux python 
    version：Python 3.12.3
    ROS 2: Jazzy

