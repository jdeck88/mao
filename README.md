# mao
Mobile App for Observations (MAO)

MAO is a terse language for sending "subject, predicate, object" observations to a graph database

The current construction is:

1) ONE TIME ONLY Setup identifier namespaces and relationships per project.  This is soon to be configured and implemented using Biocode FIMS configuration file 
(https://github.com/biocodellc/biocode-fims)

2) user understands the Terse language format (more information to come)

3) send statements to service (currently building in python, see source here)

4) service sends statements to a graph database (neo4j)




