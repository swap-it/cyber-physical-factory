import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import swapit_module_server
import assets.ComauSkills as comau_skills
import assets.AGVSkills as agv_skills


# or explicit arguments
def comau_service(part_id: str, nc_program: str) -> bool:
    # get part
    agv_skills.ComauPlaceTransportSkill()
    # execute services
    comau_skills.MillingSkill()
    # call agv
    agv_skills.ComauPickTransportSkill()

    return True


# run the server
swapit_module_server.run(
    "/opt/module-server/configs/comau_server.json", comau_service, True
)
