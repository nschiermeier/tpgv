import numpy as np
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

def create_pnoise(map_size):
  basic_noise = PerlinNoise(octaves=2)
  moderate_noise = PerlinNoise(octaves=4)
  heavy_noise = PerlinNoise(octaves=8)
  extreme_noise = PerlinNoise(octaves=16)
  
  final_noise = []

  for i in range(map_size):
    row = []
    for j in range(map_size):
      noise_val = basic_noise([i/map_size, j/map_size])
      noise_val += 0.5 * moderate_noise([i/map_size, j/map_size])
      noise_val += 0.25 * heavy_noise([i/map_size, j/map_size])
      noise_val += 0.125 * extreme_noise([i/map_size, j/map_size])
      
      row.append(noise_val)
    final_noise.append(row)
  return final_noise

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
  #noise = create_pnoise()
  #terrain = [[noise([i/map_size, j/map_size]) for j in range(map_size)] for i in range(map_size)]
  terrain = create_pnoise(map_size)

  cmap = plt.cm.colors.LinearSegmentedColormap.from_list(
                                              "terrain_map", landmarks)
  return (terrain, cmap)
