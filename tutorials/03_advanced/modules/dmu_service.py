import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import swapit_module_server
import assets.DMUSkills as dmu_skills
import assets.AGVSkills as agv_skills


# or explicit arguments
def dmu_service(part_id: str, nc_program: str) -> bool:
    # get part
    agv_skills.DMUPlaceTransportSkill()
    # execute services
    dmu_skills.MillingSkill()
    # call agv
    agv_skills.DMUPickTransportSkill()

    return True


# run the server
swapit_module_server.run(
    "/opt/module-server/configs/dmu_server.json", dmu_service, True
)
