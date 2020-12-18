import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing
import sklearn.svm as svm
from sklearn.svm import SVR
import numpy as np
import sklearn.metrics as metrics

from sklearn import utils


def execute(x_train, y_train, x_test, y_test):
    lab_enc = preprocessing.LabelEncoder()

    encodedtrain = lab_enc.fit_transform(y_train)
    encodedtest = lab_enc.fit_transform(y_test)


    for k in ['linear', 'poly', 'rbf', 'sigmoid']:
        clf = svm.SVR(kernel=k)
        clf.fit(x_train, y_train)
        confidence = clf.score(x_test, y_test)
        y_pred = clf.predict(x_test)
#        encodedy_predict = lab_enc.fit_transform(y_pred)
#        print(y_pred)
        mean_absolute_error = metrics.mean_absolute_error(y_test, y_pred)
        mse = metrics.mean_squared_error(y_test, y_pred)
        r2 = metrics.r2_score(y_test, y_pred)
        explained_variance = metrics.explained_variance_score(y_test, y_pred)

        print(k, round(confidence, 4))
        print("explained variance : ", round(explained_variance, 4))
        print("mean absolute error: ", round(mean_absolute_error, 4))
        print("mean squre error   : ", round(mse, 4))
        print("r2                 : ", round(r2, 4))
        print()




        # print(y_test.shape)
        # print(y_pred.shape)
        # print(confusion_matrix(encodedtest, encodedy_predict))
        # print(classification_report(encodedtest, encodedy_predict))














    # print(utils.multiclass.type_of_target(encodedtrain))
    #
    #
    # svclassifier = SVC(kernel='linear')
    # svclassifier.fit(x_train, encodedtrain)
    #
    # y_pred = svclassifier.predict(x_test)
    #
    # print(utils.multiclass.type_of_target(y_pred))
    # print(y_pred)
    #
    # print(utils.multiclass.type_of_target(encodedtest))
    # print(encodedtest)
    #
    # print(confusion_matrix(encodedtest, y_pred))
    # print(classification_report(encodedtest, y_pred))


    #
    # c_range = 2, 4, 6, 8, 10  #
    # svm_c_error = []
    # for c_value in c_range:
    #     model = svm.SVC(kernel='rbf', C=c_value)
    #     model.fit(X=x_train, y=encodedtrain)
    #     error = 1. - model.score(x_test, encodedtest)
    #     svm_c_error.append(error)
    # plt.plot(c_range, svm_c_error)
    # plt.title('poly SVM')
    # plt.xlabel('c values')
    # plt.ylabel('error')
    # plt.xticks(c_range)
    # plt.show()
    #
    # y_pred = model.predict(x_test)
    # print(confusion_matrix(encodedtest, y_pred))
    # print(classification_report(encodedtest, y_pred))

    # # Fit regression model
    # svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
    # svr_lin = SVR(kernel='linear', C=100, gamma='auto')
    # svr_poly = SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1,
    #                coef0=1)
    #
    # # #############################################################################
    # # Look at the results
    # lw = 2
    #
    # svrs = [svr_rbf, svr_lin, svr_poly]
    # kernel_label = ['RBF', 'Linear', 'Polynomial']
    # model_color = ['m', 'c', 'g']
    #
    # fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 10), sharey=True)
    # for ix, svr in enumerate(svrs):
    #     axes[ix].plot(x_train, svr.fit(x_train, encodedtrain).predict(x_test), color=model_color[ix], lw=lw,
    #                   label='{} model'.format(kernel_label[ix]))
    #     axes[ix].scatter(x_train[svr.support_], encodedtrain[svr.support_], facecolor="none",
    #                      edgecolor=model_color[ix], s=50,
    #                      label='{} support vectors'.format(kernel_label[ix]))
    #     axes[ix].scatter(x_train[np.setdiff1d(np.arange(len(x_train)), svr.support_)],
    #                      encodedtrain[np.setdiff1d(np.arange(len(x_train)), svr.support_)],
    #                      facecolor="none", edgecolor="k", s=50,
    #                      label='other training data')
    #     axes[ix].legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
    #                     ncol=1, fancybox=True, shadow=True)
    #
    # fig.text(0.5, 0.04, 'data', ha='center', va='center')
    # fig.text(0.06, 0.5, 'target', ha='center', va='center', rotation='vertical')
    # fig.suptitle("Support Vector Regression", fontsize=14)
    # plt.show()
