# The Ruby Workshop

- **Source:** B14197_RubyWorkshop_eBook-200128-104214.pdf
- **Drive link:** https://drive.google.com/file/d/1lQ9hD6SjsdG6-PdGMNQVt8hgZI7cMBSH/view?usp=drivesdk
- **Type:** book
- **Author/Year:** Akshat Paul, Peter Philips, Dániel Szabó, Cheyne Wallace / 2019
- **Coverage:** partial (large file, truncated extraction)

## Overview
A Packt workshop-style introduction to Ruby covering core language features, data types and collections, program flow, methods, object-oriented programming, file handling, and web development basics. The book leverages Ruby's Interactive Ruby Shell (IRB) for iterative learning and highlights Ruby's distinctive philosophy of expressiveness and convention over configuration.

## Unique contribution
Emphasizes Ruby's unique language characteristics — duck typing, metaprogramming, open classes, and the splat operator — that distinguish it from other OO languages. The book pairs every concept with practical exercises (dice roller, blackjack card game, mind reader) making abstract features immediately tangible.

## Key concepts
- Interactive Ruby Shell (IRB)
- Dynamic and duck typing
- Object-oriented programming in Ruby
- Metaprogramming
- Reflection
- Standard data types: Integer, Float, String, Boolean
- String interpolation and manipulation methods (gsub, split, join, substr)
- Arrays: iteration (each, each_with_index, map/collect), sort, uniq, push/pop
- Hashes: key-value operations, merge, delete, select/reject
- Ruby methods: positional, optional, keyword arguments, splat (*) and double-splat (**) operators
- Return values (multiple returns)
- Boolean operators (AND, OR, NOT), truthiness
- Conditional constructs (if/else/elsif, unless, case/when, ternary)
- Loop constructs (while, until, do-while, iterators)
- Variable scope (local, instance, class, global)
- Modules and mixins
- Exception handling
- File I/O
- Regular expressions
- Blocks, procs, and lambdas

## Methods / results / takeaways
- Duck typing means Ruby checks whether an object responds to a method at runtime rather than checking its class, enabling highly flexible interfaces.
- The `===` operator used in `case/when` dispatches differently depending on the receiver (Range, Regexp, Class), making `case` more powerful than a simple equality check.
- The splat operator (`*args`) enables variable-arity methods; double-splat (`**kwargs`) captures keyword arguments into a hash.
- Open classes allow extending built-in types (e.g., adding a method to Integer), which is powerful but can cause subtle bugs if not used carefully.
- Ruby's `map`/`collect` returns a new array from a block's return values; `each` is for side effects only — conflating the two is a common mistake.
