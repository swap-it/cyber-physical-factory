import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import swapit_module_server
from assets.RobotSkills import PickSkill


# use explicit arguments
def pick_service(x: float, y: float, z: float) -> bool:
    PickSkill(x, y, z)
    return True


# run the server
swapit_module_server.run("/opt/module-server/configs/robot.json", pick_service, True)
