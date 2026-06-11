Author: [[Bjarne Stroustoup]]
Type: #source #book
Link: https://www.amazon.sg/Tour-C-Bjarne-Stroustrup-dp-0136816487/dp/0136816487/ref=dp_ob_image_bk
Topics: C++, Programming

---
Last read: March 2026

### For a programmer, I think this is the most high ROI read to learn C++.

The book covers basic concepts of C++ well. It is a very good shallow deep dive into actual C++ once you are familiar with the basic syntax. It contains quite a few code samples that show example usage (sometimes even innovative). 
First 10 chapters deal with language nuances such as templates, generic programming, overloading operators, `const`, move semantics (`lvalue` and `rvalue`), `constexpr` and so on. It also talks briefly about designing functions and classes effectively from the lens of generic programming.

The second half of the book deals with STL. It has general suggestions such as use STL instead of custom whenever possible and under the hood optimisations such as short string optimisation.

One thing I feel could complement the study of this book greatly is an end of chapter quiz for each chapter and/or a final exam. AI is a pretty good idea for this. I tried Gemini live to have a conversation with me on C++. It forces me to be more explicit about my understanding and easily identify gaps. eg. pointers vs reference and when to use one over the other.

There is a lot of condensed information such as different predicates and so on. Some very niche features which a developer will certainly always lookup. But to be fair the book is supposed to be a quick over view covering as much breadth as possible.

Some of my highlights:
- [[CPP Templates]]: Generic programming which is very useful for extendable and reusable code
- [[CPP Error Handling]]: Best C++ practices for bigger codebases
- [[CPP Strings and Regular Expressions]]: Short string optimisation was particularly insightful
- [[Move Semantics CPP]]: Must know for C++. If someone doesn't know this topic well, they may know programming, but not C++