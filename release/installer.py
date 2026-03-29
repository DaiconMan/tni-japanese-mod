"""
Tower Networking Inc. 日本語化Mod インストーラー (GUI)
Single-file installer with embedded ja.po data.
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sys
import winreg
import shutil


def resource_path(filename):
    """PyInstaller bundled resource path."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


def find_steam_path():
    """Find Steam installation path from registry."""
    for key_path in [
        r"SOFTWARE\WOW6432Node\Valve\Steam",
        r"SOFTWARE\Valve\Steam",
    ]:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                val, _ = winreg.QueryValueEx(key, "InstallPath")
                return val
        except (OSError, FileNotFoundError):
            continue
    return None


def find_game_dir():
    """Auto-detect game installation directory."""
    steam_path = find_steam_path()

    # Collect candidate library folders
    library_paths = []
    if steam_path:
        library_paths.append(steam_path)
        # Parse libraryfolders.vdf for additional libraries
        vdf = os.path.join(steam_path, "steamapps", "libraryfolders.vdf")
        if os.path.exists(vdf):
            try:
                with open(vdf, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if '"path"' in line:
                            parts = line.split('"')
                            if len(parts) >= 4:
                                library_paths.append(parts[3].replace("\\\\", "\\"))
            except Exception:
                pass

    # Also check common locations
    for drive in "CDEFGH":
        for sub in [
            f"{drive}:\\Program Files (x86)\\Steam",
            f"{drive}:\\Program Files\\Steam",
            f"{drive}:\\Steam",
            f"{drive}:\\SteamLibrary",
        ]:
            if sub not in library_paths:
                library_paths.append(sub)

    # Look for the game in each library
    game_name = "Tower Networking Inc"
    for lib in library_paths:
        candidate = os.path.join(lib, "steamapps", "common", game_name)
        if os.path.isdir(os.path.join(candidate, "localizations")):
            return candidate

    return ""


class InstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tower Networking Inc. 日本語化Mod")
        self.root.resizable(False, False)

        # Center window
        w, h = 520, 370
        x = (root.winfo_screenwidth() - w) // 2
        y = (root.winfo_screenheight() - h) // 2
        root.geometry(f"{w}x{h}+{x}+{y}")

        # Try to set icon (optional)
        try:
            root.iconbitmap(default="")
        except Exception:
            pass

        self.create_widgets()
        self.detect_game()

    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#2b2b2b", height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        tk.Label(
            title_frame,
            text="Tower Networking Inc.\n日本語化Mod インストーラー",
            font=("Meiryo UI", 13, "bold"),
            fg="white",
            bg="#2b2b2b",
        ).pack(expand=True)

        # Main area
        main = tk.Frame(self.root, padx=16, pady=12)
        main.pack(fill=tk.BOTH, expand=True)

        # Game path section
        tk.Label(main, text="ゲームフォルダ:", font=("Meiryo UI", 9)).pack(anchor=tk.W)
        path_frame = tk.Frame(main)
        path_frame.pack(fill=tk.X, pady=(2, 8))
        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(
            path_frame, textvariable=self.path_var, font=("Meiryo UI", 9)
        )
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(
            path_frame,
            text="参照...",
            command=self.browse,
            font=("Meiryo UI", 9),
        ).pack(side=tk.RIGHT, padx=(6, 0))

        # Status
        self.status_var = tk.StringVar(value="")
        self.status_label = tk.Label(
            main,
            textvariable=self.status_var,
            font=("Meiryo UI", 9),
            fg="#666666",
            wraplength=480,
            justify=tk.LEFT,
        )
        self.status_label.pack(anchor=tk.W, pady=(0, 8))

        # Buttons
        btn_frame = tk.Frame(main)
        btn_frame.pack(pady=(8, 4))

        self.install_btn = tk.Button(
            btn_frame,
            text="インストール",
            command=self.install,
            font=("Meiryo UI", 11, "bold"),
            width=16,
            height=2,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            cursor="hand2",
        )
        self.install_btn.pack(side=tk.LEFT, padx=8)

        self.uninstall_btn = tk.Button(
            btn_frame,
            text="アンインストール",
            command=self.uninstall,
            font=("Meiryo UI", 11),
            width=16,
            height=2,
            cursor="hand2",
        )
        self.uninstall_btn.pack(side=tk.LEFT, padx=8)

        # Log area
        tk.Label(main, text="ログ:", font=("Meiryo UI", 9)).pack(
            anchor=tk.W, pady=(8, 2)
        )
        self.log_text = tk.Text(
            main, height=6, font=("Consolas", 9), state=tk.DISABLED, bg="#f5f5f5"
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def log(self, msg):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update_idletasks()

    def set_status(self, msg, color="#666666"):
        self.status_var.set(msg)
        self.status_label.config(fg=color)

    def detect_game(self):
        self.log("ゲームフォルダを検索中...")
        game_dir = find_game_dir()
        if game_dir:
            self.path_var.set(game_dir)
            self.log(f"検出: {game_dir}")
            self.set_status("ゲームフォルダを自動検出しました。", "#228B22")
        else:
            self.log("自動検出できませんでした。手動で選択してください。")
            self.set_status(
                "ゲームフォルダが見つかりませんでした。「参照」から選択してください。",
                "#CC0000",
            )

    def browse(self):
        d = filedialog.askdirectory(title="Tower Networking Inc. のフォルダを選択")
        if d:
            self.path_var.set(d)

    def validate_path(self):
        game_dir = self.path_var.get().strip()
        if not game_dir:
            messagebox.showwarning("警告", "ゲームフォルダを指定してください。")
            return None
        loc_dir = os.path.join(game_dir, "localizations")
        if not os.path.isdir(loc_dir):
            messagebox.showerror(
                "エラー",
                f"localizations フォルダが見つかりません。\n\n{game_dir}\n\nパスを確認してください。",
            )
            return None
        return game_dir

    def install(self):
        game_dir = self.validate_path()
        if not game_dir:
            return

        ja_src = resource_path("ja.po")
        if not os.path.exists(ja_src):
            messagebox.showerror("エラー", "ja.po が見つかりません。")
            return

        ja_dst = os.path.join(game_dir, "localizations", "ja.po")
        backup = ja_dst + ".backup"

        try:
            # Backup
            if os.path.exists(ja_dst) and not os.path.exists(backup):
                shutil.copy2(ja_dst, backup)
                self.log("バックアップ作成: ja.po → ja.po.backup")
            elif os.path.exists(backup):
                self.log("バックアップは既に存在します。")

            # Copy
            shutil.copy2(ja_src, ja_dst)
            self.log(f"コピー完了: ja.po → {ja_dst}")
            self.log("")
            self.log("インストール完了！")
            self.set_status("インストール完了！ゲームで言語を「日本語」に設定してください。", "#228B22")
            messagebox.showinfo(
                "完了",
                "日本語化Modのインストールが完了しました。\n\n"
                "ゲームを起動し、設定から言語を\n「日本語」に変更してください。",
            )
        except PermissionError:
            self.log("エラー: アクセスが拒否されました。")
            messagebox.showerror(
                "エラー",
                "ファイルのコピーに失敗しました。\n\n"
                "ゲームが起動中の場合は終了してから再実行してください。\n"
                "管理者として実行する必要がある場合があります。",
            )
        except Exception as e:
            self.log(f"エラー: {e}")
            messagebox.showerror("エラー", f"インストールに失敗しました。\n\n{e}")

    def uninstall(self):
        game_dir = self.validate_path()
        if not game_dir:
            return

        ja_dst = os.path.join(game_dir, "localizations", "ja.po")
        backup = ja_dst + ".backup"

        if not os.path.exists(backup):
            result = messagebox.askyesno(
                "確認",
                "バックアップファイル（ja.po.backup）が見つかりません。\n\n"
                "Steamの「ゲームファイルの整合性を確認」機能で\n"
                "元のファイルを復元できます。\n\n"
                "現在の ja.po を削除しますか？\n"
                "（Steamで再取得する必要があります）",
            )
            if result:
                try:
                    os.remove(ja_dst)
                    self.log("ja.po を削除しました。")
                    self.log("Steamでゲームファイルの整合性を確認してください。")
                    self.set_status("ja.poを削除しました。Steamでファイルの整合性を確認してください。", "#CC6600")
                except Exception as e:
                    self.log(f"エラー: {e}")
            return

        try:
            shutil.copy2(backup, ja_dst)
            os.remove(backup)
            self.log("バックアップから復元: ja.po.backup → ja.po")
            self.log("")
            self.log("アンインストール完了！")
            self.set_status("アンインストール完了！元のja.poが復元されました。", "#228B22")
            messagebox.showinfo("完了", "日本語化Modをアンインストールしました。\n元のja.poが復元されました。")
        except Exception as e:
            self.log(f"エラー: {e}")
            messagebox.showerror("エラー", f"復元に失敗しました。\n\n{e}")


def main():
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
