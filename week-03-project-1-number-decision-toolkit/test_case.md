# Test Cases — Number & Decision Toolkit

**Project:** Week 3 — Number & Decision Toolkit
**Author:** Chinedu Iroanyah
**Date:** 2026-10-14

These test cases cover the three tools (Calculator, Converter, Decision Checker), the main menu, and known edge cases.

**Legend:** ✅ Pass · ❌ Fail · ⚠️ Known limitation

---

## 1. Menu Navigation

| # | Input | Expected Output | Actual Output | Status |
|---|-------|-----------------|---------------|--------|
| M1 | `1` | Opens Calculator | Opens Calculator | ✅ |
| M2 | `2` | Opens Converter | Opens Converter | ✅ |
| M3 | `3` | Opens Decision Checker | Opens Decision Checker | ✅ |
| M4 | `4` | Exits the toolkit | Exits the toolkit | ✅ |
| M5 | `5` | "Invalid choice" message, menu redisplays | "Invalid choice" message, menu redisplays | ✅ |
| M6 | `abc` | "Invalid choice" message, menu redisplays | "Invalid choice" message, menu redisplays | ✅ |
| M7 | *(empty)* | "Invalid choice" message, menu redisplays | "Invalid choice" message, menu redisplays | ✅ |

---

## 2. Calculator

| # | Input Sequence | Expected Output | Actual Output | Status |
|---|----------------|-----------------|---------------|--------|
| C1 | `10`, `+`, `5`, `n` | `10 + 5 = 15`, returns to menu | `10 + 5 = 15`, returns to menu | ✅ |
| C2 | `10`, `-`, `3`, `n` | `10 - 3 = 7`, returns to menu | `10 - 3 = 7`, returns to menu | ✅ |
| C3 | `4`, `*`, `6`, `n` | `4 * 6 = 24`, returns to menu | `4 * 6 = 24`, returns to menu | ✅ |
| C4 | `20`, `/`, `4`, `n` | `20 / 4 = 5.0`, returns to menu | `20 / 4 = 5.0`, returns to menu | ✅ |
| C5 | `5`, `/`, `0`, `n` | "You cannot divide by 0", returns to operator prompt | "You cannot divide by 0", returns to operator prompt | ✅ |
| C6 | `5`, `x`, *(any)* | "Invalid choice" message, returns to operator prompt | "Invalid choice" message, returns to operator prompt | ✅ |
| C7 | `5`, `+`, `3`, `y`, `+`, `2`, `n` | `5 + 3 = 8`, then `8 + 2 = 10`, returns to menu | `5 + 3 = 8`, then `8 + 2 = 10`, returns to menu | ✅ |
| C8 | `2.5`, `*`, `4`, `n` | `2.5 * 4 = 10.0`, returns to menu | `2.5 * 4 = 10.0`, returns to menu | ✅ |
| C9 | `-3`, `+`, `5`, `n` | `-3 + 5 = 2`, returns to menu | `-3 + 5 = 2`, returns to menu | ✅ |

---

## 3. Converter (Temperature)

| # | Input Sequence | Expected Output | Actual Output | Status |
|---|----------------|-----------------|---------------|--------|
| V1 | `1`, `100`, `n` | `100.0℃ = 212.0℉`, returns to menu | `100.0℃ = 212.0℉`, returns to menu | ✅ |
| V2 | `1`, `0`, `n` | `0.0℃ = 32.0℉`, returns to menu | `0.0℃ = 32.0℉`, returns to menu | ✅ |
| V3 | `1`, `-40`, `n` | `-40.0℃ = -40.0℉`, returns to menu | `-40.0℃ = -40.0℉`, returns to menu | ✅ |
| V4 | `2`, `212`, `n` | `212.0℉ = 100.0℃`, returns to menu | `212.0℉ = 100.0℃`, returns to menu | ✅ |
| V5 | `2`, `32`, `n` | `32.0℉ = 0.0℃`, returns to menu | `32.0℉ = 0.0℃`, returns to menu | ✅ |
| V6 | `2`, `98.6`, `n` | `98.6℉ = 37.0℃`, returns to menu | `98.6℉ = 37.0℃`, returns to menu | ✅ |
| V7 | `1`, `100`, `y`, `2`, `212`, `n` | `100.0℃ = 212.0℉`, then `212.0℉ = 100.0℃`, returns to menu | `100.0℃ = 212.0℉`, then `212.0℉ = 100.0℃`, returns to menu | ✅ |
| V8 | `5`, `n` | "Invalid choice" message, asks `y/n` once, returns to menu | "Invalid choice" message, asks `y/n` once, returns to menu | ✅ |

