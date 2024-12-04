import glob
import os
import argparse
import json

from sbc_statemachine.skilldatahandle import (
    SkillDataHandle,
)
from sbc_server.skillimplementations import (
    ExternalExecuteSkill,
)
from sbc_server.skillserver_opcua_vc import SkillServer_OPCUA_VC
from sbc_server.runskillserverhelper import run_skillserver

# Specify the path to the json files subdirectory
json_directory_path = "skills/"
# empty list for storage of skills
skills = []


# 1. Implement custom skill class inheriting from ExternalExecuteSkill
class CustomSkill(ExternalExecuteSkill):
    def __init__(self, json_file) -> None:
        data = SkillDataHandle()
        data.set_fromJsonFile(json_file, toSkillDataDefault=True)
        data.reset_SkillDataCommand()
        super().__init__(data=data)


def server(machine_name, port):
    # 2. Create object of custom skill class
    # Use glob to find all JSON files in the subdirectory
    json_files = glob.glob(os.path.join(json_directory_path, "*.json"))
    for json_file in json_files:
        if machine_name.lower() in json_file.lower():
            with open(json_file, "r") as file:
                data = json.load(file)
                skill_name = data.get("strName")
            skills.append(
                CustomSkill(json_directory_path + skill_name + machine_name + ".json")
            )

    # 3. create skillserver object and inject custom skill objects
    skill_server_OPCUA = SkillServer_OPCUA_VC(
        skills,
        skill_cycletime=0.1,
        server_cycletime=0.5,
        port=port,
    )
    # 4. start skillserver, for example using run_skillserver from runskillserverhelper
    run_skillserver(skill_server_OPCUA)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--machine", default="TestMachine", help="Provide name of machine"
    )
    parser.add_argument("--port", default=4840, help="Provide port of server")
    args = parser.parse_args()
    server(args.machine, args.port)
