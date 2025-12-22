from biomes import BIOMES
import numpy as np
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

def create_pnoise(map_size):
  """
  Generate a "smoother" noise layout by using differing octave levels.

  """
  basic_noise = PerlinNoise(octaves=2)
  moderate_noise = PerlinNoise(octaves=4)
  heavy_noise = PerlinNoise(octaves=8)
  extreme_noise = PerlinNoise(octaves=16)
  
  final_noise = []

  for i in range(map_size):
  # Add noise (weighted by number of octaves, or how "noisy" it is) to a list
  # that gets the terrain applied to a color map
    row = []
    for j in range(map_size):
      noise_val = basic_noise([i/map_size, j/map_size])
      noise_val += 0.5 * moderate_noise([i/map_size, j/map_size])
      noise_val += 0.25 * heavy_noise([i/map_size, j/map_size])
      #noise_val += 0.125 * extreme_noise([i/map_size, j/map_size])
      
      row.append(noise_val)
    final_noise.append(row)
  return final_noise

def generate(map_size, biome="tundra"):
  
  # different landmarks that are being generated.
  # eventually this will be switched depending on the biome type
  landmarks = BIOMES[biome]

  # generate random values according to perlin noise
  #noise = create_pnoise()
  #terrain = [[noise([i/map_size, j/map_size]) for j in range(map_size)] for i in range(map_size)]
  terrain = create_pnoise(map_size)

  cmap = plt.cm.colors.LinearSegmentedColormap.from_list(
                                              "terrain_map", landmarks)
  return (terrain, cmap)
