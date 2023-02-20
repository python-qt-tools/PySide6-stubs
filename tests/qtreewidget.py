from typing import Optional

from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem

t = QTreeWidget()
topItem = t.topLevelItem(400)

item = QTreeWidgetItem(t, ['abc'])

# it should be possible to remove the item widget for an item
t.setItemWidget(item, 0, None)

# default type returned by topLevelItem() should allow None value
topItem = None

