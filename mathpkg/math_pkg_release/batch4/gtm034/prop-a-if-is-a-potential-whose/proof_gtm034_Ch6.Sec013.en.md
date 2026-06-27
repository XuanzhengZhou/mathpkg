---
role: proof
locale: en
of_concept: prop-a-if-is-a-potential-whose
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: Whenever $x \in R$ and $y \in A$

$$\sum_{t \in A} H_A(x,t)G(t,y) = G(x,y),$$

which was a useful identity in the proof of P24.8. Here too it is of fundamental importance. Applying $H_A(x,t)$ as an operator to the identity $f = G\psi$ one gets

(1) $$\sum_{t \in A} H_A(x,t)f(t) = f(x), \quad x \in R.$$

Hence

$$f(x) \leq \left[ \sup_{t \in A} f(t) \right] H_A(x) \leq \sup_{t \in A} f(t).$$

That was the proof of part (a), and part (b) also follows from (1) which gives

$$f_2(x) - f_1(x) = \sum_{t \in A} H_A(x,t)[

for otherwise there is nothing to prove. Since the set $A$ in P9 may not be transient we select a sequence of finite (and hence transient) sets $A_n$ which increase to $A$ as $n \to \infty$. Applying T1 to the reversed random walk we have for each of these sets

$$\sum_{t \in A_n} E^*_{A_n}(t) G(t,y) = H^*_{A_n}(y), \quad y \in R.$$

Therefore

$$0 \leq \sum_{t \in A_n} E^*_{A_n}(t) [f_2(t) - f_1(t)] = \sum_{y \in A_n} [\psi_2(y) - \psi_1(y)]$$

$$+ \sum_{y \in A - A_n} H^*_{A_n}(y) [\psi_2(y) - \psi_1(y)]$$

$$\leq \sum_{y \in A_n} [\psi_2(y) - \psi_1(y)] + \sum_{y \in A - A_n} \psi_2(y),$$

so that for each of the sets $A_n \subset A$

$$\sum_{y \in A_n} \psi_1(y) \leq \sum_{y \in A} \psi_2(y).$$

Letting $n \to \infty$ one obtains the desired conclusion of part (c) of P9.
