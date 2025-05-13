# Thoughtful-s-Automation-Challenge

# 📦 Package Sorter - Robotic Dispatch System

This project simulates a robotic arm's logic in a factory that sorts packages into the correct stacks based on their volume and mass. It's designed for integration into an automated warehouse or logistics system.

---

## 🚀 Objective

Sort incoming packages into one of the following categories:

- **STANDARD**: Not bulky or heavy
- **SPECIAL**: Either bulky or heavy
- **REJECTED**: Both bulky and heavy

---

## 📐 Rules

A package is considered:
- **Bulky** if:
  - Volume ≥ 1,000,000 cm³, or
  - Any dimension (width, height, or length) ≥ 150 cm

- **Heavy** if:
  - Mass ≥ 20 kg

---
