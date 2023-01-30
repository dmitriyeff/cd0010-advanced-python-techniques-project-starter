from filters import AttributeFilter

class NEODatabase:
    def __init__(self, neos, approaches):
        self._neos = neos
        self._approaches = approaches

        self.neos_by_designation = {}
        self.neos_by_name = {}

        for neo in self._neos:
            self.neos_by_designation[neo.designation] = neo

            if neo.name:
                self.neos_by_name[neo.name] = neo

        for approach in self._approaches:
            neo = self.neos_by_designation[approach._designation]
            approach.neo = neo

            neo.approaches.append(approach)

    def get_neo_by_designation(self, designation):
        neo_by_designation = self.neos_by_designation.get(designation)

        return neo_by_designation


    def get_neo_by_name(self, name):
        # check for exact name
        neo_by_name = self.neos_by_name.get(name)

        # if no exact matches, check for spelling and capitalization
        if not neo_by_name:
            for neo_name in self.neos_by_name.keys():
                if neo_name.strip().lower() == name:
                    neo_by_name = self.neos_by_name.get(neo_name)

        return neo_by_name


    def query(self, filters=[]):
        # TODO: Generate `CloseApproach` objects that match all of the filters.
        if not len(filters):
            #return self._approaches
            for approach in self._approaches:
                yield approach

        for approach in self._approaches:
            matched_approach = approach
            for filter in filters:
                attrFilter = AttributeFilter(filter["op"], filter["value"])
                match_criterion = attrFilter(approach, filter["key"])

                if not match_criterion:
                    # if there is no match, set approach to None and stop iteration
                    matched_approach = None
                    break

            # continue filtering if there is no match
            if not matched_approach:
                continue
            else:   
                yield matched_approach


