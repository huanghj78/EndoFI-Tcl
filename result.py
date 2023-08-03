from sklearn.metrics import roc_curve, auc
y_true = [0,0,0,0,1]
y_score = [1,1,1,1,0]
# 假设y_true是真实值，y_score是预测值
fpr, tpr, thresholds = roc_curve(y_true, y_score)
roc_auc = auc(fpr, tpr)
print(roc_auc)
