import colorama
import tkinter as tk
import random
import time
import webbrowser
from tkinter import messagebox
import os
from yaspin import yaspin
from plyer import notification

messagebox.showwarning("Внимание.", "Если у вас выключены уведомления Windows, То настоятельно рекомендую их включить вручную через параметры.")

notification.notify(
    title="ВНИМАНИЕ!",
    message="Питон может сломаться, если терминал слишком маленький по оси y (в ширину). (Максим сломает, если вкратце)",
    timeout=9,
    app_name="Дз Максима (не)",
    toast=True

)

def quiz_1488():
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()
    
    # Создаем окно квиза
    quiz_window = tk.Toplevel(window)
    quiz_window.title("КВИЗ ДЛЯ ДМИТРИЯ")
    quiz_window.geometry("400x300")
    quiz_window.configure(bg="#2c3e50")
    quiz_window.resizable(False, False)
    
    # Вопрос
    question_label = tk.Label(
        quiz_window,
        text="СКОЛЬКО СТРОЧЕК КОДА В ЭТОЙ ДОМАШКЕ?",
        font=("Arial", 16, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50",
        wraplength=350
    )
    question_label.pack(pady=20)
    
    # Варианты ответов
    answers = [
        ("1489", False),
        ("1487", False), 
        ("1488", True),  # Правильный ответ
        ("1400", False)
    ]
    
    def check_answer(answer_index, is_correct):
        if is_correct:
            # Правильный ответ - тюрьма
            result_label.config(
                text="ПРАВИЛЬНЫЙ ОТВЕТ!\nНО ПО ПРАВИЛАМ ВЫ ДОЛЖНЫ СЕСТЬ В ТЮРЬМУ ЗА 1488!",
                fg="#e74c3c"
            )
            
            # Блокируем кнопки
            for btn in answer_buttons:
                btn.config(state="disabled")
            
            # Уведомление виндовс
            try:
                notification.notify(
                    title="КВИЗ РЕЗУЛЬТАТ",
                    message="ПРАВИЛЬНЫЙ ОТВЕТ! НО ПО ПРАВИЛАМ ВЫ ДОЛЖНЫ БУДЕТЕ СЕСТЬ В ТЮРЬМУ ЗА 1488!",
                    timeout=5,
                    app_name="Дз Максима (не)",
                    toast=True
                )
            except:
                pass
            
            # Через 5 секунд тюрьма мурино
            quiz_window.after(5000, lambda: [quiz_window.destroy(), advanced_prison_1488(60)])
        else:
            # Неправильный ответ
            result_label.config(
                text="НЕПРАВИЛЬНО!",
                fg="#e67e22"
            )
            quiz_window.after(3000, lambda: [quiz_window.destroy(), advanced_prison_1488(30)])
    
    # Создаем кнопки ответов
    answer_buttons = []
    for i, (answer_text, is_correct) in enumerate(answers):
        btn = tk.Button(
            quiz_window,
            text=answer_text,
            font=("Arial", 14),
            bg="#3498db",
            fg="white",
            width=15,
            height=2,
            command=lambda idx=i, correct=is_correct: check_answer(idx, correct)
        )
        btn.pack(pady=5)
        answer_buttons.append(btn)
    
    # Метка для результата
    result_label = tk.Label(
        quiz_window,
        text="",
        font=("Arial", 12, "bold"),
        bg="#2c3e50",
        fg="#27ae60",
        wraplength=350,
        justify="center"
    )
    result_label.pack(pady=20)



class EasterEggs:
    @staticmethod
    def maybe_show():
        if random.random() < 0.09:
            eggs = [
                " ⚠️СЕКРЕТ: Ум Максима не найден! Неверный синтаксис!",
                " ⚠️ERROR: Максим.exe перестал отвечать!",
                " ⚠️PYLANCE: Максим делай дз.",
                " ⚠️SYSTEM: Обнаружена лень У Максима!",
                "⚠️DEBUG: В коде найдены следы пиццы от Максима!",
                " ⚠️ALERT: Максим играет в CS2 вместо ДЗ!",
                " ⚠️WARNING: Уровень сна Максима = 99%!",
                " ⚠️CRITICAL: Учебники Python у Максима не обнаружены!",
                " ⚠️BUG: Баг в мотивации Максима!",
                " ⚠️SECRET: Максим великий программист! (нет)"
            ]
            print(f"\033[91m{random.choice(eggs)}\033[0m")

    @staticmethod
    def maybe_show_notification():
        if random.random() < 0.1:  # 1щ0% шанс
            eggs = [
                "⚠️ СЕКРЕТ: Ум Максима не найден! Неверный синтаксис!",
                " ⚠️ERROR: Максим.exe перестал отвечать!",
                "⚠️ ПАСХАЛКА: Ты нашёл секретное сообщение!",
                " ⚠️SYSTEM: Обнаружена лень У Максима!",
                " ⚠️DEBUG: В коде найдены следы пиццы от Максима!",
                "⚠️ALERT: Максим играет в CS2 вместо ДЗ!",
                " ⚠️WARNING: Уровень сна Максима = 99%!",
                "⚠️ CRITICAL: Учебники Python у Максима не обнаружены!",
                " ⚠️BUG: Баг в мотивации Максима!",
                " ⚠️SECRET: Максим великий программист! (нет)"
            ]
            message = random.choice(eggs)
            if "ERROR" in message or "CRITICAL" in message:
                title = " ОШИБКА"
                timeout = 8
            elif "ПАСХАЛКА" in message or "СЕКРЕТ" in message:
                title = "ПАСХАЛКО"
                timeout = 12
            elif "WARNING" in message:
                title = " ПРЕДУПРЕЖДЕНИЕ"
                timeout = 6
            else:
                title = " УВЕДОМЛЕНИЕ"
                timeout = 5               
               

            try:
                notification.notify(
                    title=title,
                    message=message,
                    timeout=timeout,
                    app_name="Дз Максима (не)",
                    toast=True
                )
                print(f"{Colors.CYAN}Уведомление Успешно отправлено!{Colors.RESET}{Colors.RED}[ОТЛАДКА]{Colors.RESET}") # ОТЛАДКА
            except Exception as e:
                print(f"Ошибка! {e}")
            except Exception:
                # Если уведомления не работают, просто игнорируем
                pass




    


os.system("")
colorama.init()
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

privet0 = yaspin(text="Загружаю Крутые уведомления...", color="cyan")
privet0.start()
time.sleep(2.1)
privet0.ok("✅")
privet22 = yaspin(text="Загружаю пасхалочки...", color="cyan")
privet22.start()
time.sleep(2)
privet22.ok("✅")
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
with yaspin(text="Загружаю Максима",color="cyan",timer=False):
    time.sleep(2)
print("✅")
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet1 = yaspin(text="Загружаю ДЗ 1...", color="cyan")
privet1.start()
time.sleep(0.5)
privet1.ok("✅")
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet2 = yaspin(text="Загружаю ДЗ 2...", color="cyan")
privet2.start()
time.sleep(0.7)
privet2.ok("✅")
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet3 = yaspin(text="Загружаю ДЗ 3...", color="cyan")
privet3.start()
time.sleep(0.5)
privet3.ok("✅")
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet4 = yaspin(text="Загружаю тюрьму 1488 и МАКС...", color="cyan")
privet4.start()
time.sleep(0.7)
privet4.ok("✅")
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet5 = yaspin(text="Максим делает дз...", color="red")
privet5.start()
time.sleep(1)
privet5.fail("[❌] Максим слишком ленивый сегодня")
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet6 = yaspin(text="Загружаю пасхалку", color="cyan")
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet6.start()
time.sleep(1.5)
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet6.ok("✅")
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet7 = yaspin(text="Дмитрий ставит кодкоины...", color="cyan")
privet7.start()
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
time.sleep(1)
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
privet7.ok("✅")
print(f"{Colors.RED}Pylance error function Ум_Максима not defined!")
print("Pylance error MAX_PRISON1488 not defined!")
print(f"Pylance error{Colors.RESET}")
print(f"{Colors.YELLOW}Pylance warning Вы обязаны начислить код коины А. Матвею. failue to emergency stop")
print(f"Pylance warning я слышу звук минипекки из клеш рояля failue to emergency stop")
print(f"File c/Users/Qkrt/Onedrive/Downloads lesson_9.py, line 1488 in <module> Та я не делал эту ошибку NameError: name 'ало я не делал эту ошибку, это всё максим Мурино' is not defined{Colors.RESET} ")
print(f"{Colors.RED} Государственный мессенджер MAX не был установлен! Пожалуйста, установите мессенджер!")
print("PermissionError: [Errno 1488] Permission denied")
print("webbrowser.Error: could not locate runnable browser")
print(f"OSError: [WinError 5] Отказано в доступе{Colors.RESET}")
print(f"{Colors.YELLOW}DeprecationWarning: something is deprecated")
print(f"SyntaxError: 1488 is not defined.{Colors.RESET}")
time.sleep(1)
print(f"{Colors.GREEN} Packpages Install success: PackPage colorama installed successfully!")
print(f"yaspin Installed yet!{Colors.RESET}")



EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
with yaspin(text="Подготавливаю рекомендации...", color="yellow") as sp:
    time.sleep(1.5)
    sp.ok("✅")

notification.notify(
    title="Рекомендация:",
    message="проверяйте это дз последним или за час до занятия. Рекомендуется тестировать с открытым терминалом.",
    timeout=7,
    app_name="ДЗ Максима(нет)",
    toast=True
)
EasterEggs.maybe_show()
EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
with yaspin(text="Создаю главное окно...", color="magenta") as sp:
    time.sleep(1.2)
    sp.ok("✅")

window = tk.Tk()
window.title("ДЗ 1 -'ШАРМАНКА'")
window.geometry("300x250")




def Krasniy():
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Инициализация проверки...", color="blue") as sp:
        time.sleep(1)
        sp.ok("✅")

    ask2 = "no"
    
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    sp = yaspin(text="Ожидаю ответа...(на ответ 10 сек.)", color="cyan")
    sp.start()

    try:
        import threading

        def show_dialog():
            nonlocal ask2
            ask2 = messagebox.askquestion("Внимание.", "Вы уже красный и тд?\n\n(Автоматический ответ 'НЕТ' через 10 секунд)")
        dialog_thread = threading.Thread(target=show_dialog)
        dialog_thread.daemon = True
        dialog_thread.start()
        
        # Ждем максимум 10 секунд
        dialog_thread.join(timeout=10)
        
        if  dialog_thread.is_alive():
            ask2 = "no"
            print(f"{Colors.YELLOW} Время вышло! Автоматический ответ: НЕТ{Colors.RESET}")

    except Exception as e:
        ask2 = "no"
        print(f"{Colors.YELLOW}Неизвестная ошибка в откладке: {e}{Colors.RESET}{Colors.RED}[EXCEPTION]{Colors.RESET}")

        try:
            notification.notify(
                title="ВРЕМЯ ВЫШЛО!",
                messge="Автоматически выбран ответ 'НЕТ'",
                timeout=5,
                app_name="ДЗ Максима",
                toast=True

            )
        except Exception as Notif_error:
            print(f"{Colors.YELLOW} Ошибка уведомления: {Notif_error}{Colors.RESET}{Colors.RED}[EXCEPTION]{Colors.RESET}")
ask2 = messagebox.askquestion("Внимание.", "Вы уже красный и тд?")
if ask2 == "yes":
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Открываю доступ для красных...", color="red") as sp2:
            time.sleep(1.5)
            sp2.ok("✅")
        webbrowser.open_new_tab("https://drive.google.com/file/d/1Q-w0XtP0-ioP0u9zYyYdGsDZBFQWJsiE/view?usp=sharing")
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification() 
        sp.ok("✅")
else:
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Открываю стандартный доступ...", color="green") as sp2:
            time.sleep(1.5)
            sp2.ok("✅")
        webbrowser.open_new_tab("https://drive.google.com/file/d/1MiLohC9c3dZc-Fp1PbKDNYJiHoHBbsrN/view?usp=sharing")
        sp.fail("❌")

def RussianRoulette():
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Загружаю русскую рулетку...", color="red") as sp:
        time.sleep(2)
        sp.ok("🎰 ")
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    roulette_window = tk.Toplevel()
    roulette_window.title("🇷🇺 РУССКАЯ РУЛЕТКА 🇷🇺")
    roulette_window.attributes('-fullscreen', True)
    roulette_window.configure(bg='#000000')
    roulette_window.attributes('-topmost', True)
    
    roulette_window.protocol("WM_DELETE_WINDOW", lambda: None)
    roulette_window.bind('<Escape>', lambda e: "break")
    roulette_window.bind('<F11>', lambda e: "break")
    
    main_frame = tk.Frame(roulette_window, bg='#000000')
    main_frame.place(relx=0.5, rely=0.5, anchor='center')
    
    title_label = tk.Label(
        main_frame,
        text="🇷🇺 РУССКАЯ РУЛЕТКА 🇷🇺",
        font=("Arial", 36, "bold"),
        fg="#c0392b",
        bg='#000000'
    )
    title_label.pack(pady=30)
    
    desc_label = tk.Label(
        main_frame,
        text="В револьвере 6 патронов. Один из них настоящий.\nВаш компьютер на кону!\nУ вас 10 секунд на ход!",
        font=("Arial", 20),
        fg="#ecf0f1",
        bg='#000000',
        justify='center'
    )
    desc_label.pack(pady=20)
    
    revolver_art = "ВНИМАНИЕ! ЭТА ИГРА РЕАЛЬНО МОЖЕТ ВЫКЛЮЧИТЬ ВАШ ПК! ИГРАЙТЕ НА СВОЙ СТРАХ И РИСК!"
    
    revolver_label = tk.Label(
        main_frame,
        text=revolver_art,
        font=("Courier New", 16),
        fg="#e74c3c",
        bg='#000000'
    )
    revolver_label.pack(pady=30)
    
    bullets_left = 6
    bullet_label = tk.Label(
        main_frame,
        text=f"🎯 Патронов в барабане: {bullets_left}",
        font=("Arial", 24, "bold"),
        fg="#f1c40f",
        bg='#000000'
    )
    bullet_label.pack(pady=20)
    
    time_left = 10
    timer_label = tk.Label(
        main_frame,
        text=f"⏰ Время на ход: {time_left} сек",
        font=("Arial", 20, "bold"),
        fg="#00ff00",
        bg='#000000'
    )
    timer_label.pack(pady=10)
    
    result_label = tk.Label(
        main_frame,
        text="",
        font=("Arial", 20, "bold"),
        bg='#000000',
        height=3
    )
    result_label.pack(pady=20)
    
    button_frame = tk.Frame(main_frame, bg='#000000')
    button_frame.pack(pady=30)
    
    game_active = True
    
    def fire_gun():
        nonlocal bullets_left, game_active
        
        if not game_active or bullets_left <= 0:
            return
            
        bullets_left -= 1
        bullet_label.config(text=f"🎯 Патронов в барабане: {bullets_left}")
        
        deadly_chamber = random.randint(1, 6)
        current_chamber = 6 - bullets_left
        
        result_label.config(text="💥 ВЫ СТРЕЛЯЕТЕ...", fg="#e74c3c")
        roulette_window.update()
        time.sleep(2)
        
        if current_chamber == deadly_chamber:
            result_label.config(
                text="💀 ВЫ ПРОИГРАЛИ!\n\nКомпьютер выключается...", 
                fg="#c0392b"
            )
            fire_button.config(state="disabled")
            exit_button.config(state="disabled")
            game_active = False
            
            for i in range(5):
                blood_label = tk.Label(
                    roulette_window,
                    text="💀",
                    font=("Arial", 48),
                    fg="#c0392b",
                    bg='#000000'
                )
                x = random.randint(100, roulette_window.winfo_screenwidth() - 100)
                y = random.randint(100, roulette_window.winfo_screenheight() - 100)
                blood_label.place(x=x, y=y)
            
            roulette_window.after(2000, lambda: os.system("shutdown /s /t 1"))
            
        else:
            result_label.config(
                text=" ВАМ ПОВЕЗЛО! Холостой патрон!\nКомпьютер в безопасности!",
                fg="#27ae60"
            )
            
            if bullets_left > 0:
                nonlocal time_left
                time_left = 10
                timer_label.config(text=f" Время на ход: {time_left} сек", fg="#00ff00")
            else:
                result_label.config(
                    text=" ПОБЕДА! Все патроны разряжены!\nКомпьютер спасен!",
                    fg="#27ae60"
                )
                fire_button.config(state="disabled")
                exit_button.config(state="normal", text="ВЫЙТИ")
                game_active = False
    
    def update_timer():
        nonlocal time_left, game_active
        
        if game_active and time_left > 0:
            time_left -= 1
            timer_label.config(text=f" Время на ход: {time_left} сек")
            
            if time_left <= 5:
                timer_label.config(fg="#e74c3c")
            
            roulette_window.after(1000, update_timer)
        elif game_active and time_left <= 0:
            result_label.config(text=" ВРЕМЯ ВЫШЛО! Автоматический выстрел...", fg="#e67e22")
            roulette_window.after(1000, fire_gun)
    
    fire_button = tk.Button(
        button_frame,
        text="🔫 ВЫСТРЕЛИТЬ",
        font=("Arial", 20, "bold"),
        bg="#c0392b",
        fg="white",
        width=15,
        height=2,
        command=fire_gun
    )
    fire_button.pack(side="left", padx=20)
    
    def exit_game():
        roulette_window.destroy()
        messagebox.showinfo("Выход", "Вы вышли из игры. Компьютер в безопасности.")
    
    exit_button = tk.Button(
        button_frame,
        text="🚪 ВЫЙТИ",
        font=("Arial", 20, "bold"),
        bg="#34495e",
        fg="white",
        width=15,
        height=2,
        command=exit_game
    )
    exit_button.pack(side="left", padx=20)
    
    roulette_window.after(1000, update_timer)

def KodKoini():
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Подключаюсь к серверу кодкоинов...", color="yellow") as sp:
        time.sleep(0.9)
        sp.ok("✅ ")
    webbrowser.open_new_tab("https://erp.code-class.ru/admin/login")

def SHUTDOWN_COMP():
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Подготавливаю систему выключения...", color="red") as sp:
        time.sleep(1.5)
        sp.ok("✅ ")
    
    Confirm1 = messagebox.askquestion("ПОДОЖДИТЕ...", "ВЫ УВЕРЕНЫ ЧТО ХОТИТЕ ВЫКЛЮЧИТЬ КОМПЬЮТЕР??")
    if Confirm1 == "yes":
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Инициализирую выключение...", color="red") as sp:
            time.sleep(1)
            sp.ok("✅ ")
        print("ОТПРАВЛЯЮ messagebox.showerror")
        messagebox.showerror("ВЫКЛЮЧАЮ ПК.", "ПРОЩАЙТЕ.")
        print("ВЫКЛЮЧАЮ КОМП")
        os.system("shutdown /s /t 300")
        time.sleep(3)
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Отменяю выключение...", color="green") as sp:
            time.sleep(1)
            sp.ok("✅ ")
        print("ОТМЕНЯЮ ВЫКЛЮЧЕНИЕ КОМПА ЧЕРЕЗ ТАЙМЕР")
        os.system("shutdown /a")

def Cs2():
    cs2_path = r"C:\Program Files (x86)\Steam\steam.exe"
    
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Ожидаю ответа...", color="cyan") as sb2:
        Cs2Confirm = messagebox.askquestion(
            "Стоп.", 
            "Вы точно хотите запустить прикольный шутер от первого лица вместо проверки моего домашнего задания?"
        )
    
    if Cs2Confirm == "yes":
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Проверяю наличие КС2...", color="cyan") as sb2_1:
            time.sleep(2)
            
            if os.path.exists(cs2_path):
                sb2_1.ok("✅ ")
                
                EasterEggs.maybe_show()
                EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
                with yaspin(text="Запускаю CS2...", color="green") as sb2_2:
                    try:
                        os.system(f'"{cs2_path}" -applaunch 730')
                        time.sleep(2)
                        sb2_2.ok("✅ ")
                        print("КС2 запускается!")
                    except Exception as e:
                        sb2_2.fail("❌ ")
                        messagebox.showerror("ОШИБКА", f"Ошибка запуска: {e}")
            else:
                sb2_1.fail("❌ ")
                messagebox.showerror("ОШИБКА", "КОД НЕ СМОГ НАЙТИ У ВАС КС2. ВСЕГО ДОБРОГО.")
    
    else:
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Пользователь отказался от CS2...", color="yellow") as sp:
            time.sleep(1)
            sp.ok("✅ ")
        print("✅ Пользователь решил продолжить проверку ДЗ")

def Murino():
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Ищу информацию о Мурино...", color="blue") as Murin:
        time.sleep(1.5)
        Murin.ok("🗺️ ")
    webbrowser.open_new_tab("https://ru.wikipedia.org/wiki/Мурино")

def MINECRAFT():
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Загружаю МАЙНКР*ВТ...", color="green") as Murin1:
        time.sleep(1.5)
        Murin1.ok("✅ ")
    webbrowser.open_new_tab("https://drive.google.com/file/d/1grwi0VHUfbH4ByeM92cdJQak3ivFLReg/view?usp=sharing")
def b():
    webbrowser.open_new_tab("https://drive.google.com/file/d/12eNVIOpRR10KO34OQ-iz7hztQNCNV_n_/view?usp=sharing")
    notification.notify(
                    title="БЬ",
                    message="успешное Бь!",
                    timeout=10,
                    app_name="Дз Максима (не)",
                    toast=True
            )
dz2_clicked = False
dz3_clicked = False

secret_button = tk.Button(
    window, 
    text="СЕКРЕТКА", 
    font=("Arial", 12, "bold"),
    bg="#8B0000",
    fg="white",
    state="disabled",
    width=15,
    height=1
)
secret_button.pack(pady=5)

chislo = tk.Label(window, text="", font=("comic sans MS", 24), fg="#2e8b57")
chislo.pack(pady=20)

def check_secret_button():
    global dz2_clicked, dz3_clicked
    print(f"{Colors.YELLOW}Проверка секретки: dz2_clicked={dz2_clicked}, dz3_clicked={dz3_clicked}{Colors.RESET}")
    if dz2_clicked and dz3_clicked:
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Активирую секретную кнопку...", color="magenta") as sp:
            time.sleep(1.5)
            sp.ok("🔓 ")
        secret_button.config(state="normal", bg="#8B0000")
        notification.notify(
            title="ВНИМАНИЕ❗",
            message="Секретка Максима Бобик Мурино Открылась!",
            timeout=3,
            toast=True
        )
    else:
        print(f"{Colors.RED}Условие не выполнено: Нужно нажать обе кнопки ДЗ[ОТЛАДКА]{Colors.RESET}")


def open_secret_window():
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Открываю секретное окно...", color="red") as sp:
        time.sleep(1.5)
        sp.ok("✅ ")
    secret_window = tk.Toplevel(window)
    secret_window.title("СЕКРЕТНОЕ ОКНО")
    secret_window.geometry("500x900")
    secret_window.configure(bg="white")
    
    secret_canvas = tk.Frame(
        secret_window,
        bg="white",
        width=500,
        height=500
    )
    secret_canvas.pack(fill="both", expand=True, padx=10, pady=10)
    
    info_label = tk.Label(
        secret_canvas,
        text="ПАНЕЛЬ УПРАВЛЕНИЯ (ВЫ ДУМАЛИ ЭТО ВСЁ?)",
        font=("Arial", 10, "italic"),
        fg="gray",
        bg="white"
    )
    info_label.pack(pady=10)
    
    btn1 = tk.Button(
        secret_canvas,
        text="Я уже красный(КНОПКА СЛОМАЛАСЬ!)",
        font=("Arial", 10),
        bg="#d01414",
        fg="white",
        command=Krasniy,
        state="disabled",
    )
    btn1.pack(pady=5)
    
    btn2 = tk.Button(
        secret_canvas,
        text="запустить кс2 (если лень проверять дз)", 
        font=("Arial", 10),
        bg="orange",
        fg="white",
        command=Cs2
    )
    btn2.pack(pady=5)

    btn3 = tk.Button(
        secret_canvas,
        text="Где живет Максим",
        fg="green",
        bg="white",
        command=Murino
    )
    btn3.pack(pady=5)

    btn4 = tk.Button(
        secret_canvas,
        text="Начислить кодкоины (рекомендуется)",
        bg="cyan",
        fg="black",
        command=KodKoini,
    )
    btn4.pack(pady=5)
    
    btn5 = tk.Button(
        secret_canvas,
        text="ВЫКЛЮЧИТЬ КОМПЬЮТЕР ☠️",
        fg="white",
        bg="dark red",
        font=("Arial", 10, "bold"),
        command=SHUTDOWN_COMP
    )
    btn5.pack(pady=5)
    
    btn6 = tk.Button(
        secret_canvas,
        text="ИГРАТЬ В МАЙНКР*ВТ",
        bg="green",
        command=MINECRAFT
    )
    btn6.pack(pady=5)

    btn_roulette = tk.Button(
        secret_canvas,
        text="🔫 РУССКАЯ РУЛЕТКА",
        font=("Arial", 12, "bold"),
        bg="#c0392b",
        fg="white",
        width=25,
        height=2,
        command=RussianRoulette
        )
    btn_roulette.pack(pady=8)
    btn6 = tk.Button(
        secret_canvas,
        text="бь",
        bg="blue",
        fg="white",
        command=b
    )
    btn6.pack(pady=5)
        # Кнопка КВИЗ
    btn_quiz = tk.Button(
        secret_canvas,
        text="🧠 КВИЗ ПРО 1488",
        font=("Arial", 12, "bold"),
        bg="#9b59b6",
        fg="white",
        width=20,
        height=2,
        command=quiz_1488
    )
    btn_quiz.pack(pady=8)
    
    def fake():
        notification.notify(
                title="ИДЕТ ОПЕРАЦИЯ...",
                message="Жду ответа от VK FREE ROBUX1488...",
                timeout=1.5,
                toast=True
        )
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Проверяю наличие робуксов...", color="yellow") as sp:
            time.sleep(2)
            sp.fail("❌ ")
        notification.notify(
            title="ОШИБКА: ОТКАЗ ОТ VK FREE ROBUX1488",
            message="Извините, робуксы закончились. Приходите позже.",
            timeout=7,
            app_name="Дз Максима (не)",
            toast=True

        )

    dvd_space = tk.Frame(secret_canvas, bg="white", height=150)
    dvd_space.pack(fill="both", expand=True, pady=10)
    
    btn5_dvd = tk.Button(
        dvd_space,
        text="Поймай меня для робуксов",
        fg="white",
        bg="dark red",
        font=("Arial", 10, "bold"),
        command=fake
    )
    btn5_dvd.place(x=50, y=50)
    
    dvd_x, dvd_y = 50, 50
    dvd_dx, dvd_dy = 3, 3
    
    def move_dvd_button():
        nonlocal dvd_x, dvd_y, dvd_dx, dvd_dy
        
        dvd_x += dvd_dx
        dvd_y += dvd_dy
        
        space_width = dvd_space.winfo_width()
        space_height = dvd_space.winfo_height()
        btn_width = btn5_dvd.winfo_reqwidth()
        btn_height = btn5_dvd.winfo_reqheight()
        
        if dvd_x <= 0 or dvd_x + btn_width >= space_width:
            dvd_dx = -dvd_dx
            change_dvd_color()
            
        if dvd_y <= 0 or dvd_y + btn_height >= space_height:
            dvd_dy = -dvd_dy
            change_dvd_color()
        
        btn5_dvd.place(x=dvd_x, y=dvd_y)
        secret_window.after(20, move_dvd_button)
    
    def change_dvd_color():
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]
        new_color = random.choice(colors)
        btn5_dvd.config(bg=new_color)
    
    secret_window.after(100, move_dvd_button)

