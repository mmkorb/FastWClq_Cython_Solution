Introduction
============

FastWClq is a solver for maximum vertex weighted clique problem, and is particularly efficient for large sparse graphs.

Authors: It is developed by Shaowei Cai (Institute of Software, Chinese Academy of Sciences) and Jinkun Lin (Peking University). 

Contact: If you have any question, please send an email to caisw@ios.ac.cn.

FastWClq was implemented in c++ 11. If there is a problem in running the file, you may need to update  your g++ compiler to be able to handle c++ 11.

It is published in the following paper:
Shaowei Cai, Jinkun Lin: Fast Solving Maximum Weight Clique Problem in Massive Graphs. IJCAI 2016: 568-574.

The benchmark used to test this solver in the paper can be downloaded from http://lcs.ios.ac.cn/~caisw/Resource/weighted-massive-graphs.zip



Running Command
===============

#min and max are two parameters of the algorithm, and the default values of them are 4 and 64 respectively.
#random-seed is the random seed for running the algorithm, as it uses randomized choices.
#cutoff-time is the time limit for each run. But if the algorithm can exactly solve the instance, it terminates immediately. Otherwise, the algorithm finishes upon reaching the time limit and returns the best found solution and the time to get this solution.

min=4
max=64
./fast-wclq $file $random-seed $cutoff-time $min $max


