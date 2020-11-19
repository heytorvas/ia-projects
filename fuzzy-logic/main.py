# pip install scikit-fuzzy

import numpy, skfuzzy
from skfuzzy import control

tip = control.Consequent(numpy.arange(0, 30, 1), 'tip')
service = control.Antecedent(numpy.arange(0, 30, 1), 'service')
food = control.Antecedent(numpy.arange(0, 26, 1), 'food')

food.automf(names=['bad', 'good', 'great'])

tip['little'] = skfuzzy.trapmf(tip.universe, [0, 5, 7, 15])
tip['medium'] = skfuzzy.trapmf(tip.universe, [0, 14, 16, 30])
tip['much'] = skfuzzy.trapmf(tip.universe, [15, 25, 27, 30])

service['bad'] = skfuzzy.trapmf(tip.universe, [0, 5, 7, 15])
service['good'] = skfuzzy.trapmf(tip.universe, [0, 14, 16, 30])
service['great'] = skfuzzy.trapmf(tip.universe, [15, 25, 27, 30])

tip.view()
service.view()
food.view()

rule1 = control.Rule(service['great'] | food['great'], tip['much'])
rule2 = control.Rule(service['good'], tip['medium'])
rule3 = control.Rule(service['bad'] & food['bad'], tip['little'])

tip_control = control.ControlSystem([rule1, rule2, rule3])
tip_sim = control.ControlSystemSimulation(tip_control)

tip_sim.input['service'] = 30.5
tip_sim.input['food'] = 15.4

tip_sim.compute()

tip.view(sim=tip_sim)
service.view(sim=tip_sim)
food.view(sim=tip_sim)