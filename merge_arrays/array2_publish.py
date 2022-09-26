import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray


class array2_publisher(Node):


    '''
    This class sends out a test - array every 10 seconds to the topic /input/array2
    '''

    #constructor
    def __init__(self):
        super().__init__('array2_publisher')
        self.publisher_ = self.create_publisher(Int32MultiArray, '/input/array2', 10)
        timer_period = 10  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    #callback
    def timer_callback(self):
        msg = Int32MultiArray()
        msg.data = [43,5,3,2,67,2]
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % str(msg.data))



def main(args=None):
    rclpy.init(args=args)
    publisher = array2_publisher()
    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    array2_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()