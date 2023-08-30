import pandas as pd
import plotly.express as px

file_path = "Heat_map.xlsx"
df = pd.read_excel(file_path)

fig = px.treemap(df, path=['Area'], values='Existing Team Members Proficient with this area',
                 color='Average TeamExperties(1-5)', color_discrete_map={'Dark Green': 'rgb(88, 175, 78)',
                                                                         'One level below dark green': 'rgb(157, 209, 145)',
                                                                         'One level Above Light green': 'rgb(191, 225, 182)',
                                                                         'Two level above Light green': "rgb(180, 255, 153)",
                                                                         'White': 'rgb(255, 255, 255)',
                                                                         'Light Green': "rgb(144, 238, 144)",
                                                                         'Two level below dark green': 'rgb(134, 230, 132)'})

fig.show()
