from graphviz import Digraph

dot = Digraph('UseCaseDiagram', format='png')

# Define actors
dot.node('BA', 'Business Analyst', shape='actor')
dot.node('MGR', 'Manager/Executive', shape='actor')
dot.node('SYS', 'AI Model', shape='actor')
dot.node('DS', 'Data Source', shape='actor')

# Define use cases
use_cases = {
    "U1": "Upload Business Data",
    "U2": "Generate Forecast",
    "U3": "View Insights & Reports",
    "U4": "Adjust Forecast Parameters",
    "U5": "Export Reports",
    "U6": "Compare Historical vs. Predicted Data"
}

for key, value in use_cases.items():
    dot.node(key, value, shape='ellipse')

# Connect actors to use cases
dot.edge('BA', 'U1')
dot.edge('BA', 'U2')
dot.edge('BA', 'U3')
dot.edge('BA', 'U4')
dot.edge('BA', 'U5')
dot.edge('BA', 'U6')

dot.edge('MGR', 'U2')
dot.edge('MGR', 'U3')
dot.edge('MGR', 'U5')

dot.edge('SYS', 'U2')
dot.edge('SYS', 'U6')

dot.edge('DS', 'U1')

# Render the diagram
diagram_path = "usecase.png"
dot.render(diagram_path, format="png", cleanup=True)

# Provide the file path
# diagram_path
