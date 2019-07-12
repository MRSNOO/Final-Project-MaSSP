
import numpy as np


def haze_removal(image):

    dark_image = image.min(axis=2)
    max_of_dark_channel = dark_image.max()
    dark_image = dark_image.astype(np.double)

    t = 1 - 0.69 * (dark_image / max_of_dark_channel)

    t[t < 0.05] = 0.05

    out = image
    
    out[:, :, 0] = (image[:, :, 0] - (1 - t) * max_of_dark_channel) / t
    out[:, :, 1] = (image[:, :, 1] - (1 - t) * max_of_dark_channel) / t
    out[:, :, 2] = (image[:, :, 2] - (1 - t) * max_of_dark_channel) / t

    return out



