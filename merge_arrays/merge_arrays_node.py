from typing import List, no_type_check_decorator
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class MergeArrays(Node):

        #class attributes
        

        #constructor
        def __init__(self):
            super().__init__('merge_arrays')

            self.array1=[]
            self.array2=[]
            
            #subscription to the two topics
            self.subscription = self.create_subscription(Int32MultiArray,"/input/array1",self.sub_callback_array1,10)
            self.subscription = self.create_subscription(Int32MultiArray,"/input/array2",self.sub_callback_array2,10)

            #publisher creation 
            self.publisher_ = self.create_publisher(Int32MultiArray, '/output/array', 10)
      

        #get set
        def get_array1(self):
            return self.array1
            
        def set_array1(self,x):
            self.array1=x
        
        def get_array2(self):
            return self.array2

        def set_array2(self,x):
            self.array2=x

            
        #callback functions for receiving messages
        def sub_callback_array1(self, msg):
            #message=msg.data
            #self.get_logger().info(str(message))
            #self.get_logger().info(str(self.array1))
            #self.get_logger().info(str(msg.data))
            if len(self.array1) == 0:
                self.set_array1(msg.data)
                self.get_logger().info(str(self.array1))

            self.check_publisher_status()

        def sub_callback_array2(self, msg):
            #self.get_logger().info(str(msg.data))
            if len(self.array2) ==0:
                self.set_array2(msg.data)
                self.get_logger().info(str(self.array2))
                
            self.check_publisher_status()

        #check if two messages were received / sort the arrays / publish the message
        def check_publisher_status(self): 
            a1=list(self.get_array1())
            a2=list(self.get_array2())
            self.get_logger().info("a1: "+str(a1))
            self.get_logger().info("a2: "+str(a2))
            if len(a1) != 0 and len(a2) != 0:
                msg = Int32MultiArray()
                msg.data = sorted(a1+a2)
                self.publisher_.publish(msg)
                #self.get_logger().info("sorted: "+str(sorted(a1+a2)))
                self.get_logger().info('Publishing: "%a"' % str(msg.data))
                self.array1=[]
                self.array2=[]





def main(args=None):
    rclpy.init(args=args)

    merge_arrays = MergeArrays()

    rclpy.spin(merge_arrays)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    merge_arrays.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()