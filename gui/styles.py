"""
GUI Styles for Quality Code Checker
Supports Light and Dark themes with toggle
"""

class Styles:
    """Theme manager with light and dark mode support"""
    
    # Color definitions
    LIGHT_THEME = {
        'primary': '#2196F3',
        'primary_hover': '#1976D2',
        'primary_pressed': '#0D47A1',
        
        'background': '#FFFFFF',
        'background_alt': '#F5F5F5',
        'background_panel': '#FAFAFA',
        
        'text': '#212121',
        'text_secondary': '#757575',
        'text_disabled': '#BDBDBD',
        
        'border': '#E0E0E0',
        'border_focus': '#2196F3',
        
        'error': '#F44336',
        'warning': '#FF9800',
        'info': '#2196F3',
        'success': '#4CAF50',
        
        'code_bg': '#F5F5F5',
        'code_text': '#212121',
        'highlight': '#FFF9C4',
        
        'button': '#2196F3',
        'button_hover': '#1976D2',
        'button_text': '#FFFFFF'
    }
    
    DARK_THEME = {
        'primary': '#42A5F5',
        'primary_hover': '#64B5F6',
        'primary_pressed': '#90CAF9',
        
        'background': '#1E1E1E',
        'background_alt': '#252526',
        'background_panel': '#2D2D30',
        
        'text': '#CCCCCC',
        'text_secondary': '#9E9E9E',
        'text_disabled': '#616161',
        
        'border': '#3E3E42',
        'border_focus': '#42A5F5',
        
        'error': '#EF5350',
        'warning': '#FFA726',
        'info': '#42A5F5',
        'success': '#66BB6A',
        
        'code_bg': '#1E1E1E',
        'code_text': '#D4D4D4',
        'highlight': '#515C6A',
        
        'button': '#0E639C',
        'button_hover': '#1177BB',
        'button_text': '#FFFFFF'
    }
    
    @staticmethod
    def get_stylesheet(theme='light'):
        """Get complete QSS stylesheet for the theme"""
        colors = Styles.LIGHT_THEME if theme == 'light' else Styles.DARK_THEME
        
        return f"""
        /* Main Window */
        QMainWindow {{
            background-color: {colors['background']};
            color: {colors['text']};
        }}
        
        /* Panels and Frames */
        QFrame {{
            background-color: {colors['background_panel']};
            border: 1px solid {colors['border']};
            border-radius: 4px;
        }}
        
        QWidget {{
            background-color: {colors['background']};
            color: {colors['text']};
        }}
        
        /* Push Buttons */
        QPushButton {{
            background-color: {colors['button']};
            color: {colors['button_text']};
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: bold;
            min-width: 80px;
        }}
        
        QPushButton:hover {{
            background-color: {colors['button_hover']};
        }}
        
        QPushButton:pressed {{
            background-color: {colors['primary_pressed']};
        }}
        
        QPushButton:disabled {{
            background-color: {colors['background_alt']};
            color: {colors['text_disabled']};
        }}
        
        /* Secondary Button */
        QPushButton[class="secondary"] {{
            background-color: {colors['background_alt']};
            color: {colors['text']};
            border: 1px solid {colors['border']};
        }}
        
        QPushButton[class="secondary"]:hover {{
            background-color: {colors['background_panel']};
        }}
        
        /* Danger Button */
        QPushButton[class="danger"] {{
            background-color: {colors['error']};
        }}
        
        QPushButton[class="danger"]:hover {{
            background-color: #D32F2F;
        }}
        
        /* Text Input */
        QLineEdit, QTextEdit, QPlainTextEdit {{
            background-color: {colors['background_alt']};
            color: {colors['text']};
            border: 1px solid {colors['border']};
            border-radius: 4px;
            padding: 6px;
            selection-background-color: {colors['primary']};
        }}
        
        QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {{
            border: 2px solid {colors['border_focus']};
        }}
        
        /* List Widget */
        QListWidget {{
            background-color: {colors['background_alt']};
            color: {colors['text']};
            border: 1px solid {colors['border']};
            border-radius: 4px;
            padding: 4px;
        }}
        
        QListWidget::item {{
            padding: 4px;
            border-radius: 2px;
        }}
        
        QListWidget::item:selected {{
            background-color: {colors['primary']};
            color: white;
        }}
        
        QListWidget::item:hover {{
            background-color: {colors['background_panel']};
        }}
        
        /* Table Widget */
        QTableWidget {{
            background-color: {colors['background_alt']};
            color: {colors['text']};
            border: 1px solid {colors['border']};
            gridline-color: {colors['border']};
            selection-background-color: {colors['primary']};
        }}
        
        QTableWidget::item {{
            padding: 4px;
        }}
        
        QTableWidget::item:selected {{
            background-color: {colors['primary']};
            color: white;
        }}
        
        QHeaderView::section {{
            background-color: {colors['background_panel']};
            color: {colors['text']};
            padding: 6px;
            border: none;
            border-bottom: 2px solid {colors['border']};
            font-weight: bold;
        }}
        
        /* Tab Widget */
        QTabWidget::pane {{
            border: 1px solid {colors['border']};
            border-radius: 4px;
            background-color: {colors['background_panel']};
        }}
        
        QTabBar::tab {{
            background-color: {colors['background_alt']};
            color: {colors['text_secondary']};
            padding: 8px 16px;
            border: 1px solid {colors['border']};
            border-bottom: none;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            margin-right: 2px;
        }}
        
        QTabBar::tab:selected {{
            background-color: {colors['background_panel']};
            color: {colors['text']};
            border-bottom: 2px solid {colors['primary']};
        }}
        
        QTabBar::tab:hover {{
            background-color: {colors['background_panel']};
        }}
        
        /* Combo Box */
        QComboBox {{
            background-color: {colors['background_alt']};
            color: {colors['text']};
            border: 1px solid {colors['border']};
            border-radius: 4px;
            padding: 6px;
        }}
        
        QComboBox:hover {{
            border: 1px solid {colors['border_focus']};
        }}
        
        QComboBox::drop-down {{
            border: none;
        }}
        
        QComboBox QAbstractItemView {{
            background-color: {colors['background_alt']};
            color: {colors['text']};
            border: 1px solid {colors['border']};
            selection-background-color: {colors['primary']};
        }}
        
        /* Check Box */
        QCheckBox {{
            color: {colors['text']};
            spacing: 6px;
        }}
        
        QCheckBox::indicator {{
            width: 18px;
            height: 18px;
            border: 2px solid {colors['border']};
            border-radius: 3px;
            background-color: {colors['background_alt']};
        }}
        
        QCheckBox::indicator:checked {{
            background-color: {colors['primary']};
            border-color: {colors['primary']};
        }}
        
        /* Progress Bar */
        QProgressBar {{
            background-color: {colors['background_alt']};
            border: 1px solid {colors['border']};
            border-radius: 4px;
            text-align: center;
            color: {colors['text']};
        }}
        
        QProgressBar::chunk {{
            background-color: {colors['primary']};
            border-radius: 3px;
        }}
        
        /* Scroll Bar */
        QScrollBar:vertical {{
            background-color: {colors['background_alt']};
            width: 12px;
            border-radius: 6px;
        }}
        
        QScrollBar::handle:vertical {{
            background-color: {colors['border']};
            border-radius: 6px;
            min-height: 20px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background-color: {colors['text_secondary']};
        }}
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
        
        QScrollBar:horizontal {{
            background-color: {colors['background_alt']};
            height: 12px;
            border-radius: 6px;
        }}
        
        QScrollBar::handle:horizontal {{
            background-color: {colors['border']};
            border-radius: 6px;
            min-width: 20px;
        }}
        
        QScrollBar::handle:horizontal:hover {{
            background-color: {colors['text_secondary']};
        }}
        
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
            width: 0px;
        }}
        
        /* Label */
        QLabel {{
            color: {colors['text']};
            background-color: transparent;
        }}
        
        QLabel[class="title"] {{
            font-size: 16px;
            font-weight: bold;
            color: {colors['text']};
        }}
        
        QLabel[class="subtitle"] {{
            font-size: 12px;
            color: {colors['text_secondary']};
        }}
        
        /* Status Labels */
        QLabel[severity="error"] {{
            color: {colors['error']};
            font-weight: bold;
        }}
        
        QLabel[severity="warning"] {{
            color: {colors['warning']};
            font-weight: bold;
        }}
        
        QLabel[severity="info"] {{
            color: {colors['info']};
            font-weight: bold;
        }}
        
        QLabel[severity="success"] {{
            color: {colors['success']};
            font-weight: bold;
        }}
        
        /* Menu Bar */
        QMenuBar {{
            background-color: {colors['background_panel']};
            color: {colors['text']};
            border-bottom: 1px solid {colors['border']};
        }}
        
        QMenuBar::item {{
            padding: 6px 12px;
            background-color: transparent;
        }}
        
        QMenuBar::item:selected {{
            background-color: {colors['background_alt']};
        }}
        
        QMenu {{
            background-color: {colors['background_panel']};
            color: {colors['text']};
            border: 1px solid {colors['border']};
        }}
        
        QMenu::item {{
            padding: 6px 24px;
        }}
        
        QMenu::item:selected {{
            background-color: {colors['primary']};
            color: white;
        }}
        
        /* Tool Tip */
        QToolTip {{
            background-color: {colors['background_panel']};
            color: {colors['text']};
            border: 1px solid {colors['border']};
            padding: 4px;
        }}
        
        /* Status Bar */
        QStatusBar {{
            background-color: {colors['background_panel']};
            color: {colors['text']};
            border-top: 1px solid {colors['border']};
        }}
        
        /* Splitter */
        QSplitter::handle {{
            background-color: {colors['border']};
        }}
        
        QSplitter::handle:hover {{
            background-color: {colors['primary']};
        }}
        """
    
    @staticmethod
    def get_severity_color(severity: str, theme: str = 'light'):
        """Get color for specific severity level"""
        colors = Styles.LIGHT_THEME if theme == 'light' else Styles.DARK_THEME
        
        severity_map = {
            'error': colors['error'],
            'warning': colors['warning'],
            'info': colors['info'],
            'success': colors['success']
        }
        
        return severity_map.get(severity.lower(), colors['text'])
