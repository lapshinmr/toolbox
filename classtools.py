import datetime
import inspect
"""
Different tools for working with classes
"""


class AttrDisplay:
    def gather_atrrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gather_atrrs())


class ListInstanse:
    """
    Class for improved __str__ method. Print all attribures.
    """
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result


class LogWriter:
    def log_writer(self, add_info, mode='a'):
        print(add_info)
        log_file = open(self.log_name, mode)
        log_file.write("%s %s\n%s\n" % (
            datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            inspect.stack()[1][3],
            '=' * 80))
        log_file.write("%s\n\n" % add_info)
        log_file.close()


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = SubTest(), TopTest()
    print(X)
    print(Y)
