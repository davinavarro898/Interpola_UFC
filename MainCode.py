import pandas as pd
from ClassesDavi.SI.SaturatedTemperatureSI import SaturatedDataFrameTemperatureSI
from ClassesDavi.SI.SaturatedPressureSI import SaturatedDataFramePressureSI
from ClassesDavi.SI.SuperHeatedSI import SuperHeatedDataFrameSI
from ClassesDavi.SI.ChangeSuperHeatedSI import ChangeSuperHeatedPressureSI
from ClassesDavi.SI.CompressedSI import CompressedDataFrameSI
from ClassesDavi.SI.ChangeCompressedSI import ChangeCompressedPressureSI
from ClassesDavi.English.SaturatedTemperatureEnglish import SaturatedDataFrameTemperatureEnglish
from ClassesDavi.English.SaturatedPressureEnglish import SaturatedDataFramePressureEnglish
from ClassesDavi.English.SuperHeatedEnglish import SuperHeatedDataFrameEnglish
from ClassesDavi.English.ChangeSuperHeatedEnglish import ChangeSuperHeatedPressureEnglish
from ClassesDavi.English.CompressedEnglish import CompressedDataFrameEnglish
from ClassesDavi.English.ChangeCompressedEnglish import ChangeCompressedPressureEnglish

pd.set_option('display.max_rows', None)

