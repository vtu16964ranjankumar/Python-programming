
# In this project, you will develop a Simple Loan Calculator GUI. Write your codes below the comments corresponding to the comment texts.

# The Loan Calculator GUI is a window-based application that can accept several inputs to calculate and display the monthly and total payments at the end of the loan period. The following Instructions are the procedure required for this project.

# 1. Define a class called LoanCalculatorApp that will display the window to calculate the loan (5 pts).
# def LoanCalculatorApp: 
#     pass

# 2. Perform the following in the class constructor (30pts).
# def __init__(self):
#     # Initialize the Tkinter instance (2.5 pts).

#     # Provide the window object title and size (2.5 pts).

#     # Create five Label objects to hold the texts (5 pts)
#         Annual Interest Rate
#         Number of Months
#         Loan Amount
#         Monthly Payment
#         Total Payment

#     # Create five variables to h values for the labels (5 pts).

#     # Create the different Entities where the users of your application can enter values and where calculation resu lts will be displayed (10 pts).
    
#     # Loop the window to display it (5 pts).

# 3. Define a function called get_monthly_payment() that will calculate and return the monthly payment. (5 pts)
# def get_monthly_payment(self):

# 4. Define a function called compute_payment() that computes the total payment and displays the monthly and total payments in the corresponding labels. This function is a command in the Compute Payment button (10 pts).
# def compute_payment(self):



import tkinter as tk
from tkinter import ttk

class LoanCalculatorApp:
    def __init__(self):
        # Initialize the Tkinter instance
        self.root = tk.Tk()
        self.root.title("Loan Calculator App")
        self.root.geometry("600x300")

        # Create five Label objects to hold the texts
        ttk.Label(self.root, text="Annual Interest Rate").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.root, text="Number of Months").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.root, text="Loan Amount").grid(row=2, column=0, padx=10, pady=10)
        ttk.Label(self.root, text="Monthly Payment").grid(row=3, column=0, padx=10, pady=10)
        ttk.Label(self.root, text="Total Payment").grid(row=4, column=0, padx=10, pady=10)

        # Create five variables to hold values for the labels
        self.annual_interest_var = tk.StringVar()
        self.num_months_var = tk.StringVar()
        self.loan_amount_var = tk.StringVar()
        self.monthly_payment_var = tk.StringVar()
        self.total_payment_var = tk.StringVar()

        # Create the different Entry widgets for user input and result display
        ttk.Entry(self.root, textvariable=self.annual_interest_var).grid(row=0, column=1, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.num_months_var).grid(row=1, column=1, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.loan_amount_var).grid(row=2, column=1, padx=10, pady=10)

        # ttk.Label(self.root, textvariable=self.monthly_payment_var).grid(row=3, column=1, padx=10, pady=10)
        # ttk.Label(self.root, textvariable=self.total_payment_var).grid(row=4, column=1, padx=10, pady=10)

        # Create the Compute Payment button with right alignment
        compute_button = ttk.Button(self.root, text="Compute Payment", command=self.compute_payment)
        compute_button.grid(row=5, column=0, columnspan=2, pady=10, sticky=tk.E)  # Align to the right

        # Set justify to right for input labels
        entry_labels = [self.annual_interest_var, self.num_months_var, self.loan_amount_var]
        for label in entry_labels:
            label_entry = ttk.Entry(self.root, textvariable=label, justify="right")
            label_entry.grid(row=entry_labels.index(label), column=1, padx=10, pady=10, sticky=tk.E)  # Align to the right

        # Create output labels with right alignment
        ttk.Label(self.root, textvariable=self.monthly_payment_var, justify="right").grid(row=3, column=1, padx=10, pady=10, sticky=tk.E)  # Align to the right
        ttk.Label(self.root, textvariable=self.total_payment_var, justify="right").grid(row=4, column=1, padx=10, pady=10, sticky=tk.E)  # Align to the right

        # Loop the window to display it
        self.root.mainloop()

    def get_monthly_payment(self):
        # Function to calculate and return the monthly payment
        annual_interest = float(self.annual_interest_var.get())
        num_months = int(self.num_months_var.get())
        loan_amount = float(self.loan_amount_var.get())

        monthly_interest_rate = annual_interest / 12 / 100

        # Correct formula for monthly payment
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_months)

        return monthly_payment

    def compute_payment(self):
        # Function to compute the total payment and display the results
        try:
            annual_interest = float(self.annual_interest_var.get())
            num_months = int(self.num_months_var.get())
            loan_amount = float(self.loan_amount_var.get())

            # Call the get_monthly_payment function to calculate monthly payment
            monthly_payment = self.get_monthly_payment()

            # Calculate total payment
            total_payment = monthly_payment * num_months

            # Display results in the corresponding labels
            self.monthly_payment_var.set(f"{monthly_payment:.2f}")
            self.total_payment_var.set(f"{total_payment:.2f}")

        except ValueError:
            # Handle invalid input values (non-numeric)
            tk.messagebox.showerror("Error", "Please enter valid numeric values.")

# Create an instance of the LoanCalculatorApp class
app = LoanCalculatorApp()