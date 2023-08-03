import csv
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,roc_curve, auc
from pyod.models.ecod import ECOD
from pyod.models.abod import ABOD
from pyod.models.mcd import MCD
from pyod.models.sos import SOS
from pyod.models.lof import LOF
from pyod.models.cof import COF
from pyod.models.knn import KNN
from pyod.models.iforest import IForest
from pyod.models.lscp import LSCP
from pyod.models.loda import LODA
from pyod.models.loda import VAE

for i in range(1, 11):
    # 读取数据
    with open(f'./samples/20-{i*10}.csv', newline='') as f:
        reader = csv.reader(f)
        data = [float(row[0]) for row in reader]
    x_cpu = np.array(data).reshape(-1, 1)

    # with open('./samples/ad-io3.csv', newline='') as f:
    #     reader = csv.reader(f)
    #     data = [float(row[0]) for row in reader]
    # x_io = np.array(data).reshape(-1, 1)
    # print(data)

    x_train = x_cpu
    # x_train = np.column_stack((x_io, x_cpu))
    # y_true = [0]*20+[1]*67+[0]*126
    # y_true = [0]*20+[1]*44+[0]*44+[1]*50+[0]*365
    y_true = [0]*11+[1]*22+[0]*27

    output = ["Algorithm,Precision,Recall,F1 Score,AUC"]

    print("ECOD")
    clf = ECOD(contamination=0.37)
    clf.fit(x_train)
    y_train_pred = clf.labels_  # 返回训练数据上的分类标签 (0: 正常值, 1: 异常值)
    y_train_scores = clf.decision_scores_  # 返回训练数据上的异常值 (分值越大越异常)
    outliers = x_train[clf.predict(x_train) == 1]
    # print('ECOD outliers:', outliers.flatten())
    # print(y_train_pred)
    # print(y_train_scores)
    fpr, tpr, thresholds = roc_curve(y_true, y_train_scores)
    roc_auc = str(auc(fpr, tpr))
    print(roc_auc)
    acc = accuracy_score(y_true, y_train_pred)
    prec = str(precision_score(y_true, y_train_pred))
    rec = str(recall_score(y_true, y_train_pred))
    f1 = str(f1_score(y_true, y_train_pred))
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 score:", f1)
    output.append(",".join(["ECOD", prec, rec, f1, roc_auc]))


    print("MCD")
    clf = MCD(contamination=0.37)
    clf.fit(x_train)
    y_train_pred = clf.labels_  # 返回训练数据上的分类标签 (0: 正常值, 1: 异常值)
    y_train_scores = clf.decision_scores_  # 返回训练数据上的异常值 (分值越大越异常)
    outliers = x_train[clf.predict(x_train) == 1]
    # print('MCD outliers:', outliers.flatten())
    # print(y_train_pred)
    # print(y_train_scores)
    fpr, tpr, thresholds = roc_curve(y_true, y_train_scores)
    roc_auc = str(auc(fpr, tpr))
    print(roc_auc)
    acc = accuracy_score(y_true, y_train_pred)
    prec = str(precision_score(y_true, y_train_pred))
    rec = str(recall_score(y_true, y_train_pred))
    f1 = str(f1_score(y_true, y_train_pred))
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 score:", f1)
    output.append(",".join(["MCD", prec, rec, f1, roc_auc]))

    print("LOF")
    clf = LOF(contamination=0.37)
    clf.fit(x_train)
    y_train_pred = clf.labels_  # 返回训练数据上的分类标签 (0: 正常值, 1: 异常值)
    y_train_scores = clf.decision_scores_  # 返回训练数据上的异常值 (分值越大越异常)
    outliers = x_train[clf.predict(x_train) == 1]
    # print('LOF outliers:', outliers.flatten())
    # print(y_train_pred)
    # print(y_train_scores)
    fpr, tpr, thresholds = roc_curve(y_true, y_train_scores)
    roc_auc = str(auc(fpr, tpr))
    print(roc_auc)
    acc = accuracy_score(y_true, y_train_pred)
    prec = str(precision_score(y_true, y_train_pred))
    rec = str(recall_score(y_true, y_train_pred))
    f1 = str(f1_score(y_true, y_train_pred))
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 score:", f1)
    output.append(",".join(["LOF", prec, rec, f1, roc_auc]))

    print("KNN")
    clf = KNN(contamination=0.37)
    clf.fit(x_train)
    y_train_pred = clf.labels_  # 返回训练数据上的分类标签 (0: 正常值, 1: 异常值)
    y_train_scores = clf.decision_scores_  # 返回训练数据上的异常值 (分值越大越异常)
    outliers = x_train[clf.predict(x_train) == 1]
    # print('KNN outliers:', outliers.flatten())
    # print(y_train_pred)
    # print(y_train_scores)
    fpr, tpr, thresholds = roc_curve(y_true, y_train_scores)
    roc_auc = str(auc(fpr, tpr))
    print(roc_auc)
    acc = accuracy_score(y_true, y_train_pred)
    prec = str(precision_score(y_true, y_train_pred))
    rec = str(recall_score(y_true, y_train_pred))
    f1 = str(f1_score(y_true, y_train_pred))
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 score:", f1)
    output.append(",".join(["KNN", prec, rec, f1, roc_auc]))

    print("IForest")
    clf = IForest(contamination=0.37)
    clf.fit(x_train)
    y_train_pred = clf.labels_  # 返回训练数据上的分类标签 (0: 正常值, 1: 异常值)
    y_train_scores = clf.decision_scores_  # 返回训练数据上的异常值 (分值越大越异常)
    outliers = x_train[clf.predict(x_train) == 1]
    # print('IForest outliers:', outliers.flatten())
    # print(y_train_pred)
    # print(y_train_scores)
    fpr, tpr, thresholds = roc_curve(y_true, y_train_scores)
    roc_auc = str(auc(fpr, tpr))
    print(roc_auc)
    acc = accuracy_score(y_true, y_train_pred)
    prec = str(precision_score(y_true, y_train_pred))
    rec = str(recall_score(y_true, y_train_pred))
    f1 = str(f1_score(y_true, y_train_pred))
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 score:", f1)
    output.append(",".join(["IForest", prec, rec, f1, roc_auc]))


    print("LODA")
    lf = LODA(contamination=0.37)
    clf.fit(x_train)
    y_train_pred = clf.labels_  # 返回训练数据上的分类标签 (0: 正常值, 1: 异常值)
    y_train_scores = clf.decision_scores_  # 返回训练数据上的异常值 (分值越大越异常)
    outliers = x_train[clf.predict(x_train) == 1]
    # print('LODA outliers:', outliers.flatten())
    # print(y_train_pred)
    # print(y_train_scores)
    fpr, tpr, thresholds = roc_curve(y_true, y_train_scores)
    roc_auc = str(auc(fpr, tpr))
    print(roc_auc)
    acc = accuracy_score(y_true, y_train_pred)
    prec = str(precision_score(y_true, y_train_pred))
    rec = str(recall_score(y_true, y_train_pred))
    f1 = str(f1_score(y_true, y_train_pred))
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 score:", f1)
    output.append(",".join(["LODA", prec, rec, f1, roc_auc]))

    print("VAE")
    lf = VAE(contamination=0.37)
    clf.fit(x_train)
    y_train_pred = clf.labels_  # 返回训练数据上的分类标签 (0: 正常值, 1: 异常值)
    y_train_scores = clf.decision_scores_  # 返回训练数据上的异常值 (分值越大越异常)
    outliers = x_train[clf.predict(x_train) == 1]
    # print('LODA outliers:', outliers.flatten())
    # print(y_train_pred)
    # print(y_train_scores)
    fpr, tpr, thresholds = roc_curve(y_true, y_train_scores)
    roc_auc = str(auc(fpr, tpr))
    print(roc_auc)
    acc = accuracy_score(y_true, y_train_pred)
    prec = str(precision_score(y_true, y_train_pred))
    rec = str(recall_score(y_true, y_train_pred))
    f1 = str(f1_score(y_true, y_train_pred))
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 score:", f1)
    output.append(",".join(["VAE", prec, rec, f1, roc_auc]))

    with open(f"./results/result-20-{i*10}.csv", "w") as c:
        # 创建writer对象，用来写入每一行的数据
        writer = csv.writer(c)
        # 遍历合并后的数据，将每一对数据拼接为一行，并写入c.csv文件
        for line in output:
            writer.writerow(line.split(","))
















