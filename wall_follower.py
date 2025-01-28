class WallFollower:
    """Class to safely explore an environment (without crashing) when the pose is unknown."""
    
    def __init__(self, dt: float):
        """Wall following class initializer.

        Args:
            dt: Sampling period [s].

        """
        self._dt: float = dt
        
    def compute_commands(self, z_us: list[float], z_v: float, z_w: float) -> tuple[float, float]:
        """Wall following exploration algorithm.

        Args:
            z_us: Distance from every ultrasonic sensor to the closest obstacle [m].
            z_v: Odometric estimate of the linear velocity of the robot center [m/s].
            z_w: Odometric estimate of the angular velocity of the robot center [rad/s].

        Returns:
            v: Linear velocity [m/s].
            w: Angular velocity [rad/s].

        """
        # TODO: 1.14. Complete the function body with your code (i.e., compute v and w).
        
        midFront_error = (z_us[0] - z_us[7])
        midBack_error = (z_us[15] - z_us[8])
        error = midFront_error - midBack_error

        if error > 0.0:
            w = 0.5
        elif error < 0.0:
            w = -0.5

        # if z_us[3] and z_us[4] < 0.4:
        #     v = 0.0
        #     if z_us[3] > z_us[4]:
        #         w = -0.5
        #     else:
        #         w = 0.5
        # else:
        v = 0.5
        
        return v, w