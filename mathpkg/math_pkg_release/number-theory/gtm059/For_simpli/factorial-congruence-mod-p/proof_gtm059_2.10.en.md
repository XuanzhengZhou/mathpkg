---
role: proof
locale: en
of_concept: factorial-congruence-mod-p
source_book: gtm059
source_chapter: "2"
source_section: "The Davenport-Hasse Distribution"
---

\textbf{Proof.} We proceed by induction on $k$. For $k = 1$, the statement holds trivially since $1! = 1$ and $s(1) = 1$, $v_p(1!) = 0$.

Assume the formula holds for all positive integers less than $k$. Write $k = q + p m$ where $0 \leq q < p$ and $m = \lfloor k/p \rfloor$. Then
$$k! = k \cdot (k-1)! = (q + p m) \prod_{j=1}^{k-1} j.$$

Grouping the factors in $(k-1)!$ according to their residue modulo $p$, we apply Wilson's theorem and the induction hypothesis. The factors congruent to $1, 2, \dots, p-1$ modulo $p$ give a contribution of $(p-1)! \equiv -1 \pmod{p}$. The multiples of $p$ give a factor of $p^m \cdot m!$, and by induction,
$$\frac{m!}{p^{v_p(m!)}} \equiv (-1)^{v_p(m!)} \prod_{i \geq 1} (q_i!) \pmod{p}.$$

The valuation satisfies $v_p(k!) = m + v_p(m!)$, since the multiples of $p$ each contribute at least one factor of $p$. Therefore,
$$\frac{k!}{p^{v_p(k!)}} = \frac{k!}{p^{m + v_p(m!)}} = \frac{q! \cdot p^m \cdot m! \cdot (\text{non-multiples of }p)}{p^{m + v_p(m!)}}.$$

The non-multiples of $p$ are congruent to $(p-1)! \equiv -1 \pmod{p}$ taken $m$ times, giving $(-1)^m$. Combining with the induction hypothesis yields the result:
$$\frac{k!}{p^{v_p(k!)}} \equiv q! \cdot (-1)^m \cdot (-1)^{v_p(m!)} \prod_{i \geq 1} (q_i!) \equiv (-1)^{v_p(k!)} \prod_{i \geq 0} (q_i!) \pmod{p}.$$

The special case $k \leq p-1$ follows immediately since then $v_p(k!) = 0$, $q_0 = k$, and the formula reduces to $k! \equiv (-1)^{k+1}/k \pmod{p}$, which is equivalent to the above via the relation $k! \cdot k \equiv (-1)^{k+1} \pmod{p}$. $\square$
