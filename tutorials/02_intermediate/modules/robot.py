import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import swapit_module_server
from assets.RobotSkills import PickSkill

# Create the service implementation


# use explicit arguments
def pick_service(x: float, y: float, z: float) -> bool:
    PickSkill(x, y, z)
    return True


# The return value must correspond to the "output_param" of the config,
# i.e. boolean -> bool

# run the server
swapit_module_server.run("/opt/module-server/configs/robot.json", pick_service, False)
