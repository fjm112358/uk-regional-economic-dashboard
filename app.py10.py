# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:20:51 2026

@author: Dylan
"""
#import libraries
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px 
#open data(already been cleaned)

f_p = "regional_gdp_cleaned.xlsx"


df_gdp = pd.read_excel(f_p, sheet_name="GDP")
df_gdp = df_gdp.melt(
    id_vars=["ITL1 Region", "LA code", "LA name"],
    var_name="Year",
    value_name="GDP"
    )
df_pop = pd.read_excel(f_p, sheet_name="Population")
df_pop = df_pop.melt(
    id_vars=["ITL1 Region", "LA code", "LA name"],
    var_name="Year",
    value_name="Population"
    )
df_gdp_per_head = pd.read_excel(f_p, sheet_name="GDP per Head")
df_gdp_per_head = df_gdp_per_head.melt(
    id_vars=["ITL1 Region", "LA code", "LA name"],
    var_name="Year",
    value_name="GDP Per Head"
    )
df_acc_gdp = pd.read_excel(f_p, sheet_name="Accumulated GDP")
df_acc_gdp = df_acc_gdp.melt(
    id_vars=["ITL1 Region", "LA code", "LA name"],
    var_name="Year",
    value_name="Accumulated GDP"
    )
df_gdp_grwth = pd.read_excel(f_p, sheet_name="GDP Growth")
df_gdp_grwth = df_gdp_grwth.melt(
    id_vars=["ITL1 Region", "LA code", "LA name"],
    var_name="Year",
    value_name="GDP Growth"
    )
#using data from ONS
#creatinglists for dropdowns:
    
regions = [
    "North East",
    "North West",
    "Yorkshire and The Humber",
    "East Midlands",
    "West Midlands",
    "East",
    "London",
    "South East",
    "South West",
    "Wales",
    "Scotland",
    "Northern Ireland",
]  

datasets = [
    "GDP",
    "Population",
    "GDP per head",
    "Accumulated GDP",
    "GDP Growth",
]

fig_gdp = px.histogram(
    df_gdp,
    x = "GDP",
    title ="GDP Over 25 Years",
    )
    
fig_pop = px.histogram(
    df_pop,
    x = "Population",
    title = "Population Over 25 Years",
    )

fig_gdp_per_head = px.histogram(
    df_gdp_per_head,
    x = "GDP Per Head",
    title = "GDP Per Head Over 25 Years",
    )
    
fig_acc_gdp = px.histogram(
    df_acc_gdp,
    x = "Accumulated GDP",
    title = "Accumulated GDP Over 25 Years",
    )
    
fig_gdp_grwth = px.histogram(
    df_gdp_grwth,
    x = "GDP Growth",
    title = "GDP Growth Over 25 Years",
    )
    
app = Dash()

app.layout = [ 
    html.Div(children="UK's Regional Economic Distrobution Dashboard "),
    html.Br(),
#use id for drop down
#creating dropdown

   dcc.Dropdown(
    id="regions",
    options=[
        {"label": region, "value": region}
        for region in regions
    ],
    value="North East",
),
    
    html.Br(),
#creating radio button for data sheets:  

    dcc.RadioItems(
        id = "data sheets",
        options = [
            {"label": "GDP", "value": "gdp"},
            {"label": "Pop", "value": "population"},
            {"label": "GDP Per Head", "value":"gdp per head"},
            {"label":  "Accumulated GDP", "value":"accumulated gdp"},
            {"label": "GDP Growth", "value":"gdp growth"},
        ],
        value = "gdp",
        ),
                                    
dcc.Graph(
    id="primary graph",
    figure=fig_gdp
    ),
]
#need to add the call back for interactiveness 

@app.callback(
    Output("primary graph", "figure"),
    
    Input("regions", "value"),
    Input("data sheets", "value")
)
def update_graph(selected_region, selected_dataset):

    print("REGION:", selected_region)
    print("DATASET:", selected_dataset)

    if selected_dataset == "gdp":
        filtered_data = df_gdp[
            df_gdp["ITL1 Region"] == selected_region
        ]

        fig = px.histogram(
            filtered_data,
            x="GDP",
            title=f"GDP Over 25 Years - {selected_region}"
        )

    elif selected_dataset == "population":
        filtered_data = df_pop[
            df_pop["ITL1 Region"] == selected_region
        ]

        fig = px.histogram(
            filtered_data,
            x="Population",
            title=f"Population Over 25 Years - {selected_region}"
        )

    elif selected_dataset == "gdp per head":
        filtered_data = df_gdp_per_head[
            df_gdp_per_head["ITL1 Region"] == selected_region
        ]

        fig = px.histogram(
            filtered_data,
            x="GDP Per Head",
            title=f"GDP Per Head Over 25 Years - {selected_region}"
        )

    elif selected_dataset == "accumulated gdp":
        filtered_data = df_acc_gdp[
            df_acc_gdp["ITL1 Region"] == selected_region
        ]
        
        fig = px.histogram(
            filtered_data,
            x="Accumulated GDP",
            title=f"Accumulated GDP Over 25 Years - {selected_region}"
        )

    elif selected_dataset == "gdp growth":
        filtered_data = df_gdp_grwth[
            df_gdp_grwth["ITL1 Region"] == selected_region
        ]
        
        fig = px.histogram(
            filtered_data,
            x="GDP Growth",
            title=f"GDP Growth Over 25 Years - {selected_region}"
        )

    return fig


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)







    

    
    
        
    
 

        
    
    

        


        
        
    

        
    
    
    
    
    
    
    









