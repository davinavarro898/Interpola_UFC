import pandas as pd
import numpy as np
from ClassesDavi.FunctionsDavi.InterpolationFunction import interpolMe


class ChangeSuperHeatedPressureSI:
    def __init__(self, fluid, pressure1, chosen_pressure, pressure2):
        self.fluid = fluid
        self.pressure1 = pressure1
        self.pressure2 = pressure2
        self.chosen_pressure = chosen_pressure

    def interpolDataFrame(self):
        data_frame1 = pd.read_excel(f'{self.fluid}_SI.xlsx', sheet_name=f'{self.fluid}_SUPER_AQ_{self.pressure1}bar_SI')
        top_number1 = data_frame1.iloc[0, 0]
        bottom_number1 = data_frame1.iloc[-1, 0]
        rows1 = []
        for c1 in data_frame1['Temp(oC)']:
            rows1.append(c1)
        data_frame1.index = rows1[:]
        del data_frame1['Temp(oC)']
        columns1 = []
        for column in data_frame1:
            columns1.append(column)
        data_frame2 = pd.read_excel(f'{self.fluid}_SI.xlsx', sheet_name=f'{self.fluid}_SUPER_AQ_{self.pressure2}bar_SI')
        top_number2 = data_frame2.iloc[0, 0]
        bottom_number2 = data_frame2.iloc[-1, 0]
        rows2 = []
        for c2 in data_frame2['Temp(oC)']:
            rows2.append(c2)
        data_frame2.index = rows2[:]
        del data_frame2['Temp(oC)']
        columns2 = []
        for column in data_frame2:
            columns2.append(column)
        print(f'\033[0;33mAS PROPRIEDADES DESEJADAS SERAO INTERPOLADAS ENTRE AS TABELAS DE '
              f'{self.pressure1} bar E {self.pressure2} bar '
              f'MOSTRADAS A SEGUIR:\n\033[m')
        print(f'\033[0;33mTABELA DE {self.pressure1} bar\033[m:\n')
        print(data_frame1)
        print(f'\033[0;33mTABELA DE {self.chosen_pressure} bar\033[m:\n')
        print(interpolMe(self.chosen_pressure, self.pressure1, self.pressure2, data_frame1, data_frame2))
        print(f'\033[0;33m\nTABELA DE {self.pressure2} bar\033[m:\n')
        print(data_frame2)
        print(f'\033[0;33m\nDIGITE A TEMPERATURA ESCOLHIDA PARA OBTER OS DADOS\n'
              f'DIGITE QUALQUER LETRA PARA ENCERRAR A CONSULTA\033[m\n')
        while True:
            try:
                input_temperature = float(input('\033[0;32mTEMPERATURA EM CELSIUS:\033[m'))
                if ((input_temperature not in rows1) and (input_temperature in rows2)) or \
                        ((input_temperature not in rows2) and (input_temperature in rows1)):
                    input_temperature += 0.000000000001
            except:
                print('\n\033[0;33mATE A PROXIMA!\033[m\n')
                break
            else:
                print(f'\n\033[0;36mTEMPERATURA ESCOLHIDA:{input_temperature}'
                      f' oC\n\033[m')
                if (input_temperature <= top_number1 or input_temperature > bottom_number1) or (
                        input_temperature <= top_number2 or input_temperature > bottom_number2):
                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                    continue
                elif (input_temperature in rows1) or (input_temperature in rows2):
                    try:
                        print(interpolMe(self.chosen_pressure, self.pressure1,
                                         self.pressure2, data_frame1.loc[input_temperature],
                                         data_frame2.loc[input_temperature]))
                    except:
                        print('\033[0;31mO ALGORITMO NAO COMPUTA VALORES PRESENTES EM APENAS UMA DAS TABELAS\033[m')
                    else:
                        continue
                else:
                    values_list1 = []
                    for i, c1 in enumerate(rows1):
                        if i > 0:
                            if rows1[i - 1] < input_temperature < rows1[i]:
                                for column in data_frame1:
                                    val1 = interpolMe(input_temperature, rows1[i - 1], rows1[i],
                                                      data_frame1.loc[rows1[i - 1], f'{column}'],
                                                      data_frame1.loc[rows1[i], f'{column}'])
                                    values_list1.append(val1)
                    values_list2 = []
                    for i, c2 in enumerate(rows2):
                        if i > 0:
                            if rows2[i - 1] < input_temperature < rows2[i]:
                                for column in data_frame2:
                                    val2 = interpolMe(input_temperature, rows2[i - 1], rows2[i],
                                                      data_frame2.loc[rows2[i - 1], f'{column}'],
                                                      data_frame2.loc[rows2[i], f'{column}'])
                                    values_list2.append(val2)
                    print('\n\n')
                    final_values = interpolMe(self.chosen_pressure, self.pressure1, self.pressure2,
                                              np.array(values_list1), np.array(values_list2))
                    for pos, values in enumerate(list(final_values)):
                        print(columns1[pos], '---' * 3, '>', values)
