from skillcommunication.assetskillshandle import AssetSkillsHandle
from skillcommunication.assetskillscommunication_factory import (
    createSkillCom_Python_Asyncua,
)

skillComm = createSkillCom_Python_Asyncua(
    opc_url="opc.tcp://robot:4840",
)

# create asset skills handle, inject the skill communication object
assetHandle = AssetSkillsHandle(
    assetName="LocalPythonAsset", assetSkillCommunication=skillComm
)


def PickSkill(x=0, y=0, z=0):
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("PickSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # set new skill parameters in stSkillDataCommand, you have to know about each parameter
    skilldata.stSkillDataCommand.astParameters[0].strValue = str(x)
    skilldata.stSkillDataCommand.astParameters[1].strValue = str(y)
    skilldata.stSkillDataCommand.astParameters[2].strValue = str(z)

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("PickSkill")