secret_button.config(command=open_secret_window)


def advanced_prison_1488(initial_sentence=60, is_life_sentence=False):
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Загружаю тюрьму...", color="red") as sp:
        time.sleep(2)
        sp.ok("✅Приятно просидеть вам за решёткой! ")
        notification.notify(
            title="НАЧАЛЬНИК БОБИК МУРИНО",
            message="ОТСИДИ СВОЙ СРОК ТУТ. ТОЛЬКО ПОПРОБУЙ СБЕЖАТЬ.",
            timeout=5,
            toast=True
        )

        
    
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    prison = tk.Toplevel(window)
    prison.title(" АДСКАЯ ТЮРЬМА ЗА 1488 (ТЮРЬМА №2 Г. МУРИНО) ")
    prison.attributes('-fullscreen', True) 
    prison.configure(bg='#000000')
    prison.attributes('-topmost', True)
    
    prison.protocol("WM_DELETE_WINDOW", lambda: None)
    prison.resizable(False, False)
    
    prison.bind('<F11>', lambda e: "break")
    prison.bind('<Escape>', lambda e: "break")
    
    start_time = time.time()
    current_sentence_time = initial_sentence
    early_release_used = False
    amnesty_available = False
    amnesty_cooldown = False
    luck_used = False
    
    if is_life_sentence:
        current_sentence_time = 999999
    
    main_frame = tk.Frame(prison, bg='#000000')
    main_frame.place(relx=0.5, rely=0.5, anchor='center')
    
    if is_life_sentence:
        title_text = " ВЫ ЗАКЛЮЧЕНЫ НАВСЕГДА ЗА 1488! (ТЮРЬМА №2 Г. МУРИНО) "
    else:
        title_text = " ВЫ ЗАКЛЮЧЕНЫ ЗА 1488! (ТЮРЬМА №2 Г. МУРИНО) "
    
    title_label = tk.Label(
        main_frame,
        text=title_text, 
        font=("Arial", 36, "bold"), 
        fg="red", 
        bg='#000000'
    )
    title_label.pack(pady=30)
    
    if is_life_sentence:
        timer_text = " Пожизненное заключение! "
    else:
        timer_text = f" Осталось: {current_sentence_time} секунд"
    
    timer_label = tk.Label(
        main_frame,
        text=timer_text, 
        font=("Comic Sans MS", 28), 
        fg="yellow", 
        bg='#000000'
    )
    timer_label.pack(pady=20)
    
    amnesty_warning_label = tk.Label(
        main_frame,
        text="", 
        font=("Arial", 16, "bold"), 
        fg="#00ff00", 
        bg='#000000'
    )
    amnesty_warning_label.pack(pady=10)
    
    progress_frame = tk.Frame(main_frame, bg='#000000')
    progress_frame.pack(pady=20)
    
    progress_bar = tk.Canvas(progress_frame, width=800, height=30, bg='#333333', highlightthickness=0)
    progress_bar.pack()
    progress_fill = progress_bar.create_rectangle(0, 0, 0, 30, fill='red', outline='')
    
    quotes = [
        "«1488 - КАК НЕПРАВИЛЬНАЯ НОТА В СИМФОНИИ МАТЕМАТИКИ»",
        "«ЧИСЛА ДОЛЖНЫ ОБЪЕДИНЯТЬ, А НЕ РАЗДЕЛЯТЬ»",
        "«МАТЕМАТИКА - ЯЗЫК ВСЕЛЕННОЙ, ГОВОРИТЕ НА НЁМ КРАСИВО»",
        "«КАЖДОЕ ЧИСЛО ИМЕЕТ ДУШУ, КРОМЕ 1488»",
        "«ВЫ НАРУШИЛИ ГАРМОНИЮ ЧИСЛОВОГО КОСМОСА!»",
        "«60 СЕКУНД - МАЛЕНОЕ НАКАЗАНИЕ ЗА БОЛЬШОЕ ПРЕСТУПЛЕНИЕ»",
        "«ДУМАЙТЕ О ЧИСЛАХ: π, e, φ, i... ОНИ ПРЕКРАСНЫ!»",
        "«МАТЕМАТИКА ПРОЩАЕТ, НО НЕ ЗАБЫВАЕТ...»",
        "«РИКРОЛЛ НА ФОНЕ - ЧАСТЬ ВАШЕГО НАКАЗАНИЯ!»",
        "«НАДЕЮСЬ, ВАМ НРАВИТСЯ МУЗЫКА НА ФОНЕ!»"
    ]
    
    if is_life_sentence:
        quotes.extend([
            "«ВЫ ДУМАЛИ, ЧТО ЭТО ШУТКА? СЕРЬЕЗНО ОШИБАЛИСЬ!»",
            "«ПОЖИЗНЕННОЕ! НАДЕЮСЬ, ВАМ НРАВИТСЯ РИКРОЛЛ!»",
            "«1488 - ВАШ ПРИГОВОР, ГОСПОДИН!»",
            "«СИДИТЕ И СЛУШАЙТЕ РИКРОЛЛ ДО КОНЦА СВОИХ ДНЕЙ!»",
            "«МАТЕМАТИКА ВАС НЕНАВИДИТ, УВАЖАЕМЫЙ!»",
            "«ВЫ СОВЕРШИЛИ НЕПРОСТИТЕЛЬНУЮ ОШИБКУ!»",
            "«ЗДЕСЬ ВАМ ПРЕДСТОИТ ПРОВЕСТИ ОЧЕНЬ ДОЛГОЕ ВРЕМЯ!»"
        ])
    
    quote_label = tk.Label(
        main_frame,
        text=quotes[0], 
        font=("Arial", 16, "italic"), 
        fg="#cccccc", 
        bg='#000000',
        wraplength=1000,
        justify="center"
    )
    quote_label.pack(pady=30)
    
    escape_message = tk.Label(
        main_frame,
        text="", 
        font=("Arial", 20, "bold"), 
        fg="#ff0000", 
        bg='#000000',
        wraplength=800,
        justify="center"
    )
    escape_message.pack(pady=10)
    
    def add_more_time():
        nonlocal current_sentence_time, start_time
        if is_life_sentence:
            escape_message.config(text="НАЧАЛЬНИК БОБИК МУРИНО: КУДА СОБРАЛИСЬ? У ВАС ПОЖИЗНЕННОЕ!")
            prison.after(3000, lambda: escape_message.config(text=""))
            return
            
        current_sentence_time += 15
        start_time = time.time()
        
        escape_message.config(text="НАЧАЛЬНИК БОБИК МУРИНО(ЗЛОЙ): ПОПЫТКА ПОБЕГА! +15 СЕКУНД К СРОКУ!")
        
        def clear_message():
            escape_message.config(text="")
        
        prison.after(3000, clear_message)
    
    def request_amnesty():
        nonlocal current_sentence_time, start_time, early_release_used, amnesty_available, amnesty_cooldown
        
        if amnesty_cooldown:
            return
            
        if not amnesty_available:
            if is_life_sentence:
                escape_message.config(text="АМНИСТИЯ БУДЕТ ДОСТУПНА ЧЕРЕЗ 10 СЕКУНД!")
            else:
                escape_message.config(text="АМНИСТИЯ ДОСТУПНА ПОСЛЕ 30 СЕКУНД!")
            prison.after(2000, lambda: escape_message.config(text=""))
            return
            
        if early_release_used:
            escape_message.config(text="ВЫ УЖЕ ИСПОЛЬЗОВАЛИ АМНИСТИЮ!")
            prison.after(2000, lambda: escape_message.config(text=""))
            return
        
        amnesty_cooldown = True
        amnesty_button.config(state="disabled", bg="#666666")
        
        def enable_amnesty_button():
            nonlocal amnesty_cooldown
            amnesty_cooldown = False
            if amnesty_available and not early_release_used:
                amnesty_button.config(state="normal", bg="#006400")
        
        prison.after(5000, enable_amnesty_button)
        
        wait_time = random.randint(3, 10)
        dots = 0
        
        def update_wait_animation():
            nonlocal dots, wait_time
            dots = (dots + 1) % 4
            wait_text = "ЖДИТЕ" + "." * dots
            escape_message.config(text=wait_text, fg="#ffff00")
            
            if wait_time > 0:
                wait_time -= 1
                prison.after(1000, update_wait_animation)
            else:
                if random.random() < 0.05:
                    early_release_used = True
                    current_sentence_time = 0
                    escape_message.config(text="🎉 ВАМ ПОВЕЗЛО! ДОСРОЧНОЕ ОСВОБОЖДЕНИЕ! 🎉", fg="#00ff00")
                    exit_button.config(state="normal", bg="#006400", text=" ВЫЙТИ НА СВОБОДУ!")
                    escape_button.config(state="disabled")
                    amnesty_button.config(state="disabled")
                    if is_life_sentence:
                        luck_button.config(state="disabled")
                else:
                    if is_life_sentence:
                        escape_message.config(text="ОТКАЗАНО! ОСТАВАЙТЕСЬ В ТЮРЬМЕ!", fg="#ff0000")
                    else:
                        escape_message.config(text="ПОМИЛОВАНИЕ ОТКЛОЕННО! СИДИТЕ ДАЛЬШЕ!", fg="#ff0000")
                    prison.after(2000, lambda: escape_message.config(text=""))
        
        update_wait_animation()
    
    def use_luck():
        nonlocal luck_used, current_sentence_time, early_release_used
        
        if luck_used:
            return
            
        luck_used = True
        luck_button.config(state="disabled", bg="#666666")
        
        wait_time = 10
        dots = 0
        
        def update_luck_animation():
            nonlocal dots, wait_time
            dots = (dots + 1) % 4
            wait_text = f"ОЖИДАЙТЕ... ОСТАЛОСЬ: {wait_time} СЕКУНД" + "." * dots
            escape_message.config(text=wait_text, fg="#ffa500")
            
            if wait_time > 0:
                wait_time -= 1
                prison.after(1000, update_luck_animation)
            else:
                if random.random() < 0.2:
                    early_release_used = True
                    current_sentence_time = 0
                    escape_message.config(text="🎉 НЕВЕРОЯТНО! ВАША УДАЧА СРАБОТАЛА! ОСВОБОЖДЕНИЕ! 🎉", fg="#00ff00")
                    exit_button.config(state="normal", bg="#006400", text=" ВЫЙТИ НА СВОБОДУ!")
                    escape_button.config(state="disabled")
                    amnesty_button.config(state="disabled")
                    luck_button.config(state="disabled")
                    timer_label.config(text=" ВЫ СВОБОДНЫ БЛАГОДАРЯ УДАЧЕ!", fg="#00ff00")
                else:
                    escape_message.config(text="❌ УВЫ, ВАША УДАЧА НЕ СРАБОТАЛА! ОСТАВАЙТЕСЬ В ТЮРЬМЕ! ❌", fg="#ff0000")
                    prison.after(3000, lambda: escape_message.config(text=""))
        
        update_luck_animation()
    
    escape_button = tk.Button(
        main_frame,
        text="Я УСТАЛ ТУТ СИДЕТЬ!", 
        font=("Arial", 16, "bold"),
        bg="#8B0000", 
        fg="white",
        width=20,
        height=2,
        command=add_more_time
    )
    escape_button.pack(pady=5)
    
    amnesty_button = tk.Button(
        main_frame,
        text="ПРОСИТЬ ПОМИЛОВАНИЕ У БОБИКА МУРИНО", 
        font=("Arial", 16, "bold"),
        bg="#4B0082", 
        fg="white",
        width=80,
        height=2,
        state="disabled",
        command=request_amnesty
    )
    amnesty_button.pack(pady=5)
    
    luck_button = tk.Button(
        main_frame,
        text="ИСПЫТАТЬ УДАЧУ", 
        font=("Arial", 16, "bold"),
        bg="#FF8C00", 
        fg="white",
        width=25,
        height=2,
        state="normal" if is_life_sentence else "disabled",
        command=use_luck
    )
    
    if is_life_sentence:
        luck_button.pack(pady=5)
    
    exit_button = tk.Button(
        main_frame,
        text="ЗАКЛЮЧЁН", 
        font=("Arial", 20, "bold"),
        bg="#8B0000", 
        fg="white",
        state="disabled",
        width=25,
        height=3,
        command=prison.destroy
    )
    exit_button.pack(pady=20)
    
    rickroll_label = tk.Label(
        prison,
        text=" На фоне играет рикролл (я вас зарикроллил хаа) ", 
        font=("Arial", 14), 
        fg="#00ff00", 
        bg='#000000'
    )
    rickroll_label.place(relx=0.5, rely=0.95, anchor='center')
    
    def update_prison():
        nonlocal current_sentence_time, start_time, amnesty_available
        elapsed = time.time() - start_time
        
        if is_life_sentence:
            timer_label.config(text=f" Пожизненное: {int(elapsed)} секунд")
            
            if elapsed < 10:
                remaining_amnesty = 10 - elapsed
                amnesty_warning_label.config(text=f"Помилование у бобика мурино будет доступна через: {int(remaining_amnesty)} сек")
            elif elapsed >= 10 and not amnesty_available:
                amnesty_available = True
                amnesty_button.config(state="normal", bg="#006400")
                amnesty_warning_label.config(text="🎉 ПОМИЛОВАНИЕ ДОСТУПНО! МОЖЕТЕ ПРОСИТЬ ПОМИЛОВАНИЯ! 🎉", fg="#00ff00")
            
            quote_index = int(elapsed) % len(quotes)
            quote_label.config(text=quotes[quote_index])
            
            if int(elapsed) % 2 == 0:
                colors = ["yellow", "red", "green", "cyan", "magenta", "orange"]
                timer_label.config(fg=colors[int(elapsed) % len(colors)])
            
            prison.after(1000, update_prison)
        else:
            remaining = max(0, current_sentence_time - elapsed)
            if elapsed < 30 and not amnesty_available:
                remaining_amnesty = 30 - elapsed
                amnesty_warning_label.config(
                    text=f"Помилование бобик будет доступна через: {int(remaining_amnesty)} секунд",
                    fg="#ffff00" if remaining_amnesty <= 5 else "#00ff48"
                )
            
            if elapsed >= 30 and not amnesty_available:
                amnesty_available = True
                amnesty_button.config(state="normal", bg="#006400")
            
            timer_label.config(text=f" Осталось: {int(remaining)} секунд")
            progress = (current_sentence_time - remaining) / current_sentence_time
            progress_bar.coords(progress_fill, 0, 0, 800 * progress, 30)
            
            quote_index = int(elapsed) % len(quotes)
            quote_label.config(text=quotes[quote_index])
            
            if int(elapsed) % 2 == 0:
                colors = ["yellow", "red", "green", "cyan", "magenta", "orange"]
                timer_label.config(fg=colors[int(elapsed) % len(colors)])
            
            if remaining <= 0:
                timer_label.config(text=" ВРЕМЯ ВЫШЛО! ВЫ СВОБОДНЫ!", fg="#00ff00")
                exit_button.config(state="normal", bg="#006400", text=" ВЫЙТИ НА СВОБОДУ!")
                escape_button.config(state="disabled")
                amnesty_button.config(state="disabled")
                notification.notify(
                    title="ВЫ СВОБОДНЫ!",
                    message="Вы вышли из тюрьмы!",
                    app_icon=None, 
                    timeout=4
                    
                )
                if is_life_sentence:
                    luck_button.config(state="disabled")
                quote_label.config(text="Надеюсь, этот урок запомнится надолго! Больше не вводите 1488!")
                rickroll_label.config(text="ИДИТЕ РИКРОЛЛ ВЫКЛЮЧИТЕ В БРАУЗЕРЕ")
            else:
                prison.after(1000, update_prison)
    
    if is_life_sentence:
        amnesty_warning_label.config(text="Амнистия будет доступна через: 10 сек", fg="#ffff00")
    
    update_prison()

