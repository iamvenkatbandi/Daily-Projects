# ⚡ Electricity Bill Calculator

A simple Python-based Electricity Bill Calculator that calculates the total electricity bill based on the **APERC Domestic LT (Telescopic)** tariff system.

This beginner-friendly project demonstrates how to use Python functions, conditional statements, user input, and error handling to solve a real-world problem.

---

## 📌 Features

- Calculate electricity bill based on units consumed
- Slab-wise energy charge calculation
- Fixed charge calculation
- Input validation using `try` and `except`
- Clean and easy-to-read output
- Beginner-friendly code with functions

---

## 🛠 Technologies Used

- Python 3

---

## 📚 Python Concepts Used

- Variables
- User Input (`input()`)
- Functions
- Conditional Statements (`if`, `elif`, `else`)
- Arithmetic Operators
- Return Statements
- Exception Handling (`try` and `except`)
- Formatted Strings (f-strings)

---

## 📖 Tariff Used

This project uses the **APERC Domestic LT (Telescopic)** electricity tariff.

### Energy Charges

| Units | Rate (₹/Unit) |
|--------|--------------:|
| 0 – 30 | 1.90 |
| 31 – 75 | 3.00 |
| 76 – 125 | 4.50 |
| 126 – 225 | 6.00 |
| 226 – 400 | 8.75 |
| Above 400 | 9.75 |

### Fixed Charge

- ₹10 per month (for this beginner implementation)

---

## 📂 Project Structure

```
Electricity-Bill-Calculator/
│
├── Electricity Bill Calculator.py
├── README.md
└── LICENSE
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Electricity-Bill-Calculator.git
```

### 2. Navigate to the project folder

```bash
cd Electricity-Bill-Calculator
```

### 3. Run the program

```bash
python electricity_bill.py
```

---

## 💻 Example

### Input

```
Enter Units Consumed: 150
```

### Output

```
========================================
      ELECTRICITY BILL CALCULATOR
========================================

----------- BILL DETAILS -----------
Units Consumed : 150.0
Energy Charge  : ₹567.00
Fixed Charge   : ₹10.00
------------------------------------
Total Bill     : ₹577.00
------------------------------------
```

---

## ⚙️ How It Works

1. User enters the number of electricity units consumed.
2. The program determines the applicable tariff slabs.
3. It calculates the energy charge.
4. It adds the fixed charge.
5. Finally, it displays the total electricity bill.

---

## 🚀 Future Improvements

- Show slab-wise bill breakdown
- Support multiple consumer categories
- Calculate electricity taxes
- Generate printable bill (PDF)
- Store bill history
- Graph monthly electricity usage
- GUI version using Tkinter
- Web version using Flask or Django

---

## 🎯 Learning Outcomes

By building this project, you will learn:

- Real-world problem solving with Python
- Writing reusable functions
- Using conditional logic effectively
- Handling invalid user input
- Organizing Python programs
- Creating beginner-friendly command-line applications

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

Happy Coding! 🚀
