import pandas as pd
from ClassesDavi.FunctionsDavi.InterpolationFunction import interpolMe


class SaturatedDataFramePressureEnglish:
    def __init__(self, fluid):
        self.fluid = fluid

    def research(self):
        data_frame = pd.read_excel(f'{self.fluid}_INGLES.xlsx', sheet_name=f'{self.fluid}_SAT_PRESS_INGLES')
        top_number = data_frame.iloc[0, 0]
        bottom_number = data_frame.iloc[-1, 0]
        rows = []
        for k in data_frame['Press(psi)']:
            rows.append(k)
        data_frame.index = rows
        del data_frame['Press(psi)']
        columns = []
        for column in data_frame:
            columns.append(column)
        print(data_frame)
        print('\033[0;33mDIGITE A PRESSAO ESCOLHIDA PARA OBTER OS DADOS\n'
              'DIGITE QUALQUER LETRA PARA ENCERRAR A CONSULTA\033[m')
        while True:
            try:
                input_pressure = float(input('\033[0;32mPRESSAO EM PSI:\033[m'))
            except:
                print('\n\033[0;32mATE A PROXIMA!\033[m\n')
                break
            else:
                if input_pressure < top_number or input_pressure > bottom_number:
                    print('\n\033[0;31mNUMERO FORA DA TABELA\033[m\n')

                elif input_pressure in rows:
                    print(data_frame.loc[input_pressure])

                else:
                    values_list = []
                    for i, c1 in enumerate(rows):
                        if i > 0:
                            if rows[i - 1] < input_pressure < rows[i]:
                                for column in data_frame:
                                    val = interpolMe(input_pressure, rows[i - 1], rows[i],
                                                     data_frame.loc[rows[i - 1], f'{column}'],
                                                     data_frame.loc[rows[i], f'{column}'])
                                    values_list.append(val)
                    for pos, values in enumerate(values_list):
                        print(columns[pos], '---' * 3, '>', values)
