from manimlib.imports import *

class Example3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(circle,axes, vec1)
        #self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(PI)
        #self.stop_3dillusion_camera_rotation()

