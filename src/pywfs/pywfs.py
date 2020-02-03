""""

"""

from ctypes import c_uint8, c_int16, c_int32, c_double, c_ulong, c_float, c_bool, c_char, c_char_p, create_string_buffer, byref, POINTER
import numpy as np

try:
    from .helper import log
except:
    from helper import log


# defining names according to the manual
ViStatus = c_int32
ViBoolean = c_bool
ViSession = c_ulong
ViUInt8 = c_uint8
ViInt16 = c_int16
ViInt32 = c_int32
ViReal32 = c_float
ViReal64 = c_double
ViChar256 = c_char * 256
ViChar512 = c_char * 512
# ViChar256 = lambda: create_string_buffer("", 256)
# ViChar512 = lambda: create_string_buffer("", 512)
ViRsrc = ViChar256

# VI_NULL = lambda: None
VI_NULL = lambda: c_ulong()


class WFSError(Exception):
    pass


class WFSLib(object):
    """
    This class provides a Python wrapper for the bare C functions
    """

    def __init__(self, dll):
        # general methods for WFS library
        dll.WFS_init.restype = ViStatus
        dll.WFS_init.argtypes = [ViRsrc, ViBoolean, ViBoolean, POINTER(ViSession)]

        dll.WFS_close.restype = ViStatus
        dll.WFS_close.argtypes = [ViSession]
        
        # configuration functions
        dll.WFS_GetInstrumentInfo.restype = ViStatus
        dll.WFS_GetInstrumentInfo.argtypes = [ViSession, ViChar256, ViChar256, ViChar256, ViChar256]

        dll.WFS_ConfigureCam.restype = ViStatus
        dll.WFS_ConfigureCam.argtypes = [ViSession, ViInt32, ViInt32, POINTER(ViInt32), POINTER(ViInt32)]

        dll.WFS_SetHighspeedMode.restype = ViStatus
        dll.WFS_SetHighspeedMode.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ViInt32]

        dll.WFS_GetHighspeedWindows.restype = ViStatus
        dll.WFS_GetHighspeedWindows.argtypes = [POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32), ViInt32, ViInt32]

        dll.WFS_CheckHighspeedCentroids.restype = ViStatus
        dll.WFS_CheckHighspeedCentroids.argtypes = [ViSession]

        dll.WFS_GetExposureTimeRange.restype = ViStatus
        dll.WFS_GetExposureTimeRange.argtypes = [ViSession, POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64)]

        dll.WFS_SetExposureTime.restype = ViStatus
        dll.WFS_SetExposureTime.argtypes = [ViSession, ViReal64, POINTER(ViReal64)]

        dll.WFS_GetExposureTime.restype = ViStatus
        dll.WFS_GetExposureTime.argtypes = [ViSession, POINTER(ViReal64)]

        dll.WFS_GetMasterGainRange.restype = ViStatus
        dll.WFS_GetMasterGainRange.argtypes = [ViSession, POINTER(ViReal64), POINTER(ViReal64)]

        dll.WFS_SetMasterGain.restype = ViStatus
        dll.WFS_SetMasterGain.argtypes = [ViSession, ViReal64, POINTER(ViReal64)]

        dll.WFS_GetMasterGain.restype = ViStatus
        dll.WFS_GetMasterGain.argtypes = [ViSession, POINTER(ViReal64)]

        dll.WFS_SetBlackLevelOffset.restype = ViStatus
        dll.WFS_SetBlackLevelOffset.argtypes = [ViSession, ViInt32]

        dll.WFS_GetBlackLevelOffset.restype = ViStatus
        dll.WFS_GetBlackLevelOffset.argtypes = [ViSession, POINTER(ViInt32)]

        dll.WFS_SetTriggerMode.restype = ViStatus
        dll.WFS_SetTriggerMode.argtypes = [ViSession, ViInt32]

        dll.WFS_GetTriggerMode.restype = ViStatus
        dll.WFS_GetTriggerMode.argtypes = [ViSession, POINTER(ViInt32)]

        # dll.WFS_SetTriggerDelayRange.restype = ViStatus
        # dll.WFS_SetTriggerDelayRange.argtypes = [ViSession, POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32)]

        dll.WFS_GetMlaCount.restype = ViStatus
        dll.WFS_GetMlaCount.argtypes = [ViSession, POINTER(ViInt32)]

        dll.WFS_GetMlaData.restype = ViStatus
        dll.WFS_GetMlaData.argtypes = [ViSession, ViInt32, ViChar256, POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64)]
        
        dll.WFS_GetMlaData2.restype = ViStatus
        dll.WFS_GetMlaData2.argtypes = [ViSession, ViInt32, ViChar256, POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64)]

        dll.WFS_SelectMla.restype = ViStatus
        dll.WFS_SelectMla.argtypes = [ViSession, ViInt32]

        # WFS_SetAoi and WFS_SetAoi are undocumented and thus left out

        dll.WFS_SetPupil.restype = ViStatus
        dll.WFS_SetPupil.argtypes = [ViSession, ViReal64, ViReal64, ViReal64, ViReal64]

        dll.WFS_GetPupil.restype = ViStatus
        dll.WFS_GetPupil.argtypes = [ViSession, POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64)]

        dll.WFS_SetReferencePlane.restype = ViStatus
        dll.WFS_SetReferencePlane.argtypes = [ViSession, ViInt32]

        dll.WFS_GetReferencePlane.restype = ViStatus
        dll.WFS_GetReferencePlane.argtypes = [ViSession, POINTER(ViInt32)]

        # Action/Status Functions
        dll.WFS_GetStatus.restype = ViStatus
        dll.WFS_GetStatus.argtypes = [ViSession, POINTER(ViInt32)]

        # Data Functions
        dll.WFS_TakeSpotfieldImage.restype = ViStatus
        dll.WFS_TakeSpotfieldImage.argtypes = [ViSession]

        dll.WFS_TakeSpotfieldImageAutoExpos.restype = ViStatus
        dll.WFS_TakeSpotfieldImageAutoExpos.argtypes = [ViSession, POINTER(ViReal64), POINTER(ViReal64)]

        # WFS_GetSpotfieldImage left out

        dll.WFS_GetSpotfieldImageCopy.restype = ViStatus
        dll.WFS_GetSpotfieldImageCopy.argtypes = [ViSession, ViUInt8, POINTER(ViInt32), POINTER(ViInt32)]  # ViUInt8[]

        dll.WFS_AverageImage.restype = ViStatus
        dll.WFS_AverageImage.argtypes = [ViSession, ViInt32, POINTER(ViInt32)]

        dll.WFS_AverageImageRolling.restype = ViStatus
        dll.WFS_AverageImageRolling.argtypes = [ViSession, ViInt32, ViInt32]

        dll.WFS_CutImageNoiseFloor.restype = ViStatus
        dll.WFS_CutImageNoiseFloor.argtypes = [ViSession, ViInt32]

        dll.WFS_CalcImageMinMax.restype = ViStatus
        dll.WFS_CalcImageMinMax.argtypes = [ViSession, POINTER(ViInt32), POINTER(ViInt32), POINTER(ViReal64)]

        dll.WFS_CalcMeanRmsNoise.restype = ViStatus
        dll.WFS_CalcMeanRmsNoise.argtypes = [ViSession, POINTER(ViReal64), POINTER(ViReal64)]

        dll.WFS_GetLine.restype = ViStatus
        dll.WFS_GetLine.argtypes = [ViSession, ViInt32, c_float] # float[]

        dll.WFS_GetLineView.restype = ViStatus
        dll.WFS_GetLineView.argtypes = [ViSession, c_float, c_float] # float[]

        dll.WFS_CalcBeamCentroidDia.restype = ViStatus
        dll.WFS_CalcBeamCentroidDia.argtypes = [ViSession, POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64)]

        dll.WFS_CalcSpotsCentrDiaIntens.restype = ViStatus
        dll.WFS_CalcSpotsCentrDiaIntens.argtypes = [ViSession, ViInt32, ViInt32]

        dll.WFS_GetSpotCentroids.restype = ViStatus
        dll.WFS_GetSpotCentroids.argtypes = [ViSession, c_float, c_float] # float[]

        dll.WFS_GetSpotDiameters.restype = ViStatus
        dll.WFS_GetSpotDiameters.argtypes = [ViSession, c_float, c_float] # float[]

        dll.WFS_GetSpotDiaStatistics.restype = ViStatus
        dll.WFS_GetSpotDiaStatistics.argtypes = [ViSession, POINTER(ViInt32), POINTER(ViInt32), POINTER(ViInt32)]

        dll.WFS_GetSpotIntensities.restype = ViStatus
        dll.WFS_GetSpotIntensities.argtypes = [ViSession, c_float] # float[]

        dll.WFS_CalcSpotToReferenceDeviations.restype = ViStatus
        dll.WFS_CalcSpotToReferenceDeviations.argtypes = [ViSession, ViInt32]

        dll.WFS_GetSpotReferencePositions.restype = ViStatus
        dll.WFS_GetSpotReferencePositions.argtypes = [ViSession, c_float, c_float] # float[]

        dll.WFS_GetSpotDeviations.restype = ViStatus
        dll.WFS_GetSpotDeviations.argtypes = [ViSession, c_float, c_float] # float[]

        dll.WFS_ZernikeLsf.restype = ViStatus
        dll.WFS_ZernikeLsf.argtypes = [ViSession, POINTER(ViInt32), c_float, c_float, POINTER(ViReal64)] # float[]

        dll.WFS_CalcFourierOptometric.restype = ViStatus
        dll.WFS_CalcFourierOptometric.argtypes = [ViSession, ViInt32, ViInt32, POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64)]

        dll.WFS_CalcReconstrDeviations.restype = ViStatus
        dll.WFS_CalcReconstrDeviations.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, POINTER(ViReal64), POINTER(ViReal64)] # ViInt32[]

        dll.WFS_CalcWavefront.restype = ViStatus
        # dll.WFS_CalcWavefront.argtypes = [ViSession, ViInt32, ViInt32, c_float] # float[]

        dll.WFS_CalcWavefrontStatistics.restype = ViStatus
        dll.WFS_CalcWavefrontStatistics.argtypes = [ViSession, POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64), POINTER(ViReal64)]

        # Utility Functions
        dll.WFS_self_test.restype = ViStatus
        dll.WFS_self_test.argtypes = [ViSession, ViInt16, c_char_p] # ViChar[]

        dll.WFS_reset.restype = ViStatus
        dll.WFS_reset.argtypes = [ViSession]

        dll.WFS_revision_query.restype = ViStatus
        dll.WFS_revision_query.argtypes = [ViSession, c_char_p, c_char_p] # ViChar[]

        dll.WFS_error_query.restype = ViStatus
        dll.WFS_error_query.argtypes = [ViSession, POINTER(ViInt32), c_char_p] # ViChar[]

        dll.WFS_error_message.restype = ViStatus
        dll.WFS_error_message.argtypes = [ViSession, ViStatus, ViChar256]

        dll.WFS_GetInstrumentListLen.restype = ViStatus
        dll.WFS_GetInstrumentListLen.argtypes = [ViSession, POINTER(ViInt32)]

        dll.WFS_GetInstrumentListInfo.restype = ViStatus
        dll.WFS_GetInstrumentListInfo.argtypes = [ViSession, ViInt32, POINTER(ViInt32), POINTER(ViInt32), ViChar256, ViChar256, ViRsrc] # ViChar[]

        dll.WFS_GetXYScale.restype = ViStatus
        dll.WFS_GetXYScale.argtypes = [ViSession, c_float, c_float] # float[]

        dll.WFS_ConvertWavefrontWaves.restype = ViStatus
        dll.WFS_ConvertWavefrontWaves.argtypes = [ViSession, ViReal64, ViReal32, ViReal32] # ViReal[]

        dll.WFS_Flip2DArray.restype = ViStatus
        dll.WFS_Flip2DArray.argtypes = [ViSession, ViReal32, ViReal32] # ViReal32

        # Calibration Functions
        dll.WFS_SetSpotsToUserReference.restype = ViStatus
        dll.WFS_SetSpotsToUserReference.argtypes = [ViSession]

        dll.WFS_SetCalcSpotsToUserReference.restype = ViStatus
        dll.WFS_SetCalcSpotsToUserReference.argtypes = [ViSession, ViInt32, c_float, c_float] # float[]

        dll.WFS_CreateDefaultUserReference.restype = ViStatus
        dll.WFS_CreateDefaultUserReference.argtypes = [ViSession]

        dll.WFS_SaveUserRefFile.restype = ViStatus
        dll.WFS_SaveUserRefFile.argtypes = [ViSession]

        dll.WFS_LoadUserRefFile.restype = ViStatus
        dll.WFS_LoadUserRefFile.argtypes = [ViSession]

        dll.WFS_DoSphericalRef.restype = ViStatus
        dll.WFS_DoSphericalRef.argtypes = [ViSession]


        self._dll = dll

    @staticmethod
    def result(dev_status):
        """
         This function queries the instrument and returns instrument-specific error information. 
        """
        if dev_status != 0:
            log.error(f"ViStatus code {dev_status} occured")
            # raise WFSError(dev_status)


    def device_count(self):
        """
        This function reads all Wavefront Sensor devices connected to the PC and returns the number of it.
        Use function GetInstrumentListInfo to retrieve information about each WFS instrument.
        """
        count = ViInt32()
        WFSLib.result(self._dll.WFS_GetInstrumentListLen(VI_NULL(), byref(count)))
        log.spam(f"WFS_GetInstrumentListLen: {count.value} connected sensors")
        return count.value

    def device_info(self):
        """
        This function returns information about connected WFS instruments. 
        """
        count = self.device_count()
        sensors = []
        for list_index in range(count):
            device_id = ViInt32()
            in_use = ViInt32()
            instrument_name = ViChar256()
            instrument_sn = ViChar256()
            resource_name = ViRsrc()
            WFSLib.result(self._dll.WFS_GetInstrumentListInfo(VI_NULL(), list_index, byref(device_id), byref(in_use), instrument_name, instrument_sn, resource_name))
            log.info(f"WFS deviceID: {device_id.value}")
            log.info(f"in use: {in_use.value}")
            log.info(f"instrumentName: {instrument_name.value}")
            log.info(f"instrumentSN: {instrument_sn.value}")
            log.info(f"resourceName: {resource_name.value}")
            sensors.append([device_id.value, in_use.value, instrument_name.value, instrument_sn.value, resource_name.value])
        return sensors

    def open(self, list_index=0):
        """
        This function initializes the instrument driver session and performs the following initialization actions:
        (1) Opens a session to the Default Resource Manager resource and a session to the selected device using the Resource Name.
        (2) Performs an identification query on the Instrument.
        (3) Resets the instrument to a known state.
        (4) Sends initialization commands to the instrument.
        (5) Returns an instrument handle.
        """
        log.spam(f"opening sensor with index {list_index}")
        resource_name = ViRsrc()
        id_query = ViBoolean()
        reset_device = ViBoolean()
        handle = ViSession()
        # check if device is already in use
        instrument = self.device_info()[list_index]
        if instrument[1] != 0:
            raise WFSError(f"device is already in use!")
        resource_name.value = instrument[-1]
        WFSLib.result(self._dll.WFS_init(resource_name, id_query, reset_device, byref(handle)))
        log.spam(f"sensor initialized with handle {handle.value}")
        return WFSSensor(handle, self._dll)

    def close(self, handle: ViSession):
        """
        This function closes the instrument driver session.
        Note: The instrument must be reinitialized to use it again. 
        """
        log.spam(f"closing instrument with handle {handle.value}")
        WFSLib.result(self._dll.WFS_close(handle))


