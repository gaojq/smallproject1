import unittest
import time
import subprocess
import os


class Test3(unittest.TestCase):
    

    def test_number_of_photos(self):
    	count = 0
    	subprocess.call("python Video.py",shell = True)
    	for file in os.listdir('.'):
        	if file.endswith('Video.mp4'):
        		count = count + 1
    	self.assertEqual(count,1)






if __name__ == '__main__':
    unittest.main()
