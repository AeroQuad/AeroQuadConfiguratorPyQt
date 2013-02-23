Subpanel Class
==============

This class defines commonly needed functions used for all subpanels.  It defaults to looking up a telemetry command in AeroQuadConfigurator.xml and setting up a continuous telemetry stream from the AeroQuad board.  Redefine :py:meth:`~subPanelTemplate.subpanel.start` if you desire different behaviour (such as read telemetry once, or don't read any telemetry at all).

.. autoclass:: subPanelTemplate.subpanel
   :members: