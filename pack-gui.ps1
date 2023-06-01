# Activate virtual environment
& ./venv/Scripts/Activate.ps1

# Run PyInstaller
pyinstaller --onedir --noconsole --version-file file_version_info.txt slicer-gui.py --noconfirm

# Remove useless components
Remove-Item ./dist/slicer-gui/PySide6/opengl32sw.dll
Remove-Item ./dist/slicer-gui/PySide6/Qt6Quick.dll
Remove-Item ./dist/slicer-gui/PySide6/Qt6Pdf.dll
Remove-Item ./dist/slicer-gui/PySide6/Qt6Qml.dll
Remove-Item ./dist/slicer-gui/PySide6/Qt6OpenGL.dll
Remove-Item ./dist/slicer-gui/PySide6/Qt6Network.dll
Remove-Item ./dist/slicer-gui/PySide6/QtNetwork.pyd
Remove-Item ./dist/slicer-gui/PySide6/Qt6QmlModels.dll
Remove-Item ./dist/slicer-gui/PySide6/Qt6VirtualKeyboard.dll
Remove-Item -Path ./dist/slicer-gui/PySide6/translations -Recurse

# Compress files
Compress-Archive -Path .\dist\slicer-gui -DestinationPath .\dist\slicer-gui-windows.zip -Force