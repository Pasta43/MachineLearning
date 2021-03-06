from base_predict import Model


class KNN(Model):
    def __init__(self, k):
        """
        Constructor of KNN class
        k - that is the neighbor number
        """
        super().__init__()
        self.neighbours = k
        self.X_train = None
        self.y = None
        
    def fit(self, X, y):
        """
        Fit the model with KNN algorithm
        X - features
        y - target
        """
        self.X_train = X
        self.y = y
        self.classes=self.get_unique_elements(self.y)

    def predict(self, X):
        """
        Predict the labels of the data
        X - features
        """
        prediction = []
        for x in X:
            distances = []
            for x_train in self.X_train:
                distances.append((x_train, self.distance(x, x_train)))
            distances.sort(key=lambda x: x[1])
            k_nearest = distances[:self.neighbours]
            k_nearest_labels = []
            for k in k_nearest:
                k_nearest_labels.append(self.y[self.X_train.index(k[0])])
            prediction.append(self.majority(k_nearest_labels))
        return prediction

    def predict_proba(self, X):
        """
        Predict the probabilities of each class of the data
        X - features
        Returns the probabilities of the data (for each label)
        # """
        prediction = []
        for x in X:
            distances = []
            for x_train in self.X_train:
                distances.append((x_train, self.distance(x, x_train)))
            distances.sort(key=lambda x: x[1])
            k_nearest = distances[:self.neighbours]
            k_nearest_labels = []
            for k in k_nearest:
                k_nearest_labels.append(self.y[self.X_train.index(k[0])])
            prediction.append(self.probability(k_nearest_labels))
        return prediction

    def distance(self, x, x_train=None):
        """
        Calculate the distance between two data
        x - data
        x_train - data
        """
        return sum([(x[i]-x_train[i])**2 for i in range(len(x_train))])

    def majority(self, k_nearest_labels):
        """
        Calculate the majority of the labels
        k_nearest_labels - labels of the k nearest data
        """
        return max(set(k_nearest_labels), key=k_nearest_labels.count)

    def probability(self, k_nearest_labels):
        """
        Calculate the probabilities of the labels of each class
        k_nearest_labels - labels of the k nearest data
        """
        probabilities = []
        for label in self.classes:
            probabilities.append(k_nearest_labels.count(label)/len(k_nearest_labels))
        return probabilities
        
    def get_unique_elements(self, lst):
        """
        Get the unique elements of the list
        lst - list
        """
        a = lst
        b = []
        for i in a:
            if i not in b:
                b.append(i)
        return b
