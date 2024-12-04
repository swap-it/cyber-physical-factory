Glossary
========
.. glossary::


    Assignment Agent
        Entity that interacts with an Execution Engine and a Device Registry to assign a service to one concrete resource out of a set of possible resources.

    Device Registry
        Registry Module where resource OPC UA server, representing field level devices, can register themself and thus, make themself available to execute PFDL services. In addition,
        the Device Registry has a build-in functionality to filter suitable resources for a service execution based on a resource's capabilities.

    Execution Engine
        Interface between the PFDL scheduler and field level resources that executes the scheduled services on the field level. In addition, it handles the parameter flow between services and tasks.

    Module Server
        Precompiled resource server based on the Common Information Model, which is configured with a JSON file and provided as a Python package.

    OPC UA Information Model
        Contains all nodes and references to map a specific entity to an OPC UA server.

    PFDL
        The Production Flow Description Language is a domain specific language that describes a production order. It is parsed by the scheduler and transformed into a structure to schedule the execution.

    PFDL Scheduler
        Generates a process sequence out of a PFDL description and schedules the specified services and tasks.

    Process Agent
        Agent consisting of a PFDL scheduler and an Execution Engine. It drives the execution of the process specified within a PFDL.

   PFDL
      Production Flow Description Language is a domain specific language to configure the PFDL-scheduler

   Skill-based control framework
      Framework for implementing skills in python and provide them via an opc ua server. It makes it possible to call python functions vie the skill interface based on the Module Type Package (MTP) service interface.