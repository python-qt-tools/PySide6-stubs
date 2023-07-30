import sys


if sys.platform == 'linux' and 0:
    ### To be tested under linux
    from QtDBus import QDBusAbstractInterface, QDBus, QDBusInterface

    iface = QDBusInterface()
    iface.asyncCall(method='toto')
    iface.asyncCall('toto', 1, b'abc', '123')
    iface.call(method='toto')
    iface.call('toto', 1, b'abc', '123')
    iface.call('toto', 1, b'abc', '123')
    iface.call(QDBus.Block, 'toto')
    iface.call(QDBus.Block, 'toto', 1, b'abc', '123')
