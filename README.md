# mao
Mobile App for Observations (MAO) -- alpha

MAO adopts a very terse language for sending "subject, predicate, object" observations to a graph database.  Observational data can be sent via email, SMS, app, curl statements, or web interfaces.

An observation such as {subject} "inheat" can be sent to an email address.  The sender is the observer.  The date sent is the date of the observation.  The subject is defined by the user (an ID tag) and the descriptive property is a single word.  These terms can be expanded based on the context of the sender or the recipient.

Subject: Thing: Prefix (drop-down) / Suffix (text)
Predicate:
     Has State OR Interaction (Drop-down interactions)
Object:
    If Predicate = Has State (Drop-down States)
    if Predicate = Interaction, Prefix (drop-down) / Suffix (text)

WORKFLOW:

1) Setup identifier namespaces and relationships per project.  Configuration file format soon to come, likely adapting the configuration file syntax of the Biocode FIMS project (https://github.com/biocodellc/biocode-fims)

2) User understands the Terse language format.  More information on this coming.  This is partly based on the configuration file specified in step 1 and partly based on triple syntax using subject predicate object statements

3) Send statements to service (currently building in python, see source here)

4) service sends statements to a graph database (neo4j)

REQUIREMENTS:

1) neo4j (http://neo4j.com/)

2) python (https://www.python.org/)

3) py2neo (http://py2neo.org/)




