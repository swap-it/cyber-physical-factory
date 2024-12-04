import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import swapit_module_server
import assets.CMMSkills as cmm_skills
import assets.VisionCMMSkills as vcmm_skills
import assets.AGVSkills as agv_skills


# or explicit arguments
def cmm_service(part_id: str, nc_program: str) -> bool:
    # get part
    agv_skills.CMMPlaceTransportSkill()
    # execute services
    vcmm_skills.DetectBarcodeSkill()
    cmm_skills.StartMeasurementSkill(
        MeasurementProgramm=nc_program, WorkpieceID=part_id
    )
    # call agv
    agv_skills.CMMPickTransportSkill()

    return True


# run the server
swapit_module_server.run(
    "/opt/module-server/configs/cmm_server.json", cmm_service, True
)
