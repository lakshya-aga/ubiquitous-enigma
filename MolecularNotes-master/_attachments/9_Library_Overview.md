<tuple>

tuple, get<>(), tuple_size<>
<stdexcept>

length_error, out_of_range, runtime_error
<sstream>

istringstream, ostringstream
<unordered_map>

unordered_map, unordered_multimap
<thread>

thread
<vector>

vector
<variant>

variant
<utility>

move(), swap(), pair
<set>

set, multiset
<string_view>

string_view
<string>

string, basic_string
<regex>

regex, smatch
<ranges>

sized_range, subrange, take(), split(), iterator_t
<random>

default_random_engine, normal_distribution
<memory>

unique_ptr, shared_ptr, allocator
<map>

map, multimap
<iostream>

istream, ostream, cin, cout
<ios>

hex, dec, scientific, fixed, defaultfloat
<future>

future, promise
<functional>

function, greater_equal, hash, range_value_t
<fstream>

fstream, ifstream, ofstream
<format>

format()
<format>

format()
<filesystem>

path
<concepts>

floating_point, copyable, predicate, invocable
<complex>

complex, sqrt(), pow()
<cmath>

sqrt(), pow()
<chrono>

duration, time_point, month, time_zone
<array>

array
<algorithm>

copy(), find(), sort()
A traditional sequence version taking a pair of iterators; e.g., sort(begin(v),v.end())

A range version taking a single range; e.g., sort(v)
There is no coherent philosophy for what should be in a sub-namespace. However, suffixes cannot be explicitly qualified so we can only bring in a single set of suffixes into a scope without risking ambiguities. Therefore suffixes for a library meant to work with other libraries (that might define their own suffixes) are placed in sub-namespaces
polymorphic memory resources
It is generally in poor taste to dump every name from a namespace into the global namespace. However, in this book, I use the standard library exclusively and it is good to know what it offers.
The standard library is defined in a namespace (§3.3) called std. To use standard-library facilities, the std:: prefix can be used:
Ways of manipulating sequences of elements, such as views (§14.2), string_views (§10.3), and spans (§15.2.2).
Support for absolute time and durations, e.g., time_point and system_clock (§16.2.1).
Special-purpose containers, such as array (§15.3.1), bitset (§15.3.2), and tuple (§15.3.3).
Support for concurrent programming, including threads and locks (Chapter 18). The concurrency support is foundational so that users can add support for new models of concurrency as libraries.
Parallel versions of most STL algorithms and of some numerical algorithms, such as sort() (§13.6) and reduce() (§17.3.1).
Synchronous and asynchronous coroutines
Concepts for fundamental types and ranges (§14.5).
Ranges (§14.1), including views (§14.2), generators (§14.3), and pipes
A framework of containers (such as vector and map; Chapter 12) and algorithms (such as find(), sort(), and merge(); Chapter 13). This framework, conventionally called the STL [Stepanov,1994], is extensible so users can add their own containers and algorithms.
I/O streams is an extensible framework for input and output to which users can add their own types, streams, buffering strategies, locales, and character sets (Chapter 11). It also offers facilities for flexible output formatting (§11.6.2).

A library for manipulating file systems in a portable manner (§11.9)
Strings with support for international character sets, localization, and read-only views of substrings (§10.2).

Support for regular expression matching (§10.4).
The standard-library facilities described in this book are part of every complete C++ implementation. In addition to the standard-library components, most implementations offer “graphical user interface” systems (GUIs), Web interfaces, database interfaces, etc.
The specification of the standard library is over two thirds of the ISO C++ standard. Explore it, and prefer it to home-made alternatives
you are strongly encouraged not to be distracted or discouraged by an incomplete understanding of details.
