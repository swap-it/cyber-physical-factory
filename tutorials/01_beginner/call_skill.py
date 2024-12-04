from sbc_communication.assetskillshandle import AssetSkillsHandle
from sbc_communication.assetskillscommunication_factory import (
    createSkillCom_Python_Asyncua,
)

skillComm = createSkillCom_Python_Asyncua(
    opc_url="opc.tcp://127.0.0.1:4841",
)

# create asset skills handle, inject the skill communication object
assetHandle = AssetSkillsHandle(
    assetName="LocalPythonAsset", assetSkillCommunication=skillComm
)

availableSkills = assetHandle.read_availableSkills()

skillName = "PickSkill"

# read actual skilldata (SkillData) as reference
skilldata = assetHandle.read_stSkillData(skillName)
# reset skillDataCommand
skilldata.reset_SkillDataCommand()

# set new skill parameters in stSkillDataCommand, you have to know about each parameter
skilldata.stSkillDataCommand.astParameters[0].strValue = str(0)
skilldata.stSkillDataCommand.astParameters[1].strValue = str(0)
skilldata.stSkillDataCommand.astParameters[2].strValue = ""

# execute skill, skill parameters from skilldata will be written inside
result = assetHandle.skillExecHandler.executeSkill(skillName)
