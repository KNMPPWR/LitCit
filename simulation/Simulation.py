import numpy as np
from typing import List

from models.TissueModel import TissueModel
from models.ROIModel import ROIModel
from models.LaserModel import LaserModel


class Simulation(object):
    def __init__(self, tissue: TissueModel, roi: ROIModel, lasers: List[LaserModel],
                 time_interval: np.float64, total_time: np.float64):
        # input data
        self.tissue = tissue
        self.roi = roi
        self.lasers = lasers

        self.time_interval = time_interval
        self.total_time = total_time
        self.total_steps = int(total_time / time_interval)
        self.current_step = 0

        # output data
        self.current_temperature_array_shape = (
            roi.no_of_voxels_in_x_direction, roi.no_of_voxels_in_y_direction, roi.no_of_voxels_in_z_direction)
        self.current_temperature = np.zeros(self.current_temperature_array_shape, dtype=np.float64)

        self.max_temperature_over_time = np.zeros(self.total_steps, dtype=np.float64)

    def next_step(self):
        if self.current_step == self.total_steps:
            return

        # update simulation
        self.current_temperature = np.random.rand(*self.current_temperature_array_shape)
        self.max_temperature_over_time[self.current_step] = np.max(self.current_temperature)

        self.current_step += 1