def sharmanka():
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Кручу шарманку...", color="yellow") as sp:
        time.sleep(1.2)
        sp.ok("✅ ")
    
    if random.random() < 0.2:
        result = 1488
        chislo.config(text=str(result), fg="red")
        
        answer = messagebox.askyesno(
            "ВОПРОС ОТ ШАРМАНКИ", 
            "ВЫ ЧТО, СПЕЦИАЛЬНО ВЫЗВАЛИ 1488?\n\n"
            "ДА - если сделали это специально\n"
            "НЕТ - если это случайность"
        )
        
        if answer:
            EasterEggs.maybe_show()
            EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
            with yaspin(text="Передаю в тюрьму...", color="red") as sp:
                time.sleep(1.5)
                sp.ok("🔒 ")
            messagebox.showwarning("ОПАСНОСТЬ!", "ШАРМАНКА ПЕРЕДАЕТ ВАС В ТЮРЬМУ!")
            advanced_prison_1488(60)
        else:
            EasterEggs.maybe_show()
            EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
            with yaspin(text="Проверяю искренность...", color="green") as sp:
                time.sleep(1)
                sp.ok("✅ ")
            messagebox.showinfo("УДАЧА!", "На этот раз прощаем...")
    else:
        result = random.randint(1, 1000)
        chislo.config(text=str(result), fg="#2e8b57")

