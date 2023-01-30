from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    def __init__(self, **info):
        self.designation = info.get("pdes") or ''
        self.name = info.get("name") or None
        self.diameter = float(info.get("diameter")) if info.get("diameter") else float('nan')
        self.hazardous = True if info.get("pha") == 'Y' else False

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        return f"{self.designation} {self.name}"

    def __str__(self):
        return f"A NearEarthObject {self.fullname} diameter is {self.diameter:.3f}, {'it is potentially hazardous object' if self.hazardous else 'is not hazardous object'}"

    def __repr__(self):
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    def __init__(self, **info):
        self._designation = info.get('des') or ''
        self.time = cd_to_datetime(info.get('cd')) if info.get('cd') else None  # TODO: Use the cd_to_datetime function for this attribute.
        self.distance = float(info.get('dist')) if info.get('dist') else 0.0
        self.velocity = float(info.get('v_rel')) if info.get('v_rel') else 0.0

        self.neo = None

    @property
    def time_str(self):
        # TODO: Use self.designation and self.name to build a fullname for this object.
        return datetime_to_str(self.time)

    def __str__(self):
        return f"A CloseApproach {self._designation}, on {self.time_str}, approaches Earth at a distance of {self.distance} in astronomical units, and velocity {self.velocity} of km/s."

    def __repr__(self):
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
