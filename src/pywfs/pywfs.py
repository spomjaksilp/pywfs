""""

"""

from ctypes import c_int32, c_double, c_ulong, c_bool, create_string_buffer, byref, POINTER

from .helper import log


# defining names according to the manual
ViStatus = c_int32
ViBoolean = c_bool
ViSession = c_ulong
ViInt32 = c_int32
ViReal64 = c_double
ViChar256 = lambda: create_string_buffer("", 256)
ViChar512 = lambda: create_string_buffer("", 512)


class WFSError(Exception):
    pass


class WFSLib(object):
    """
    This class provides a Python wrapper for the bare C functions
    """

    def __init__(self, dll):
        """
        #Set the data types compatible with C DLL
        count = ViInt32()
        deviceID  = ViInt32()
        instrumentListIndex  = ViInt32() 
        inUse = ViInt32() 
        instrumentName = ViChar256()
        instrumentSN = ViChar256()
        resourceName = ViChar256()
        IDQuery = ViBoolean()
        resetDevice = ViBoolean()
        instrumentHandle = ViSession()
        pupilCenterXMm = ViReal64()
        pupilCenterYMm = ViReal64()
        pupilDiameterXMm = ViReal64()
        pupilDiameterYMm = ViReal64()
        exposureTimeAct = ViReal64()
        masterGainAct = ViReal64()
        dynamicNoiseCut = ViInt32()
        calculateDiameters = ViInt32()
        cancelWavefrontTilt = ViInt32()
        errorMessage = ViChar512()
        errorCode = ViInt32()
        pixelFormat = ViInt32()
        pixelFormat.value = 0 #currently 8 bit only
        camResolIndex = ViInt32()
        spotsX = ViInt32()
        spotsY = ViInt32()
        wavefrontType = ViInt32()
        limitToPupil = ViInt32()
        """

        # general methods for WFS library
        dll.WFS_init.restype = ViStatus
        
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
        dll.WFS_GetExposureTimeRange.argtypes = [ViSession, ]