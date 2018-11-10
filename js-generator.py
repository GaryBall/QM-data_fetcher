import pandas as pd
import xlrd


def convert1():
    df1 = pd.read_excel('MC_by_state.xlsx', sheet_name='sheet1')
    moreThan035 =df1[df1.o_rate>0.35]
    N_list = []
    str = '''
        regions:[
        
        '''
    for i in range(0,len(moreThan035)):
        N_list.append(moreThan035.iloc[i]['state'])
        str +='''{
            name:'%s',
            itemStyle: {areaColor: '#228fbd' }
        },
        
        '''%moreThan035.iloc[i]['state']

    moreThan030 = df1[(df1.o_rate > 0.30)&(df1.o_rate<=0.35)]
    for i in range(0, len(moreThan030)):
        N_list.append(moreThan030.iloc[i]['state'])
        str += '''{
            name:'%s',
            itemStyle: {areaColor: '#33a3dc' }
        },

        ''' % moreThan030.iloc[i]['state']


    moreThan025 = df1[(df1.o_rate > 0.25) & (df1.o_rate <= 0.30)]
    for i in range(0, len(moreThan025)):
        N_list.append(moreThan025.iloc[i]['state'])
        str += '''{
                name:'%s',
                itemStyle: {areaColor: '#7bbfea' }
            },

            ''' % moreThan025.iloc[i]['state']


    moreThan020 = df1[(df1.o_rate > 0.20) & (df1.o_rate <= 0.25)]
    for i in range(0, len(moreThan020)):
        N_list.append(moreThan020.iloc[i]['state'])
        str += '''{
                name:'%s',
                itemStyle: {areaColor: '#90d7ec' }
            },

            ''' % moreThan020.iloc[i]['state']


    lessThan020 = df1[(df1.o_rate < 0.20)]
    for i in range(0, len(lessThan020)):
        N_list.append(lessThan020.iloc[i]['state'])
        str += '''{
                name:'%s', 
                itemStyle: {areaColor: '#afdfe4' }
            },

            ''' % lessThan020.iloc[i]['state']
    str+=''']'''
    print(str)

    print('end')


def convert2():
    df2 = pd.read_excel('MC_by_state.xlsx', sheet_name='sheet1')
    str ='''['''
    for i in range(0, len(df2)):
        str += '''{
            name: "%s",
            value: %.2f
        
        },
        '''%(df2.iloc[i]['state'],df2.iloc[i]['m_per_p']*20)
    str +=']'
    print(str)


def convert3():
    str = ''''''
    df3 = pd.read_excel('MC_by_state.xlsx', sheet_name='sheet1')
    for i in range(0,len(df3)):
        str +='''
        "%s": [%.2f,%.2f], 
        '''%(df3.iloc[i]['state'], df3.iloc[i]['S'], df3.iloc[i]['N'])
    print(str)


def main():
    #convert1()
    convert2()
    #convert3()




if __name__ == "__main__":
    main()
