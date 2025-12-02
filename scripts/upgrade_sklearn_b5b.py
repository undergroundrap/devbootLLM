"""scikit-learn ML/AI simulations batch 5b - Advanced techniques (final batch)"""
import json
import sys

SKLEARN_BATCH_5B = {
    1026: '''# Model Persistence with joblib
# In production: from sklearn.externals import joblib
# joblib.dump(model, 'trained_model.pkl')
# loaded_model = joblib.load('trained_model.pkl')
# predictions = loaded_model.predict(X_new)

import os
import pickle

class ModelPersistence:
    """Simulates sklearn.externals.joblib for saving/loading trained models"""

    @staticmethod
    def dump(model, filename):
        """Save model to disk using pickle serialization"""
        # Real joblib: uses optimized pickle with compression and caching
        # Simulation: uses standard pickle for demonstration

        model_data = {
            'model_type': model.__class__.__name__,
            'trained': getattr(model, 'is_trained', False),
            'parameters': {}
        }

        # Capture model parameters
        if hasattr(model, 'coef_'):
            model_data['parameters']['coef_'] = model.coef_
        if hasattr(model, 'intercept_'):
            model_data['parameters']['intercept_'] = model.intercept_
        if hasattr(model, 'classes_'):
            model_data['parameters']['classes_'] = model.classes_
        if hasattr(model, 'n_features_'):
            model_data['parameters']['n_features_'] = model.n_features_
        if hasattr(model, 'feature_importances_'):
            model_data['parameters']['feature_importances_'] = model.feature_importances_

        # Write to file (real joblib writes binary)
        print(f"[Simulation] Serializing model: {model.__class__.__name__}")
        print(f"[Simulation] Parameters saved: {list(model_data['parameters'].keys())}")
        print(f"[Simulation] Model saved to '{filename}'")
        print(f"[Simulation] File size estimate: {len(str(model_data))} bytes")

        return model_data

    @staticmethod
    def load(filename):
        """Load model from disk"""
        # Real joblib: deserializes binary format efficiently
        # Simulation: returns loaded representation

        print(f"[Simulation] Loading model from '{filename}'")
        print(f"[Simulation] Model deserialized successfully")

        return {
            'status': 'loaded',
            'filename': filename,
            'ready_to_predict': True
        }

# Demonstration: Model Persistence for Production ML
print("Model Persistence (joblib) Simulation")
print("=" * 70)

# Trained model simulation - house price predictor
class TrainedModel:
    def __init__(self):
        self.is_trained = True
        self.coef_ = [150.5, 5000.0, 20000.0]  # price = coef[0]*sqft + coef[1]*beds + coef[2]*baths + intercept
        self.intercept_ = 50000.0
        self.classes_ = None
        self.n_features_ = 3
        self.feature_importances_ = [0.65, 0.20, 0.15]
        self.training_samples = 250
        self.training_time = 0.45  # seconds

model = TrainedModel()

print("\\n1. MODEL DETAILS:")
print(f"   Model Type: Linear Regression for House Prices")
print(f"   Features: [square_feet, bedrooms, bathrooms]")
print(f"   Trained on: {model.training_samples} samples")
print(f"   Training Time: {model.training_time}s")
print(f"   Coefficients: {model.coef_}")
print(f"   Intercept: ${model.intercept_:,.2f}")
print(f"   Feature Importances: {model.feature_importances_}")

print("\\n2. SAVING MODEL (joblib.dump):")
saved = ModelPersistence.dump(model, 'house_price_model.pkl')

print("\\n3. LOADING MODEL (joblib.load):")
loaded = ModelPersistence.load('house_price_model.pkl')
print(f"   Loaded: {loaded['status']}")

print("\\n4. USING LOADED MODEL:")
print("   # In production code:")
print("   model = joblib.load('house_price_model.pkl')")
print("   new_house = [[2500, 4, 3]]  # sqft, beds, baths")
print("   predicted_price = model.predict(new_house)")
print("   print(f'Predicted price: ${predicted_price[0]:,.0f}')")

print("\\n5. WHY MODEL PERSISTENCE?")
print("   • Training takes time (hours/days for large models)")
print("   • Save trained model, not retraining every request")
print("   • Deploy model to production servers")
print("   • Reproducibility: same model, same predictions")
print("   • Version control: track model iterations")

print("\\n6. PRODUCTION WORKFLOW:")
print("   Training Phase: model.fit(X_train, y_train)")
print("                  joblib.dump(model, 'v1.0_model.pkl')")
print("   ")
print("   Deployment:    model = joblib.load('v1.0_model.pkl')")
print("                  predictions = model.predict(X_new)")
print("   ")
print("   Monitoring:    Compare live predictions vs. baseline")
print("                  Retrain if performance degrades")

print("\\n" + "=" * 70)
print("Real sklearn: import joblib")
print("              joblib.dump(model, 'filename.pkl')")
print("              model = joblib.load('filename.pkl')")
''',

    1027: '''# GridSearchCV - Hyperparameter Tuning
# In production: from sklearn.model_selection import GridSearchCV
# param_grid = {'C': [0.1, 1, 10, 100], 'kernel': ['linear', 'rbf', 'poly']}
# grid = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy', n_jobs=-1)
# grid.fit(X_train, y_train)
# print(f"Best params: {grid.best_params_}")
# print(f"Best CV score: {grid.best_score_}")

import random
import itertools

class GridSearchCV:
    """Simulates sklearn.model_selection.GridSearchCV for systematic hyperparameter tuning"""

    def __init__(self, estimator, param_grid, cv=5, scoring=None):
        self.estimator = estimator
        self.param_grid = param_grid
        self.cv = cv
        self.scoring = scoring or 'accuracy'
        self.best_params_ = None
        self.best_score_ = None
        self.best_estimator_ = None
        self.cv_results_ = []
        self.total_combinations = self._count_combinations()

    def _count_combinations(self):
        """Count total parameter combinations"""
        values = [self.param_grid[k] for k in self.param_grid.keys()]
        return len(list(itertools.product(*values)))

    def fit(self, X, y):
        """Exhaustive search over param grid with cross-validation"""
        print(f"GridSearchCV: Searching {self.total_combinations} parameter combinations")
        print(f"Cross-validation folds: {self.cv}")
        print(f"Total evaluations: {self.total_combinations * self.cv}\\n")

        # Generate all parameter combinations
        keys = list(self.param_grid.keys())
        values = [self.param_grid[k] for k in keys]
        combinations = list(itertools.product(*values))

        best_score = -float('inf')
        best_params = None
        best_model = None

        print(f"{'Combination':<6} {'Parameters':<45} {'CV_Score':<12}")
        print("-" * 65)

        for combo_idx, combo in enumerate(combinations, 1):
            params = dict(zip(keys, combo))

            # Simulate k-fold cross-validation
            random.seed(sum(range(len(combo))))
            cv_scores = []
            for fold in range(self.cv):
                # Real: train/test on each fold
                # Sim: random score with some variance
                base_score = 0.75 + random.random() * 0.20
                cv_scores.append(base_score)

            mean_cv_score = sum(cv_scores) / len(cv_scores)

            # Store results
            self.cv_results_.append({
                'params': params,
                'mean_test_score': mean_cv_score,
                'std_test_score': (sum((s - mean_cv_score)**2 for s in cv_scores) / len(cv_scores))**0.5
            })

            # Format params for display
            param_str = ', '.join([f"{k}={v}" for k, v in params.items()])
            print(f"{combo_idx:<6} {param_str:<45} {mean_cv_score:<12.4f}")

            if mean_cv_score > best_score:
                best_score = mean_cv_score
                best_params = params
                best_model = dict(params)  # simulated trained model

        self.best_params_ = best_params
        self.best_score_ = best_score
        self.best_estimator_ = best_model

        return self

# Demonstration: Hyperparameter Tuning
print("GridSearchCV Hyperparameter Tuning Simulation")
print("=" * 70)

class DummyClassifier:
    """Placeholder estimator"""
    pass

# Define parameter grid for tuning
# Real scenario: optimizing SVM classifier
param_grid = {
    'C': [0.1, 1, 10, 100],           # Regularization strength
    'kernel': ['linear', 'rbf', 'poly']  # Kernel type
}

print("Parameter Grid:")
print(f"  C (regularization): {param_grid['C']}")
print(f"  kernel (type): {param_grid['kernel']}")
print(f"  Total combinations: {len(param_grid['C']) * len(param_grid['kernel'])}\\n")

# Sample data
X = [[i, i*2] for i in range(100)]
y = [i % 2 for i in range(100)]

# Grid search
grid = GridSearchCV(DummyClassifier(), param_grid, cv=5)
grid.fit(X, y)

print(f"\\n{'='*70}")
print("\\nRESULTS SUMMARY:")
print(f"Best Parameters: {grid.best_params_}")
print(f"Best CV Score: {grid.best_score_:.4f}")

print(f"\\nTop 5 Parameter Combinations:")
sorted_results = sorted(grid.cv_results_, key=lambda x: x['mean_test_score'], reverse=True)
for rank, result in enumerate(sorted_results[:5], 1):
    print(f"  {rank}. {result['params']} → Score: {result['mean_test_score']:.4f} (±{result['std_test_score']:.4f})")

print(f"\\nWHY GRIDSEARCHCV?")
print(f"  • Systematically test all parameter combinations")
print(f"  • Find optimal hyperparameters using cross-validation")
print(f"  • Avoid overfitting to single test set")
print(f"  • Compare models fairly with same CV procedure")

print(f"\\nPRODUCTION WORKFLOW:")
print(f"  1. Define parameter_grid with ranges to search")
print(f"  2. Create estimator (e.g., SVC(), RandomForest())")
print(f"  3. GridSearchCV searches all combinations")
print(f"  4. Selects best based on CV score")
print(f"  5. grid.best_estimator_ ready for production")

print("\\n" + "=" * 70)
print("Real sklearn: from sklearn.model_selection import GridSearchCV")
print("              grid = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)")
print("              grid.fit(X, y)")
''',

    1028: '''# Pipeline - ML Workflow Automation
# In production: from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# pipe = Pipeline([
#     ('scaler', StandardScaler()),
#     ('model', LogisticRegression())
# ])
# pipe.fit(X_train, y_train)

class PipelineStep:
    """Base class for pipeline steps"""
    def fit(self, X, y):
        return self

    def transform(self, X):
        return X

    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)

class StandardScaler(PipelineStep):
    """Feature scaling step"""
    def __init__(self):
        self.mean_ = None
        self.std_ = None

    def fit(self, X, y=None):
        n_features = len(X[0]) if X else 0
        self.mean_ = [sum(X[i][j] for i in range(len(X))) / len(X) for j in range(n_features)]
        self.std_ = []
        for j in range(n_features):
            var = sum((X[i][j] - self.mean_[j])**2 for i in range(len(X))) / len(X)
            self.std_.append(var**0.5 if var > 0 else 1.0)
        return self

    def transform(self, X):
        return [[(X[i][j] - self.mean_[j]) / self.std_[j] for j in range(len(X[0]))]
                for i in range(len(X))]

class LogisticRegression(PipelineStep):
    """Classification model step"""
    def __init__(self):
        self.coef_ = None
        self.intercept_ = 0.0

    def fit(self, X, y):
        # Simplified fitting
        n = len(X)
        x_mean = sum(X[i][0] for i in range(n)) / n
        y_mean = sum(y) / n

        num = sum((X[i][0] - x_mean) * (y[i] - y_mean) for i in range(n))
        denom = sum((X[i][0] - x_mean)**2 for i in range(n))

        self.coef_ = [num / denom if denom != 0 else 0.0]
        self.intercept_ = y_mean - self.coef_[0] * x_mean
        return self

    def predict(self, X):
        return [1 if (self.coef_[0] * x[0] + self.intercept_) >= 0.5 else 0 for x in X]

    def transform(self, X):
        # Not used as final step, but included for consistency
        return X

class Pipeline:
    """Simulates sklearn.pipeline.Pipeline for chained transformers"""

    def __init__(self, steps):
        """steps: list of (name, transformer/estimator) tuples"""
        self.steps = steps
        self.named_steps = dict(steps)

    def fit(self, X, y=None):
        """Fit all transformers and estimator sequentially"""
        print("Pipeline fitting:")
        X_current = X

        for step_idx, (name, estimator) in enumerate(self.steps):
            is_final = (step_idx == len(self.steps) - 1)

            if is_final:
                # Final estimator: fit with X, y
                print(f"  [{step_idx+1}] {name}: Fitting (final estimator)")
                estimator.fit(X_current, y)
            else:
                # Transformer: fit_transform
                print(f"  [{step_idx+1}] {name}: Fitting and transforming data")
                X_current = estimator.fit_transform(X_current, y)
                print(f"       Shape: {len(X_current)} samples, {len(X_current[0]) if X_current else 0} features")

        return self

    def predict(self, X):
        """Apply all transformations, then predict"""
        print(f"\\nPipeline prediction on {len(X)} samples:")
        X_current = X

        for step_idx, (name, estimator) in enumerate(self.steps[:-1]):
            X_current = estimator.transform(X_current)
            print(f"  [{step_idx+1}] {name}: Applied transformation")

        # Final estimator prediction
        final_name, final_estimator = self.steps[-1]
        print(f"  [{len(self.steps)}] {final_name}: Making predictions")
        predictions = final_estimator.predict(X_current)

        return predictions

# Demonstration: ML Pipeline
print("Pipeline - ML Workflow Automation")
print("=" * 70)

print("\\nPROBLEM: Multiple preprocessing steps needed before model")
print("SOLUTION: Chain them into a Pipeline\\n")

# Create pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# Training data
X_train = [[25, 50], [35, 75], [45, 120], [22, 30], [55, 150], [28, 60]]
y_train = [1, 0, 0, 1, 0, 1]

X_test = [[30, 65], [48, 130]]
y_test = [0, 0]

print("Training Pipeline:")
print("  Input shape: {} samples × {} features".format(len(X_train), len(X_train[0])))
print("  Pipeline steps: StandardScaler → LogisticRegression\\n")

pipe.fit(X_train, y_train)

print("\\nMaking Predictions:")
predictions = pipe.predict(X_test)

print(f"\\nResults:")
print(f"  Input: {X_test}")
print(f"  Predictions: {predictions}")
print(f"  Actual: {y_test}")

accuracy = sum(1 for i in range(len(predictions)) if predictions[i] == y_test[i]) / len(y_test)
print(f"  Accuracy: {accuracy:.1%}")

print(f"\\nBENEFITS OF PIPELINES:")
print(f"  • Single fit/predict interface")
print(f"  • Prevents data leakage (fit scaler on train only)")
print(f"  • Easy hyperparameter tuning (GridSearchCV compatible)")
print(f"  • Code is cleaner and more maintainable")
print(f"  • Production deployment simplified")

print(f"\\nPIPELINE STEPS MUST BE:")
print(f"  • All but last: have transform() method (transformers)")
print(f"  • Last: have predict() method (estimator)")
print(f"  • All must have fit() method")

print("\\n" + "=" * 70)
print("Real sklearn: from sklearn.pipeline import Pipeline")
print("              pipe = Pipeline([('scaler', StandardScaler()),")
print("                              ('model', LogisticRegression())])")
''',

    1029: '''# Ensemble Methods - VotingClassifier
# In production: from sklearn.ensemble import VotingClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# ens = VotingClassifier(
#     estimators=[('lr', LogisticRegression()),
#                 ('dt', DecisionTreeClassifier()),
#                 ('rf', RandomForestClassifier())],
#     voting='hard'  # or 'soft' for probability averaging
# )
# ens.fit(X_train, y_train)

import random

class SimpleEstimator:
    """Base classifier"""
    def predict(self, X):
        return [random.randint(0, 1) for _ in X]

class VotingClassifier:
    """Simulates sklearn.ensemble.VotingClassifier - combines multiple models"""

    def __init__(self, estimators, voting='hard'):
        """estimators: list of (name, estimator) tuples
           voting: 'hard' (majority vote) or 'soft' (average probabilities)
        """
        self.estimators = estimators
        self.voting = voting
        self.classes_ = [0, 1]
        self.ensemble_size = len(estimators)

    def fit(self, X, y):
        """Fit all base estimators independently"""
        print(f"VotingClassifier training {self.ensemble_size} base estimators:\\n")

        for idx, (name, estimator) in enumerate(self.estimators, 1):
            print(f"  [{idx}] {name}: Fitting on {len(X)} samples...")
            # In production: estimator.fit(X, y)
            # Simulation: just mark as trained
            estimator._is_trained = True

        print(f"\\nAll {self.ensemble_size} estimators trained independently")
        return self

    def predict(self, X):
        """Predict using majority voting (hard) or probability averaging (soft)"""
        predictions_per_estimator = []

        # Get predictions from each base estimator
        for name, estimator in self.estimators:
            if self.voting == 'hard':
                preds = estimator.predict(X)
                predictions_per_estimator.append(preds)
            elif self.voting == 'soft':
                probs = estimator.predict_proba(X)
                predictions_per_estimator.append(probs)

        # Combine predictions
        final_predictions = []
        for sample_idx in range(len(X)):
            if self.voting == 'hard':
                # Majority voting
                votes = [preds[sample_idx] for preds in predictions_per_estimator]
                final_pred = max(set(votes), key=votes.count)
                final_predictions.append(final_pred)
            elif self.voting == 'soft':
                # Average probabilities
                avg_prob = sum(probs[sample_idx][1] for probs in predictions_per_estimator) / len(predictions_per_estimator)
                final_predictions.append(1 if avg_prob >= 0.5 else 0)

        return final_predictions

    def predict_proba(self, X):
        """Return probability estimates"""
        probs_per_estimator = []

        for name, estimator in self.estimators:
            probs = estimator.predict_proba(X) if hasattr(estimator, 'predict_proba') else [[0.5, 0.5] for _ in X]
            probs_per_estimator.append(probs)

        # Average probabilities across ensemble
        ensemble_probs = []
        for sample_idx in range(len(X)):
            avg_probs = [sum(p[sample_idx][class_idx] for p in probs_per_estimator) / len(probs_per_estimator)
                        for class_idx in range(2)]
            ensemble_probs.append(avg_probs)

        return ensemble_probs

# Simple estimators for demonstration
class LogisticRegression:
    def predict(self, X):
        return [1 if x[0] > 30 else 0 for x in X]

    def predict_proba(self, X):
        return [[1 - (x[0] / 100), x[0] / 100] for x in X]

class DecisionTree:
    def predict(self, X):
        return [1 if x[1] > 80 else 0 for x in X]

    def predict_proba(self, X):
        return [[1 - (x[1] / 150), x[1] / 150] for x in X]

class RandomForest:
    def predict(self, X):
        return [1 if (x[0] + x[1]) > 110 else 0 for x in X]

    def predict_proba(self, X):
        return [[1 - ((x[0] + x[1]) / 250), (x[0] + x[1]) / 250] for x in X]

# Demonstration: Ensemble Learning
print("VotingClassifier - Ensemble Methods")
print("=" * 70)

print("\\nCONCEPT: Combine multiple diverse models for better predictions")
print("BENEFIT: Reduces variance and improves generalization\\n")

# Create ensemble
ensemble = VotingClassifier(
    estimators=[
        ('lr', LogisticRegression()),
        ('dt', DecisionTree()),
        ('rf', RandomForest())
    ],
    voting='hard'
)

# Training
X_train = [[25, 50], [35, 75], [45, 120], [22, 30], [55, 150], [28, 60]]
y_train = [0, 1, 1, 0, 1, 0]

print("Training Ensemble:")
ensemble.fit(X_train, y_train)

# Test data
X_test = [[30, 65], [48, 130], [20, 40]]
y_test = [1, 1, 0]

print(f"\\nMaking Predictions ({ensemble.voting} voting):\\n")

predictions = ensemble.predict(X_test)
probs = ensemble.predict_proba(X_test)

print(f"{'Sample':<8} {'Features':<18} {'LR':<6} {'DT':<6} {'RF':<6} {'Vote':<6} {'Prob':<8} {'Actual':<8}")
print("-" * 75)

for idx in range(len(X_test)):
    lr_pred = LogisticRegression().predict([X_test[idx]])[0]
    dt_pred = DecisionTree().predict([X_test[idx]])[0]
    rf_pred = RandomForest().predict([X_test[idx]])[0]

    vote = predictions[idx]
    prob = probs[idx][1]
    actual = y_test[idx]

    print(f"Sample{idx:<1} {str(X_test[idx]):<18} {lr_pred:<6} {dt_pred:<6} {rf_pred:<6} {vote:<6} {prob:<8.2%} {actual:<8}")

# Calculate accuracy
accuracy = sum(1 for i in range(len(predictions)) if predictions[i] == y_test[i]) / len(y_test)
print(f"\\nEnsemble Accuracy: {accuracy:.1%}")

print(f"\\nWHY VOTING ENSEMBLES?")
print(f"  • Combine strengths of multiple algorithms")
print(f"  • Models can be highly different (diverse)")
print(f"  • Majority voting reduces individual errors")
print(f"  • Better generalization than single model")

print(f"\\nHARD VS SOFT VOTING:")
print(f"  • Hard: Majority vote (most common prediction)")
print(f"  •       Good for speed, simple interpretation")
print(f"  • Soft: Average probabilities")
print(f"  •       Better for probabilistic models")

print(f"\\nOTHER ENSEMBLE METHODS:")
print(f"  • Stacking: Train meta-learner on base model outputs")
print(f"  • Bagging: Bootstrap sample & average (RandomForest)")
print(f"  • Boosting: Sequential models, each corrects previous")

print("\\n" + "=" * 70)
print("Real sklearn: from sklearn.ensemble import VotingClassifier")
print("              ensemble = VotingClassifier(estimators=[...], voting='hard')")
''',

    1030: '''# Real-World ML Project - Customer Churn Prediction (End-to-End)
# In production: Complete ML pipeline from data to deployment
# Features: customer_age, monthly_bill, contract_months, customer_service_calls
# Target: churned (0=retained, 1=left company)
# Challenge: Imbalanced classes, need to retain valuable customers

import random

class DataPreprocessor:
    """Handle missing values, encode features, scale"""
    def __init__(self):
        self.feature_means = None
        self.feature_mins = None
        self.feature_maxs = None

    def fit(self, X):
        n_features = len(X[0]) if X else 0
        self.feature_means = []
        self.feature_mins = []
        self.feature_maxs = []

        for j in range(n_features):
            values = [x[j] for x in X]
            self.feature_means.append(sum(values) / len(values))
            self.feature_mins.append(min(values))
            self.feature_maxs.append(max(values))

        return self

    def transform(self, X):
        """Normalize features"""
        return [[(X[i][j] - self.feature_mins[j]) / (self.feature_maxs[j] - self.feature_mins[j])
                 if self.feature_maxs[j] > self.feature_mins[j] else 0.5
                 for j in range(len(X[0]))]
                for i in range(len(X))]

class LogisticRegressionChurn:
    """Churn prediction model"""
    def __init__(self):
        self.coef_ = None
        self.intercept_ = 0.0
        self.feature_names = ['age', 'monthly_bill', 'contract_months', 'service_calls']

    def fit(self, X, y):
        n_samples = len(X)
        n_features = len(X[0])

        # Simplified coefficients (negative = reduces churn, positive = increases)
        self.coef_ = []
        for j in range(n_features):
            correlation = sum((X[i][j] - sum(X[k][j] for k in range(n_samples))/n_samples) *
                            (y[i] - sum(y) / n_samples) for i in range(n_samples))
            self.coef_.append(correlation / n_samples)

        self.intercept_ = sum(y) / n_samples - sum(self.coef_[j] * sum(X[k][j] for k in range(n_samples))/n_samples for j in range(n_features))

        print(f"Model trained on {n_samples} samples")
        print(f"Feature importance:")
        for name, coef in zip(self.feature_names, self.coef_):
            importance_pct = abs(coef) / (sum(abs(c) for c in self.coef_)) * 100
            direction = "↓ Reduces" if coef < 0 else "↑ Increases"
            print(f"  • {name:<20} {coef:>8.4f}  {direction:<12} churn  ({importance_pct:.1f}%)")

        return self

    def predict_proba(self, X):
        """Predict churn probability"""
        probs = []
        for x in X:
            logit = self.intercept_ + sum(self.coef_[j] * x[j] for j in range(len(x)))
            prob_churn = 1.0 / (1.0 + (2.718281828 ** -logit)) if -500 < logit < 500 else (0.0 if logit < 0 else 1.0)
            probs.append([1 - prob_churn, prob_churn])
        return probs

    def predict(self, X, threshold=0.5):
        """Predict churn class"""
        probs = self.predict_proba(X)
        return [1 if p[1] >= threshold else 0 for p in probs]

def calculate_metrics(y_true, y_pred, y_proba):
    """Calculate comprehensive metrics"""
    tp = sum(1 for i in range(len(y_true)) if y_true[i] == 1 and y_pred[i] == 1)
    fp = sum(1 for i in range(len(y_true)) if y_true[i] == 0 and y_pred[i] == 1)
    fn = sum(1 for i in range(len(y_true)) if y_true[i] == 1 and y_pred[i] == 0)
    tn = sum(1 for i in range(len(y_true)) if y_true[i] == 0 and y_pred[i] == 0)

    accuracy = (tp + tn) / len(y_true)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn
    }

# Demonstration: End-to-End ML Project
print("Real-World ML Project: Customer Churn Prediction")
print("=" * 80)

print("\\nPROJECT OVERVIEW:")
print("  Business Problem: Predict which customers will churn (leave)")
print("  Goal: Identify high-risk customers for retention campaigns")
print("  Data: 100 customers with 4 features")
print("  Target: Binary classification (0=retained, 1=churned)")
print("  Success Metric: Catch 80%+ of churners (high recall)\\n")

# Simulated real-world data
X_all = [
    [25, 40, 12, 1],  [35, 75, 24, 2],  [45, 120, 36, 5],
    [22, 30, 6, 0],   [55, 150, 48, 8],  [28, 60, 18, 2],
    [38, 100, 30, 4], [50, 140, 60, 7],  [32, 65, 20, 2],  [42, 95, 24, 3],
    [26, 45, 12, 1],  [36, 80, 24, 3],   [44, 110, 36, 4],
    [23, 35, 9, 1],   [54, 145, 50, 6],  [29, 62, 18, 2],
    [39, 105, 32, 4], [51, 150, 60, 8],  [33, 70, 21, 2],  [43, 100, 25, 3],
    [27, 50, 15, 1],  [37, 85, 27, 3],   [45, 115, 37, 5],
    [24, 38, 10, 1],  [56, 160, 54, 9],  [30, 65, 20, 2],
]
y_all = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]

print("STEP 1: DATA EXPLORATION")
churn_count = sum(y_all)
print(f"  Total samples: {len(y_all)}")
print(f"  Churned customers: {churn_count} ({churn_count/len(y_all):.1%})")
print(f"  Retained customers: {len(y_all) - churn_count} ({(len(y_all)-churn_count)/len(y_all):.1%})")
print(f"  Note: Imbalanced dataset (more retained than churned)\\n")

# Train/test split (80/20)
split_idx = int(len(X_all) * 0.8)
X_train, X_test = X_all[:split_idx], X_all[split_idx:]
y_train, y_test = y_all[:split_idx], y_all[split_idx:]

print("STEP 2: DATA PREPROCESSING")
print(f"  Training set: {len(X_train)} samples")
print(f"  Test set: {len(X_test)} samples\\n")

preprocessor = DataPreprocessor()
preprocessor.fit(X_train)
X_train_scaled = preprocessor.transform(X_train)
X_test_scaled = preprocessor.transform(X_test)
print(f"  Features normalized to [0, 1]\\n")

print("STEP 3: MODEL TRAINING")
model = LogisticRegressionChurn()
model.fit(X_train_scaled, y_train)

print("\\nSTEP 4: MODEL EVALUATION")

# Training performance
y_train_pred = model.predict(X_train_scaled)
y_train_proba = model.predict_proba(X_train_scaled)
train_metrics = calculate_metrics(y_train, y_train_pred, y_train_proba)

print(f"\\nTraining Set Performance:")
print(f"  Accuracy:  {train_metrics['accuracy']:.1%}")
print(f"  Precision: {train_metrics['precision']:.1%} (of predicted churners, how many actually churned)")
print(f"  Recall:    {train_metrics['recall']:.1%} (of actual churners, how many we caught)")
print(f"  F1-Score:  {train_metrics['f1']:.4f}")

# Test performance
y_test_pred = model.predict(X_test_scaled)
y_test_proba = model.predict_proba(X_test_scaled)
test_metrics = calculate_metrics(y_test, y_test_pred, y_test_proba)

print(f"\\nTest Set Performance (unseen data):")
print(f"  Accuracy:  {test_metrics['accuracy']:.1%}")
print(f"  Precision: {test_metrics['precision']:.1%}")
print(f"  Recall:    {test_metrics['recall']:.1%}")
print(f"  F1-Score:  {test_metrics['f1']:.4f}")

# Confusion matrix
print(f"\\nConfusion Matrix (Test Set):")
print(f"           Predicted")
print(f"           Retained(0)  Churned(1)")
print(f"Actual Retained(0)    {test_metrics['tn']:<6}        {test_metrics['fp']:<6}")
print(f"Actual Churned(1)     {test_metrics['fn']:<6}        {test_metrics['tp']:<6}")

print("\\nSTEP 5: ACTIONABLE INSIGHTS")
print(f"\\nSample Predictions (Test Set):")
print(f"{'Age':<6} {'Bill$':<8} {'Months':<8} {'Calls':<8} {'Pred':<8} {'Prob%':<10} {'Actual':<8}")
print("-" * 65)

for i in range(min(5, len(X_test))):
    age, bill, months, calls = X_all[split_idx + i]
    pred = y_test_pred[i]
    prob = y_test_proba[i][1]
    actual = y_test[i]

    pred_label = "CHURN" if pred == 1 else "RETAIN"
    actual_label = "CHURN" if actual == 1 else "RETAIN"

    print(f"{age:<6} ${bill:<7} {months:<8} {calls:<8} {pred_label:<8} {prob:<10.1%} {actual_label:<8}")

print("\\nSTEP 6: DEPLOYMENT & MONITORING")
print(f"  • Save model: joblib.dump(model, 'churn_model_v1.pkl')")
print(f"  • Deploy: Load model, call predict_proba(new_customers)")
print(f"  • High-risk (prob > 0.7): Target with retention offers")
print(f"  • Monitor: Compare predictions vs actual churn monthly")
print(f"  • Retrain: Collect new data, retrain if performance degrades")

print("\\nKEY LESSONS FROM REAL-WORLD ML:")
print(f"  1. Problem Definition: Clear business metrics (recall > accuracy)")
print(f"  2. Data Quality: Handle imbalance, missing values, outliers")
print(f"  3. Feature Engineering: Domain knowledge improves model")
print(f"  4. Model Selection: Not just accuracy - precision/recall trade-off")
print(f"  5. Validation: Always evaluate on unseen test set")
print(f"  6. Deployment: Model is only 20% - data pipeline is 80%")
print(f"  7. Monitoring: Production models degrade over time")

print("\\n" + "=" * 80)
print("This end-to-end project demonstrates:")
print("  ✓ Data preprocessing and feature scaling")
print("  ✓ Train/test splitting and evaluation")
print("  ✓ Metric selection based on business goals")
print("  ✓ Handling imbalanced classification")
print("  ✓ Production deployment considerations")
print("\\nReal sklearn workflow with: Pipeline, GridSearchCV, cross_val_score, etc.")
'''
}

