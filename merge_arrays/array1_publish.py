import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray


class array1_publisher(Node):

    def __init__(self):
        super().__init__('array1_publisher')
        self.publisher_ = self.create_publisher(Int32MultiArray, '/input/array1', 10)
        timer_period = 10  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32MultiArray()
        msg.data = [1,4,5,3]
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % str(msg.data))



def main(args=None):
    rclpy.init(args=args)

    publisher = array1_publisher()

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    array1_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()