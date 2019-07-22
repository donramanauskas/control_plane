
class InfluxDBInterface:

    """
    Code for communicating with Grafana.
    """

    def __init__(self, grafana_data):
        self.grafana_data = grafana_data

    def info(self):
        return self.grafana_data