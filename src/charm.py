#!/usr/bin/env python3
import sys

sys.path.append("lib")

from ops.charm import CharmBase
from ops.main import main
from ops.framework import StoredState
from ops.model import (
    ActiveStatus,
    BlockedStatus,
    WaitingStatus,
    MaintenanceStatus,
)


class MyCharm(CharmBase):
    state = StoredState()

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self.on_install)

    def on_install(self, event):
        unit = self.framework.model.unit
        unit.status = ActiveStatus()


if __name__ == "__main__":
    main(MyCharm)

