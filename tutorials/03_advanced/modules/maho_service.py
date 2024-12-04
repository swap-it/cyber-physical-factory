import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import swapit_module_server
import assets.RoboOperatorSkills as ro_skills
import assets.VisionRoboOperatorSkills as vro_skills
import assets.AGVSkills as agv_skills


# or explicit arguments
def maho_service(part_id: str, nc_program: str) -> bool:
    # get part
    agv_skills.RoboOperatorPlaceTransportSkill()
    # execute services
    vro_skills.DetectBarcodeSkill()
    ro_skills.StartConfigurationSkill()
    # call agv
    agv_skills.RoboOperatorPickTransportSkill()

    return True


# run the server
swapit_module_server.run(
    "/opt/module-server/configs/maho_server.json", maho_service, True
)
