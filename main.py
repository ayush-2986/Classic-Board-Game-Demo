import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

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
        self.root.geometry("500x600")
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        title_label = ctk.CTkLabel(
            main_frame,
            text="Tic Tac Toe",
            font=("Segoe UI", 32, "bold")
        )
        title_label.pack(pady=20)
        
        self.info_label = ctk.CTkLabel(
            main_frame,
            text=f"Player {self.current_player}'s turn",
            font=("Segoe UI", 16)
        )
        self.info_label.pack(pady=10)
        
        board_frame = ctk.CTkFrame(main_frame)
        board_frame.pack(pady=20)
        
        for i in range(3):
            for j in range(3):
                btn = ctk.CTkButton(
                    board_frame,
                    text=" ",
                    font=("Segoe UI", 48, "bold"),
                    width=80,
                    height=80,
                    command=lambda r=i, c=j: self.on_click(r, c)
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn
        
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(fill="x", pady=20)
        
        reset_btn = ctk.CTkButton(
            button_frame,
            text="Reset Game",
            command=self.reset_game,
            font=("Segoe UI", 14),
            height=40
        )
        reset_btn.pack(fill="x")
    
    def on_click(self, row, col):
        if self.board[row][col] != " ":
            messagebox.showwarning("Invalid", "Cell already taken!")
            return
        
        self.board[row][col] = self.current_player
        self.buttons[row][col].configure(text=self.current_player)
        
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
        self.info_label.configure(text=f"Player {self.current_player}'s turn")
    
    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.info_label.configure(text=f"Player {self.current_player}'s turn")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text=" ")

if __name__ == "__main__":
    root = ctk.CTk()
    game = TicTacToe(root)
    root.mainloop()