knopka = tk.Button(window, text="ЗАПУСТИТЬ ШАРМАНКУ", command=sharmanka, bg="green", fg="white")
knopka.pack(pady=10)

def open_second_window():
    global dz2_clicked
    dz2_clicked = True
    print(f"{Colors.GREEN}ДЗ2 Нажато: dz2_clicked={dz2_clicked}{Colors.RESET}")
    
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Открываю ДЗ 2...", color="red") as sp:
        time.sleep(1.5)
        sp.ok("🔓 ")
    
    check_secret_button()
    
    window2 = tk.Toplevel(window)
    window2.title("ДЗ 2 - РАДУЖН. ШАРМАНКА")
    window2.geometry("600x300")

    Rframe = tk.Frame(window2)
    Rframe.pack(pady=20)

    numbers = []
    for i in range(11):
        label = tk.Label(Rframe, text="", font=("Comic Sans MS", 20), width=3)
        label.pack(side=tk.LEFT, padx=5)
        numbers.append(label)

    def rainbow_sharmanka():
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Создаю радугу...", color="magenta") as sp:
            time.sleep(1.2)
            sp.ok("🌈 ")
        
        if random.random() < 0.05:
            for i in range(11):
                numbers[i].config(text="1488"[i % 4], fg="red")
            
            answer = messagebox.askyesno("ОПЯТЬ 1488??", "ОПЯТЬ 1488, УВАЖАЕМЫЙ??\n\nДА - если Вы это сделали намеренно\n""НЕТ - если это была случайность")
            
            
            if answer:
                EasterEggs.maybe_show()
                EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
                with yaspin(text="Подготавливаю пожизненное...", color="red") as sp:
                    time.sleep(2)
                    sp.ok("🔒 ")
                messagebox.showwarning("ПОЖИЗНЕННОЕ!", "ВЫ САМИ ВИНОВАТЫ! ПОЖИЗНЕННОЕ ЗАКЛЮЧЕНИЕ!")
                advanced_prison_1488(is_life_sentence=True)
            else:
                EasterEggs.maybe_show()
                EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
                with yaspin(text="Назначаю наказание...", color="orange") as sp:
                    time.sleep(1.5)
                    sp.ok("⏱️ ")
                messagebox.showwarning("НАКАЗАНИЕ!", "ВСЁ РАВНО В ТЮРЬМУ! 70 СЕКУНД!")
                advanced_prison_1488(70)
        elif random.random() < 0.2:
            for i in range(11):
                numbers[i].config(text="1488"[i % 4], fg="red")
            
            answer = messagebox.askyesno("ОПЯТЬ 1488?!","ВЫ СНОВА ВЫЗВАЛИ 1488! ЭТО СПЕЦИАЛЬНО?\n\nДА - если это был умысел\nНЕТ - если это случайность"
            )
            
            if answer:
                EasterEggs.maybe_show()
                EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
                with yaspin(text="Увеличиваю срок...", color="red") as sp:
                    time.sleep(1.5)
                    sp.ok("🔒 ")
                messagebox.showwarning("РЕЦИДИВ!", "ВТОРОЙ РАЗ ЗА 1488! В ТЮРЬМУ НАДОЛГО!")
                advanced_prison_1488(70)
            else:
                EasterEggs.maybe_show()
                EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
                with yaspin(text="Проверяю историю...", color="green") as sp:
                    time.sleep(1)
                    sp.ok("✅ ")
                messagebox.showinfo("ПРОЩАЕМ...", "Но будьте осторожнее с числами!")
        else:
            colors = ["red", "yellow", "green", "blue", "dark blue", "purple", "pink", "brown", "gray", "cyan", "magenta"]
            for i in range(11):
                number = random.randint(0, 9)
                numbers[i].config(text=str(number), fg=colors[i])

    rainbow_button = tk.Button(window2, text="ЗАПУСТИТЬ РАДУЖНУЮ ШАРМАНКУ", command=rainbow_sharmanka, bg="purple", fg="white")
    rainbow_button.pack(pady=10)