---

## 4. Decision Checker (Grade Classifier)

| # | Input Sequence | Expected Output | Actual Output | Status |
|---|----------------|-----------------|---------------|--------|
| D1 | `95`, `n` | "Your grade is A", returns to menu | "Your grade is A", returns to menu | ✅ |
| D2 | `90`, `n` | "Your grade is A" (boundary) | "Your grade is A" (boundary) | ✅ |
| D3 | `89`, `n` | "Your grade is B" (boundary) | "Your grade is B" (boundary) | ✅ |
| D4 | `80`, `n` | "Your grade is B" (boundary) | "Your grade is B" (boundary) | ✅ |
| D5 | `75`, `n` | "Your grade is C", returns to menu | "Your grade is C", returns to menu | ✅ |
| D6 | `65`, `n` | "Your grade is D", returns to menu | "Your grade is D", returns to menu | ✅ |
| D7 | `55`, `n` | "Your grade is E", returns to menu | "Your grade is E", returns to menu | ✅ |
| D8 | `49`, `n` | "Your grade is F" (boundary) | "Your grade is F" (boundary) | ✅ |
| D9 | `0`, `n` | "Your grade is F" (boundary) | "Your grade is F" (boundary) | ✅ |
| D10 | `-5`, `n` | "Your grade is Invalid score", returns to menu | "Your grade is Invalid score", returns to menu | ✅ |
| D11 | `150`, `n` | "Your grade is Invalid score", returns to menu | "Your grade is Invalid score", returns to menu | ✅ |
| D12 | `100`, `n` | "Your grade is A" (upper boundary) | "Your grade is A" (upper boundary) | ✅ |
| D13 | `95`, `y`, `42`, `n` | "Your grade is A", then "Your grade is F", returns to menu | "Your grade is A", then "Your grade is F", returns to menu | ✅ |

---

## 5. Edge Cases and Known Limitations

| # | Input | Expected Behaviour | Actual Behaviour | Status |
|---|-------|--------------------|------------------|--------|
| E1 | Non-numeric input in Calculator (e.g., `abc` for first number) | Should prompt again | Crashes with `ValueError` | ⚠️ |
| E2 | Non-numeric input in Converter (e.g., `abc` for temperature) | Should prompt again | Crashes with `ValueError` | ⚠️ |
| E3 | Non-numeric input in Decision Checker (e.g., `abc` for score) | Should prompt again | Crashes with `ValueError` | ⚠️ |
| E4 | Non-numeric input in main menu (e.g., `abc`) | "Invalid choice" message, menu redisplays | "Invalid choice" message, menu redisplays | ✅ |
| E5 | Very large number (e.g., `999999999` in Calculator) | Handles without issue | Handles without issue | ✅ |
| E6 | Negative score in Decision Checker (`-1`) | "Invalid score" | "Invalid score" | ✅ |
| E7 | Score above 100 in Decision Checker (`101`) | "Invalid score" | "Invalid score" | ✅ |

---

## Known Limitations

1. **Non-numeric input crashes the program.**  
   Entering letters instead of numbers raises `ValueError` because `int()` and `float()` cannot convert text. Fixing this requires `try/except`, which is a Week 6 topic. Once learned, all three tools will be updated to prompt again instead of crashing.

2. **`continue_tool()` uses a module-level `global`.**  
   The function updates `run_tool` using `global`, which works but is not ideal. A cleaner design would return a boolean. Planned refactor for Week 5 (Functions & Clean Code).

---

## How These Tests Were Run

All tests were executed manually in the terminal on Windows 11 using Python 3.13.5 in a `.venv` virtual environment. Each test was performed on the final committed version of `number_decision_toolkit.py`.

---

## Summary

| Category | Total Tests | Passed | Known Limitations |
|----------|-------------|--------|-------------------|
| Menu Navigation | 7 | 7 | 0 |
| Calculator | 9 | 9 | 0 |
| Converter | 8 | 8 | 0 |
| Decision Checker | 13 | 13 | 0 |
| Edge Cases | 7 | 4 | 3 (non-numeric input) |
| **Total** | **44** | **41** | **3** |