import numpy as np
import matplotlib.pyplot as plt
from generation import generate


if __name__ == "__main__":
  # Eventually needs to be turned into a parameter
  map_size = 50

  plot, terrain = generate(map_size)

  plt.imshow(plot, cmap=terrain, origin="upper")
  plt.colorbar()
  plt.title("Procedurally Generated Terrain Map")
  plt.show()
