#/usr/bin/python

# a simple neo4j script to create two nodes and an edge

# setup user name & password
import myconfig
print myconfig.getUser()

from py2neo import Graph, Path, Node, Relationship
graph = Graph("http://"+myconfig.getUser()+":"+myconfig.getPass()+"@localhost:7474/db/data")

# graph.merge_one only creates this node if it has to
subject = graph.merge_one("instance","uniqueid", "E58")
object = graph.merge_one("instance","uniqueid", "billy2")

# only create unique relationships, don't need to keep re-expressing the same thing
# this fails for some reason
#rel = graph.create_unique(Relationship(subject,"bredBy",object))
rel = Relationship(subject,"bredBy",object)

graph.create(rel)

