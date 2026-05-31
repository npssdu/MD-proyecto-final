import json
import os
import sys
import time
import traceback
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import HTML, Markdown, display


ROOT = Path(r"C:\Users\andru\Documents\2026-I (S10)\Mineria de Datos\Proyecto Final")
NOTEBOOK = ROOT / "entrega-final" / "MD_Proyecto_Final_Completo.ipynb"


def source_text(cell):
    src = cell.get("source", "")
    return "".join(src) if isinstance(src, list) else src


def main():
    os.chdir(NOTEBOOK.parent)
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    code_cells = [(i, source_text(c)) for i, c in enumerate(nb["cells"]) if c.get("cell_type") == "code"]

    shell = InteractiveShell.instance()
    shell.user_ns["display"] = display
    shell.user_ns["Markdown"] = Markdown
    shell.user_ns["HTML"] = HTML

    print(f"Notebook: {NOTEBOOK}")
    print(f"Working directory: {Path.cwd()}")
    print(f"Code cells: {len(code_cells)}")

    start = time.time()
    for n, (idx, code) in enumerate(code_cells, start=1):
        if not code.strip():
            continue
        # Notebook magics such as %matplotlib inline are valid in Jupyter/Colab.
        # This lightweight local runner uses Agg, so it skips those frontend-only lines.
        code = "\n".join(
            line for line in code.splitlines()
            if not line.lstrip().startswith("%matplotlib")
        )
        if not code.strip():
            continue
        preview = " ".join(code.strip().splitlines()[:2])[:180]
        print(f"[{n:03d}/{len(code_cells):03d}] cell {idx}: {preview}")
        result = shell.run_cell(code, store_history=False)
        plt.close("all")
        if result.error_before_exec is not None or result.error_in_exec is not None:
            err = result.error_before_exec or result.error_in_exec
            print("\nEXECUTION_FAILED")
            print(f"Cell index: {idx}")
            print(f"Preview: {preview}")
            traceback.print_exception(type(err), err, err.__traceback__)
            return 1

    elapsed = time.time() - start
    print(f"\nEXECUTION_OK in {elapsed:.1f} seconds")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
