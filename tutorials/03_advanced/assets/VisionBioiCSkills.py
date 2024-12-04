from skillcommunication.assetskillshandle import AssetSkillsHandle
from skillcommunication.assetskillscommunication_factory import (
    createSkillCom_Python_Asyncua,
)

skillComm = createSkillCom_Python_Asyncua(
    opc_url="opc.tcp://visionbioic:4840",
)

# create asset skills handle, inject the skill communication object
assetHandle = AssetSkillsHandle(
    assetName="LocalPythonAsset", assetSkillCommunication=skillComm
)


def DetectBarcodeSkill(**kwargs):
    """Executes DetectBarcodeSkill"""
    assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("DetectBarcodeSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("DetectBarcodeSkill")
