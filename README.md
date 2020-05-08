# KickStart 2018 Practice Round (Problem A. GBus count)

Problem
There exist some cities that are built along a straight road. The cities are numbered 1, 2, 3... from left to right.

There are N GBuses that operate along this road. For each GBus, we know the range of cities that it serves: the i-th gBus serves the cities with numbers between Ai and Bi, inclusive.

We are interested in a particular subset of P cities. For each of those cities, we need to find out how many GBuses serve that particular city.

Input
The first line of the input gives the number of test cases, T. Then, T test cases follow; each case is separated from the next by one blank line. (Notice that this is unusual for Kickstart data sets.)

In each test case:

The first line contains one integer N: the number of GBuses.
The second line contains 2N integers representing the ranges of cities that the buses serve, in the form A1 B1 A2 B2 A3 B3 ... AN BN. That is, the first GBus serves the cities numbered from A1 to B1 (inclusive), and so on.
The third line contains one integer P: the number of cities we are interested in, as described above. (Note that this is not necessarily the same as the total number of cities in the problem, which is not given.)
Finally, there are P more lines; the i-th of these contains the number Ci of a city we are interested in.
Output
For each test case, output one line containing Case #x: y, where x is the number of the test case (starting from 1), and y is a list of P integers, in which the i-th integer is the number of GBuses that serve city Ci.

Limits
1 ≤ T ≤ 10.
Small dataset
1 ≤ N ≤ 50 
1 ≤ Ai ≤ 500, for all i.
1 ≤ Bi ≤ 500, for all i.
1 ≤ Ci ≤ 500, for all i.
1 ≤ P ≤ 50.
Large dataset
1 ≤ N ≤ 500.
1 ≤ Ai ≤ 5000, for all i.
1 ≤ Bi ≤ 5000, for all i.
1 ≤ Ci ≤ 5000, for all i.
1 ≤ P ≤ 500.
Sample

Input 
 	
2
4
15 25 30 35 45 50 10 20
2
15
25

10
10 15 5 12 40 55 1 10 25 35 45 50 20 28 27 35 15 40 4 5
3
5
10
27



Output 
 
Case #1: 2 1
Case #2: 3 3 4

In Sample Case #1, there are four GBuses. The first serves cities 15 through 25, the second serves cities 30 through 35, the third serves cities 45 through 50, and the fourth serves cities 10 through 20. City 15 is served by the first and fourth buses, so the first number in our answer list is 2. City 25 is served by only the first bus, so the second number in our answer list is 1.
[![Run on Repl.it](https://repl.it/badge/github/akat5uki/test1)](https://repl.it/github/akat5uki/test1)