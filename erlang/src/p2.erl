-module(p2).

-export([sum_if_less_than_fifty/2]).

sum_if_less_than_fifty(NumOne, NumTwo) when NumOne + NumTwo < 50 ->
    NumOne + NumTwo;
sum_if_less_than_fifty(_NumOne, _NumTwo) ->
    none.
