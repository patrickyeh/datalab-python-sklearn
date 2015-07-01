__author__ = 'Vetom'

algorithms = [
    {
        'name': 'DecisionTree',
        'module':'DecisionTreeModel',
        'entry_class': 'DecisionTreeModel',
        'description': 'Sklearn decision tree model',
        'require_params': []
    },
    {
        'name': 'Lasso',
        'module':'Lasso',
        'entry_class': 'LassoModel',
        'description': 'Sklearn Lasso',
        'require_params': []
    },
    {
        'name': 'SGDClassifier',
        'module':'SGDClassifier',
        'entry_class': 'SGDClassifier',
        'description': 'Sklearn SGDClassifier',
        'require_params': []
    },
    {
        'name': 'Support Vector Machine',
        'module':'SVM',
        'entry_class': 'SVM',
        'description': 'Sklearn SGDClassifier',
        'require_params': []
    },
]

require_package = ['numpy', 'sklearn']
