import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    talker = launch_ros.actions.Node(
            package='mypkg',
            executable='talker',
        )
    listener = launch_ros.actions.Node(
             package='mypkg',
             executable='listener',
             output='screen'
        )
    saver = launch_ros.actions.Node(
            package='mypkg',
            executable='saver',
            output='screen',
            parameters=[{'topic': 'countup', 'output': '/home/yui31/mylogs/mylog.csv'}]
        )

    )
    return launch.LaunchDescription([talker, listener, saver])
