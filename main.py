from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, BoundedNumericProperty, ObjectProperty
from kivy.clock import Clock

class Rect(Widget):
  col = ListProperty([1,1,1,1])

class Layers(Widget):
  r1 = ObjectProperty(None)
  r2 = ObjectProperty(None)

  r_y = BoundedNumericProperty(0,min=-100,max=100)
  inc = 1

  def __init__(self,*args,**kwargs):
    super(Layers,self).__init__(*args,**kwargs)
    Clock.schedule_interval(self.update,0)

  def update(self,t):
    try:
      self.r_y += self.inc
      self.r2.y += self.inc
    except ValueError:
      self.inc *= -1

    children_sorted = sorted(self.children,key=lambda w: w.y)
    children_sorted.reverse()

    for i in children_sorted:
      self.remove_widget(i)
      self.add_widget(i)

class Main(App):
  def build(self):
    return Layers()

Main().run()
