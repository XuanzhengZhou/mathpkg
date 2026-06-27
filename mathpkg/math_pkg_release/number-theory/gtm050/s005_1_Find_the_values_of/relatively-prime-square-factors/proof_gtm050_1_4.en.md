---
role: proof
locale: en
of_concept: relatively-prime-square-factors
source_book: gtm050
source_chapter: "1"
source_section: "1.4"
---

Suppose $v$ and $w$ are relatively prime and $vw$ is a square, but one of them (say $v$) is not a square. Write $vw = u^2$. Let $P$ be any prime factor of $v$. Since $v$ and $w$ are relatively prime, $P$ does not divide $w$. Since $vw = u^2$ is a square, the exponent of $P$ in $vw$ is even. But the exponent of $P$ in $w$ is zero, so the exponent of $P$ in $v$ must be even. Since this holds for every prime $P$ dividing $v$, one would conclude that $v$ is a square, contradicting the assumption.

Alternatively, the proof via infinite descent: assume $v$ and $w$ are relatively prime, $vw$ is a square, but $v$ is not a square. Write $v = Pk$ where $P$ is a prime dividing $v$ to an odd exponent. Then $P$ divides $vw = u^2$, so $P$ divides $u$. Write $u = Pm$. Then $v w = P^2 m^2$, so $Pk w = P^2 m^2$, giving $k w = P m^2$. Since $P$ divides the right side, $P$ divides $k w$. But $P$ does not divide $w$ (since $v$ and $w$ are coprime), so $P$ divides $k$. Write $k = P v'$. Then $v = Pk = P^2 v'$.

Now $P^2 v' w = P^2 m^2$ gives $v' w = m^2$. Since $v = P^2 v'$, any divisor of $v'$ is a divisor of $v$, so $v'$ and $w$ are still relatively prime. Moreover, if $v'$ were a square then $v = P^2 v'$ would be a square, which it is not. Thus $v'$ is not a square. The numbers $v', w$ have the same three properties as $v, w$ but $v' < v$.

Repeating the argument indefinitely gives an infinite strictly decreasing sequence $v > v' > v'' > \cdots$ of positive integers, which is impossible. Therefore the assumption that $v$ is not a square is false, and both $v$ and $w$ must be squares.
