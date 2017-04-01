# DI-WHY

**Flag:** `CSCOSU{correct_horse_battery_staple}`

When connecting, the remote password manager prompts for an authentication password. It XOR's this password against a
hard-coded key and checks the result against a hard-coded secret.

Given the source code (and knowledge of XOR), it should be easy to recover the necessary password `honeycomb`.
