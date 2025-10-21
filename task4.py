import numpy as np

class NaiveBayesClassifier:
    """
    A Naïve Bayes classifier that assumes conditional independence among features.
    This implementation uses categorical (count-based) probabilities and log probabilities to prevent underflow.
    """
    
    def __init__(self):
        """
        Initialize necessary data structures for the classifier.
        - self.classes: Stores the unique class labels.
        - self.class_counts: A dictionary to count occurrences of each class.
        - self.feature_counts: A dictionary to count occurrences of feature values for each class.
        - self.feature_totals: A dictionary to store total feature occurrences per class.
        """
        self.classes = None  # Stores unique class labels
        self.class_counts = {}  # Dictionary to store class counts
        self.feature_counts = {}  # Dictionary to store feature counts per class
        self.feature_totals = {}  # Dictionary to store total feature occurrences per class

    def fit(self, X, y):
        """
        Train the Naïve Bayes classifier using count-based probabilities.
        Steps:
        1. Identify unique class labels from `y`.
        2. Count occurrences of each class label to compute prior probabilities.
        3. Count occurrences of feature values for each class to compute likelihood probabilities.
        
        :param X: 2D list or numpy array, where each row represents a sample and each column represents a feature.
        :param y: 1D list or numpy array, where each element corresponds to the class label of a sample.
        """
        self.classes = np.unique(y)  # Step 1: Identify unique class labels
        
        for xi, label in zip(X, y):  # Iterate over each sample
            # Step 2: Count class occurrences
            # ...
            
            # Initialize feature count storage for each class if not present
            # ...
            
            # Step 3: Count occurrences of each feature value for each class
            # ...
            pass

    def _class_probability(self, x, c):
        """
        Compute the log probability of class `c` given input sample `x` using Naïve Bayes formula.
        Steps:
        1. Compute the log prior probability of class `c`.
        2. Compute the log likelihood of the input sample `x` given class `c`.
        3. Sum log prior and log likelihood to get the final log probability.
        
        :param x: 1D list or numpy array representing a single sample.
        :param c: Class label for which probability is being computed.
        :return: Computed log probability of `c` given `x`.
        """
        # Step 1: Compute log prior probability log(P(C))
        # log_prior = ...
        
        # Step 2: Compute log likelihood log(P(X|C)) by apply laplace smoothing
        log_likelihood = 0
        # ...
        
        # Step 3: Compute final log probability log(P(C|X)) (ignoring P(X))
        return log_prior + log_likelihood

    def predict(self, X):
        """
        Predict class labels for given input `X`.
        Steps:
        1. Compute the log probability for each class using `_class_probability`.
        2. Choose the class with the highest log probability as the prediction.
        
        :param X: 2D list or numpy array where each row represents a sample.
        :return: 1D numpy array of predicted class labels.
        """
        y_pred = []
        for x in X:
            # Step 1: Compute log probability for each class
            # ...

            # Step 2: Choose the class with the highest probability
            # ...
            pass

        return np.array(y_pred)