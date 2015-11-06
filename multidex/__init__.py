import operator


class MultiIndexBase(dict):
    """
    Add find method, also update indexes on adding or deleting item
    """
    def __delitem__(self, key):
        item = self[key]
        super(MultiIndexIndexBase, self).__delitem__(key)
        self.__deindex_item__(item)

    def __setitem__(self, key, value):
        super(MultiIndexBase, self).__setitem__(key, value)
        self.__index_item__(value)
        
    def find(self, name, value):
        """
        return sequence of all matching items
        """
        index = getattr(self, '__%s_index__' % name)
        return tuple(index.get(value, []))
        
class MultiIndex(type):
    """
    Metaclass enables instance methods to be used as handlers.
    """
    def __new__(meta, name, bases, dct):
        # Ideally the indexes would be weakrefdicts but
        # str cannot be used in them
        try:
            alt_indexes = dct.pop("alt_indexes")
            for name, getter in alt_indexes.items():
                dct['__%s_index__' % name] = {}

            def __index_item__(self, item):
                for name, getter in alt_indexes.items():
                    index = dct['__%s_index__' % name]
                    
                    key = getter(item)
                    items = index.get(key)
                    if items is None:

                        items = {item}
                        index[key] = items
                    else:
                        items.add(item)
                        
            def __deindex_item__(self, item):
                for name, getter in alt_indexes.items():
                    index = dct['__%s_index__' % name]
                    
                    key = getter(item)
                    items = index.get(key)
                    if items is not None:
                        items.remove(item)
                        if not items:
                            del index[key]

            
            dct['__deindex_item__'] = __deindex_item__
            dct['__index_item__'] = __index_item__
        except IndexError:
            raise ValueError("Missing alt_indexes")
        
        bases = (MultiIndexBase,) + bases
        return super(MultiIndex, meta).__new__(meta, name, bases, dct)
    
    def __init__(cls, name, bases, dct):
        super(MultiIndex, cls).__init__(name, bases, dct)
