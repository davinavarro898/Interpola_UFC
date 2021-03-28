import pandas as pd
from ClassesDavi.FunctionsDavi.InterpolationFunction import interpolMe


class SuperHeatedDataFrameSI:
    def __init__(self, fluid, pressure):
        self.fluid = fluid
        self.pressure = pressure

    def research(self):
        data_frame = \
            pd.read_excel(f'{self.fluid}_SI.xlsx', sheet_name=f'{self.fluid}_SUPER_AQ_{self.pressure}bar_SI')
        top_number = data_frame.iloc[0, 0]
        bottom_number = data_frame.iloc[-1, 0]
        rows = []
        for k in data_frame['Temp(oC)']:
            rows.append(k)
        data_frame.index = rows
        del data_frame['Temp(oC)']
        columns = []
        for column in data_frame:
            columns.append(column)
        print(data_frame)
        print('\033[0;33mDIGITE A TEMPERATURA ESCOLHIDA PARA OBTER OS DADOS\n'
              'DIGITE QUALQUER LETRA PARA ENCERRAR A CONSULTA\033[m')
        while True:
            try:
                input_temperature = float(input('\033[0;32mTEMPERATURA EM CELSIUS:\033[m'))
            except:
                print('\n\033[0;32mATE A PROXIMA!\033[m\n')
                break
            else:
                if input_temperature < top_number or input_temperature > bottom_number:
                    print('\n\033[0;31mNUMERO FORA DA TABELA\033[m\n')

                elif input_temperature in rows:
                    print(data_frame.loc[input_temperature])

                else:
                    values_list = []
                    for i, c1 in enumerate(rows):
                        if i > 0:
                            if rows[i - 1] < input_temperature < rows[i]:
                                for column in data_frame:
                                    val = interpolMe(input_temperature, rows[i - 1], rows[i],
                                                     data_frame.loc[rows[i - 1], f'{column}'],
                                                     data_frame.loc[rows[i], f'{column}'])
                                    values_list.append(val)
                    for pos, values in enumerate(values_list):
                        print(columns[pos], '---' * 3, '>', values)
