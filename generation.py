import numpy as np
import matplotlib.pyplot as plt

def generate(map_size, biome="plains"):
  
  # different landmarks that are being generated.
  # eventually this will be switched depending on the biome type
  landmarks = [
    (0.0, "blue"),      # water -- lakes, ponds, etc
    (0.3, "green"),     # grass -- plains, hills, etc
    (0.6, "darkgreen"), # woods -- forrests / brush
    (0.8, "gray"),      # mountains
    (1.0, "white")      # snowcap mountains
  ]


  # generate random values from 0 - 1 to use 
  terrain = np.random.rand(map_size, map_size)

  cmap = plt.cm.colors.LinearSegmentedColormap.from_list(
                                              "terrain_map", landmarks)
  return (terrain, cmap)
