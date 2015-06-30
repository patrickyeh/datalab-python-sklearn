__author__ = 'Vetom'

algorithms = [
    {
        'name': 'DecisionTree',
        'module':'DecisionTreeModel',
        'class': 'DecisionTreeModel',
        'description': 'Sklearn decision tree model',
        'require_params': []
    },
    {
        'name': 'Lasso',
        'module':'Lasso',
        'class': 'LassoModel',
        'description': 'Sklearn Lasso',
        'require_params': []
    },
    {
        'name': 'SGDClassifier',
        'module':'SGDClassifier',
        'class': 'SGDClassifier',
        'description': 'Sklearn SGDClassifier',
        'require_params': []
    },
    {
        'name': 'Support Vector Machine',
        'module':'SVM',
        'class': 'SVM',
        'description': 'Sklearn SGDClassifier',
        'require_params': []
    },
]

require_package = ['numpy', 'sklearn']
