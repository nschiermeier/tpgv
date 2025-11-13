import numpy as np
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

def create_pnoise():
  noise = PerlinNoise(octaves=4)
  # Can eventually stack noise
  
  return noise

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


  # generate random values according to perlin noise
  noise = create_pnoise()
  terrain = [[noise([i/map_size, j/map_size]) for j in range(map_size)] for i in range(map_size)]

  cmap = plt.cm.colors.LinearSegmentedColormap.from_list(
                                              "terrain_map", landmarks)
  return (terrain, cmap)
