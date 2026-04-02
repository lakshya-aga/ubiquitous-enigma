For full portability, use the character class names rather than these abbreviations.

|Abbreviation |Meaning |POSIX Equivalent |
|---|---|---|
|`\d`|A decimal digit|`[[:digit:]]`|
|`\s`|A space (space, tab, etc.)|`[[:space:]]`|
|`\w`|A letter (`a-z`) or digit (`0-9`) or underscore (`_`)|`[_[:alnum:]]`|
|`\D`|Not `\d`|`[^[:digit:]]`|
|`\S`|Not `\s`|`[^[:space:]]`|
|`\W`|Not `\w`|`[^_[:alnum:]]`|



Character class names must be used inside a bracket expression. For example:

```cpp
[[:digit:]]
```

Not:
```cpp
[:digit:]
```

## Greedy and lazy matching

A suffix `?` after a repetition operator such as `?`, `*`, `+`, or `{}` makes the matcher lazy or non-greedy.

This means it looks for the shortest match rather than the longest.

By default, regex matching is greedy: it prefers the longest possible match. This is often called the **Max Munch** rule.

## Repetition and optional patterns

A pattern can be optional or repeated by adding a suffix. The default is exactly one occurrence.

Common repetition forms include:
The regular expression syntax and semantics are designed so that regular expressions can be compiled into ```
```

state machines for efficient execution
```


[Cox,2007]. The regex type performs this compilation at run time.
In <regex>, the standard library provides support for regular expressions:

regex_match(): Match a regular expression against a string (of known size) (§10.4.2).

regex_search(): Search for a string that matches a regular expression in an (arbitrarily long) stream of data (§10.4.1).

regex_replace(): Search for strings that match a regular expression in an (arbitrarily long) stream of data and replace them.

regex_iterator: Iterate over matches and submatches (§10.4.3).

regex_token_iterator: Iterate over non-matches.
might consider using a span
For manipulation like lower and upper case
using namespace std::literals::string_view_literals;
It can be used for character sequences managed in many different ways.

We can easily pass a substring.

We don’t have to create a string to pass a C-style string argument.
compose() that takes const string&
In that, it resembles an STL pair of iterators
A string_view is like a pointer or a reference in that it does not own the characters
using Jstring = basic_string<Jchar>;
Now we can do all the usual string operations on Jstring, a string of Japanese characters.
To handle multiple character sets, string is really an alias for a general template basic_string with the character type char:
The actual performance of strings can depend critically on the run-time environment. In particular, in multi-threaded implementations, memory allocation can be relatively costly. Also, when lots of strings of differing lengths are used, memory fragmentation can result. These are the main reasons that the short-string optimization has become ubiquitous.
std::string use an s suffix
A string literal is by definition a const char*
Note that the replacement string need not be the same size as the substring that it is replacing.
name[0] = toupper(name[0]);
Immutable?
The standard string has a move constructor, so returning even long strings by value is efficient
string is a regular type (§8.2, §14.5) for owning and manipulating a sequence of characters of various character types
A string_view type allows us to manipulate sequences of characters however they may be stored (e.g., in a std::string or a char[]).
