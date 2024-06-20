import platform

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QLabel, QProgressBar, QVBoxLayout


from .options import OptionsLayout
from .display import Display
from .status import StatusBar


class Layout(QVBoxLayout):
    """Main layout, which is a simple vertical stack.

    Only the layout, content, and appearance are defined here and in the various custom
    objects the layout contains, but not the behaviour (e.g. what happens when something
    is clicked or changed.)
    """

    def __init__(self, resource_directory, config):
        super().__init__()
        self.add_elements(resource_directory, config)

    def add_elements(self, resource_directory, config):
        # Title and version info header
        with open(resource_directory / "version.txt", encoding="utf-8") as f:
            version_info = "".join(f.readlines()[:5])
        version_box = QLabel(version_info)
        version_box.setAlignment(Qt.AlignHCenter)
        self.addWidget(version_box)

        # All the user-configurable options
        self.opts = OptionsLayout(config)
        self.addLayout(self.opts)

        # Status bar to inform user of the current stage of a check
        self.status_bar = StatusBar()
        self.addWidget(self.status_bar)

        # Alias start and cancel buttons to save changing many references to them
        self.start_check_button = self.status_bar.start_button
        self.interrupt_button = self.status_bar.cancel_button

        # Progress bar for check
        self.prog_bar = QProgressBar()
        self.prog_bar.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        if platform.system() == "Windows" and platform.release() == "11":
            # Looks bad (with initial Qt Win11 theme at least) so disable text
            self.prog_bar.setTextVisible(False)
        self.addWidget(self.prog_bar)

        # Box to display output of check function (list of copied spectra)
        self.display = Display()
        self.addWidget(self.display)

        # Extra notification that spectra have been found, dismissable
        self.notification = QPushButton()
        self.notification.hide()
        self.addWidget(self.notification)
