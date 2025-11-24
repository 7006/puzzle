-module(p6).
-export([filter_even_length_strings/1]).

filter_even_length_strings(InputStrs) ->
    [I || I <- InputStrs, len(I) rem 2 =:= 0].

len(Str) when is_list(Str) ->
    erlang:length(Str);
len(Bin) when is_binary(Bin) ->
    erlang:byte_size(Bin).