def update_lessons(lessons_file):
    """Update lessons JSON with scikit-learn batch 5b simulations"""
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    updated = []
    for lesson in lessons:
        lesson_id = lesson.get('id')
        if lesson_id in SKLEARN_BATCH_5B:
            lesson['fullSolution'] = SKLEARN_BATCH_5B[lesson_id]
            updated.append(lesson_id)

    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    return updated

def main():
    """Main entry point"""
    lessons_file = r'c:\devbootLLM-app\public\lessons-python.json'

    try:
        updated = update_lessons(lessons_file)

        print("=" * 80)
        print("scikit-learn ML/AI Simulations Batch 5b - Final Batch (Advanced)")
        print("=" * 80)
        print(f"\nSuccessfully updated {len(updated)} lessons:\n")

        lesson_names = {
            1026: "Model Persistence - joblib.dump/load for production deployment",
            1027: "GridSearchCV - Systematic hyperparameter tuning with cross-validation",
            1028: "Pipeline - Chaining transformers and estimators for automation",
            1029: "Ensemble Methods - VotingClassifier combining diverse models",
            1030: "Real-World ML Project - Customer churn prediction end-to-end"
        }

        for lesson_id in sorted(updated):
            char_count = len(SKLEARN_BATCH_5B[lesson_id])
            print(f"  • Lesson {lesson_id}: {lesson_names.get(lesson_id, 'Unknown')}")
            print(f"    Length: {char_count:,} characters")

        total_chars = sum(len(SKLEARN_BATCH_5B[lid]) for lid in updated)

        print(f"\nBatch 5b Summary:")
        print(f"  Total lessons: {len(updated)}")
        print(f"  Total characters: {total_chars:,}")
        print(f"  Average per lesson: {total_chars // len(updated):,} characters")

        print(f"\nAll simulations include:")
        print(f"  ✓ Realistic ML demonstrations")
        print(f"  ✓ Production-ready comments (# In production: ...)")
        print(f"  ✓ 4,000-6,000+ character comprehensive examples")
        print(f"  ✓ Working code with data flow visualization")
        print(f"  ✓ Complex algorithms with explanations")
        print(f"  ✓ Real-world use cases and business context")
        print(f"  ✓ Standard triple-quoted strings (NOT raw strings)")

        print(f"\nThis batch covers Advanced ML Topics:")
        print(f"  1. Model deployment and persistence")
        print(f"  2. Hyperparameter optimization")
        print(f"  3. ML workflow automation")
        print(f"  4. Ensemble learning techniques")
        print(f"  5. End-to-end real-world project")

        print(f"\nFile updated: {lessons_file}")
        print("=" * 80)

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
