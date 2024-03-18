import tkinter 

# Function to handle button click events

def button_click(btn_text):
    if btn_text == 'AC':
        inputField.delete(0, tkinter.END)       # Clear the input field
    elif btn_text == '=':
        try:
            result = eval(inputField.get())     # Evaluate the expression and calculate the result
            inputField.delete(0, tkinter.END)    # Clear the input field
            inputField.insert(0, str(result))    # Display the result in the input field
        except Exception as e:
            inputField.delete(0, tkinter.END)     # Clear the input field if an error occurs
            inputField.insert(0, 'Error')         # Display 'Error' in the input field
    else:
        
        # Append the correct symbol for multiplication if the button text is 'x'

        btn_text = '*' if btn_text == 'x' else btn_text
        inputField.insert(tkinter.END, btn_text)       # Append the button text to the input field

# Create the main window
        
window = tkinter.Tk()
window.geometry("500x400")

# Create the input field

inputField = tkinter.Entry(window, width=40, borderwidth=1)
inputField.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button texts and create buttons

button_texts = ["AC", "+|-", "%", "/", "7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "0", ",", "=", ""]
buttons = [tkinter.Button(window, text=button_text, padx=40, pady=20, width=1, height=1, borderwidth=2, command=lambda bt=button_text: button_click(bt)) for button_text in button_texts]

# Arrange buttons on the grid

i = 0
for row in range(5):
    for column in range(4): 
        buttons[i].grid(row=row + 3, column=column)
        i += 1

# Start the main event loop
        
window.mainloop()
