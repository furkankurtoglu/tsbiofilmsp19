 
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

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='seeding_method', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.seeding_method = Text(
          value='box',
          style=style, layout=widget_layout)

        param_name2 = Button(description='cell_default_inital_energy', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.cell_default_inital_energy = FloatText(
          value=7.01,
          step=0.1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='cell_default_energy_creation_rate', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.cell_default_energy_creation_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name4 = Button(description='cell_default_energy_use_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.cell_default_energy_use_rate = FloatText(
          value=0.02,
          step=0.001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='cell_default_cycle_energy_threshold', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.cell_default_cycle_energy_threshold = FloatText(
          value=10.0 ,
          step=1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='cell_default_death_energy_threshold', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.cell_default_death_energy_threshold = FloatText(
          value=6,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='cell_default_aplha', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.cell_default_aplha = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name8 = Button(description='cell_default_beta', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.cell_default_beta = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='cell_default_gamma', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.cell_default_gamma = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='cell_default_rho', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.cell_default_rho = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name11 = Button(description='cell_default_phi', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.cell_default_phi = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='cell_default_chi', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.cell_default_chi = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='wound_cell_glucose_secretion_rate', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.wound_cell_glucose_secretion_rate = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='wound_cell_ECM_secretion_rate', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.wound_cell_ECM_secretion_rate = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name15 = Button(description='anaerobic_cell_alpha', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.anaerobic_cell_alpha = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name16 = Button(description='anaerobic_cell_beta', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.anaerobic_cell_beta = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='anaerobic_cell_gamma', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.anaerobic_cell_gamma = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='anaerobic_cell_rho', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.anaerobic_cell_rho = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name19 = Button(description='anaerobic_cell_phi', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.anaerobic_cell_phi = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='anaerobic_cell_chi', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.anaerobic_cell_chi = FloatText(
          value=2.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name21 = Button(description='anaerobic_ECM_secretion_rate', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.anaerobic_ECM_secretion_rate = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name22 = Button(description='anaerobic_glucose_uptake_rate', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.anaerobic_glucose_uptake_rate = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name23 = Button(description='aerobic_cell_alpha', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.aerobic_cell_alpha = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name24 = Button(description='aerobic_cell_beta', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.aerobic_cell_beta = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name25 = Button(description='aerobic_cell_gamma', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.aerobic_cell_gamma = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name26 = Button(description='aerobic_cell_rho', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.aerobic_cell_rho = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name27 = Button(description='aerobic_cell_phi', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.aerobic_cell_phi = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name28 = Button(description='aerobic_cell_chi', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.aerobic_cell_chi = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name29 = Button(description='aerobic_ECM_secretion_rate', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.aerobic_ECM_secretion_rate = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name30 = Button(description='aerobic_glucose_uptake_rate', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.aerobic_glucose_uptake_rate = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name31 = Button(description='aerobic_oxygen_uptake_rate', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.aerobic_oxygen_uptake_rate = FloatText(
          value=1000.0,
          step=100,
          style=style, layout=widget_layout)

        param_name32 = Button(description='apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.apoptosis_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name33 = Button(description='proliferation_rate', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.proliferation_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name34 = Button(description='ECM_diffusion_coeff', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.ECM_diffusion_coeff = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name35 = Button(description='ECM_decay_constant', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'lightgreen'

        self.ECM_decay_constant = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name36 = Button(description='glucose_diffusion_coeff', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'tan'

        self.glucose_diffusion_coeff = FloatText(
          value=1.6e3,
          step=100,
          style=style, layout=widget_layout)

        param_name37 = Button(description='glucose_decay_constant', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'lightgreen'

        self.glucose_decay_constant = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='a.u', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='a.u/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='a.u/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='a.u', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='a.u', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'
        units_button31 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'lightgreen'
        units_button32 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'tan'
        units_button33 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'lightgreen'
        units_button34 = Button(description='um2/min', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'tan'
        units_button35 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'lightgreen'
        units_button36 = Button(description='um2/min', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'tan'
        units_button37 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'lightgreen'

        desc_button1 = Button(description='Method for seeding. Can be vertical,horizontal, random, or box (default)', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='Initialized energy level', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='Energy creation rate for bacterial cells', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='Energy usage rate for bacterial cells', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='Cycling energy threshold for bacterial cells', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='Apoptosis energy threshold for bacterial cells', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='Energy creation Rate modifier for aerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='Energy creation Rate modifier for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='Energy usage modulator for bacterial cells', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='Energy degradation rate modifier for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='Energy creation rate modulator for aerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='Energy creation rate modulator for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='Glucose secretion rate for wound cells', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='Glucose secretion rate for wound cells', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='Energy Creation Rate modifier for aerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='Energy Creation Rate modifier for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='Energy usage modulator for bacterial cells', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='Energy degradation rate modifier for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='Energy creation rate modulator for aerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='Energy creation rate modulator for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='ECM creation rate for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='Glucose uptake rate for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='Energy Creation Rate modifier for aerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='Energy Creation Rate modifier for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='Energy usage modulator for bacterial cells', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='Energy degradation rate modifier for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='Energy creation rate modulator for aerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='Energy creation rate modulator for anaerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='ECM creation rate for aerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='Glucose uptake rate for aerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='Oxygen uptake rate for aerobic cells', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='Apoptosis rate for bacterial cells', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='Proliferation rate for bacterial cells', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'

        row1 = [param_name1, self.seeding_method, units_button1, desc_button1] 
        row2 = [param_name2, self.cell_default_inital_energy, units_button2, desc_button2] 
        row3 = [param_name3, self.cell_default_energy_creation_rate, units_button3, desc_button3] 
        row4 = [param_name4, self.cell_default_energy_use_rate, units_button4, desc_button4] 
        row5 = [param_name5, self.cell_default_cycle_energy_threshold, units_button5, desc_button5] 
        row6 = [param_name6, self.cell_default_death_energy_threshold, units_button6, desc_button6] 
        row7 = [param_name7, self.cell_default_aplha, units_button7, desc_button7] 
        row8 = [param_name8, self.cell_default_beta, units_button8, desc_button8] 
        row9 = [param_name9, self.cell_default_gamma, units_button9, desc_button9] 
        row10 = [param_name10, self.cell_default_rho, units_button10, desc_button10] 
        row11 = [param_name11, self.cell_default_phi, units_button11, desc_button11] 
        row12 = [param_name12, self.cell_default_chi, units_button12, desc_button12] 
        row13 = [param_name13, self.wound_cell_glucose_secretion_rate, units_button13, desc_button13] 
        row14 = [param_name14, self.wound_cell_ECM_secretion_rate, units_button14, desc_button14] 
        row15 = [param_name15, self.anaerobic_cell_alpha, units_button15, desc_button15] 
        row16 = [param_name16, self.anaerobic_cell_beta, units_button16, desc_button16] 
        row17 = [param_name17, self.anaerobic_cell_gamma, units_button17, desc_button17] 
        row18 = [param_name18, self.anaerobic_cell_rho, units_button18, desc_button18] 
        row19 = [param_name19, self.anaerobic_cell_phi, units_button19, desc_button19] 
        row20 = [param_name20, self.anaerobic_cell_chi, units_button20, desc_button20] 
        row21 = [param_name21, self.anaerobic_ECM_secretion_rate, units_button21, desc_button21] 
        row22 = [param_name22, self.anaerobic_glucose_uptake_rate, units_button22, desc_button22] 
        row23 = [param_name23, self.aerobic_cell_alpha, units_button23, desc_button23] 
        row24 = [param_name24, self.aerobic_cell_beta, units_button24, desc_button24] 
        row25 = [param_name25, self.aerobic_cell_gamma, units_button25, desc_button25] 
        row26 = [param_name26, self.aerobic_cell_rho, units_button26, desc_button26] 
        row27 = [param_name27, self.aerobic_cell_phi, units_button27, desc_button27] 
        row28 = [param_name28, self.aerobic_cell_chi, units_button28, desc_button28] 
        row29 = [param_name29, self.aerobic_ECM_secretion_rate, units_button29, desc_button29] 
        row30 = [param_name30, self.aerobic_glucose_uptake_rate, units_button30, desc_button30] 
        row31 = [param_name31, self.aerobic_oxygen_uptake_rate, units_button31, desc_button31] 
        row32 = [param_name32, self.apoptosis_rate, units_button32, desc_button32] 
        row33 = [param_name33, self.proliferation_rate, units_button33, desc_button33] 
        row34 = [param_name34, self.ECM_diffusion_coeff, units_button34, desc_button34] 
        row35 = [param_name35, self.ECM_decay_constant, units_button35, desc_button35] 
        row36 = [param_name36, self.glucose_diffusion_coeff, units_button36, desc_button36] 
        row37 = [param_name37, self.glucose_decay_constant, units_button37, desc_button37] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.seeding_method.value = (uep.find('.//seeding_method').text)
        self.cell_default_inital_energy.value = float(uep.find('.//cell_default_inital_energy').text)
        self.cell_default_energy_creation_rate.value = float(uep.find('.//cell_default_energy_creation_rate').text)
        self.cell_default_energy_use_rate.value = float(uep.find('.//cell_default_energy_use_rate').text)
        self.cell_default_cycle_energy_threshold.value = float(uep.find('.//cell_default_cycle_energy_threshold').text)
        self.cell_default_death_energy_threshold.value = float(uep.find('.//cell_default_death_energy_threshold').text)
        self.cell_default_aplha.value = float(uep.find('.//cell_default_aplha').text)
        self.cell_default_beta.value = float(uep.find('.//cell_default_beta').text)
        self.cell_default_gamma.value = float(uep.find('.//cell_default_gamma').text)
        self.cell_default_rho.value = float(uep.find('.//cell_default_rho').text)
        self.cell_default_phi.value = float(uep.find('.//cell_default_phi').text)
        self.cell_default_chi.value = float(uep.find('.//cell_default_chi').text)
        self.wound_cell_glucose_secretion_rate.value = float(uep.find('.//wound_cell_glucose_secretion_rate').text)
        self.wound_cell_ECM_secretion_rate.value = float(uep.find('.//wound_cell_ECM_secretion_rate').text)
        self.anaerobic_cell_alpha.value = float(uep.find('.//anaerobic_cell_alpha').text)
        self.anaerobic_cell_beta.value = float(uep.find('.//anaerobic_cell_beta').text)
        self.anaerobic_cell_gamma.value = float(uep.find('.//anaerobic_cell_gamma').text)
        self.anaerobic_cell_rho.value = float(uep.find('.//anaerobic_cell_rho').text)
        self.anaerobic_cell_phi.value = float(uep.find('.//anaerobic_cell_phi').text)
        self.anaerobic_cell_chi.value = float(uep.find('.//anaerobic_cell_chi').text)
        self.anaerobic_ECM_secretion_rate.value = float(uep.find('.//anaerobic_ECM_secretion_rate').text)
        self.anaerobic_glucose_uptake_rate.value = float(uep.find('.//anaerobic_glucose_uptake_rate').text)
        self.aerobic_cell_alpha.value = float(uep.find('.//aerobic_cell_alpha').text)
        self.aerobic_cell_beta.value = float(uep.find('.//aerobic_cell_beta').text)
        self.aerobic_cell_gamma.value = float(uep.find('.//aerobic_cell_gamma').text)
        self.aerobic_cell_rho.value = float(uep.find('.//aerobic_cell_rho').text)
        self.aerobic_cell_phi.value = float(uep.find('.//aerobic_cell_phi').text)
        self.aerobic_cell_chi.value = float(uep.find('.//aerobic_cell_chi').text)
        self.aerobic_ECM_secretion_rate.value = float(uep.find('.//aerobic_ECM_secretion_rate').text)
        self.aerobic_glucose_uptake_rate.value = float(uep.find('.//aerobic_glucose_uptake_rate').text)
        self.aerobic_oxygen_uptake_rate.value = float(uep.find('.//aerobic_oxygen_uptake_rate').text)
        self.apoptosis_rate.value = float(uep.find('.//apoptosis_rate').text)
        self.proliferation_rate.value = float(uep.find('.//proliferation_rate').text)
        self.ECM_diffusion_coeff.value = float(uep.find('.//ECM_diffusion_coeff').text)
        self.ECM_decay_constant.value = float(uep.find('.//ECM_decay_constant').text)
        self.glucose_diffusion_coeff.value = float(uep.find('.//glucose_diffusion_coeff').text)
        self.glucose_decay_constant.value = float(uep.find('.//glucose_decay_constant').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//seeding_method').text = str(self.seeding_method.value)
        uep.find('.//cell_default_inital_energy').text = str(self.cell_default_inital_energy.value)
        uep.find('.//cell_default_energy_creation_rate').text = str(self.cell_default_energy_creation_rate.value)
        uep.find('.//cell_default_energy_use_rate').text = str(self.cell_default_energy_use_rate.value)
        uep.find('.//cell_default_cycle_energy_threshold').text = str(self.cell_default_cycle_energy_threshold.value)
        uep.find('.//cell_default_death_energy_threshold').text = str(self.cell_default_death_energy_threshold.value)
        uep.find('.//cell_default_aplha').text = str(self.cell_default_aplha.value)
        uep.find('.//cell_default_beta').text = str(self.cell_default_beta.value)
        uep.find('.//cell_default_gamma').text = str(self.cell_default_gamma.value)
        uep.find('.//cell_default_rho').text = str(self.cell_default_rho.value)
        uep.find('.//cell_default_phi').text = str(self.cell_default_phi.value)
        uep.find('.//cell_default_chi').text = str(self.cell_default_chi.value)
        uep.find('.//wound_cell_glucose_secretion_rate').text = str(self.wound_cell_glucose_secretion_rate.value)
        uep.find('.//wound_cell_ECM_secretion_rate').text = str(self.wound_cell_ECM_secretion_rate.value)
        uep.find('.//anaerobic_cell_alpha').text = str(self.anaerobic_cell_alpha.value)
        uep.find('.//anaerobic_cell_beta').text = str(self.anaerobic_cell_beta.value)
        uep.find('.//anaerobic_cell_gamma').text = str(self.anaerobic_cell_gamma.value)
        uep.find('.//anaerobic_cell_rho').text = str(self.anaerobic_cell_rho.value)
        uep.find('.//anaerobic_cell_phi').text = str(self.anaerobic_cell_phi.value)
        uep.find('.//anaerobic_cell_chi').text = str(self.anaerobic_cell_chi.value)
        uep.find('.//anaerobic_ECM_secretion_rate').text = str(self.anaerobic_ECM_secretion_rate.value)
        uep.find('.//anaerobic_glucose_uptake_rate').text = str(self.anaerobic_glucose_uptake_rate.value)
        uep.find('.//aerobic_cell_alpha').text = str(self.aerobic_cell_alpha.value)
        uep.find('.//aerobic_cell_beta').text = str(self.aerobic_cell_beta.value)
        uep.find('.//aerobic_cell_gamma').text = str(self.aerobic_cell_gamma.value)
        uep.find('.//aerobic_cell_rho').text = str(self.aerobic_cell_rho.value)
        uep.find('.//aerobic_cell_phi').text = str(self.aerobic_cell_phi.value)
        uep.find('.//aerobic_cell_chi').text = str(self.aerobic_cell_chi.value)
        uep.find('.//aerobic_ECM_secretion_rate').text = str(self.aerobic_ECM_secretion_rate.value)
        uep.find('.//aerobic_glucose_uptake_rate').text = str(self.aerobic_glucose_uptake_rate.value)
        uep.find('.//aerobic_oxygen_uptake_rate').text = str(self.aerobic_oxygen_uptake_rate.value)
        uep.find('.//apoptosis_rate').text = str(self.apoptosis_rate.value)
        uep.find('.//proliferation_rate').text = str(self.proliferation_rate.value)
        uep.find('.//ECM_diffusion_coeff').text = str(self.ECM_diffusion_coeff.value)
        uep.find('.//ECM_decay_constant').text = str(self.ECM_decay_constant.value)
        uep.find('.//glucose_diffusion_coeff').text = str(self.glucose_diffusion_coeff.value)
        uep.find('.//glucose_decay_constant').text = str(self.glucose_decay_constant.value)
