Intermediate
############

This tutorial demonstrates how to set up a precompiled resource server based on the *Common Information Model*. From here on we will call this server *module server*. This module server creates the prerequisites for the universal connector on the SWAP-IT side.

The Python packages for the module server that is required to run this tutorial and detailed instructions for installing and deploying it can be found in the following repository:

- `SWAP-IT Module Server <https://github.com/cognitive-production/swap-it-module-server>`_ (Python Package for providing precompiled SWAP-IT resource servers based on the *Common Information Model* and the *open62541 Server Template*)

Please navigate to the *02_intermediate* folder of the repository to start the intermediate tutorial.

Start a module server
*********************

Again there are two methods to implement this example in the context of this tutorial. 
The first option is to clone the repository and install the Python package. To configure a module server, based on a JSON file, the following lines of code are necessary:

.. code-block:: python
    :linenos:

    import swapit_module_server
    from assets.RobotSkills import PickSkill

    # Create the service implementation


    # use explicit arguments
    def pick_service(x: float, y: float, z: float) -> bool:
        PickSkill(x, y, z)
        return True


    # The return value must correspond to the "output_param" of the config,
    # i.e. boolean -> bool

    # run the server
    swapit_module_server.run("/opt/module-server/configs/robot.json", pick_service, False)


.. list-table:: Explanation of code
   :widths: 10 70
   :header-rows: 1

   * - line number
     - meaning
   * - 1
     - import of installed python packages
   * - 2
     - import of Robot Skill
   * - 8-10
     - definition of module server service (execution of PickSkill)
   * - 17
     - | - the server is started, passing the JSON config file path, the service name and whether 
       | the module server is to register with the *Device Registry* or not
       | - typically it is to do so, otherwise the "Execution Engine" will not be able to assign 
       | process steps to this asset, because it is just not known to it, but since so far there 
       | is no registry running the flag is set to *False*

The service calls the *Robot PickSkill* which is provided by the Python module *RobotSkills.py* in the *assets* folder. The module looks like this:

.. code-block:: python
    :linenos:

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

.. list-table:: Explanation of code
   :widths: 10 70
   :header-rows: 1

   * - line number
     - meaning
   * - 6-8
     - creates handle for connection to skill server
   * - 16-30
     - | wraps skill communication in a Python function, that can be imported and executed in 
       | other modules (see :doc:`Beginner <04_1_beginner>`)

The JSON file specifying the module server looks like this:

.. code-block:: JSON
    :linenos:

    {
        "application_name": "Robot",
        "resource_ip": "Module_Server_Robot",
        "port": "14841",
        "module_type": "PickModuleType",
        "module_name": "RobotModule",
        "service_name": "PickService",
        "device_registry": "opc.tcp://Device_Registry:8000",
        "registry_subscriptions": [
            {
                "object": "State"
            },
            {
                "object": "Capabilities"
            }
        ],
        "Capabilities": [
            {
                "variable_name": "payload",
                "variable_type": "numeric",
                "variable_value": "10",
                "relational_operator": "SmallerOrEqual"
            },
            {
                "variable_name": "costs",
                "variable_type": "numeric",
                "variable_value": "100",
                "relational_operator": "Greater"
            }
        ],
        "channels": "100",
        "sessions": "100",
        "namespace": "https://cps.iwu.fraunhofer.de/UA/CpsDemo",
        "input_params": {
            "x": "number",
            "y": "number",
            "z": "number"
        },
        "output_param": {
            "success": "boolean"
        }
    }

.. list-table:: Explanation of code
   :widths: 10 70
   :header-rows: 1

   * - line number
     - meaning
   * - 3
     - name of service in a docker compose network
   * - 4
     - port at which module server is available
   * - 6
     - name by which module server can be found in a OPC-UA client application
   * - 7
     - name of OPC-UA service
   * - 8
     - *Device_Registry* entpoint in a docker compose network
   * - 17-30
     - definition of capabilities (will be explained later on)
   * - 34-38
     - definition of input parameters of service
   * - 39-41
     - definition of output parameters of service

.. important::
    
    Given the advantages of the second method described in the :doc:`Beginner <04_1_beginner>` tutorial, only the docker compose approach will be presented in the remainder of this and the next tutorial.

The server can be started with the following docker compose command:

.. code-block:: bash

    docker compose -f docker-compose-start-module-server.yml -p intermediate up -d

The YAML files looks like this:

.. code-block:: yaml
    :linenos:

    services:

    Module_Server_Robot:
        image: ghcr.io/swap-it/cyberphysicalfactory/module-server:latest
        ports:
            - 14841:14841
        volumes:
            - "./assets:/opt/assets"
            - "./modules:/opt/module-server"
        command: ["/opt/module-server/robot.py"]

Given the similarity to the compose file of the skill server, the code needs no further explanation.

Once the module server is running, you can take a look at it with the OPC-UA client:

.. figure:: ../fig/uaexpert_idle_intermediate.PNG
   :align: center

   *UaExpert* view on *Robot* module server. The server is in state (4) *ASSET_STATE_IDLE* waiting for execution.

Start the Robot skill server
****************************

To start both a skill and a module server, the following YAML file is executed with docker compose:

.. code-block:: YAML
    :linenos:

    services:

        Module_Server_Robot:
            image: ghcr.io/swap-it/cyberphysicalfactory/module-server:latest
            ports:
                - 14841:14841
            volumes:
                - "./assets:/opt/assets"
                - "./modules:/opt/module-server"
            command: ["/opt/module-server/robot.py"]
            
        Skill_Server_Robot:
            hostname: robot
            image: ghcr.io/swap-it/cyberphysicalfactory/skill-server:latest
            ports:
            - "4841:4840"
            volumes:
            - ./skills:/usr/skill_server/skills
            command: ["start_skill_server.py",--machine, Robot]

Execute this YAML file with docker compose by typing the following command in a terminal:

.. code-block:: bash

    docker compose -f docker-compose-start-skill-and-module-server.yml -p intermediate up -d

This wil start two containers in *Docker Desktop*. One, running the module server and one running the skill server. Both are communicating with each other.

.. figure:: ../fig/docker_desktop_intermediate.PNG
   :align: center

   *Docker Desktop* view on *Robot* skill and module servers.

Taking a look at these two servers the user will see, that they are both in an *idle* state.

.. figure:: ../fig/uaexpert_skill_and_module_server_intermediate.PNG
   :align: center

   *UaExpert* view on *Robot* skill and module server. The skill server is in state (4) *idle* and the module server is in state (4) *ASSET_STATE_IDLE*.

After manually calling the *PickService* of the module server the *PickSkill* of the skill server will be executed.

.. figure:: ../fig/uaexpert_skill_and_module_server_executing_intermediate.PNG
   :align: center

   *UaExpert* view on *Robot* skill and module server. The skill server is in state (6) *execute* and the module server is in state (4) *ASSET_STATE_IDLE* after right clicking the *PickService* and calling it.

The main difference and the big leap forward in connecting the machines to the SWAP-IT software architecture is the fact that skills of a skill server can now be called via a SWAP-IT compatible module server. 
In the next tutorial, the user will learn how to connect the module servers to the SWAP-IT architecture to execute production processes modeled as PFDL.