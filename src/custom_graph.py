"""
This is the custom module for graph with some additional logic.
"""
import re

from rdflib import URIRef, BNode, Literal, Namespace, Graph
from rdflib.namespace import Namespace, NamespaceManager
from rdflib.plugins import sparql
from rdflib.namespace import RDF, RDFS, XSD
from rdflib.serializer import Serializer

from .data_structures import GraphData


class CustomGraph(Graph):

    def __init__(self):
        super().__init__()
        self.classes: dict[GraphData] = {}
        self.object_properties: dict[GraphData] = {}
        self.data_properties: dict[GraphData] = {}

    def parse(self, iri: object, *args, **kwargs):
        """
        has the same args as graph.parse
        but has iri-arg that contains DB IRI-prefix
        ex: http://www.semanticweb.org/football/smt (http://www.semanticweb.org/football - is IRI) 
        """
        super().parse(*args, **kwargs)
        #TODO() assert re.match(iri)
        self.iri = iri

    def add_class(self, name: object):
        self.classes[name] = GraphData(name, self.iri)

    def add_object_property(self, name: object):
        self.object_properties[name] = GraphData(name, self.iri)

    def add_data_property(self, name: object):
        self.data_properties[name] = GraphData(name, self.iri)

    def get_list_classes(self):
        return list(self.classes.keys())

    def get_list_object_properties(self):
        return list(self.object_properties.keys())

    def get_list_data_properties(self):
        return list(self.data_properties.keys())
