import customtkinter as ctk
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

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x600")
        self.root.resizable(True, True)
        
        self.current_frame = None
        self.show_start_menu()
    
    def show_start_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ctk.CTkFrame(self.root)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        title_label = ctk.CTkLabel(
            self.current_frame,
            text="Tic Tac Toe",
            font=("Segoe UI", 48, "bold")
        )
        title_label.pack(pady=50)
        
        start_btn = ctk.CTkButton(
            self.current_frame,
            text="Start Game",
            command=self.start_game,
            font=("Segoe UI", 24),
            height=60
        )
        start_btn.pack(pady=20)
        
        quit_btn = ctk.CTkButton(
            self.current_frame,
            text="Quit",
            command=self.root.quit,
            font=("Segoe UI", 24),
            height=60
        )
        quit_btn.pack(pady=20)
    
    def start_game(self):
        if self.current_frame:
            self.current_frame.destroy()
        
        # Pass the end menu function as a callback
        self.current_frame = GameFrame(self.root, self.show_start_menu, self.show_end_menu)
        self.current_frame.pack(fill="both", expand=True)
    
    def show_end_menu(self, message):
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ctk.CTkFrame(self.root)
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        result_label = ctk.CTkLabel(
            self.current_frame,
            text=message,
            font=("Segoe UI", 32, "bold")
        )
        result_label.pack(pady=50)
        
        play_again_btn = ctk.CTkButton(
            self.current_frame,
            text="Play Again",
            command=self.start_game,
            font=("Segoe UI", 24),
            height=60
        )
        play_again_btn.pack(pady=20)
        
        menu_btn = ctk.CTkButton(
            self.current_frame,
            text="Main Menu",
            command=self.show_start_menu,
            font=("Segoe UI", 24),
            height=60
        )
        menu_btn.pack(pady=20)

class GameFrame(ctk.CTkFrame):
    def __init__(self, parent, back_to_menu_callback, end_game_callback):
        super().__init__(parent)
        self.back_to_menu_callback = back_to_menu_callback
        self.end_game_callback = end_game_callback # Store the callback
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.setup_ui()
    
    def setup_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        title_label = ctk.CTkLabel(
            self,
            text="Tic Tac Toe",
            font=("Segoe UI", 32, "bold")
        )
        title_label.grid(row=0, column=0, pady=20)
        
        self.info_label = ctk.CTkLabel(
            self,
            text=f"Player {self.current_player}'s turn",
            font=("Segoe UI", 16)
        )
        self.info_label.grid(row=1, column=0, pady=10)
        
        board_frame = ctk.CTkFrame(self)
        board_frame.grid(row=2, column=0, pady=20)
        
        for i in range(3):
            for j in range(3):
                btn = ctk.CTkButton(
                    board_frame,
                    text=" ",
                    width=100,
                    height=100,
                    font=("Segoe UI", 48, "bold"),
                    command=lambda r=i, c=j: self.on_click(r, c)
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn
        
        reset_btn = ctk.CTkButton(
            self,
            text="Reset Game",
            command=self.reset_game,
            font=("Segoe UI", 14)
        )
        reset_btn.grid(row=3, column=0, pady=20)
    
    def on_click(self, row, col):
        if self.board[row][col] != " ":
            messagebox.showwarning("Invalid", "Cell already taken!")
            return
        
        self.board[row][col] = self.current_player
        self.buttons[row][col].configure(text=self.current_player)
        
        winner = check_winner(self.board)
        if winner:
            self.end_game_callback(f"Player {winner} wins!")
            return
        
        if is_full(self.board):
            self.end_game_callback("It's a tie!")
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
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = TicTacToeApp(root)
    root.mainloop()