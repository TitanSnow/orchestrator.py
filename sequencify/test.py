from sequencify import sequencify
from unittest import TestCase

class TestSequencify(TestCase):
    dependencyTree = {
		'a': [],
		'b': ['a'],
		'c': ['a'],
		'd': ['b','c'],
		'e': ['f'],
		'f': ['e'],
		'g': ['g'],
	}

    @staticmethod
    def noop():
        pass

    @staticmethod
    def makeTests(tree):
        tasks = {}
        for p in tree:
            tasks[p] = {
                'name': p,
                'dep': tree[p],
                'fn': TestSequencify.noop,
            }
        return tasks

    @staticmethod
    def theTest(self, source, expected):
        tasks = TestSequencify.makeTests(TestSequencify.dependencyTree)
        actual = sequencify(tasks, source.split(','))
        self.assertEqual(','.join(actual['sequence']), expected)
        self.assertEqual(len(actual['missingTasks']), 0)
        self.assertEqual(len(actual['recursiveDependencies']), 0)

    @staticmethod
    def theTestError(source):
        tasks = TestSequencify.makeTests(TestSequencify.dependencyTree)
        actual = sequencify(tasks, source.split(','))
        return actual

    def test_a2a(self):
        TestSequencify.theTest(self, 'a', 'a')

    def test_aa2a(self):
        TestSequencify.theTest(self, 'a,a', 'a')

    def test_c2ac(self):
        TestSequencify.theTest(self, 'c', 'a,c')

    def test_b2ab(self):
        TestSequencify.theTest(self, 'b', 'a,b')

    def test_cb2acb(self):
        TestSequencify.theTest(self, 'c,b', 'a,c,b')

    def test_bc2abc(self):
        TestSequencify.theTest(self, 'b,c', 'a,b,c')

    def test_ba2ab(self):
        TestSequencify.theTest(self, 'b,a', 'a,b')

    def test_d2abcd(self):
        TestSequencify.theTest(self, 'd', 'a,b,c,d')

    def test_cd2acbd(self):
        TestSequencify.theTest(self, 'c,d', 'a,c,b,d')

    def test_bd2abcd(self):
        TestSequencify.theTest(self, 'b,d', 'a,b,c,d')

    def test_e2recursive(self):
        expectedRecursionList = ['e','f','e']
        actual = TestSequencify.theTestError('e')
        self.assertEqual(len(actual['recursiveDependencies']), 1)
        self.assertEqual(len(actual['recursiveDependencies'][0]), len(expectedRecursionList))
        for i in range(len(expectedRecursionList)):
            self.assertEqual(actual['recursiveDependencies'][0][i], expectedRecursionList[i])

    def test_g2recursive(self):
        expectedRecursionList = ['g', 'g']
        actual = TestSequencify.theTestError('g')
        self.assertEqual(len(actual['recursiveDependencies']), 1)
        self.assertEqual(len(actual['recursiveDependencies'][0]), len(expectedRecursionList))
        for i in range(len(expectedRecursionList)):
            self.assertEqual(actual['recursiveDependencies'][0][i], expectedRecursionList[i])

    def test_h2missing(self):
        actual = TestSequencify.theTestError('h')
        self.assertEqual(actual['missingTasks'], ['h'])

__all__ = ('TestSequencify',)
