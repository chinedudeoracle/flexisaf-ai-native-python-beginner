# Test Cases — Week 4 (Collections)

**Author:** Chinedu Iroanyah
**Date:** 2026-10-21

Below are the manual tests performed to verify the Contact Book and Student Scores scripts.

---

## 1. Contact Book (`contact_book.py`)

### Add Contact
| # | Input Sequence | Expected Output | Actual Output | Status |
|---|----------------|-----------------|---------------|--------|
| C1 | `1` → `Alice` → `2` → `0801` → `0802` | "Alice has been added..." | Match | ✅ |
| C2 | `1` → `Bob` → `1` → `0909` | "Bob has been added..." | Match | ✅ |

### View Contacts
| # | Input Sequence | Expected Output | Actual Output | Status |
|---|----------------|-----------------|---------------|--------|
| C3 | `2` (with contacts added) | Sorted list of names with comma-separated numbers | Match | ✅ |
| C4 | `2` (empty book) | "Your contact book is empty" | Match | ✅ |

### Delete Contact
| # | Input Sequence | Expected Output | Actual Output | Status |
|---|----------------|-----------------|---------------|--------|
| C5 | `3` → `Alice` | "Alice has been deleted." | Match | ✅ |
| C6 | `3` → `Charlie` (not in book) | "Charlie is not in your contact book" | Match | ✅ |

### Menu & Edge Cases
| # | Input Sequence | Expected Output | Actual Output | Status |
|---|----------------|-----------------|---------------|--------|
| C7 | `5` (invalid menu) | "Invalid Input. Choose between 1 to 4" | Match | ✅ |
| C8 | `4` (exit) | Program terminates | Match | ✅ |

---

## 2. Student Scores (`student_scores.py`)

### Normal Calculation
| # | Input Sequence | Expected Output | Actual Output | Status |
|---|----------------|-----------------|---------------|--------|
| S1 | `John` → `STU01` → `3` → `85` → `92` → `78` | Average: 85.00, Highest: 92, Passing: [85, 92, 78] | Match | ✅ |
| S2 | `Mary` → `STU02` → `2` → `40` → `30` | Average: 35.00, Highest: 40, Passing: [] | Match | ✅ |

### Edge Cases
| # | Input Sequence | Expected Output | Actual Output | Status |
|---|----------------|-----------------|---------------|--------|
| S3 | `Test` → `T01` → `0` (zero scores) | "No scores were entered." | Match | ✅ |
| S4 | `Fail` → `F01` → `3` → `10` → `20` → `30` | Passing Scores: [] (empty list) | Match | ✅ |
| S5 | `Perfect` → `P01` → `1` → `100` | Average: 100.00, Passing: [100] | Match | ✅ |

---

## Summary
All primary features (Add, View, Delete, Calculate Scores, Filter Passing) were tested and passed. Edge cases such as an empty contact book, a missing contact, and zero input scores were handled gracefully without crashing.