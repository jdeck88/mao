# mao

Mobile App for Observations (MAO) -- alpha

## Language Overview 

MAO implements a terse language for transmitting "subject, predicate, object" observations. The mode of transmission and data storage system is outside the scope of this specification.  The purpose then, is to clearly define a language construct where humans and machines can cooperate on quickly and easily transmitting information.  The MAO language is composed of [heirarchical identifiers](#heirarchical-identifiers), dates, literals (any text string available which is available in one more [configurable dictionary](#configurable-dictionary)).

MAO accepts any statement in triple format, with:

 * {subject} and, optionally, {object} implementing heirarchical identifiers (see below)

 * {predicate} comes from a pre-defined set of predicates.  This is available in a [configurable dictionary](#configurable-dictionary) of terms. 

 * {object} can be one of a: a literal term (from pre-configured terms), date, URI, or [heirarchical identifiers](#heirarchical-identifiers)
 
## Heirarchical Identifiers

{persistent, resolvable identifier root} + {local identifier}
The persistent identifier is an ARK registered through the Biocode Commons identifier service and enables a {local identifier}, any local identifier that the user adopts and follows an approved form (TODO: link to this).

## Configurable Dictionary

One or more JSON lists of key:value pairs where key="term" and value="URI:pointing to reference ontology".  Adopts a common set of high level terms and then subsequent terms defined in whatever language.  All terms must register to a term in a community standard ontology, even if at a very high level.  
