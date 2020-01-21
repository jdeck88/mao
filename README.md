# MAO

MAO is a "Mobile App for Observations" and is a A DRAFT specification for a human to machine language.   

The idea for a human to machine language comes from the idea that well structured information about the natural world, primarily coming from observations should not be confined to user interfaces but should instead should arise as a natural form of language.  For example, as a (part-time) farmer, my time in the field is extremely valuable and to make the most of my observations in the field, I don't want to constrain my recorded observations to sessions demanding my later interaction with an interface or which demands me to think in terms of some arbitrary and bespoke structure built to fit the machine.  My hands are dirty, i can't type, and i need to be mostly unecumbered by technology in that moment.  If i can speak and/or understand a language which can also be understood by machines that can retain context, I can be free to observe the world around me quickly and accurately, referring to objects around me in a manner that has contextual meaning for myself as well as anyone in the world and then communicate that to one or more mediums of my choosing.  As a language construct, MAO can extend to any mobile applications and provide context about the specific notions of anyone's personal world, which in turn provides the ability to instantly provide information to a global distributed database.

On the name "Mao": The name signifies the potential for bold transformations and organization of human society, and is a memorable and easily pronouncable 3 letter acronym.  However, the name "Mao"... yeah... all of the horrible effects of Maoist policy which, for me, makes me think about the responsibility we have in using technology and thinking about downstream consequences.   A note of caution or a super unfortunate name choice?

## Language Overview 

Machines understand identifiers and logical constructs.  Humans understand human speech. MAO is a construct which bridges the gap, lowering the barriers for humans to interact with machines.  The MAO language is composed of of [heirarchical identifiers](#heirarchical-identifiers), dates, and literals (any text string available which is available in one more [configurable dictionary](#configurable-dictionary)).  MAO understands simple sentences built on RDF triples, consisting of subjects, predicates, and objects, where:

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
 
## Example MAO statements
```E28 "gave birth to" 201```

In my language, "E28" is a cow. it is a local identifier which will be prefixed by an {identifer root} which identifiers this thing as about cows.  My {identifier root} could just as easily be about cardinal fish, airplanes, or employees.  I also have a short-list of predicates which have some global meaning for my work.  By constraining the terms that i use personally for a particular study (and my terms can be study-specific) I can easily record meaning that can later be turned into. Saying "gave birth to" i can infer that the object of the statement "201" is also a cow.

```201 "has sex" female```

I can construct further statements about the object of the first statement and assign roles to those subjects.  female is a term that i can register as an available term of the predicate "has sex".  "sex" would be defined as a term that has a particular controlled vocabularly and which available terms would be reference an ontology that describes the nature of what is "female".  

```201 "born on" 2020-01-20```

Finally, i can assign dates for particular actions.  The predicate "born on" would require an object of a date to be provided in this context.

