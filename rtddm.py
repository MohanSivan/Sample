import dash
#import dash_core_components as dcc
#import dash_html_components as html
from dash import dcc,html,dash_table
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime
from tkinter.ttk import Style
import plotly
from dash import dcc,html,dash_table
import plotly.express as px
import numpy as np

#import dash_daq as daqasset
# pip install pyorbital
#from pyorbital.orbital import Orbital
#satellite = Orbital('TERRA')

#Read_Excell file_formet with Add Column Names:
col_names=['Description', 'Machine', 'Readings', 'Datetime']
#df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
meta_tags=[{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, df1]

df = pd.DataFrame(df1)
#df.to_csv(r'F:\RTTDM_Dataexport_dataframe.csv', index=False, header=True)
#df.to_excel(r'F:\RTTDM_Data\.%d%Y%H%.xlsx', index=False)


app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app.server
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('Kh_Logo.png'),
                    style={ "height": "50px"},
                    className = 'title_image'
                    ),
            html.Div([
                html.H6("Real Time Data Disply Monitoring ( RTDDM )", 
                    style={'color': 'Yellow'},
                    className = 'title'),
            ]),
        ], className="logo_title"),
            html.H6(id = 'get_date_time',
                    style = {'color': 'white'},
                    className = 'adjust_date_time'
                )
    ], className = 'title_date_time_container'),
    html.Div([
        dcc.Interval(id = 'update_date_time',
                     interval = 5000,
                     n_intervals = 0),
    ]),
    html.Div([
        dcc.Interval(id = 'update_value',
                     interval = 5000,
                     n_intervals = 0),
     ]),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div(id = 'text_row1'),
                    ], className = 'first_card_column'),
                ], className = 'adjust_first_card'),
                html.Div([
                    html.Div([
                        html.Div(id = 'text_row2'),
                    ], className = 'second_card_column'),
                ], className = 'adjust_second_card'),
                html.Div([
                    html.Div([
                        html.Div(id = 'text_row3'),
                    ], className = 'third_card_column'),
                ], className = 'adjust_third_card'),
                html.Div([
                    html.Div([
                        html.Div(id = 'text_row4'),
                    ], className = 'fourth_card_column'),
                ], className = 'adjust_fourth_card')
        ], className = 'flexbox_container'),
        ], className = 'adjust_margin'),

        html.Div([
           html.Div([
                html.Div([
                    html.Div([
                        html.Div(id = 'text_row5'),
                    ], className = 'fiveth_card_column'),
                ], className = 'adjust_fiveth_card'),
                html.Div([
                    html.Div([
                        html.Div(id = 'text_row6'),
                    ], className = 'sixth_card_column'),
                ], className = 'adjust_sixth_card'),
                html.Div([
                    html.Div([
                        html.Div(id = 'text_row7'),
                    ], className = 'seventh_card_column'),
                ], className = 'adjust_seventh_card'),
                html.Div([
                    html.Div([
                        html.Div(id = 'text_row8'),
                    ], className = 'eigth_card_column'),
                ], className = 'adjust_eigth_card'),
            ], className = 'flexbox_container'),
        ], className = 'adjust_margin'),

    html.Div([
        html.Footer(
            'Note:- This demo is just a sample that shows how to display real time data in python  and above data ',
            className = 'footer_text')
    ], className = 'footer_content')
])



#Update_Excel_Datetime :
@app.callback(Output('get_date_time', 'children'),
              [Input('update_date_time', 'n_intervals')])