while True:
    print('\033[0;33mSELECIONE A LETRA DA OPCAO CORRESPONDENTE AO SISTEMA DE UNIDADES A SER UTILIZADO:\033[m\n'
          'A -> SISTEMA INTERNACIONAL DE UNIDADES (SI)\n'
          'B -> SISTEMA INGLES OU IMPERIAL\n'
          'C -> SAIR DO PROGRAMA\n')
    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
    if option not in ['A', 'B', 'C']:
        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
        continue
    elif option == 'C':
        break
    elif option == 'A':
        print('\033[0;36mSISTEMA DE UNIDADES ESCOLHIDO: SI\033[m')
        while True:
            print('\033[0;33mSELECIONE A LETRA DA OPCAO CORRESPONDENTE AO FLUIDO DE TRABALHO DESEJADO:\033[m\n'
                  'A -> AGUA\n'
                  'B -> R22\n'
                  'C -> R134a\n'
                  'D -> AMONIA\n'
                  'E -> PROPANO\n'
                  'F -> VOLTAR AO MENU ANTERIOR\n')
            option = str(input('\033[0;32mOPCAO DE FLUIDO:\033[m')).strip().upper()
            if option not in ['A', 'B', 'C', 'D', 'E', 'F']:
                print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                continue
            elif option == 'F':
                break
            elif option == 'A':
                while True:
                    chosen_fluid = 'AGUA'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: AGUA\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> AGUA SATURADA (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> AGUA SATURADA (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> AGUA SUPERAQUECIDA\n'
                          f'D -> AGUA COMPRIMIDA\n'
                          f'E -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D', 'E']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'E':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureSI(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureSI(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM BAR:\033[m'))
                                pressureList = [0.06, 0.35, 0.7, 1.0, 1.5, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0,
                                                30.0, 40.0, 60.0, 80.0, 100.0,
                                                120.0, 140.0, 160.0, 180.0, 200.0, 240.0, 280.0, 320.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameSI(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureSI(chosen_fluid, pressureList[r - 1],
                                                                            option,
                                                                            pressureList[r]).interpolDataFrame()
                                            else:
                                                continue
                    elif option == 'D':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM BAR:\033[m'))
                                pressureList = [25.0, 50.0, 75.0, 100.0, 150.0, 200.0, 250.0, 300.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    CompressedDataFrameSI(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeCompressedPressureSI(chosen_fluid, pressureList[r - 1],
                                                                           option,
                                                                           pressureList[r]).interpolDataFrame()
                                            else:
                                                continue
                        continue
            elif option == 'B':
                while True:
                    chosen_fluid = 'R22'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: R22\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> R22 SATURADO (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> R22 SATURADO (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> R22 SUPERAQUECIDO\n'
                          f'D -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'D':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureSI(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureSI(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM BAR:\033[m'))
                                pressureList = [0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5,
                                                6.0,
                                                7.0, 8.0,
                                                9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameSI(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureSI(chosen_fluid, pressureList[r - 1],
                                                                            option,
                                                                            pressureList[r]).interpolDataFrame()
                                            else:
                                                continue
            elif option == 'C':
                while True:
                    chosen_fluid = 'R134a'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: R134a\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> R134a SATURADO (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> R134a SATURADO (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> R134a SUPERAQUECIDO\n'
                          f'D -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'D':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureSI(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureSI(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM BAR:\033[m'))
                                pressureList = [0.6, 1.0, 1.4, 1.8, 2.0, 2.4, 2.8, 3.2, 4.0, 5.0, 6.0, 7.0, 8.0,
                                                9.0, 10.0, 12.0, 14.0, 16.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameSI(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureSI(chosen_fluid, pressureList[r - 1],
                                                                            option,
                                                                            pressureList[r]).interpolDataFrame()
                                            else:
                                                continue

            elif option == 'D':
                while True:
                    chosen_fluid = 'AMONIA'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: AMONIA\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> AMONIA SATURADA (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> AMONIA SATURADA (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> AMONIA SUPERAQUECIDA\n'
                          f'D -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'D':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureSI(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureSI(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM BAR:\033[m'))
                                pressureList = [0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0,
                                                5.5, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameSI(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureSI(chosen_fluid, pressureList[r - 1],
                                                                            option,
                                                                            pressureList[r]).interpolDataFrame()
                                            else:
                                                continue
            elif option == 'E':
                while True:
                    chosen_fluid = 'PROPANO'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: PROPANO\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> PROPANO SATURADO (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> PROPANO SATURADO (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> PROPANO SUPERAQUECIDO\n'
                          f'D -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'D':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureSI(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureSI(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM BAR:\033[m'))
                                pressureList = [0.05, 0.1, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,
                                                10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 30.0,
                                                35.0,
                                                40.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameSI(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureSI(chosen_fluid, pressureList[r - 1],
                                                                            option,
                                                                            pressureList[r]).interpolDataFrame()
                                            else:
                                                continue
    else:
        print('\033[0;36mSISTEMA DE UNIDADES ESCOLHIDO: INGLES OU IMPERIAL\033[m')
        while True:
            print('\033[0;33mSELECIONE A LETRA DA OPCAO CORRESPONDENTE AO FLUIDO DE TRABALHO DESEJADO:\033[m\n'
                  'A -> AGUA\n'
                  'B -> R22\n'
                  'C -> R134a\n'
                  'D -> AMONIA\n'
                  'E -> PROPANO\n'
                  'F -> VOLTAR AO MENU ANTERIOR\n')
            option = str(input('\033[0;32mOPCAO DE FLUIDO:\033[m')).strip().upper()
            if option not in ['A', 'B', 'C', 'D', 'E', 'F']:
                print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                continue
            elif option == 'F':
                break
            elif option == 'A':
                while True:
                    chosen_fluid = 'AGUA'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: AGUA\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> AGUA SATURADA (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> AGUA SATURADA (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> AGUA SUPERAQUECIDA\n'
                          f'D -> AGUA COMPRIMIDA\n'
                          f'E -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D', 'E']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'E':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM PSI:\033[m'))
                                pressureList = [1.0, 5.0, 10.0, 14.7, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0,
                                                140.0,
                                                160.0, 180.0, 200.0, 250.0, 300.0, 350.0, 400.0, 450.0, 500.0,
                                                600.0, 700.0, 800.0, 900.0, 1000.0, 1200.0, 1400.0, 1600.0,
                                                1800.0, 2000.0, 2500.0, 3000.0, 3500.0, 4000.0, 4400.0, 4800.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameEnglish(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureEnglish(chosen_fluid,
                                                                                 pressureList[r - 1],
                                                                                 option,
                                                                                 pressureList[
                                                                                     r]).interpolDataFrame()
                                            else:
                                                continue
                    elif option == 'D':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM PSI:\033[m'))
                                pressureList = [500.0, 1000.0, 1500.0, 2000.0, 3000.0, 4000.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    CompressedDataFrameEnglish(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeCompressedPressureEnglish(chosen_fluid,
                                                                                pressureList[r - 1],
                                                                                option,
                                                                                pressureList[
                                                                                    r]).interpolDataFrame()
                                            else:
                                                continue
                        continue
            elif option == 'B':
                while True:
                    chosen_fluid = 'R22'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: R22\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> R22 SATURADO (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> R22 SATURADO (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> R22 SUPERAQUECIDO\n'
                          f'D -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'D':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM PSI:\033[m'))
                                pressureList = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0,
                                                80.0, 90.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 225.0,
                                                250.0, 275.0, 300.0, 325.0, 350.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameEnglish(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureEnglish(chosen_fluid,
                                                                                 pressureList[r - 1],
                                                                                 option,
                                                                                 pressureList[
                                                                                     r]).interpolDataFrame()
                                            else:
                                                continue

            elif option == 'C':
                while True:
                    chosen_fluid = 'R134a'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: R134a\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> R134a SATURADO (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> R134a SATURADO (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> R134a SUPERAQUECIDO\n'
                          f'D -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'D':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM PSI:\033[m'))
                                pressureList = [10.0, 15.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0,
                                                100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 300.0, 400.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameEnglish(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureEnglish(chosen_fluid,
                                                                                 pressureList[r - 1],
                                                                                 option,
                                                                                 pressureList[
                                                                                     r]).interpolDataFrame()
                                            else:
                                                continue
            elif option == 'D':
                while True:
                    chosen_fluid = 'AMONIA'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: AMONIA\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> AMONIA SATURADA (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> AMONIA SATURADA (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> AMONIA SUPERAQUECIDA\n'
                          f'D -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'D':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM PSI:\033[m'))
                                pressureList = [6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 30.0, 40.0, 50.0,
                                                60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0,
                                                150.0,
                                                200.0, 250.0, 300.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameEnglish(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureEnglish(chosen_fluid,
                                                                                 pressureList[r - 1],
                                                                                 option,
                                                                                 pressureList[
                                                                                     r]).interpolDataFrame()
                                            else:
                                                continue
            elif option == 'E':
                while True:
                    chosen_fluid = 'PROPAN'
                    print(f'\n\033[0;36mFLUIDO SELECIONADO: PROPANO\033[m\n')
                    print(f'\033[0;33mSELECIONE A TABELA DESEJADA:\033[m\n'
                          f'A -> PROPANO SATURADO (LIQUIDO-VAPOR): TABELA DE TEMPERATURA\n'
                          f'B -> PROPANO SATURADO (LIQUIDO-VAPOR): TABELA DE PRESSAO\n'
                          f'C -> PROPANO SUPERAQUECIDO\n'
                          f'D -> VOLTAR AO MENU ANTERIOR\n')
                    option = str(input('\033[0;32mOPCAO ESCOLHIDA:\033[m')).strip().upper()
                    if option not in ['A', 'B', 'C', 'D']:
                        print('\n\033[0;31mENTRADA INVALIDA!\033[m\n')
                        continue
                    elif option == 'D':
                        break
                    elif option == 'A':
                        SaturatedDataFrameTemperatureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'B':
                        SaturatedDataFramePressureEnglish(chosen_fluid).research()
                        continue
                    elif option == 'C':
                        while True:
                            try:
                                print('\033[0;33mDIGITE ALGUMA LETRA PARA PARA VOLTAR AO MENU ANTERIOR\033[m')
                                option = float(input('\033[0;33mDIGITE A PRESSAO DESEJADA EM PSI:\033[m'))
                                pressureList = [0.75, 1.5, 5.0, 10.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0,
                                                140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 280.0, 320.0,
                                                360.0, 400.0, 450.0, 500.0, 600.0]
                            except Exception as error:
                                if type(error) == bool:
                                    continue
                                break
                            else:
                                if (option < pressureList[0]) or (option > pressureList[-1]):
                                    print('\033[0;31mNUMERO FORA DA TABELA\033[m')
                                    continue
                                elif option in pressureList:
                                    SuperHeatedDataFrameEnglish(chosen_fluid, option).research()
                                else:
                                    for r, c in enumerate(pressureList):
                                        if r > 0:
                                            if pressureList[r - 1] < option < pressureList[r]:
                                                ChangeSuperHeatedPressureEnglish(chosen_fluid,
                                                                                 pressureList[r - 1],
                                                                                 option,
                                                                                 pressureList[
                                                                                     r]).interpolDataFrame()
                                            else:
                                                continue
