import sys
import rospy
from lab2_2021.srv import AddTwoInts, AddTwoIntsResponse

def add_two_ints_client(x, y):
  rospy.wait_for_service('add_two_ints')
  
  try:
    add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
    resp1 = add_two_ints(x, y)
    return resp1.sum
  except (rospy.ServiceException, e):
    print("Service call failed: %s" %e)
   
def usage():
  return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":

  if len(sys.argv) == 3:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
  else:
    print('default: 5 + 3 = 8')
    x = rospy.get_param("Int_1")
    y = rospy.get_param("Int_2")
  print("Requesting %s+%s"%(x, y))
  print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
