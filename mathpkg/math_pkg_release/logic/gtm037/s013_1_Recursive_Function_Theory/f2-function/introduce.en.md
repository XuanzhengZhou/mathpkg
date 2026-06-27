---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The family of functions $f_2^m$ is defined recursively. The base case $f_2^1$ uses the concatenation function $\text{Cat}$ to combine the constant $2$ with $f_1 x$. For the inductive step, $f_2^{m+1}(x_0, \ldots, x_m)$ concatenates $f_2^m(x_0, \ldots, x_{m-1})$ with $f_2^1 x_m$. These functions encode sequences of numbers as Gödel numbers of specific word patterns.
