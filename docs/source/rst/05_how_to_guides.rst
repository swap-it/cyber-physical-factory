How-to-Guides
#############

Start the Cyber-Physical Factory Docker Application
***************************************************
Pre-build docker containers for all software components that are required to start the Application Scenario are available in the repository's container registry. With these containers, it is possible to start a docker-compose project to provide all ressources necessary to test the SWAP-IT architecture. To start this docker-compose environment, start docker on your local device. Clone the *swap-it-cyberphysicalfactory* repository and enter it from a terminal. Afterwards, the project can be started with the docker-compose up command:

.. code-block:: python

    git clone https://github.com/swap-it/swap-it-cyberphysicalfactory
    cd swap-it-cyberphysicalfactory
    docker-compose up


This docker-compose project features the SWAP-IT dashboard. To monitor the execution progress from the dashboard, open a browser and connect to:

.. code-block:: python
    
    http://localhost:8080

after the docker-compose project is started.

Writing PFDL files
******************
Throughout the Tutorials section, the *Cyber-Physical Factory* PFDL is recreated. However, to get a deeper insight into the PFDL and its usage, please have a look at `Production Flow Description Language (PFDL) <https://github.com/iml130/pfdl>`_.
