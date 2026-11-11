# Week 7 — Object-Oriented Programming Fundamentals

**Author:** Chinedu Iroanyah
**Date:** 2026-11-11

## Overview
This project models a simple e-commerce purchasing system using Object-Oriented Programming (OOP). It demonstrates inheritance, encapsulation, and composition.

## The Classes
1. **`Product` (`product.py`):** The parent class representing a physical item. It includes validation in its constructor to prevent negative prices.
2. **`DigitalProduct` (`digital_product.py`):** The child class that inherits from `Product`. It reuses the parent's validation while adding a unique `download_link` attribute.
3. **`Account` (`account.py`):** Represents a user's wallet. It uses **composition** to hold a list of purchased products. It includes methods for buying products (with insufficient funds validation) and topping up the balance.

## Why use Classes instead of loose functions?
Classes bundle data (attributes) and behavior (methods) together. Instead of managing scattered dictionaries and variables, the `Account` object holds its own state and rules. This makes the code easier to maintain, scale, and debug. 

## Class Diagram
See `class_diagram.png` in this folder for the visual representation of the classes, their attributes, methods, and relationships.

## How to Run
```bash
python main.py
```
🎥 Demo
Recording: [link to be added]

Live URL: N/A (CLI tool, not deployed)