from data_cleaning import data_cleaning
import plotly.express as px
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
import io
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def data_vis():
    data = data_cleaning()

    column=list(data.columns)
    column_to_remove = ["dental caries", "hearing(left)", "hearing(right)", "Urine protein", "LDL", "waist(cm)"]
    for col_to_remove in column_to_remove:
        column.remove(col_to_remove)

    print("columns---------------------", column)
    #
    columns_to_remove_outliers = ['age', 'ALT', 'AST', 'Cholesterol', 'eyesight(left)', 'eyesight(right)', 
                                  'fasting blood sugar', 'Gtp', 'HDL', 'height(cm)', 'hemoglobin', 'relaxation',
                                  'serum creatinine', "triglyceride", "systolic"]
    #outliers removal
    for col in columns_to_remove_outliers:
        q1 = data[col].quantile(0.25)
        q3 = data[col].quantile(0.75)
        iqr = q3 - q1
        upper_limit = q3 + (1.5 * iqr)
        lower_limit = q1 - (1.5 * iqr)

        # Apply the filtering conditions to the original DataFrame
        data = data.loc[(data[col] < upper_limit) & (data[col] > lower_limit)]


    #pie chart
    data['smoking'].replace({0: 'not smoking', 1: 'smoking'}, inplace=True)
    top_products = data['smoking'].value_counts().head(10).index.tolist()
    filtered_df = data[data['smoking'].isin(top_products)]
    product_counts = filtered_df['smoking'].value_counts()
    fig = go.Figure(data=[go.Pie(labels=product_counts.index, values=product_counts.values)])
    fig.update_layout(
        template='plotly_dark',
        title='Percentage of smoking and non_smoking users.'
    )
    fig.write_image("pie_chart.jpg")

    grouped_data = data.groupby(['age', 'smoking']).size().unstack(fill_value=0).reset_index()

    # Rename columns for easier plotting
    grouped_data.columns = ['age', 'Non-Smoking', 'Smoking']

    # Create the plot
    fig = go.Figure()

    # Add bars for Non-Smoking
    fig.add_trace(go.Bar(
        x=grouped_data['age'],
        y=grouped_data['Non-Smoking'],
        name='Non-Smoking'
    ))

    # Add bars for Smoking
    fig.add_trace(go.Bar(
        x=grouped_data['age'],
        y=grouped_data['Smoking'],
        name='Smoking'
    ))

    # Update layout to use 'plotly_dark' template
    fig.update_layout(
        barmode='stack',
        template='plotly_dark',
        title='Number of Persons by Age and Smoking Status',
        xaxis=dict(title='Age'),
        yaxis=dict(title='Number of Persons'),
        legend_title='Smoking Status'
    )

    # Save the plot as a jpg file
    fig.write_image('smoking status by age.jpg')

    #box plot
    for i in column:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"{i}_box.jpg")

    #correlaton matrx
    columns_to_remove = ["smoking"]
    df=data.drop(columns=columns_to_remove,axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark', height=1500, width=1500)
    # fig.show()
    fig.write_image("Correlaton_Matrix.jpg")

    print("-=-------------", data['age'].value_counts())

    return data

data_vis()