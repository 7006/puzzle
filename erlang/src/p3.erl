-module(p3).
-export([sum_even/1]).
-export([sum_even_2/1]).
-export([sum_even_3/1]).

sum_even(InputNums) ->
    lists:sum([Num || Num <- InputNums, Num rem 2 =:= 0]).

sum_even_2(InputNums) ->
    sum_even_2(InputNums, 0).

sum_even_2([], Sum) ->
    Sum;
sum_even_2([Num | InputNums], Sum) when Num rem 2 =:= 0 ->
    sum_even_2(InputNums, Sum + Num);
sum_even_2([_Num | InputNums], Sum) ->
    sum_even_2(InputNums, Sum).

sum_even_3(InputNums) ->
    Fn = fun
        (Num, Sum) when Num rem 2 =:= 0 ->
            Sum + Num;
        (_Num, Sum) ->
            Sum
    end,
    lists:foldl(Fn, 0, InputNums).
