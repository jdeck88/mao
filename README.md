# MAO

A DRAFT specification for a human to machine language.  MAO comes from "Mobile App for Observations"

## Language Overview 

MAO is meant to be a terse language which humans can easily learn and machines can easily parse. Machines understand identifiers and logical constructs.  Humans understand human human speach.  The MAO language is composed of of [heirarchical identifiers](#heirarchical-identifiers), dates, and literals (any text string available which is available in one more [configurable dictionary](#configurable-dictionary)).  MAO understands simple sentences built on RDF triples, consisting of subjects, predicates, and objects, where:

 * {subject} are a [heirarchical identifier](#heirarchical-identifiers)

 * {predicate} is one of a [configurable dictionary](#configurable-dictionary) of terms. 

 * {object} can be one of a: [configurable dictionary term](#configurable-dictionary), date, URI, or [heirarchical identifiers](#heirarchical-identifiers)
 
MAO statements may or may not reside in a database.  As language is spoken and interpreted it may not always be necessary to record it: thus, databasing the language itself is outside this specification.  However, MAO is ultimately designed to facilitate recording all statements into database format.  
 
## Heirarchical Identifiers

{identifier root} + {local identifier}

Humans refer to all kinds of things around them, such as "2007 Tundra" (my car), "E28" (a cow), "Eva" (a grandchild).  These identifiers have meaning in my own life, and i understand them their context but in order for them to have meaning to a machine, and in turn the much larger world, i need to add an {identifier root}.  The {identifier root} is resolvable, persistent, and has a defined context.  The BCID scheme (insert REF), enables users to create an {identifier root} that meets these criteria.  

## Configurable Dictionary

One or more lists of key:value pairs where key="term" and value="URI:pointing to reference ontology".  Adopts a common set of high level terms and then subsequent terms defined in whatever language.  All terms must register to a term in a community standard ontology, even if at a very high level.  

## Date

TODO: Insert format for dates.

## URIs

TODO: Insert format for URIs.

## Syntax validator

Service for validating all MAO statements, which includes:
 * structure (subject, predicate, object)
 * format (e.g. date, URI format)
 * identifier syntax -- resolvable, context defined, parseable local identifier
 * term lists (needs further definition).
 

