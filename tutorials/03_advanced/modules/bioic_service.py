import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import swapit_module_server
import assets.BioiCSkills as bioic_skills
import assets.VisionBioiCSkills as vbioic_skills
import assets.AGVSkills as agv_skills


# or explicit arguments
def bioic_service(part_id: str, color: float) -> bool:
    # get part
    agv_skills.BioiCPlaceTransportSkill()
    # execute services
    vbioic_skills.DetectBarcodeSkill()
    bioic_skills.DBBPickAndPlaceSkill(color=int(color))
    # call agv
    agv_skills.BioiCPickTransportSkill()

    return True


# run the server
swapit_module_server.run(
    "/opt/module-server/configs/bioic_server.json", bioic_service, True
)
