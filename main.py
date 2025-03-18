import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

calorias = ctrl.Antecedent(np.arange(0, 3000, 1), 'calorias')
atividadeFisica = ctrl.Antecedent(np.arange(0, 10, 1), 'atividadeFisica')
peso = ctrl.Consequent(np.arange(0, 200, 1), 'peso')

calorias['baixa'] = fuzz.trimf(calorias.universe, [0, 0, 1500])
calorias['media'] = fuzz.trimf(calorias.universe, [0, 1500, 3000])
calorias['alta'] = fuzz.trimf(calorias.universe, [1500, 3000, 3000])

atividadeFisica['baixa'] = fuzz.trimf(atividadeFisica.universe, [0, 0, 5])
atividadeFisica['media'] = fuzz.trimf(atividadeFisica.universe, [0, 5, 10])
atividadeFisica['alta'] = fuzz.trimf(atividadeFisica.universe, [5, 10, 10])

peso['baixo'] = fuzz.trimf(peso.universe, [0, 0, 100])
peso['medio'] = fuzz.trimf(peso.universe, [0, 100, 200])
peso['alto'] = fuzz.trimf(peso.universe, [100, 200, 200])

calorias.automf(names=['baixa', 'media', 'alta'])

atividadeFisica.automf(names=['baixa', 'media', 'alta'])

peso.automf(names=['magro', 'media', 'obesidade'])

regra1= ctrl.Rule(calorias['baixa'] & atividadeFisica['baixa'], peso['magro'])
regra2= ctrl.Rule(calorias['media'] & atividadeFisica['media'], peso['media'])
regra3= ctrl.Rule(calorias['media'] & atividadeFisica['alta'], peso['magro'])
regra4= ctrl.Rule(calorias['alta'] & atividadeFisica['baixa'], peso['obesidade'])
regra5= ctrl.Rule(calorias['alta'] & atividadeFisica['media'], peso['obesidade'])
regra6= ctrl.Rule(calorias['alta'] & atividadeFisica['alta'], peso['media'])


controlador = ctrl.ControlSystem([regra1, regra2, regra3,regra4, regra5, regra6])


simulaPeso = ctrl.ControlSystemSimulation(controlador)
simulaPeso.input['calorias'] = 500
simulaPeso.input['atividadeFisica'] = 5

simulaPeso.compute()

print(simulaPeso.output['peso'])
calorias.view(sim=simulaPeso)
peso.view(sim=simulaPeso)
atividadeFisica.view(sim=simulaPeso)
plt.show()