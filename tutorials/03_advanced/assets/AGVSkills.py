from skillcommunication.assetskillshandle import AssetSkillsHandle
from skillcommunication.assetskillscommunication_factory import (
    createSkillCom_Python_Asyncua,
)

skillComm = createSkillCom_Python_Asyncua(
    opc_url="opc.tcp://agv:4840",
)

# create asset skills handle, inject the skill communication object
assetHandle = AssetSkillsHandle(
    assetName="LocalPythonAsset", assetSkillCommunication=skillComm
)


def BioiCPickTransportSkill(**kwargs):
    """Executes BioiCPickTransportSkill"""

    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("BioiCPickTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("BioiCPickTransportSkill")


def BioiCPlaceTransportSkill(**kwargs):
    """Executes BioiCPlaceTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("BioiCPlaceTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("BioiCPlaceTransportSkill")


def CMMPickTransportSkill(**kwargs):
    """Executes CMMPickTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("CMMPickTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("CMMPickTransportSkill")


def CMMPlaceTransportSkill(**kwargs):
    """Executes CMMPlaceTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("CMMPlaceTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("CMMPlaceTransportSkill")


def ComauPickTransportSkill(**kwargs):
    """Executes ComauPickTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("ComauPickTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("ComauPickTransportSkill")


def ComauPlaceTransportSkill(**kwargs):
    """Executes ComauPlaceTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("ComauPlaceTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("ComauPlaceTransportSkill")


def DMUPickTransportSkill(**kwargs):
    """Executes DMUPickTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("DMUPickTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("DMUPickTransportSkill")


def DMUPlaceTransportSkill(**kwargs):
    """Executes DMUPlaceTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("DMUPlaceTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("DMUPlaceTransportSkill")


def RoboOperatorPickTransportSkill(**kwargs):
    """Executes RoboOperatorPickTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("RoboOperatorPickTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("RoboOperatorPickTransportSkill")


def RoboOperatorPlaceTransportSkill(**kwargs):
    """Executes RoboOperatorPlaceTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("RoboOperatorPlaceTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill(
        "RoboOperatorPlaceTransportSkill"
    )


def SeamHexPickTransportSkill(**kwargs):
    """Executes SeamHexPickTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("SeamHexPickTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("SeamHexPickTransportSkill")


def SeamHexPlaceTransportSkill(**kwargs):
    """Executes SeamHexPlaceTransportSkill"""
    availableSkills = assetHandle.read_availableSkills()

    # read actual skilldata (SkillData) as reference
    skilldata = assetHandle.read_stSkillData("SeamHexPlaceTransportSkill")
    # reset skillDataCommand
    skilldata.reset_SkillDataCommand()

    # execute skill, skill parameters from skilldata will be written inside
    result = assetHandle.skillExecHandler.executeSkill("SeamHexPlaceTransportSkill")
