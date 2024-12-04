from skillcommunication.assetskillshandle import AssetSkillsHandle
from skillcommunication.assetskillscommunication_factory import (
    createSkillCom_Python_Asyncua,
)

skillComm = createSkillCom_Python_Asyncua(
    opc_url="opc.tcp://seamhex:4840",
)

# create asset skills handle, inject the skill communication object
assetHandle = AssetSkillsHandle(
    assetName="LocalPythonAsset", assetSkillCommunication=skillComm
)


def StartNcProgramSkill(WorkpieceID="", CNCProgramFilename="", **kwargs):
    """Executes StartNcProgramSkill"""
    assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("StartNcProgramSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # set new skill parameters in stSkillDataCommand, you have to know about each parameter
    skilldata.stSkillDataCommand.astParameters[0].strValue = str(WorkpieceID)
    skilldata.stSkillDataCommand.astParameters[1].strValue = str(CNCProgramFilename)

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("StartNcProgramSkill")
