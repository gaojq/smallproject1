import unittest
import time
import subprocess


class Test1(unittest.TestCase):
    

    def test_time(self):
        start = time.clock()
        subprocess.call("python Twitter.py",shell = True)
        stop = time.clock()
        time1 = stop - start
        self.assertLess(time1,0.000000000001)






if __name__ == '__main__':
    unittest.main()
