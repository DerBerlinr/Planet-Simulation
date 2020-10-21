from gui import *


class Main:

#-------------init-------------

    def __init__(self): #init
        gui = GUI()

    def get_first_pos(self,pos): #erhaelt die ersten Positionen der Planenten aus der Tabelle
        gui.data[0]

#-------------reset-------------

    def adjusted_data(self): #File löschen um Zugriff auf flasche Daten zu verhindern
        pass

#-------------calculation-------------

    def calc(self,amount=1): #berechnet naechste Positionen
        pass

#-------------time-------------

    def calc_next_pos(self): #errechnet naechste Planeten Positionen
        pass

#-------------time-jumping-------------

    def get_pos_time_f(self, time): #Holt Positionen für Zeiten in der Zukunft (vorspulen)
        pass

    def get_pos_time_p(self, time): #Holt Positionen für Zeiten in der Zukunft (zurueckspulen)
        pass

#-------------button-usage and user-entries-------------

    def start(self): #startet die Simulation
        pass

    def pause(self): #pausiert die Simulation
        pass

    def speed_up(self): #erhöht Geschwindigkeit der Simulation
        pass

    def speed_down(self): #verringert Geschwindigkeit der Simulation
        pass

    def get_display_data(self): #liest Daten aus und leitet an GUI weiter zur dortigen visuellen Darstellung
        pass
