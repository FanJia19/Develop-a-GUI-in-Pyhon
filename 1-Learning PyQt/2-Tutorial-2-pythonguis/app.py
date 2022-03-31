############################################################################################
################################ 1-1- Creating an application ##############################
#
# from PyQt5.QtWidgets import QApplication, QWidget
# # First, we import the PyQt classes that we need for the application. Here we're importing
# # QApplication = the application handler, and QWidget = a basic empty GUI widget, both from the
# # QtWidgets module. The main modules of Qt are QtWidgets, QtGui and QtCore.
# import sys  # Only needed for access to command line arguments
#
# app = QApplication(sys.argv)
# # You need one (and only one) QApplication instance per application.
# # Pass in sys.argv, which is Python list containing the command line arguments passed to the
# # application, to allow command line arguments for your app.
# # If you know you won't use command line arguments QApplication([]) works too.
#
# window = QWidget()
# # Create a Qt widget, which will be our window. In Qt all top level widgets are windows --
# # that is, they don't have a parent and are not nested within another widget or layout.
# # This means you can technically create a window using any widget you like.

# window.show()
# # IMPORTANT!!!!! Widgets (here the "window" Vr) without a parent are invisible by default.
# # So, after creating the window object, we must always call .show() to make it visible.
# # You can remove the .show() and run the app, but you'll have no way to quit it!
#
# app.exec()
# # Start the event loop. In PyQt5 you can also use app.exec_(). This was a legacy feature
# # avoid a clash with the exec reserved word in Python 2.
#
# # ----------------
# # Your application won't reach here until you exit and the event loop has stopped.
# # Run it! You will now see your window. Qt automatically creates a window with the normal
# # window decorations, and you can drag it around and resize it like any window.




################################ 1-2- Event Loop ##############################
# app = QApplication(sys.argv)
# The core of every Qt Applications is the QApplication class. Every application needs one
# — and only one — QApplication object to function. This object holds the event loop of
# your application — the core loop which governs all user interaction with the GUI.
#
# Each interaction with your application — whether a press of a key, click of a mouse, or mouse
# movement — generates an event which is placed on the event queue. In the event loop, the
# queue is checked on each iteration and if a waiting event is found, the event and control
# is passed to the specific event handler for the event. The event handler deals with the event,
# then passes control back to the event loop to wait for more events. There is only one running
# event loop per application.Your application sits waiting in the event loop until an action is
# taken - There is only one event loop running at any time




################################ 1-3- QMainWindow ##############################
# As we discovered in the last part, in Qt any widgets can be windows. For example, if you
# replace QtWidget with QPushButton. In the example below, you would get a window with a single
# push-able button in it.

# import sys
# from PyQt5.QtWidgets import QApplication, QPushButton
#
# app = QApplication(sys.argv)
#
# window = QPushButton("Push Me")
# window.show()
#
# app.exec()

# As we'll discover later, the ability to nest widgets within other widgets using layouts means
# you can construct complex UIs inside an empty QWidget.

# ------------
# But, Qt already has a solution for you -- the QMainWindow. This is a pre-made widget which
# provides a lot of standard window features you'll use in your apps, including toolbars,
# menus, a statusbar, dockable widgets and more. We'll look at these advanced features later,
# but for now, we'll add a simple empty QMainWindow to our application.

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()
# app.exec()

# Run it! You will now see your main window. It looks exactly the same as before!
# So our QMainWindow isn't very interesting at the moment.

# ------------
# We can fix that by adding some content. If you want to create a custom window, the best
# approach is to subclass QMainWindow and then include the setup for the window in the
# __init__ block. This allows the window behavior to be self-contained. We can add our own
# subclass of QMainWindow — call it MainWindow to keep things simple.

import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    # Inherit from superclass 'QMainWindow' to create and
    # customize subclass 'MainWindow' which is your application's main window
    def __init__(self):  # self = QMainWindow
        super().__init__()
        # About 'super()': https://realpython.com/python-super/
        # When you make a subclass from a Qt class you must always call the super __init__
        # function to allow Qt to set up the object.

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        # For this demo we're using a QPushButton. The core Qt widgets are always imported
        # from the QtWidgets namespace, as are the QMainWindow and QApplication classes.

        self.setCentralWidget(button)
        # Set the central widget of the Window. When using QMainWindow we use .setCentralWidget
        # to place a widget (here a QPushButton) in the QMainWindow -- by default it takes the
        # whole of the window.


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# In our '__init__' block we first use '.setWindowTitle()' to change the title of our main window.
# Then we add our first widget — a 'QPushButton' — to the middle of the window. This is one of
# the basic widgets available in Qt. When creating the button you can pass in the text that you
# want the button to display. Finally, we call '.setCentralWidget()' on the window. This is a
# 'QMainWindow' specific function that centers the widget in the middle of the window.




################################# 1-4- Sizing windows and widgets ##############################
# The window is currently freely resizable -- While it's good to let your users resize your
# applications, sometimes you may want to place restrictions on minimum or maximum sizes,
# or lock a window to a fixed size.

# import sys
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# # Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press Me!")
#
#         self.setFixedSize(QSize(400, 300))
#         # In Qt sizes are defined using a 'QSize' object. This accepts '(width, height)'
#         # parameters in that order. As well as .setFixedSize() you can also call
#         # '.setMinimumSize()' and '.setMaximumSize()' to set the minimum and maximum sizes
#         # respectively. Experiment! You can use these size methods on any widget.
#
#         self.setCentralWidget(button)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()

# Run it! You will see a fixed size window -- try and resize it, it won't work. control is disabled
# on Windows & Linux. On macOS, you can maximize the app to fill the screen, but the central widget
# will not resize.




############################################################################################
################################## 2-1- Signals & Slots ####################################
# What we need is a way to connect the action of pressing the button to making something happen.
# In Qt, this is provided by 'signals' and 'slots' or events.

# 【Signals】are notifications emitted by widgets when something happens. That something can be any
# number of things, from pressing a button, to the text of an input box changing, to the text of
# the window changing. Many signals are initiated by user action, but this is not a rule.
# In addition to notifying about something happening, signals can also send data to provide
# additional context about what happened.
# You can also create your own custom signals, which we'll explore later.

# 【Slots】is the name Qt uses for the "receivers of signals". In Python any function (or method)
# in your application can be used as a slot -- simply by connecting the signal to it. If the signal
# sends data, then the receiving function will receive that data too. Many Qt widgets also have
# their own built-in slots, meaning you can hook Qt widgets together directly.

# EXAMPLE:
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press Me!")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         # hook up the button to a customized Python method.
#
#         self.setCentralWidget(button)
#
#     def the_button_was_clicked(self):
#         print("The Button was Clicked!")
#         # Here we create a simple custom slot named the_button_was_clicked which accepts
#         # the clicked signal from the QPushButton.
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()
