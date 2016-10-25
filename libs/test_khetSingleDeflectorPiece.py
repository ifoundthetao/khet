import unittest

from nose2.tools import params
from .khetSingleDeflectorPiece import KhetSingleDeflectorPiece

class Test(unittest.TestCase):

    def testDidReflectWorkProperly(self):
        testCases = self.didReflectWorkProperlyProvider()
        for testCase in testCases:
            expected, orientation, shotDirection = testCase
            piece = KhetSingleDeflectorPiece(playersPiece = 1, orientation = orientation)

            reflectionDirection = piece.didReflect(shotDirection)
            assert reflectionDirection == expected

    def didReflectWorkProperlyProvider(self):
        #Expected, orientation, shotDirection
        return (
            (False, 0, 0),
            (0,     0, 1),
            (3,     0, 2),
            (False, 0, 3),
            (False, 1, 0),
            (False, 1, 1),
            (1,     1, 2),
            (0,     1, 3),
            (1,     2, 0),
            (False, 2, 1),
            (False, 2, 2),
            (2,     2, 3),
            (3,     3, 0),
            (2,     3, 1),
            (False, 3, 2),
            (False, 3, 3),
        )
