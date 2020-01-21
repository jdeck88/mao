# MAO

MAO is a "Mobile App for Observations" and is a A DRAFT specification for a human to machine language.   

The idea for a human to machine language comes from the idea that well structured information about the natural world, primarily coming from observations should not be confined to user interfaces but should instead should arise as a natural form of language. As a (part-time) farmer, my time in the field is extremely valuable and to make the most of my observations in the field, I don't want to constrain my recorded observations to sessions demanding my later interaction with an interface or which demands me to think in terms of a 2 dimensional array (e.g. spreadsheet) or even a mobile app.  My hands are dirty, i can't type on a mobile phone, and i need to be mostly unecumbered by technology in that moment.  However, if i can speak and/or understand a language which can also be understood by machines that can retain the context, I can be free to observe the world around me quickly and accurately, referring to objects around me in a manner that has contextual meaning for myself as well as anyone in the world.  As a language construct, MAO can easily be extended to other mobile applications and provide context about the specific notions of my anyone's personal world, which in turn provides the ability to instantly provide information to a global distributed database.

On the name "Mao": The name signifies the potential for bold transformations and organization of human society, and is a memorable and easily pronouncable 3 letter acronym.  However, the name "Mao"... yeah... all of the horrible effects of Maoist policy which, for me, makes me think about the responsibility we have in using technology and thinking about downstream consequences.   A note of caution or a super unfortunate name choice?

## Language Overview 

MAO is meant to be a terse language which humans can easily learn and machines can easily parse. Machines understand identifiers and logical constructs.  Humans understand human human speach.  The MAO language is composed of of [heirarchical identifiers](#heirarchical-identifiers), dates, and literals (any text string available which is available in one more [configurable dictionary](#configurable-dictionary)).  MAO understands simple sentences built on RDF triples, consisting of subjects, predicates, and objects, where:

 * {subject} are a [heirarchical identifier](#heirarchical-identifiers)

 * {predicate} is one of a [configurable dictionary](#configurable-dictionary) of terms. 

 * {object} can be one of a: [configurable dictionary term](#configurable-dictionary), date, URI, or [heirarchical identifiers](#heirarchical-identifiers)
 
MAO statements may or may not reside in a database.  As language is spoken and interpreted it may not always be necessary to record it: thus, databasing the language itself is outside this specification.  However, MAO is ultimately designed to facilitate recording all statements into database format.  
 
## Heirarchical Identifiers

{identifier root} + {local identifier}

Humans refer to all kinds of things around them, such as "2007 Tundra" (my car), "E28" (a cow), "Eva" (a grandchild).  These identifiers have meaning for some people, and i understand the context, but in order for them to have meaning to a machine, and in turn the much larger world, i need to add an {identifier root} which makes the complete identifier resolvable, persistent, and pointing to a defined context which is derived from an ontology.  The BCID scheme (insert REF), enables users to create an {identifier root} that meets these criteria.  

## Configurable Dictionary

One or more lists of key:value pairs where key="my local term" and value="URI:pointing to reference ontology".  Adopts a common set of high level terms and then subsequent terms defined in whatever language.  All terms must register to a term in a community standard ontology, even if at a very high level.  User-provided local term configurations.  For this to work locally, we would need to download OWL files of relevant high-level ontologies.  For communication beyond our own sphere and provide context to the world, we transmit the "value" of the key:value pair to the world so computers can transmit and infer based on the ontology term that is referenced.

## Date

TODO: Insert format for dates.

## URIs

Insert format for URIs.  This is just a pointer to any resource on the web.

## Syntax validator

Service for validating all MAO statements, which includes:
 * structure (subject, predicate, object)
 * format (e.g. date, URI format)
 * identifier syntax -- resolvable, context defined, parseable local identifier
 * term lists (needs further definition).
 

