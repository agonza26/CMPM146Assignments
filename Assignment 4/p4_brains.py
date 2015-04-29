
import random

# EXAMPLE STATE MACHINE
class MantisBrain:

  def __init__(self, body):
    self.body = body
    self.state = 'idle'
    self.target = None
    





  def find_Obstacle(self):
          try:
            self.target=self.body.find_nearest("Obstacle")
            self.body.follow(self.target)
            self.body.set_alarm(0.25)
            self.state = 'rage'
          except:
            print("no targets sorry, Mantis, find_Obstacle")
            self.state = "idle"







  def handle_event(self, message, details):

    if self.state is 'idle':



      if message == 'timer':
        # go to a random point, wake up sometime in the next 10 seconds
        world = self.body.world
        x, y = random.random()*world.width, random.random()*world.height
        self.body.go_to((x,y))
        self.body.set_alarm(random.random()*10)



        if random.random() <0.2:
          print("RRRRRRAAAAAAAAHHHHHHH")

          self.body.color = self.body.rage_color
          self.body.stop()
          self.find_Obstacle();



      elif message == 'collide' and details['what'] == 'Slug':
        # a slug bumped into us; get curious
        self.state = 'curious'
        self.body.set_alarm(1) # think about this for a sec
        self.body.stop()
        self.target = details['who']





    elif self.state == 'rage':

      if random.random() <0.05:
        print("I calmed down")
        self.body.color = self.body.default_color
        self.body.stop()
        self.state = "idle"
        self.target = None
      
      elif message == 'timer':
        self.target=self.body.find_nearest("Obstacle")
        self.body.follow(self.target)
        self.body.set_alarm(0.25)

      elif message == 'collide' and details['what'] == 'Obstacle':
      # a slug bumped into us; get curious
        self.body.radius += 0.3
        self.target.radius += 0.5








    elif self.state == 'curious':


      if message == 'timer':
        # chase down that slug who bumped into us
        if self.target:
          if random.random() < 0.5:
            self.body.stop()
            self.state = 'idle'
          else:
            self.body.follow(self.target)
          self.body.set_alarm(1)


      elif message == 'collide' and details['what'] == 'Slug':
        # we meet again!
        slug = details['who']
        slug.amount -= 0.01 # take a tiny little bite





    


























class SlugBrain:

  def __init__(self, body):
    self.body = body
    self.state = 'idle'
    self.target = None


    self.prev_state = 'idle' 
    self.prev_target = None



    self.have_resource = False






  def handle_order(self, details):
    if type(details) is tuple:
      self.state = "goto"
      self.target = details
      self.body.set_alarm(0.5)
      



    elif type(details) is str:

      if details in commands:
        if commands[details] is 'x':
          self.body.amount -= 0.51

        if commands[details] is 'i':
          self.state = 'idle'
          self.body.stop()

        elif commands[details] is 'a':
          self.state = 'attack'
          self.nearest_Mantis()

        elif commands[details] is 'b':
          self.state = 'build'
          self.nearest_Nest()


        elif commands[details] is 'h':
          if not self.have_resource:
            self.state = 'harvest'
            self.nearest_Resource()
          else:
            self.state = 'harvest'
            self.nearest_Nest()
      else:
        print("not in commands")










  def nearest_Mantis(self):
    try:
      self.target=self.body.find_nearest("Mantis")
      self.body.follow(self.target)
      self.body.set_alarm(1)
    except:
      print("no targets sorry, nearest_Mantis")
      self.state = "idle"



  def nearest_Nest(self):
    try:
      self.target=self.body.find_nearest("Nest")
      self.body.go_to(self.target)
      self.body.set_alarm(0.5)
    except:
      print("no targets sorry, nearest_Nest")
      self.state = "idle"
      

  def nearest_Resource(self):
    try:
      self.target=self.body.find_nearest("Resource")
      self.body.go_to(self.target)
      self.body.set_alarm(0.5)
    except:
      print("no targets sorry, nearest_Resource")
      self.state = "idle"
  








  def handle_event(self, message, details):
    if message == 'order':
        self.handle_order(details)
    




    if self.body.amount < 0.51:
      self.prev_state =  self.state 
      self.prev_target = self.target
      self.state = 'flee'
      self.nearest_Nest()



    #-------------------------------------------------
    if self.state is 'idle':

      if message == 'timer':
        self.body.stop()
    #-------------------------------------------------
    if self.state is 'goto':

      if message == 'timer':
        self.body.go_to(self.target)















    #-------------------------------------------------
    elif self.state is 'attack':

      if message == 'timer':
        self.nearest_Mantis()

      elif message == 'collide' and details['what'] == 'Mantis':
        self.body.stop()
        details['who'].amount-=5




    #-------------------------------------------------
    elif self.state is 'build':

      if self.target.amount ==1:
        self.state = 'idle'
        self.target = None

      elif message == 'timer':
        self.nearest_Nest()

      elif message == 'collide' and details['what'] == 'Nest':
        self.target = details['who']
        self.target.amount+= 0.01








   #-------------------------------------------------
    elif self.state is 'harvest':

      if message == 'timer':
        if not self.have_resource:
          self.nearest_Resource()
        else:
          self.nearest_Nest()

      elif message == 'collide' and details['what'] == 'Resource':
        if not self.have_resource:
          self.have_resource = True
          details['who'].amount-= 0.25
          self.nearest_Nest()


      elif message == 'collide' and details['what'] == 'Nest':
        if self.have_resource:
          self.have_resource = False
          self.nearest_Resource()


          if not self.have_resource:
            self.nearest_Resource()
          else:
            self.nearest_Nest()






    #-------------------------------------------------  




    elif self.state is 'flee': 



      if message == 'timer':
        self.nearest_Nest()



      elif message == 'collide' and details['what'] == 'Nest':
          self.body.amount += 0.51



      if self.body.amount >=0.51:
        self.state = self.prev_state 
        self.target = self.prev_target  













    






commands = {
  'i': 'i',
  'a': 'a',
  'b': 'b',
  'h': 'h',
  'x': 'x',
}


   

world_specification = {
  #'worldgen_seed': 13, # comment-out to randomize
  'nests': 2,
  'obstacles': 25,
  'resources': 0,
  'slugs': 5,
  'mantises': 15,
}

brain_classes = {
  'mantis': MantisBrain,
  'slug': SlugBrain,
}