def open_third_window():
    global dz3_clicked
    dz3_clicked = True
    print(f"{Colors.GREEN}ДЗ3 Нажато: dz3_clicked={dz3_clicked}{Colors.RESET}")
    
    EasterEggs.maybe_show()
    EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
    with yaspin(text="Открываю ДЗ 3...", color="blue") as sp:
        time.sleep(1.5)
        sp.ok("🔓 ")
    
    check_secret_button()
    
    window3 = tk.Toplevel(window)
    window3.title("ДЗ 3 - ГЕНЕРАТОР НОМЕРОВ")
    window3.geometry("500x250")
    
    phone_label = tk.Label(window3, text="", font=("Arial", 24, "bold"), fg="#2e8b57")
    phone_label.pack(pady=30)
    
    def generate_phone():
        EasterEggs.maybe_show()
        EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
        with yaspin(text="Генерирую номер...", color="cyan") as sp:
            time.sleep(1)
            sp.ok("✅ ")
        
        if random.random() < 0.05:
            special_number = "+7 (906) 130-23-11"
            phone_label.config(text=special_number, fg="red")
            messagebox.showinfo(
                "СООБЩЕНИЕ ДЛЯ ДМИТРИЯ", 
                "Ой, вы случайно сгенерировали свой номер..."
            )
        else:
            region = ''.join([str(random.randint(0, 9)) for _ in range(3)])
            first_part = ''.join([str(random.randint(0, 9)) for _ in range(3)])
            second_part = ''.join([str(random.randint(0, 9)) for _ in range(2)])
            third_part = ''.join([str(random.randint(0, 9)) for _ in range(2)])
            phone_number = f"+7 ({region}) {first_part}-{second_part}-{third_part}"
            phone_label.config(text=phone_number, fg="#2e8b57")
    
    phone_button = tk.Button(window3, text="СГЕНЕРИРОВАТЬ НОМЕР", font=("Arial", 16, "bold"),bg="#1e90ff", fg="white",command=generate_phone)
    phone_button.pack(pady=10)
    
    def copy_phone():
        phone = phone_label.cget("text")
        if phone:
            EasterEggs.maybe_show()
            EasterEggs.maybe_show_notification()  # Добавлен вызов уведомления
            with yaspin(text="Копирую номер...", color="green") as sp:
                time.sleep(1)
                sp.ok("📋 ")
            window3.clipboard_clear()
            window3.clipboard_append(phone)
            messagebox.showinfo("СКОПИРОВАНО!", f"Номер {phone} скопирован в буфер (зачем вам скопированный номер?)!")
    
    copy_button = tk.Button(window3,text="КОПИРОВАТЬ НОМЕР",font=("Arial", 12),bg="#32cd32",fg="white", command=copy_phone)
    copy_button.pack(pady=5)

