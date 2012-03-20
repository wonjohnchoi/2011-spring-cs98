# WDD Lab 8
# Starter code
#
# Add things where the comments say WDD TODO

import tornado.ioloop
from tornado.web import *

#########################
# Configuration options #
#########################

tornado_options = {
  "port": 8888
}

#########################
# Handlers go here      #
#########################

class MainHandler(RequestHandler):
  """
  Handles the index page, which displays the
    form for the user to fill out.
  Don't need to change this, but you can if
    you want to be fancy.
  """

  def get(self):
    self.render("index.html")

class DoublerHandler(RequestHandler):
  """
  Does the doubling.
  You need to fill out the request method(s).
  A helper method 'makeEmbedUrl' is provided for you;
    read the comments there to see how to use it.
  """

  ###########################
  # WDD TODO                #
  ###########################

  def get(self):
    # WDD TODO
    # Set the variables v1_url and v2_url correctly
    time = self.get_argument('time')
    v1_url = self.makeEmbedUrl(self.get_argument('id1'), time)
    v2_url = self.makeEmbedUrl(self.get_argument('id2'), time)
    self.render("double.html", v1_url=v1_url, v2_url=v2_url)

  ###### get ends here ######

  def makeEmbedUrl(self, videoID, startTime=0):
    """
    Makes a YouTube embed link.
    Usage:
      theUrl = self.makeEmbedURL(videoID, startTime)

      Where the first argument is the YouTube video ID (the part after youtube.com/watch?v=)
      And the second argument (optional) is the start time in seconds.
      The variable 'theUrl' will then contain the complete embed URL.
    """
    try:
      startTime = int(startTime)
    except:
      startTime = 0

    return "http://youtube.com/embed/%s?autoplay=1&start=%d" % (videoID, startTime)

############################
# Routes go here           #
############################
application = tornado.web.Application([

  # WDD TODO
  # Add more route(s) to handle the doubling

  (r"/",       MainHandler),
  (r"/double", DoublerHandler),

  ###### routes end here ######

#########################
# Don't change this     #
#########################
], debug=True,
   template_path=os.path.join(os.path.dirname(__file__), "templates"),
   static_path=os.path.join(os.path.dirname(__file__), "static"),
)

if __name__ == "__main__":
  application.listen(tornado_options["port"])
  tornado.ioloop.IOLoop.instance().start()
