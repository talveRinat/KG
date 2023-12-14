from SPARQLWrapper import JSON, SPARQLWrapper


class Wrapper:
    def __init__(self):
        self.sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        self.sparql.addDefaultGraph("http://dbpedia.org")

    def set_query(self, query: str):
        self.sparql.setQuery(query)

        def wrapper_generator(results):
            vars_ = results["head"]["vars"]
            for val in results["results"]["bindings"]:
                wrapper_dict = {}
                for var in vars_:
                    wrapper_dict[var] = val[var]["value"].replace(" ", "_")
                yield wrapper_dict

        try:
            self.sparql.setReturnFormat(JSON)
            results = self.sparql.query().convert()
        except Exception as e:
            print(e)

        return wrapper_generator(results)
