import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from app.export import export_png
from app.models import ExportConfig
from app.plotting import (
    build_frequency_inverse_wavelength,
    build_linear_plot,
    build_velocity_sqrt_tension,
    build_wavelength_inverse_harmonic,
)


GRAPH_TYPES = {
    "Frequência em função do inverso do comprimento de onda": "frequency_inverse_wavelength",
    "Comprimento de onda em função do inverso do número harmônico": "wavelength_inverse_harmonic",
    "Velocidade em função da raiz quadrada da tensão": "velocity_sqrt_tension",
}

GRAPH_COLUMNS = {
    "frequency_inverse_wavelength": (
        ("n", "n"),
        ("Frequência (Hz)", "frequency_hz"),
        ("Comprimento de onda (m)", "lambda_m"),
        ("Incerteza do comprimento (m)", "delta_lambda_m"),
        ("Incerteza da frequência (Hz)", "delta_frequency_hz"),
    ),
    "wavelength_inverse_harmonic": (
        ("n", "harmonic_n"),
        ("Comprimento de onda (m)", "lambda_m"),
        ("Incerteza do comprimento (m)", "delta_lambda_m"),
    ),
    "velocity_sqrt_tension": (
        ("Massa (kg)", "mass_kg"),
        ("Frequência (Hz)", "frequency_hz"),
        ("Comprimento de onda (m)", "lambda_m"),
        ("Incerteza da massa (kg)", "delta_mass_kg"),
        ("Incerteza da frequência (Hz)", "delta_frequency_hz"),
        ("Incerteza do comprimento (m)", "delta_lambda_m"),
    ),
}

DEFAULT_ROWS = {
    "frequency_inverse_wavelength": [
        {"n": "1", "frequency_hz": "10", "lambda_m": "0.5", "delta_lambda_m": "0.01", "delta_frequency_hz": "0.1"},
        {"n": "2", "frequency_hz": "20", "lambda_m": "0.25", "delta_lambda_m": "0.01", "delta_frequency_hz": "0.1"},
        {"n": "3", "frequency_hz": "30", "lambda_m": "0.167", "delta_lambda_m": "0.01", "delta_frequency_hz": "0.1"},
    ],
    "wavelength_inverse_harmonic": [
        {"harmonic_n": "1", "lambda_m": "1.2", "delta_lambda_m": "0.02"},
        {"harmonic_n": "2", "lambda_m": "0.6", "delta_lambda_m": "0.02"},
        {"harmonic_n": "4", "lambda_m": "0.3", "delta_lambda_m": "0.02"},
    ],
    "velocity_sqrt_tension": [
        {"mass_kg": "0.1", "frequency_hz": "10", "lambda_m": "0.5", "delta_mass_kg": "0.01", "delta_frequency_hz": "0.1", "delta_lambda_m": "0.01"},
        {"mass_kg": "0.2", "frequency_hz": "14", "lambda_m": "0.5", "delta_mass_kg": "0.01", "delta_frequency_hz": "0.1", "delta_lambda_m": "0.01"},
        {"mass_kg": "0.4", "frequency_hz": "20", "lambda_m": "0.5", "delta_mass_kg": "0.01", "delta_frequency_hz": "0.1", "delta_lambda_m": "0.01"},
    ],
}


class MainWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Helper Fisica")
        self.root.geometry("1200x760")
        self.root.minsize(960, 640)

        self.graph_type = tk.StringVar(value=next(iter(GRAPH_TYPES)))
        self.width_var = tk.StringVar(value="1600")
        self.height_var = tk.StringVar(value="1000")
        self.dpi_var = tk.StringVar(value="300")
        self.status_var = tk.StringVar(value="Preencha os dados e gere um grafico.")
        self.rows: list[dict[str, ttk.Entry]] = []
        self.current_figure = None
        self.current_config: ExportConfig | None = None

        self._build_layout()
        self._refresh_table()

    def _build_layout(self) -> None:
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        controls = ttk.Frame(self.root, padding=16)
        controls.grid(row=0, column=0, sticky="nsew")
        controls.columnconfigure(0, weight=1)
        controls.rowconfigure(3, weight=1)

        preview = ttk.Frame(self.root, padding=(0, 16, 16, 16))
        preview.grid(row=0, column=1, sticky="nsew")
        preview.columnconfigure(0, weight=1)
        preview.rowconfigure(1, weight=1)

        ttk.Label(controls, text="Experimento", font=("Segoe UI", 11, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 4)
        )
        experiment = ttk.Combobox(
            controls,
            values=["Movimento ondulatório: onda na corda"],
            state="readonly",
        )
        experiment.set("Movimento ondulatório: onda na corda")
        experiment.grid(row=1, column=0, sticky="ew", pady=(0, 14))

        ttk.Label(controls, text="Tipo de gráfico", font=("Segoe UI", 11, "bold")).grid(
            row=2, column=0, sticky="w", pady=(0, 4)
        )
        graph_selector = ttk.Combobox(
            controls,
            textvariable=self.graph_type,
            values=list(GRAPH_TYPES),
            state="readonly",
        )
        graph_selector.grid(row=3, column=0, sticky="new", pady=(0, 14))
        graph_selector.bind("<<ComboboxSelected>>", lambda _event: self._refresh_table())

        table_section = ttk.LabelFrame(controls, text="Dados experimentais", padding=8)
        table_section.grid(row=4, column=0, sticky="nsew", pady=(0, 12))
        table_section.columnconfigure(0, weight=1)
        table_section.rowconfigure(1, weight=1)
        self.table_frame = ttk.Frame(table_section)
        self.table_frame.grid(row=0, column=0, sticky="nsew")
        table_buttons = ttk.Frame(table_section)
        table_buttons.grid(row=1, column=0, sticky="w", pady=(8, 0))
        ttk.Button(table_buttons, text="Adicionar linha", command=self._add_row).grid(row=0, column=0, padx=(0, 6))
        ttk.Button(table_buttons, text="Remover linha", command=self._remove_row).grid(row=0, column=1)

        export_section = ttk.LabelFrame(controls, text="Exportação PNG", padding=8)
        export_section.grid(row=5, column=0, sticky="ew", pady=(0, 12))
        for column in range(3):
            export_section.columnconfigure(column, weight=1)
        for column, (label, variable) in enumerate(
            (("Largura (px)", self.width_var), ("Altura (px)", self.height_var), ("DPI", self.dpi_var))
        ):
            ttk.Label(export_section, text=label).grid(row=0, column=column, sticky="w")
            ttk.Entry(export_section, textvariable=variable, width=10).grid(row=1, column=column, sticky="ew", padx=(0, 5))

        actions = ttk.Frame(controls)
        actions.grid(row=6, column=0, sticky="ew")
        actions.columnconfigure(0, weight=1)
        actions.columnconfigure(1, weight=1)
        ttk.Button(actions, text="Gerar grafico", command=self._generate).grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.export_button = ttk.Button(actions, text="Exportar PNG", command=self._export, state="disabled")
        self.export_button.grid(row=0, column=1, sticky="ew", padx=(5, 0))
        ttk.Label(controls, textvariable=self.status_var, wraplength=320).grid(row=7, column=0, sticky="w", pady=(10, 0))

        ttk.Label(preview, text="Visualização", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 8))
        self.preview_frame = ttk.Frame(preview, relief="sunken", borderwidth=1)
        self.preview_frame.grid(row=1, column=0, sticky="nsew")
        self.preview_frame.columnconfigure(0, weight=1)
        self.preview_frame.rowconfigure(0, weight=1)
        ttk.Label(self.preview_frame, text="O gráfico aparecerá aqui.").grid(row=0, column=0)

    def _refresh_table(self) -> None:
        for child in self.table_frame.winfo_children():
            child.destroy()
        self.rows.clear()
        graph_key = GRAPH_TYPES[self.graph_type.get()]
        columns = GRAPH_COLUMNS[graph_key]
        for column, (label, _key) in enumerate(columns):
            ttk.Label(self.table_frame, text=label).grid(row=0, column=column, padx=3, pady=(0, 4), sticky="w")
        for row_index, values in enumerate(DEFAULT_ROWS[graph_key], start=1):
            self._create_row(row_index, values, columns)

    def _create_row(self, row_index: int, values: dict[str, str], columns: tuple[tuple[str, str], ...]) -> None:
        row: dict[str, ttk.Entry] = {}
        for column, (_label, key) in enumerate(columns):
            entry = ttk.Entry(self.table_frame, width=11)
            entry.insert(0, values.get(key, ""))
            entry.grid(row=row_index, column=column, padx=3, pady=2, sticky="ew")
            row[key] = entry
        self.rows.append(row)

    def _add_row(self) -> None:
        graph_key = GRAPH_TYPES[self.graph_type.get()]
        columns = GRAPH_COLUMNS[graph_key]
        self._create_row(len(self.rows) + 1, {}, columns)

    def _remove_row(self) -> None:
        if not self.rows:
            return
        row = self.rows.pop()
        for entry in row.values():
            entry.destroy()

    def _read_number(self, entry: ttk.Entry, label: str, optional: bool = False) -> float | None:
        value = entry.get().strip()
        if optional and not value:
            return None
        return float(value)

    def _collect_arrays(self, keys: tuple[str, ...]) -> dict[str, np.ndarray | None]:
        result: dict[str, np.ndarray | None] = {}
        for key in keys:
            optional = key.startswith("delta_")
            values = [self._read_number(row[key], key, optional) for row in self.rows]
            if optional and all(value is None for value in values):
                result[key] = None
            elif any(value is None for value in values):
                raise ValueError(f"Preencha todos os valores de {key} ou deixe a coluna vazia.")
            else:
                result[key] = np.array(values, dtype=float)
        return result

    def _export_config(self) -> ExportConfig:
        return ExportConfig(
            width_px=int(self.width_var.get()),
            height_px=int(self.height_var.get()),
            dpi=int(self.dpi_var.get()),
        )

    def _generate(self) -> None:
        try:
            graph_key = GRAPH_TYPES[self.graph_type.get()]
            if graph_key == "frequency_inverse_wavelength":
                data = self._collect_arrays(("frequency_hz", "lambda_m", "delta_lambda_m", "delta_frequency_hz"))
                plot_data, fit_result, fit_label, parameter_text = build_frequency_inverse_wavelength(**data)
            elif graph_key == "wavelength_inverse_harmonic":
                data = self._collect_arrays(("harmonic_n", "lambda_m", "delta_lambda_m"))
                data["length_m"] = 0.6
                result = build_wavelength_inverse_harmonic(**data)
                plot_data, fit_result, fit_label, parameter_text = result.plot_data, result.fit_result, result.fit_label, result.parameter_text
            else:
                data = self._collect_arrays(("mass_kg", "frequency_hz", "lambda_m", "delta_mass_kg", "delta_frequency_hz", "delta_lambda_m"))
                result = build_velocity_sqrt_tension(**data)
                plot_data, fit_result, fit_label, parameter_text = result.plot_data, result.fit_result, result.fit_label, result.parameter_text
            config = self._export_config()
            figure = build_linear_plot(plot_data, fit_result, fit_label, parameter_text, config)
            self._show_figure(figure)
            self.current_figure = figure
            self.current_config = config
            self.export_button.configure(state="normal")
            self.status_var.set("Gráfico gerado. Você pode revisar a visualização ou exportar o PNG.")
        except (ValueError, TypeError) as error:
            messagebox.showerror("Nao foi possivel gerar o grafico", str(error), parent=self.root)

    def _show_figure(self, figure) -> None:
        for child in self.preview_frame.winfo_children():
            child.destroy()
        canvas = FigureCanvasTkAgg(figure, master=self.preview_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def _export(self) -> None:
        if self.current_figure is None or self.current_config is None:
            return
        path = filedialog.asksaveasfilename(
            parent=self.root,
            title="Exportar grafico PNG",
            defaultextension=".png",
            filetypes=[("Imagem PNG", "*.png")],
        )
        if not path:
            return
        output = export_png(self.current_figure, Path(path), self.current_config)
        self.status_var.set(f"PNG salvo em {output}")


def create_app(root: tk.Tk) -> MainWindow:
    return MainWindow(root)
