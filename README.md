# mao

Mobile App for Observations (MAO) -- a draft specification for a language where humans and machines cooperate.

## Language Overview 

MAO implements a terse language for transmitting "subject, predicate, object" observations. The mode of transmission and data storage system is outside the scope of this specification.  The purpose then, is to clearly define a language construct where humans and machines can cooperate on quickly and easily transmitting information.  Machines understand identifiers and logical constructs.  Humans understand human human speach.  The MAO language is meant to bridge the gap between humans by enabling a very simple language that humans can learn and which is also computable.  The MAO language is composed of of [heirarchical identifiers](#heirarchical-identifiers), dates, and literals (any text string available which is available in one more [configurable dictionary](#configurable-dictionary)).

MAO accepts any statement in triple format, with:

 * {subject} and, optionally, {object} implementing heirarchical identifiers (see below)

 * {predicate} comes from a pre-defined set of predicates.  This is available in a [configurable dictionary](#configurable-dictionary) of terms. 

 * {object} can be one of a: a literal term (from pre-configured terms), date, URI, or [heirarchical identifiers](#heirarchical-identifiers)
 
## Heirarchical Identifiers

{identifier root} + {local identifier}
The persistent identifier is an ARK registered through the Biocode Commons identifier service and enables a {local identifier}, any local identifier that the user adopts and follows an approved form (TODO: link to this).  Humans refer to all kinds of things around them, such as "2007 Tundra" (my car), "E28" (a cow), "Eva" (a grandchild).  These identifiers have meaning in my own life, but in order for them to have meaning in a larger context, i need to work on structuring an {identifier root}.  The {identifier root} is a resolvable, persistent, and is structured around a particular context.  The BCID scheme (insert REF), enables users to create an {identifier root} that meets these criteria. 

## Configurable Dictionary

One or more JSON lists of key:value pairs where key="term" and value="URI:pointing to reference ontology".  Adopts a common set of high level terms and then subsequent terms defined in whatever language.  All terms must register to a term in a community standard ontology, even if at a very high level.  

## Date

TODO: Insert format for dates.

## URIs

TODO: Insert format for URIs.

## Syntax validator

Service for validating all MAO statements.  
