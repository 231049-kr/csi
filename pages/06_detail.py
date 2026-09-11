import tkinter as tk
from tkinter import ttk, messagebox

class DetailScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="#EDF2F7")
        self.pack(fill="both", expand=True)

        # === 共通変数の定義 ===
        self.user_id = "100234"           # UserId: 6桁の識別ID
        self.password = "********"         # Password
        self.user_name = "鈴木 花子"       # UserName
        self.room_number = "102号室"      # RoomNumber
        self.status = "検知"              # Status: 正常 / 要確認 / 検知
        self.information = 95             # Information: CSI解析信頼度 (%)
        self.datetime_val = "2026-09-11 11:42" # Date & Time
        
        # バイタル情報
        self.heart_rate = "78 bpm"        # 心拍数
        self.respiration = "18 回/分"     # 呼吸数
        
        # 過去の履歴データ（Status Log連携用サンプル）
        self.history_logs = [
            ("2026-09-11 11:42", "102号室", "高", "転倒検知"),
            ("2026-09-11 08:15", "102号室", "低", "離床検知"),
            ("2026-09-10 22:30", "102号室", "低", "就寝確認"),
        ]

        # Urgency (緊急度) の自動算出 ("低", "中", "高")
        self.urgency = self.calculate_urgency(self.status, self.information)

        self.create_widgets()

    def calculate_urgency(self, status, confidence):
        if status == "検知":
            return "高" if confidence >= 80 else "中"
        elif status == "要確認":
            return "中"
        else:
            return "低"

    def get_urgency_color_style(self, urgency):
        styles = {
            "高": {
                "bg": "#FDF2F2", "border": "#F3B1B1", "main": "#E02424", 
                "text": "#9B1C1C", "tag_text": "⚠️ 転倒検知 (緊急度: 高)", "icon": "!"
            },
            "中": {
                "bg": "#FFFBEB", "border": "#FDE68A", "main": "#D97706", 
                "text": "#92400E", "tag_text": "⚡ 状態変化 (緊急度: 中)", "icon": "▲"
            },
            "低": {
                "bg": "#F3F1F6", "border": "#DEF7EC", "main": "#057A55", 
                "text": "#03543F", "tag_text": "正 正常動作中 (緊急度: 低)", "icon": "✓"
            }
        }
        return styles.get(urgency, styles["低"])

    def create_widgets(self):
        style = self.get_urgency_color_style(self.urgency)

        # --- Top Header ---
        top_header = tk.Frame(self, bg="#E1EFFE", height=50)
        top_header.pack(fill="x", side="top")
        
        lbl_title = tk.Label(
            top_header, text="6 監視対象者 詳細画面", 
            font=("Hiragino Sans", 18, "bold"), fg="#1A56DB", bg="#E1EFFE", pady=12
        )
        lbl_title.pack(side="left", padx=20)

        # --- System Bar ---
        sys_bar = tk.Frame(self, bg="#111928", height=40)
        sys_bar.pack(fill="x")
        
        tk.Label(sys_bar, text="🏠 WiFi-CSI 見守りシステム", font=("Hiragino Sans", 11), fg="white", bg="#111928").pack(side="left", padx=20, pady=8)
        tk.Label(sys_bar, text=f"👤 {self.user_name} ({self.user_id})", font=("Hiragino Sans", 11), fg="white", bg="#111928").pack(side="right", padx=20, pady=8)

        # --- Main Container ---
        container = tk.Frame(self, bg="white", highlightthickness=1, highlightbackground="#D1D5DB")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # 「一覧に戻る」リンク
        lbl_back = tk.Label(container, text="< 一覧に戻る (Room Info)", font=("Hiragino Sans", 10), fg="#1A56DB", bg="white", cursor="hand2")
        lbl_back.pack(anchor="w", padx=20, pady=(15, 5))

        # --- User Info Area ---
        profile_frame = tk.Frame(container, bg="white")
        profile_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(profile_frame, text="👤", font=("Hiragino Sans", 28), fg="#6B7280", bg="#E5E7EB", width=2).pack(side="left", padx=(0, 12))
        
        name_frame = tk.Frame(profile_frame, bg="white")
        name_frame.pack(side="left")
        
        tk.Label(name_frame, text=f"{self.room_number}  {self.user_name}", font=("Hiragino Sans", 16, "bold"), fg="#111928", bg="white").pack(anchor="w")
        tk.Label(name_frame, text=f"ID: {self.user_id} | 最終更新: {self.datetime_val}", font=("Hiragino Sans", 10), fg="#6B7280", bg="white").pack(anchor="w", pady=(2, 0))
        
        lbl_urgency_tag = tk.Label(
            profile_frame, text=style["tag_text"], font=("Hiragino Sans", 10, "bold"),
            fg=style["text"], bg=style["bg"], padx=10, pady=5,
            highlightthickness=1, highlightbackground=style["border"]
        )
        lbl_urgency_tag.pack(side="right", anchor="n")

        # --- Tab Buttons Area ---
        tab_frame = tk.Frame(container, bg="white")
        tab_frame.pack(fill="x", padx=20, pady=(15, 0))

        self.btn_tab_status = tk.Button(
            tab_frame, text="現在の状態", font=("Hiragino Sans", 10, "bold"), fg="white", bg="#1A56DB", 
            relief="flat", padx=15, pady=6, command=lambda: self.switch_tab("status")
        )
        self.btn_tab_status.pack(side="left", padx=(0, 5))

        self.btn_tab_vital = tk.Button(
            tab_frame, text="バイタル情報", font=("Hiragino Sans", 10), fg="#4B5563", bg="#F9FAFB", 
            relief="flat", padx=15, pady=6, command=lambda: self.switch_tab("vital")
        )
        self.btn_tab_vital.pack(side="left", padx=5)

        self.btn_tab_history = tk.Button(
            tab_frame, text="過去の履歴", font=("Hiragino Sans", 10), fg="#4B5563", bg="#F9FAFB", 
            relief="flat", padx=15, pady=6, command=lambda: self.switch_tab("history")
        )
        self.btn_tab_history.pack(side="left", padx=5)

        # --- Content Display Frame (切り替え対象コンテンツ表示エリア) ---
        self.content_frame = tk.Frame(container, bg="white")
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # 初期表示（現在の状態）
        self.style = style
        self.show_status_view()

        # --- Bottom Buttons ---
        btn_frame = tk.Frame(container, bg="white")
        btn_frame.pack(fill="x", side="bottom", padx=20, pady=15)
        
        btn_action = tk.Button(
            btn_frame, text="対応する (Status Log連携)", font=("Hiragino Sans", 11, "bold"), 
            fg="white", bg=style["main"], activebackground=style["main"], relief="flat", padx=20, pady=8,
            command=self.on_status_log_action
        )
        btn_action.pack(side="left")
        
        btn_view = tk.Button(
            btn_frame, text="詳細履歴を見る", font=("Hiragino Sans", 11), 
            fg="#1A56DB", bg="white", relief="flat", highlightthickness=1, highlightbackground="#1A56DB", padx=20, pady=8,
            command=lambda: self.switch_tab("history")
        )
        btn_view.pack(side="right")

    def clear_content(self):
        """表示コンテンツエリアのクリア"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def update_tab_styles(self, active_tab):
        """タブボタンの見た目更新"""
        tabs = {
            "status": self.btn_tab_status,
            "vital": self.btn_tab_vital,
            "history": self.btn_tab_history
        }
        for name, btn in tabs.items():
            if name == active_tab:
                btn.configure(fg="white", bg="#1A56DB", font=("Hiragino Sans", 10, "bold"))
            else:
                btn.configure(fg="#4B5563", bg="#F9FAFB", font=("Hiragino Sans", 10))

    def switch_tab(self, tab_name):
        """タブ切替処理"""
        self.clear_content()
        self.update_tab_styles(tab_name)
        
        if tab_name == "status":
            self.show_status_view()
        elif tab_name == "vital":
            self.show_vital_view()
        elif tab_name == "history":
            self.show_history_view()

    def show_status_view(self):
        """「現在の状態」画面"""
        style = self.style
        
        # Alert Panel
        alert_panel = tk.Frame(self.content_frame, bg=style["bg"], highlightthickness=1, highlightbackground=style["border"])
        alert_panel.pack(fill="x", pady=(5, 10))
        
        alert_content = tk.Frame(alert_panel, bg=style["bg"])
        alert_content.pack(side="left", padx=15, pady=12)
        
        tk.Label(alert_content, text=style["icon"], font=("Hiragino Sans", 18, "bold"), fg="white", bg=style["main"], width=2).pack(side="left", padx=(0, 10))
        
        text_frame = tk.Frame(alert_content, bg=style["bg"])
        text_frame.pack(side="left")
        
        msg_text = f"【ステータス: {self.status}】" + (" 転倒の可能性があります" if self.status == "検知" else " 状態確認が必要です" if self.status == "要確認" else " 正常に稼働中")
        tk.Label(text_frame, text=msg_text, font=("Hiragino Sans", 13, "bold"), fg=style["text"], bg=style["bg"]).pack(anchor="w")
        
        info_sub = tk.Frame(text_frame, bg=style["bg"])
        info_sub.pack(anchor="w", pady=(2, 0))
        tk.Label(info_sub, text="CSI解析信頼度: ", font=("Hiragino Sans", 10), fg=style["text"], bg=style["bg"]).pack(side="left")
        tk.Label(info_sub, text=f"{self.information}%", font=("Hiragino Sans", 11, "bold"), fg=style["main"], bg=style["bg"]).pack(side="left")

        # Details
        details = [
            ("ユーザーID (UserId)", self.user_id),
            ("部屋番号 (RoomNumber)", self.room_number),
            ("ステータス (Status)", self.status),
            ("緊急度 (Urgency)", self.urgency),
            ("信頼度 (Information)", f"{self.information}%"),
            ("日時 (Date & Time)", self.datetime_val),
            ("センサー状態", "正常")
        ]
        
        detail_frame = tk.Frame(self.content_frame, bg="white")
        detail_frame.pack(fill="x", pady=5)
        for i, (k, v) in enumerate(details):
            tk.Label(detail_frame, text=k, font=("Hiragino Sans", 10), fg="#4B5563", bg="white", anchor="w", width=22).grid(row=i, column=0, pady=2)
            color = style["main"] if k.startswith("緊急度") else ("#057A55" if k == "センサー状態" else "#111928")
            tk.Label(detail_frame, text=v, font=("Hiragino Sans", 10, "bold" if k in ["緊急度 (Urgency)", "センサー状態"] else "normal"), fg=color, bg="white").grid(row=i, column=1, pady=2, sticky="w")

    def show_vital_view(self):
        """「バイタル情報」画面"""
        panel = tk.Frame(self.content_frame, bg="#F3F4F6", highlightthickness=1, highlightbackground="#E5E7EB", pady=15)
        panel.pack(fill="x", pady=10)

        tk.Label(panel, text="🫀 バイタルリアルタイムモニタリング", font=("Hiragino Sans", 12, "bold"), fg="#111928", bg="#F3F4F6").pack(anchor="w", padx=15, pady=(0, 10))

        vitals = [
            ("心拍数 (Heart Rate)", self.heart_rate, "🟢 正常範囲"),
            ("呼吸数 (Respiration)", self.respiration, "🟢 正常範囲"),
            ("体温推定", "36.5 ℃", "🟢 正常範囲"),
            ("CSI非接触センシング", "安定受信中", "🔵 高精度モード")
        ]

        for k, v, status in vitals:
            row = tk.Frame(panel, bg="white", highlightthickness=1, highlightbackground="#E5E7EB", padx=10, pady=8)
            row.pack(fill="x", padx=15, pady=4)
            tk.Label(row, text=k, font=("Hiragino Sans", 10, "bold"), fg="#374151", bg="white", width=20, anchor="w").pack(side="left")
            tk.Label(row, text=v, font=("Hiragino Sans", 11, "bold"), fg="#1A56DB", bg="white", width=15, anchor="w").pack(side="left")
            tk.Label(row, text=status, font=("Hiragino Sans", 9), fg="#057A55", bg="white").pack(side="right")

    def show_history_view(self):
        """「過去の履歴」画面 (Status Log連携)"""
        panel = tk.Frame(self.content_frame, bg="white")
        panel.pack(fill="both", expand=True, pady=5)

        tk.Label(panel, text="📜 直近の検知・アクセス履歴 (Status Log)", font=("Hiragino Sans", 11, "bold"), fg="#111928", bg="white").pack(anchor="w", pady=(0, 8))

        # テーブルヘッダー
        headers = ["日時", "場所", "緊急度", "記録内容"]
        header_frame = tk.Frame(panel, bg="#E5E7EB")
        header_frame.pack(fill="x")
        
        widths = [18, 10, 8, 20]
        for h, w in zip(headers, widths):
            tk.Label(header_frame, text=h, font=("Hiragino Sans", 9, "bold"), fg="#374151", bg="#E5E7EB", width=w, anchor="w", padx=5, pady=4).pack(side="left")

        # 履歴行
        for log in self.history_logs:
            row = tk.Frame(panel, bg="white", highlightthickness=1, highlightbackground="#F3F4F6")
            row.pack(fill="x", pady=2)
            
            dt, loc, urg, desc = log
            urg_color = "#E02424" if urg == "高" else ("#D97706" if urg == "中" else "#057A55")
            
            tk.Label(row, text=dt, font=("Hiragino Sans", 9), fg="#4B5563", bg="white", width=18, anchor="w", padx=5, pady=4).pack(side="left")
            tk.Label(row, text=loc, font=("Hiragino Sans", 9), fg="#4B5563", bg="white", width=10, anchor="w", padx=5, pady=4).pack(side="left")
            tk.Label(row, text=urg, font=("Hiragino Sans", 9, "bold"), fg=urg_color, bg="white", width=8, anchor="w", padx=5, pady=4).pack(side="left")
            tk.Label(row, text=desc, font=("Hiragino Sans", 9), fg="#111928", bg="white", width=20, anchor="w", padx=5, pady=4).pack(side="left")

    def on_status_log_action(self):
        messagebox.showinfo(
            "対応完了", 
            f"Status Logに対応履歴を記録しました。\n\n"
            f"・日時: {self.datetime_val}\n"
            f"・場所: {self.room_number}\n"
            f"・緊急度(Urgency): {self.urgency}\n"
            f"・状態(Status): {self.status}"
        )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("WiFi-CSI 見守りシステム - 詳細画面")
    root.geometry("640x700")
    app = DetailScreen(master=root)
    root.mainloop()