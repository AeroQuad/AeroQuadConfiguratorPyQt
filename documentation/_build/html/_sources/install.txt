Source Code Setup and Installation
==================================

Installation Requirements
-------------------------
- `Python v2.7 <http://python.org/download/releases/2.7.3/>`_
- `PyQt with Qt Designer <http://www.riverbankcomputing.co.uk/software/pyqt/download>`_ (get Binary Package) 
- `Eclipse <http://www.eclipse.org/downloads/>`_ (you'll download PyDev inside Eclipse, I got the C++ version) 
- `PyDev <http://pydev.org/manual_101_install.html>`_ (can execute Python code directly from Eclipse)
- `Setup code completion in Eclipse for PyDev <http://www.saltycrane.com/blog/2007/06/how-to-get-code-completion-for-pyqt/>`_
- `PySerial <http://pyserial.sourceforge.net/pyserial.html#installation>`_ (serial drivers for Python)
- `PyQtGraph <http://www.pyqtgraph.org/>`_
- `NumPy <http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy>`_
- `SciPy <http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy>`_
- `How to setup Git inside of Eclipse <http://www.vogella.com/articles/EGit/article.html>`_
- The GitHub repo is at: https://github.com/AeroQuad/AeroQuadConfiguratorPyQt.git

Configuring Eclipse
-------------------
- Insure c:\\Python27 is in PATH
- Change PyDev - Interpreter from default to python
- Update PyDev - PYTHONPATH -> External Libraries -> pyqtgraph to point to python27
- Follow this link to `hide certain files/folders in the Eclipse project view <http://stackoverflow.com/questions/6137848/eclipse-how-to-hide-custom-files-in-project-explorer>`_
- To run the application, look for AeroQuadConfigurator.py in the project window and double click it to open the file. Then hit the Run button (the green circle with a triangle button pointing to the right) to execute it.

Configuring Visual Studio 2012
------------------------------
- Setup: http://aeroquad.com/showwiki.php?title=Visual+Studio+2012+based+Python+IDE