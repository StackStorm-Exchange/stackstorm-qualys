from qualysapi.connector import QGConnector
from parsers import ResultSets
from st2common.runners.base_action import Action

__all__ = [
    'QualysBaseAction',
]


class QualysBaseAction(Action):
    def __init__(self, config):
        super(QualysBaseAction, self).__init__(config)
        self.connection = QGConnector(
            (config['username'],
             config['password']),
            config['hostname']
        )
        self.resultsets = ResultSets()
