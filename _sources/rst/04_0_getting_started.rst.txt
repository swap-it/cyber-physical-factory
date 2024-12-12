Getting Started
###############

Requirements and Installation
*****************************




Tutorials
*********

The following sections provide a set of tutorials with increasing complexity for beginner, intermediate and advanced users.
After successfully completing all three tutorials, the user will be capable of implementing the first three stages of the methodical approach as outlined in :doc:`Introduction to Use Case <02_overview_introduction>`. He will be in a position to equip machines and systems on the shop floor with the skill-based control framework and to define skills. He will also know how these systems can be connected to the SWAP IT architecture by setting up module servers. The user will be able to model processes as PFDLs and to have them executed by the SWAP-IT software architecture.

In the first tutorial, the user is introduced to the *skill-based control framework*. It demonstrates how to define a skill, configure and start a server and then execute a skill. These are necessary steps to equip the shop floor assets with skill servers.

In the second tutorial, the user is introduced to the *module server*. It demonstrates how to define a service, configure and start a server and then execute the service to call skills of a skill server. These are necessary steps to connect the skill server to the SWAP-IT architecture.

In the third tutorial, the user will learn how a process can be modeled as a PFDL. He will also learn to describe the capabilities of the machines and then specify them in the PFDL so that a process step is assigned to a matching machine at runtime.

At the end of all three tutorials, the use case, outlined in :doc:`Introduction to Use Case <02_overview_introduction>`, will be fully implemented, based on a simulation environment.

The following software must be installed in order to run the tutorials:
   - `Docker Desktop <https://docs.docker.com/desktop/>`_
   - Python (`miniconda <https://docs.anaconda.com/miniconda/install/>`_)

.. toctree::
   :maxdepth: 2

   04_1_beginner.rst
   04_2_intermediate.rst
   04_3_advanced.rst