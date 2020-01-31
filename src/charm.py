import sys
sys.path.append('lib')

from ops.charm import CharmBase
from ops.main import main

class MyCharm(CharmBase):
    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.start, self.on_start)

     def on_start(self, event):
        print("\n\n\n\nhello charm\n\n\n\n")


if __name__ == "__main__":
    main(MyCharm)

