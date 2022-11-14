import visnetwork as vis
import matplotlib.pyplot as plt

# Run EPANET2.0 Simulation and store results
model = vis.VisnetModel(r"Networks/CTown.inp")  

# Define figure to be drawn to
fig, ax = plt.subplots(figsize=(12, 12))

# Disables frame around figure
ax.set_frame_on(False)

#Get mean pressure at each node
mean, elmnt_list = model.get_parameter("node",parameter="pressure",value="mean")
#Get standard deviation at  each node
stddev, elmnt_list = model.get_parameter("node",parameter="pressure",value="stddev")
#Bin standard deviation values
binnedParameter, interval_names = model.bin_parameter(stddev, elmnt_list, 5)
#Set bin_sizes and create node_sizes array
interval_sizes = [100, 200, 300, 400]
node_sizes = [None]*len(elmnt_list)
#Set node_sizes according to bin_sizes
for interval_name, size in zip(interval_names, interval_sizes):
    for element in binnedParameter[interval_name]:
        node_sizes[elmnt_list.index(element)]=size
#Plot continuous mean data and pass custom node_sizes
model.plot_unique_data(
    ax,parameter="custom_data",
    parameter_type="node",data_type="continuous",
    custom_data_values=[elmnt_list,mean],
    color_bar_title="Mean Pressure (m)",cmap="gist_heat_r",
    node_size=node_sizes,
    element_size_intervals=4,
    element_size_legend_title="Standard Deviation (m)",
    element_size_legend_loc="lower left",
    element_size_legend_labels=interval_names,
)
plt.show()