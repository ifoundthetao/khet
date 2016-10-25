import unittest

from nose2.tools import params
from .khetDoubleDeflectorPiece import KhetDoubleDeflectorPiece

class Test(unittest.TestCase):

    def testDidReflectWorkProperly(self):
        testCases = self.didReflectWorkProperlyProvider()
        for testCase in testCases:
            expected, orientation, shotDirection = testCase
            piece = KhetDoubleDeflectorPiece(playersPiece = 1, orientation = orientation)

            reflectionDirection = piece.didReflect(shotDirection)
            assert reflectionDirection == expected

    def didReflectWorkProperlyProvider(self):
        #Expected, orientation, shotDirection
        return (
            (1, 0, 0),
            (0, 0, 1),
            (3, 0, 2),
            (2, 0, 3),
            (3, 1, 0),
            (2, 1, 1),
            (1, 1, 2),
            (0, 1, 3),
            (1, 2, 0),
            (0, 2, 1),
            (3, 2, 2),
            (2, 2, 3),
            (3, 3, 0),
            (2, 3, 1),
            (1, 3, 2),
            (0, 3, 3),
        )
        """
        """
