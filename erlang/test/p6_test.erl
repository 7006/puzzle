-module(p6_test).
-include_lib("eunit/include/eunit.hrl").

filter_even_length_strings_test_() ->
    [
        ?_assertEqual(
            ["fish", "elephant"],
            p6:filter_even_length_strings([
                "cat", "dog", "fish", "elephant"
            ])
        ),
        ?_assertEqual(
            [],
            p6:filter_even_length_strings([
                "q", "w", "e", "r", "t", "y"
            ])
        ),
        ?_assertEqual(
            ["qq", "ww", "ee", "rr", "yy"],
            p6:filter_even_length_strings([
                "qq", "ww", "ee", "rr", "t", "yy"
            ])
        )
    ].

filter_even_length_binary_strings_test_() ->
    [
        ?_assertEqual(
            [<<"fish">>, <<"elephant">>],
            p6:filter_even_length_strings([
                <<"cat">>, <<"dog">>, <<"fish">>, <<"elephant">>
            ])
        ),
        ?_assertEqual(
            [],
            p6:filter_even_length_strings([
                <<"q">>, <<"w">>, <<"e">>, <<"r">>, <<"t">>, <<"y">>
            ])
        ),
        ?_assertEqual(
            [<<"qq">>, <<"ww">>, <<"ee">>, <<"rr">>, <<"yy">>],
            p6:filter_even_length_strings([
                <<"qq">>, <<"ww">>, <<"ee">>, <<"rr">>, <<"t">>, <<"yy">>
            ])
        )
    ].
