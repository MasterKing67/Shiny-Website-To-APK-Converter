"""
Shiny Website To APK Converter
GUI

Author: Shiny Studios
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shiny Website To APK Converter")
        self.resize(700, 500)

        self.setup_ui()
        self.apply_style()

    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.setSpacing(15)

        # -----------------------------
        # Title
        # -----------------------------
        title = QLabel("🌐 Shiny Website To APK Converter")
        title.setObjectName("title")
        layout.addWidget(title)

        # -----------------------------
        # Website Settings
        # -----------------------------
        website_box = QGroupBox("Website")

        website_layout = QVBoxLayout()

        website_layout.addWidget(QLabel("Website URL"))
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://example.com")
        website_layout.addWidget(self.url_input)

        website_box.setLayout(website_layout)
        layout.addWidget(website_box)

        # -----------------------------
        # App Settings
        # -----------------------------
        app_box = QGroupBox("Application")

        app_layout = QVBoxLayout()

        app_layout.addWidget(QLabel("App Name"))
        self.app_name = QLineEdit()
        self.app_name.setPlaceholderText("My Website")
        app_layout.addWidget(self.app_name)

        app_layout.addWidget(QLabel("Package Name"))
        self.package_name = QLineEdit()
        self.package_name.setPlaceholderText("com.shiny.myapp")
        app_layout.addWidget(self.package_name)

        app_box.setLayout(app_layout)
        layout.addWidget(app_box)

        # -----------------------------
        # Icon
        # -----------------------------
        icon_box = QGroupBox("Application Icon")

        icon_layout = QHBoxLayout()

        self.icon_path = QLineEdit()
        self.icon_path.setPlaceholderText("Choose an icon...")

        browse_icon = QPushButton("Browse")
        browse_icon.clicked.connect(self.choose_icon)

        icon_layout.addWidget(self.icon_path)
        icon_layout.addWidget(browse_icon)

        icon_box.setLayout(icon_layout)
        layout.addWidget(icon_box)

        # -----------------------------
        # Output Folder
        # -----------------------------
        output_box = QGroupBox("Output Folder")

        output_layout = QHBoxLayout()

        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("Choose output folder...")

        browse_output = QPushButton("Browse")
        browse_output.clicked.connect(self.choose_output)

        output_layout.addWidget(self.output_path)
        output_layout.addWidget(browse_output)

        output_box.setLayout(output_layout)
        layout.addWidget(output_box)

        # -----------------------------
        # Generate Button
        # -----------------------------
        self.generate_button = QPushButton("🚀 Generate Android Project")
        self.generate_button.clicked.connect(self.generate_project)

        layout.addWidget(self.generate_button)

    # ---------------------------------

    def choose_icon(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Choose Icon",
            "",
            "Images (*.png *.jpg *.jpeg *.ico)"
        )

        if file:
            self.icon_path.setText(file)

    # ---------------------------------

    def choose_output(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Choose Output Folder"
        )

        if folder:
            self.output_path.setText(folder)

    # ---------------------------------

    def generate_project(self):
        QMessageBox.information(
            self,
            "Coming Soon",
            "The project generator will be added next!"
        )

    # ---------------------------------

    def apply_style(self):
        self.setStyleSheet("""
        QMainWindow {
            background: #1E1E1E;
        }

        QLabel {
            color: white;
            font-size: 11pt;
        }

        #title {
            font-size: 20pt;
            font-weight: bold;
            color: #4DA3FF;
        }

        QGroupBox {
            color: white;
            border: 1px solid #3A3A3A;
            border-radius: 8px;
            margin-top: 8px;
            padding: 10px;
            font-weight: bold;
        }

        QLineEdit {
            background: #2B2B2B;
            color: white;
            border: 1px solid #555;
            border-radius: 5px;
            padding: 8px;
        }

        QPushButton {
            background: #2D89EF;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px;
            font-weight: bold;
        }

        QPushButton:hover {
            background: #409EFF;
        }

        QPushButton:pressed {
            background: #1B6EC2;
        }
        """)
