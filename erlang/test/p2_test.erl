-module(p2_test).
-include_lib("eunit/include/eunit.hrl").

sum_if_less_than_fifty_test_() ->
    [
        {"20 + 20 = 40", ?_assertEqual(40, p2:sum_if_less_than_fifty(20, 20))},
        {"20 + 30 = none", ?_assertEqual(none, p2:sum_if_less_than_fifty(20, 30))},
        {"20 + 100 = none", ?_assertEqual(none, p2:sum_if_less_than_fifty(20, 100))}
    ].
