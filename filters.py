"""Provide filters for querying close approaches and limit the generated results.

The `create_filters` function produces a collection of objects that is used by
the `query` method to generate a stream of `CloseApproach` objects that match
all of the desired criteria. The arguments to `create_filters` are provided by
the main module and originate from the user's command-line options.

This function can be thought to return a collection of instances of subclasses
of `AttributeFilter` - a 1-argument callable (on a `CloseApproach`) constructed
from a comparator (from the `operator` module), a reference value, and a class
method `get` that subclasses can override to fetch an attribute of interest from
the supplied `CloseApproach`.

The `limit` function simply limits the maximum number of values produced by an
iterator.

You'll edit this file in Tasks 3a and 3c.
"""
import operator


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""


class AttributeFilter:
    def __init__(self, op, value):
        self.op = op
        self.value = value

    # added additional parameter `attr` that stands for approach attribute
    def __call__(self, approach, attr):
        """Invoke `self(approach)`."""
        return self.op(self.get(approach, attr), self.value)

    @classmethod
    def get(cls, approach, attr):
        """Get an attribute of interest from a close approach.
        
        Concrete subclasses must override this method to get an attribute of
        interest from the supplied `CloseApproach`.

        :param approach: A `CloseApproach` on which to evaluate this filter.
        :return: The value of an attribute of interest, comparable to `self.value` via `self.op`.
        """

        if attr == 'time':
            return approach.time.date()
        elif attr == 'distance':
            return approach.distance
        elif attr == 'velocity':
            return approach.velocity
        elif attr == 'diameter':
            return approach.neo.diameter
        elif attr == 'hazardous':
            return approach.neo.hazardous
        else:
            raise UnsupportedCriterionError

    def __repr__(self):
        return f"{self.__class__.__name__}(op=operator.{self.op.__name__}, value={self.value})"


def create_filters(
        date=None, start_date=None, end_date=None,
        distance_min=None, distance_max=None,
        velocity_min=None, velocity_max=None,
        diameter_min=None, diameter_max=None,
        hazardous=None
):
    # TODO: Decide how you will represent your filters.
    mapped_filters = {
        "date": { "value": date, "op": operator.eq, "key": "time" }, # operator.eq
        "start_date": { "value": start_date, "op": operator.ge, "key": "time" }, # operator.ge
        "end_date": { "value": end_date, "op": operator.le, "key": "time" }, # le(a,b)
        "distance_min": { "value": distance_min, "op": operator.ge, "key": "distance" }, # ge(a,b)
        "distance_max": { "value": distance_max, "op": operator.le, "key": "distance" }, # le(a,b)
        "velocity_min": { "value": velocity_min, "op": operator.ge, "key": "velocity" }, # ge(a,b)
        "velocity_max": { "value": velocity_max, "op": operator.le, "key": "velocity" }, # le(a,b)
        "diameter_min": { "value": diameter_min, "op": operator.ge, "key": "diameter" }, # ge(a,b)
        "diameter_max": { "value": diameter_max, "op": operator.le, "key": "diameter" }, # le(a,b)
        "hazardous": { "value": hazardous, "op": operator.eq, "key": "hazardous" } # operator.eq
    }

    collection_of_filters = []

    for filter_data in mapped_filters.values():
        if filter_data.get("value") is not None:
             collection_of_filters.append(filter_data)

    if not len(collection_of_filters):
        return []
    
    return collection_of_filters


def limit(iterator, n=None):
    """Produce a limited stream of values from an iterator.

    If `n` is 0 or None, don't limit the iterator at all.

    :param iterator: An iterator of values.
    :param n: The maximum number of values to produce.
    :yield: The first (at most) `n` values from the iterator.
    """
    # TODO: Produce at most `n` values from the given iterator.

    if n is None or n == 0:
        for item in iterator: 
            yield item
    else:
        # init counter
        value = 0
        
        for item in iterator:
            if value >= n:
                break

            value += 1    
            yield item
