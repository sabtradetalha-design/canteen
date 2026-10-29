# Campus Canteen Billing System

A beginner-friendly command-line billing program written in basic Python.

## Features

- Displays a menu with four canteen items and prices in PKR.
- Allows customers to place multiple orders.
- Uses `0` to check out.
- Calculates subtotal and total quantity of items.
- Applies a 10% discount when the subtotal is PKR 1,000 or more.
- Displays the final bill.

## Menu

| Choice | Item | Price |
|---|---|---:|
| 1 | Burger | PKR 350 |
| 2 | Sandwich | PKR 250 |
| 3 | Fries | PKR 150 |
| 4 | Tea | PKR 100 |
| 0 | Checkout | — |

## Requirements

- Python 3
- No external packages required

## How to Run

1. Install Python 3 if it is not already installed.
2. Open a terminal or command prompt in this project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

4. Select menu items and enter quantities.
5. Enter `0` when you are ready to check out.

## Discount Rule

A 10% discount is applied when the subtotal is **PKR 1,000 or more**.

## Example

If you order 2 burgers (PKR 700) and 2 sandwiches (PKR 500), the subtotal is PKR 1,200. The 10% discount is PKR 120, so the final bill is PKR 1,080.

## Concepts Used

Variables, `print()`, `input()`, arithmetic operators, `if` / `elif` / `else`, `while`, `break`, and `continue`.
