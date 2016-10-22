# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 03:53:17 2016

@author: tbolton
"""

from .khetPiece import KhetPiece
class KhetBlockerPiece(KhetPiece):
    def __init__(self, playersPiece, orientation = 0):
        super().__init__(playersPiece, orientation)
        """
        We probably don't need "canBlock", but it's descriptive
        """
        self.isBlocker = True
        self.isSwappable = True
        
    def wasShotFatal(self, shotDirection):
        wasBlocked = self.didBlock(shotDirection)
        
        return not wasBlocked

    def didBlock(self, shotDirection):
        # Here's why we have this equation..
        # Orientation table:
        #                               ^
        #                               |
        #  Facing "up"    0             0
        #  Facing "right" 1    <---- 3     1  --->
        #  Facing "down"  2             2
        #  Facing "left"  3             |
        #                               v
        #
        #  So, if a shot comes in from the right (1)
        #  And it hits the right facing "Blocker" head on  (3),
        #  the blocker survives:
        #
        #  SHOT(1)------>     *<--Blocker(3)
        #   3 - 1 = 2
        #
        #
        # If we reverse it, and the blocker is facing left and the shot right:
        #  Blocker(1)-->   <-------SHOT(3)
        #  1 - 3 = -2
        #
        #  If we apply this to top / down we get:
        #                 SHOT(2)
        #                   |
        #                   v
        #                   *
        #                   ^
        #                   |
        #                Blocker(0)
        # 2 - 0 = 2,
        # And the otherway we get, 0 - 2 = -2.
        # So, we take the absolute value, and get 2.  This signals a successful block.

        if abs(shotDirection - self.orientation) == 2:
            return True
        else:
            return False