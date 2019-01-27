import wx

from gooey.gui import formatters
from gooey.gui.components.widgets.bases import TextContainer
from gooey.gui.lang.i18n import _
from gooey.gui.util import wx_util

class SpinControl(TextContainer):

    def getWidget(self, parent, *args, **options):
        return wx.SpinCtrl(
            parent=parent,
            style=wx.SP_ARROW_KEYS,
            min=self._options.get('min', 0),
            max=self._options.get('max', 100),
            initial=self._options.get('initial', 50),
            value=self._options.get('value', '')
        )

    def getWidgetValue(self):
        return str(self.widget.GetValue())

    def formatOutput(self, metadata, value):
        return formatters.general(metadata, value)

class SpinControlDouble(TextContainer):

    def getWidget(self, parent, *args, **options):

        return wx.SpinCtrlDouble(
            parent=parent,
            style=wx.SP_ARROW_KEYS,
            min=self._options.get('min', 0.0),
            max=self._options.get('max', 100.0),
            initial=self._options.get('initial', 0.0),
            inc=self._options.get('inc', 1.0),
            value=self._options.get('value', '')
        )

    def getWidgetValue(self):
        return str(self.widget.GetValue())

    def formatOutput(self, metadata, value):
        return formatters.general(metadata, value)