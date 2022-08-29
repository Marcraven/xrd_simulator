"""A scattering unit is generated by the :class:`xrd_simulator.polycrystal.Polycrystal` as the beam interacts with the sample.
For advanced users it can be usefull to interact with the scattering units, this is preferably done via the
:class:`xrd_simulator.detector.Detector` which will hold all the scatterign units created during diffraction
from the polycrystal.

"""
import numpy as np


class ScatteringUnit(object):

    """Defines a scattering region in space as a single crystal as a convex polyhedra.

    The scattering unit is described in laboratory coordinates.

    Args:
        convex_hull (:obj:`scipy.spatial.ConvexHull`): Object describing the convex hull of the scattering unit.
        scattered_wave_vector (:obj:`numpy array`): Scattered wavevector ```shape=(3,)```
        incident_wave_vector (:obj:`numpy array`): Incident wavevector ```shape=(3,)```
        wavelength (:obj:`float`):  Wavelength of xrays in units of angstrom.
        incident_polarization_vector (:obj:`numpy array`): Unit vector of linear polarization ```shape=(3,)```
        rotation_axis (:obj:`numpy array`): Sample motion rotation axis ```shape=(3,)```
        time (:obj:`numpy array`): Parametric value in range [0,1] determining at which instance during sample
            motion the scattering occured.
        phase (:obj:`xrd_simulator.phase.Phase`): The phase of the scattering unit.
        hkl_indx (:obj:`int`): Index of Miller index in the `phase.miller_indices` list.

    Attributes:
        convex_hull (:obj:`scipy.spatial.ConvexHull`): Object describing the convex hull of the scattering unit.
        scattered_wave_vector (:obj:`numpy array`): Scattered wavevector ```shape=(3,)```
        incident_wave_vector (:obj:`numpy array`): Incident wavevector ```shape=(3,)```
        wavelength (:obj:`float`):  Wavelength of xrays in units of angstrom.
        incident_polarization_vector (:obj:`numpy array`): Unit vector of linear polarization ```shape=(3,)```
        rotation_axis (:obj:`numpy array`): Sample motion rotation axis ```shape=(3,)```
        time (:obj:`numpy array`): Parametric value in range [0,1] determining at which instance during sample
            motion the scattering occured.
        phase (:obj:`xrd_simulator.phase.Phase`): The phase of the scattering unit.
        hkl_indx (:obj:`int`): Index of Miller index in the `phase.miller_indices` list.
        element_index (:obj:`int`): Index of mesh tetrahedral element refering to a `xrd_simulator.polycrystal.Polycrystal`
            object from which the scattering unit originated.

    """

    def __init__(
            self,
            convex_hull,
            scattered_wave_vector,
            incident_wave_vector,
            wavelength,
            incident_polarization_vector,
            rotation_axis,
            time,
            phase,
            hkl_indx,
            element_index):
        self.convex_hull = convex_hull
        self.scattered_wave_vector = scattered_wave_vector
        self.incident_wave_vector = incident_wave_vector
        self.wavelength = wavelength
        self.incident_polarization_vector = incident_polarization_vector
        self.rotation_axis = rotation_axis
        self.time = time
        self.phase = phase
        self.hkl_indx = hkl_indx
        self.element_index = element_index

    @property
    def hkl(self):
        """hkl (:obj:`numpy array`): Miller indices [h,k,l] ``shape=(3,)``."""
        return self.phase.miller_indices[self.hkl_indx]

    @property
    def real_structure_factor(self):
        """hkl (:obj:`numpy array`): Real part of unit cell structure factor"""
        if self.phase.structure_factors is not None:
            return self.phase.structure_factors[self.hkl_indx, 0]
        else:
            return self.phase.structure_factors

    @property
    def imaginary_structure_factor(self):
        """hkl (:obj:`numpy array`): Imaginary part of unit cell structure factor"""
        if self.phase.structure_factors is not None:
            return self.phase.structure_factors[self.hkl_indx, 1]
        else:
            return self.phase.structure_factors

    @property
    def lorentz_factor(self):
        """Compute the Lorentz intensity factor for a scattering_unit.
        """
        k = self.incident_wave_vector
        kp = self.scattered_wave_vector
        theta = np.arccos(k.dot(kp) / (np.linalg.norm(k)**2)) / 2.
        korthogonal = kp - (k * kp.dot(k) / (np.linalg.norm(k)**2))
        eta = np.arccos(
            self.rotation_axis.dot(korthogonal) /
            np.linalg.norm(korthogonal))
        tol = 0.5
        if np.abs(np.degrees(eta)) < tol or np.abs(np.degrees(eta)) > 180-tol or np.degrees(theta) < tol:
            return np.inf
        else:
            return 1. / (np.sin(2 * theta) * np.abs(np.sin(eta)))

    @property
    def polarization_factor(self):
        """Compute the Polarization intensity factor for a scattering_unit.
        """
        khatp = self.scattered_wave_vector / \
            np.linalg.norm(self.scattered_wave_vector)
        return 1 - np.dot(self.incident_polarization_vector, khatp)**2

    @property
    def centroid(self):
        """centroid (:obj:`numpy array`): centroid of the scattering region. ``shape=(3,)``
        """
        return np.mean(
            self.convex_hull.points[self.convex_hull.vertices], axis=0)

    @property
    def volume(self):
        """volume (:obj:`float`): volume of the scattering region volume
        """
        return self.convex_hull.volume
