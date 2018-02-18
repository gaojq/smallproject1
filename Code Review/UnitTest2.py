import unittest
import time
import subprocess
import os


class Test2(unittest.TestCase):
    

    def test_number_of_photos(self):
    	count = 0
    	subprocess.call("python Twitter.py",shell = True)
    	for file in os.listdir('.'):
        	if file.endswith('jpg'):
        		count = count + 1




    	self.assertEqual(count,21)






if __name__ == '__main__':
    unittest.main()
