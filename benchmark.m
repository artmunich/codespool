%Benckmark by MATLAB
%This program will compare the speed of your computer with others.
%At the end, a bar-figure will be plotted and printed out.
%
%Author: Xiaowei Huai
%2015/7/3

clear;close all;clc;
bench

set(1,'PaperPositionMode','manual');
set(1,'PaperUnits','points')
set(1,'PaperPosition',[0 0 800 400])

print -f1 -dpng -r300 matlabbench