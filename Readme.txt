You need few modules before running this code.

To download the necessary modules, run this code in a new vs code tab once:
[

import subprocess

def install_if_needed(package):
    try:
        import importlib
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call(["pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

install_if_needed("requests")
install_if_needed("selenium")
install_if_needed("webdriver-manager")
install_if_needed("pytube")
install_if_needed("pyQt5")
install_if_needed("PyQt5.QtWidgets")
install_if_needed("qt_material")

]

(You can alternatively download all the modules in a single command in cmd app: pip install selenium, pytube, webdriver-manager, requests,pyQt5,PyQt5.QtWidgets,qt_material)

(The main code also has this code but in commented form. To download the modules , uncomment this part of the code for once and run it. It will take a while while running for the first time. Comment this part of code when you are running after running for once. Please not that code will still work if you don't comment this part but it will make the code slow.)


(I'm assuming you have python installed in your computer at least. And pip too.)

Point to note: You have to write the location where you want to save your file in the code (code will show you where you have to write it). And then run the code.




