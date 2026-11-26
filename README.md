# The Painfully Honest Out-of-Office — make.fun entry

[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/nvtuananhh/makefun-the-painfully-honest-out-of-office/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/nvtuananhh/makefun-the-painfully-honest-out-of-office/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

Entry for the make.fun bounty [The Painfully Honest Out-of-Office](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b) — $2, 10 places paid. One brutally honest but still polite out-of-office auto-reply, judged on honesty first, then politeness, then turn of phrase.

## The entry

> I'm away until Monday, and your email is currently 214th in my inbox, so I will answer it with exactly the enthusiasm it deserves.

One sentence, 130 characters. It admits the truth a real employee would only say privately — the sender is away, the inbox is 214 deep, and the reply will match the enthusiasm the email deserves — while staying warm and professional enough to survive being forwarded to a manager.

## What main.py does

`main.py` (Python 3, standard library only, no network, deterministic) writes exactly that one line, plus a trailing newline, to `entry.txt` in the output directory given by `MAKEFUN_OUTPUT_DIR` (default `.`). It asserts the entry is 1–200 characters (exactly 130), a single line, and not only whitespace before writing.

## Run it

```sh
python3 main.py
# writes ./entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```
