# mao
Mobile App for Observations (MAO)

MAO is a terse language for sending "subject, predicate, object" observations to a graph database.  MAO forms the foundation for easily sending observational data to a repository from a variety of sources (email, SMS, app, curl statements, web pages).

The current construction is:

1) Setup identifier namespaces and relationships per project.  Configuration file format soon to come, likely adapting the configuration file syntax of the Biocode FIMS project (https://github.com/biocodellc/biocode-fims)

2) User understands the Terse language format.  More information on this coming.  This is partly based on the configuration file specified in step 1 and partly based on triple syntax using subject predicate object statements

3) Send statements to service (currently building in python, see source here)

4) service sends statements to a graph database (neo4j)




