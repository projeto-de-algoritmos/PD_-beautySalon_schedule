import tkinter as tk
from tkinter import messagebox


def weighted_interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])  # Ordena os intervalos pelo horário de término
    n = len(intervals)
    memo = [0] * (n + 1)

    for i in range(1, n + 1):
        value = intervals[i - 1][2]
        j = i - 1
        while j >= 1 and intervals[j - 1][1] > intervals[i - 1][0]:
            j -= 1
        value += memo[j]
        memo[i] = max(value, memo[i - 1])

    schedule = []
    i = n
    while i > 0:
        if intervals[i - 1][2] + memo[i - 1] >= memo[i]:
            schedule.append(intervals[i - 1])
            j = i - 1
            while j >= 1 and intervals[j - 1][1] > intervals[i - 1][0]:
                j -= 1
            i = j
        else:
            i -= 1
    schedule.reverse()

    return schedule


def handle_submit():
    num_intervals = int(entry_num_intervals.get())

    intervals = []
    for i in range(num_intervals):
        name = entry_names[i].get()
        description = entry_descriptions[i].get()
        start = int(entry_starts[i].get())
        end = int(entry_ends[i].get())
        value = int(entry_values[i].get())
        intervals.append((start, end, value, name, description))

    result = weighted_interval_scheduling(intervals)

    total_value = sum(interval[2] for interval in result)
    messagebox.showinfo("Agendamento", f"Valor total: {total_value}\n\n{format_result(result)}")


def format_result(result):
    formatted = "Agendamentos:\n"
    for interval in result:
        formatted += f"Nome: {interval[3]}, Descrição: {interval[4]}, Início: {interval[0]}, Término: {interval[1]}, Valor: {interval[2]}\n"
    return formatted


# Interface Gráfica
root = tk.Tk()
root.title("Beauty Salon Schedule")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=20)

label_num_intervals = tk.Label(frame, text="Número de agendamentos:")
label_num_intervals.pack()

entry_num_intervals = tk.Entry(frame)
entry_num_intervals.pack(pady=10)

frame_intervals = tk.Frame(root)
frame_intervals.pack()

entry_names = []
entry_descriptions = []
entry_starts = []
entry_ends = []
entry_values = []

def create_interval_fields():
    num_intervals = int(entry_num_intervals.get())

    for i in range(num_intervals):
        label_name = tk.Label(frame_intervals, text=f"Nome cliente {i+1}:")
        label_name.pack()

        entry_name = tk.Entry(frame_intervals)
        entry_name.pack()
        entry_names.append(entry_name)

        label_description = tk.Label(frame_intervals, text=f"Descrição {i+1}:")
        label_description.pack()

        entry_description = tk.Entry(frame_intervals)
        entry_description.pack()
        entry_descriptions.append(entry_description)

        label_start = tk.Label(frame_intervals, text=f"Início {i+1}:")
        label_start.pack()

        entry_start = tk.Entry(frame_intervals)
        entry_start.pack()
        entry_starts.append(entry_start)

        label_end = tk.Label(frame_intervals, text=f"Término {i+1}:")
        label_end.pack()

        entry_end = tk.Entry(frame_intervals)
        entry_end.pack()
        entry_ends.append(entry_end)

        label_value = tk.Label(frame_intervals, text=f"Valor {i+1}:")
        label_value.pack()

        entry_value = tk.Entry(frame_intervals)
        entry_value.pack()
        entry_values.append(entry_value)

    btn_submit = tk.Button(root, text="Agendar", command=handle_submit)
    btn_submit.pack(pady=10)

btn_create_fields = tk.Button(frame, text="Criar Campos", command=create_interval_fields)
btn_create_fields.pack()

root.mainloop()