class WFSSensor(object):
    """
    This class is a python wrapper for sensor specific function calls (all calls that need a specific handle)
    """

    def __init__(self, handle: ViSession, dll):
        """
        Instances of WFSSensor are created by invoking WFSLib.open()
        """
        self._handle = handle
        self._dll = dll

    def configure(self, cam_resol_index):
        """
        This function configures the WFS instrument's camera resolution and returns the max. number of detectable spots in X and Y direction.
        The result depends on the selected microlens array in function WFS_SelectMla().
        """
        self.pixel_format = ViInt32(0)
        self.cam_resol_index = ViInt32(cam_resol_index)
        self.spots = [ViInt32(), ViInt32()]
        WFSLib.result(self._dll.WFS_ConfigureCam(self._handle, self.pixel_format, self.cam_resol_index, byref(self.spots[0]), byref(self.spots[1])))
        log.spam(f"sensor configured with {self.spots[0].value} x {self.spots[1].value} spots")

    def set_pupil(self, center=[0, 0], diameter=[3, 3]):
        """
        This function defines the pupil in position and size. 
        """
        self.pupil_center = [ViReal64(center[0]), ViReal64(center[1])]
        self.pupil_diameter = [ViReal64(diameter[0]), ViReal64(diameter[1])]
        log.spam(f"configuring pupil")
        WFSLib.result(self._dll.WFS_SetPupil(self._handle, *self.pupil_center, *self.pupil_diameter))

    def take_spot_field_image_auto_expos(self):
        """
        This function tries to find optimal exposure and gain settings and then it receives a spotfield image from the WFS camera into a driver buffer. The reference to this buffer is provided by function GetSpotfieldImage() and an image copy is returned by function GetSpotfieldImageCopy().
        The exposure and gain settings used for this image are returned.
        """
        self.exposure_time_act = ViReal64()
        self.master_gain_act = ViReal64()
        log.spam(f"taking spot field with auto exposure")
        WFSLib.result(self._dll.WFS_TakeSpotfieldImageAutoExpos(self._handle, byref(self.exposure_time_act), byref(self.master_gain_act)))
        log.spam(f"exposure_time_act {self.exposure_time_act.value}")
        log.spam(f"master_gain_act {self.master_gain_act.value}")

    def calc_spot(self, dynamic_noise_cut=True, calculate_diameters=False):
        """
        This function calculates the centroids, diameters (optional) and intensities of all spots generated by the lenslets.
        Data arrays are returned by separate functions:
            GetSpotCentroids
            GetSpotDiameters
            GetSpotIntensities
        """
        self.dynamic_noise_cut = ViInt32(dynamic_noise_cut)
        self.calculate_diameters = ViInt32(calculate_diameters)
        log.spam("calculating spot centroids and diameters")
        WFSLib.result(self._dll.WFS_CalcSpotsCentrDiaIntens(self._handle, self.dynamic_noise_cut, self.calculate_diameters))

    def calc_deviations(self, cancel_spot_wavefront_tilt=True):
        """
        This function calculates reference positions and deviations for all spots depending on the setting ref_idx(internal/user) set by function SetWavefrontReference.
        When option CancelWavefrontTilt is enabled the mean deviation in X and Y direction, which is measured within the pupil, is subtracted from the deviation data arrays.
        Reference positions can be retrieved using function GetSpotReferencePositions and calculated deviations by function GetSpotDeviations. 
        """
        self.cancel_spot_wavefront_tilt = ViInt32(cancel_spot_wavefront_tilt)
        log.spam("calculating spot deviation from reference")
        WFSLib.result(self._dll.WFS_CalcSpotToReferenceDeviations(self._handle, self.cancel_spot_wavefront_tilt))

    def calc_wavefront(self, wavefront_type=0, limit_to_pupil=True, max_spots=[50, 50]):
        """
        This function calculates the wavefront based on the spot deviations.
        max_spots is a bit dirty, will be hopefully removed.
        """
        self.wavefront_type = ViInt32(wavefront_type)
        self.limit_to_pupil = ViInt32(limit_to_pupil)
        array_wavefront = np.zeros(max_spots, dtype = np.float32)
        log.spam(f"calculating wavefront type {self.wavefront_type.value}")
        WFSLib.result(self._dll.WFS_CalcWavefront(self._handle, self.wavefront_type, self.limit_to_pupil, array_wavefront.ctypes.data))
        return array_wavefront[:self.spots[1].value, :self.spots[0].value].copy()
        # return array_wavefront.copy()


# some example code to acquire one wavefront and close the instrument
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import ctypes as ct
    import sys
    dll = ct.windll.WFS_32

    # list devices
    lib = WFSLib(dll)
    print(lib.device_info())
    # sys.exit()
    # get handle
    sensor = lib.open(list_index=0)

    # configuration
    sensor.configure(cam_resol_index=2) # 1024**2 for WFS30
    sensor.set_pupil(center=[0, 0], diameter=[3,3])

    # actual image and wavefront calculation
    sensor.take_spot_field_image_auto_expos()
    sensor.calc_spot()
    sensor.calc_deviations()
    try:
        result = sensor.calc_wavefront(limit_to_pupil=False, max_spots=[100, 100])
        print(result)
        plt.imshow(result)
        plt.show()
    except Exception as e:
        log.critical(f"{e}")
    finally:
        WFSLib(dll).close(sensor._handle)