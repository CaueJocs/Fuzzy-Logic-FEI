import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

calorias = ctrl.Antecedent(np.arange(0, 3000, 1), 'calorias')
peso = ctrl.Consequent(np.arange(0, 200, 1), 'peso')

#Triangular
calorias['baixa'] = fuzz.trimf(calorias.universe, [0, 0, 1500])
calorias['media'] = fuzz.trimf(calorias.universe, [0, 1500, 3000])
calorias['alta'] = fuzz.trimf(calorias.universe, [1500, 3000, 3000])
#calorias.view()
#plt.show()

#Gauss
calorias['baixa'] = fuzz.gaussmf(calorias.universe, 500, 400)
calorias['media'] = fuzz.gaussmf(calorias.universe, 1500, 600)
calorias['alta'] = fuzz.gaussmf(calorias.universe, 2500, 400)
#calorias.view()
#plt.show()

#Trapezoidal
calorias['baixa'] = fuzz.trapmf(calorias.universe, [0, 0, 1000, 1500])
calorias['media'] = fuzz.trapmf(calorias.universe, [1000, 1500, 2000, 2500])
calorias['alta'] = fuzz.trapmf(calorias.universe, [2000, 2500, 3000, 3000])
#calorias.view()
#plt.show()

peso['baixo'] = fuzz.trimf(peso.universe, [0, 0, 100])
peso['medio'] = fuzz.trimf(peso.universe, [0, 100, 200])
peso['alto'] = fuzz.trimf(peso.universe, [100, 200, 200])

calorias.automf(names=['baixa', 'media', 'alta'])


peso.automf(names=['magro', 'media', 'obesidade'])

regra1= ctrl.Rule(calorias['baixa'], peso['magro'])
regra2= ctrl.Rule(calorias['media'], peso['media'])
regra3= ctrl.Rule(calorias['alta'], peso['obesidade'])


controlador = ctrl.ControlSystem([regra1, regra2, regra3])


simulaPeso = ctrl.ControlSystemSimulation(controlador)
simulaPeso.input['calorias'] = 2500

simulaPeso.compute()

print(simulaPeso.output['peso'])
calorias.view(sim=simulaPeso)
peso.view(sim=simulaPeso)
plt.show()