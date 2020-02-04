""""
This file only contains python code, no C is to be found here.
"""

import numpy as np

try:
    from .helper import log
    from .sdk import WfsLib, WfsSDK, WFSError
except:
    from helper import log
    from sdk import WfsLib, WfsSDK, WfsError


class WFSCamera(object):
    """
    This class represents a higher level pythonic way of interaction with the WFS
    """

    def __init__(self, sdk, default_configuration={}):
        """
        This function initializes a camera with a given sdk
        """
        self._sdk = sdk
        self._default_configuration = default_configuration
        self._configuration = None

    def close(self):
        """
        This function closes the camera connection
        """
        self._sdk.close()

    def set_feature(self, feature, kwargs):
        """
        This functions calls a set_ methos in WfsSDK with kwargs
        """
        return getattr(self._sdk, f"set_{feature}")(**kwargs)

    @property
    def default_configuration(self):
        """
        This function return the default configuration
        """
        return self._default_configuration

    @property
    def configuration(self):
        """
        This function return the current configuration
        """
        return self._configuration

    def configure(self, configuration=None):
        """
        This functions configures the sensor via a provided dict, else a default is used
        """
        self._configuration = self._default_configuration if configuration is None else configuration
        for feature in self.configuration:
            # only execute a call if it is really a feature
            if hasattr(self._sdk, f"set_{feature}"):
                self.set_feature(feature, self.configuration[feature])

    def acquire_wavefront(self, limit_to_pupil=True):
        """
        This function gets one wavefront from the sensor
        """
        # check if the device has been already initiated
        if self.configuration is None:
            self.configure()
        # necessaray steps to get one wavefront
        self._sdk.take_spot_field_image_auto_expos()
        self._sdk.calc_spot()
        self._sdk.calc_deviations()
        return sdk.calc_wavefront(limit_to_pupil=limit_to_pupil)

    def acquire_wavefront_full(self):
        """
        This function gets one wavefront from the sensor which is not cut off at the pupil
        """
        return self.acquire_wavefront(limit_to_pupil=False)


if __name__ == "__main__":
    import ctypes as ct
    import sys
    import matplotlib.pyplot as plt
    dll = ct.windll.WFS_32
    # list devices
    lib = WfsLib(dll)
    # get handle
    sdk = lib.open(list_index=0)
    camera = WFSCamera(sdk)
    conf = {
        "mla": {"mla_index": 0},
        "resolution": {"cam_resol_index": 2},
        "reference_plane": {"internal": True},
        "pupil": {"center": [0, 0], "diameter": [3, 3]}
        }
    try:
        camera.configure(conf)
        result = camera.acquire_wavefront()
        plt.imshow(result)
        plt.colorbar()
        plt.show()
    except Exception as e:
        print(e)
    finally:
        camera.close()
