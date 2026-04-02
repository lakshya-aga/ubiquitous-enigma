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

The regular expression syntax and semantics are designed so that regular expressions can be compiled into  state machines for efficient execution


# Regex

The standard library provides support for regular expressions through `<regex>`.
### Main facilities

- `regex_match()`  
    Matches a regular expression against a whole string of known size.
- `regex_search()`  
    Searches for a match in a string or stream of data.
- `regex_replace()`  
    Finds strings that match a regular expression and replaces them.
- `regex_iterator`  
    Iterates over matches and submatches.
- `regex_token_iterator`  
    Iterates over selected parts of matches or non-matching parts.

### Note

- The `regex` type performs pattern compilation at run time.


## `std::string`

### What it is

- `string` is a regular type for owning and manipulating a sequence of characters.
- `std::string` is actually an alias of a more general template:
- `basic_string<char>`

### Character-set generalization

- To handle other character types, we can use `basic_string` directly.
- Example:
    
    using Jstring =` basic_string<Jchar>;
    
    This lets us perform usual string operations on strings of Japanese characters or other custom character types.
    

### String literals

- A string literal is, by definition, a `const char*`.

### Efficiency

- `string` has a move constructor, so returning even long strings by value is efficient.
- Performance may depend on the run-time environment.
- In multithreaded programs, memory allocation can be relatively costly.
- When many strings of different lengths are used, memory fragmentation can occur.
- These are major reasons why the short-string optimization is widely used.

### Modification example

- Strings are mutable:
    
    `name[0] = toupper(name[0]);
    

### Replacement

- When replacing part of a string, the replacement text does not need to be the same size as the original substring.

### String literal suffix

- `std::string` can be created from literals using the `"s"` suffix.

Example:
```
using namespace std::literals;  
  
auto s = "hello"s;
```
We can easily pass a substring.

## `std::string_view`

### What it is

- `string_view` allows us to manipulate sequences of characters without owning them.
- It can refer to characters stored in:
    - `std::string`
    - C-style strings
    - character arrays
    - substrings

### Key idea

- A `string_view` is like a pointer or reference: it does **not** own the characters it refers to.

### Benefits

- It can be used for character sequences managed in many different ways.
- We can easily pass a substring.
- We do not have to create a `std::string` just to pass a C-style string argument.

### Comparison

- In some ways, `string_view` resembles an STL pair of iterators.
- You might also consider using a `span` in related situations.

### Literal suffix

To use string-view literals:

using namespace std::literals::string_view_literals;

Example:

auto sv = "hello"sv;
