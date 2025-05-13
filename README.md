# Inventus-Inventory-Stock-Cycle-Count
🍫 Inventus - Inventory/Stock Cycle Count
Inventus is a simple and interactive terminal-based inventory management system built in Python for tracking chocolates in a warehouse setting. It helps manage stock levels, detect discrepancies, and maintain delivery records.
 
---

## 🚀 Features

* 📦 **View Inventory** – See current stock of all chocolates.
* 📉 **Stock Counter** – Compare actual (physical) stock with system stock and update discrepancies.
* ➕ **Insert New Delivery** – Add new chocolate items to the inventory.
* ➖ **Pull Out Item** – Remove items from inventory.
* 🔍 **Item Details** – View information for a specific chocolate item.
* 📊 **Total Items Delivered** – Track chocolates delivered into inventory.
* 🛠️ **Modify Item Details** – Edit name or stock of existing items.
* ❌ **Exit** – Gracefully exit the program.

---

## 🧰 How It Works
 
* The program starts with a pre-defined list of chocolate inventory.
* Users can check for discrepancies between physical stock and system stock.
* Discrepancies (overstock or shortage) can be reviewed and optionally corrected.
* New chocolate items can be added to the inventory.
* Items can be removed or modified (name or stock count).
* Users can view details of specific items or print the entire inventory.
* All delivered items are tracked separately for reference.
 
### Sample Inventory Structure:

```python
inventory = {
    "Item001": {"name": "Meigi", "stock": 50},
    "Item002": {"name": "Ferrero", "stock": 30},
    ...
}
```

---

## 🖥️ Usage

### Requirements

* Python 3.x

### Running the program

1. Run the Python script:
 
   python3 inventory.py
 
---

## 📸 Sample Menu

```
|- Welcome to Inventus -|
--------------------------
1. Stock Counter
2. Insert new Delivery
3. Pull out
4. Item Details
5. Total Items Delivered
6. Warehouse Inventory
7. Modify Item Details
8. Exit
--------------------------
```

---

## 📂 File Structure

```
inventus-inventory/
├── inventus.py    # Main script with inventory logic
├── README.md       # Project documentation
```

---

## ✍️ Author

* **Capili, Bayani, Caindoy** – [@yourgithub](https://github.com/Solo-2414)

---
 

