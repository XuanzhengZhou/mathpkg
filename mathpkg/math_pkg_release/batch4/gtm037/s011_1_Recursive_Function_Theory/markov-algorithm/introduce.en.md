---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A Markov algorithm (also called a normal algorithm) is a formal system for string rewriting introduced by A. A. Markov. It consists of a finite ordered list of production rules, each of the form $a \to b$ (with an associated termination flag $c \in \{0,1\}$). Given an input word, the algorithm applies the first applicable rule to the leftmost occurrence of its left-hand side, producing the right-hand side as output. The process repeats until a rule with termination flag $c = 1$ is applied (a terminating step) or no rule is applicable. Markov algorithms provide another equivalent characterization of computable functions, alongside Turing machines and recursive functions.
