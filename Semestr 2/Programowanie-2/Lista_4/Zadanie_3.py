from matplotlib import pyplot as plt
from spyre import server
from scipy.integrate import odeint
import Zadanie_1
import numpy as np


class SEIR_App(server.App):
    """
    Tworzymy klasę SEIR_App
    """
    # Nadajemy tytuł nagłówka głównego na stronie
    title = "Model SEIR"
    inputs = [
        {   # Tworzymy suwaki do poszczególnych wielkości
            "type": "slider",
            "label": "Wielkość populacji",
            "min": 100, "max": 5000, "value": 1000,
            "key": "slider_1",
            "action_id": "plot"

        }, {
            "type": "slider",
            "label": "Suspectible",
            "min": 100, "max": 5000, "value": 999,
            "key": "slider_2",
            "action_id": "plot"
        }, {
            "type": "slider",
            "label": "Exposed",
            "min": 0, "max": 100, "value": 1,
            "key": "slider_3",
            "action_id": "plot"
        }, {
            "type": "slider",
            "label": "Infected",
            "min": 0, "max": 100, "value": 0,
            "key": "slider_4",
            "action_id": "plot"
        }, {
            "type": "slider",
            "label": "Recovered",
            "min": 0, "max": 100, "value": 0,
            "key": "slider_5",
            "action_id": "plot"
        }, {
            "type": "slider",
            "label": "Wskaźnik infekcji",
            "min": 0.0, "max": 10.0, "step": 0.01, "value": 1.34,
            "key": "slider_6",
            "action_id": "plot"
        }, {
            "type": "slider",
            "label": "Wskaźnik inkubacji",
            "min": 0.0, "max": 10.0, "step": 0.01, "value": 0.19,
            "key": "slider_7",
            "action_id": "plot"
        }, {
            "type": "slider",
            "label": "Wskaźnik wyzdrowień",
            "min": 0.0, "max": 10.0, "step": 0.01, "value": 0.34,
            "key": "slider_8",
            "action_id": "plot"
        },{
            "type": "slider",
            "label": "Czas",
            "min": 0.0, "max": 500, "step": 1, "value": 100,
            "key": "slider_9",
            "action_id": "plot"
        },
    ]

    outputs = [{
        "type": "plot",
        "id": "plot"
    }
    ]

    def getPlot(self, params):
        """
        :param params: Parametry zadane na suwakach (jeśli użytkownik nie zmieni wartości początkowych na suwakach to
        program zadziała od początkowo zadanych wartości :return: Wykres, na którym pokazana będzie liczba osób
        podatnych, narażonych, zainfekowanych i wyzdrowiałych, w zależności od czasu
        """
        # Tworzymy tuple z parametrów zadanych na suwakach
        x_p = int(params['slider_2']), int(params['slider_3']), int(params['slider_4']), int(params['slider_5'])
        argumenty = float(params['slider_6']), float(params['slider_7']), float(params['slider_8'])

        # tworzymy tablicę, korzystając z pakietu numpy, która próbkuje nam czas co 1
        t = np.linspace(0, int(params['slider_9']), int(params['slider_9']+1))
        # korzystamy z pakietu odeint do rozwiązywania równań różniczkowych i wprowadzamy potrzebne dane
        # (Funkcja SEIR_model pochodzi z Zadania_1)
        wynik = odeint(Zadanie_1.SEIR_model, x_p, t, args=argumenty)

        # Tworzymy wykres
        fig = plt.figure()

        splt = fig.add_subplot(1, 1, 1)
        splt.plot(t, wynik[:, 0])
        splt.plot(t, wynik[:, 1])
        splt.plot(t, wynik[:, 2])
        splt.plot(t, wynik[:, 3])
        splt.set_xlabel("Czas")
        splt.set_ylabel("Liczba populacji")
        splt.set_title("Model SEIR")
        splt.legend(["Suspectible", "Exposed", "Infected", "Recovered"], loc="best")

        return fig


if __name__ == '__main__':
    app = SEIR_App()
    app.launch(port=9097)
