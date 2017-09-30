import numpy as np

total_error = 0.25757363957

ret = 1.69442156163387

mtx = np.array([[  2.65260389e+03, 0.00000000e+00, 1.70147367e+03], [  0.00000000e+00, 2.63963564e+03, 1.28097111e+03], [  0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

dist = np.array([[  1.57358247e-01, 7.74419994e-02, -3.30858728e-04, 5.87865782e-03, -1.39352510e+00]])

rvecs = np.array([[[ 0.51405061], [-0.60801489], [ 1.53850711]], [[ 0.02738829], [-0.72800136], [ 0.00086445]], [[ 1.20112997], [-0.20671539], [ 2.90169103]], [[-0.3869177 ], [-0.32492143], [-1.54826054]], [[-0.87368992], [ 0.40071712], [-2.41985605]], [[-0.57496841], [-0.29880345], [-0.98657755]], [[-0.12932852], [-0.78596178], [ 0.41961213]], [[ 0.56743426], [-0.88583321], [ 1.88288427]], [[ 0.06752287], [ 0.12100877], [-1.82664421]], [[-0.03522303], [-0.03117646], [-1.56043004]], [[ 0.05820617], [-0.1769565 ], [-3.13112965]], [[-0.02451809], [-0.02956135], [-1.6859788 ]]])

tvecs = np.array([[[  2.10291514], [ -3.57535021], [ 12.82128169]], [[ -3.96011672], [ -2.75189092], [ 11.86776492]], [[  4.21608655], [  3.26071386], [ 11.43973814]], [[ -0.68745932], [  0.87106946], [ 12.98541488]], [[  1.45770373], [  4.03131137], [ 14.77263029]], [[ -1.92893939], [  1.06141462], [ 13.60904396]], [[ -0.99384051], [ -3.43284576], [ 13.0376588 ]], [[  4.08663516], [ -3.3698154 ], [ 13.23140964]], [[ -0.65602553], [  3.32297241], [ 16.73863002]], [[ -0.74848241], [  4.09750264], [ 16.43697856]], [[  3.14971498], [  1.89721967], [ 14.23809063]], [[ -2.27580191], [  2.68838064], [ 12.61000724]]])

objpoints = np.array([np.array([[ 0., 0., 0.], [ 1., 0., 0.], [ 2., 0., 0.], [ 3., 0., 0.], [ 4., 0., 0.], [ 5., 0., 0.], [ 6., 0., 0.], [ 0., 1., 0.], [ 1., 1., 0.], [ 2., 1., 0.], [ 3., 1., 0.], [ 4., 1., 0.], [ 5., 1., 0.], [ 6., 1., 0.], [ 0., 2., 0.], [ 1., 2., 0.], [ 2., 2., 0.], [ 3., 2., 0.], [ 4., 2., 0.], [ 5., 2., 0.], [ 6., 2., 0.], [ 0., 3., 0.], [ 1., 3., 0.], [ 2., 3., 0.], [ 3., 3., 0.], [ 4., 3., 0.], [ 5., 3., 0.], [ 6., 3., 0.], [ 0., 4., 0.], [ 1., 4., 0.], [ 2., 4., 0.], [ 3., 4., 0.], [ 4., 4., 0.], [ 5., 4., 0.], [ 6., 4., 0.], [ 0., 5., 0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32), np.array([[ 0.,  0.,  0.], [ 1.,  0.,  0.], [ 2.,  0.,  0.], [ 3.,  0.,  0.], [ 4.,  0.,  0.], [ 5.,  0.,  0.], [ 6.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  1.,  0.], [ 2.,  1.,  0.], [ 3.,  1.,  0.], [ 4.,  1.,  0.], [ 5.,  1.,  0.], [ 6.,  1.,  0.], [ 0.,  2.,  0.], [ 1.,  2.,  0.], [ 2.,  2.,  0.], [ 3.,  2.,  0.], [ 4.,  2.,  0.], [ 5.,  2.,  0.], [ 6.,  2.,  0.], [ 0.,  3.,  0.], [ 1.,  3.,  0.], [ 2.,  3.,  0.], [ 3.,  3.,  0.], [ 4.,  3.,  0.], [ 5.,  3.,  0.], [ 6.,  3.,  0.], [ 0.,  4.,  0.], [ 1.,  4.,  0.], [ 2.,  4.,  0.], [ 3.,  4.,  0.], [ 4.,  4.,  0.], [ 5.,  4.,  0.], [ 6.,  4.,  0.], [ 0.,  5.,  0.], [ 1.,  5.,  0.], [ 2.,  5.,  0.], [ 3.,  5.,  0.], [ 4.,  5.,  0.], [ 5.,  5.,  0.], [ 6.,  5.,  0.]], dtype=np.float32)])

imgpoints = np.array([[[ 2147.49560547,   531.77355957]], \
       [[ 2110.44946289,   721.54351807]], \
       [[ 2078.42822266,   894.07897949]], \
       [[ 2049.28198242,  1050.30224609]], \
       [[ 2023.38183594,  1189.21459961]], \
       [[ 1999.60559082,  1315.90795898]], \
       [[ 1978.38537598,  1434.18652344]], \
       [[ 1937.20043945,   525.61346436]], \
       [[ 1911.70678711,   715.65576172]], \
       [[ 1888.98999023,   886.68725586]], \
       [[ 1869.24633789,  1042.0333252 ]], \
       [[ 1851.3203125 ,  1181.87084961]], \
       [[ 1835.07104492,  1310.53613281]], \
       [[ 1820.66491699,  1430.49377441]], \
       [[ 1726.38928223,   519.45068359]], \
       [[ 1712.30493164,   709.90142822]], \
       [[ 1700.09606934,   881.19189453]], \
       [[ 1689.03442383,  1035.89440918]], \
       [[ 1679.29333496,  1177.55053711]], \
       [[ 1670.47949219,  1306.9017334 ]], \
       [[ 1662.24060059,  1428.00183105]], \
       [[ 1513.67675781,   511.99185181]], \
       [[ 1511.3729248 ,   704.19812012]], \
       [[ 1509.91638184,   876.79101562]], \
       [[ 1507.87646484,  1032.36584473]], \
       [[ 1505.82287598,  1174.09680176]], \
       [[ 1504.46105957,  1304.48864746]], \
       [[ 1502.64404297,  1426.1809082 ]], \
       [[ 1297.6484375 ,   503.65609741]], \
       [[ 1307.53125   ,   697.38031006]], \
       [[ 1316.5411377 ,   871.54852295]], \
       [[ 1323.88378906,  1028.45739746]], \
       [[ 1330.54956055,  1170.96765137]], \
       [[ 1336.42700195,  1302.41564941]], \
       [[ 1341.3145752 ,  1424.78198242]], \
       [[ 1077.32910156,   494.49224854]], \
       [[ 1099.97839355,   689.89788818]], \
       [[ 1119.5501709 ,   866.20556641]], \
       [[ 1136.86010742,  1024.60388184]], \
       [[ 1152.3392334 ,  1168.75146484]], \
       [[ 1165.71411133,  1300.65698242]], \
       [[ 1177.20349121,  1423.33789062]]], dtype=np.float32), np.array([[[  803.01507568,   656.50177002]], \
       [[ 1013.55310059,   690.824646  ]], \
       [[ 1204.08642578,   721.14117432]], \
       [[ 1374.94812012,   748.28771973]], \
       [[ 1526.47290039,   772.09100342]], \
       [[ 1663.16259766,   794.11895752]], \
       [[ 1790.45483398,   812.65563965]], \
       [[  803.95550537,   884.97216797]], \
       [[ 1013.47570801,   906.56384277]], \
       [[ 1200.92785645,   925.43103027]], \
       [[ 1369.36462402,   942.13293457]], \
       [[ 1521.07214355,   956.89428711]], \
       [[ 1658.92077637,   969.75939941]], \
       [[ 1786.9440918 ,   981.34088135]], \
       [[  805.08251953,  1111.42224121]], \
       [[ 1013.88897705,  1119.57434082]], \
       [[ 1200.28234863,  1126.94836426]], \
       [[ 1367.3848877 ,  1133.19116211]], \
       [[ 1518.35168457,  1138.84521484]], \
       [[ 1656.76245117,  1143.55163574]], \
       [[ 1785.00793457,  1147.78063965]], \
       [[  805.33917236,  1336.43273926]], \
       [[ 1014.30102539,  1331.08813477]], \
       [[ 1200.2043457 ,  1326.6529541 ]], \
       [[ 1366.93591309,  1322.79382324]], \
       [[ 1517.16247559,  1319.34399414]], \
       [[ 1654.8918457 ,  1315.9498291 ]], \
       [[ 1783.46643066,  1313.03063965]], \
       [[  804.6451416 ,  1560.45874023]], \
       [[ 1013.25427246,  1541.97570801]], \
       [[ 1199.70068359,  1525.7487793 ]], \
       [[ 1366.09265137,  1511.67956543]], \
       [[ 1516.56420898,  1498.92883301]], \
       [[ 1654.26586914,  1487.92492676]], \
       [[ 1782.33435059,  1478.28955078]], \
       [[  803.4487915 ,  1785.4588623 ]], \
       [[ 1011.69732666,  1753.73852539]], \
       [[ 1198.54968262,  1725.93273926]], \
       [[ 1365.59790039,  1701.17663574]], \
       [[ 1515.96105957,  1679.48693848]], \
       [[ 1654.03381348,  1660.32409668]], \
       [[ 1781.46765137,  1643.28820801]]], dtype=np.float32), np.array([[[ 2708.64111328,  2057.04931641]], \
       [[ 2487.54443359,  1994.6282959 ]], \
       [[ 2289.10986328,  1940.96789551]], \
       [[ 2112.42480469,  1892.73535156]], \
       [[ 1957.9284668 ,  1849.44921875]], \
       [[ 1820.31774902,  1810.36572266]], \
       [[ 1693.24755859,  1776.5291748 ]], \
       [[ 2707.84057617,  1825.13769531]], \
       [[ 2485.23828125,  1776.78540039]], \
       [[ 2287.05810547,  1734.39294434]], \
       [[ 2111.34350586,  1697.12719727]], \
       [[ 1955.70117188,  1664.81555176]], \
       [[ 1815.79858398,  1635.68725586]], \
       [[ 1687.09533691,  1610.36547852]], \
       [[ 2705.99951172,  1590.66992188]], \
       [[ 2480.98852539,  1556.36645508]], \
       [[ 2281.81542969,  1527.32348633]], \
       [[ 2106.45068359,  1502.17431641]], \
       [[ 1950.32128906,  1479.95471191]], \
       [[ 1809.01757812,  1460.53027344]], \
       [[ 1679.15368652,  1443.00158691]], \
       [[ 2703.96704102,  1351.36535645]], \
       [[ 2476.64477539,  1333.2557373 ]], \
       [[ 2276.70825195,  1317.9453125 ]], \
       [[ 2100.35620117,  1305.11218262]], \
       [[ 1943.36608887,  1293.1907959 ]], \
       [[ 1801.38867188,  1282.8215332 ]], \
       [[ 1670.98937988,  1273.70349121]], \
       [[ 2703.37182617,  1106.60791016]], \
       [[ 2473.640625  ,  1105.59301758]], \
       [[ 2271.2956543 ,  1104.73632812]], \
       [[ 2094.01928711,  1103.95214844]], \
       [[ 1935.72302246,  1102.91418457]], \
       [[ 1792.96472168,  1102.0892334 ]], \
       [[ 1661.61193848,  1101.37280273]], \
       [[ 2702.90185547,   855.79870605]], \
       [[ 2470.94433594,   871.53485107]], \
       [[ 2266.34741211,   885.76202393]], \
       [[ 2087.04882812,   898.05786133]], \
       [[ 1927.42358398,   908.48834229]], \
       [[ 1783.69519043,   917.03186035]], \
       [[ 1652.07910156,   924.59405518]]], dtype=np.float32), np.array([[[ 1560.5625    ,  1457.58959961]], \
       [[ 1565.65563965,  1275.87329102]], \
       [[ 1570.60168457,  1102.71679688]], \
       [[ 1575.04626465,   938.97546387]], \
       [[ 1579.83813477,   787.34411621]], \
       [[ 1584.01464844,   643.51220703]], \
       [[ 1587.80969238,   504.34869385]], \
       [[ 1764.50170898,  1455.36413574]], \
       [[ 1763.16479492,  1273.82348633]], \
       [[ 1762.36547852,  1102.39978027]], \
       [[ 1761.33569336,   940.16656494]], \
       [[ 1760.50305176,   786.80413818]], \
       [[ 1760.0579834 ,   641.2822876 ]], \
       [[ 1759.60241699,   500.82015991]], \
       [[ 1971.32653809,  1452.98510742]], \
       [[ 1962.57763672,  1270.63110352]], \
       [[ 1954.70861816,  1099.41503906]], \
       [[ 1948.35144043,   936.9543457 ]], \
       [[ 1942.59387207,   783.47479248]], \
       [[ 1937.15393066,   636.91418457]], \
       [[ 1932.82434082,   494.76556396]], \
       [[ 2181.52587891,  1450.58276367]], \
       [[ 2165.31665039,  1266.77783203]], \
       [[ 2150.83129883,  1093.90869141]], \
       [[ 2138.11938477,   931.00378418]], \
       [[ 2127.1574707 ,   777.02337646]], \
       [[ 2116.90869141,   629.99981689]], \
       [[ 2107.92114258,   487.61691284]], \
       [[ 2397.30688477,  1447.94812012]], \
       [[ 2372.41601562,  1262.58728027]], \
       [[ 2351.23950195,  1088.15991211]], \
       [[ 2332.21679688,   924.56274414]], \
       [[ 2314.84741211,   769.63494873]], \
       [[ 2299.37841797,   622.02984619]], \
       [[ 2285.36328125,   479.88140869]], \
       [[ 2617.59667969,  1445.47302246]], \
       [[ 2585.0065918 ,  1258.09899902]], \
       [[ 2556.12939453,  1081.67431641]], \
       [[ 2530.00244141,   916.89746094]], \
       [[ 2506.28857422,   761.01416016]], \
       [[ 2484.72387695,   613.33880615]], \
       [[ 2464.91772461,   471.6053772 ]]], dtype=np.float32), np.array([[[ 1966.44445801,  2011.09985352]], \
       [[ 1843.39196777,  1883.87988281]], \
       [[ 1727.00805664,  1766.96179199]], \
       [[ 1618.06872559,  1658.51135254]], \
       [[ 1519.01672363,  1556.56652832]], \
       [[ 1425.55371094,  1460.42224121]], \
       [[ 1335.58300781,  1370.68066406]], \
       [[ 2045.62414551,  1880.43688965]], \
       [[ 1916.99243164,  1753.8770752 ]], \
       [[ 1796.85144043,  1638.57678223]], \
       [[ 1684.54150391,  1531.0567627 ]], \
       [[ 1579.70214844,  1430.84875488]], \
       [[ 1480.98217773,  1336.85888672]], \
       [[ 1385.80236816,  1248.26989746]], \
       [[ 2129.18408203,  1742.37646484]], \
       [[ 1993.59277344,  1618.07226562]], \
       [[ 1868.02453613,  1504.16589355]], \
       [[ 1750.68640137,  1398.24926758]], \
       [[ 1640.83117676,  1299.77392578]], \
       [[ 1536.97351074,  1207.27270508]], \
       [[ 1437.26574707,  1120.32739258]], \
       [[ 2218.24243164,  1596.05151367]], \
       [[ 2074.85058594,  1473.69104004]], \
       [[ 1941.96362305,  1362.04223633]], \
       [[ 1819.06628418,  1258.00622559]], \
       [[ 1703.90319824,  1161.27270508]], \
       [[ 1595.16455078,  1070.49157715]], \
       [[ 1490.45666504,   984.48345947]], \
       [[ 2314.4519043 ,  1439.95214844]], \
       [[ 2162.05395508,  1320.33666992]], \
       [[ 2021.27331543,  1210.55578613]], \
       [[ 1891.53417969,  1108.77050781]], \
       [[ 1770.36450195,  1013.64117432]], \
       [[ 1656.28613281,   924.45349121]], \
       [[ 1546.88232422,   840.77478027]], \
       [[ 2418.16918945,  1272.14331055]], \
       [[ 2255.63110352,  1155.6237793 ]], \
       [[ 2105.93164062,  1048.47180176]], \
       [[ 1968.49645996,   949.26409912]], \
       [[ 1840.67944336,   856.29827881]], \
       [[ 1720.45837402,   769.49902344]], \
       [[ 1606.52453613,   687.02368164]]], dtype=np.float32), np.array([[[ 1324.11865234,  1485.13647461]], \
       [[ 1437.84924316,  1348.53564453]], \
       [[ 1543.16931152,  1218.83410645]], \
       [[ 1641.76062012,  1097.08203125]], \
       [[ 1733.67565918,   985.5713501 ]], \
       [[ 1820.87988281,   880.23065186]], \
       [[ 1902.89501953,   778.57452393]], \
       [[ 1484.90246582,  1574.76745605]], \
       [[ 1595.21179199,  1432.19384766]], \
       [[ 1697.46459961,  1298.64758301]], \
       [[ 1792.69970703,  1173.49206543]], \
       [[ 1882.54589844,  1056.05908203]], \
       [[ 1966.56567383,   944.81848145]], \
       [[ 2046.85437012,   837.98748779]], \
       [[ 1653.29443359,  1668.64794922]], \
       [[ 1759.91491699,  1518.82958984]], \
       [[ 1858.68188477,  1379.12365723]], \
       [[ 1950.93444824,  1248.81237793]], \
       [[ 2037.51635742,  1126.53173828]], \
       [[ 2119.6796875 ,  1009.86529541]], \
       [[ 2197.43725586,   898.16204834]], \
       [[ 1831.40075684,  1767.74829102]], \
       [[ 1934.11169434,  1609.75097656]], \
       [[ 2029.10266113,  1462.86962891]], \
       [[ 2117.93505859,  1326.47741699]], \
       [[ 2201.47192383,  1198.13977051]], \
       [[ 2280.66137695,  1076.7097168 ]], \
       [[ 2356.07617188,   960.31616211]], \
       [[ 2021.48828125,  1874.7512207 ]], \
       [[ 2119.41210938,  1706.70129395]], \
       [[ 2210.21386719,  1551.48132324]], \
       [[ 2295.02954102,  1407.86083984]], \
       [[ 2375.45483398,  1273.43444824]], \
       [[ 2451.11010742,  1146.57568359]], \
       [[ 2523.43164062,  1025.22387695]], \
       [[ 2225.50927734,  1988.84277344]], \
       [[ 2317.9230957 ,  1810.51843262]], \
       [[ 2404.31860352,  1645.52124023]], \
       [[ 2484.734375  ,  1494.01916504]], \
       [[ 2560.68481445,  1352.27844238]], \
       [[ 2632.0871582 ,  1219.60620117]], \
       [[ 2700.27905273,  1093.61035156]]], dtype=np.float32), np.array([[[ 1499.39086914,   576.94226074]], \
       [[ 1631.10998535,   694.11895752]], \
       [[ 1753.04602051,   798.80322266]], \
       [[ 1864.76879883,   893.64868164]], \
       [[ 1963.86938477,   979.887146  ]], \
       [[ 2054.50854492,  1059.00842285]], \
       [[ 2141.05688477,  1131.66662598]], \
       [[ 1428.25244141,   754.81463623]], \
       [[ 1565.04455566,   863.83111572]], \
       [[ 1689.96386719,   962.42675781]], \
       [[ 1804.22314453,  1051.14587402]], \
       [[ 1908.16149902,  1131.64233398]], \
       [[ 2004.18188477,  1205.82092285]], \
       [[ 2095.40625   ,  1274.1138916 ]], \
       [[ 1355.46801758,   938.01525879]], \
       [[ 1498.22570801,  1039.6385498 ]], \
       [[ 1627.9107666 ,  1130.64160156]], \
       [[ 1746.07592773,  1212.87731934]], \
       [[ 1854.47338867,  1287.61132812]], \
       [[ 1954.98596191,  1356.53417969]], \
       [[ 2049.95581055,  1420.24450684]], \
       [[ 1279.55969238,  1128.57006836]], \
       [[ 1429.57336426,  1221.86132812]], \
       [[ 1565.10754395,  1304.98034668]], \
       [[ 1688.25854492,  1380.43237305]], \
       [[ 1800.74780273,  1449.47412109]], \
       [[ 1905.69152832,  1512.41479492]], \
       [[ 2004.14562988,  1571.49914551]], \
       [[ 1200.06286621,  1326.77319336]], \
       [[ 1357.92382812,  1410.77319336]], \
       [[ 1500.27404785,  1486.48730469]], \
       [[ 1628.66003418,  1554.85009766]], \
       [[ 1746.1229248 ,  1616.96398926]], \
       [[ 1854.94250488,  1674.78662109]], \
       [[ 1957.48583984,  1728.36804199]], \
       [[ 1116.03442383,  1535.47253418]], \
       [[ 1282.49365234,  1609.71948242]], \
       [[ 1432.31005859,  1676.71679688]], \
       [[ 1567.53710938,  1737.31054688]], \
       [[ 1690.01391602,  1792.88208008]], \
       [[ 1803.44677734,  1844.14648438]], \
       [[ 1909.37438965,  1892.35742188]]], dtype=np.float32), np.array([[[ 2544.39575195,   593.71673584]], \
       [[ 2410.5222168 ,   738.73822021]], \
       [[ 2289.57592773,   869.99920654]], \
       [[ 2182.55810547,   990.97613525]], \
       [[ 2084.71118164,  1097.35595703]], \
       [[ 1996.2076416 ,  1190.45300293]], \
       [[ 1916.38378906,  1280.09680176]], \
       [[ 2376.11889648,   515.16290283]], \
       [[ 2246.77026367,   666.88922119]], \
       [[ 2136.18188477,   804.515625  ]], \
       [[ 2030.36987305,   928.83282471]], \
       [[ 1939.81384277,  1038.80859375]], \
       [[ 1857.08178711,  1141.18017578]], \
       [[ 1781.44177246,  1234.55334473]], \
       [[ 2199.38061523,   431.92602539]], \
       [[ 2078.56665039,   592.75280762]], \
       [[ 1973.30212402,   737.96807861]], \
       [[ 1877.29614258,   867.29302979]], \
       [[ 1792.02148438,   981.52819824]], \
       [[ 1712.68444824,  1088.14953613]], \
       [[ 1642.23449707,  1187.40771484]], \
       [[ 2014.44470215,   346.73574829]], \
       [[ 1902.25097656,   516.29992676]], \
       [[ 1803.9967041 ,   668.24822998]], \
       [[ 1712.83154297,   804.66442871]], \
       [[ 1635.42944336,   927.01904297]], \
       [[ 1561.30297852,  1037.43225098]], \
       [[ 1495.94750977,  1139.16333008]], \
       [[ 1820.05834961,   252.78707886]], \
       [[ 1715.45996094,   432.93151855]], \
       [[ 1624.88781738,   594.47735596]], \
       [[ 1542.98803711,   737.48242188]], \
       [[ 1470.1829834 ,   865.12194824]], \
       [[ 1404.71582031,   981.79626465]], \
       [[ 1344.26306152,  1089.55383301]], \
       [[ 1611.0769043 ,   153.14749146]], \
       [[ 1517.63098145,   346.43798828]], \
       [[ 1437.09643555,   517.58636475]], \
       [[ 1364.36938477,   667.04626465]], \
       [[ 1297.67797852,   801.503479  ]], \
       [[ 1238.40234375,   923.78588867]], \
       [[ 1183.54931641,  1034.68371582]]], dtype=np.float32), np.array([[[ 1594.61633301,  1807.49072266]], \
       [[ 1553.62927246,  1657.10803223]], \
       [[ 1512.32177734,  1507.41516113]], \
       [[ 1470.27453613,  1354.60388184]], \
       [[ 1427.55529785,  1198.60510254]], \
       [[ 1383.97766113,  1039.94824219]], \
       [[ 1339.21142578,   880.35418701]], \
       [[ 1749.44311523,  1767.81018066]], \
       [[ 1708.72546387,  1617.27685547]], \
       [[ 1667.9609375 ,  1466.35290527]], \
       [[ 1626.85314941,  1312.88977051]], \
       [[ 1585.0579834 ,  1155.99963379]], \
       [[ 1542.36242676,   997.58288574]], \
       [[ 1498.88366699,   837.44281006]], \
       [[ 1905.18164062,  1729.42150879]], \
       [[ 1864.91381836,  1577.81762695]], \
       [[ 1824.78051758,  1425.76965332]], \
       [[ 1783.71777344,  1270.8840332 ]], \
       [[ 1742.72900391,  1113.49279785]], \
       [[ 1701.29187012,   954.48217773]], \
       [[ 1659.16784668,   794.11352539]], \
       [[ 2062.80029297,  1690.92358398]], \
       [[ 2022.54870605,  1538.7277832 ]], \
       [[ 1982.62402344,  1385.4798584 ]], \
       [[ 1942.4095459 ,  1229.31982422]], \
       [[ 1902.46325684,  1070.58862305]], \
       [[ 1861.45410156,   910.8526001 ]], \
       [[ 1821.10705566,   749.24407959]], \
       [[ 2223.21337891,  1653.00463867]], \
       [[ 2182.88818359,  1499.43701172]], \
       [[ 2143.21728516,  1344.38366699]], \
       [[ 2103.51904297,  1186.81884766]], \
       [[ 2063.8359375 ,  1027.20043945]], \
       [[ 2024.24475098,   866.42169189]], \
       [[ 1985.05041504,   703.6260376 ]], \
       [[ 2386.265625  ,  1614.51037598]], \
       [[ 2346.44335938,  1459.79663086]], \
       [[ 2306.50024414,  1302.97241211]], \
       [[ 2267.28955078,  1143.5847168 ]], \
       [[ 2228.50512695,   982.74938965]], \
       [[ 2190.11083984,   821.00292969]], \
       [[ 2151.83813477,   656.66137695]]], dtype=np.float32), np.array([[[ 1579.96240234,  1944.08349609]], \
       [[ 1582.51721191,  1779.57263184]], \
       [[ 1585.22497559,  1617.32763672]], \
       [[ 1585.78356934,  1456.5715332 ]], \
       [[ 1587.43847656,  1297.60302734]], \
       [[ 1589.53820801,  1137.6151123 ]], \
       [[ 1589.51330566,   978.32696533]], \
       [[ 1744.46569824,  1946.43188477]], \
       [[ 1744.70507812,  1781.58703613]], \
       [[ 1745.4206543 ,  1618.54125977]], \
       [[ 1747.84277344,  1457.95666504]], \
       [[ 1748.0255127 ,  1298.69689941]], \
       [[ 1749.31140137,  1139.84777832]], \
       [[ 1749.78161621,   980.37701416]], \
       [[ 1908.37841797,  1949.25048828]], \
       [[ 1906.83129883,  1781.77270508]], \
       [[ 1907.85266113,  1620.61437988]], \
       [[ 1908.06958008,  1459.61816406]], \
       [[ 1908.41418457,  1301.65490723]], \
       [[ 1909.49353027,  1141.80908203]], \
       [[ 1910.9909668 ,   982.43103027]], \
       [[ 2072.58154297,  1952.80078125]], \
       [[ 2069.72485352,  1787.69677734]], \
       [[ 2070.05029297,  1622.6361084 ]], \
       [[ 2069.68969727,  1461.83959961]], \
       [[ 2068.98754883,  1301.48034668]], \
       [[ 2070.69213867,  1143.55334473]], \
       [[ 2071.44067383,   983.82788086]], \
       [[ 2237.97167969,  1958.00366211]], \
       [[ 2234.48339844,  1790.015625  ]], \
       [[ 2233.30810547,  1627.44091797]], \
       [[ 2233.84326172,  1465.62365723]], \
       [[ 2231.86987305,  1304.70300293]], \
       [[ 2233.48754883,  1144.77404785]], \
       [[ 2235.37280273,   984.86901855]], \
       [[ 2406.23339844,  1962.21801758]], \
       [[ 2403.5       ,  1795.5       ]], \
       [[ 2399.88647461,  1631.48010254]], \
       [[ 2398.6862793 ,  1467.5546875 ]], \
       [[ 2398.30297852,  1306.37561035]], \
       [[ 2398.16113281,  1145.69677734]], \
       [[ 2398.64575195,   985.6104126 ]]], dtype=np.float32), np.array([[[ 2297.77905273,  1635.88513184]], \
       [[ 2107.80322266,  1634.89111328]], \
       [[ 1916.93273926,  1634.16833496]], \
       [[ 1728.8137207 ,  1631.84130859]], \
       [[ 1542.11865234,  1631.50146484]], \
       [[ 1351.14782715,  1632.60217285]], \
       [[ 1159.13598633,  1632.75878906]], \
       [[ 2290.2902832 ,  1446.46520996]], \
       [[ 2103.12670898,  1446.49035645]], \
       [[ 1917.30444336,  1444.97302246]], \
       [[ 1729.43395996,  1444.71191406]], \
       [[ 1542.58300781,  1444.0670166 ]], \
       [[ 1356.7220459 ,  1444.62341309]], \
       [[ 1164.41760254,  1443.63635254]], \
       [[ 2286.50170898,  1262.43505859]], \
       [[ 2099.8828125 ,  1262.12927246]], \
       [[ 1915.04321289,  1261.8203125 ]], \
       [[ 1730.69116211,  1261.28723145]], \
       [[ 1545.27880859,  1259.08288574]], \
       [[ 1359.44897461,  1260.24450684]], \
       [[ 1170.3659668 ,  1257.0357666 ]], \
       [[ 2282.63964844,  1082.77062988]], \
       [[ 2097.76708984,  1082.29907227]], \
       [[ 1914.41479492,  1081.5447998 ]], \
       [[ 1731.57946777,  1080.90380859]], \
       [[ 1547.51086426,  1077.29663086]], \
       [[ 1362.52502441,  1074.82873535]], \
       [[ 1175.16882324,  1072.77478027]], \
       [[ 2281.03417969,   900.86853027]], \
       [[ 2096.46435547,   903.4418335 ]], \
       [[ 1914.37365723,   900.58612061]], \
       [[ 1733.07397461,   901.04986572]], \
       [[ 1549.14245605,   897.78167725]], \
       [[ 1365.03735352,   895.02526855]], \
       [[ 1179.1427002 ,   890.85858154]], \
       [[ 2278.67382812,   723.97454834]], \
       [[ 2097.47290039,   724.18652344]], \
       [[ 1915.45166016,   722.7409668 ]], \
       [[ 1732.54431152,   721.78497314]], \
       [[ 1551.50891113,   719.77172852]], \
       [[ 1369.16870117,   715.07220459]], \
       [[ 1182.06274414,   710.12359619]]], dtype=np.float32), np.array([[[ 1220.27355957,  1849.11291504]], \
       [[ 1198.16821289,  1636.80749512]], \
       [[ 1176.99377441,  1427.28747559]], \
       [[ 1152.94555664,  1219.79187012]], \
       [[ 1129.48876953,  1013.14007568]], \
       [[ 1105.38024902,   805.25585938]], \
       [[ 1079.89147949,   596.10772705]], \
       [[ 1431.33691406,  1824.62084961]], \
       [[ 1408.78271484,  1612.07141113]], \
       [[ 1385.80200195,  1404.05224609]], \
       [[ 1361.8404541 ,  1197.16540527]], \
       [[ 1337.20263672,   990.62078857]], \
       [[ 1314.79882812,   782.84472656]], \
       [[ 1289.35192871,   574.55828857]], \
       [[ 1641.11999512,  1797.41296387]], \
       [[ 1616.89599609,  1586.74035645]], \
       [[ 1593.65258789,  1378.2487793 ]], \
       [[ 1569.68725586,  1173.86132812]], \
       [[ 1546.10473633,   967.484375  ]], \
       [[ 1522.67492676,   761.72076416]], \
       [[ 1497.10119629,   551.44586182]], \
       [[ 1849.93676758,  1773.33752441]], \
       [[ 1825.36938477,  1563.02380371]], \
       [[ 1799.81555176,  1354.45959473]], \
       [[ 1775.16662598,  1149.42480469]], \
       [[ 1750.84118652,   942.40350342]], \
       [[ 1728.67248535,   737.03118896]], \
       [[ 1705.15002441,   526.77972412]], \
       [[ 2061.99780273,  1752.94042969]], \
       [[ 2036.22229004,  1539.81079102]], \
       [[ 2009.4576416 ,  1331.44238281]], \
       [[ 1984.18994141,  1126.09936523]], \
       [[ 1959.72106934,   917.97943115]], \
       [[ 1938.03417969,   712.97875977]], \
       [[ 1914.12011719,   502.30377197]], \
       [[ 2277.44897461,  1731.66992188]], \
       [[ 2246.2355957 ,  1517.70068359]], \
       [[ 2218.98510742,  1308.20153809]], \
       [[ 2194.78442383,  1099.37719727]], \
       [[ 2168.23095703,   890.97247314]], \
       [[ 2145.44360352,   686.31591797]], \
       [[ 2123.42773438,   475.35968018]]], dtype=np.float32)


## gray.shape[::-1] = (3280, 2464)
resolution = (3280, 2464)

imgpoints2 = np.array([[[ 1219.25622559,  1849.18664551]], \
       [[ 1197.61450195,  1637.09558105]], \
       [[ 1175.50341797,  1427.90368652]], \
       [[ 1152.73156738,  1220.45263672]], \
       [[ 1129.18530273,  1013.54321289]], \
       [[ 1104.85009766,   806.09558105]], \
       [[ 1079.97155762,   597.46697998]], \
       [[ 1430.77087402,  1823.07849121]], \
       [[ 1407.93017578,  1611.79248047]], \
       [[ 1384.96972656,  1403.43945312]], \
       [[ 1361.74157715,  1196.78088379]], \
       [[ 1338.11584473,   990.59191895]], \
       [[ 1313.99206543,   783.71917725]], \
       [[ 1289.40405273,   575.31219482]], \
       [[ 1640.96240234,  1798.04846191]], \
       [[ 1616.8059082 ,  1587.23925781]], \
       [[ 1592.94091797,  1379.32800293]], \
       [[ 1569.22351074,  1173.0559082 ]], \
       [[ 1545.5135498 ,   967.20269775]], \
       [[ 1521.67797852,   760.5916748 ]], \
       [[ 1497.64160156,   552.28033447]], \
       [[ 1850.98193359,  1774.04187012]], \
       [[ 1825.45507812,  1563.31066895]], \
       [[ 1800.64318848,  1355.42810059]], \
       [[ 1776.39221191,  1149.13708496]], \
       [[ 1752.55310059,   943.22015381]], \
       [[ 1728.98083496,   736.5020752 ]], \
       [[ 1705.53527832,   528.04174805]], \
       [[ 2062.05444336,  1750.91772461]], \
       [[ 2035.11450195,  1539.86230469]], \
       [[ 2009.30065918,  1331.59790039]], \
       [[ 1984.46276855,  1124.88537598]], \
       [[ 1960.44152832,   918.50708008]], \
       [[ 1937.06994629,   711.3147583 ]], \
       [[ 1914.13000488,   502.46636963]], \
       [[ 2275.32885742,  1728.47583008]], \
       [[ 2246.99414062,  1516.74133301]], \
       [[ 2220.13208008,  1307.6965332 ]], \
       [[ 2194.64355469,  1100.16259766]], \
       [[ 2170.359375  ,   892.94543457]], \
       [[ 2147.05371094,   684.97766113]], \
       [[ 2124.36645508,   475.6427002 ]]], dtype=np.float32)

