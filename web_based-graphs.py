from plotly.subplots import make_subplots
import plotly.graph_objects as go

figure = make_subplots(rows = 2, cols = 2, subplot_titles = ("Scatter plot", "Bar chart", "Pie chart", "Histograph"), specs = [[{"type":"xy"},{"type":"xy"}],[{"type":"domain"},{"type":"xy"}]])

#Scatter plot 
sctrplt = go.Scatter(
    x = [1,2,3,4,5], 
    y = [9,10,4,6,8],
    mode = "markers"

)

figure.add_trace(sctrplt, row = 1, col = 1)

#Bar chart
bar_chart = go.Bar(
    x = [11,27,34,0,12],
    y = [1,2,3,4,9]
)
figure.add_trace(bar_chart, row = 1, col = 2)

#Pie chart
pie = go.Pie(
    labels = ["drawing", "reading", "playing an instument(s)", "coding"],
    values = [1, 3, 4, 8]
)
figure.add_trace(pie, row = 2, col = 1)

marks = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75,
         75, 78, 80, 82, 85, 88, 90, 92, 95, 98]
#Histograph
histo = go.Histogram(
    x = marks,
    xbins = dict(start = 40, end = 100, size = 10)

)
figure.add_trace(histo, row = 2, col = 2)

figure.update_layout(title = "Example of Subplots", width = 1000, height = 1000)
figure.write_html("Subplots.html", auto_open = True)

