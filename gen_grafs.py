# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import plotly
from datetime import timedelta, datetime
import datetime
import plotly.graph_objects as go
from plotly.offline import plot

def create_graf_principal(df,date,primero):
    last_df=df[df['date']==date.strftime("%Y-%m-%d")].sort_values('median')
    median=last_df['median']
    lower_80=(last_df['lower_80']-median)*-1
    upper_80=last_df['upper_80']-median
    provincias=last_df['region']
    
    color = [
        -1 if v < 1 else 1
        for v in median
    ]
    
    colorscale = [[0, 'blue'], [1, 'red']]
    
    fig = go.Figure(data=go.Scatter(
            x=provincias,
            y=median,
            marker = {'color': color,
                  'colorscale': colorscale,
                  'size': 10
                 },
            mode='markers',
            error_y=dict(
                type='data',
                symmetric=False,
                array=upper_80,
                arrayminus=lower_80)))
    fig.update_layout(title="Estimaciones para el "+date.strftime("%Y-%m-%d"),
                      xaxis_title="Provincias",
                      yaxis_title="Rt",
                      template='plotly_white')
    return fig.write_html(r"D:\Users\Georg\Documents\GitHub\covidrd\assets\img\\"+primero+".html")
    
df=pd.read_csv(r'D:\Users\Georg\Documents\GitHub\covid-model\results\resultado_consolidado\result_master.csv')
date=max(df['date'])
date = datetime.datetime.strptime(date, '%Y-%m-%d')
date2=(date.date() - pd.Timedelta(days = 30))
date3=(date.date() - pd.Timedelta(days = 60))

create_graf_principal(df,date,"primero")
create_graf_principal(df,date2,"segundo")
create_graf_principal(df,date3,"tercero")

def create_graf_prov(df,provincia):
    df=df[df['region']==provincia]
    
    fig = go.Figure([
        go.Scatter(
            name='Mediana',
            x=df['date'],
            y=df['median'],
            mode='lines',
            line=dict(color='rgb(31, 119, 180)'),
            showlegend=False
        ),
        go.Scatter(
            name='Banda 80%',
            x=df['date'],
            y=df['upper_80'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ),
        go.Scatter(
            name='Banda 20%',
            x=df['date'],
            y=df['lower_80'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        )
    ])
    fig.update_layout(
        yaxis_title='Rt',
        title="Tasa de Reproducción Efectiva para "+provincia,
        hovermode="x",
        template='plotly_white'
    )
    return fig.write_html(r"D:\Users\Georg\Documents\GitHub\covidrd\assets\img\\"+provincia+".html")

provincias=df['region'].unique()
for i in provincias:
    create_graf_prov(df,i)
