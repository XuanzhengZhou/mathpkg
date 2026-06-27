---
role: proof
locale: en
of_concept: borel-covering-theorem
source_book: gtm002
source_chapter: "1"
source_section: "1"
---
The text presents a proof using a scaling argument. We reconstruct the standard proof:

Assume first that $I = [a, b]$ is closed and that all the covering intervals $I_n$ are open. (The general case follows by enlarging each $I_n$ slightly.) By the Heine-Borel theorem, a finite subcollection $I_1, \dots, I_N$ already covers $[a, b]$.

Order the intervals so that the left endpoint of $I_1$ is less than $a$, and then choose $I_2$ whose left endpoint is less than the right endpoint of $I_1$, and so on. If $b_1, b_2, \dots, b_N$ are the right endpoints, then $\sum |I_n| \geq (b_1 - a) + (b_2 - b_1) + \cdots + (b_N - b_{N-1}) = b_N - a \geq b - a = |I|$.

For an infinite sequence of intervals covering $I$, the sum of the lengths of the finite subcover is already at least $|I|$, so the infinite sum is at least $|I|$ as well.

\textbf{Corollary:} No non-degenerate interval is a nullset. Indeed, if $I$ were a nullset, we could cover it with intervals of total length less than $|I|$, contradicting the theorem.
