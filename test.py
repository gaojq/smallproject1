import Twitter
import video
import Lable

import glob


Imager.twitter_api('consumer_token',"consumer_secret","key","secret")

Twitter.image_down("etcwilde")


for infile in glob.glob("*.jpg"):
	lab= vision.labels(infile,'')
	if (lab != False):
		img2video.labelonImage(lab,infile)

img2video.jpg2mp4()
