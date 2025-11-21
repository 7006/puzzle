-module(pzl_test).
-include_lib("eunit/include/eunit.hrl").

add_test_() ->
    [
        {"1+1 = 2", ?_assertEqual(2, pzl:add(1, 1))}
    ].
