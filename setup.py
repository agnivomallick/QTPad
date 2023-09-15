from cx_Freeze import setup, Executable
import sys

base = "Win32GUI" if sys.platform == "win32" else None


build_exe_options = {
    "packages": ["PyQt5", "sys", "time"],
    "include_msvcr": True,
    "include_files": [
        'copy.png', 'cut.png', 'exit.jpeg', 'new.png', 
        'open.jpeg', 'paste.jpeg', 'redo.jpeg', 'save.png', 
        'saveas.png', 'splash_grad.jpg', 'splash.ui', 'window.ui', 'qtpad_win_icon.png', 'undo.jpg',
        'qtpad_win_icon.ico'
    ]
}

setup(
    name="QTPad",
    author="Agnivo\'s Software Corporation",
    description="QTPad",
    options = {"build_exe": build_exe_options},
    executables = [
        Executable(
            "QTPad.py",
            base=base,
            target_name="qtpad",
            icon="qtpad_win_icon.ico",
        )
    ]
)