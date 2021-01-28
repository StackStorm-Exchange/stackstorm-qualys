from qualysapi.connector import QGConnector

from st2common.runners.base_action import Action

from lib.parsers import ResultSets

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
