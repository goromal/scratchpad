g=9.81;
m=2;
ml=1;
mr=1;
mu=0.2;
d=1;
Jc=1;

T1=tf(1,[ml*d+mr*d+Jc 0 0]);
T2=tf(-g*(m+ml+mr),[m+ml+mr mu 0]);

bode(T1*T2)

