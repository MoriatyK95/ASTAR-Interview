function [cc] = labelconnectedcomponent(filename)
% FUNCTION[CC] = LABELCONNECTEDCOMPONENT(ADJMATRIX)
% Inputs: input file's name (string)
% Outputs: labeled connected component m by n matrix

 
adjmatrix = readmatrix(filename); %read input file and turn it into a matrix

cc = bwlabel(adjmatrix,4);   %using matlab's image processing tool bwlabel to label connected component
%with connectivity of 4

dlmwrite('output_question_4', cc, ' ')  %write cc into a file

end

