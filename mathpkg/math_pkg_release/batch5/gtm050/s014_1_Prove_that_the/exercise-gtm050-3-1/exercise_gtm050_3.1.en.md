---
role: exercise
locale: en
chapter: "3"
section: "3"
exercise_number: 1
---
Prove that the 7th powers mod 29 are $0, \pm 1, \pm 12$. [Since $2^7 = -12$ mod 29, all 5 of these numbers are 7th powers. The fact that these are the only 7th powers can be proved by computing $3^7, 4^7, \ldots, 28^7$ mod 29. More efficient than this is to notice that if $x \not\equiv 0$ mod 29 is a 7th power then $x^4 - 1 \equiv 0$ mod 29. Thus it will suffice to prove that if $f(x)$ is a polynomial of degree $n$ with leading coefficient 1 then the congruence $f(x) \equiv 0$ mod $p$ has at most $n$ distinct solutions mod $p$. This can be done using the Remainder Theorem as in Exercise 9 of Section 2.4. Alternatively one can multiply $f(x)$ by $(x - r_1)(x - r_2) \ldots (x - r_k)$ where $r_i$ ranges over distinct integers which are not solutions of $f(x) \equiv 0$. In this way one could construct a polynomial $g(x)$, with leading coefficient 1 and degree less than $p$, all of whose values are zero mod $p$. Euler's differencing argument of Section 2.4 shows that this is impossible.]
