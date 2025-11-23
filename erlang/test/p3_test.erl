-module(p3_test).
-include_lib("eunit/include/eunit.hrl").

sum_even_test_() ->
    [
        ?_assertEqual(30, p3:sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
        ?_assertEqual(150, p3:sum_even([10, 20, 30, 40, 50])),
        ?_assertEqual(0, p3:sum_even([9, 7, 5, 3, 1]))
    ].

sum_even_2_test_() ->
    [
        ?_assertEqual(30, p3:sum_even_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
        ?_assertEqual(150, p3:sum_even_2([10, 20, 30, 40, 50])),
        ?_assertEqual(0, p3:sum_even_2([9, 7, 5, 3, 1]))
    ].

sum_even_3_test_() ->
    [
        ?_assertEqual(30, p3:sum_even_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
        ?_assertEqual(150, p3:sum_even_3([10, 20, 30, 40, 50])),
        ?_assertEqual(0, p3:sum_even_3([9, 7, 5, 3, 1]))
    ].