dz2 = tk.Button(window, text="ПЕРЕЙТИ К ДЗ 2☠️", command=open_second_window, bg="red", fg="white")
dz2.pack(pady=5)

dz3 = tk.Button(
    window, 
    text="ПЕРЕЙТИ К ДЗ 3", 
    command=open_third_window, 
    bg="#1e90ff", 
    fg="white"
)
dz3.pack(pady=5)

window.mainloop()

wait1 = yaspin(text="Ожидаю ответа...",color="cyan",spinner="arrow",side="right",on_color="on_red",attrs=["bold", "blink"],reversal=False) 
wait1.start()
time.sleep(1)
ask1 = messagebox.askquestion("ВНИМАНИЕ", "ВАМ ПОНРАВИЛОСЬ?")
if ask1 == "yes":
    wait1.stop()
    wait1.ok("✅")
    notification.notify(
        title="СПАСИБО!",
        message="СПАСИБО ЗА ВАШУ ОЦЕНКУ!",
        timeout=5,
        app_name="Дз Максима",
        toast=True
    )  
else:
    webbrowser.open_new_tab("https://docs.google.com/forms/d/e/1FAIpQLSedGEJScN33ESgAvnIbxNs-vDmb0PmIwpDxfT78wS8sJYjb_g/viewform?usp=dialog")
    wait1.stop()
    wait1.fail("❌")
    notification.notify(
        title="ЧТО!?",
        message="СЕЙЧАС ОТКРОЕТСЯ ССЫЛКА, ВОТ ТАМ И РАССКАЖЕТЕ ПОЧЕМУ НЕ ПОНРАВИЛОСЬ",
        timeout=5,
        app_name="Дз Максима",
        toast=True)
# ГООООООООООЛ!!!!!
