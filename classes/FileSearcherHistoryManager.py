
class HistoryManager:
    def __init__(this):
        this.__dict__.update({
            'history': []
        })
        this.__store = this.__dict__['history']

    def add_history(this, history):
        if history == None:
            return {
                'status': False,
                'cause': 'history argument is None'
            }
        elif type(history) != dict:
            return {
                'status': False,
                'cause': 'expecting a dictionary argument'
            }
        elif not 'stamp' in history:
            return {
                'status': False,
                'cause': 'expecting argument property: stamp'
            }
        elif not 'keyword' in history:
            return {
                'status': False,
                'cause': 'expecting argument property: keyword'
            }
        else:
            this.__store.update({
                '{}'.format(history.stamp): '{}'.history.keyword
            })
            return {'status': True}
