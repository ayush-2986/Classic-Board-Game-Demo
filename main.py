import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.info_label = tk.Label(root, text=f"Player {self.current_player}'s turn", font=("Arial", 14))
        self.info_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        for i in range(3):
            for j in range(3):
                btn = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                               command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i+1, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn
        
        self.reset_btn = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_btn.grid(row=4, column=0, columnspan=3, pady=10)
    
    def on_click(self, row, col):
        if self.board[row][col] != " ":
            messagebox.showwarning("Invalid", "Cell already taken!")
            return
        
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        
        winner = check_winner(self.board)
        if winner:
            messagebox.showinfo("Winner", f"Player {winner} wins!")
            self.reset_game()
            return
        
        if is_full(self.board):
            messagebox.showinfo("Tie", "It's a tie!")
            self.reset_game()
            return
        
        self.current_player = "O" if self.current_player == "X" else "X"
        self.info_label.config(text=f"Player {self.current_player}'s turn")
    
    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.info_label.config(text=f"Player {self.current_player}'s turn")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()