#-------------------------------------------------
#
# Project created by QtCreator 2014-05-28T14:49:02
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = BeamProfiler
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    setup.cpp \
    cameraview.cpp

HEADERS  += mainwindow.h \
    setup.h \
    cameraview.h

FORMS    += mainwindow.ui \
    setup.ui \
    cameraview.ui
