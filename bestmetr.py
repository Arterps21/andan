from catboost import CatBoostClassifier

classifier = CatBoostClassifier()
classifier.fit(X_train, y_train)
pred = classifier.predict(X_test)