def update_data(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        #df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
        df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
        dt_string=str(df1['Datetime'].iloc[-1].strftime("%B %d,%Y %H:%M"))
        df = pd.DataFrame(df1)
        #df.to_csv(r'F:\RTTDM_Dataexport_dataframe.csv', index=False, header=True)
        df.to_excel(r'F:\RTTDM_Data\.%d%Y%H%.xlsx', index=False)  
        df.to_excel(r'https://github.com/MohanSivan/rtddm_excel_file.git')    
        
        
        #print( dt_string)
    return [
        html.Div(dt_string),
    ]


@app.callback(Output('text_row1', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        #df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
        df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
    return [
            html.Div([
                html.Div([
                    html.P('Total Machines',
                        style={
                            'color': 'white',
                            'fontSize': 20},
                        className = 'coin_name')
                ]),
            html.Div([
                html.P(f"{df1.Machine.nunique()}" ,
                        style={

                            'color': 'orange',
                            'fontSize': 20},
                        )
                     ], className = 'coin_price'),
                ], className = 'coin_price_column'),
    ]

@app.callback(Output('text_row2', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        #df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
        df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
        filterkey_F=["F.Actual Outputs"]
        cleardf5=df1[df1.iloc[:,0].isin(filterkey_F)]

    return [
            html.Div([
                html.Div([
                    html.P('Actual Outputs',
                        style={
                            'color': 'white',
                            'fontSize': 20},
                        className = 'Actual_Outputs_Name')
                ]),
            html.Div([
               html.P(f"{((cleardf5.Readings.sum()) / (df1.Machine.nunique()*250)*100):,.2f}" + '%',
                        style={

                            'color': 'orange',
                            'fontSize': 20},
                        )
                     ], className = 'Actual_Outputs'),
                ], className = 'coin_price_column'),
    ]

@app.callback(Output('text_row3', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        #df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
        df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
        filterkey_I=["I.Machine Utilization %"]
        cleardf6=df1[df1.iloc[:,0].isin(filterkey_I)]

    return [
            html.Div([
                html.Div([
                    html.P('Total Utilizations',
                        style={
                            'color': 'white',
                            'fontSize': 20},
                        className = 'Actual_Outputs_Name')
                ]),
            html.Div([
               html.P(f"{((cleardf6.Readings.sum()) / (df1.Machine.nunique())):,.2f}" + '%',
                        style={

                            'color': 'orange',
                            'fontSize': 20},
                        )
                     ], className = 'Actual_Outputs'),
                ], className = 'coin_price_column'),
    ]
    
@app.callback(Output('text_row4', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        #df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
        df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
        filterkey_J=["J.Target Efficiency %"]
        cleardf7=df1[df1.iloc[:,0].isin(filterkey_J)]

    return [
            html.Div([
                html.Div([
                    html.P('Target Efficiency',
                        style={
                            'color': 'white',
                            'fontSize': 20},
                        className = 'Actual_Outputs_Name')
                ]),
            html.Div([
               html.P(f"{((cleardf7.Readings.sum()) / (df1.Machine.nunique())):,.0f}" + '%',
                        style={

                            'color': 'orange',
                            'fontSize': 20},
                        )
                     ], className = 'Actual_Outputs'),
                ], className = 'coin_price_column'),
    ]
    
@app.callback(Output('text_row5', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        #df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
        df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
        filterkey_B=["B.Run Time in Min"]
        cleardf1=df1[df1.iloc[:,0].isin(filterkey_B)]
        #cleardfB=(cleardf1.iloc[0:1000, [2]].sum())
        Total_Sft_Rt = cleardf1.Readings.sum()
        Total_Machine_Counts = df1.Machine.nunique()
        Avg_Toatal_Sft_Rt = ( Total_Sft_Rt / Total_Machine_Counts)

    return [
            html.Div([
                html.Div([
                    html.P('Run Time : '+ str(Avg_Toatal_Sft_Rt),
                        style={
                            'color': 'white',
                            'fontSize': 20},
                        className = 'Actual_Outputs_Name')
                ]),
            html.Div([
               html.P(f"{((cleardf1.Readings.sum()) / (df1.Machine.nunique()*480)*100):,.2f}" + '%',
                        style={

                            'color': 'orange',
                            'fontSize': 20},
                        )
                     ], className = 'Actual_Outputs'),
                ], className = 'coin_price_column'),
    ]

@app.callback(Output('text_row6', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        #df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
        df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
        filterkey_C=["C.Idle Time in Min"]
        cleardf2=df1[df1.iloc[:,0].isin(filterkey_C)]
        Total_Machine_Counts = df1.Machine.nunique()
        Total_Sft_It = cleardf2.Readings.sum()
        Avg_Toatal_Sft_It = ( Total_Sft_It / Total_Machine_Counts)

    return [
            html.Div([
                html.Div([
                    html.P('Idle Time : '+ str(Avg_Toatal_Sft_It),
                        style={
                            'color': 'white',
                            'fontSize': 20},
                        className = 'Actual_Outputs_Name')
                ]),
            html.Div([
               html.P(f"{((cleardf2.Readings.sum()) / (df1.Machine.nunique()*480)*100):,.2f}" + '%',
                        style={

                            'color': 'orange',
                            'fontSize': 20},
                        )
                     ], className = 'Actual_Outputs'),
                ], className = 'coin_price_column'),
    ]
    
@app.callback(Output('text_row7', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        #df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
        df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
        filterkey_D=["D.DeadLock Time in Min"]
        cleardf3=df1[df1.iloc[:,0].isin(filterkey_D)]
        Total_Machine_Counts = df1.Machine.nunique()
        Total_Sft_Dt = cleardf3.Readings.sum()
        Avg_Toatal_Sft_Dt = ( Total_Sft_Dt / Total_Machine_Counts)

    return [
            html.Div([
                html.Div([
                    html.P('DeadLock Time : '+ str(Avg_Toatal_Sft_Dt),
                        style={
                            'color': 'white',
                            'fontSize': 20},
                        className = 'DeadLock_Name')
                ]),
            html.Div([
               html.P(f"{((cleardf3.Readings.sum()) / (df1.Machine.nunique()*480)*100):,.2f}" + '%',
                        style={

                            'color': 'orange',
                            'fontSize': 20},
                        )
                     ], className = 'Actual_Outputs'),
                ], className = 'coin_price_column'),
    ]
    
@app.callback(Output('text_row8', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        #df1 = pd.read_excel(r"\\ebsserver\A&R\RTDDM\RTDataCapture(01).xlsx",names=col_names, header=None)
        df1 = pd.read_excel(r"RTDataCapture(01).xlsx",names=col_names, header=None)
        filterkey_E=["E.Break Down Time in Min"]
        cleardf4=df1[df1.iloc[:,0].isin(filterkey_E)]
        Total_Machine_Counts = df1.Machine.nunique()
        Total_Sft_BDt = cleardf4.Readings.sum()
        Avg_Toatal_Sft_BDt = ( Total_Sft_BDt / Total_Machine_Counts)

    return [
            html.Div([
                html.Div([
                    html.P('Break Down Time : '+ str(Avg_Toatal_Sft_BDt),
                        style={
                            'color': 'white',
                            'fontSize': 20},
                        className = 'Break_Down_Name')
                ]),
            html.Div([
               html.P(f"{((cleardf4.Readings.sum()) / (df1.Machine.nunique()*480)*100):,.2f}" + '%',
                        style={

                            'color': 'orange',
                            'fontSize': 20},
                        )
                     ], className = 'Actual_Outputs'),
                ], className = 'coin_price_column'),
    ]
    
if __name__ == "__main__":
    app.run_server(debug = True,port=10451)
