__author__ = 'Vetom'

algorithms = [
    {
        'name': 'DecisionTree',
        'module':'DecisionTreeModel.py',
        'entry_class': 'DecisionTreeModel',
        'description': 'Sklearn decision tree model',
        'require_params': []
    },
    {
        'name': 'Lasso',
        'module':'Lasso.py',
        'entry_class': 'LassoModel',
        'description': 'Sklearn Lasso',
        'require_params': []
    },
    {
        'name': 'SGDClassifier',
        'module':'SGDClassifier.py',
        'entry_class': 'SGDClassifierModel',
        'description': 'Sklearn SGDClassifier',
        'require_params': []
    },
    {
        'name': 'Support Vector Machine',
        'module':'SVM.py',
        'entry_class': 'SVM',
        'description': 'Sklearn SGDClassifier',
        'require_params': []
    },
]

require_package = ['numpy', 'sklearn']
