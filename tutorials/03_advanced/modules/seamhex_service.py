import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import swapit_module_server
import assets.SeamHexSkills as seamhex_skills
import assets.AGVSkills as agv_skills


# or explicit arguments
def seamhex_service(part_id: str, nc_program: str) -> bool:
    # execute services
    seamhex_skills.StartNcProgramSkill(
        WorkpieceID=int(part_id), CNCProgramFilename=nc_program
    )
    # call agv
    agv_skills.SeamHexPickTransportSkill()
    return True


# run the server
swapit_module_server.run(
    "/opt/module-server/configs/seamhex_server.json", seamhex_service, True
)
