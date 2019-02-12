 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        style = {'description_width': '250px'}
        layout = {'width': '400px'}

        self.tumor_radius = FloatText(
          description='tumor_radius',
          value=250.0,
          step=10,
          style=style, layout=layout)

        self.oncoprotein_mean = FloatText(
          description='oncoprotein_mean',
          value=1.0,
          step=0.1,
          style=style, layout=layout)

        self.oncoprotein_sd = FloatText(
          description='oncoprotein_sd',
          value=0.25,
          step=0.01,
          style=style, layout=layout)

        self.oncoprotein_min = FloatText(
          description='oncoprotein_min',
          value=0.0,
          step=0.01,
          style=style, layout=layout)

        self.oncoprotein_max = FloatText(
          description='oncoprotein_max',
          value=2,
          step=0.1,
          style=style, layout=layout)

        param_button_layout={'width':'400px'} 

        desc_row1 = Button(description='initial size of the tumor', disabled=True, layout=param_button_layout) 
        desc_row1.style.button_color = 'lightgreen'
        desc_row2 = Button(description='desired mean (for random dist)', disabled=True, layout=param_button_layout) 
        desc_row2.style.button_color = 'tan'
        desc_row3 = Button(description='desired std dev (for random dist)', disabled=True, layout=param_button_layout) 
        desc_row3.style.button_color = 'lightgreen'
        desc_row4 = Button(description='min threshold', disabled=True, layout=param_button_layout) 
        desc_row4.style.button_color = 'tan'
        desc_row5 = Button(description='max threshold', disabled=True, layout=param_button_layout) 
        desc_row5.style.button_color = 'lightgreen'

        row1 = [self.tumor_radius, Label('micron' , layout=Layout(flex='1 1 auto', width='auto')), desc_row1] 
        row2 = [self.oncoprotein_mean, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row2] 
        row3 = [self.oncoprotein_sd, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row3] 
        row4 = [self.oncoprotein_min, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row4] 
        row5 = [self.oncoprotein_max, Label('' , layout=Layout(flex='1 1 auto', width='auto')), desc_row5] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.oncoprotein_mean.value = float(uep.find('.//oncoprotein_mean').text)
        self.oncoprotein_sd.value = float(uep.find('.//oncoprotein_sd').text)
        self.oncoprotein_min.value = float(uep.find('.//oncoprotein_min').text)
        self.oncoprotein_max.value = float(uep.find('.//oncoprotein_max').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//oncoprotein_mean').text = str(self.oncoprotein_mean.value)
        uep.find('.//oncoprotein_sd').text = str(self.oncoprotein_sd.value)
        uep.find('.//oncoprotein_min').text = str(self.oncoprotein_min.value)
        uep.find('.//oncoprotein_max').text = str(self.oncoprotein_max.value)
